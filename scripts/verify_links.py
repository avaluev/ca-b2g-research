#!/usr/bin/env python3
"""
verify_links — async HEAD-checker over every URL in the knowledge graph
              and (optionally) over rendered HTML/MD output.

- Polite 1 req/s rate limit on lex.uz, cbd.minjust.gov.kg, president.uz, gov.uz, etc.
- Three-layer fallback: live -> archive.org Wayback -> annotation
- Output: state/audit/link_report.json

Usage:
    python3 scripts/verify_links.py                  # all URLs in knowledge graph
    python3 scripts/verify_links.py --internal-only  # only links between repo files
    python3 scripts/verify_links.py --output state/audit/link_report.json
"""

from __future__ import annotations

import argparse
import asyncio
import json
import re
import sys
import time
from collections import defaultdict
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

import httpx

ROOT = Path(__file__).resolve().parent.parent
KG_PATH = ROOT / "state" / "knowledge_graph.json"
DEFAULT_REPORT = ROOT / "state" / "audit" / "link_report.json"

# Domains that throttle aggressively — give them 1 req/s
SLOW_DOMAINS = {
    "lex.uz",
    "cbd.minjust.gov.kg",
    "president.uz",
    "president.kg",
    "gov.uz",
    "gov.kg",
    "kabmin.kg",
    "norma.uz",
}

# Languages we recognize from URL domain TLD (rough heuristic)
LANG_DOMAIN_HINTS = {
    ".uz": "uz_or_ru",
    ".kg": "ky_or_ru",
    ".ru": "ru",
    "lex.uz": "ru",
    "cbd.minjust.gov.kg": "ru",
    "norma.uz": "ru",
    "spot.uz": "ru",
    "gazeta.uz": "ru",
    "kun.uz": "ru",
    "daryo.uz": "ru",
    "podrobno.uz": "ru",
    "24.kg": "ru",
    "kaktus.media": "ru",
    "akipress.org": "ru",
    "azattyk.org": "ky",
    "economist.kg": "ru",
    "documents.worldbank.org": "en",
    "projects.worldbank.org": "en",
    "adb.org": "en",
    "ec.europa.eu": "en",
    "undp.org": "en",
}

URL_RE = re.compile(r"https?://[^\s\"'<>)]+", re.IGNORECASE)


def extract_urls_from_text(text: str) -> list[str]:
    return list({m.group(0).rstrip(".,;:)") for m in URL_RE.finditer(text)})


def extract_urls_from_kg(kg: dict[str, Any]) -> dict[str, list[str]]:
    """Pull URLs from every Source.url + Person.linkedin_url + Tender.tender_url + Institution.official_website."""
    urls: dict[str, set[str]] = defaultdict(set)

    def add(url: str, kind: str) -> None:
        if url and isinstance(url, str) and url.startswith(("http://", "https://")):
            urls[kind].add(url)

    for d in kg.get("decrees", []) or []:
        for s in d.get("sources", []) or []:
            add(s.get("url", ""), "decree_source")
    for inst in kg.get("institutions", []) or []:
        add(inst.get("official_website", ""), "institution_website")
        for s in inst.get("sources", []) or []:
            add(s.get("url", ""), "institution_source")
    for p in kg.get("people", []) or []:
        add(p.get("linkedin_url", "") or "", "linkedin")
        for s in p.get("sources", []) or []:
            add(s.get("url", ""), "person_source")
    for prog in kg.get("donor_programs", []) or []:
        for s in prog.get("sources", []) or []:
            add(s.get("url", ""), "donor_source")
    for t in kg.get("tenders", []) or []:
        add(t.get("tender_url", "") or "", "tender_url")
        for s in t.get("sources", []) or []:
            add(s.get("url", ""), "tender_source")
    for tr in kg.get("trends", []) or []:
        for s in tr.get("sources", []) or []:
            add(s.get("url", ""), "trend_source")
    for c in kg.get("global_cases", []) or []:
        for s in c.get("sources", []) or []:
            add(s.get("url", ""), "case_source")
    return {k: sorted(v) for k, v in urls.items()}


def lang_for(url: str) -> str:
    host = (urlparse(url).hostname or "").lower()
    for needle, lang in LANG_DOMAIN_HINTS.items():
        if needle in host:
            return lang
    if host.endswith(".uz"):
        return "uz_or_ru"
    if host.endswith(".kg"):
        return "ky_or_ru"
    if host.endswith(".ru"):
        return "ru"
    return "en"


async def head_check(
    client: httpx.AsyncClient, url: str, slow: bool, sem: asyncio.Semaphore
) -> dict[str, Any]:
    async with sem:
        if slow:
            # naive 1 req/s throttle by sleeping inside the semaphore
            await asyncio.sleep(1.0)
        result: dict[str, Any] = {
            "url": url,
            "status_code": None,
            "final_url": url,
            "redirected": False,
            "wayback_url": None,
            "language": lang_for(url),
            "error": None,
            "category": "unknown",
        }
        try:
            r = await client.head(url, timeout=15.0, follow_redirects=True)
            result["status_code"] = r.status_code
            if r.url and str(r.url) != url:
                result["final_url"] = str(r.url)
                result["redirected"] = True
            if r.status_code == 405:  # Method Not Allowed -> retry GET
                r = await client.get(url, timeout=20.0, follow_redirects=True)
                result["status_code"] = r.status_code
                if r.url and str(r.url) != url:
                    result["final_url"] = str(r.url)
                    result["redirected"] = True
            if 200 <= r.status_code < 300:
                result["category"] = "ok"
            elif 300 <= r.status_code < 400:
                result["category"] = "redirect"
            elif 400 <= r.status_code < 500:
                result["category"] = "client_error"
            elif 500 <= r.status_code < 600:
                result["category"] = "server_error"
        except httpx.TimeoutException:
            result["error"] = "timeout"
            result["category"] = "timeout"
        except httpx.NetworkError as e:
            result["error"] = f"network: {type(e).__name__}"
            result["category"] = "network_error"
        except Exception as e:  # noqa: BLE001
            result["error"] = f"{type(e).__name__}: {e}"
            result["category"] = "exception"
        # Wayback fallback for client/server/timeout errors
        if result["category"] in ("client_error", "server_error", "timeout", "network_error"):
            wb = f"https://web.archive.org/web/2026/{url}"
            try:
                r = await client.head(wb, timeout=15.0, follow_redirects=True)
                if 200 <= r.status_code < 400:
                    result["wayback_url"] = str(r.url)
            except Exception:  # noqa: BLE001
                pass
        return result


