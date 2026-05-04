# IA Audit — Central Asia B2G Intelligence
**Auditor role:** Information Architect | **Date:** 2026-05-03
**Site:** https://avaluev.github.io/ca-b2g-research/

---

## Sitemap (current state)

```
/ (Home)
├── /methodology/
├── /lenses/
├── /scoring/
├── /decrees/
│   ├── /decrees/uz/        ← no /decrees/ landing page exists
│   └── /decrees/kg/
├── /institutions/
├── /donors/
├── /procurement/
├── /trends/
├── /people/
├── /initiatives/
├── /mvp/
├── /honesty/
└── /provenance/

Utility assets (not in nav):
  sitemap.xml, robots.txt, llms.txt, llms-full.txt, feed.xml,
  manifest.webmanifest, favicon.svg, humans.txt
```

No `/decrees/` section landing exists (direct child dirs are `/uz/` and `/kg/`).
No `/404.html`. No `/search/`. No HTML sitemap page.

---

## First-time visitor 5-second test

A visitor lands on `/` and sees:

- Brand: "Central Asia B2G" (top-left, small)
- 15 nav links across a single line, wrapping on any viewport below ~1400 px
- H1: "Central Asia B2G Intelligence"
- Green-highlighted lead paragraph (40–60 words, correctly placed)
- KPI grid: 9 numbers

**What the visitor understands:** Something about research and numbers. The KPIs are unlabelled by context — "100 Decrees", "49 Donor programmes" — against an unknown frame. The nav bar reveals nothing about grouping or purpose before clicking.

**What the visitor does NOT understand:** Whether this is a data tool, a consultancy pitch deck, a research download, or a market-intelligence subscription. The phrase "B2G Initiatives" in the nav is opaque to anyone who does not already know what B2G means. "Solo MVPs" next to "B2G Initiatives" signals a scope jump with no explanation.

**Verdict:** Passes the smell test for a returning specialist; fails for a first-time visitor or an AI crawler trying to extract the value proposition.

---

## Nav redesign mockup

Current: 15 flat links. Recommended: 5 top-level groups + 1 CTA.

```
Central Asia B2G  |  Research ▾  |  Country Maps ▾  |  Opportunities ▾  |  Integrity ▾  |  GitHub →
```

**Dropdown: Research**
- Methodology
- Lenses
- Scoring
- Trends

**Dropdown: Country Maps**
- Decrees (UZ + KG) → /decrees/   [new landing]
- Institutions         → /institutions/
- People & Contacts    → /people/
- Donors               → /donors/

**Dropdown: Opportunities**
- B2G Initiatives (Top 100)  → /initiatives/
- Live Tenders               → /procurement/
- Solo MVPs                  → /mvp/

**Dropdown: Integrity**
- Honesty (What We Missed)   → /honesty/
- Provenance & Sources       → /provenance/

**Renderer change required** in `scripts/render_site.py`, `NAV_LINKS` list (line 103) and the nav HTML block (lines 205–209). Also requires adding dropdown CSS (no JS needed if using `<details>/<summary>` or CSS-only hover pattern).

---

## Per-page IA score (1–10)

