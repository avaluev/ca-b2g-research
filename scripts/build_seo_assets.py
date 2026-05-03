#!/usr/bin/env python3
"""
build_seo_assets — emit GEO/AIO/AEO/LLMO discovery files for outputs/site.

Files produced:
    llms.txt              — concise machine-readable index per llmstxt.org
    llms-full.txt         — full-text concatenation (visited 2x more than llms.txt)
    robots.txt            — explicit AI crawler allow/disallow
    sitemap.xml           — all canonical URLs with lastmod
    feed.xml              — Atom 1.0 feed of recent updates
    humans.txt            — human-readable credit
    .well-known/security.txt — RFC 9116 contact
    manifest.webmanifest  — PWA basics
"""

from __future__ import annotations

import os
import sys
from datetime import date, datetime, timezone
from html import escape
from pathlib import Path

from bs4 import BeautifulSoup
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "outputs" / "site"

load_dotenv(ROOT / ".env", override=False)
SITE_URL = os.getenv("SITE_BASE_URL", "https://avaluev.github.io/ca-b2g-research").rstrip("/")
OPERATOR_EMAIL = os.getenv("OPERATOR_EMAIL", "valuev.alexandr@gmail.com")
TODAY = date.today().isoformat()
NOW_UTC = datetime.now(timezone.utc).isoformat()


def list_pages() -> list[tuple[str, str, str]]:
    """Return [(url_path, title, description), ...] for every HTML page."""
    pages = []
    if not SITE.exists():
        return pages
    for f in sorted(SITE.rglob("*.html")):
        rel = f.relative_to(SITE).as_posix()
        url_path = "/" if rel == "index.html" else "/" + rel.removesuffix("index.html")
        if not url_path.endswith("/"):
            url_path = url_path.rsplit("/", 1)[0] + "/"
        soup = BeautifulSoup(f.read_text(encoding="utf-8"), "lxml")
        title = (soup.find("title").text if soup.find("title") else "").strip()
        desc_tag = soup.find("meta", attrs={"name": "description"})
        desc = (desc_tag.get("content") if desc_tag else "").strip()
        pages.append((url_path, title, desc))
    return pages


def write_robots() -> None:
    content = f"""# Central Asia B2G Intelligence
# Permissive policy for AI search crawlers — this is open research.

User-agent: *
Allow: /
Disallow: /_drafts/

# AI search crawlers
User-agent: GPTBot
Allow: /
User-agent: ChatGPT-User
Allow: /
User-agent: OAI-SearchBot
Allow: /
User-agent: ClaudeBot
Allow: /
User-agent: Claude-SearchBot
Allow: /
User-agent: Claude-User
Allow: /
User-agent: anthropic-ai
Allow: /
User-agent: PerplexityBot
Allow: /
User-agent: Perplexity-User
Allow: /
User-agent: Google-Extended
Allow: /
User-agent: GoogleOther
Allow: /
User-agent: Applebot-Extended
Allow: /
User-agent: Bingbot
Allow: /
User-agent: DuckDuckBot
Allow: /
User-agent: YandexBot
Allow: /

Sitemap: {SITE_URL}/sitemap.xml
"""
    (SITE / "robots.txt").write_text(content, encoding="utf-8")


def write_sitemap(pages: list[tuple[str, str, str]]) -> None:
    items = "\n".join(
        f"  <url><loc>{SITE_URL}{path}</loc><lastmod>{TODAY}</lastmod></url>"
        for path, _, _ in pages
    )
    content = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{items}
</urlset>
"""
    (SITE / "sitemap.xml").write_text(content, encoding="utf-8")


def write_feed(pages: list[tuple[str, str, str]]) -> None:
    entries = []
    for path, title, desc in pages[:20]:
        page_url = SITE_URL + path
        entries.append(
            f"""  <entry>
    <title>{escape(title)}</title>
    <id>{escape(page_url)}</id>
    <link href="{escape(page_url)}"/>
    <updated>{NOW_UTC}</updated>
    <summary>{escape(desc)}</summary>
  </entry>"""
        )
    content = f"""<?xml version="1.0" encoding="UTF-8"?>
