# Audit 14 — Conversion / CTA
**Site**: https://avaluev.github.io/ca-b2g-research/  
**Auditor role**: Conversion / CTA specialist  
**Date**: 2026-05-03  

---

## Findings summary

Every page has a citable summary lead (the `<p class="lead summary">` block). No page has a primary CTA button, a persona routing block, a "Cite this research" widget, a visible RSS/refresh link, or a data-download link. The nav lists 15 destination links with no hierarchy — every persona lands on the same flat list and must self-orient. Share links, BibTeX, and inline body-prose CTAs are entirely absent.

---

## 1. Audience–CTA matrix

| Persona | Primary action needed | Top 3 actions (in priority order) |
|---|---|---|
| B2G operator / vendor gov-affairs | Identify which Tier-A initiative to bid first | 1. Open Initiatives filtered to Tier-A → 2. Open matching Procurement tender → 3. Email author to validate approach |
| Donor counterpart (WB, ADB, EU PM) | Map their programme to initiatives that cite it | 1. Open Donors → find own programme → 2. Cross-link to Initiatives citing same donor → 3. Clone repo for offline use |
| Investment team (frontier EM) | Download the structured dataset to model exposure | 1. Download `master.csv` → 2. Read Scoring rubric → 3. Email author for LP-grade memo |
| Central-Asian government decision-maker | Find decrees that authorise their sector's work | 1. Open Decrees UZ or KG → 2. Find initiatives that cite those decrees → 3. Contact author for official briefing |
| Researcher / journalist | Cite specific statistics or methodology | 1. Copy BibTeX citation → 2. Open Provenance for source links → 3. Subscribe to RSS for refresh notifications |

---

## 2. Per-page primary-action mapping (17 pages)

| Page | Current primary action | Status | Recommended primary CTA |
|---|---|---|---|
| `/` Home | Read "Where to start" paragraph | WEAK — no button, no routing | Persona-routing block (see §4) |
| `/initiatives/` | Scan the 100-row table | WEAK — table only, no filter | "Download Tier-A CSV" + "Email about top initiative" |
| `/procurement/` | Scan 50-row tender table | WEAK | "Download tenders CSV" |
| `/donors/` | Scan 49-row table | WEAK | "Download donor CSV" |
| `/people/` | Scan decision-makers | WEAK | "Download decision-makers CSV" |
| `/methodology/` | Read pipeline description | ADEQUATE — informational | "Clone the repo" link (inline, prominent) |
| `/lenses/` | Read five lenses | ADEQUATE — informational | "Apply lenses to Initiatives →" |
| `/scoring/` | Read rubric table | ADEQUATE — informational | "See scored initiatives →" |
| `/decrees/uz/` | Scan decrees table | WEAK | "Download UZ decrees CSV" |
| `/decrees/kg/` | Scan decrees table | WEAK | "Download KG decrees CSV" |
| `/institutions/` | Scan institutions table | WEAK | "Download institutions CSV" |
| `/trends/` | Scan trends table | WEAK | "Download trends JSON" |
| `/mvp/` | Scan 200-row MVP table | WEAK | "Download MVP CSV" |
| `/mvp/uz/` | Scan UZ MVP table | WEAK | "Download UZ MVP CSV" |
| `/mvp/kg/` | Scan KG MVP table | WEAK | "Download KG MVP CSV" |
| `/honesty/` | Read gaps narrative | ADEQUATE — informational | "Contribute a correction (GitHub issue)" |
| `/provenance/` | Read provenance explanation | ADEQUATE — informational | "Browse source files on GitHub" |

**Summary**: 10 of 17 pages have no actionable CTA. The three data-heavy tables (Initiatives, Procurement, Donors) are the highest-traffic destinations and have zero download or contact affordance.

---

## 3. "Cite this research" widget (HTML, pasteable)

Insert once per page, immediately after `<p class="lead summary">`. Use `<details>` so the widget is in the DOM (avoids hidden FAQ penalty) but collapsed by default.