| Page | URL | Score | Key issue |
|------|-----|-------|-----------|
| Home | `/` | 6/10 | No nav grouping; KPI grid lacks context sentence; "B2G" unexpanded on first view |
| Methodology | `/methodology/` | 8/10 | Well-structured; wave table is clear; no breadcrumb below H1 |
| Lenses | `/lenses/` | 7/10 | Good content; no breadcrumb; label "Lenses" is cryptic in nav |
| Scoring | `/scoring/` | 7/10 | Table clear; no cross-link to Initiatives |
| Decrees UZ | `/decrees/uz/` | 5/10 | No section landing at `/decrees/`; no breadcrumb; no link to KG counterpart within body |
| Decrees KG | `/decrees/kg/` | 5/10 | Same as above; "Decrees KG" in nav gives no hint of content volume |
| Institutions | `/institutions/` | 6/10 | Single combined page; people IDs in Head ID column are plain text, not hyperlinks |
| Donors | `/donors/` | 7/10 | Good summary lead; TTL column has `[TTL_NOT_FOUND]` noise in 30+ rows |
| Procurement | `/procurement/` | 6/10 | Label "Procurement" undersells; "Live tenders" is more informative |
| Trends | `/trends/` | 6/10 | Nav label "Trends" is generic; page title differs from nav label |
| People | `/people/` | 5/10 | Institution IDs (e.g. `KG-UDP`) are plain text, not links to `/institutions/` |
| B2G Initiatives | `/initiatives/` | 7/10 | Good lead; no filter/sort UI; Tier tag visible but no link to Scoring rubric |
| Solo MVPs | `/mvp/` | 5/10 | "Solo MVPs" label is jargon; "Solopreneur Bootstraps" or "Quick-Win Products" more legible; honesty page flag `Wizard of Oz` term visible in body — jargon violation |
| Honesty | `/honesty/` | 6/10 | Excellent content; raw markdown artifacts visible (`###`, `**`, `---`) — renderer not converting inner markdown |
| Provenance | `/provenance/` | 7/10 | Good concept; label predicts content well for specialists |

**Average: 6.3 / 10**

---

## Internal-link graph density assessment

Cross-record linking is near-zero. Findings:

- **People → Institutions:** Zero hyperlinks. The "Institution" column in `/people/` shows raw IDs (`KG-UDP`, `UZ-MINTSIFRY`) as plain text. Every ID should be a link to `/institutions/#<id>`.
- **Institutions → People:** Zero hyperlinks. "Head ID" column (`uz-sherzod-shermatov`) is plain text, not linked to the corresponding row in `/people/`.
- **Decrees → Institutions:** Zero hyperlinks. Decrees reference authorising agencies in prose but not via `<a>` to institution records.
- **Initiatives → Decrees:** Two nav-level links only (to `/decrees/uz/` and `/decrees/kg/` from the global nav). Zero initiative rows link to the specific decree that authorises them.
- **Initiatives → People:** Zero hyperlinks. Every initiative has a buyer decision-maker but the name is not linked to `/people/`.
- **Donors → Initiatives:** Zero hyperlinks.
- **Procurement → Initiatives:** Zero hyperlinks. Tenders map to initiatives by implication, never by `<a>`.

**Graph density: 0/10 cross-record links in the body HTML.** The knowledge graph exists in JSON but the site renders flat tables with no hypertext.

---

## 12 Prioritised fixes

### P0 — Ship-blocking or high-scent failures

**P0-1: Add cross-record hyperlinks to People, Institutions, Initiatives tables.**
In `scripts/render_site.py`, when rendering Institution IDs and Head IDs, wrap plain-text ID values in anchors pointing to the appropriate section or future detail page. Minimum viable: link Head IDs in `/institutions/` to the anchor `#<person-id>` within `/people/`, and link Institution column in `/people/` to `#<institution-id>` within `/institutions/`. Affected function: wherever `<table>` rows for these entities are generated.

**P0-2: Create `/decrees/` section landing page.**
Add `outputs/site/decrees/index.html` with a 50-word summary, count of UZ vs KG decrees, and two prominent cards linking to `/decrees/uz/` and `/decrees/kg/`. Add `("/decrees/", "Decrees")` to `NAV_LINKS` or the new grouped nav. Without this, `/decrees/uz/` is an orphan — a visitor navigating up from the URL gets a 404.

**P0-3: Create `/404.html`.**
GitHub Pages serves a default 404. A custom page should match the site nav and offer a link to Home, Initiatives, and the Sitemap page. File goes directly in `outputs/site/404.html` (no subdirectory).