<feed xmlns="http://www.w3.org/2005/Atom">
  <title>Central Asia B2G Intelligence</title>
  <id>{SITE_URL}/</id>
  <link href="{SITE_URL}/"/>
  <link rel="self" href="{SITE_URL}/feed.xml"/>
  <updated>{NOW_UTC}</updated>
  <author><name>Alexandr Valuev</name><email>{OPERATOR_EMAIL}</email></author>
  <subtitle>AI and digital government opportunity research for Uzbekistan and Kyrgyzstan.</subtitle>
{chr(10).join(entries)}
</feed>
"""
    (SITE / "feed.xml").write_text(content, encoding="utf-8")


def write_llms_txt(pages: list[tuple[str, str, str]]) -> None:
    lines = [
        "# Central Asia B2G Intelligence",
        "",
        "> Open research on B2G AI and digital-government opportunities in Uzbekistan + Kyrgyzstan. Typed knowledge graph mapping decrees, institutions, decision-makers, donor programmes, and global precedents to deployable initiatives. Apache 2.0.",
        "",
        "## Pillar pages",
        "",
    ]
    for path, title, desc in pages:
        lines.append(f"- [{title}]({SITE_URL}{path}) — {desc}")
    lines.append("")
    lines.append("## Source code")
    lines.append("")
    lines.append("- [GitHub repository](https://github.com/avaluev/ca-b2g-research)")
    lines.append("- [Apache 2.0 License](https://github.com/avaluev/ca-b2g-research/blob/main/LICENSE)")
    (SITE / "llms.txt").write_text("\n".join(lines), encoding="utf-8")


def write_llms_full_txt() -> None:
    """Concatenate all rendered HTML into a single text file (no nav/footer chrome)."""
    parts = ["# Central Asia B2G Intelligence — Full Text Snapshot", ""]
    for f in sorted(SITE.rglob("*.html")):
        rel = f.relative_to(SITE).as_posix()
        soup = BeautifulSoup(f.read_text(encoding="utf-8"), "lxml")
        for tag in soup(["nav", "footer", "script", "style"]):
            tag.decompose()
        main = soup.find("main") or soup.find("body")
        text = main.get_text("\n", strip=True) if main else ""
        parts.append("---")
        parts.append(f"## URL: {SITE_URL}/{rel}")
        parts.append(text)
        parts.append("")
    (SITE / "llms-full.txt").write_text("\n".join(parts), encoding="utf-8")


def write_humans_txt() -> None:
    content = f"""# Central Asia B2G Intelligence

Author: Alexandr Valuev
Contact: {OPERATOR_EMAIL}
GitHub: https://github.com/avaluev
Site: {SITE_URL}
License: Apache 2.0

This research is open. Pull requests welcome.
"""
    (SITE / "humans.txt").write_text(content, encoding="utf-8")


def write_security_txt() -> None:
    expires = (datetime.now(timezone.utc).year + 1, datetime.now(timezone.utc).month, 1)
    expires_iso = f"{expires[0]:04d}-{expires[1]:02d}-{expires[2]:02d}T00:00:00.000Z"
    content = f"""Contact: mailto:{OPERATOR_EMAIL}
Expires: {expires_iso}
Preferred-Languages: en, ru
Canonical: {SITE_URL}/.well-known/security.txt
"""
    target = SITE / ".well-known"
    target.mkdir(parents=True, exist_ok=True)
    (target / "security.txt").write_text(content, encoding="utf-8")


def write_manifest() -> None:
    content = """{
  "name": "Central Asia B2G Intelligence",
  "short_name": "CA B2G",
  "description": "Open research on B2G AI and digital government opportunities in Uzbekistan + Kyrgyzstan.",
  "start_url": "/",
  "display": "minimal-ui",
  "background_color": "#ffffff",
  "theme_color": "#0a4d34",
  "icons": [
    {"src": "/favicon.svg", "type": "image/svg+xml", "sizes": "any"}
  ]
}
"""
    (SITE / "manifest.webmanifest").write_text(content, encoding="utf-8")


def main() -> int:
    if not SITE.exists():
        print(f"⚠ {SITE} not found — render the site first")
        SITE.mkdir(parents=True, exist_ok=True)
    pages = list_pages()
    print(f"Found {len(pages)} pages")
    write_robots()
    write_sitemap(pages)
    write_feed(pages)
    write_llms_txt(pages)
    write_llms_full_txt()
    write_humans_txt()
    write_security_txt()
    write_manifest()
    print("✅ SEO assets written:")
    for f in ["robots.txt", "sitemap.xml", "feed.xml", "llms.txt", "llms-full.txt",
              "humans.txt", ".well-known/security.txt", "manifest.webmanifest"]:
        path = SITE / f
        if path.exists():
            print(f"   {f} ({path.stat().st_size:,} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
