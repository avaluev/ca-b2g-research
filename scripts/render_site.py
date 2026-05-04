#!/usr/bin/env python3
"""
render_site — emit a static HTML site from the knowledge graph.

15 pages covering: Home, Methodology, Lenses, Scoring,
Decree Atlases (UZ + KG), Institution Maps (UZ + KG),
Donor Pipeline, Procurement, Trends, People, Initiatives,
Honesty, Provenance.

Per-page contract enforced by check_quality.py:
  - Single <h1>
  - 40-60 word citable summary lead in first <p>
  - JSON-LD @graph: Organization + WebSite + BreadcrumbList + page-type
  - Required meta: title, description, canonical, OG, Twitter Card, robots
  - dateModified ≤ 90 days

Usage:
    python3 scripts/render_site.py
    SITE_BASE_URL=https://avaluev.github.io/ca-b2g-research python3 scripts/render_site.py
"""

from __future__ import annotations

import html
import json
import os
import re
import shutil
import sys
from datetime import date, datetime, timezone
from html import escape
from pathlib import Path
from typing import Any

from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent.parent
GRAPH_PATH = ROOT / "state" / "knowledge_graph.json"
SITE = ROOT / "outputs" / "site"
DOCS = ROOT / "docs"

load_dotenv(ROOT / ".env", override=False)
SITE_URL = os.getenv("SITE_BASE_URL", "https://avaluev.github.io/ca-b2g-research").rstrip("/")
# Path prefix for every internal link. Derived from SITE_URL so localhost / custom-
# domain deployments work too. Empty when the site is hosted at host root.
# Example: SITE_URL='https://avaluev.github.io/ca-b2g-research' -> BASE_PATH='/ca-b2g-research'
import urllib.parse as _urlparse
BASE_PATH = _urlparse.urlparse(SITE_URL).path.rstrip("/")


def _bp(path: str) -> str:
    """Prefix an internal absolute path with BASE_PATH. No-op when BASE_PATH is empty."""
    if not path.startswith("/"):
        return path
    if not BASE_PATH:
        return path
    if path.startswith(BASE_PATH + "/") or path == BASE_PATH:
        return path
    return BASE_PATH + path
OPERATOR = os.getenv("OPERATOR_NAME", "Alexandr Valuev")
OPERATOR_EMAIL = os.getenv("OPERATOR_EMAIL", "valuev.alexandr@gmail.com")
OPERATOR_LINKEDIN = os.getenv("OPERATOR_LINKEDIN", "https://www.linkedin.com/in/avaluev/")
OPERATOR_GITHUB = os.getenv("OPERATOR_GITHUB", "https://github.com/avaluev")
TODAY = date.today().isoformat()
NOW_ISO = datetime.now(timezone.utc).isoformat()


def slugify(s: str) -> str:
    s = (s or "").lower().strip()
    s = re.sub(r"[^\w\s\-]", "", s, flags=re.UNICODE)
    s = re.sub(r"[\s_]+", "-", s)
    return re.sub(r"-+", "-", s).strip("-")


def index_by_id(arr: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    return {r.get("id"): r for r in arr if isinstance(r, dict) and r.get("id")}


# ────────────────────────────────────────────────────────────────────────────
# Page chrome
# ────────────────────────────────────────────────────────────────────────────


CSS = """
:root{
  --c-fg:#0d1117;--c-fg-muted:#3a4147;--c-fg-soft:#5a6066;
  --c-bg:#fff;--c-bg-soft:#f6f8fa;--c-bg-card:#fafbfc;
  --c-border:#d8dde2;--c-border-soft:#e7ebee;
  --c-accent:#005c27;--c-accent-strong:#00471d;--c-accent-soft:#e9f6ee;
  --c-link:#0057cc;--c-link-hover:#003e94;
  --c-tier-a-bg:#fdebd3;--c-tier-a-fg:#7a4900;
  --c-tier-b-bg:#e9f6ee;--c-tier-b-fg:#005c27;
  --c-tier-c-bg:#f0f1f3;--c-tier-c-fg:#4a5158;
  --c-focus:#005fcc;
  --r-sm:3px;--r-md:6px;--r-lg:10px;
  --s-1:4px;--s-2:8px;--s-3:12px;--s-4:16px;--s-5:24px;--s-6:32px;--s-7:48px;--s-8:64px;
  --fz-h1:clamp(1.875rem,1.4rem + 2.4vw,2.625rem);
  --fz-h2:clamp(1.375rem,1.15rem + 1.1vw,1.625rem);
  --fz-h3:clamp(1.125rem,1.05rem + 0.4vw,1.25rem);
  --fz-lead:clamp(1.05rem,1.0rem + 0.4vw,1.18rem);
  --fz-body:1rem;--fz-sm:0.875rem;
  --max-w-prose:64ch;--max-w-shell:760px;--max-w-wide:1200px;
}
@media (prefers-color-scheme:dark){
  :root{
    --c-fg:#e6edf3;--c-fg-muted:#9ba8b4;--c-fg-soft:#7a868f;
    --c-bg:#0d1117;--c-bg-soft:#161b22;--c-bg-card:#1a1f26;
    --c-border:#30363d;--c-border-soft:#21262d;
    --c-accent:#3fb960;--c-accent-strong:#56d77a;--c-accent-soft:#0f2a18;
    --c-link:#58a6ff;--c-link-hover:#79b8ff;
    --c-tier-a-bg:#3a2607;--c-tier-a-fg:#f5b95d;
    --c-tier-b-bg:#0f2a18;--c-tier-b-fg:#56d77a;
    --c-tier-c-bg:#1a1f26;--c-tier-c-fg:#a3acb6;
    --c-focus:#58a6ff;
  }
}
*,*::before,*::after{box-sizing:border-box}
html{font-family:system-ui,-apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif;line-height:1.6;color:var(--c-fg);background:var(--c-bg);-webkit-text-size-adjust:100%;text-rendering:optimizeLegibility}
body{margin:0;padding:0;font-size:var(--fz-body)}
.container{max-inline-size:var(--max-w-shell);margin-inline:auto;padding-block:var(--s-5) var(--s-8);padding-inline:max(var(--s-5),env(safe-area-inset-left)) max(var(--s-5),env(safe-area-inset-right))}
.container > p, .container > ul, .container > ol{max-inline-size:var(--max-w-prose)}
header.nav{position:sticky;top:0;background:var(--c-bg);border-block-end:1px solid var(--c-border);z-index:50}
header.nav nav{max-inline-size:var(--max-w-wide);margin-inline:auto;padding-block:var(--s-2);padding-inline:max(var(--s-5),env(safe-area-inset-left)) max(var(--s-5),env(safe-area-inset-right));display:flex;flex-wrap:wrap;gap:var(--s-1) var(--s-3);align-items:center}
header.nav a{color:var(--c-fg-muted);text-decoration:none;font-size:var(--fz-sm);font-weight:500;padding:10px 8px;min-height:44px;display:inline-flex;align-items:center;border-radius:var(--r-sm)}
header.nav a:hover{color:var(--c-accent)}
header.nav a[aria-current="page"]{color:var(--c-fg);background:var(--c-bg-soft)}
header.nav .brand{font-weight:700;color:var(--c-fg);font-size:1rem;margin-inline-end:auto;text-decoration:none;padding-block:var(--s-2);min-height:44px;display:inline-flex;align-items:center;letter-spacing:-0.01em}
header.nav .brand::before{content:"\\25C6 ";color:var(--c-accent);margin-inline-end:6px}
header.nav details.nav-more{position:relative;display:inline-flex;align-items:center;min-height:44px}
header.nav details.nav-more>summary{list-style:none;cursor:pointer;color:var(--c-fg-muted);font-size:var(--fz-sm);font-weight:500;padding:10px 8px;min-height:44px;display:inline-flex;align-items:center;border-radius:var(--r-sm);user-select:none}
header.nav details.nav-more>summary::-webkit-details-marker{display:none}
header.nav details.nav-more>summary:hover{color:var(--c-accent)}
header.nav details.nav-more>summary:focus-visible{outline:2px solid var(--c-focus);outline-offset:2px}
header.nav details.nav-more[open]>summary{color:var(--c-fg);background:var(--c-bg-soft)}
header.nav .nav-more-panel{position:absolute;top:calc(100% + 4px);right:0;min-width:220px;background:var(--c-bg);border:1px solid var(--c-border);border-radius:var(--r-md);box-shadow:0 8px 24px rgba(0,0,0,.08);padding:6px;display:flex;flex-direction:column;gap:2px;z-index:60}
header.nav .nav-more-panel a{display:block;padding:10px 12px;min-height:44px;border-radius:var(--r-sm)}
header.nav .nav-more-panel a:hover{background:var(--c-bg-soft);color:var(--c-accent)}
@media (max-width:640px){header.nav .nav-more-panel{position:static;box-shadow:none;border:none;padding:0;margin-block-start:var(--s-1);width:100%}}
nav.breadcrumbs{font-size:var(--fz-sm);color:var(--c-fg-soft);margin-block-start:var(--s-2)}
nav.breadcrumbs ol{list-style:none;display:flex;flex-wrap:wrap;gap:var(--s-2);padding:0;margin:0}
nav.breadcrumbs li::after{content:" \\203A ";color:var(--c-fg-soft);margin-inline-start:var(--s-2)}
nav.breadcrumbs li:last-child::after{content:""}
nav.breadcrumbs a{color:var(--c-link);text-decoration:none}
nav.breadcrumbs a:hover{text-decoration:underline}
h1{font-size:var(--fz-h1);line-height:1.15;margin-block:var(--s-5) var(--s-3);color:var(--c-fg);font-weight:700;letter-spacing:-0.02em;max-inline-size:18ch}
h2{font-size:var(--fz-h2);line-height:1.25;margin-block:var(--s-7) var(--s-2);padding-block-start:var(--s-5);border-block-start:1px solid var(--c-border-soft);color:var(--c-fg);font-weight:650;letter-spacing:-0.01em}
h3{font-size:var(--fz-h3);margin-block:var(--s-5) var(--s-2);color:var(--c-fg);font-weight:600}
p{margin-block:var(--s-2) var(--s-4);max-inline-size:var(--max-w-prose)}
p.lead.summary{font-size:var(--fz-lead);line-height:1.55;color:var(--c-fg);background:var(--c-bg-soft);border-inline-start:3px solid var(--c-accent);padding-block:var(--s-3);padding-inline:var(--s-4);margin-block:var(--s-4) var(--s-5);border-radius:0 var(--r-md) var(--r-md) 0;max-inline-size:none}
ul,ol{padding-inline-start:var(--s-5);max-inline-size:var(--max-w-prose)}
li{margin-block:var(--s-1)}
.table-scroll{overflow-x:auto;-webkit-overflow-scrolling:touch;margin-block:var(--s-3) var(--s-5);border:1px solid var(--c-border-soft);border-radius:var(--r-md);background:var(--c-bg)}
table{border-collapse:collapse;inline-size:100%;font-size:var(--fz-sm);table-layout:auto;min-inline-size:max-content}
th,td{padding:var(--s-2) var(--s-3);border-block-end:1px solid var(--c-border-soft);text-align:start;vertical-align:top}
thead th{background:var(--c-bg-soft);font-weight:600;color:var(--c-fg);position:sticky;top:0}
tbody tr:hover{background:color-mix(in srgb,var(--c-accent-soft) 30%,transparent)}
caption{caption-side:top;text-align:start;font-size:var(--fz-sm);color:var(--c-fg-soft);padding-block:var(--s-2);font-style:italic}
code,pre,kbd,samp{font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:0.9em}
code{background:var(--c-bg-soft);padding:1px 5px;border-radius:var(--r-sm);color:var(--c-fg)}
pre{background:var(--c-bg-soft);padding:var(--s-3) var(--s-4);border-radius:var(--r-md);overflow-x:auto;line-height:1.5}
a{color:var(--c-link)}
a:hover{color:var(--c-link-hover)}
:focus-visible{outline:3px solid var(--c-focus);outline-offset:2px;border-radius:var(--r-sm)}
.skip-link{position:absolute;inset-block-start:-9999px;inset-inline-start:auto;width:1px;height:1px;overflow:hidden}
.skip-link:focus{position:fixed;inset-block-start:0;inset-inline-start:0;width:auto;height:auto;padding:var(--s-2) var(--s-4);background:var(--c-fg);color:var(--c-bg);font-size:var(--fz-sm);font-weight:600;z-index:9999;outline:2px solid var(--c-bg)}
.tag{display:inline-block;background:var(--c-tier-c-bg);color:var(--c-tier-c-fg);font-size:0.75rem;padding:2px 8px;border-radius:99px;margin-inline-end:6px;font-weight:500;letter-spacing:0.01em}
.tier-a{background:var(--c-tier-a-bg);color:var(--c-tier-a-fg)}
.tier-b{background:var(--c-tier-b-bg);color:var(--c-tier-b-fg)}
.tier-c{background:var(--c-tier-c-bg);color:var(--c-tier-c-fg)}
.verified{color:var(--c-accent);font-weight:600}
.l2-verified{color:var(--c-link);font-weight:500}
.inferred{color:var(--c-fg-soft);font-style:italic}
footer.site{border-block-start:1px solid var(--c-border);padding-block:var(--s-6);padding-inline:max(var(--s-5),env(safe-area-inset-left)) max(var(--s-5),env(safe-area-inset-right));color:var(--c-fg-muted);font-size:var(--fz-sm);max-inline-size:var(--max-w-wide);margin:var(--s-8) auto 0;line-height:1.7}
footer.site h3{margin-block-start:0;color:var(--c-fg);font-size:1rem;border:0;padding:0}
footer.site .grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:var(--s-5)}
footer.site a{color:var(--c-link)}
footer.site .colophon{margin-block-start:var(--s-5);padding-block-start:var(--s-3);border-block-start:1px solid var(--c-border-soft);font-size:0.78rem;color:var(--c-fg-soft)}
.kpi-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:var(--s-3);margin-block:var(--s-5)}
.kpi-grid .kpi{background:var(--c-bg-soft);padding:var(--s-3) var(--s-4);border-radius:var(--r-md);border:1px solid var(--c-border-soft)}
.kpi .num{font-size:1.625rem;font-weight:700;color:var(--c-accent);line-height:1.1;font-variant-numeric:tabular-nums}
.kpi .lbl{font-size:0.72rem;color:var(--c-fg-soft);text-transform:uppercase;letter-spacing:0.06em;margin-block-start:2px}
.persona-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:var(--s-3);margin-block:var(--s-5)}
.persona{background:var(--c-bg-soft);border:1px solid var(--c-border-soft);border-radius:var(--r-md);padding:var(--s-4);transition:border-color .15s}
.persona:hover{border-color:var(--c-accent)}
.persona h3{margin:0 0 var(--s-2);font-size:1rem;border:0;padding:0}
.persona p{margin-block:0 var(--s-2);font-size:var(--fz-sm)}
.persona a{font-weight:500;font-size:var(--fz-sm)}
.cite-widget{margin-block:var(--s-6);border:1px solid var(--c-border-soft);border-radius:var(--r-md);background:var(--c-bg-soft)}
.cite-widget summary{padding:var(--s-3) var(--s-4);font-weight:600;cursor:pointer;font-size:var(--fz-sm);color:var(--c-fg);list-style:none}
.cite-widget summary::-webkit-details-marker{display:none}
.cite-widget pre{margin:0;border-radius:0 0 var(--r-md) var(--r-md);font-size:0.78rem;background:var(--c-bg);border-block-start:1px solid var(--c-border-soft);white-space:pre-wrap;word-break:break-word}
.cite-widget .cite-tabs{padding:var(--s-2) var(--s-4);background:var(--c-bg);border-block-start:1px solid var(--c-border-soft);font-size:var(--fz-sm);color:var(--c-fg-muted)}
.cite-widget .cite-tabs strong{color:var(--c-fg)}
.show-more{margin-block:var(--s-3);border:1px solid var(--c-border-soft);border-radius:var(--r-md)}
.show-more summary{padding:var(--s-3) var(--s-4);cursor:pointer;font-size:var(--fz-sm);font-weight:600;color:var(--c-fg-muted);list-style:none}
.show-more summary::-webkit-details-marker{display:none}
.show-more summary::before{content:"+ ";color:var(--c-accent);font-weight:700}
.show-more[open] summary::before{content:"\\2212 "}
.banner{background:var(--c-tier-a-bg);color:var(--c-tier-a-fg);padding:var(--s-2) var(--s-4);border-radius:var(--r-md);font-size:var(--fz-sm);margin-block:var(--s-3);border:1px solid color-mix(in srgb,var(--c-tier-a-fg) 25%,transparent)}
.share-row{display:flex;flex-wrap:wrap;gap:var(--s-3);margin-block:var(--s-5);font-size:var(--fz-sm);color:var(--c-fg-soft);align-items:center}
.share-row a{color:var(--c-link);text-decoration:none}
.share-row a:hover{text-decoration:underline}
.section-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:var(--s-4);margin-block:var(--s-5)}
.section-grid .card{background:var(--c-bg-soft);padding:var(--s-4);border-radius:var(--r-md);border:1px solid var(--c-border-soft)}
.section-grid .card h3{margin-block-start:0;border:0;padding:0}
.section-grid .card .meta{font-size:var(--fz-sm);color:var(--c-fg-soft);margin-block:0 var(--s-2)}
abbr[title]{text-decoration:underline dotted;text-decoration-color:var(--c-fg-soft);text-underline-offset:2px;cursor:help}
time{font-variant-numeric:tabular-nums}
hr{border:0;border-block-start:1px solid var(--c-border-soft);margin-block:var(--s-6)}
blockquote{border-inline-start:3px solid var(--c-accent);padding-inline-start:var(--s-4);margin-inline:0;color:var(--c-fg-muted);font-style:italic}
@media (max-width:560px){
  header.nav nav{gap:0}
  .container{padding-block:var(--s-4) var(--s-7)}
  table{font-size:0.82rem}
  th,td{padding:var(--s-2)}
  .kpi .num{font-size:1.4rem}
  footer.site .grid{grid-template-columns:1fr}
}
@media (prefers-reduced-motion:reduce){
  *,*::before,*::after{animation-duration:0.01ms !important;transition-duration:0.01ms !important}
}
@media print{
  header.nav,footer.site .grid,.share-row,.cite-widget,.show-more,.banner,.skip-link{display:none}
  body{font-size:11pt;color:#000;background:#fff}
  .container{max-inline-size:100%;padding:0}
  h1,h2,h3{page-break-after:avoid}
  table,figure{page-break-inside:avoid}
  a[href^="http"]::after{content:" (" attr(href) ")";font-size:0.85em;color:#444;word-break:break-all}
  thead{display:table-header-group}
  tr{page-break-inside:avoid}
}
"""

# Primary nav — always visible. Keep small; ≥ 12 items wraps badly on mobile.
NAV_PRIMARY = [
    ("/", "Home"),
    ("/uzbekistan/", "Uzbekistan"),
    ("/kyrgyzstan/", "Kyrgyzstan"),
    ("/initiatives/", "Initiatives"),
    ("/donors/", "Donors"),
    ("/procurement/", "Procurement"),
]
# Secondary nav — collapsed under a "More ▾" disclosure.
NAV_SECONDARY = [
    ("/decrees/uz/", "Decrees UZ"),
    ("/decrees/kg/", "Decrees KG"),
    ("/institutions/", "Institutions"),
    ("/people/", "People"),
    ("/trends/", "Trends"),
    ("/mvp/", "Solo MVPs"),
    ("/methodology/", "Methodology"),
    ("/lenses/", "Lenses"),
    ("/scoring/", "Scoring"),
    ("/audit-team/", "Audit Team"),
    ("/honesty/", "Honesty"),
    ("/provenance/", "Provenance"),
]
# Backwards-compat: full list for breadcrumbs / sitemap consumers.
NAV_LINKS = NAV_PRIMARY + NAV_SECONDARY


def jsonld_graph(
    *, page_url: str, title: str, description: str, page_type: str, breadcrumbs: list[tuple[str, str]]
) -> str:
    site_id = SITE_URL + "/#website"
    org_id = SITE_URL + "/#organization"
    person_id = SITE_URL + "/#operator"
    page_id = page_url + "#" + page_type.lower()
    crumbs = [
        {
            "@type": "ListItem",
            "position": idx + 1,
            "name": name,
            "item": SITE_URL + path if path.startswith("/") else path,
        }
        for idx, (path, name) in enumerate(breadcrumbs)
    ]
    graph = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "Organization",
                "@id": org_id,
                "name": "Central Asia B2G Intelligence",
                "url": SITE_URL,
                "logo": SITE_URL + "/favicon.svg",
                "founder": {"@id": person_id},
                "sameAs": [OPERATOR_GITHUB, OPERATOR_LINKEDIN],
            },
            {
                "@type": "Person",
                "@id": person_id,
                "name": OPERATOR,
                "url": OPERATOR_GITHUB,
                "email": OPERATOR_EMAIL,
                "jobTitle": "B2G Market Research",
                "knowsAbout": [
                    "Central Asia", "B2G", "AI in government",
                    "Uzbekistan", "Kyrgyzstan", "digital procurement",
                    "donor-funded projects", "government technology",
                ],
                "sameAs": [OPERATOR_LINKEDIN, OPERATOR_GITHUB],
            },
            {
                "@type": "WebSite",
                "@id": site_id,
                "url": SITE_URL,
                "name": "Central Asia B2G Intelligence",
                "description": "AI/digital government opportunity research for Uzbekistan and Kyrgyzstan.",
                "publisher": {"@id": org_id},
                "inLanguage": "en",
            },
            {
                "@type": "BreadcrumbList",
                "itemListElement": crumbs,
            },
            {
                "@type": page_type,
                "@id": page_id,
                "url": page_url,
                "name": title,
                "headline": title,
                "description": description,
                "isPartOf": {"@id": site_id},
                "publisher": {"@id": org_id},
                "author": {"@id": person_id},
                "datePublished": TODAY,
                "dateModified": TODAY,
                "inLanguage": "en",
            },
        ],
    }
    return json.dumps(graph, ensure_ascii=False, indent=2)


