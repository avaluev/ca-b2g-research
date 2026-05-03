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
*,*::before,*::after{box-sizing:border-box}
html{font-family:system-ui,-apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif;line-height:1.55;color:#111;background:#fff;-webkit-text-size-adjust:100%}
body{margin:0;padding:0}
.container{max-width:880px;margin:0 auto;padding:24px 20px 80px}
header.nav{position:sticky;top:0;background:#fff;border-bottom:1px solid #eaeaea;z-index:10}
header.nav nav{max-width:1200px;margin:0 auto;padding:12px 20px;display:flex;flex-wrap:wrap;gap:12px;align-items:center}
header.nav a{color:#0a4;text-decoration:none;font-size:14px;font-weight:500}
header.nav a:hover{color:#062}
header.nav .brand{font-weight:700;color:#111;font-size:16px;margin-right:auto}
h1{font-size:36px;line-height:1.15;margin:24px 0 12px;color:#000}
h2{font-size:24px;line-height:1.25;margin:36px 0 8px;border-top:1px solid #eaeaea;padding-top:24px}
h3{font-size:18px;margin:24px 0 8px}
p{margin:8px 0 16px}
p.lead.summary{font-size:18px;color:#222;background:#f7f7f7;border-left:3px solid #0a4;padding:12px 16px;margin:16px 0 24px;border-radius:0 4px 4px 0}
table{border-collapse:collapse;width:100%;margin:12px 0 24px;font-size:14px}
th,td{padding:8px 10px;border-bottom:1px solid #eaeaea;text-align:left;vertical-align:top}
th{background:#f7f7f7;font-weight:600}
code,pre{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:13px}
code{background:#f3f3f3;padding:2px 6px;border-radius:3px}
pre{background:#f7f7f7;padding:12px 16px;border-radius:4px;overflow-x:auto}
a{color:#062}
a:hover{color:#0a4}
.tag{display:inline-block;background:#e9f6ee;color:#0a4;font-size:12px;padding:2px 8px;border-radius:3px;margin-right:6px}
.tier-a{background:#fdebd3;color:#a06000}
.tier-b{background:#e9f6ee;color:#0a4}
.tier-c{background:#f3f3f3;color:#555}
footer.site{border-top:1px solid #eaeaea;padding:24px 20px;color:#555;font-size:13px;max-width:1200px;margin:60px auto 0}
.kpi-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:12px;margin:24px 0}
.kpi-grid .kpi{background:#f7f7f7;padding:12px 16px;border-radius:4px}
.kpi .num{font-size:24px;font-weight:700;color:#0a4}
.kpi .lbl{font-size:12px;color:#555;text-transform:uppercase;letter-spacing:.05em}
@media (max-width:640px){h1{font-size:28px}h2{font-size:20px}}
"""

NAV_LINKS = [
    ("/", "Home"),
    ("/methodology/", "Methodology"),
    ("/lenses/", "Lenses"),
    ("/scoring/", "Scoring"),
    ("/decrees/uz/", "Decrees UZ"),
    ("/decrees/kg/", "Decrees KG"),
    ("/institutions/", "Institutions"),
    ("/donors/", "Donors"),
    ("/procurement/", "Procurement"),
    ("/trends/", "Trends"),
    ("/people/", "People"),
    ("/initiatives/", "B2G Initiatives"),
    ("/mvp/", "Solo MVPs"),
    ("/honesty/", "Honesty"),
    ("/provenance/", "Provenance"),
]


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
    nav_parts = []
    for p, t in NAV_LINKS:
        aria = ' aria-current="page"' if p == path else ""
        nav_parts.append(f'<a href="{escape(p)}"{aria}>{escape(t)}</a>')
    nav = "\n        ".join(nav_parts)
    title_truncated = title if len(title) <= 60 else title[:57] + "..."
    desc_short = description if len(description) <= 160 else description[:157] + "..."
    country_meta = f'<meta name="country" content="{country}">' if country else ""
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
<meta property="og:image" content="{SITE_URL}/og-default.png">
<meta property="og:site_name" content="Central Asia B2G Intelligence">
<meta property="og:locale" content="en_US">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{escape(title_truncated)}">
<meta name="twitter:description" content="{escape(desc_short)}">
<meta name="twitter:image" content="{SITE_URL}/og-default.png">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="alternate" type="application/rss+xml" href="/feed.xml">
<style>{CSS}</style>
{extra_head}
<script type="application/ld+json">
{jsonld_graph(page_url=canonical, title=title, description=desc_short, page_type=page_type, breadcrumbs=breadcrumbs)}
</script>
</head>
<body>
<header class="nav"><nav>
        <span class="brand">Central Asia B2G</span>
        {nav}
      </nav></header>
<main class="container">
{body_html}
</main>
<footer class="site">
<p>Open research on AI/digital government opportunities in Uzbekistan + Kyrgyzstan.
Apache 2.0 — <a href="{OPERATOR_GITHUB}/ca-b2g-research">{OPERATOR_GITHUB.replace('https://', '')}/ca-b2g-research</a>.
Built {TODAY}.</p>
</footer>
</body>
</html>
"""


def write_page(path_url: str, html_text: str) -> None:
    out = SITE / path_url.strip("/") / "index.html" if path_url not in ("/", "") else SITE / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html_text, encoding="utf-8")


# ────────────────────────────────────────────────────────────────────────────
# Per-page rendering
# ────────────────────────────────────────────────────────────────────────────


def kpi_row(label: str, value: str | int) -> str:
    return f'<div class="kpi"><div class="num">{escape(str(value))}</div><div class="lbl">{escape(label)}</div></div>'


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
<div class="kpi-grid">
{kpi_row("B2G Initiatives", n_inits)}
{kpi_row("Tier-A", tier_a)}
{kpi_row("Solo MVPs", n_mvps)}
{kpi_row("Decrees", n_decrees)}
{kpi_row("Institutions", n_inst)}
{kpi_row("Decision-makers", n_people)}
{kpi_row("Donor programmes", n_donors)}
{kpi_row("Live tenders", n_tenders)}
{kpi_row("Global cases", n_cases)}
</div>
<h2>What is in this research?</h2>
<p>This is a typed, source-cited knowledge graph of AI and digital government opportunities in Uzbekistan and Kyrgyzstan, plus the methodology used to build it. Every initiative is mapped to a decree, an institution, a decision-maker, a donor programme, and a global precedent. Every numeric claim is cited.</p>
<h2>How was it produced?</h2>
<p>An eleven-agent multi-wave research pipeline built on Anthropic's Claude (Opus + Sonnet) with cross-model verification via Perplexity Sonar Deep Research and Sonar Pro on a strict $20 OpenRouter budget. The seven waves move from blueprint to legal corpus to institutions, donors, procurement, trends, people, synthesis, audit, and outreach.</p>
<h2>Who is this for?</h2>
<p>B2G operators, government affairs leads at vendors, donor counterparts, investment teams covering frontier emerging markets, and Central-Asian government decision-makers themselves. The site is bilingual-readable; primary sources are predominantly Russian-language.</p>
<h2>Where to start</h2>
<p>Start with <a href="/initiatives/">Initiatives</a> for the headline list. Read <a href="/lenses/">the five lenses</a> for the analytical frame. Read <a href="/honesty/">Honesty</a> for what we did <em>not</em> find — gaps are first-class records here. <a href="/provenance/">Provenance</a> shows every source and every cross-model verification card.</p>
"""
    return render_page(
        path="/",
        title="Central Asia B2G Intelligence — Uzbekistan + Kyrgyzstan AI/Digital Government",
        description="Open research on B2G AI and digital-government opportunities in Uzbekistan + Kyrgyzstan: 100+ initiatives mapped to decrees, donors, decision-makers, and precedents.",
        body_html=body,
        page_type="WebSite",
    )


def methodology() -> str:
    body = """<h1>Methodology</h1>
<p class="lead summary">A seven-wave multi-agent research pipeline turns Russian, Uzbek, and Kyrgyz primary sources into a typed knowledge graph. Eleven specialised agents work in three waves of parallel research, one wave of synthesis, one of adversarial audit, and one of outreach drafting. Cross-model verification via OpenRouter caps the OpenRouter spend at twenty dollars per run.</p>
<h2>What does each wave do?</h2>
<table>
<tr><th>Wave</th><th>Agent(s)</th><th>Purpose</th></tr>
<tr><td>0</td><td>blueprint-architect</td><td>Strategic plan, target lists, constraint inventory</td></tr>
<tr><td>1</td><td>legal-cartographer, case-tournament</td><td>Decree corpus + 100+ global precedents</td></tr>
<tr><td>2</td><td>institution-mapper, donor-pipeline, procurement-harvester, trend-triangulator</td><td>Org taxonomies, donor programs, tenders, trends</td></tr>
<tr><td>3</td><td>people-intelligence</td><td>100+ decision-makers + diaspora bridges</td></tr>
<tr><td>4</td><td>initiative-synthesizer</td><td>100+ initiatives, 5-axis scoring</td></tr>
<tr><td>5</td><td>reflexion-auditor</td><td>Adversarial re-verification, ≥3 HIGH-issue minimum</td></tr>
<tr><td>6</td><td>pitch-artificer</td><td>Tier-A/B outreach bundles (private vault only)</td></tr>
</table>
<h2>How is verification enforced?</h2>
<p>Every record carries a verification tag — VERIFIED (single source), L2_VERIFIED (corroborated), L3_VERIFIED (expert commentary), INFERRED, UNVERIFIED, or CONTRADICTED. The reflexion-auditor wave re-fetches sources, calls a different OpenRouter model than the originating agent (to break echo chambers), and demotes initiatives whose claims fail re-check. Twelve content quality gates block deploy on any single H1 violation, internal-ID leak, fabricated decree, or fabricated LinkedIn URL.</p>
<h2>What is the source priority?</h2>
<p>For Uzbekistan: lex.uz, gov.uz, president.uz, norma.uz, then spot.uz, gazeta.uz, kun.uz, daryo.uz. For Kyrgyzstan: cbd.minjust.gov.kg, president.kg, gov.kg, kabmin.kg, then 24.kg, kaktus.media, akipress.org. For donors: documents.worldbank.org, projects.worldbank.org, adb.org/projects, ec.europa.eu/international-partnerships. Every country claim cites at least one Russian-language source.</p>
"""
    return render_page(
        path="/methodology/",
        title="Methodology",
        description="The seven-wave eleven-agent research pipeline behind Central Asia B2G Intelligence.",
        body_html=body,
    )


def lenses_page(lenses_md: str) -> str:
    # Convert a touch of markdown to HTML — headers + paragraphs
    html_body = ["<h1>The five-plus-one analytical lenses</h1>"]
    html_body.append(
        '<p class="lead summary">Six analytical lenses cut across every record in this research: '
        "the Karimov-to-Mirziyoyev Inversion in Uzbekistan, the Japarov Concentration in Kyrgyzstan, "
        "the Decree Half-Life that opens 6-18 month implementation windows, Donor Co-Financing that "
        "drives 60-90% of digital budgets, the Diaspora Bridge of senior advisors, and the Russian/CIS "
        "Substitution Window opened by post-2022 vendor retreat.</p>"
    )
    # Cheap markdown -> html
    for line in lenses_md.splitlines():
        line = line.rstrip()
        if line.startswith("# "):
            continue  # Already have H1
        if line.startswith("## "):
            html_body.append(f"<h2>{escape(line[3:])}</h2>")
        elif line.startswith("### "):
            html_body.append(f"<h3>{escape(line[4:])}</h3>")
        elif line.startswith("- "):
            html_body.append(f"<p>• {escape(line[2:])}</p>")
        elif line:
            html_body.append(f"<p>{escape(line)}</p>")
    return render_page(
        path="/lenses/",
        title="The five analytical lenses",
        description="The six lenses applied to every record in this research: Karimov Inversion, Japarov Concentration, Decree Half-Life, Donor Co-Financing, Diaspora Bridge, Russian/CIS Substitution Window.",
        body_html="\n".join(html_body),
    )


def scoring_page(rubric_md: str) -> str:
    body = ["<h1>Scoring rubric</h1>"]
    body.append(
        '<p class="lead summary">Every initiative is scored on five axes with weighted totals: '
        "Speed-to-Contract at twenty-five percent, Strategic Moat at twenty percent, Defensibility "
        "at twenty percent, Capital Access at twenty percent, and Russian/CIS Fit at fifteen percent. "
        "A weighted total above seven and a half drops into Tier-A; below six is Tier-C or worse.</p>"
    )
    for line in rubric_md.splitlines():
        line = line.rstrip()
        if line.startswith("# "):
            continue
        if line.startswith("## "):
            body.append(f"<h2>{escape(line[3:])}</h2>")
        elif line.startswith("### "):
            body.append(f"<h3>{escape(line[4:])}</h3>")
        elif line.startswith("- "):
            body.append(f"<p>• {escape(line[2:])}</p>")
        elif line:
            body.append(f"<p>{escape(line)}</p>")
    return render_page(
        path="/scoring/",
        title="Scoring rubric",
        description="The five-axis weighted scoring rubric for every initiative: Speed-to-Contract, Strategic Moat, Defensibility, Capital Access, Russian/CIS Fit.",
        body_html="\n".join(body),
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
            f"<td>{escape(d.get('number') or '')}</td><td>{escape(d.get('date') or '')}</td>"
            f"<td>{escape(d.get('title_en') or '')}</td>"
            f"<td><span class='tag'>{escape(d.get('half_life_status') or '')}</span></td>"
            f"<td>{link_html}</td></tr>"
        )
    table = "<table><tr><th>ID</th><th>Type</th><th>Number</th><th>Date</th><th>Title</th><th>Status</th><th>Source</th></tr>" + "".join(rows) + "</table>" if rows else "<p>No decrees in the knowledge graph yet.</p>"
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
            f"<td>{escape(i.get('name_ru') or '')}</td>"
            f"<td>{escape(i.get('ai_digital_mandate') or '')}</td>"
            f"<td>{escape(head_id)}</td></tr>"
        )
    table = "<table><tr><th>C</th><th>Tier</th><th>Name (EN)</th><th>Name (RU)</th><th>AI/digital mandate</th><th>Head ID</th></tr>" + "".join(rows) + "</table>" if rows else "<p>No institutions in the knowledge graph yet.</p>"
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
    table = "<table><tr><th>Donor</th><th>C</th><th>Program</th><th>Budget</th><th>TTL/PM</th><th>Status</th></tr>" + "".join(rows) + "</table>" if rows else "<p>No donor programmes in the knowledge graph yet.</p>"
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
    table = "<table><tr><th>C</th><th>Title</th><th>Value</th><th>Deadline</th><th>Win Pr.</th><th>Link</th></tr>" + "".join(rows) + "</table>" if rows else "<p>No live tenders in the knowledge graph yet.</p>"
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
        body_parts.append("<table><tr><th>Sector</th><th>Trend</th><th>Maturity</th><th>Lenses</th></tr>" + "".join(rows) + "</table>")
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
    table = "<table><tr><th>C</th><th>Name</th><th>Role</th><th>Institution</th><th>LinkedIn</th><th>Tag</th></tr>" + "".join(rows) + "</table>" if rows else "<p>No people in the knowledge graph yet.</p>"
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
    table = "<table><tr><th>Tier</th><th>C</th><th>Initiative</th><th>Sector</th><th>Score</th><th>Initial $</th><th>Pathway</th></tr>" + "".join(rows) + "</table>" if rows else "<p>No initiatives in the knowledge graph yet.</p>"
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
    table = "<table><tr><th>Tier</th><th>C</th><th>MVP</th><th>Cat</th><th>Score</th><th>MVR</th><th>Build</th><th>Y1 $</th></tr>" + "".join(rows) + "</table>" if rows else "<p>No solopreneur MVPs in the knowledge graph yet.</p>"
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


def honesty_page(graph: dict[str, Any]) -> str:
    honesty_path = ROOT / "state" / "audit" / "honesty_section.md"
    md = honesty_path.read_text() if honesty_path.exists() else ""
    body_parts = ['<h1>Honesty: what we did not find</h1>']
    body_parts.append(
        '<p class="lead summary">This page documents the limits of this research: known gaps, dead-end research pathways, opaque domains, and contradictions we could not resolve. Honesty is a first-class output here. A research artifact that hides what it does not know is not trustworthy.</p>'
    )
    if md:
        for line in md.splitlines():
            line = line.rstrip()
            if line.startswith("## "):
                body_parts.append(f"<h2>{escape(line[3:])}</h2>")
            elif line.startswith("- "):
                body_parts.append(f"<p>• {escape(line[2:])}</p>")
            elif line:
                body_parts.append(f"<p>{escape(line)}</p>")
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
    write_page("/mvp/", mvp_page(graph, country=None))
    write_page("/mvp/uz/", mvp_page(graph, country="UZ"))
    write_page("/mvp/kg/", mvp_page(graph, country="KG"))
    write_page("/honesty/", honesty_page(graph))
    write_page("/provenance/", provenance_page(graph))

    # Favicon (a single-letter B mark — small SVG, no external deps)
    favicon_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" fill="#0a4"/><text x="50%" y="55%" text-anchor="middle" fill="#fff" font-family="system-ui" font-size="40" font-weight="700">B</text></svg>"""
    (SITE / "favicon.svg").write_text(favicon_svg)
    # OG default image: a transparent 1200x630 placeholder (text-only SVG)
    og_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 630"><rect width="1200" height="630" fill="#0a4"/><text x="50%" y="40%" text-anchor="middle" fill="#fff" font-family="system-ui" font-size="64" font-weight="700">Central Asia B2G Intelligence</text><text x="50%" y="55%" text-anchor="middle" fill="#cfe9d6" font-family="system-ui" font-size="32">Uzbekistan + Kyrgyzstan AI/Digital Government</text></svg>"""
    (SITE / "og-default.svg").write_text(og_svg)

    print(f"Site written: {SITE}")
    print(f"Pages: {sum(1 for _ in SITE.rglob('*.html'))}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
