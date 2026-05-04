# Mobile-First QA Audit — Central Asia B2G Intelligence
**Auditor**: Mobile-First QA  
**Date**: 2026-05-03  
**Site**: https://avaluev.github.io/ca-b2g-research/  
**CSS source**: `scripts/render_site.py` → `CSS` constant (lines 68–101)

---

## 1. Existing `@media (max-width:640px)` Rule — Critique

Current rule (line 100):
```css
@media (max-width:640px){h1{font-size:28px}h2{font-size:20px}}
```

**What it does**: Reduces H1 from 36px → 28px and H2 from 24px → 20px. That is all.

**What is missing**:
- No nav collapse — 15 links + brand wrap into 2–4 rows at 320px, consuming 80–120px of sticky viewport height and burying every page's H1 below the fold.
- No table overflow — tables render at `width:100%` but `table-layout` is not `fixed`; 7-column decree/initiative tables force the browser to fit all columns into 280px of usable content width (320px minus 40px padding), resulting in single-character columns or horizontal overflow bleeding outside `.container`.
- No tap target enlargement — nav `<a>` elements inherit `font-size:14px` with `gap:12px` and no explicit `min-height`, giving effective tap areas of roughly 20×14px — less than half the WCAG 2.5.5 minimum of 44×44px.
- KPI grid `minmax(160px,1fr)`: at 320px usable width of 280px, two 160px columns already require a 0px gap — any label text wider than ~140px clips or wraps badly.
- Body font size not explicitly set — inherits from `html` which has no explicit `font-size`. Browsers default to 16px but `-webkit-text-size-adjust:100%` only prevents auto-scaling; it does not guarantee 16px in all WebView contexts.
- No `line-height` adjustment for narrow columns; current `1.55` on body is fine, but `.kpi .lbl` at `12px` / 1.55 is a readability concern at narrow widths.
- No `max-width:100%; overflow:hidden` on images or SVGs — `og-default.svg` and `favicon.svg` are not displayed as `<img>` in body, but any future inline SVG or `<img>` has no safe default.
- No `padding` reduction on `.container` — current `padding:24px 20px` on a 320px screen leaves only 280px usable; reducing to `padding:16px` at ≤640px recovers 8px each side.

---

## 2. Per-Breakpoint Issue List

### 320px — iPhone SE (critical path)

1. **Nav collapse FAIL**: 15 links + brand span ~3 rows of wrapping flex; sticky header consumes ~110px, pushing H1 off-screen on every page.
2. **Decree/Initiative tables overflow**: 7-column tables at `width:100%` produce columns of ~30px each — unreadable; no `overflow-x:auto` wrapper exists.
3. **KPI grid crowding**: Two 160px columns in 280px usable space = 0px gap remaining; `.kpi .num` at 24px bold wraps on long labels (e.g. "Decision-makers").
4. **Tap targets**: Nav `<a>` effective area ≈ 20×14px. All links in body text also fail — no padding on `a` within `p`.
5. **Lead summary padding**: `.lead.summary` at `padding:12px 16px` — fine, but `font-size:18px` at 320px produces ~14 chars/line, which is acceptable.
6. **H3 at 18px**: `margin:24px 0 8px` adds 24px above — at 320px this wastes vertical space; reduce to `margin:16px 0 6px` for mobile.
7. **Footer links**: `footer.site` links have no tap padding; link text is the full GitHub URL, wrapping unpredictably.
8. **`.tag` badges**: `padding:2px 8px` at `font-size:12px` → ~24×18px tap area, below 44px minimum.
9. **Table `th`/`td` padding**: 8px top/bottom is borderline; header row combined with 7 columns at 320px = columns of ~25px each.
10. **No `<meta name="theme-color">`** in rendered HTML (manifest has `theme_color` but the `<meta>` is absent from `render_page()`).

### 375px — iPhone 12 Mini