def render_page(
    *,
    path: str,  # e.g. "/decrees/uz/" — must end with /
    title: str,
    description: str,
    body_html: str,
    page_type: str = "Article",
    breadcrumbs: list[tuple[str, str]] | None = None,
    country: str | None = None,
    extra_head: str = "",
) -> str:
    canonical = SITE_URL + path
    breadcrumbs = breadcrumbs or [("/", "Home")]
    if (path, title) not in breadcrumbs:
        breadcrumbs = breadcrumbs + [(path, title)]
    primary_parts = []
    for p, t in NAV_PRIMARY:
        aria = ' aria-current="page"' if p == path else ""
        primary_parts.append(f'<a href="{escape(_bp(p))}"{aria}>{escape(t)}</a>')
    secondary_parts = []
    secondary_active = False
    for p, t in NAV_SECONDARY:
        aria = ' aria-current="page"' if p == path else ""
        if p == path:
            secondary_active = True
        secondary_parts.append(f'<a href="{escape(_bp(p))}"{aria}>{escape(t)}</a>')
    open_attr = " open" if secondary_active else ""
    more_block = (
        f'<details class="nav-more"{open_attr}>'
        f'<summary aria-label="More navigation links">More <span aria-hidden="true">▾</span></summary>'
        f'<div class="nav-more-panel" role="group" aria-label="Secondary navigation">'
        + "".join(secondary_parts)
        + '</div></details>'
    )
    nav = "\n        ".join(primary_parts) + "\n        " + more_block
    # Visible breadcrumbs (skip on home)
    bc_html = ""
    if path != "/" and len(breadcrumbs) > 1:
        items = []
        for i, (bp, bn) in enumerate(breadcrumbs):
            if i == len(breadcrumbs) - 1:
                items.append(f'<li aria-current="page">{escape(bn)}</li>')
            else:
                items.append(f'<li><a href="{escape(_bp(bp))}">{escape(bn)}</a></li>')
        bc_html = (
            f'<nav class="breadcrumbs" aria-label="Breadcrumb">'
            f'<ol>{"".join(items)}</ol></nav>'
        )
    title_truncated = title if len(title) <= 60 else title[:57] + "..."
    desc_short = description if len(description) <= 160 else description[:157] + "..."
    country_meta = f'<meta name="country" content="{country}">' if country else ""
    body_with_bc = bc_html + body_html
    cite_widget = _cite_widget(canonical, title_truncated)
    share_row = _share_row(canonical, title_truncated)
    footer = _site_footer()
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{escape(title_truncated)}</title>
<meta name="description" content="{escape(desc_short)}">
<link rel="canonical" href="{escape(canonical)}">
<meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1">
<meta name="dateModified" content="{NOW_ISO}">
{country_meta}
<meta property="og:type" content="article">
<meta property="og:title" content="{escape(title_truncated)}">
<meta property="og:description" content="{escape(desc_short)}">
<meta property="og:url" content="{escape(canonical)}">
<meta property="og:image" content="{SITE_URL}/og-default.svg">
<meta property="og:site_name" content="Central Asia B2G Intelligence">
<meta property="og:locale" content="en_US">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{escape(title_truncated)}">
<meta name="twitter:description" content="{escape(desc_short)}">
<meta name="twitter:image" content="{SITE_URL}/og-default.svg">
<link rel="icon" href="{_bp('/favicon.svg')}" type="image/svg+xml">
<link rel="manifest" href="{_bp('/manifest.webmanifest')}">
<link rel="alternate" type="application/atom+xml" href="{_bp('/feed.xml')}" title="Central Asia B2G Intelligence">
<style>{CSS}</style>
{extra_head}
<script type="application/ld+json">
{jsonld_graph(page_url=canonical, title=title, description=desc_short, page_type=page_type, breadcrumbs=breadcrumbs)}
</script>
</head>
<body>
<a class="skip-link" href="#main-content">Skip to main content</a>
<header class="nav"><nav aria-label="Main navigation">
        <a href="{_bp('/') or '/'}" class="brand" aria-label="Central Asia B2G — home">Central Asia B2G</a>
        {nav}
      </nav></header>
<main id="main-content" class="container">
{body_with_bc}
{share_row}
{cite_widget}
</main>
{footer}
</body>
</html>
"""


def write_page(path_url: str, html_text: str) -> None:
    out = SITE / path_url.strip("/") / "index.html" if path_url not in ("/", "") else SITE / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html_text, encoding="utf-8")


# ────────────────────────────────────────────────────────────────────────────
# Reusable HTML components
# ────────────────────────────────────────────────────────────────────────────


_DATA_VINTAGE = TODAY[:7]


def _cite_widget(canonical: str, title: str) -> str:
    year = TODAY[:4]
    bibtex = (
        f"@misc{{valuev{year[2:]}cab2g,\n"
        f"  author = {{Valuev, Alexandr}},\n"
        f"  title  = {{Central Asia B2G Intelligence: {title}}},\n"
        f"  year   = {{{year}}},\n"
        f"  url    = {{{canonical}}},\n"
        f"  note   = {{Data vintage {_DATA_VINTAGE}, Apache 2.0}}\n"
        f"}}"
    )
    apa = (
        f"Valuev, A. ({year}). Central Asia B2G Intelligence: {title}. "
        f"Retrieved from {canonical}"
    )
    mla = (
        f'Valuev, Alexandr. "Central Asia B2G Intelligence: {title}." '
        f'Data vintage {_DATA_VINTAGE}, {canonical}.'
    )
    return f"""<details class="cite-widget">
