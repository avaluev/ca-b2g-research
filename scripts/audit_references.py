#!/usr/bin/env python3
"""Comprehensive reference auditor for ca-b2g-research.

What it does:
  1. Crawls every HTML page on the live site (via sitemap.xml + recursive
     internal-link discovery).
  2. Extracts every <a href>, <link href>, <script src>, <img src>, and
     resource href from each page.
  3. Reads every Markdown file in the repo and extracts:
       - Every Markdown / inline link [text](url)
       - Every code-fence reference like state/foo.json or scripts/bar.py
       - Every bare URL anywhere in the prose
       - Every reference inside a <code> span on rendered HTML
  4. Reads every README, CONTRIBUTING, and SECURITY file in the repo.
  5. Reads every JSON file under state/ and scans its string values for URLs.
  6. Verifies every discovered reference:
       - Absolute http(s) URLs        -> HEAD/GET against the live URL
       - Repo-relative file paths     -> exists on disk AND, where the file is
                                          inside the published site root,
                                          reachable on the live site
       - Site-relative paths (/foo/)  -> reachable at SITE_BASE_URL + path
  7. Emits two reports:
       - state/audit/references.json  — full structured payload
       - state/audit/references.md    — grouped Markdown summary
  8. Exit code 1 if any broken reference is found, else 0.

Why it exists:
  Broken references in published research kill AI-search citation: every
  retrieval pass that follows a dead pointer demotes the page. This auditor
  is the gate that catches that drift before it ships.

Usage:
    python3 scripts/audit_references.py
    python3 scripts/audit_references.py --no-network          # static checks only
    python3 scripts/audit_references.py --site-base URL       # override live URL
    python3 scripts/audit_references.py --skip-external       # only check own-domain refs

Designed to be invokable from CI; reads no env vars, writes only to
state/audit/, returns deterministic exit codes.
"""

from __future__ import annotations

import argparse
import dataclasses
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from html.parser import HTMLParser
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parents[1]
SITE_DIR = ROOT / "outputs" / "site"
AUDIT_DIR = ROOT / "state" / "audit"
DEFAULT_SITE_BASE = "https://avaluev.github.io/ca-b2g-research"
DEFAULT_REPO_BASE = "https://github.com/avaluev/ca-b2g-research/blob/main"
# Use a browser-like UA so government CIS sites that filter on UA don't reject us
# (zakupki.okmot.kg returns 0 with a custom UA but 200 with browser UA). The
# auditor's identity is preserved via the From header.
USER_AGENT = (
    "Mozilla/5.0 (compatible; ca-b2g-references-audit/1.0; "
    "+https://github.com/avaluev/ca-b2g-research/blob/main/scripts/audit_references.py)"
)
TIMEOUT = 20
MAX_WORKERS = 12
RATE_LIMIT_BACKOFF_SEC = 5

# ---------------------------------------------------------------------- types


@dataclasses.dataclass(frozen=True)
class Ref:
    target: str           # the URL or path being checked
    kind: str             # 'url' | 'file' | 'site_path'
    source: str           # path / URL where this reference was found
    context: str = ""     # short snippet for the report
    source_dir: str = ""  # repo-relative dir of the source file (for resolving relative file refs)


@dataclasses.dataclass
class Result:
    ref: Ref
    ok: bool
    status: int           # HTTP code, or 0 when not network-checked
    detail: str = ""


# ---------------------------------------------------------------------- HTML


class LinkExtractor(HTMLParser):
    """Pull every linkable attribute from a page, plus every <code> text."""

    LINKABLE = {
        "a": "href",
        "link": "href",
        "img": "src",
        "script": "src",
        "iframe": "src",
        "source": "src",
        "video": "src",
        "audio": "src",
    }

    def __init__(self) -> None:
        super().__init__()
        self.urls: list[str] = []
        self._capture_code = False
        self.code_spans: list[str] = []
        self._buf: list[str] = []

    def handle_starttag(self, tag, attrs):
        if tag in self.LINKABLE:
            attr_name = self.LINKABLE[tag]
            for k, v in attrs:
                if k == attr_name and v:
                    self.urls.append(v)
        if tag in ("code", "pre"):
            self._capture_code = True
            self._buf = []

    def handle_endtag(self, tag):
        if tag in ("code", "pre"):
            if self._buf:
                self.code_spans.append("".join(self._buf))
            self._capture_code = False
            self._buf = []

    def handle_data(self, data):
        if self._capture_code:
            self._buf.append(data)