```html
<details class="cite-widget" style="margin:0 0 24px;background:#f7f7f7;border-radius:4px;padding:12px 16px;font-size:13px">
  <summary style="cursor:pointer;font-weight:600;color:#062">Cite this research</summary>
  <div style="margin-top:12px">
    <p style="margin:0 0 6px"><strong>APA</strong></p>
    <pre id="cite-apa" style="margin:0 0 8px;white-space:pre-wrap">Valuev, A. (2026). <em>Central Asia B2G Intelligence: AI and digital government opportunities in Uzbekistan and Kyrgyzstan</em>. https://avaluev.github.io/ca-b2g-research/</pre>
    <p style="margin:8px 0 6px"><strong>MLA</strong></p>
    <pre id="cite-mla" style="margin:0 0 8px;white-space:pre-wrap">Valuev, Alexandr. "Central Asia B2G Intelligence." 2026, avaluev.github.io/ca-b2g-research/.</pre>
    <p style="margin:8px 0 6px"><strong>BibTeX</strong></p>
    <pre id="cite-bib" style="margin:0 0 8px;white-space:pre-wrap">@misc{valuev2026cab2g,
  author    = {Valuev, Alexandr},
  title     = {Central Asia B2G Intelligence},
  year      = {2026},
  url       = {https://avaluev.github.io/ca-b2g-research/},
  note      = {Open research on AI/digital government in Uzbekistan + Kyrgyzstan}
}</pre>
    <button onclick="navigator.clipboard.writeText(document.getElementById('cite-bib').textContent).then(()=>this.textContent='Copied!')" style="background:#0a4;color:#fff;border:0;padding:6px 14px;border-radius:3px;cursor:pointer;font-size:13px">Copy BibTeX</button>
  </div>
</details>
```

The `<details>` element is in the DOM at load time — no hidden FAQ violation. The `onclick` clipboard call needs no external JS library.

---

## 4. Persona-routing landing pattern (home page)

Replace the current "Where to start" paragraph with this block. Insert immediately after the KPI grid.

```html
<h2>Where to start</h2>
<div class="persona-grid" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px;margin:16px 0 32px">
  <a href="/initiatives/" style="display:block;padding:14px 16px;border:1px solid #c8e6d3;border-radius:6px;text-decoration:none;color:#111">
    <div style="font-weight:700;color:#0a4;margin-bottom:4px">B2G Operator / Vendor</div>
    <div style="font-size:13px;color:#444">Find your next government contract — start with 28 Tier-A initiatives.</div>
  </a>
  <a href="/donors/" style="display:block;padding:14px 16px;border:1px solid #c8e6d3;border-radius:6px;text-decoration:none;color:#111">
    <div style="font-weight:700;color:#0a4;margin-bottom:4px">Donor / Development Finance</div>
    <div style="font-size:13px;color:#444">Map your programme against 49 active donor pipelines and their TTLs.</div>
  </a>
  <a href="/scoring/" style="display:block;padding:14px 16px;border:1px solid #c8e6d3;border-radius:6px;text-decoration:none;color:#111">
    <div style="font-weight:700;color:#0a4;margin-bottom:4px">Investment Team</div>
    <div style="font-size:13px;color:#444">Read the scoring rubric, then download the full dataset as CSV.</div>
  </a>
  <a href="/decrees/uz/" style="display:block;padding:14px 16px;border:1px solid #c8e6d3;border-radius:6px;text-decoration:none;color:#111">
    <div style="font-weight:700;color:#0a4;margin-bottom:4px">Government Decision-Maker</div>
    <div style="font-size:13px;color:#444">Browse decree atlases for Uzbekistan or Kyrgyzstan and their AI mandates.</div>
  </a>
  <a href="/methodology/" style="display:block;padding:14px 16px;border:1px solid #c8e6d3;border-radius:6px;text-decoration:none;color:#111">
    <div style="font-weight:700;color:#0a4;margin-bottom:4px">Researcher / Journalist</div>
    <div style="font-size:13px;color:#444">Read the methodology, cite the data, or subscribe to the RSS refresh feed.</div>
  </a>
</div>
```

Remove the old paragraph that begins "Start with Initiatives for the headline list…" — the routing block replaces it entirely.

---

## 5. TL;DR enhancement plan

Current state: every page has a `<p class="lead summary">` immediately under `<h1>`. These are 40–60 words and serve as citable summary leads — the requirement is already met.

Gaps found:
- The Honesty page lead is correct in `<p class="lead summary">` but the next element is a raw markdown-formatted paragraph (`# Absolute Honesty Section…`) that leaked through the renderer. Strip the raw markdown heading from the honesty page body prose.
- The Scoring page renders the rubric table as raw markdown pipe-table text (`| Axis | Weight | Notes |` and `|---|---|---|`) instead of an HTML `<table>`. The lead is fine; the body prose fails.
- The MVP page uses the term "Wizard of Oz" in body prose (line 176 of `/mvp/index.html`), which is on the jargon ban list in `content-quality-gates.md`. Replace with "manual-fulfillment prototype".

No new TL;DR blocks are needed; the existing leads are adequate.

---

## 6. Privacy-respecting share-link pattern

No JS. No tracking pixel. Plain `<a href>` only. Insert at the bottom of `<main>` on every page, above `<footer>`.