<summary>Cite this research</summary>
<div class="cite-tabs"><strong>BibTeX</strong></div>
<pre>{escape(bibtex)}</pre>
<div class="cite-tabs"><strong>APA</strong> &nbsp; {escape(apa)}</div>
<div class="cite-tabs"><strong>MLA</strong> &nbsp; {escape(mla)}</div>
</details>"""


def _share_row(canonical: str, title: str) -> str:
    import urllib.parse as _u
    enc_url = _u.quote(canonical, safe="")
    enc_title = _u.quote(title, safe="")
    tw = f"https://twitter.com/intent/tweet?text={enc_title}&url={enc_url}"
    li = f"https://www.linkedin.com/sharing/share-offsite/?url={enc_url}"
    em = f"mailto:?subject={enc_title}&body={enc_url}"
    return (
        '<div class="share-row" role="navigation" aria-label="Share and follow">'
        f'<span>Share:</span>'
        f'<a href="{tw}" rel="noopener" target="_blank">X / Twitter</a>'
        f'<a href="{li}" rel="noopener" target="_blank">LinkedIn</a>'
        f'<a href="{em}">Email</a>'
        f'<span aria-hidden="true">·</span>'
        f'<a href="{_bp("/feed.xml")}">RSS feed</a>'
        f'<a href="https://github.com/avaluev/ca-b2g-research">GitHub repo</a>'
        '</div>'
    )


def _site_footer() -> str:
    return f"""<footer class="site">
<div class="grid">
  <div>
    <h3>About this research</h3>
    <p>An open knowledge graph of B2G AI and digital-government opportunities in
    Uzbekistan and Kyrgyzstan. Every claim is typed, sourced, and reproducible.
    Built by {OPERATOR}.</p>
    <p><a href="{_bp('/about/')}">About the author</a> · <a href="{_bp('/methodology/')}">Methodology</a> · <a href="{_bp('/honesty/')}">Honesty: what we did not find</a></p>
  </div>
  <div>
    <h3>Reproduce yourself</h3>
    <p>Clone the repository, follow the quickstart, and run the same eleven-agent
    pipeline. Total runtime ~10 hours, paid OpenRouter under USD 20.</p>
    <p><a href="https://github.com/avaluev/ca-b2g-research">github.com/avaluev/ca-b2g-research</a></p>
  </div>
  <div>
    <h3>Stay current</h3>
    <p>Quarterly refresh. Subscribe via the Atom feed or watch the GitHub repository for releases.</p>
    <p><a href="{_bp('/feed.xml')}">Atom feed</a> · <a href="https://github.com/avaluev/ca-b2g-research/releases">Releases</a> · <a href="https://github.com/avaluev/ca-b2g-research/issues/new">Found an error?</a></p>
  </div>
  <div>
    <h3>Contact</h3>
    <address style="font-style:normal">
      {OPERATOR}<br>
      <a href="mailto:{OPERATOR_EMAIL}">{OPERATOR_EMAIL}</a><br>
      <a href="{OPERATOR_LINKEDIN}">LinkedIn</a><br>
      <a href="{OPERATOR_GITHUB}">GitHub</a>
    </address>
  </div>
</div>
<div class="colophon">
  <p>Apache 2.0 licensed · Data vintage <time datetime="{TODAY}">{_DATA_VINTAGE}</time> · Built with Claude (Opus + Sonnet) on Anthropic and Perplexity Sonar Pro on OpenRouter · Last build {TODAY}</p>
</div>
</footer>"""


# ────────────────────────────────────────────────────────────────────────────
# Per-page rendering
# ────────────────────────────────────────────────────────────────────────────


def ru(text: str) -> str:
    """Wrap non-empty text in a Russian-language span (WCAG 3.1.2)."""
    if not text:
        return ""
    return f'<span lang="ru">{escape(text)}</span>'


_CYRILLIC_RE = re.compile(r"[Ѐ-ӿԀ-ԯ]+(?:[\s.,\-—:;\d№][Ѐ-ӿԀ-ԯ\d]+)*")


def auto_lang(text: str | None, lang: str = "ru") -> str:
    """Auto-wrap Cyrillic runs in <span lang="..."> for screen readers."""
    if not text:
        return ""
    s = escape(text)
    return _CYRILLIC_RE.sub(lambda m: f'<span lang="{lang}">{m.group(0)}</span>', s)


def render_table(
    headers: list[str],
    rows: list[str],
    *,
    caption: str | None = None,
    paginate_after: int | None = None,
    empty_msg: str = "No data yet.",
) -> str:
    """Render a semantic, scrollable, optionally paginated table.

    `rows` is a list of pre-rendered "<tr>...</tr>" strings.
    """
    if not rows:
        return f'<p>{escape(empty_msg)}</p>'
    head_html = "".join(f'<th scope="col">{h}</th>' for h in headers)
    cap = f"<caption>{escape(caption)}</caption>" if caption else ""
    if paginate_after and len(rows) > paginate_after:
        first = "".join(rows[:paginate_after])
        rest = "".join(rows[paginate_after:])
        body = (
            f"<tbody>{first}</tbody>"
            f"<tbody class='show-more-rows' hidden>{rest}</tbody>"
        )
        toggle = (
            f'<details class="show-more">'
            f'<summary>Show all {len(rows)} rows ({len(rows) - paginate_after} more)</summary>'
            f'<p style="padding:0 16px 12px;color:var(--c-fg-soft);font-size:var(--fz-sm)">'
            f'All {len(rows)} rows are present in the DOM for crawlers and remain in the source HTML; the rest are revealed when this section is expanded.</p>'
            f'</details>'
        )
        return (
            f'<div class="table-scroll">'
            f'<table>{cap}<thead><tr>{head_html}</tr></thead>'
            f'<tbody>{first}{rest}</tbody></table></div>{toggle}'
        )
    body = f"<tbody>{''.join(rows)}</tbody>"
    return (
        f'<div class="table-scroll">'
        f'<table>{cap}<thead><tr>{head_html}</tr></thead>{body}</table></div>'
    )


def kpi_row(label: str, value: str | int) -> str:
    return f'<div class="kpi" role="listitem"><div class="num">{escape(str(value))}</div><div class="lbl">{escape(label)}</div></div>'


def _md_inline(text: str) -> str:
    """Tiny inline markdown: **bold**, *italic*, `code`, [text](url)."""
    s = escape(text)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<![*\w])\*([^*]+)\*(?![\w*])", r"<em>\1</em>", s)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\[([^\]]+)\]\((https?://[^)]+)\)", r'<a href="\2">\1</a>', s)
    return s


def _md_to_html(md: str, *, skip_h1: bool = True) -> str:
    """Lightweight Markdown → HTML for our generated audit / lenses / rubric files.

    Handles: # h1 / ## h2 / ### h3, - / * bullet lists, numeric lists, paragraphs,
    horizontal rules, fenced code blocks, blockquotes, inline emphasis/links.
    """
    lines = md.replace("\r\n", "\n").split("\n")
    out: list[str] = []
    in_ul = in_ol = in_code = in_bq = False

    def close_lists() -> None:
        nonlocal in_ul, in_ol, in_bq
        if in_ul:
            out.append("</ul>")
            in_ul = False
        if in_ol:
            out.append("</ol>")
            in_ol = False
        if in_bq:
            out.append("</blockquote>")
            in_bq = False

    for raw in lines:
        line = raw.rstrip()
        if line.startswith("```"):
            close_lists()
            if not in_code:
                out.append("<pre><code>")
                in_code = True
            else:
                out.append("</code></pre>")
                in_code = False
            continue
        if in_code:
            out.append(escape(raw) + "\n")
            continue
        if not line.strip():
            close_lists()
            continue
        if re.match(r"^---+$|^\*\*\*+$", line.strip()):
            close_lists()
            out.append("<hr>")
            continue
        if skip_h1 and line.startswith("# "):
            continue
        m = re.match(r"^(#{1,6})\s+(.+)$", line)
        if m:
            close_lists()
            level = min(len(m.group(1)), 6)
            level = max(level, 2)  # never emit duplicate H1
            out.append(f"<h{level}>{_md_inline(m.group(2))}</h{level}>")
            continue
        if line.startswith("> "):
            if not in_bq:
                close_lists()
                out.append("<blockquote>")
                in_bq = True
            out.append(f"<p>{_md_inline(line[2:])}</p>")
            continue
        m = re.match(r"^[-*]\s+(.+)$", line)
        if m:
            if not in_ul:
                close_lists()
                out.append("<ul>")
                in_ul = True
            out.append(f"<li>{_md_inline(m.group(1))}</li>")
            continue
        m = re.match(r"^(\d+)\.\s+(.+)$", line)
        if m:
            if not in_ol:
                close_lists()
                out.append("<ol>")
                in_ol = True
            out.append(f"<li>{_md_inline(m.group(2))}</li>")
            continue
        # Plain paragraph
        close_lists()
        out.append(f"<p>{_md_inline(line)}</p>")
    close_lists()
    if in_code:
        out.append("</code></pre>")
    return "\n".join(out)


def home(graph: dict[str, Any]) -> str:
    n_inits = len(graph.get("initiatives", []) or [])
    n_decrees = len(graph.get("decrees", []) or [])
    n_inst = len(graph.get("institutions", []) or [])
    n_people = len(graph.get("people", []) or [])
    n_donors = len(graph.get("donor_programs", []) or [])
    n_tenders = len(graph.get("tenders", []) or [])
    n_trends = len(graph.get("trends", []) or [])
    n_cases = len(graph.get("global_cases", []) or [])
    n_mvps = len(graph.get("solopreneur_mvps", []) or [])
    tier_a = sum(1 for i in graph.get("initiatives", []) or [] if i.get("confidence_tier") == "A")

    # 40-60 word lead
    lead = (
        f"This open research catalogues {n_inits} deployable AI and digital-government "
        f"initiatives across Uzbekistan and Kyrgyzstan, scored on five axes and grounded "
        f"in {n_decrees} decrees, {n_inst} institutions, {n_people} decision-makers, "
        f"{n_donors} donor programmes, and {n_cases} global precedents. Every claim is typed, "
        f"verifiable, and cross-referenced. {tier_a} initiatives are rated Tier-A — deal-ready."
    )
    body = f"""<h1>Central Asia B2G Intelligence</h1>
<p class="lead summary">{escape(lead)}</p>
<div class="kpi-grid" role="list" aria-label="Headline counts">
{kpi_row("B2G initiatives", n_inits)}
{kpi_row("Tier-A deals", tier_a)}
{kpi_row("Solo MVPs", n_mvps)}
{kpi_row("Decrees", n_decrees)}
{kpi_row("Institutions", n_inst)}
{kpi_row("Decision-makers", n_people)}
{kpi_row("Donor programmes", n_donors)}
{kpi_row("Live tenders", n_tenders)}
{kpi_row("Global cases", n_cases)}
</div>

<div class="banner">
  <strong>April 2026 KG structural break:</strong> the Ministry of Digital Development was abolished and its functions transferred to the Presidential Administration (УДП). Every legacy donor programme counterpart is in flux through Q3 2026. <a href="{_bp('/decrees/kg/')}">See KG decrees</a>.
</div>

<h2>Where should you start?</h2>
<p>Pick the entry that matches what you do — each card lands you on the page that answers your first question.</p>
<div class="persona-grid" role="list" aria-label="Reader entry paths">
  <div class="persona" role="listitem">
    <h3>Vendor / B2G operator</h3>
    <p>Find Tier-A initiatives with verified buyer, decree anchor, donor co-financing, and a credible 12-month deal path.</p>
    <p><a href="{_bp('/initiatives/')}">→ Initiatives top 100</a> · <a href="{_bp('/procurement/')}">live procurement</a></p>
  </div>
  <div class="persona" role="listitem">
    <h3>Donor / IFI counterpart</h3>
    <p>{n_donors} active and pipeline programmes from World Bank, ADB, EU, UN agencies, and bilaterals — TTL or PM named on each.</p>
    <p><a href="{_bp('/donors/')}">→ Donor pipeline</a> · <a href="{_bp('/people/')}">decision-makers</a></p>
  </div>
  <div class="persona" role="listitem">
    <h3>Investor / VC</h3>
    <p>{n_mvps} solopreneur MVPs and {tier_a} Tier-A B2G initiatives, scored on five axes with local market fit and Russian/CIS substitution lenses.</p>
    <p><a href="{_bp('/mvp/')}">→ Solopreneur MVPs</a> · <a href="{_bp('/lenses/')}">analytical lenses</a></p>
  </div>
  <div class="persona" role="listitem">
    <h3>Government / regulator</h3>
    <p>How peers are deploying AI in courts, tax, health, and digital identity — with tournament-ranked transferability scores.</p>
    <p><a href="{_bp('/methodology/')}">→ Methodology</a> · <a href="{_bp('/honesty/')}">what we did not find</a></p>
  </div>
  <div class="persona" role="listitem">
    <h3>Researcher / journalist</h3>
    <p>Every prompt, every source URL, every audit finding is public. Reproduce the whole pipeline yourself for under USD 20 of paid API calls.</p>
    <p><a href="https://github.com/avaluev/ca-b2g-research">→ GitHub repository</a> · <a href="{_bp('/provenance/')}">provenance</a></p>
  </div>
</div>

<h2>What is in this research?</h2>
<p>A typed, source-cited knowledge graph of AI and digital government opportunities in Uzbekistan and Kyrgyzstan, plus the methodology used to build it. Each initiative is mapped to a specific decree, institution, decision-maker, donor programme, and global precedent. Numeric claims carry a verified URL; uncertain claims are tagged <code>L2_VERIFIED</code> or <code>INFERRED</code> rather than dropped.</p>

<h2>How was it produced?</h2>
<p>An eleven-agent multi-wave pipeline built on Claude (Opus + Sonnet) with cross-model verification via Perplexity Sonar Deep Research on a strict USD 20 OpenRouter budget. The seven waves move from blueprint to legal corpus to institutions, donors, procurement, trends, people, synthesis, adversarial audit, and outreach. The audit wave caught four wrong Tier-1 identities before publication; corrections are public.</p>