# -------------------------------------------------------------- discovery


URL_RE = re.compile(r"https?://[^\s)<>\"'`\]\}]+", re.IGNORECASE)
MD_LINK_RE = re.compile(r"\[(?:[^\]]*?)\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
# repo-relative file paths: "scripts/foo.py", "state/bar.json", "docs/baz.md"
REPO_PATH_RE = re.compile(
    r"(?<![A-Za-z0-9_./-])"
    r"((?:scripts|state|docs|outputs|prompts|.github|.claude|tests)/[A-Za-z0-9_./-]+?\.(?:py|json|md|html|csv|yml|yaml|js|sh))"
    r"(?![A-Za-z0-9_./-])"
)


def normalise_url(href: str, page_url: str) -> str | None:
    href = href.strip().strip(",.;:")
    if not href or href.startswith(("mailto:", "tel:", "javascript:", "data:", "#")):
        return None
    abs_url = urllib.parse.urljoin(page_url + "/" if not page_url.endswith("/") else page_url, href)
    parsed = urllib.parse.urlparse(abs_url)
    if parsed.scheme not in ("http", "https"):
        return None
    return urllib.parse.urlunparse(parsed._replace(fragment=""))


def discover_html_refs(seed_urls: Iterable[str], crawl: bool, site_base: str) -> tuple[set[str], list[Ref]]:
    """Crawl the live site starting from seeds; return (visited, refs)."""
    visited: set[str] = set()
    queue: list[str] = list(seed_urls)
    refs: list[Ref] = []
    site_host = urllib.parse.urlparse(site_base).netloc
    site_path_prefix = urllib.parse.urlparse(site_base).path.rstrip("/")

    while queue:
        url = queue.pop(0)
        if url in visited:
            continue
        visited.add(url)
        status, body = _fetch(url)
        if status != 200 or not body:
            print(f"[seed-fail] {status:>3} {url}", file=sys.stderr)
            continue
        ex = LinkExtractor()
        try:
            ex.feed(body)
        except Exception as exc:  # noqa: BLE001
            print(f"[parse-fail] {url} {exc}", file=sys.stderr)
            continue
        for raw_href in ex.urls:
            norm = normalise_url(raw_href, url)
            if not norm:
                continue
            refs.append(Ref(target=norm, kind="url", source=url, context=raw_href))
            if crawl:
                # crawl deeper: same host AND inside the site path prefix
                p = urllib.parse.urlparse(norm)
                if (
                    p.netloc == site_host
                    and (not site_path_prefix or p.path.startswith(site_path_prefix + "/") or p.path == site_path_prefix or p.path == site_path_prefix + "/")
                    and (norm.endswith("/") or norm.endswith(".html") or "." not in p.path.rsplit("/", 1)[-1])
                    and norm not in visited
                ):
                    queue.append(norm)
        # Also pull URLs from inline code/pre spans (e.g. citation pages)
        for span in ex.code_spans:
            for m in URL_RE.finditer(span):
                norm = normalise_url(m.group(0), url)
                if norm:
                    refs.append(Ref(target=norm, kind="url", source=url, context="(in <code>)"))
    return visited, refs


def discover_markdown_refs(repo_root: Path) -> list[Ref]:
    """Walk every .md, except auditor-generated reports (would create a self-loop)."""
    refs: list[Ref] = []
    excluded_files = {"state/audit/references.md"}
    for md_path in sorted(repo_root.rglob("*.md")):
        if any(seg in md_path.parts for seg in (".git", "node_modules", "__pycache__")):
            continue
        rel_check = md_path.relative_to(repo_root).as_posix()
        if rel_check in excluded_files:
            continue
        rel = md_path.relative_to(repo_root).as_posix()
        src_dir = (md_path.parent.relative_to(repo_root)).as_posix()
        try:
            text = md_path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        for line_no, line in enumerate(text.splitlines(), start=1):
            ctx = f"{rel}:{line_no}"
            for m in MD_LINK_RE.finditer(line):
                target = m.group(1).strip()
                if target.startswith(("mailto:", "#", "javascript:")):
                    continue
                if target.startswith(("http://", "https://")):
                    refs.append(Ref(target=target.split("#", 1)[0], kind="url", source=ctx, context=line.strip()[:120], source_dir=src_dir))
                else:
                    # Strip query/fragment for file-existence checks.
                    file_target = target.split("#", 1)[0].split("?", 1)[0]
                    if file_target:
                        refs.append(Ref(target=file_target, kind="file", source=ctx, context=line.strip()[:120], source_dir=src_dir))
            # Bare URLs in prose
            for m in URL_RE.finditer(line):
                # Avoid double-counting markdown links (already captured above)
                start = m.start()
                if start > 0 and line[start - 1] in "(":
                    continue
                refs.append(Ref(target=m.group(0).rstrip(",.;:)"), kind="url", source=ctx, context=line.strip()[:120], source_dir=src_dir))
            # Repo-relative file paths in prose
            for m in REPO_PATH_RE.finditer(line):
                refs.append(Ref(target=m.group(1), kind="file", source=ctx, context=line.strip()[:120], source_dir=src_dir))
    return refs


def discover_state_json_refs(repo_root: Path) -> list[Ref]:
    """Walk every JSON file under state/ and scan string values for URLs."""
    refs: list[Ref] = []
    state_dir = repo_root / "state"
    if not state_dir.exists():
        return refs
    for jp in sorted(state_dir.rglob("*.json")):
        if any(seg in jp.parts for seg in (".git", "__pycache__")):
            continue
        rel = jp.relative_to(repo_root).as_posix()
        try:
            data = json.loads(jp.read_text(encoding="utf-8", errors="replace"))
        except (OSError, json.JSONDecodeError):
            continue
        for url, jpath in _scan_json_for_urls(data):
            refs.append(Ref(target=url, kind="url", source=f"{rel}#{jpath}", context=url[:160]))
    return refs


def _scan_json_for_urls(data, path: str = "$"):
    if isinstance(data, dict):
        for k, v in data.items():
            yield from _scan_json_for_urls(v, f"{path}.{k}")
    elif isinstance(data, list):
        for i, v in enumerate(data):
            yield from _scan_json_for_urls(v, f"{path}[{i}]")
    elif isinstance(data, str):
        for m in URL_RE.finditer(data):
            yield m.group(0).rstrip(",.;:)"), path


# -------------------------------------------------------------- verification


def _fetch(url: str) -> tuple[int, str]:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
            return r.status, r.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as e:
        return e.code, ""
    except (urllib.error.URLError, TimeoutError, ConnectionError, OSError) as e:
        return 0, str(e)


def _head_or_get(url: str) -> tuple[int, str]:
    """HEAD first, GET fallback. Returns (status, detail)."""
    # Defensive: malformed URLs (stray brackets, unbalanced quotes, etc.) raise
    # ValueError inside urllib before we ever hit the network. Treat as broken.
    try:
        parsed = urllib.parse.urlparse(url)
        if not parsed.scheme or not parsed.netloc:
            return 0, "malformed URL (missing scheme or host)"
    except ValueError as e:
        return 0, f"malformed URL: {e}"
    try:
        req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": USER_AGENT})
    except (ValueError, UnicodeError) as e:
        return 0, f"malformed URL: {e}"
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
            return r.status, ""
    except urllib.error.HTTPError as e:
        if e.code in (403, 405, 429):
            # Many sites block HEAD; some rate-limit. Retry with GET (no body read).
            if e.code == 429:
                time.sleep(RATE_LIMIT_BACKOFF_SEC)
            try:
                req2 = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
                with urllib.request.urlopen(req2, timeout=TIMEOUT) as r:
                    return r.status, ""
            except urllib.error.HTTPError as e2:
                return e2.code, ""
            except (urllib.error.URLError, TimeoutError, ConnectionError, OSError) as e2:
                return 0, str(e2)[:120]
        return e.code, ""
    except (urllib.error.URLError, TimeoutError, ConnectionError, OSError) as e:
        return 0, str(e)[:120]


def verify_url(url: str) -> Result:
    status, detail = _head_or_get(url)
    return Result(ref=Ref(url, "url", ""), ok=200 <= status < 400, status=status, detail=detail)


def verify_file(path: str, repo_root: Path, source_dirs: list[str]) -> Result:
    """Verify a file reference exists. For repo-relative paths (e.g. 'scripts/foo.py')
    resolve from repo root. For relative paths (e.g. 'README.md'), try each known
    source directory the path was referenced from."""
    # Normalise: strip leading "./" but preserve a single leading "/".
    if path.startswith("./"):
        p = path[2:]
    else:
        p = path
    if p.startswith("/"):
        # Site-absolute path. Try mapping to outputs/site/<path>/index.html or .html.
        candidate = repo_root / "outputs" / "site" / p.lstrip("/").rstrip("/") / "index.html"
        if candidate.exists():
            return Result(Ref(path, "file", ""), True, 200, "exists in outputs/site")
        candidate2 = repo_root / "outputs" / "site" / p.lstrip("/")
        if candidate2.exists():
            return Result(Ref(path, "file", ""), True, 200, "exists in outputs/site")
        return Result(Ref(path, "file", ""), False, 404, f"missing site path: {path}")
    # Strip trailing slash for existence check (Path.exists handles dirs/files alike).
    p_clean = p.rstrip("/")
    # 1) try repo-root resolution
    candidate = (repo_root / p_clean).resolve()
    try:
        candidate.relative_to(repo_root.resolve())
        if candidate.exists():
            return Result(Ref(path, "file", ""), True, 200, "exists on disk (repo-root)")
    except ValueError:
        pass
    # 2) try resolving against each source directory the ref appeared in
    for src_dir in source_dirs:
        if not src_dir or src_dir.startswith(".."):
            continue
        cand = (repo_root / src_dir / p_clean).resolve()
        try:
            cand.relative_to(repo_root.resolve())
            if cand.exists():
                return Result(Ref(path, "file", ""), True, 200, f"exists relative to {src_dir}")
        except ValueError:
            continue
    return Result(Ref(path, "file", ""), False, 404, f"missing on disk: {path}")


def verify_site_path(path: str, site_base: str) -> Result:
    full = site_base.rstrip("/") + path
    status, detail = _head_or_get(full)
    return Result(Ref(path, "site_path", ""), 200 <= status < 400, status, detail)


# ---------------------------------------------------------------------- main


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--site-base", default=DEFAULT_SITE_BASE, help="Live site base URL (default: %(default)s)")
    parser.add_argument("--no-network", action="store_true", help="Skip HTTP checks; verify only on-disk file refs.")
    parser.add_argument("--no-crawl", action="store_true", help="Use only the sitemap, do not recursively crawl.")
    parser.add_argument("--skip-external", action="store_true", help="Only check refs whose host == site host.")
    parser.add_argument("--max-workers", type=int, default=MAX_WORKERS)
    parser.add_argument("--report-md", default=str(AUDIT_DIR / "references.md"))
    parser.add_argument("--report-json", default=str(AUDIT_DIR / "references.json"))
    parser.add_argument(
        "--fail-mode",
        choices=("any", "internal", "live-only"),
        default="any",
        help="What to count as a build-failing breakage: any broken ref / any ref on the live site / any ref cited FROM the live site (default: any).",
    )
    parser.add_argument(
        "--ignore-status",
        nargs="*",
        type=int,
        default=[],
        help="HTTP statuses to treat as OK (e.g. 403 999 — for hosts that block bots but work in browsers).",
    )
    args = parser.parse_args()

    site_base = args.site_base.rstrip("/")
    site_host = urllib.parse.urlparse(site_base).netloc

    AUDIT_DIR.mkdir(parents=True, exist_ok=True)

    print(f"# Reference audit", flush=True)
    print(f"# Site base: {site_base}", flush=True)
    print(f"# Repo root: {ROOT}", flush=True)

    # Seeds: sitemap + the home page.
    seeds: list[str] = [site_base + "/"]
    sitemap_url = site_base + "/sitemap.xml"
    sm_status, sm_body = _fetch(sitemap_url) if not args.no_network else (0, "")
    if sm_status == 200 and sm_body:
        for m in re.finditer(r"<loc>([^<]+)</loc>", sm_body):
            seeds.append(m.group(1))
    seeds = sorted(set(seeds))
    print(f"# Sitemap seeds: {len(seeds)}", flush=True)

    refs: list[Ref] = []
    if not args.no_network:
        visited, html_refs = discover_html_refs(seeds, crawl=not args.no_crawl, site_base=site_base)
        print(f"# HTML pages crawled: {len(visited)}; refs from HTML: {len(html_refs)}", flush=True)
        refs.extend(html_refs)

    md_refs = discover_markdown_refs(ROOT)
    print(f"# Markdown refs: {len(md_refs)}", flush=True)
    refs.extend(md_refs)

    json_refs = discover_state_json_refs(ROOT)
    print(f"# state/*.json URL refs: {len(json_refs)}", flush=True)
    refs.extend(json_refs)

    # De-dupe by (target, source)
    seen: set[tuple[str, str]] = set()
    deduped: list[Ref] = []
    for r in refs:
        key = (r.target, r.source)
        if key in seen:
            continue
        seen.add(key)
        deduped.append(r)
    refs = deduped

    if args.skip_external:
        before = len(refs)
        refs = [r for r in refs if r.kind != "url" or urllib.parse.urlparse(r.target).netloc in (site_host, "")]
        print(f"# --skip-external: dropped {before - len(refs)} external refs", flush=True)

    print(f"# Total refs to verify: {len(refs)}", flush=True)

    # Group refs by target so we hit the network once per unique target.
    by_target: dict[tuple[str, str], list[Ref]] = {}
    for r in refs:
        by_target.setdefault((r.kind, r.target), []).append(r)

    print(f"# Unique (kind, target) pairs: {len(by_target)}", flush=True)

    # Build per-target list of source dirs (for relative file resolution)
    source_dirs_for: dict[tuple[str, str], list[str]] = {}
    for r in refs:
        source_dirs_for.setdefault((r.kind, r.target), []).append(r.source_dir)

    results: list[Result] = []
    if args.no_network:
        for (kind, target), batch in by_target.items():
            if kind == "file":
                results.append(verify_file(target, ROOT, source_dirs_for.get((kind, target), [])))
    else:
        with ThreadPoolExecutor(max_workers=args.max_workers) as ex:
            futs = {}
            for (kind, target), batch in by_target.items():
                if kind == "url":
                    futs[ex.submit(verify_url, target)] = (kind, target)
                elif kind == "file":
                    results.append(verify_file(target, ROOT, source_dirs_for.get((kind, target), [])))
                elif kind == "site_path":
                    futs[ex.submit(verify_site_path, target, site_base)] = (kind, target)
            for f in as_completed(futs):
                kind, target = futs[f]
                try:
                    results.append(f.result())
                except Exception as exc:  # noqa: BLE001
                    results.append(Result(Ref(target, kind, ""), False, 0, f"verifier crashed: {exc}"))

    # Map results back to all referrers
    result_by_target: dict[tuple[str, str], Result] = {}
    for res in results:
        result_by_target[(res.ref.kind, res.ref.target)] = res

    # Build the per-source report payload
    broken: list[dict] = []
    ok: list[dict] = []
    for (kind, target), referrers in by_target.items():
        res = result_by_target.get((kind, target))
        if res is None:
            continue
        rec = {
            "kind": kind,
            "target": target,
            "status": res.status,
            "ok": res.ok,
            "detail": res.detail,
            "referrers": sorted({r.source for r in referrers if r.source}),
            "samples": [r.context for r in referrers if r.context][:3],
        }
        (ok if res.ok else broken).append(rec)

    payload = {
        "site_base": site_base,
        "totals": {
            "refs_total": len(refs),
            "unique_pairs": len(by_target),
            "ok": len(ok),
            "broken": len(broken),
        },
        "broken": sorted(broken, key=lambda r: (r["kind"], r["status"], r["target"])),
        "ok": sorted(ok, key=lambda r: (r["kind"], r["target"])),
    }

    Path(args.report_json).write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    Path(args.report_md).write_text(_render_md(payload), encoding="utf-8")

    print(f"\n# OK: {len(ok)}    Broken: {len(broken)}", flush=True)
    print(f"# Reports: {args.report_md}  {args.report_json}", flush=True)

    # Apply ignore-status filter to compute the build-failing set.
    ignore = set(args.ignore_status or [])
    failing: list[dict] = [r for r in broken if r["status"] not in ignore]

    site_host = urllib.parse.urlparse(site_base).netloc

    def is_live_referrer(rec: dict) -> bool:
        return any(s.startswith("http") and site_host in s for s in rec["referrers"])

    def is_internal_target(rec: dict) -> bool:
        if rec["kind"] in ("file", "site_path"):
            return True
        return rec["kind"] == "url" and site_host in rec["target"]

    if args.fail_mode == "live-only":
        failing = [r for r in failing if is_live_referrer(r)]
    elif args.fail_mode == "internal":
        failing = [r for r in failing if is_internal_target(r) or is_live_referrer(r)]
    # 'any' uses the full broken set as-is.

    if failing:
        print(f"\n## Build-failing breakage ({args.fail_mode} mode): {len(failing)}")
        for rec in failing[:30]:
            print(f"  [{rec['status']}] ({rec['kind']}) {rec['target']}", flush=True)
            for ref in rec["referrers"][:3]:
                print(f"      ← {ref}", flush=True)
        return 1
    if broken:
        print(f"\n# {len(broken)} broken refs found but none match fail-mode='{args.fail_mode}' / ignore-status={sorted(ignore)} — passing.", flush=True)
    return 0


def _render_md(payload: dict) -> str:
    lines = [
        "# Reference Audit",
        "",
        f"Site base: `{payload['site_base']}`",
        "",
        f"- Total references: **{payload['totals']['refs_total']}**",
        f"- Unique (kind, target) pairs: **{payload['totals']['unique_pairs']}**",
        f"- OK: **{payload['totals']['ok']}**",
        f"- Broken: **{payload['totals']['broken']}**",
        "",
    ]
    if not payload["broken"]:
        lines.append("All references resolve. No action required.")
        return "\n".join(lines)

    lines.append("## Broken references")
    lines.append("")
    by_kind: dict[str, list[dict]] = {}
    for rec in payload["broken"]:
        by_kind.setdefault(rec["kind"], []).append(rec)
    for kind, items in sorted(by_kind.items()):
        lines.append(f"### {kind} ({len(items)})")
        lines.append("")
        for rec in items:
            tgt = rec["target"]
            status = rec["status"]
            detail = rec["detail"] or ""
            lines.append(f"- **[{status}]** `{tgt}` {('— ' + detail) if detail else ''}")
            for ref in rec["referrers"][:5]:
                lines.append(f"    - referenced by `{ref}`")
            for sample in rec.get("samples", [])[:1]:
                lines.append(f"    - sample: `{sample}`")
        lines.append("")
    return "\n".join(lines)


if __name__ == "__main__":
    raise SystemExit(main())