1. Nav still wraps to 2 rows (~80px sticky height); H1 partially below fold.
2. 7-column tables: columns are ~40px each — still unreadable without horizontal scroll.
3. KPI grid: 280→335px usable; two 160px columns fit with ~15px gap. Acceptable but tight.
4. Tap targets: still fail for all nav links.
5. `.lead.summary font-size:18px` — comfortable at 375px.

### 414px — iPhone 14 Pro Max

1. Nav may fit in ~1.5 rows depending on link text length; still wraps.
2. Tables: 374px usable — 7 columns at ~50px each; ID column and Status column are now functional.
3. KPI grid: two columns with comfortable gap.
4. Tap targets: still fail for nav links (no `min-height` or `padding` set).
5. First acceptable breakpoint for readable body prose.

### 768px — iPad Portrait

1. Nav fits in one row (868px max-width flex); no wrapping.
2. Tables: all 7 columns readable.
3. KPI grid: `repeat(auto-fit,minmax(160px,1fr))` → 4 columns (768−40)/160 = ~4.55, so 4 fit. Fine.
4. Tap targets: still technically fail for nav links, but stylus usage reduces risk.
5. `.container max-width:880px` — content spans nearly full width at 768px (768−40=728px). Readable.

### 1024px — iPad Landscape

1. No issues. Nav fits. Tables readable. KPI grid shows 5–6 columns.
2. `.container` max-width 880px centers with 72px margins each side. Fine.

### 1440px — Desktop

1. No issues. Full layout as designed.
2. Nav `max-width:1200px` vs `.container max-width:880px` mismatch is intentional (nav spans wider than body). Acceptable.

---

## 3. Tap-Target Audit — Home Page Interactive Elements

| Element | Selector | Current size (est.) | WCAG 2.5.5 pass? | Fix |
|---|---|---|---|---|
| Brand link | `header.nav .brand` | 120×22px | YES (wide, short) | Add `padding:11px 0` to reach 44px height |
| Nav link (15×) | `header.nav a` | ~80×20px | NO (height <44px) | `padding:12px 6px; min-height:44px` |
| Body `<a>` in `<p>` | `p a`, `.lead a` | text-height ~22px | NO | `padding:4px 0` or wrap in larger click area |
| `.tag` badges | `.tag` | ~60×24px | NO | `padding:8px 10px; min-height:44px` when tappable |
| Footer `<a>` (repo link) | `footer.site a` | ~20×18px | NO | `padding:8px 0; display:inline-block` |
| No buttons or form inputs | — | — | N/A | — |

---

## 4. Proposed Mobile-First CSS Additions — Full Code (112 lines)

Paste this **after** the existing `@media` block inside the `CSS` constant in `render_site.py`.