<h2>Who built this?</h2>
<p>{escape(OPERATOR)} — independent researcher focused on B2G market intelligence in Central Asia. Reachable at <a href="mailto:{OPERATOR_EMAIL}">{OPERATOR_EMAIL}</a> · <a href="{OPERATOR_LINKEDIN}">LinkedIn</a> · <a href="{OPERATOR_GITHUB}">GitHub</a>. The full prompt set, agent definitions, and source code are <a href="https://github.com/avaluev/ca-b2g-research">openly licensed under Apache 2.0</a>.</p>
"""
    return render_page(
        path="/",
        title="Central Asia B2G Intelligence — Uzbekistan + Kyrgyzstan AI/Digital Government",
        description="Open research on B2G AI and digital-government opportunities in Uzbekistan + Kyrgyzstan: 100+ initiatives mapped to decrees, donors, decision-makers, and precedents.",
        body_html=body,
        page_type="CollectionPage",
        extra_head=_faq_jsonld_home() + _dataset_jsonld() + _speakable_jsonld(),
    )


def _faq_jsonld_home() -> str:
    """FAQPage schema for the home page Q&A sections."""
    faq = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": "What is in this research?",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": (
                        "A typed, source-cited knowledge graph of AI and digital government "
                        "opportunities in Uzbekistan and Kyrgyzstan. Every initiative is mapped "
                        "to a decree, an institution, a decision-maker, a donor programme, and "
                        "a global precedent. Every numeric claim is cited."
                    ),
                },
            },
            {
                "@type": "Question",
                "name": "How was the Central Asia B2G research produced?",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": (
                        "An eleven-agent multi-wave research pipeline built on Anthropic's Claude "
                        "(Opus and Sonnet) with cross-model verification via Perplexity Sonar Deep "
                        "Research and Sonar Pro on a strict $20 OpenRouter budget. Seven waves move "
                        "from blueprint to legal corpus to institutions, donors, procurement, trends, "
                        "people, synthesis, audit, and outreach."
                    ),
                },
            },
            {
                "@type": "Question",
                "name": "Who is the Central Asia B2G Intelligence research for?",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": (
                        "B2G operators, government affairs leads at vendors, donor counterparts, "
                        "investment teams covering frontier emerging markets, and Central-Asian "
                        "government decision-makers. Primary sources are predominantly Russian-language."
                    ),
                },
            },
            {
                "@type": "Question",
                "name": "Where should a B2G operator start with this research?",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": (
                        "Start with the Initiatives page for the headline list of 100 deployable "
                        "opportunities. Read the five lenses for the analytical frame. Read Honesty "
                        "for gaps — gaps are first-class records here. Provenance shows every "
                        "source and cross-model verification card."
                    ),
                },
            },
        ],
    }
    return f'\n<script type="application/ld+json">\n{json.dumps(faq, ensure_ascii=False, indent=2)}\n</script>'


def _dataset_jsonld() -> str:
    """Dataset schema pointing at the public knowledge graph JSON."""
    dataset = {
        "@context": "https://schema.org",
        "@type": "Dataset",
        "name": "Central Asia B2G Knowledge Graph",
        "description": (
            "Typed knowledge graph of AI and digital government opportunities in Uzbekistan "
            "and Kyrgyzstan: decrees, institutions, decision-makers, donor programmes, "
            "procurement tenders, sectoral trends, global precedents, and scored initiatives."
        ),
        "url": "https://github.com/avaluev/ca-b2g-research",
        "license": "https://www.apache.org/licenses/LICENSE-2.0",
        "creator": {"@id": SITE_URL + "/#operator"},
        "dateModified": TODAY,
        "inLanguage": ["en", "ru"],
        "keywords": [
            "Uzbekistan", "Kyrgyzstan", "B2G", "AI government", "digital procurement",
            "Central Asia", "knowledge graph", "open data",
        ],
        "distribution": [
            {
                "@type": "DataDownload",
                "encodingFormat": "application/json",
                "contentUrl": "https://github.com/avaluev/ca-b2g-research/blob/main/state/knowledge_graph.json",
            }
        ],
    }
    return f'\n<script type="application/ld+json">\n{json.dumps(dataset, ensure_ascii=False, indent=2)}\n</script>'


def _speakable_jsonld() -> str:
    """SpeakableSpecification — tells Google Assistant which selectors to read aloud."""
    speakable = {
        "@context": "https://schema.org",
        "@type": "WebPage",
        "speakable": {
            "@type": "SpeakableSpecification",
            "cssSelector": ["h1", ".lead.summary"],
        },
        "url": SITE_URL + "/",
    }
    return f'\n<script type="application/ld+json">\n{json.dumps(speakable, ensure_ascii=False, indent=2)}\n</script>'


def methodology() -> str:
    waves_rows = [
        ("<tr><td><strong>0</strong></td><td>blueprint-architect</td><td>Strategic plan, target lists, and the constraint inventory that scaffolds every later wave.</td></tr>"),
        ("<tr><td><strong>1</strong></td><td>legal-cartographer · case-tournament</td><td>Catalogue the decree corpus on lex.uz and cbd.minjust.gov.kg; tournament 100 global precedents for transferability to UZ and KG.</td></tr>"),
        ("<tr><td><strong>2</strong></td><td>institution-mapper · donor-pipeline · procurement-harvester · trend-triangulator</td><td>Map state bodies (8 tiers), donor programmes with named TTL, live tenders, sector trends.</td></tr>"),
        ("<tr><td><strong>3</strong></td><td>people-intelligence</td><td>100+ decision-makers, including the 16 diaspora bridges who shape policy from London, Dubai, and Silicon Valley.</td></tr>"),
        ("<tr><td><strong>4</strong></td><td>initiative-synthesizer · solopreneur-mvp-synthesizer</td><td>100 institutional B2G initiatives plus 200 solopreneur MVPs, scored on five weighted axes.</td></tr>"),
        ("<tr><td><strong>5</strong></td><td>reflexion-auditor</td><td>Adversarial re-verification with a different model, minimum three HIGH-severity issues, public corrections.</td></tr>"),
        ("<tr><td><strong>6</strong></td><td>pitch-artificer</td><td>Tier-A and Tier-B outreach bundles. Private outreach scripts stay in the contributor vault.</td></tr>"),
    ]
    waves_table = render_table(["Wave", "Agent(s)", "Purpose"], waves_rows, caption="The seven waves of the research pipeline")
    body = f"""<h1>Methodology</h1>
<p class="lead summary">A seven-wave multi-agent pipeline turns Russian, Uzbek, and Kyrgyz primary sources into a typed knowledge graph. Eleven specialised agents work in three parallel research waves, one synthesis wave, one adversarial audit, and one outreach wave. Cross-model verification on a strict twenty-dollar OpenRouter budget keeps every Tier-A claim independently re-checked.</p>
<h2>What does each wave do?</h2>
<p>Each wave produces a typed JSON artefact under <code>state/</code>. Every record carries a verification tag and a sources array. The merged knowledge graph at <code>state/knowledge_graph.json</code> is the single read view that downstream waves consume.</p>
{waves_table}
<h2>How is verification enforced?</h2>
<p>Every record carries one of six verification tags: <span class="verified">VERIFIED</span> (primary source plus one corroboration), <span class="l2-verified">L2_VERIFIED</span> (primary source only), L3_VERIFIED (primary plus expert commentary), <span class="inferred">INFERRED</span> (indirect evidence), UNVERIFIED, or CONTRADICTED. The reflexion-auditor calls a different model than the original agent — Sonar Pro re-checks Sonar Deep Research output, breaking the echo chamber. Twelve content quality gates block any deploy on a single H1 violation, internal ID leak, fabricated decree, or fabricated LinkedIn URL.</p>
<h2>What is the source priority?</h2>
<p>Uzbekistan: lex.uz, gov.uz, president.uz, norma.uz, then spot.uz, gazeta.uz, kun.uz, daryo.uz. Kyrgyzstan: cbd.minjust.gov.kg, president.kg, gov.kg, kabmin.kg, then 24.kg, kaktus.media, akipress.org. Donors: documents.worldbank.org, projects.worldbank.org, adb.org/projects, ec.europa.eu/international-partnerships. Every country claim cites at least one Russian-language source. Fifty-three percent of all sources in this run are Russian-language.</p>
<h2>Reproduce this research yourself</h2>
<p>The full pipeline is open-source. Clone <a href="https://github.com/avaluev/ca-b2g-research">github.com/avaluev/ca-b2g-research</a>, copy <code>.env.example</code> to <code>.env</code> and add your OpenRouter key, then run <code>make run</code>. Total runtime: about ten hours wall-clock. Total OpenRouter spend (with the audit wave on paid Sonar Pro): under twenty dollars. Anthropic Claude usage runs on your own subscription.</p>
"""
    howto = {
        "@context": "https://schema.org",
        "@type": "HowTo",
        "name": "How to run the Central Asia B2G research pipeline",
        "description": "Seven-wave eleven-agent pipeline for mapping AI/digital government opportunities in Uzbekistan and Kyrgyzstan.",
        "step": [
            {"@type": "HowToStep", "position": 1, "name": "Wave 0 — Blueprint", "text": "blueprint-architect: strategic plan, target lists, constraint inventory"},
            {"@type": "HowToStep", "position": 2, "name": "Wave 1 — Legal + Cases", "text": "legal-cartographer maps decree corpus; case-tournament harvests 100+ global precedents"},
            {"@type": "HowToStep", "position": 3, "name": "Wave 2 — Institutions, Donors, Procurement, Trends", "text": "Four parallel agents: institution-mapper, donor-pipeline, procurement-harvester, trend-triangulator"},
            {"@type": "HowToStep", "position": 4, "name": "Wave 3 — People", "text": "people-intelligence: 100+ decision-makers + diaspora bridges"},
            {"@type": "HowToStep", "position": 5, "name": "Wave 4 — Synthesis", "text": "initiative-synthesizer: 100+ initiatives, 5-axis scoring"},
            {"@type": "HowToStep", "position": 6, "name": "Wave 5 — Adversarial Audit", "text": "reflexion-auditor: cross-model re-verification, minimum 3 HIGH issues"},
            {"@type": "HowToStep", "position": 7, "name": "Wave 6 — Outreach", "text": "pitch-artificer: Tier-A/B outreach bundles (private vault)"},
        ],
    }
    howto_ld = f'\n<script type="application/ld+json">\n{json.dumps(howto, ensure_ascii=False, indent=2)}\n</script>'
    return render_page(
        path="/methodology/",
        title="Methodology",
        description="The seven-wave eleven-agent research pipeline behind Central Asia B2G Intelligence.",
        body_html=body,
        page_type="Article",
        extra_head=howto_ld,
    )


def lenses_page(lenses_md: str) -> str:
    head = (
        '<h1>The six analytical lenses</h1>'
        '<p class="lead summary">Six lenses cut across every record in this research: the Karimov-to-Mirziyoyev Inversion in Uzbekistan, the Japarov Concentration in Kyrgyzstan, the Decree Half-Life that opens six-to-eighteen month implementation windows, Donor Co-Financing behind sixty to ninety percent of digital budgets, the Diaspora Bridge of senior advisors, and the Russian/CIS Substitution Window opened by post-2022 vendor retreat.</p>'
    )
    return render_page(
        path="/lenses/",
        title="Six analytical lenses on Central Asia B2G",
        description="Six lenses applied to every record in this research: Karimov Inversion, Japarov Concentration, Decree Half-Life, Donor Co-Financing, Diaspora Bridge, Russian/CIS Substitution.",
        body_html=head + _md_to_html(lenses_md, skip_h1=True),
    )


def scoring_page(rubric_md: str) -> str:
    rubric_rows = [
        '<tr><td><strong>Speed-to-Contract</strong></td><td>25%</td><td>How quickly can a vendor reach signature given decree status, procurement modality, and incumbent landscape?</td></tr>',
        '<tr><td><strong>Strategic Moat</strong></td><td>20%</td><td>Does winning this contract pre-position you for a much larger downstream play?</td></tr>',
        '<tr><td><strong>Defensibility</strong></td><td>20%</td><td>Once deployed, how protected from competitor displacement (data accumulation, regulatory pre-qualification, language model fine-tune)?</td></tr>',
        '<tr><td><strong>Capital Access</strong></td><td>20%</td><td>Is funding identified — donor programme, ministry budget line, or PPP — and credibly close to disbursement?</td></tr>',
        '<tr><td><strong>Russian / CIS Fit</strong></td><td>15%</td><td>Does the solution match local language, data localization, and post-2022 vendor preference dynamics?</td></tr>',
    ]
    rubric_table = render_table(["Axis", "Weight", "What it measures"], rubric_rows, caption="The five scoring axes")
    tier_rows = [
        '<tr><td><span class="tag tier-a">A</span></td><td>≥ 7.5</td><td>Deal-ready. All key reference fields verified. Twelve-month deal path documented.</td></tr>',
        '<tr><td><span class="tag tier-b">B</span></td><td>≥ 6.0</td><td>Develop. Most fields VERIFIED or L2_VERIFIED. One or two gaps to close before pursuit.</td></tr>',
        '<tr><td><span class="tag tier-c">C</span></td><td>≥ 4.5</td><td>Backlog. Significant gaps or weak verification. Revisit on next refresh.</td></tr>',
        '<tr><td>D</td><td>&lt; 4.5</td><td>Reconsider — usually dropped from the list entirely.</td></tr>',
    ]
    tier_table = render_table(["Tier", "Weighted total", "Treatment"], tier_rows, caption="Tier mapping for B2G initiatives")
    head = (
        '<h1>Scoring rubric</h1>'
        '<p class="lead summary">Every initiative is scored on five weighted axes: Speed-to-Contract (25%), Strategic Moat (20%), Defensibility (20%), Capital Access (20%), and Russian/CIS Fit (15%). A weighted total of 7.5 or more puts an initiative in Tier-A — deal-ready with every reference field verified. Below 6.0 is Tier-C or worse.</p>'
        '<h2>The five axes</h2>'
        + rubric_table +
        '<h2>Tier mapping</h2>'
        + tier_table +
        '<h2>Why these weights?</h2>'
        '<p>Speed-to-Contract is weighted highest because in B2G the largest losses come from chasing slow opportunities. Russian/CIS Fit is weighted lowest because it is necessary but not sufficient — a poor fit kills a deal but a good fit alone does not win one. The other three axes are weighted equally because they trade off against one another in real bid decisions.</p>'
    )
    rest = _md_to_html(rubric_md, skip_h1=True)
    return render_page(
        path="/scoring/",
        title="Five-axis scoring rubric for B2G initiatives",
        description="The weighted scoring rubric for every initiative: Speed-to-Contract, Strategic Moat, Defensibility, Capital Access, Russian/CIS Fit.",
        body_html=head + '<h2>Detailed axis definitions</h2>' + rest,
    )


def about_page() -> str:
    body = f"""<h1>About this research and its author</h1>
