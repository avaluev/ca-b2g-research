# Audit 10 — HTML Code Quality
**Auditor**: HTML Code Quality (member 10 of 16)
**Date**: 2026-05-03
**Scope**: `render_site.py` (authoritative source) + rendered outputs in `outputs/site/`
**Note**: `render_site.py` is newer than the rendered outputs (script mtime > index mtime). Findings are reported against both; patches apply to the script.

---

## W3C Validation Summary (estimated)

| Issue | Count | Severity |
|---|---|---|
| `<span class="brand">` as non-interactive nav label (rendered outputs only — fixed in script) | 17 pages | Warning |
| `<table>` with no `<thead>`, `<tbody>`, or `<caption>` | all 11 data tables | Error |
| `<th>` with no `scope` attribute | all 44 `<th>` elements across 11 tables | Error |
| `<p>•` bullets masquerading as `<ul><li>` | ~102 instances across lenses, scoring, honesty | Warning |
| JSON-LD `@graph` contains two `WebSite` nodes with same `@id` on home page | 1 | Warning |
| `og:image` references `og-default.png` but only `og-default.svg` exists | all 17 pages | Error |
| No `<time datetime>` for any date in content or footer | site-wide | Warning |
| No `<abbr title>` for any domain acronym | site-wide | Warning |
| Inline `style=` attribute on `<p>` in MVP pages | 3 pages | Warning |

Estimated W3C errors/warnings before patch: **~180 errors, ~140 warnings** (bulk from `<th>` scope + no thead/tbody).

---

## Landmark Map

### Current (rendered outputs)
```
<body>
  <header class="nav">
    <nav>                 ← no aria-label
      <span .brand>       ← non-interactive, not a link
      <a> × 15            ← nav links
    </nav>
  </header>
  <main class="container">
    <h1> ... <h2> ...     ← no <article> or <section> wrapping
  </main>
  <footer class="site">
    <p>...                ← no <address> for contact
  </footer>
</body>
```

### Current (script — already improved)
- Skip link added (`<a class="skip-link" href="#main-content">`)
- `<main id="main-content">` added
- `<nav aria-label="Main navigation">` added
- Brand rendered as `<a>` not `<span>`
- `:focus-visible` rule and nav tap-target min-height 44 px added

### Ideal (still missing in script)
```
<body>
  <a class="skip-link" href="#main-content">Skip to main content</a>  ← present
  <header role="banner">                       ← role redundant on <header> but harmless
    <nav aria-label="Main navigation">         ← present
  </header>
  <main id="main-content">                     ← present
    <article>  or  <section aria-labelledby="h2-id">
      content
    </article>
  </main>
  <footer role="contentinfo">                  ← redundant but harmless; <address> missing
</body>
```

Missing landmarks: `<article>` / `<section>` wrappers for body content; `<address>` in footer.

---

## Heading Hierarchy Audit

All pages: H1 present and unique. No H3 used anywhere. H2 sections present and relevant.
No heading is skipped (H1 → H2 direct). No H3 used in any page — correct given page depth.

Issue on **scoring** and **lenses** pages: markdown `### ` headings in source `.md` files would render as H3, but the current markdown parser in `lenses_page()` / `scoring_page()` does handle `### ` → `<h3>`. These source files contain no `### ` headings currently, so no skip occurs. Status: **PASS**.

---

## 15 Specific HTML Patches

### P1 — `<table>` missing `<thead>`, `<tbody>`, `<caption>` (11 tables site-wide)

**Location**: `render_site.py`, all `table =` string literals, e.g. L444, L464, L503, L515, L536, L543, L575, L601, L638, L680.

**Before** (example from `decrees_page`, L444):
```python
table = "<table><tr><th>ID</th><th>Type</th><th>Number</th><th>Date</th>"
        "<th>Title</th><th>Status</th><th>Source</th></tr>" + "".join(rows) + "</table>"
```