**P0-4: Fix Honesty page raw markdown rendering.**
`/honesty/index.html` contains literal `###`, `**text**`, and `---` strings in `<p>` tags. The renderer passes pre-formatted markdown as body text. In `scripts/render_site.py`, the honesty section content must be converted (either via `markdown` lib or manual replacement) before injecting into the HTML template.

### P1 — High-impact IA improvements

**P1-5: Collapse nav from 15 flat links to 5 grouped dropdowns.**
Implement the mockup in the "Nav redesign" section above. Modify `NAV_LINKS` and `render_page()` in `scripts/render_site.py`. CSS-only hover dropdowns require ~30 lines of CSS added to the `CSS` constant. No JavaScript required.

**P1-6: Add visible breadcrumb component on every page.**
JSON-LD BreadcrumbList is already emitted (good). The visual breadcrumb trail is absent. Add an `<nav aria-label="breadcrumb">` block directly after `<main class="container">` and before `<h1>`. Renderer change: add `breadcrumb_html` output from `render_page()` using the existing `breadcrumbs` parameter already threaded through to JSON-LD.

**P1-7: Create section landing pages at `/institutions/`, `/donors/`, `/people/`.**
`/institutions/` already has an `index.html` but serves the full table. Split into: (a) a landing summary with counts by tier and country and two anchor links (`#uzbekistan`, `#kyrgyzstan`), then (b) the full table below the fold. Same pattern for `/donors/` and `/people/`. This improves scent and reduces cognitive load.

**P1-8: Rename nav labels for clarity.**
`Procurement` → `Live Tenders` (matches the H1 of the target page: "Live procurement").
`Solo MVPs` → `Quick-Start Products` or `Bootstrappable MVPs` (removes insider jargon).
`Lenses` → `Analytical Lenses` (adds one word, removes ambiguity).
Change in `NAV_LINKS` in `scripts/render_site.py` line 103–119.

**P1-9: Add initiative-to-decree and initiative-to-person links in `/initiatives/` table.**
The initiatives table has columns for sector and pathway but no linked references to the authorising decree or target person. Add two columns: "Decree" (linked to the specific decree anchor) and "Buyer" (linked to the person record). This turns the initiative table into the connective hub of the site.

### P2 — Recommended enhancements

**P2-10: Add Pagefind static search.**
Pagefind (https://pagefind.app) runs as a post-build step: `npx pagefind --site outputs/site`. It indexes all HTML, adds a `<link>` to a generated CSS/JS bundle, and requires a `<div id="search"></div>` in a search widget page. Add `outputs/site/search/index.html` as a new page. Add to nav under "Research" dropdown. Build-time cost: ~2 seconds; zero runtime server cost.

**P2-11: Add HTML sitemap page at `/sitemap/`.**
XML sitemap exists at `sitemap.xml` but human-readable HTML sitemap is absent. A one-page sitemap listing all 17 pages with one-sentence descriptions aids discovery for both humans and AI crawlers. Wire into footer link.

**P2-12: Expand footer to include sitemap, license, contributing CTA, and contact.**
Current footer: 2 lines (license + GitHub link). Add: (a) link to `/sitemap/` (P2-11), (b) `<a href="https://github.com/avaluev/ca-b2g-research/issues">Suggest a correction</a>`, (c) email contact link using the operator email already in `OPERATOR_EMAIL` env var. Renderer change: modify the footer template in `render_page()` at line 251–254 of `scripts/render_site.py`.

---

## Summary

The content quality is high; the navigational structure impedes it. The single most impactful fix is P0-1 (cross-record hyperlinks): the knowledge graph already knows that `uz-sherzod-shermatov` heads `UZ-MINTSIFRY` which authorises `UZ-UP-2025-189` which is the basis for initiative `AI Labs at 15 Universities` — but the site renders these as four disconnected flat tables. Wiring them up with `<a href>` costs one rendering pass and turns a reference corpus into a navigable intelligence tool.