<p class="lead summary">{escape(OPERATOR)} built this research as an open, reproducible alternative to the Big-4 frontier-market opportunity reports that cost six figures and disappear into a PDF. Every prompt, every script, every quality gate is public. Every claim is typed. Every error is named.</p>

<h2>Who is the author?</h2>
<p>{escape(OPERATOR)} is an independent researcher focused on B2G market intelligence in Central Asia. Reachable at <a href="mailto:{OPERATOR_EMAIL}">{OPERATOR_EMAIL}</a> · <a href="{OPERATOR_LINKEDIN}">LinkedIn</a> · <a href="{OPERATOR_GITHUB}">GitHub</a>.</p>

<h2>Why build this?</h2>
<p>Standard B2G consultancies tell you "the Ministry of Digital Development is leading AI strategy" — useless for capture. This site tells you the deputy minister responsible for AI procurement, their LinkedIn, the donor programme co-financing their pipeline, the decree authorising their budget, the half-life remaining on that decree, the closest global precedent, and the named pitch hook that maps to their published commitment. And when something is wrong, the <a href="{_bp('/honesty/')}">Honesty page</a> says so.</p>

<h2>How is this different from a Big-4 report?</h2>
<ul>
  <li><strong>Open.</strong> Apache 2.0. Clone, fork, rerun.</li>
  <li><strong>Typed.</strong> Eight record types with foreign-key integrity. The data is a knowledge graph, not a stack of slides.</li>
  <li><strong>Reproducible.</strong> Total runtime ten hours, total paid OpenRouter under twenty dollars. The pipeline is one <code>make run</code> away.</li>
  <li><strong>Adversarial.</strong> Wave 5 finds at least three HIGH-severity issues. In this run it caught four wrong Tier-1 identities — corrected, sourced, and named in <a href="{_bp('/honesty/')}">Honesty</a>.</li>
  <li><strong>Localised.</strong> Fifty-three percent of sources are Russian-language. Cyrillic content carries proper <code>lang</code> attribution.</li>
</ul>

<h2>What is the refresh cadence?</h2>
<p>Quarterly. Each refresh re-runs Waves 1, 2, and 5 and incrementally extends Waves 3, 4, and 6. Releases are tagged on GitHub with the data vintage. Subscribe to the <a href="{_bp('/feed.xml')}">Atom feed</a> or watch the repository for releases.</p>

<h2>How can I help?</h2>
<p>Open an issue with a <a href="https://github.com/avaluev/ca-b2g-research/issues/new?template=research-correction.md">research correction</a> if you spot wrong data — wrong decree number, stale role, missing donor programme. Open a PR if you want to extend the schema, add an agent, or improve a renderer. Both are welcome.</p>

<h2>Privacy and ethics</h2>
<p>This site never publishes private contact details — phone numbers, home addresses, personal email — for any named individual. It never speculates on political loyalties; only documented public positions. The private outreach kits with warm-intro paths and diaspora-flagged advisors live only in a contributor vault, not on the public site.</p>

<h2>Funding and conflicts of interest</h2>
<p>This research is self-funded. {escape(OPERATOR)} has no current vendor or donor mandate dependent on its findings. The site lists no advertising and accepts no sponsorship.</p>
"""
    return render_page(
        path="/about/",
        title=f"About {OPERATOR} and this research",
        description=f"{OPERATOR} built this open research alternative to Big-4 frontier-market reports. Apache 2.0, reproducible in 10h for under USD 20.",
        body_html=body,
        page_type="AboutPage",
    )


def audit_team_page() -> str:
    specialists = [
        ("01", "Reference Benchmarker", "Score the audit site vs the padel-market-analysis reference dimension-by-dimension; identify copyable patterns and structural advantages.", "01_reference_benchmark"),
        ("02", "Information Architect", "Audit nav, hierarchy, breadcrumbs, internal-link graph, and scent of information across all rendered pages.", "02_information_architecture"),
        ("03", "Content Voice Editor", "Plain English, anti-jargon, third-person professional, Flesch-Kincaid grade ≤ 10. No marketing badges, no hedging fluff.", "03_voice_edit"),
        ("04", "Citation / Provenance", "Every numeric claim and named entity traceable to a source. Russian / Uzbek / Kyrgyz share ≥ 30%. Dead-link health.", "04_citations"),
        ("05", "GEO / AIO / AEO / LLMO", "Maximise discoverability for ChatGPT Search, Claude, Perplexity, Gemini, AI Overviews. llms.txt, JSON-LD @graph, FAQPage, HowTo, Dataset schemas.", "05_geo_aio_aeo_llmo"),
        ("06", "Visual / Typography", "Beautiful, calm, scannable typography. Fluid type scale, 60–80ch line length, WCAG AA contrast, whitespace rhythm.", "06_visual_typography"),
        ("07", "Mobile-First QA", "Flawless on a 320 px iPhone SE. Tap targets ≥ 44 px (WCAG 2.5.5), no horizontal scroll, hamburger nav, card layout for narrow viewports.", "07_mobile"),
        ("08", "Accessibility (WCAG 2.2 AA)", "Skip-link, focus-visible, scope=col, lang attribution, semantic HTML5. Screen-reader-friendly + keyboard-only parity.", "08_accessibility"),
        ("09", "Performance Engineer", "Core Web Vitals green: LCP < 1.5 s, FCP < 0.4 s, CLS < 0.05, INP < 100 ms. Lighthouse Performance ≥ 97.", "09_performance"),
        ("10", "HTML Code Quality", "Semantic HTML5, W3C-validating, proper landmark structure. thead / tbody / scope=col, abbr, time, cite, figure.", "10_html_quality"),
        ("11", "CSS Architect", "Custom properties, fluid clamp() type, logical properties, prefers-color-scheme dark mode, prefers-reduced-motion, complete print stylesheet.", "11_css"),
        ("12", "Data Visualization", "Charts that justify their existence. Sortable tables ≥ 10 rows. Inline SVG. No chartjunk.", "12_dataviz"),
        ("13", "Trust & Brand", "Establish trust at first scroll. Distinguish from generic SEO content farms and Big-4 boilerplate. Author surface, license badge, methodology openness, ethics statement.", "13_trust_brand"),
        ("14", "Conversion / CTA", "Every page has ONE primary action (≤ 2 secondary). Persona-specific routing. Cite-this-research widget. Privacy-respecting share row.", "14_conversion"),
        ("15", "Internationalization", "Cyrillic content renders correctly, is searchable, and screen-reader-friendly with proper lang= attribution. Hreflang for any /ru/ mirror pages.", "15_i18n"),
        ("16", "Dev-Ex / Reproducibility", "Anyone can clone the repo and reproduce or extend. README clarity, mermaid architecture, CI badges, CONTRIBUTING, issue templates, citation file.", "16_devex"),
    ]
    cards_html = "\n".join(
        f'''<div class="persona" role="listitem">
            <h3>{escape(num)} · {escape(name)}</h3>
            <p class="meta">Specialist mandate</p>
            <p>{escape(desc)}</p>
            <p>
              <a href="https://github.com/avaluev/ca-b2g-research/blob/main/.claude/audit-team/{escape(num)}_{slugify(name).replace("-", "_")}.md">Dispatch prompt</a>
              · <a href="https://github.com/avaluev/ca-b2g-research/blob/main/state/audit/team/{escape(slug)}.md">Audit report</a>
            </p>
          </div>'''
        for num, name, desc, slug in specialists
    )

    body = f"""<h1>Auditor AI Team</h1>
<p class="lead summary">After every release, sixteen specialist sub-agents audit the live site in parallel. Each scores its own dimension one to ten and ships pasteable patches with priorities P0, P1, or P2. Every dispatch prompt is public. Every audit report is public. The pipeline that produces the data is reviewed by a separate pipeline that critiques the rendering.</p>

<h2>Why a 16-specialist team?</h2>
<p>A single reviewer always misses dimensions outside their lane. A research site serves vendors, donors, investors, government officials, journalists, contributors, and AI search crawlers — each judges different things. The specialists below are organised so each pair of dimensions has at least one dedicated auditor.</p>