```css
/* ── MOBILE-FIRST ADDITIONS ─────────────────────────────────── */

/* 4a. Body text floor & safe tap padding on all inline links */
body{font-size:16px}
a{padding:2px 0}

/* 4b. Tap target: body links get minimum height via line-box */
p a,li a,.lead a{padding:4px 0;display:inline-block;line-height:1.4}

/* 4c. Images and SVGs scale safely */
img,svg{max-width:100%;height:auto;display:block}

/* 4d. Table horizontal-scroll container (applied in HTML — see §6) */
.table-scroll{overflow-x:auto;-webkit-overflow-scrolling:touch;margin:12px 0 24px}
.table-scroll table{margin:0;white-space:nowrap}

/* 4e. Footer link tap target */
footer.site a{display:inline-block;padding:6px 0}

/* ── HAMBURGER NAV — CSS-only checkbox hack ─────────────────── */
/* See §5 for required HTML changes */
#nav-toggle{display:none}
.nav-hamburger{display:none;cursor:pointer;padding:10px 16px;font-size:22px;
  line-height:1;color:#0a4;background:none;border:none;min-width:44px;min-height:44px;
  align-items:center;justify-content:center;margin-left:auto}

/* ── BREAKPOINT: ≤640px ─────────────────────────────────────── */
@media(max-width:640px){

  /* Typography */
  h1{font-size:26px;margin:16px 0 8px}
  h2{font-size:19px;margin:24px 0 6px;padding-top:16px}
  h3{font-size:16px;margin:16px 0 6px}
  p.lead.summary{font-size:16px;padding:10px 12px}
  .container{padding:12px 16px 60px}

  /* KPI grid: 140px min prevents zero-gap at 280px usable */
  .kpi-grid{grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:8px;margin:16px 0}
  .kpi .num{font-size:20px}
  .kpi .lbl{font-size:11px}

  /* Nav: show hamburger, collapse links */
  header.nav nav{flex-wrap:nowrap;padding:0 12px;min-height:48px;align-items:stretch}
  header.nav .brand{display:flex;align-items:center;padding:0;font-size:14px}
  .nav-hamburger{display:flex}

  /* Nav link list hidden until checkbox checked */
  .nav-links{
    display:none;
    position:absolute;top:48px;left:0;right:0;
    background:#fff;border-bottom:2px solid #0a4;
    padding:8px 0;z-index:20;
    flex-direction:column;gap:0
  }
  #nav-toggle:checked ~ nav .nav-links{display:flex}
  .nav-links a{
    padding:12px 20px;font-size:15px;min-height:44px;
    display:flex;align-items:center;
    border-bottom:1px solid #f0f0f0
  }
  .nav-links a:last-child{border-bottom:none}

  /* Tag badges: larger touch area */
  .tag{padding:5px 10px;font-size:12px}

  /* Prevent table cells from being too narrow */
  table th,table td{padding:6px 8px;font-size:13px}

  /* Footer */
  footer.site{padding:16px;font-size:12px}
}

/* ── BREAKPOINT: ≤375px — extreme narrow ───────────────────── */
@media(max-width:375px){
  h1{font-size:22px}
  .kpi-grid{grid-template-columns:1fr 1fr}
  .kpi .num{font-size:18px}
}
```

---

## 5. Hamburger Menu — CSS-Only Implementation (HTML changes required)

Replace the `<header class="nav"><nav>` block in `render_page()` with:

```html
<header class="nav">
  <input type="checkbox" id="nav-toggle" aria-label="Toggle navigation">
  <nav>
    <span class="brand">Central Asia B2G</span>
    <label class="nav-hamburger" for="nav-toggle" aria-label="Menu">&#9776;</label>
    <div class="nav-links">
      <!-- nav links rendered here -->
    </div>
  </nav>
</header>
```

The `<input>` is visually hidden (`display:none` hides it from all viewports including screen readers — replace with `.sr-only` pattern if accessibility is required for the toggle). The `<label>` triggers the checkbox state. The CSS rule `#nav-toggle:checked ~ nav .nav-links{display:flex}` opens the menu. No JavaScript. This pattern works on all static GitHub Pages deployments.

**Python change** in `render_page()` — update the `return f"""..."""` block:

```python
# Replace:
return f"""...
<header class="nav"><nav>
        <span class="brand">Central Asia B2G</span>
        {nav}
      </nav></header>
..."""

# With:
nav_links_html = f'<div class="nav-links">\n        {nav}\n      </div>'
return f"""...
<input type="checkbox" id="nav-toggle">
<header class="nav">
  <nav>
    <span class="brand">Central Asia B2G</span>
    <label class="nav-hamburger" for="nav-toggle">&#9776;</label>
    {nav_links_html}
  </nav>
</header>
..."""
```

---

## 6. Card-Layout Fallback for Wide Tables

For the 7-column decree/initiative/institution tables, wrap every `<table>` in a `<div class="table-scroll">` **plus** add a card-layout that activates on narrow screens.

### Proposed CSS (add to mobile block in §4):
```css
@media(max-width:640px){
  /* Already included in §4 block — card layout for data tables */
  .table-card table,
  .table-card thead{display:none}
  .table-card .card-row{
    display:block;background:#f7f7f7;border-radius:6px;
    padding:12px 14px;margin:8px 0;
  }
  .table-card .card-row dt{
    font-size:11px;font-weight:600;color:#555;
    text-transform:uppercase;letter-spacing:.04em;margin-top:8px
  }
  .table-card .card-row dd{margin:2px 0 0 0;font-size:14px;color:#111}
}
```