**After**:
```python
table = (
    "<table>"
    "<caption>Decrees — " + cname + "</caption>"
    "<thead><tr>"
    "<th scope='col'>ID</th><th scope='col'>Type</th><th scope='col'>Number</th>"
    "<th scope='col'>Date</th><th scope='col'>Title</th>"
    "<th scope='col'>Status</th><th scope='col'>Source</th>"
    "</tr></thead>"
    "<tbody>" + "".join(rows) + "</tbody>"
    "</table>"
)
```

Apply the same `<thead>/<tbody>/<caption>` pattern to all 11 table builders.

---

### P2 — `<th>` missing `scope` attribute (44 `<th>` elements across all tables)

Already included in P1. All column headers need `scope="col"`. No row headers in current tables.

---

### P3 — `<p>•` bullets must be `<ul><li>` (scoring, lenses, honesty pages)

**Location**: `render_site.py` L385 (shared by both `lenses_page` and `scoring_page`); L731 (honesty bullet loop).

**Before** (L385):
```python
elif line.startswith("- "):
    html_body.append(f"<p>• {escape(line[2:])}</p>")
```

**After**: Collect consecutive `- ` lines into a single `<ul>`:
```python
# Replace the per-line append with a list-accumulator pattern:
# When a "- " line is encountered, open a <ul> if not already open.
# When a non-"- " line follows, close the </ul> first.
elif line.startswith("- "):
    if not in_list:
        html_body.append("<ul>")
        in_list = True
    html_body.append(f"<li>{escape(line[2:])}</li>")
else:
    if in_list:
        html_body.append("</ul>")
        in_list = False
    if line:
        html_body.append(f"<p>{escape(line)}</p>")
# After loop: if in_list: html_body.append("</ul>")
```

This affects ~102 `<p>•` instances.

---

### P4 — JSON-LD: duplicate `WebSite` node on home page

**Location**: `render_site.py` L190–L199 (`render_page` signature) + L320–L325 (home page call).

**Root cause**: Home page passes `page_type="WebSite"` to `render_page()`, which adds a 5th `@graph` item typed `WebSite`. The 3rd item in the graph is already `WebSite` with `@id …/#website`. The 5th item duplicates that `@id`, confusing structured data parsers.

**Fix**: Change home page call at L320:
```python
# Before:
page_type="WebSite",
# After:
page_type="Article",
```
Or, in `jsonld_graph()`, skip emitting the page-level node when `page_type == "WebSite"` to avoid the collision.

---

### P5 — OG image references `.png` but only `.svg` exists

**Location**: `render_site.py` L231.

**Before**:
```python
<meta property="og:image" content="{SITE_URL}/og-default.png">
```

**After**:
```python
<meta property="og:image" content="{SITE_URL}/og-default.svg">
```

Also update L236 (twitter:image) and L804 where the SVG file is written as `og-default.svg`. Note: many OG scrapers do not support SVG. Preferred fix is to convert the SVG to a raster PNG at build time, but correcting the extension is the minimum fix.

---

### P6 — `<time datetime>` for dates in decree tables and footer

**Location**: `render_site.py` L429 (decree date cell), L258 (footer "Built" date).

**P6a — Decree date cells** (L429):
```python
# Before:
f"<td>{escape(d.get('date') or '')}</td>"
# After:
date_val = d.get('date') or ''
f"<td><time datetime='{escape(date_val)}'>{escape(date_val)}</time></td>"
```

**P6b — Footer build date** (L258):
```python
# Before:
Built {TODAY}.</p>
# After:
Built <time datetime="{TODAY}">{TODAY}</time>.</p>
```

---

### P7 — `<abbr title>` for first-use acronyms

No `<abbr>` tags exist anywhere on the site. High-frequency domain acronyms needing first-use wrapping:

| Acronym | Title | Occurrences |
|---|---|---|
| B2G | Business-to-Government | 44 |
| AI | Artificial Intelligence | 392 |
| ADB | Asian Development Bank | 38 |
| WB | World Bank | 23 |
| PIU | Project Implementation Unit | 20 |
| CIS | Commonwealth of Independent States | 18 |
| TTL | Task Team Leader | 13 |
| MVP | Minimum Viable Product | 12 |
| MVR | Minimum Viable Representation | 12 |
| EBRD | European Bank for Reconstruction and Development | 10 |
| ICT | Information and Communications Technology | 8 |
| LLM | Large Language Model | 6 |
| SOE | State-Owned Enterprise | 2 |