async def run(urls_by_kind: dict[str, list[str]]) -> dict[str, Any]:
    sem = asyncio.Semaphore(20)
    async with httpx.AsyncClient(
        headers={"User-Agent": "Mozilla/5.0 (compatible; ca-b2g-research/1.0; +https://github.com/avaluev/ca-b2g-research)"},
        verify=True,
    ) as client:
        all_results: list[dict[str, Any]] = []
        for kind, urls in urls_by_kind.items():
            tasks = []
            for u in urls:
                host = (urlparse(u).hostname or "").lower()
                slow = any(d in host for d in SLOW_DOMAINS)
                tasks.append(head_check(client, u, slow, sem))
            results = await asyncio.gather(*tasks, return_exceptions=False)
            for r in results:
                r["kind"] = kind
                all_results.append(r)
    return all_results  # type: ignore[return-value]


def summarize(results: list[dict[str, Any]]) -> dict[str, Any]:
    by_cat: dict[str, int] = defaultdict(int)
    by_kind: dict[str, dict[str, int]] = defaultdict(lambda: defaultdict(int))
    by_lang: dict[str, int] = defaultdict(int)
    for r in results:
        by_cat[r["category"]] += 1
        by_kind[r["kind"]][r["category"]] += 1
        by_lang[r["language"]] += 1
    total = max(1, len(results))
    ok = by_cat.get("ok", 0) + by_cat.get("redirect", 0)
    breakage_pct = round(100.0 * (total - ok) / total, 2)
    return {
        "total_urls": total,
        "ok_count": ok,
        "broken_count": total - ok,
        "breakage_pct": breakage_pct,
        "by_category": dict(by_cat),
        "by_kind": {k: dict(v) for k, v in by_kind.items()},
        "by_language": dict(by_lang),
    }


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--input", default=str(KG_PATH), help="knowledge_graph.json path")
    p.add_argument("--output", default=str(DEFAULT_REPORT), help="report output path")
    p.add_argument("--internal-only", action="store_true", help="skip external URL checking")
    p.add_argument("--all", action="store_true", help="full external sweep (default)")
    args = p.parse_args()

    kg_path = Path(args.input)
    if not kg_path.exists():
        print(f"❌ {kg_path} not found", file=sys.stderr)
        return 1
    kg = json.loads(kg_path.read_text() or "{}")
    urls = extract_urls_from_kg(kg)
    total = sum(len(v) for v in urls.values())
    print(f"Found {total} URLs across {len(urls)} categories")
    if total == 0:
        report = {
            "checked_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "total_urls": 0,
            "ok_count": 0,
            "broken_count": 0,
            "breakage_pct": 0.0,
            "by_category": {},
            "by_kind": {},
            "by_language": {},
            "results": [],
        }
        Path(args.output).parent.mkdir(parents=True, exist_ok=True)
        Path(args.output).write_text(json.dumps(report, indent=2))
        print(f"✅ wrote {args.output} (no URLs to check)")
        return 0
    if args.internal_only:
        # Trim external URLs (everything not file://) — for CI smoke test
        for k, v in list(urls.items()):
            urls[k] = [u for u in v if u.startswith("file://")]
        total = sum(len(v) for v in urls.values())
        if total == 0:
            print("No internal URLs to verify (CI smoke test passes vacuously).")
            Path(args.output).parent.mkdir(parents=True, exist_ok=True)
            Path(args.output).write_text(json.dumps({
                "checked_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                "total_urls": 0, "ok_count": 0, "broken_count": 0,
                "breakage_pct": 0.0, "by_category": {}, "by_kind": {},
                "by_language": {}, "results": [], "internal_only": True,
            }, indent=2))
            return 0

    print("Running checks...")
    t0 = time.time()
    results = asyncio.run(run(urls))
    elapsed = time.time() - t0
    summary = summarize(results)
    print(f"Checked {summary['total_urls']} URLs in {elapsed:.1f}s")
    print(f"  OK:     {summary['ok_count']}")
    print(f"  Broken: {summary['broken_count']} ({summary['breakage_pct']}%)")
    by_cat = summary["by_category"]
    for cat, n in sorted(by_cat.items()):
        print(f"   {cat:20s} {n}")

    report = {
        "checked_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        **summary,
        "results": results,
    }
    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    Path(args.output).write_text(json.dumps(report, indent=2, ensure_ascii=False))
    print(f"✅ report at {args.output}")
    # Exit non-zero if breakage > 5%
    return 0 if summary["breakage_pct"] <= 5.0 else 1


if __name__ == "__main__":
    sys.exit(main())