<h2>What did the audit catch in v1.0.0?</h2>
<ul>
  <li>17 HIGH severity issues + 16 MEDIUM + 2 LOW.</li>
  <li>Four wrong Tier-1 identities (IT Park UZ CEO, KG UDP head, KG Min Health, KG last Минцифры minister) — caught by paid Sonar Pro re-verification, corrected before publication.</li>
  <li>WCAG contrast failure (#00aa44 at 2.89:1) before audit; replaced with #005c27 at 4.5:1 after.</li>
  <li>OG image referenced .png but only .svg existed — every social share card was broken until this audit caught it.</li>
  <li>169 Cyrillic cells without lang= attribution; auto-wrapped via the new ru() helper.</li>
  <li>Nav buried H1 below the fold at 320 px — fixed with a CSS-only hamburger pattern and tap targets ≥ 44 px.</li>
</ul>

<h2>The team</h2>
<p>Each card links to the dispatch prompt (so you can re-run any specialist yourself) and the actual audit report it produced.</p>
<div class="persona-grid" role="list" aria-label="The 16 audit specialists">
{cards_html}
</div>

<h2>How to re-run the full audit</h2>
<p>The audit dispatches 16 Claude sub-agents in parallel using <code>subagent_type=general-purpose</code> and <code>run_in_background=true</code>. Total wall-clock per pass: about 30 minutes. Anthropic spend on Sonnet: about USD 4–8. Zero paid OpenRouter calls — the audit team reads only the public web and local files.</p>
<pre><code># 1. Fan out 16 specialists in parallel from a single Claude Code session:
for spec in .claude/audit-team/*.md; do
  echo "Dispatch: $spec"
done
# 2. Each writes to state/audit/team/&lt;NN&gt;_*.md
# 3. Synthesise, apply patches, re-render, re-deploy</code></pre>

<h2>Where do the prompts live?</h2>
<p>Two mirrored locations — Claude Code agent specs at <a href="https://github.com/avaluev/ca-b2g-research/tree/main/.claude/audit-team"><code>.claude/audit-team/</code></a> and a public flat-file index at <a href="https://github.com/avaluev/ca-b2g-research/tree/main/prompts/audit-team"><code>prompts/audit-team/</code></a>. The actual reports live at <a href="https://github.com/avaluev/ca-b2g-research/tree/main/state/audit/team"><code>state/audit/team/</code></a>.</p>
"""
    return render_page(
        path="/audit-team/",
        title="Auditor AI Team — 16 specialists",
        description="Sixteen specialist Claude sub-agents audit the live site in parallel after every release. Every dispatch prompt and every audit report is public.",
        body_html=body,
        page_type="CollectionPage",
    )


def not_found_page() -> str:
    body = """<h1>Page not found</h1>
<p class="lead summary">The link you followed does not match any page in the Central Asia B2G Intelligence research site. The site is organised around six pillar pages plus the methodology, lenses, scoring rubric, and an honesty page that names what we did not find.</p>

<h2>Where to start instead</h2>
<ul>
  <li><a href="{_bp('/')}">Home</a> — the headline counts and where to start by reader type.</li>
  <li><a href="{_bp('/initiatives/')}">B2G initiatives</a> — the top 100 deployable opportunities, tier-bucketed.</li>
  <li><a href="{_bp('/mvp/')}">Solopreneur MVPs</a> — 200 individually-bootstrappable plays.</li>
  <li><a href="{_bp('/donors/')}">Donor pipeline</a> — 49 active programmes with named TTL/PM.</li>
  <li><a href="{_bp('/methodology/')}">Methodology</a> — how the seven-wave pipeline works.</li>
  <li><a href="{_bp('/honesty/')}">Honesty</a> — what we did not find and where the audit caught us.</li>
</ul>

<p>If you found this 404 from a broken link inside the site, please <a href="https://github.com/avaluev/ca-b2g-research/issues/new">open an issue</a>.</p>
"""
    return render_page(
        path="/404.html",
        title="Page not found",
        description="The page you requested does not exist. Try the home page or one of the six pillar pages.",
        body_html=body,
        page_type="WebPage",
    )


def decrees_page(graph: dict[str, Any], country: str) -> str:
    decrees = [d for d in graph.get("decrees", []) or [] if d.get("country") == country]
    decrees = sorted(decrees, key=lambda d: d.get("date") or "", reverse=True)
    n = len(decrees)
    active = sum(1 for d in decrees if d.get("half_life_status") == "active_window")
    cname = "Uzbekistan" if country == "UZ" else "Kyrgyzstan"
    rows = []
    for d in decrees:
        sources = d.get("sources") or []
        src = sources[0] if sources else None
        link_html = (
            f'<a href="{escape(src.get("url"))}">primary source</a>' if src and src.get("url") else "—"
        )
        rows.append(
            f"<tr><td>{escape(d.get('id') or '')}</td><td>{escape(d.get('decree_type') or '')}</td>"
            f"<td>{ru(d.get('number') or '')}</td><td>{escape(d.get('date') or '')}</td>"
            f"<td>{escape(d.get('title_en') or '')}</td>"
            f"<td><span class='tag'>{escape(d.get('half_life_status') or '')}</span></td>"
            f"<td>{link_html}</td></tr>"
        )
    table = render_table(
        ["ID", "Type", "Number", "Date", "Title", "Status", "Source"],
        rows,
        paginate_after=25,
        empty_msg="No decrees in the knowledge graph yet.",
    )
    body = f"""<h1>Decree atlas — {cname}</h1>
<p class="lead summary">This atlas catalogues {n} presidential decrees, government resolutions, and sectoral laws shaping AI and digital government in {cname}, with {active} currently in their six-to-eighteen-month active implementation window. Every decree is verified on the official government source and cross-checked in independent media.</p>
<h2>What is the decree half-life?</h2>
<p>The decree half-life lens identifies decrees in their 6–18 month implementation window — the period when ministries are actively procuring under that authority. Decrees outside this window are either expired, superseded, or merely aspirational.</p>
<h2>Decrees</h2>
{table}
"""
    return render_page(
        path=f"/decrees/{country.lower()}/",
        title=f"{cname} — Decree Atlas",
        description=f"Decrees and resolutions on AI and digital government in {cname}, with implementation half-life status.",
        body_html=body,
        country=country,
    )


def institutions_page(graph: dict[str, Any]) -> str:
    insts = graph.get("institutions", []) or []
    n = len(insts)
    rows = []
    for i in sorted(insts, key=lambda x: (x.get("country") or "", x.get("tier") or 99)):
        head_id = i.get("head_person_id") or ""
        rows.append(
            f"<tr><td>{escape(i.get('country') or '')}</td><td>{escape(str(i.get('tier') or ''))}</td>"
            f"<td>{escape(i.get('name_en') or '')}</td>"
            f"<td>{ru(i.get('name_ru') or '')}</td>"
            f"<td>{escape(i.get('ai_digital_mandate') or '')}</td>"
            f"<td>{escape(head_id)}</td></tr>"
        )
    table = render_table(
        ["Country", "Tier", "Name (EN)", "Name (RU)", "AI/digital mandate", "Head"],
        rows,
        paginate_after=30,
        empty_msg="No institutions in the knowledge graph yet.",
    )
    body = f"""<h1>Institution map</h1>
<p class="lead summary">This map covers {n} state institutions across Uzbekistan and Kyrgyzstan with AI or digital mandate, organised in eight tiers from Presidential Administration through Cabinet, line ministries, agencies, SOEs, regulators, working groups, and donor PIUs. Every institution names its current head, parent, and recent decisions.</p>
<h2>What are the eight tiers?</h2>
<ol>
<li>Presidential Administration</li>
<li>Cabinet</li>
<li>Line ministries</li>
<li>State committees, agencies, authorities</li>
<li>Digital infrastructure SOEs</li>
<li>Regulators</li>
<li>Commissions, councils, working groups</li>
<li>Donor-embedded Project Implementation Units (PIUs)</li>
</ol>
<h2>Institutions</h2>
{table}
"""
    return render_page(
        path="/institutions/",
        title="Institution map (UZ + KG)",
        description="Eight-tier institution taxonomy covering AI/digital state bodies in Uzbekistan and Kyrgyzstan.",
        body_html=body,
    )


def donors_page(graph: dict[str, Any]) -> str:
    progs = graph.get("donor_programs", []) or []
    n = len(progs)
    rows = []
    for p in sorted(progs, key=lambda x: x.get("total_budget_usd") or 0, reverse=True):
        rows.append(
            f"<tr><td>{escape(p.get('donor') or '')}</td><td>{escape(p.get('country') or '')}</td>"
            f"<td>{escape(p.get('program_name') or '')}</td>"
            f"<td>${(p.get('total_budget_usd') or 0):,.0f}</td>"
            f"<td>{escape(p.get('ttl_pm_name') or '')}</td>"
            f"<td>{escape(p.get('status') or '')}</td></tr>"
        )
    table = render_table(
        ["Donor", "Country", "Programme", "Budget", "TTL / Project manager", "Status"],
        rows,
        paginate_after=25,
        empty_msg="No donor programmes in the knowledge graph yet.",
    )
    body = f"""<h1>Donor programme pipeline</h1>
<p class="lead summary">This pipeline lists {n} active and forthcoming donor programmes from World Bank, ADB, EU, EBRD, UN agencies, and bilaterals that fund AI and digital government work in Uzbekistan and Kyrgyzstan. Every record names the donor's TTL or project manager and the government counterpart they work with.</p>
<h2>Why does the donor matter?</h2>
<p>In both countries 60–90% of AI/digital government budgets are donor-financed, often through World Bank or ADB project implementation units. The donor's TTL or task team leader is frequently the real customer, not the formal ministry head. Vendor entry pathways depend on knowing this dyad.</p>
<h2>Programmes</h2>
{table}
"""
    return render_page(
        path="/donors/",
        title="Donor pipeline (WB · ADB · EU · others)",
        description="Active and pipeline donor programmes funding AI and digital government in Uzbekistan and Kyrgyzstan, with TTL/PM and government counterpart for each.",
        body_html=body,
    )


def procurement_page(graph: dict[str, Any]) -> str:
    tenders = [t for t in graph.get("tenders", []) or [] if t.get("status") in ("live", "forthcoming")]
    n = len(tenders)
    rows = []
    for t in sorted(tenders, key=lambda x: x.get("submission_deadline") or "9999"):
        url = t.get("tender_url")
        link = f"<a href='{escape(url)}'>tender</a>" if url else "—"
        rows.append(
            f"<tr><td>{escape(t.get('country') or '')}</td>"
            f"<td>{escape(t.get('title_en') or t.get('title') or '')}</td>"
            f"<td>${(t.get('estimated_value_usd') or 0):,.0f}</td>"
            f"<td>{escape(t.get('submission_deadline') or '')}</td>"
            f"<td>{escape(t.get('win_probability') or '')}</td>"
            f"<td>{link}</td></tr>"
        )
    table = render_table(
        ["Country", "Title", "Value (USD)", "Deadline", "Win probability", "Link"],
        rows,
        paginate_after=20,
        empty_msg="No live tenders in the knowledge graph yet.",
    )
    body = f"""<h1>Live procurement</h1>
<p class="lead summary">This page tracks {n} live and forthcoming AI or digital government tenders in Uzbekistan and Kyrgyzstan, including donor-funded procurement through World Bank STEP and ADB CSRN. Each tender is annotated with incumbent risk, win probability, and the authorising decree where traceable.</p>
<h2>How is win probability assessed?</h2>
<p>Win probability factors in foreign-eligibility, incumbent advantage, scope match, and submission window. Tenders flagged with high incumbent risk and short submission windows are scored low even if values are large — vendor-locked specs are a waste of bid effort.</p>
<h2>Tenders</h2>
{table}
"""
    return render_page(
        path="/procurement/",
        title="Live procurement (UZ + KG)",
        description="Live and forthcoming AI/digital government tenders in Uzbekistan and Kyrgyzstan, with win probability and incumbent risk annotations.",
        body_html=body,
    )


def trends_page(graph: dict[str, Any]) -> str:
    trends = graph.get("trends", []) or []
    n = len(trends)
    by_country = {"UZ": [], "KG": [], "BOTH": []}
    for t in trends:
        by_country.setdefault(t.get("country", "BOTH"), []).append(t)
    body_parts = [f"""<h1>Sectoral trends</h1>
<p class="lead summary">Twelve sectoral trends shape the AI and digital government opportunity surface in Uzbekistan and Kyrgyzstan in 2025–2026: public administration, justice, health, education, agriculture and water, energy, transport, finance, security, environment, tourism, and labour migration. Each trend is grounded in specific decrees, donor programmes, and named decision-makers.</p>
<h2>Convergent windows</h2>
<p>The most strategically valuable trends are convergent windows — places where multiple lenses align (active decree + donor co-financing + named decision-maker + market readiness). The Russian/CIS substitution lens is particularly active for sovereign LLM and cybersecurity work post-2022.</p>"""]
    for ct, items in by_country.items():
        if not items:
            continue
        cname = {"UZ": "Uzbekistan", "KG": "Kyrgyzstan", "BOTH": "Both countries"}[ct]
        body_parts.append(f"<h2>{cname} trends</h2>")
        rows = []
        for t in sorted(items, key=lambda x: x.get("name") or ""):
            rows.append(
                f"<tr><td>{escape(t.get('sector') or '')}</td>"
                f"<td>{escape(t.get('name') or '')}</td>"
                f"<td>{escape(t.get('maturity') or '')}</td>"
                f"<td>{escape(', '.join(t.get('lens_tags', []) or []))}</td></tr>"
            )
        body_parts.append(render_table(
            ["Sector", "Trend", "Maturity", "Lenses"],
            rows,
            paginate_after=20,
            empty_msg="No trends in the knowledge graph yet.",
        ))
    if n == 0:
        body_parts.append("<p>No trends in the knowledge graph yet.</p>")
    return render_page(
        path="/trends/",
        title="Sectoral trends",
        description=f"{n} AI and digital government trends across 12 sectors in Uzbekistan and Kyrgyzstan, with lens annotations.",
        body_html="\n".join(body_parts),
    )


def people_page(graph: dict[str, Any]) -> str:
    people = graph.get("people", []) or []
    n = len(people)
    diaspora = sum(1 for p in people if p.get("diaspora_advisor_flag"))
    # Public partition: skip personal contact details (already enforced by schema)
    rows = []
    for p in sorted(people, key=lambda x: (x.get("priority_tier") or 99, x.get("country") or "")):
        if p.get("priority_tier") not in (1, 2):
            continue
        link = ""
        if p.get("linkedin_status") == "verified" and p.get("linkedin_url"):
            link = f'<a href="{escape(p["linkedin_url"])}">LinkedIn</a>'
        rows.append(
            f"<tr><td>{escape(p.get('country') or '')}</td>"
            f"<td>{escape(p.get('full_name_latin') or '')}</td>"
            f"<td>{escape(p.get('current_role') or '')}</td>"
            f"<td>{escape(p.get('current_institution_id') or '')}</td>"
            f"<td>{link}</td>"
            f"<td>{'diaspora' if p.get('diaspora_advisor_flag') else ''}</td></tr>"
        )
    table = render_table(
        ["Country", "Name", "Role", "Institution", "LinkedIn", "Tag"],
        rows,
        paginate_after=25,
        empty_msg="No people in the knowledge graph yet.",
    )
    body = f"""<h1>Decision-makers and diaspora bridges</h1>
<p class="lead summary">This list catalogues {n} named decision-makers across Uzbekistan and Kyrgyzstan with mandate over AI or digital procurement, plus {diaspora} diaspora advisors who shape policy from London, Dubai, Moscow, San Francisco, and other cities. Only Tier-1 and Tier-2 individuals are shown publicly; outreach scripts and warm-intro paths stay in the private vault.</p>
<h2>What is the diaspora bridge?</h2>
<p>Senior Uzbek and Kyrgyz professionals at FAANG, McKinsey, BCG, top universities, and global central banks frequently advise the home government informally — often with higher LinkedIn responsiveness than ministers themselves. They are routinely the highest-leverage targets in B2G outreach.</p>
<h2>Tier-1 / Tier-2 decision-makers</h2>
{table}
<p><em>This page redacts personal contact details. Outreach scripts and warm-intro paths are available only in the private Obsidian vault.</em></p>
"""
    return render_page(
        path="/people/",
        title="Decision-makers (UZ + KG)",
        description=f"{n} named decision-makers across Uzbekistan and Kyrgyzstan with mandate over AI/digital procurement, plus diaspora advisors.",
        body_html=body,
    )


def initiatives_page(graph: dict[str, Any]) -> str:
    inits = graph.get("initiatives", []) or []
    n = len(inits)
    a = [i for i in inits if i.get("confidence_tier") == "A"]
    rows = []
    for i in sorted(inits, key=lambda x: (x.get("scoring", {}).get("weighted_total") or 0), reverse=True):
        sc = i.get("scoring", {})
        tier = i.get("confidence_tier") or "—"
        cls = {"A": "tier-a", "B": "tier-b"}.get(tier, "tier-c")
        rows.append(
            f"<tr><td><span class='tag {cls}'>{escape(tier)}</span></td>"
            f"<td>{escape(i.get('country') or '')}</td>"
            f"<td>{escape(i.get('short_name') or '')}</td>"
            f"<td>{escape(i.get('sector') or '')}</td>"
            f"<td>{(sc.get('weighted_total') or 0):.2f}</td>"
            f"<td>${(i.get('estimated_initial_contract_usd') or 0):,.0f}</td>"
            f"<td>{escape(i.get('procurement_pathway') or '')}</td></tr>"
        )
    table = render_table(
        ["Tier", "Country", "Initiative", "Sector", "Score", "Initial contract (USD)", "Pathway"],
        rows,
        paginate_after=25,
        empty_msg="No initiatives in the knowledge graph yet.",
    )
    body = f"""<h1>Initiative top {n}</h1>
<p class="lead summary">This is the headline list: {n} deployable AI and digital government initiatives across Uzbekistan and Kyrgyzstan, scored on five axes and tier-bucketed. {len(a)} initiatives are Tier-A — every key reference field is verified, and a credible 12-month deal path is documented. The scoring rubric is on the Scoring page.</p>
<h2>How is each initiative grounded?</h2>
<p>Every Tier-A initiative names its target buyer (Person), lead institution, authorising decree, secondary funding via a specific donor programme, and the global precedent it transfers from. The verification cascade re-fetches sources during the audit wave; failures demote tier.</p>
<h2>Initiatives</h2>
{table}
"""
    return render_page(
        path="/initiatives/",
        title="Initiative top 100 — Tier-A B2G deals",
        description=f"{n} deployable AI/digital government initiatives in Uzbekistan and Kyrgyzstan, scored on five axes, with {len(a)} Tier-A deal-ready opportunities.",
        body_html=body,
    )


def mvp_page(graph: dict[str, Any], country: str | None = None) -> str:
    mvps = graph.get("solopreneur_mvps", []) or []
    if country:
        mvps = [m for m in mvps if m.get("country") == country]
    n = len(mvps)
    a = [m for m in mvps if m.get("confidence_tier") == "A"]
    cname = {"UZ": "Uzbekistan", "KG": "Kyrgyzstan"}.get(country, "Both countries")
    rows = []
    for m in sorted(mvps, key=lambda x: (x.get("scoring", {}).get("weighted_total") or 0), reverse=True):
        sc = m.get("scoring", {})
        tier = m.get("confidence_tier") or "—"
        cls = {"A": "tier-a", "B": "tier-b"}.get(tier, "tier-c")
        mon = m.get("monetization") or {}
        plan = m.get("mvr_plan") or {}
        rows.append(
            f"<tr><td><span class='tag {cls}'>{escape(tier)}</span></td>"
            f"<td>{escape(m.get('country') or '')}</td>"
            f"<td>{escape(m.get('short_name') or '')}</td>"
            f"<td>{escape(m.get('category') or '')}</td>"
            f"<td>{(sc.get('weighted_total') or 0):.2f}</td>"
            f"<td>{escape(plan.get('vehicle') or '')}</td>"
            f"<td>{plan.get('build_time_days') or ''}d</td>"
            f"<td>${(mon.get('year_1_revenue_target_usd') or 0):,.0f}</td></tr>"
        )
    table = render_table(
        ["Tier", "Country", "MVP", "Category", "Score", "MVR vehicle", "Build (days)", "Year 1 revenue (USD)"],
        rows,
        paginate_after=25,
        empty_msg="No solopreneur MVPs in the knowledge graph yet.",
    )
    if country:
        path = f"/mvp/{country.lower()}/"
        title = f"Solopreneur MVPs — {cname}"
    else:
        path = "/mvp/"
        title = "Solopreneur MVPs (UZ + KG)"
    body = f"""<h1>{escape(title)}</h1>
<p class="lead summary">This is a parallel track to the institutional B2G initiatives: {n} solopreneur-bootstrappable MVPs grounded in the knowledge graph and HubSpot's $1M Solopreneur MVR framework. {len(a)} are Tier-A. Every idea has a one-week build plan, a quantified validation target, and a price point grounded in local purchasing power.</p>
<h2>What is a Minimum Viable Representation?</h2>
<p>An MVR is a landing page, demo video, free tool, directory, manifesto, or Wizard-of-Oz manual service — <em>not</em> a finished product. The framework's premise: validate demand in 7 days, not 12 months. One paying customer on day one beats twelve months of speculation.</p>
<h2>Eight MVR vehicles</h2>
<ol>
<li><strong>Landing page + waitlist</strong> — for SaaS demand signaling</li>
<li><strong>Squeeze page</strong> — for pure demand validation</li>
<li><strong>Demo video</strong> — Loom or Twitter-native, especially for AI tools</li>
<li><strong>Free tool</strong> — solves one micro-problem, no login</li>
<li><strong>Directory</strong> — content-driven, ad/listing-fee monetised</li>
<li><strong>Wizard of Oz</strong> — manual fulfillment behind an "automated" facade</li>
<li><strong>Ad-validated booking</strong> — Facebook/Instagram ad with direct booking</li>
<li><strong>Manifesto / blog post</strong> — viral-leaning, audience-building</li>
</ol>
<h2>How is each MVP grounded?</h2>
<p>Every MVP references a real Trend, Decree, or Donor program from the knowledge graph, names a concrete target customer (not "small businesses" but "Andijan-based wedding photographers booking via Instagram"), and prices to local purchasing power (UZ avg salary ~$300/month; KG ~$250/month).</p>
<h2>Top solopreneur MVPs</h2>
{table}
<p style="font-size: 13px; color: #555;"><em>Methodology: HubSpot's "$1M Solopreneur MVP" framework, encoded into a synthesizer agent that walks the knowledge graph and outputs 100 ideas per country.</em></p>
"""
    breadcrumbs = [("/", "Home"), ("/mvp/", "Solo MVPs")]
    return render_page(
        path=path,
        title=title,
        description=f"{n} solopreneur-bootstrappable MVP ideas across {cname}, scored on demand clarity, speed-to-MVR, monetization, founder feasibility, and local market fit.",
        body_html=body,
        breadcrumbs=breadcrumbs,
        country=country,
    )


def country_page(graph: dict[str, Any], country: str) -> str:
    """Render a country-level live report aggregating every record type for one country."""
    cname = {"UZ": "Uzbekistan", "KG": "Kyrgyzstan"}[country]
    cname_ru = {"UZ": "Узбекистан", "KG": "Кыргызстан"}[country]
    slug = {"UZ": "uzbekistan", "KG": "kyrgyzstan"}[country]

    # Filter
    inits = [i for i in (graph.get("initiatives") or []) if i.get("country") == country]
    decrees = [d for d in (graph.get("decrees") or []) if d.get("country") == country]
    insts = [i for i in (graph.get("institutions") or []) if i.get("country") == country]
    people = [p for p in (graph.get("people") or []) if p.get("country") == country]
    donors = [p for p in (graph.get("donor_programs") or []) if p.get("country") in (country, "BOTH")]
    tenders = [t for t in (graph.get("tenders") or []) if t.get("country") == country]
    trends = [t for t in (graph.get("trends") or []) if t.get("country") == country]
    mvps = [m for m in (graph.get("solopreneur_mvps") or []) if m.get("country") == country]

    inst_idx = index_by_id(insts + (graph.get("institutions") or []))
    person_idx = index_by_id(people + (graph.get("people") or []))
    decree_idx = index_by_id(decrees + (graph.get("decrees") or []))
    donor_idx = index_by_id(donors + (graph.get("donor_programs") or []))

    tier_a = [i for i in inits if i.get("confidence_tier") == "A"]
    active_decrees = [d for d in decrees if d.get("half_life_status") == "active_window"]
    live_tenders = [t for t in tenders if t.get("status") in ("live", "forthcoming")]
    tier_a_mvps = [m for m in mvps if m.get("confidence_tier") == "A"]

    # Lead summary (40-60 words, country-specific framing)
    if country == "UZ":
        lead = (
            f"Uzbekistan is the larger surface: {len(inits)} deployable AI and digital-government "
            f"initiatives, {len(tier_a)} of them Tier-A, anchored in {len(decrees)} decrees including "
            f"the $100M PP-320 AI fund and the УП-189 mandate for 100 AI projects by end-2026. "
            f"{len(donors)} donor programmes, {len(people)} named decision-makers, "
            f"{len(live_tenders)} live tenders. Russian-Uzbek bilingual UX is non-negotiable."
        )
        headline_shift = (
            "<strong>October 2025 structural mandate:</strong> УП-189 and PP-320 created a $100M National "
            "AI Project Support Fund and ordered 100 deployed AI projects across state bodies by end-2026. "
            "AI procurement under the new fund became eligible 1 January 2026. Vendors with Russian-Uzbek "
            "bilingual capability and existing IT-Park residency win first."
        )
    else:
        lead = (
            f"Kyrgyzstan is in flux: {len(inits)} initiatives, {len(tier_a)} Tier-A, mapped against "
            f"{len(decrees)} decrees and the April 2026 abolition of the Ministry of Digital Development. "
            f"All {len(donors)} donor programmes are renegotiating counterparts inside the Presidential "
            f"Administration (УДП). {len(people)} decision-makers tracked. {len(live_tenders)} live tenders. "
            f"Whoever co-drafts the new Digital Code regulations defines the next decade."
        )
        headline_shift = (
            "<strong>April 2026 structural break:</strong> Kabmin postanovlenie abolished the Ministry of "
            "Digital Development. Authority transferred to Presidential Administration (УДП). Every legacy "
            "donor counterpart is under renegotiation through Q3 2026. The Digital Code (in force) needs "
            "secondary regulations — first-mover vendors who help draft them lock in the regulatory rails."
        )

    # ── KPI grid
    kpis = "\n".join([
        kpi_row("B2G initiatives", len(inits)),
        kpi_row("Tier-A deals", len(tier_a)),
        kpi_row("Decrees mapped", len(decrees)),
        kpi_row("Active-window decrees", len(active_decrees)),
        kpi_row("Donor programmes", len(donors)),
        kpi_row("Decision-makers", len(people)),
        kpi_row("Live tenders", len(live_tenders)),
        kpi_row("Solo MVPs", len(mvps)),
        kpi_row("Tier-A MVPs", len(tier_a_mvps)),
    ])

    # ── Top initiatives table
    init_rows = []
    inits_sorted = sorted(inits, key=lambda x: (x.get("scoring", {}).get("weighted_total") or 0), reverse=True)
    for i in inits_sorted[:15]:
        sc = i.get("scoring", {}) or {}
        tier = i.get("confidence_tier") or "—"
        cls = {"A": "tier-a", "B": "tier-b"}.get(tier, "tier-c")
        lead_inst_id = i.get("lead_institution_id") or ""
        lead_inst = (inst_idx.get(lead_inst_id) or {}).get("name_en") or lead_inst_id
        decree_ids = i.get("authorizing_decree_ids") or []
        decree_chip = ", ".join(decree_ids[:2]) if decree_ids else "—"
        init_rows.append(
            f"<tr><td><span class='tag {cls}'>{escape(tier)}</span></td>"
            f"<td>{escape(i.get('short_name') or '')}</td>"
            f"<td>{escape(i.get('sector') or '')}</td>"
            f"<td>{(sc.get('weighted_total') or 0):.2f}</td>"
            f"<td>${(i.get('estimated_initial_contract_usd') or 0):,.0f}</td>"
            f"<td>{escape(lead_inst)}</td>"
            f"<td>{escape(decree_chip)}</td></tr>"
        )
    init_table = render_table(
        ["Tier", "Initiative", "Sector", "Score", "Initial contract (USD)", "Lead institution", "Authorising decrees"],
        init_rows,
        paginate_after=15,
        empty_msg="No initiatives in the knowledge graph yet.",
    )

    # ── Tier-A deep cards (top 5)
    deep_cards: list[str] = []
    for i in [x for x in inits_sorted if x.get("confidence_tier") == "A"][:5]:
        sc = i.get("scoring", {}) or {}
        target_id = i.get("target_buyer_person_id") or ""
        target = (person_idx.get(target_id) or {}).get("full_name_latin") or target_id or "[unnamed]"
        target_role = (person_idx.get(target_id) or {}).get("current_role") or ""
        funding = i.get("primary_funding") or "—"
        sec_donor_id = i.get("secondary_funding_donor_program_id") or ""
        sec_donor = (donor_idx.get(sec_donor_id) or {}).get("program_name") or sec_donor_id or "—"
        pathway = i.get("procurement_pathway") or "—"
        pitch = i.get("pitch_hook") or i.get("one_liner") or ""
        deep_cards.append(
            f"<div class='persona' role='listitem'>"
            f"<h3>{escape(i.get('short_name') or '')}</h3>"
            f"<p><strong>One-liner:</strong> {escape(i.get('one_liner') or '')}</p>"
            f"<p><strong>Pitch hook:</strong> {escape(pitch)}</p>"
            f"<p><strong>Score {sc.get('weighted_total', 0):.2f}</strong> · "
            f"speed {sc.get('speed_to_contract', 0)}/10 · moat {sc.get('strategic_moat', 0)}/10 · "
            f"defensibility {sc.get('defensibility', 0)}/10 · capital {sc.get('capital_access', 0)}/10 · "
            f"RU/CIS fit {sc.get('russian_cis_fit', 0)}/10</p>"
            f"<p><strong>Target buyer:</strong> {escape(target)} — <em>{escape(target_role)}</em></p>"
            f"<p><strong>Funding:</strong> {escape(funding)}"
            + (f" + secondary via <em>{escape(sec_donor)}</em>" if sec_donor != "—" else "")
            + f"</p>"
            f"<p><strong>Procurement pathway:</strong> {escape(pathway)} · "
            f"<strong>Initial contract:</strong> ${(i.get('estimated_initial_contract_usd') or 0):,.0f}</p>"
            f"</div>"
        )
    deep_block = (
        '<div class="persona-grid" role="list" aria-label="Tier-A initiative deep cards">'
        + "".join(deep_cards) + "</div>"
        if deep_cards else "<p>No Tier-A initiatives surfaced yet.</p>"
    )

    # ── Decrees (top 10 active or most recent)
    dec_sorted = sorted(decrees, key=lambda d: (d.get("half_life_status") != "active_window", d.get("date") or ""), reverse=False)
    dec_sorted = sorted(dec_sorted, key=lambda d: d.get("date") or "", reverse=True)
    dec_rows = []
    for d in dec_sorted[:12]:
        sources = d.get("sources") or []
        src = sources[0] if sources else None
        link_html = f'<a href="{escape(src.get("url"))}">primary source</a>' if src and src.get("url") else "—"
        dec_rows.append(
            f"<tr><td>{escape(d.get('id') or '')}</td>"
            f"<td>{escape(d.get('decree_type') or '')}</td>"
            f"<td>{ru(d.get('number') or '')}</td>"
            f"<td>{escape(d.get('date') or '')}</td>"
            f"<td>{escape(d.get('title_en') or '')}</td>"
            f"<td><span class='tag'>{escape(d.get('half_life_status') or '')}</span></td>"
            f"<td>{link_html}</td></tr>"
        )
    dec_table = render_table(
        ["ID", "Type", "Number", "Date", "Title", "Status", "Source"],
        dec_rows,
        paginate_after=12,
        empty_msg="No decrees in the knowledge graph yet.",
    )

    # ── Donors (top 10 by budget)
    don_rows = []
    for p in sorted(donors, key=lambda x: x.get("total_budget_usd") or 0, reverse=True)[:12]:
        don_rows.append(
            f"<tr><td>{escape(p.get('donor') or '')}</td>"
            f"<td>{escape(p.get('program_name') or '')}</td>"
            f"<td>${(p.get('total_budget_usd') or 0):,.0f}</td>"
            f"<td>{escape((p.get('ttl_pm_name') or '')[:80])}</td>"
            f"<td>{escape(p.get('status') or '')}</td></tr>"
        )
    don_table = render_table(
        ["Donor", "Programme", "Budget (USD)", "TTL / PM", "Status"],
        don_rows,
        paginate_after=12,
        empty_msg="No donor programmes in the knowledge graph yet.",
    )

    # ── Live tenders
    ten_rows = []
    for t in sorted(live_tenders, key=lambda x: x.get("submission_deadline") or "9999")[:12]:
        url = t.get("tender_url")
        link = f"<a href='{escape(url)}'>tender</a>" if url else "—"
        ten_rows.append(
            f"<tr><td>{escape(t.get('title_en') or t.get('title') or '')}</td>"
            f"<td>${(t.get('estimated_value_usd') or 0):,.0f}</td>"
            f"<td>{escape(t.get('submission_deadline') or '')}</td>"
            f"<td>{escape(t.get('procurement_method') or '')}</td>"
            f"<td>{escape(t.get('win_probability') or '')}</td>"
            f"<td>{link}</td></tr>"
        )
    ten_table = render_table(
        ["Title", "Value (USD)", "Deadline", "Method", "Win prob.", "Link"],
        ten_rows,
        paginate_after=12,
        empty_msg="No live tenders in the knowledge graph yet.",
    )

    # ── Trends (top 10 by TAM)
    tr_sorted = sorted(trends, key=lambda x: x.get("estimated_tam_2025_2026_usd") or 0, reverse=True)
    tr_rows = []
    for t in tr_sorted[:12]:
        tr_rows.append(
            f"<tr><td>{escape(t.get('sector') or '')}</td>"
            f"<td>{escape(t.get('name') or '')}</td>"
            f"<td>{escape(t.get('maturity') or '')}</td>"
            f"<td>${(t.get('estimated_tam_2025_2026_usd') or 0):,.0f}</td>"
            f"<td>{escape(str(t.get('window_months_remaining') or ''))}</td></tr>"
        )
    tr_table = render_table(
        ["Sector", "Trend", "Maturity", "TAM 2025-26 (USD)", "Window (mo.)"],
        tr_rows,
        paginate_after=12,
        empty_msg="No trends in the knowledge graph yet.",
    )

    # ── Decision-makers (Tier 1+2)
    ppl_rows = []
    ppl_sorted = sorted(people, key=lambda x: (x.get("priority_tier") or 99, x.get("full_name_latin") or ""))
    for p in ppl_sorted:
        if p.get("priority_tier") not in (1, 2):
            continue
        link = ""
        if p.get("linkedin_status") == "verified" and p.get("linkedin_url"):
            link = f'<a href="{escape(p["linkedin_url"])}">LinkedIn</a>'
        inst_id = p.get("current_institution_id") or ""
        inst_name = (inst_idx.get(inst_id) or {}).get("name_en") or inst_id
        ppl_rows.append(
            f"<tr><td>{escape(str(p.get('priority_tier') or ''))}</td>"
            f"<td>{escape(p.get('full_name_latin') or '')}</td>"
            f"<td>{escape(p.get('current_role') or '')}</td>"
            f"<td>{escape(inst_name)}</td>"
            f"<td>{link}</td></tr>"
        )
    ppl_table = render_table(
        ["Tier", "Name", "Role", "Institution", "LinkedIn"],
        ppl_rows,
        paginate_after=15,
        empty_msg="No Tier-1/2 decision-makers in the knowledge graph yet.",
    )

    # ── Institutions (Tier 1-3)
    inst_rows = []
    for i in sorted(insts, key=lambda x: (x.get("tier") or 99, x.get("name_en") or "")):
        if (i.get("tier") or 99) > 4:
            continue
        head_id = i.get("head_person_id") or ""
        head_name = (person_idx.get(head_id) or {}).get("full_name_latin") or head_id or "—"
        inst_rows.append(
            f"<tr><td>{escape(str(i.get('tier') or ''))}</td>"
            f"<td>{escape(i.get('name_en') or '')}</td>"
            f"<td>{ru(i.get('name_ru') or '')}</td>"
            f"<td>{escape(head_name)}</td></tr>"
        )
    inst_table = render_table(
        ["Tier", "Institution (EN)", "Institution (RU)", "Head"],
        inst_rows,
        paginate_after=15,
        empty_msg="No institutions in the knowledge graph yet.",
    )

    body = f"""<h1>{cname} — live B2G AI report</h1>
<p class="lead summary">{escape(lead)}</p>

<div class="banner">{headline_shift}</div>

<div class="kpi-grid" role="list" aria-label="{cname} headline counts">
{kpis}
</div>

<h2>Where should you start?</h2>
<p>Pick the entry that matches what you do. Each card lands you on the page that answers your first question.</p>
<div class="persona-grid" role="list" aria-label="{cname} reader entry paths">
  <div class="persona" role="listitem">
    <h3>Vendor / B2G operator</h3>
    <p>The {len(tier_a)} Tier-A initiatives below are deal-ready: verified buyer, decree anchor, donor co-financing pathway, credible 12-month plan.</p>
    <p><a href="#tier-a-initiatives">→ Tier-A initiatives</a> · <a href="#live-tenders">live tenders</a></p>
  </div>
  <div class="persona" role="listitem">
    <h3>Donor / IFI counterpart</h3>
    <p>{len(donors)} active and pipeline programmes touching {cname}, with TTL or PM and government counterpart named on each.</p>
    <p><a href="#donor-programmes">→ Donor programmes</a> · <a href="{_bp('/donors/')}">full pipeline</a></p>
  </div>
  <div class="persona" role="listitem">
    <h3>Solopreneur / bootstrapper</h3>
    <p>{len(mvps)} solopreneur MVP ideas grounded in the {cname} knowledge graph, scored on demand clarity, speed-to-MVR, and local market fit.</p>
    <p><a href="{_bp(f'/mvp/{country.lower()}/')}">→ {cname} solo MVPs</a></p>
  </div>
  <div class="persona" role="listitem">
    <h3>Government / regulator</h3>
    <p>The decree atlas and {len(active_decrees)} active-window decrees show what is already authorised but not yet procured.</p>
    <p><a href="{_bp(f'/decrees/{country.lower()}/')}">→ {cname} decree atlas</a></p>
  </div>
</div>

<h2 id="tier-a-initiatives">Top {min(5, len(tier_a))} Tier-A initiatives — deep view</h2>
<p>Each card pulls the named target buyer, the funding stack, the procurement pathway, and the five-axis score for the highest-rated Tier-A {cname} deals. Full record at <a href="{_bp('/initiatives/')}">Initiatives</a>.</p>
{deep_block}

<h2>All Tier-A and Tier-B initiatives — table</h2>
<p>Top {min(15, len(inits_sorted))} {cname} initiatives by weighted score. Full list of {len(inits)} on the <a href="{_bp('/initiatives/')}">Initiatives</a> page.</p>
{init_table}

<h2 id="decrees">Decrees ({len(active_decrees)} in active implementation window)</h2>
<p>The {min(12, len(dec_sorted))} most recent decrees in {cname} authorising AI or digital-government work. Status flag indicates whether the decree is in its 6–18 month active implementation window.</p>
{dec_table}

<h2 id="donor-programmes">Donor programmes ({len(donors)} active or pipeline)</h2>
<p>The largest active and pipeline donor programmes in {cname} by total budget. The donor's TTL or task team leader is frequently the real customer, not the formal ministry head.</p>
{don_table}

<h2 id="live-tenders">Live and forthcoming tenders ({len(live_tenders)})</h2>
<p>Live or forthcoming AI/digital procurements in {cname}, ordered by submission deadline. Each is annotated with win probability and procurement method.</p>
{ten_table}

<h2 id="trends">Sectoral trends ({len(trends)})</h2>
<p>The {min(12, len(tr_sorted))} highest-TAM AI/digital trends in {cname} for 2025–2026, with the closing window in months.</p>
{tr_table}

<h2 id="decision-makers">Tier-1 and Tier-2 decision-makers</h2>
<p>Named individuals with mandate over AI or digital procurement in {cname}. Personal contact details are redacted on the public site; outreach scripts and warm-intro paths stay in the private vault.</p>
{ppl_table}

<h2 id="institutions">Institutions (Tier 1–4)</h2>
<p>State institutions in {cname} with explicit AI or digital mandate: Presidential Administration, Cabinet, line ministries, and agencies/SOEs.</p>
{inst_table}

<h2>Methodology</h2>
<p>This report is auto-generated from <code>state/knowledge_graph.json</code> on every site build. The {len(inits)} {cname} initiatives are scored on five axes (speed-to-contract, strategic moat, defensibility, capital access, Russian/CIS fit) per the <a href="{_bp('/scoring/')}">scoring rubric</a>. Records are sourced and verified per the <a href="{_bp('/methodology/')}">methodology</a>; uncertainty is documented on the <a href="{_bp('/honesty/')}">honesty page</a>.</p>

<h2>Reproduce this report</h2>
<p>The full pipeline is open at <a href="https://github.com/avaluev/ca-b2g-research">github.com/avaluev/ca-b2g-research</a> (Apache 2.0). The 16-specialist <a href="{_bp('/audit-team/')}">Audit Team</a> verifies every page on every build. Cited in your work? Use the citation widget at the bottom of this page.</p>
"""
    return render_page(
        path=f"/{slug}/",
        title=f"{cname} — live B2G AI/digital report",
        description=(
            f"Live country report for {cname}: {len(tier_a)} Tier-A B2G initiatives, "
            f"{len(decrees)} decrees, {len(donors)} donor programmes, {len(people)} decision-makers, "
            f"{len(live_tenders)} live tenders. Auto-generated, cited, reproducible."
        ),
        body_html=body,
        page_type="Report",
        country=country,
    )


def honesty_page(graph: dict[str, Any]) -> str:
    honesty_path = ROOT / "state" / "audit" / "honesty_section.md"
    md = honesty_path.read_text() if honesty_path.exists() else ""
    body_parts = ['<h1>Honesty: what we did not find</h1>']
    body_parts.append(
        '<p class="lead summary">This page documents the limits of this research: known gaps, dead-end research pathways, opaque domains, and contradictions we could not resolve. Honesty is a first-class output here. A research artifact that hides what it does not know is not trustworthy.</p>'
    )
    if md:
        body_parts.append(_md_to_html(md, skip_h1=True))
    else:
        body_parts.append("<p>The honesty section is generated by the reflexion-auditor (Wave 5). It will appear once the pipeline runs.</p>")
    return render_page(
        path="/honesty/",
        title="Honesty: what we did not find",
        description="The known gaps, dead-end pathways, and opaque domains in this research. Honesty as a first-class output.",
        body_html="\n".join(body_parts),
    )


def provenance_page(graph: dict[str, Any]) -> str:
    n_sources = sum(len(d.get("sources") or []) for d in graph.get("decrees", []) or [])
    n_sources += sum(len(i.get("sources") or []) for i in graph.get("institutions", []) or [])
    n_sources += sum(len(p.get("sources") or []) for p in graph.get("people", []) or [])
    n_sources += sum(len(p.get("sources") or []) for p in graph.get("donor_programs", []) or [])
    body = f"""<h1>Provenance and audit trail</h1>
<p class="lead summary">Every record in this research carries one or more cited sources, totalling roughly {n_sources} references across decrees, institutions, people, and donor programmes. Every cross-model verification call to OpenRouter — Perplexity Sonar Deep Research, Sonar Pro, o4-mini-deep-research, Owl Alpha, and Gemma — is logged as an evidence card under <code>state/external/</code> in the public repo.</p>
<h2>How can I audit any single claim?</h2>
<p>Open the relevant page (Decrees, People, Donors), find the record's <code>sources</code> array, and follow each URL. Numeric claims always cite the source within the rendered table or paragraph. The reflexion-auditor wave (Wave 5) re-fetches a sample of sources during every run; failures appear in <code>state/audit/audit_report.md</code>.</p>
<h2>Where is the source code?</h2>
<p>The full pipeline is open at <a href="https://github.com/avaluev/ca-b2g-research">github.com/avaluev/ca-b2g-research</a> under Apache 2.0. Every agent specification (<code>.claude/agents/*.md</code>), every script, and every quality gate is committed.</p>
"""
    return render_page(
        path="/provenance/",
        title="Provenance and audit trail",
        description="Every claim's source, every cross-model verification card, every audit finding — public and reproducible.",
        body_html=body,
    )


# ────────────────────────────────────────────────────────────────────────────


def main() -> int:
    if SITE.exists():
        for child in SITE.iterdir():
            if child.is_dir():
                shutil.rmtree(child)
            else:
                child.unlink()
    SITE.mkdir(parents=True, exist_ok=True)

    if not GRAPH_PATH.exists():
        print(f"⚠ {GRAPH_PATH} not found — rendering stub site")
        graph: dict[str, Any] = {}
    else:
        graph = json.loads(GRAPH_PATH.read_text())

    lenses_md = (DOCS / "lenses.md").read_text() if (DOCS / "lenses.md").exists() else ""
    rubric_md = (DOCS / "scoring_rubric.md").read_text() if (DOCS / "scoring_rubric.md").exists() else ""

    write_page("/", home(graph))
    write_page("/uzbekistan/", country_page(graph, "UZ"))
    write_page("/kyrgyzstan/", country_page(graph, "KG"))
    write_page("/methodology/", methodology())
    write_page("/lenses/", lenses_page(lenses_md))
    write_page("/scoring/", scoring_page(rubric_md))
    write_page("/decrees/uz/", decrees_page(graph, "UZ"))
    write_page("/decrees/kg/", decrees_page(graph, "KG"))
    write_page("/institutions/", institutions_page(graph))
    write_page("/donors/", donors_page(graph))
    write_page("/procurement/", procurement_page(graph))
    write_page("/trends/", trends_page(graph))
    write_page("/people/", people_page(graph))
    write_page("/initiatives/", initiatives_page(graph))
    write_page("/about/", about_page())
    write_page("/audit-team/", audit_team_page())
    # Custom 404 (GitHub Pages serves /404.html by default)
    (SITE / "404.html").write_text(not_found_page(), encoding="utf-8")
    write_page("/mvp/", mvp_page(graph, country=None))
    write_page("/mvp/uz/", mvp_page(graph, country="UZ"))
    write_page("/mvp/kg/", mvp_page(graph, country="KG"))
    write_page("/honesty/", honesty_page(graph))
    write_page("/provenance/", provenance_page(graph))

    # Favicon (a single-letter B mark — small SVG, no external deps)
    favicon_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" role="img" aria-label="Central Asia B2G Intelligence logo"><title>Central Asia B2G Intelligence</title><rect width="64" height="64" fill="#007a33"/><text x="50%" y="55%" text-anchor="middle" fill="#fff" font-family="system-ui" font-size="40" font-weight="700">B</text></svg>"""
    (SITE / "favicon.svg").write_text(favicon_svg)
    # OG default image: a transparent 1200x630 placeholder (text-only SVG)
    og_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 630"><rect width="1200" height="630" fill="#0a4"/><text x="50%" y="40%" text-anchor="middle" fill="#fff" font-family="system-ui" font-size="64" font-weight="700">Central Asia B2G Intelligence</text><text x="50%" y="55%" text-anchor="middle" fill="#cfe9d6" font-family="system-ui" font-size="32">Uzbekistan + Kyrgyzstan AI/Digital Government</text></svg>"""
    (SITE / "og-default.svg").write_text(og_svg)

    print(f"Site written: {SITE}")
    print(f"Pages: {sum(1 for _ in SITE.rglob('*.html'))}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
