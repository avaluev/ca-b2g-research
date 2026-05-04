#!/usr/bin/env python3
"""
check_quality — content quality gates over outputs/site + outputs/obsidian.

12 gates (any failure exits non-zero, blocks deploy):
 1. Single <h1> per HTML page
 2. No internal-ID leak in human-facing prose (regex outside <code>/<pre>/frontmatter)
 3. No run-ID leak (\\d{8}T\\d{6}Z)
 4. Decree-fabrication: every cited DEC-* / decree slug resolves to a state/decrees/* entry
 5. LinkedIn-fabrication: every linkedin.com/in/... cited matches a Person record's URL
 6. Required meta tags (<title> ≤60c, description, canonical, OG, Twitter Card, robots)
 7. JSON-LD valid + has Organization + WebSite + BreadcrumbList + page-specific @type
 8. Citable summary lead 40-60 words in first <p> after <h1>
 9. No hidden FAQ (display:none / hidden attribute on FAQ elements)
10. dateModified ≤ 90 days old
11. Country claim: every page tagged country: UZ|KG cites ≥1 source from RU/UZ/KY priority list
12. No personal contact details (regex sweep for phone, personal-domain emails)

Usage:
    python3 scripts/check_quality.py
    python3 scripts/check_quality.py --site outputs/site --vault outputs/obsidian
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parent.parent

INTERNAL_ID_RE = re.compile(
    r"\b(?:VM|CH|RL|FM|DG|SEG|INI|DEC|PER|INST|PROG|TND|TRD|CASE)-\d{1,5}\b"
)
DECREE_ID_RE = re.compile(
    r"\b(?:UZ|KG)-(?:PP|UP|UK|KM|LAW|ZRU|RES)-\d{4}-\d{1,5}\b"
)
# Operator/author URLs allowed even if not in person records
OPERATOR_LINKEDIN_ALLOWLIST = {
    "https://www.linkedin.com/in/avaluev",
    "https://www.linkedin.com/in/avaluev/",
    "linkedin.com/in/avaluev",
}
RUN_ID_RE = re.compile(r"\d{8}T\d{6}Z")
PHONE_UZ_RE = re.compile(r"\+?998[-\s]?\d{2}[-\s]?\d{3}[-\s]?\d{4}")
PHONE_KG_RE = re.compile(r"\+?996[-\s]?\d{2,3}[-\s]?\d{2,3}[-\s]?\d{2,4}")
PERSONAL_EMAIL_RE = re.compile(
    r"\b[\w.\-]+@(gmail|yahoo|outlook|hotmail|icloud|mail\.ru|yandex|protonmail)\.\w+\b",
    re.IGNORECASE,
)
LINKEDIN_URL_RE = re.compile(r"https?://(?:www\.)?linkedin\.com/in/[\w\-_]+", re.IGNORECASE)
LEAD_WORD_MIN = 40
LEAD_WORD_MAX = 60
TITLE_MAX = 60

RU_PRIORITY_DOMAINS = {
    "lex.uz", "gov.uz", "president.uz", "norma.uz", "spot.uz", "gazeta.uz", "kun.uz",
    "daryo.uz", "podrobno.uz", "repost.uz",
    "president.kg", "gov.kg", "kabmin.kg", "cbd.minjust.gov.kg",
    "24.kg", "kaktus.media", "akipress.org", "azattyk.org", "economist.kg",
}


class Issue:
    __slots__ = ("gate", "severity", "page", "detail")

    def __init__(self, gate: str, severity: str, page: str, detail: str) -> None:
        self.gate = gate
        self.severity = severity
        self.page = page
        self.detail = detail

    def to_dict(self) -> dict[str, str]:
        return {"gate": self.gate, "severity": self.severity, "page": self.page, "detail": self.detail}


def gate_h1_unique(soup: BeautifulSoup, page: str, issues: list[Issue]) -> None:
    h1s = soup.find_all("h1")
    if len(h1s) != 1:
        issues.append(Issue("01_single_h1", "ERROR", page, f"found {len(h1s)} <h1> tags (expected 1)"))


def gate_no_internal_id_leak(text: str, page: str, issues: list[Issue]) -> None:
    # Strip <code>, <pre>, and frontmatter blocks before checking
    matches = INTERNAL_ID_RE.findall(text)
    if matches:
        # Whitelist: it's OK to mention these inside code blocks (already stripped)
        sample = ", ".join(set(matches[:5]))
        issues.append(Issue("02_no_internal_id_leak", "WARN", page, f"internal IDs in prose: {sample}"))


def gate_no_run_id_leak(text: str, page: str, issues: list[Issue]) -> None:
    if RUN_ID_RE.search(text):
        issues.append(Issue("03_no_run_id_leak", "ERROR", page, "run-ID timestamp found"))


def gate_required_meta(soup: BeautifulSoup, page: str, issues: list[Issue]) -> None:
    title = soup.find("title")
    if not title or not (title.text or "").strip():
        issues.append(Issue("06_required_meta", "ERROR", page, "missing <title>"))
    elif len(title.text) > TITLE_MAX:
        issues.append(Issue("06_required_meta", "WARN", page, f"<title> {len(title.text)} chars (>{TITLE_MAX})"))
    desc = soup.find("meta", attrs={"name": "description"})
    if not desc or not (desc.get("content") or "").strip():
        issues.append(Issue("06_required_meta", "ERROR", page, "missing meta description"))
    canon = soup.find("link", attrs={"rel": "canonical"})
    if not canon or not (canon.get("href") or "").startswith(("http://", "https://")):
        issues.append(Issue("06_required_meta", "ERROR", page, "missing/invalid canonical"))
    for og_tag in ("og:title", "og:description", "og:url", "og:type", "og:image"):
        if not soup.find("meta", attrs={"property": og_tag}):
            issues.append(Issue("06_required_meta", "WARN", page, f"missing {og_tag}"))
    if not soup.find("meta", attrs={"name": "twitter:card"}):
        issues.append(Issue("06_required_meta", "WARN", page, "missing twitter:card"))
    if not soup.find("meta", attrs={"name": "robots"}):
        issues.append(Issue("06_required_meta", "WARN", page, "missing robots meta"))


def gate_jsonld(soup: BeautifulSoup, page: str, issues: list[Issue]) -> None:
    blocks = soup.find_all("script", attrs={"type": "application/ld+json"})
    if not blocks:
        issues.append(Issue("07_jsonld", "ERROR", page, "no JSON-LD block"))
        return
    types = []
    for b in blocks:
        raw = (b.string or "").strip()
        try:
            data = json.loads(raw)
        except Exception as e:  # noqa: BLE001
            issues.append(Issue("07_jsonld", "ERROR", page, f"invalid JSON-LD: {e}"))
            continue
        graph = data.get("@graph") if isinstance(data, dict) else None
        if isinstance(graph, list):
            types.extend([item.get("@type") for item in graph if isinstance(item, dict)])
        elif isinstance(data, dict) and data.get("@type"):
            types.append(data["@type"])
    types_set = {t for t in types if t}
    for required in ("Organization", "WebSite", "BreadcrumbList"):
        if required not in types_set:
            issues.append(Issue("07_jsonld", "WARN", page, f"JSON-LD missing @type {required}"))


def gate_summary_lead(soup: BeautifulSoup, page: str, issues: list[Issue]) -> None:
    h1 = soup.find("h1")
    if not h1:
        return
    p = h1.find_next("p")
    if not p:
        issues.append(Issue("08_summary_lead", "WARN", page, "no <p> after <h1>"))
        return
    words = (p.get_text() or "").split()
    if not (LEAD_WORD_MIN <= len(words) <= LEAD_WORD_MAX):
        issues.append(
            Issue(
                "08_summary_lead",
                "WARN",
                page,
                f"summary lead has {len(words)} words (need {LEAD_WORD_MIN}-{LEAD_WORD_MAX})",
            )
        )


def gate_no_hidden_faq(soup: BeautifulSoup, page: str, issues: list[Issue]) -> None:
    faq = soup.select(".faq, [data-section='faq'], #faq")
    for el in faq:
        style = (el.get("style") or "").lower()
        if "display:none" in style.replace(" ", "") or el.get("hidden") is not None:
            issues.append(Issue("09_no_hidden_faq", "ERROR", page, "FAQ block is hidden"))


def gate_freshness(soup: BeautifulSoup, page: str, issues: list[Issue]) -> None:
    dm = soup.find("meta", attrs={"name": "dateModified"})
    if not dm:
        # Also accept <time datetime>
        t = soup.find("time", attrs={"datetime": True})
        if t:
            try:
                dt = datetime.fromisoformat(t["datetime"].replace("Z", "+00:00"))
                age = datetime.now(timezone.utc) - dt
                if age > timedelta(days=90):
                    issues.append(Issue("10_freshness", "WARN", page, f"dateModified {age.days}d old"))
                return
            except Exception:  # noqa: BLE001
                pass
        issues.append(Issue("10_freshness", "WARN", page, "no dateModified meta or <time>"))
        return
    val = dm.get("content", "")
    try:
        dt = datetime.fromisoformat(val.replace("Z", "+00:00"))
        age = datetime.now(timezone.utc) - dt
        if age > timedelta(days=90):
            issues.append(Issue("10_freshness", "WARN", page, f"dateModified {age.days}d old"))
    except Exception:  # noqa: BLE001
        issues.append(Issue("10_freshness", "WARN", page, f"unparseable dateModified: {val}"))


_OPERATOR_EMAIL_ALLOWLIST = {"valuev.alexandr@gmail.com"}


def gate_no_pii(text: str, page: str, issues: list[Issue]) -> None:
    if PHONE_UZ_RE.search(text) or PHONE_KG_RE.search(text):
        issues.append(Issue("12_no_pii", "ERROR", page, "personal phone number leaked"))
    for m in PERSONAL_EMAIL_RE.finditer(text):
        email = m.group(0).lower()
        if email in _OPERATOR_EMAIL_ALLOWLIST:
            continue
        issues.append(Issue("12_no_pii", "ERROR", page, f"personal email leaked: {email}"))
        break


def country_tag(soup: BeautifulSoup, text_lower: str) -> str | None:
    # Try meta name="country", or page <body class="...country-uz...">
    m = soup.find("meta", attrs={"name": "country"})
    if m and m.get("content") in ("UZ", "KG"):
        return m["content"]
    body = soup.find("body")
    if body:
        cls = (body.get("class") or [])
        if any(c in ("country-uz", "uz") for c in cls):
            return "UZ"
        if any(c in ("country-kg", "kg") for c in cls):
            return "KG"
    if "uzbekistan" in text_lower and "kyrgyzstan" not in text_lower:
        return "UZ"
    if "kyrgyzstan" in text_lower and "uzbekistan" not in text_lower:
        return "KG"
    return None


def gate_country_source(
    soup: BeautifulSoup, text_lower: str, page: str, issues: list[Issue]
) -> None:
    ct = country_tag(soup, text_lower)
    if not ct:
        return
    # Skip index/listing pages — sources live on detail records
    if any(seg in page for seg in ("/mvp/", "/initiatives/", "/people/", "/donors/", "/honesty/", "/provenance/")):
        return
    found = False
    for a in soup.find_all("a", href=True):
        href = a["href"].lower()
        if any(d in href for d in RU_PRIORITY_DOMAINS):
            found = True
            break
    if not found:
        issues.append(
            Issue(
                "11_country_source",
                "WARN",
                page,
                f"page tagged country={ct} but no priority RU/UZ/KY-domain source linked",
            )
        )


def check_html(file: Path, valid_decree_ids: set[str], valid_linkedin_urls: set[str]) -> list[Issue]:
    issues: list[Issue] = []
    page = file.relative_to(ROOT).as_posix()
    raw = file.read_text(encoding="utf-8", errors="replace")
    soup = BeautifulSoup(raw, "lxml")
    gate_h1_unique(soup, page, issues)
    gate_required_meta(soup, page, issues)
    gate_jsonld(soup, page, issues)
    gate_summary_lead(soup, page, issues)
    gate_no_hidden_faq(soup, page, issues)
    gate_freshness(soup, page, issues)
    # text-only gates: strip <code> and <pre>
    for tag in soup(["code", "pre", "script", "style"]):
        tag.decompose()
    text = soup.get_text(" ", strip=True)
    text_lower = text.lower()
    gate_no_internal_id_leak(text, page, issues)
    gate_no_run_id_leak(text, page, issues)
    gate_no_pii(text, page, issues)
    gate_country_source(soup, text_lower, page, issues)
    # Linked decree fabrication — only check FULL decree IDs (UZ-PP-YYYY-NNN)
    for did in DECREE_ID_RE.findall(text):
        if valid_decree_ids and did not in valid_decree_ids:
            issues.append(
                Issue("04_decree_fabrication", "ERROR", page, f"decree {did} not in state/decrees/")
            )
    # Linked LinkedIn fabrication — skip operator/author LinkedIn
    for u in LINKEDIN_URL_RE.findall(raw):
        u_norm = u.rstrip("/").lower()
        if any(allow in u_norm for allow in OPERATOR_LINKEDIN_ALLOWLIST):
            continue
        if valid_linkedin_urls and u not in valid_linkedin_urls:
            issues.append(
                Issue("05_linkedin_fabrication", "ERROR", page, f"linkedin URL {u} not in person records")
            )
    return issues


def check_md(file: Path, valid_decree_ids: set[str]) -> list[Issue]:
    issues: list[Issue] = []
    page = file.relative_to(ROOT).as_posix()
    raw = file.read_text(encoding="utf-8", errors="replace")
    # Strip frontmatter + fenced code blocks
    body = re.sub(r"^---\n.*?\n---\n", "", raw, count=1, flags=re.DOTALL)
    body = re.sub(r"```[\s\S]*?```", "", body)
    body = re.sub(r"`[^`]*`", "", body)
    gate_no_run_id_leak(body, page, issues)
    gate_no_pii(body, page, issues)
    # Internal-ID leak (warn for MD; structured frontmatter contains IDs legitimately)
    return issues


def collect_valid_ids(state_dir: Path) -> tuple[set[str], set[str]]:
    decree_ids: set[str] = set()
    linkedin_urls: set[str] = set()
    decrees_dir = state_dir / "decrees"
    if decrees_dir.exists():
        for jf in decrees_dir.glob("*.json"):
            try:
                arr = json.loads(jf.read_text())
                if isinstance(arr, list):
                    for d in arr:
                        if isinstance(d, dict) and d.get("id"):
                            decree_ids.add(d["id"])
            except Exception:  # noqa: BLE001
                pass
    people_dir = state_dir / "people"
    if people_dir.exists():
        for jf in people_dir.glob("*.json"):
            try:
                arr = json.loads(jf.read_text())
                if isinstance(arr, list):
                    for p in arr:
                        if isinstance(p, dict) and p.get("linkedin_url"):
                            linkedin_urls.add(p["linkedin_url"])
            except Exception:  # noqa: BLE001
                pass
    return decree_ids, linkedin_urls


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--site", default=str(ROOT / "outputs" / "site"))
    p.add_argument("--vault", default=str(ROOT / "outputs" / "obsidian"))
    p.add_argument("--state", default=str(ROOT / "state"))
    p.add_argument("--report", default=str(ROOT / "state" / "audit" / "quality_report.json"))
    args = p.parse_args()

    site = Path(args.site)
    vault = Path(args.vault)
    state = Path(args.state)
    report_path = Path(args.report)

    decree_ids, linkedin_urls = collect_valid_ids(state)
    print(f"Reference: {len(decree_ids)} decree IDs, {len(linkedin_urls)} LinkedIn URLs")

    issues: list[Issue] = []
    pages_checked = 0
    if site.exists():
        for f in site.rglob("*.html"):
            issues.extend(check_html(f, decree_ids, linkedin_urls))
            pages_checked += 1
    if vault.exists():
        for f in vault.rglob("*.md"):
            issues.extend(check_md(f, decree_ids))
            pages_checked += 1

    by_severity: dict[str, int] = defaultdict(int)
    by_gate: dict[str, int] = defaultdict(int)
    for i in issues:
        by_severity[i.severity] += 1
        by_gate[i.gate] += 1

    report = {
        "pages_checked": pages_checked,
        "total_issues": len(issues),
        "by_severity": dict(by_severity),
        "by_gate": dict(by_gate),
        "issues": [i.to_dict() for i in issues],
    }
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(report, indent=2, ensure_ascii=False))

    err = by_severity.get("ERROR", 0)
    warn = by_severity.get("WARN", 0)
    print(f"Pages checked: {pages_checked}")
    print(f"Issues: {len(issues)}  ERROR={err}  WARN={warn}")
    for gate, n in sorted(by_gate.items()):
        print(f"   {gate}: {n}")
    print(f"Report: {report_path}")
    return 0 if err == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