**Location**: These all appear in per-page body strings in `render_site.py`. Add a `abbr_wrap(text, term, title)` utility and apply to the lead summary paragraph and first H2 paragraph of each page where the acronym first appears.

**Minimal patch** — helper function (add after L57):
```python
_ABBR_DONE: set[str] = set()

def abbr(term: str, title: str) -> str:
    """Wrap term in <abbr title> on first use per render run; plain text thereafter."""
    if term in _ABBR_DONE:
        return escape(term)
    _ABBR_DONE.add(term)
    return f'<abbr title="{escape(title)}">{escape(term)}</abbr>'
```
Reset `_ABBR_DONE.clear()` at start of each `write_page()` call (per-page first-use).

---

### P8 — Inline `style=` attribute in MVP pages

**Location**: `render_site.py` L705 (inside `mvp_page()`).

**Before**:
```python
<p style="font-size: 13px; color: #555;"><em>Methodology: ...
```

**After** — move to CSS block (L68–L103) and use a class:
```css
/* Add to CSS constant: */
.footnote{font-size:13px;color:#555}
```
```python
# L705:
<p class="footnote"><em>Methodology: ...
```

---

### P9 — `<nav aria-label>` missing in rendered output (fixed in script, re-render needed)

**Status**: Fixed in script (L248). Rendered outputs are stale — re-run `python3 scripts/render_site.py`.

---

### P10 — Skip link missing in rendered output (fixed in script, re-render needed)

**Status**: Fixed in script (L247, CSS L101–L102). Rendered outputs are stale.

---

### P11 — Brand `<span>` should be `<a>` in rendered output (fixed in script, re-render needed)

**Status**: Fixed in script (L249). Rendered outputs are stale.

---

### P12 — `<address>` for contact info in footer

**Location**: `render_site.py` L255–L259.

**Before**:
```python
<footer class="site">
<p>Open research on AI/digital government opportunities ...
Apache 2.0 — <a href="...">...</a>.
Built {TODAY}.</p>
</footer>
```

**After**:
```python
<footer class="site">
<p>Open research on AI/digital government opportunities in Uzbekistan + Kyrgyzstan.
Apache 2.0 — <a href="{OPERATOR_GITHUB}/ca-b2g-research">{OPERATOR_GITHUB.replace('https://', '')}/ca-b2g-research</a>.</p>
<address>Contact: <a href="mailto:{OPERATOR_EMAIL}">{OPERATOR_EMAIL}</a> ·
<a href="{OPERATOR_LINKEDIN}">LinkedIn</a></address>
<p>Built <time datetime="{TODAY}">{TODAY}</time>.</p>
</footer>
```

---

### P13 — `<section aria-labelledby>` wrappers for long-form pages

Pages with 4+ H2 sections (scoring: 8, lenses: 7, honesty: 8) benefit from `<section>` wrapping each H2 block for landmark navigation. No implementation change is strictly required for validity, but it improves screen-reader navigation.

**Location**: Markdown-to-HTML loops in `lenses_page()` (L366–L381), `scoring_page()` (L393–L410), `honesty_page()` (L722–L731).

**Pattern**:
```python
# Before each h2 append, close prior section and open new one:
if line.startswith("## "):
    sec_id = slugify(line[3:])
    if in_section:
        html_body.append("</section>")
    html_body.append(f'<section aria-labelledby="{sec_id}">')
    html_body.append(f'<h2 id="{sec_id}">{escape(line[3:])}</h2>')
    in_section = True
```

---

### P14 — `<figure>/<figcaption>` opportunities

No images or charts exist in the rendered output. The KPI grid cards (`<div class="kpi">`) on the home page are effectively data figures and would benefit from `<figure>` semantics when an actual chart is added. No change needed now, but note for when Chart.js is integrated.