### HTML pattern (generated by render_site.py alongside each wide table):
```html
<!-- Mobile card view — hidden on desktop -->
<div class="table-card">
  <div class="card-row">
    <dl>
      <dt>ID</dt><dd>UZ-DECREE-001</dd>
      <dt>Type</dt><dd>Presidential Decree</dd>
      <dt>Date</dt><dd>2024-03-15</dd>
      <dt>Status</dt><dd><span class="tag">active_window</span></dd>
      <dt>Source</dt><dd><a href="...">primary source</a></dd>
    </dl>
  </div>
</div>
<!-- Desktop table view — hidden on mobile -->
<div class="table-scroll">
  <table>...</table>
</div>
```

For static sites, the simplest approach is `overflow-x:auto` on `.table-scroll` (included in §4) without the card duplication. The card pattern is the higher-fidelity option for the initiatives page which has the densest table data.

---

## 7. PWA Manifest — "Add to Home Screen" Readiness

Current manifest:
```json
{
  "display": "minimal-ui",
  "icons": [{"src": "/favicon.svg", "type": "image/svg+xml", "sizes": "any"}]
}
```

**Issues**:
1. `display: "minimal-ui"` shows browser chrome — use `"standalone"` for a full Add-to-Home-Screen experience.
2. SVG-only icon: Chrome on Android requires at least one raster PNG icon ≥192×192px to trigger the install banner. Apple Safari on iOS ignores the manifest entirely and requires `<link rel="apple-touch-icon">` in `<head>`.
3. Missing `<meta name="theme-color" content="#0a4d34">` in `render_page()` head — the manifest `theme_color` is not applied without this tag.
4. Missing `<link rel="manifest" href="/manifest.webmanifest">` in `render_page()` head — the manifest file exists but is not linked from any page.
5. Missing `<link rel="apple-touch-icon" href="/apple-touch-icon.png">` — iOS Safari will not show an icon on home screen without this.

**Minimum fix** (two changes in `render_page()` `<head>`):
```html
<link rel="manifest" href="/manifest.webmanifest">
<meta name="theme-color" content="#0a4d34">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
```

---

## 8. Lighthouse Mobile Estimate — Before / After

| Metric | Before | After (estimated) |
|---|---|---|
| Performance | 85–90 | 90–95 (no new resources added) |
| Accessibility | 55–65 | 80–88 (tap targets fixed, nav labelled) |
| Best Practices | 80 | 88 (manifest linked, theme-color present) |
| SEO | 82 | 90 (mobile-friendly, tap targets pass) |
| PWA | 30 | 65 (manifest linked, theme-color, still missing raster icon) |

Key Lighthouse audit items resolved by these fixes:
- "Tap targets are not sized appropriately" — fixed by §4 padding rules.
- "Does not have a `<meta name=viewport>`" — already present in `render_page()`. Pass.
- "Content is sized correctly for the viewport" — resolved by `.container` padding reduction and table scroll wrapper.
- "Text remains visible during webfont load" — no web fonts used; system-ui stack. Pass.
- "Links are not crawlable" — no change; links already valid.

---

## Summary of Required Changes to `render_site.py`

| Change | Location | Lines affected |
|---|---|---|
| Replace single `@media` line with full CSS block (§4) | `CSS` constant, line 100 | Replace 1 line with ~112 lines |
| Add hamburger HTML structure (§5) | `render_page()` return string | ~10 lines |
| Add `<link rel="manifest">`, `<meta name="theme-color">`, `<link rel="apple-touch-icon">` to `<head>` | `render_page()` head template | +3 lines |
| Wrap all `<table>` calls in `<div class="table-scroll">` | `decrees_page()`, `institutions_page()`, `donors_page()`, `procurement_page()`, `methodology()` | ~6 table sites |