```html
<div class="share-row" style="margin:40px 0 0;padding-top:16px;border-top:1px solid #eaeaea;font-size:13px;color:#555">
  Share:
  <a href="https://twitter.com/intent/tweet?url=PAGE_URL&amp;text=PAGE_TITLE" rel="noopener noreferrer" target="_blank" style="margin-left:8px;color:#062">Twitter/X</a>
  &middot;
  <a href="https://www.linkedin.com/sharing/share-offsite/?url=PAGE_URL" rel="noopener noreferrer" target="_blank" style="margin-left:4px;color:#062">LinkedIn</a>
  &middot;
  <a href="mailto:?subject=PAGE_TITLE&amp;body=PAGE_URL" style="margin-left:4px;color:#062">Email</a>
  &middot;
  <a href="/feed.xml" style="margin-left:4px;color:#062">RSS feed</a>
</div>
```

`PAGE_URL` and `PAGE_TITLE` are rendered server-side by `render_site.py` using the existing `canonical` and `title` variables per page. No third-party scripts load. The RSS link doubles as the refresh-subscription affordance required by audit item 7 — this replaces the need for a separate "Get notified" link on every page.

---

## 7. 10 inline body-prose CTAs to add

| # | Page | Insert after sentence | CTA text + target |
|---|---|---|---|
| 1 | `/` Home | "28 initiatives are rated Tier-A — deal-ready." | `— <a href="/initiatives/">see all 28 Tier-A initiatives</a>` |
| 2 | `/` Home | "…primary sources are predominantly Russian-language." | `Read the <a href="/honesty/">Honesty page</a> before acting on any optimistic finding.` |
| 3 | `/initiatives/` | Lead paragraph ends "…a credible 12-month deal path is documented." | `<a href="/procurement/">Cross-check against live tenders</a> before committing to a bid.` |
| 4 | `/initiatives/` | "The scoring rubric is on the Scoring page." | Change "Scoring page" to `<a href="/scoring/">Scoring page</a>` (currently plain text). |
| 5 | `/donors/` | "…the donor's TTL or task team leader is frequently the real customer." | `See <a href="/people/">decision-makers</a> for the named government counterparts.` |
| 6 | `/procurement/` | "…a waste of bid effort." | `Cross-reference with <a href="/initiatives/">Tier-A initiatives</a> to align bid focus.` |
| 7 | `/methodology/` | "Cross-model verification via OpenRouter caps the OpenRouter spend at twenty dollars per run." | `The full pipeline is open-source — <a href="https://github.com/avaluev/ca-b2g-research">clone it on GitHub</a>.` |
| 8 | `/scoring/` | Lead paragraph ends "…below six is Tier-C or worse." | `<a href="/initiatives/">Browse all scored initiatives</a> or <a href="/provenance/">verify a claim</a>.` |
| 9 | `/honesty/` | "A research artifact that hides what it does not know is not trustworthy." | `If a gap is incorrect or resolvable, <a href="https://github.com/avaluev/ca-b2g-research/issues">open a GitHub issue</a>.` |
| 10 | `/mvp/` | Lead paragraph ends "…a price point grounded in local purchasing power." | `See the <a href="/initiatives/">institutional B2G track</a> for larger-scale opportunities.` |

---

## 8. Download affordance plan

The CRM CSVs already exist at `outputs/crm/`. They are not linked from any HTML page.

Add to `render_site.py` a `_download_block(page_slug)` helper that emits:

```html
<div class="dl-row" style="margin:16px 0 24px;font-size:13px">
  Download:
  <a href="https://github.com/avaluev/ca-b2g-research/raw/main/outputs/crm/FILENAME.csv" style="color:#062">CSV</a>
  &middot;
  <a href="https://github.com/avaluev/ca-b2g-research/raw/main/state/initiatives/initiatives.json" style="color:#062">JSON</a>
</div>
```

Map per page: Initiatives → `tier_a_only.csv` + `initiatives.json`; Procurement → `top_speed.csv`; Donors → `programs.json`; People → `people_master.csv`; Trends → `convergent_windows.csv`.

Insert the block immediately after each page's `<p class="lead summary">` and before the first `<h2>`.

---

## 9. Feed discoverability

`feed.xml` is referenced in `<head>` via `<link rel="alternate">` — not visible on page. The share-row block in §6 adds a visible "RSS feed" link on every page, resolving item 7 of the mandate.

---

## Implementation notes for `render_site.py`

1. Add `_cite_widget(page_url, page_title)` function — returns the HTML in §3 with per-page URL/title substituted.
2. Add `_share_row(page_url, page_title)` function — returns the HTML in §6.
3. Add `_download_block(slug)` function — returns the HTML in §8 with slug-based filename lookup.
4. In `render_page()`, call all three helpers and splice into the body at the documented positions.
5. Replace the home "Where to start" paragraph with the persona-grid in §4.
6. Fix the Honesty page: strip raw markdown from body prose.
7. Fix the Scoring page: render the rubric table as `<table>` HTML, not pipe-table text.
8. Fix the MVP page: replace "Wizard of Oz" with "manual-fulfillment prototype".