---

### P15 — Table `<caption>` text must not duplicate visible heading above

When adding captions (P1), ensure the caption text is descriptive but differs from the H2 above it (e.g., H2 "Decrees" + `<caption>Decree list — Uzbekistan` is fine; `<caption>Decrees` directly repeating the H2 is redundant noise for screen readers). Use country-qualified captions.

---

## Acronym `<abbr>` Candidate List

All terms below appear untagged in current HTML. Tag on first use per page.

| Term | Full form |
|---|---|
| `B2G` | Business-to-Government |
| `AI` | Artificial Intelligence |
| `ADB` | Asian Development Bank |
| `WB` | World Bank |
| `PIU` | Project Implementation Unit |
| `CIS` | Commonwealth of Independent States |
| `TTL` | Task Team Leader |
| `MVP` | Minimum Viable Product |
| `MVR` | Minimum Viable Representation |
| `EBRD` | European Bank for Reconstruction and Development |
| `ICT` | Information and Communications Technology |
| `LLM` | Large Language Model |
| `SOE` | State-Owned Enterprise |
| `RFP` | Request for Proposal |
| `CRM` | Customer Relationship Management |
| `SaaS` | Software as a Service |
| `FAANG` | Meta/Apple/Amazon/Netflix/Google (tech employers) |

---

## `<time>`, `<cite>`, `<figure>` Usage Opportunities

| Element | Where | Current | Recommended |
|---|---|---|---|
| `<time datetime>` | Decree date cells (all tables) | plain text | `<time datetime="YYYY-MM-DD">` |
| `<time datetime>` | Footer "Built DATE" | plain text | `<time datetime="{TODAY}">` |
| `<time datetime>` | `dateModified` meta (already in `<head>`) | meta only | also add visible "Last updated" `<time>` near H1 |
| `<cite>` | Source links ("primary source") | bare `<a>` | `<cite><a href="...">primary source</a></cite>` |
| `<figure>` | KPI grid on home | `<div class="kpi-grid">` | `<figure>` wrapper when chart added |
| `<figure>` | Wave diagram in methodology | absent | add ASCII/SVG diagram in `<figure><figcaption>` |

---

## DOM-Size Statistics

| Page | Element count | Notes |
|---|---|---|
| `mvp/` | 2,085 | Largest page — 200 MVP rows × ~10 cells |
| `mvp/kg/` | 1,086 | |
| `mvp/uz/` | 1,086 | |
| `initiatives/` | 961 | 100 rows × ~7 cells |
| `institutions/` | 803 | |
| `decrees/uz/` | 622 | 56 rows × ~7 cells |
| `people/` | 538 | |
| `decrees/kg/` | 502 | |
| `procurement/` | 460 | |
| `donors/` | 403 | |
| `index.html` | 90 | Lightest |
| **Total (17 pages)** | **9,576** | Well within budget |

No DOM-size concerns. All pages are within safe thresholds for rendering and parsing.

---

## Summary Priority

| Priority | Issue | Patch |
|---|---|---|
| HIGH | `<thead>/<tbody>/<caption>` missing on all tables | P1 |
| HIGH | `<th scope>` missing on all 44 header cells | P2 (in P1) |
| HIGH | `og:image` 404 (.png referenced, .svg present) | P5 |
| HIGH | JSON-LD duplicate `WebSite` node on home | P4 |
| MEDIUM | `<p>•` bullets not in `<ul><li>` (~102 instances) | P3 |
| MEDIUM | No `<abbr>` for any domain acronym | P7 |
| MEDIUM | No `<time datetime>` for dates | P6 |
| MEDIUM | Inline `style=` on MVP footnote | P8 |
| LOW | No `<address>` in footer | P12 |
| LOW | `<section>` wrappers for long-form pages | P13 |
| LOW | `<cite>` for source links | P6 / `<cite>` section |
| DONE (re-render) | Skip link, nav aria-label, brand as `<a>`, focus-visible | P9–P11 |
