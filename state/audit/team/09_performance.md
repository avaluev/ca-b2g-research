# Performance Audit — 09_performance.md

**Auditor**: Performance Engineer
**Site**: https://avaluev.github.io/ca-b2g-research/
**Date**: 2026-05-03

---

## Resource Budget (per-page, worst case)

| Resource | Raw | Gzip transfer | Notes |
|---|---|---|---|
| HTML — Home | 10.4 KB | 3.1 KB | Smallest page; good baseline |
| HTML — Institutions | 59.9 KB | 16.8 KB | Largest page; 106-row table |
| HTML — MVP | 41.7 KB | 6.7 KB | 200-row table; high repetition compresses well |
| HTML — Initiatives | 27.0 KB | 5.6 KB | 100-row table |
| Inline CSS | 2.3 KB | ~0.9 KB | Single `<style>` block; no external sheet |
| Inline JSON-LD | 2.7 KB | included above | Per-page, consistent schema |
| JavaScript | **0 B** | 0 B | Zero JS; zero parser blocking |
| Favicon SVG | 228 B | ~120 B | Has `width`/`height`; clean |
| OG image SVG | 411 B | ~200 B | SVG served but meta references `.png` — **mismatch** |
| Web fonts | **0 B** | 0 B | `system-ui` stack; no font request |
| External CSS/JS | **0** | — | None; render path is fully local |
| **Total transfer (home)** | — | **~4 KB** | Well under any budget |
| **Total transfer (worst)** | — | **~18 KB** | Institutions page |

---

## Estimated Core Web Vitals (current)

| Metric | Target | Estimated current | Status |
|---|---|---|---|
| FCP | < 0.4 s | ~0.15 s | Green — zero blocking resources; CSS inline |
| LCP | < 1.5 s | ~0.2 s | Green — LCP element is text (`<h1>`), no image to load |
| CLS | < 0.05 | ~0.02–0.08 | Amber — tables without `table-layout:fixed` can shift |
| INP | < 100 ms | ~0 ms | Green — zero JS event handlers |
| TTFB | < 0.8 s | ~0.05 s | Green — GitHub Pages CDN; static file |

---

## 10 Specific Optimisations

### OPT-1: Fix OG image format mismatch (Critical — broken social sharing)

`render_site.py` writes `og-default.svg` but meta tags reference `og-default.png`. Social crawlers (Twitter/X, LinkedIn, Facebook) reject SVG OG images. Fix: either rename to `.png` and generate a raster version, or serve the SVG and fix the meta. Quickest patch — update the meta reference to match the SVG that is already generated.

**Patch in `render_site.py`, `render_page` function:**
```python
# Change:
<meta property="og:image" content="{SITE_URL}/og-default.png">
<meta name="twitter:image" content="{SITE_URL}/og-default.png">
# To:
<meta property="og:image" content="{SITE_URL}/og-default.svg">
<meta name="twitter:image" content="{SITE_URL}/og-default.svg">
```
Preferred fix: add a `generate_og_png()` call in `main()` using Python's `cairosvg` or a pure Python rasteriser to emit a real `1200×630` PNG.

---

### OPT-2: Add `table-layout: fixed` to prevent CLS on table pages

Current CSS: `table{border-collapse:collapse;width:100%;margin:12px 0 24px;font-size:14px}`. Without `table-layout:fixed`, the browser must measure all cell content before committing column widths — causing a layout shift visible as CLS.

**Patch in the `CSS` constant:**
```python
table{border-collapse:collapse;width:100%;table-layout:fixed;margin:12px 0 24px;font-size:14px}
th,td{...;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
```
Add explicit column-width hints via a `<colgroup>` block in each table function, or use percentage widths on `<th>`.

---

### OPT-3: Add `content-visibility: auto` to off-screen table rows (CLS + render cost)

For the MVP (200-row) and Institutions (106-row) tables, wrapping the `<tbody>` content with `content-visibility: auto` tells the browser to skip rendering off-screen rows, reducing first-paint style cost.

**Patch in the `CSS` constant:**
```python
tbody{content-visibility:auto;contain-intrinsic-size:0 2000px}
```

---

### OPT-4: Build-time HTML minification

All pages are pretty-printed Python f-strings with newlines between tags. The Institutions page is 60 KB raw; its gzip ratio is only 28% because whitespace breaks repetition patterns. Minifying before write would cut raw size ~20–30% and improve gzip ratio.

**Patch in `write_page()`:**
```python
import re as _re

def _minify(html: str) -> str:
    # Collapse whitespace between tags (safe for pre/code-free pages)
    html = _re.sub(r'>\s+<', '><', html)
    html = _re.sub(r'\s{2,}', ' ', html)
    return html.strip()

def write_page(path_url: str, html_text: str) -> None:
    out = ...
    out.write_text(_minify(html_text), encoding="utf-8")
```
Projected saving: Institutions 60 KB → ~44 KB raw (17 KB → ~14 KB gzip).

---

### OPT-5: Progressive disclosure for 200-row MVP table (mobile UX + DOM size)

The MVP page has 2,062 DOM nodes — above Chrome's recommended 1,500-node budget. On low-end Android this triggers a style recalculation cost of ~150–400 ms. For SEO the full content must stay in the DOM (Google requires visible content; hidden FAQ ban applies).

**Pattern: show top-25 rows, expand remainder with a native `<details>` element:**
```html
<table><!-- header + first 25 rows --></table>
<details>
  <summary>Show all 175 remaining MVPs</summary>
  <table><!-- rows 26-200 --></table>
</details>
```
This keeps all content in DOM (crawler-readable), halves initial render cost, and requires zero JavaScript.

**Patch in `mvp_page()`:** Split `rows` list at index 25; render first slice in main table, remainder inside `<details><summary>Show remaining {n-25} MVPs</summary><table>...</table></details>`.

---

### OPT-6: Add `<meta http-equiv="Cache-Control">` for GitHub Pages

GitHub Pages serves static files with a default `max-age=600` (10 minutes). Adding a hint bumps the browser cache.

**Patch in `render_page()` head section:**
```html
<meta http-equiv="Cache-Control" content="public, max-age=86400">
```

---

### OPT-7: Add `loading="lazy"` to any future images

Currently zero raster images — good. When the first `<img>` tag is added to any page, the template must include `loading="lazy"` and explicit `width`/`height` attributes. Add a guard comment to `render_page()`:
```python
# POLICY: every <img> MUST carry loading="lazy" width=N height=N alt=""
```

---

### OPT-8: Reduce JSON-LD per-page size

Each page embeds a full `@graph` with Organization, Person, WebSite, BreadcrumbList, and Article nodes — 2.7 KB raw. Organization, Person, and WebSite are identical across all 17 pages; this is ~40 KB of duplicated schema across the site. Consider emitting Organization/WebSite/Person in the home page JSON-LD only, and using `@id` references (`{"@id": ".../#organization"}`) on all other pages.

**Savings:** ~1.8 KB per inner page; ~27 KB total across the site. No SEO impact — `@id` cross-references are valid schema.

---

### OPT-9: Add `contain: layout` to `.kpi-grid` items

The KPI grid on the home page uses CSS Grid with `auto-fit`. Each `.kpi` card is an independent layout context. Adding `contain: layout style` prevents their reflows from bubbling to the root.

**Patch in CSS:**
```css
.kpi-grid .kpi{...;contain:layout style}
```

---

### OPT-10: Explicit `width`/`height` on favicon `<link>` (Lighthouse hint)

The `<link rel="icon" href="/favicon.svg">` tag has no `sizes` attribute. Lighthouse deducts points for this. The SVG favicon has a `64×64` viewBox.

**Patch in `render_page()`:**
```html
<link rel="icon" href="/favicon.svg" type="image/svg+xml" sizes="any">
```

---

## SVG Dimension Audit (CLS Prevention)

| Asset | Has `viewBox` | Has `width` | Has `height` | CLS risk |
|---|---|---|---|---|
| `favicon.svg` | Yes (0 0 64 64) | Yes (64) | Yes (64) | None |
| `og-default.svg` | Yes (0 0 1200 630) | Yes (1200) | Yes (630) | None — not rendered in page body |

Both SVGs carry explicit dimensions. No inline `<svg>` blocks in any rendered page body. CLS from SVG is not a current issue; add a linter check to `check_quality.py` to enforce this for any future inline SVGs: `assert not re.search(r'<svg(?![^>]*width)', page_html)`.

---

## Predicted Lighthouse Performance After All Fixes

| Metric | Before | After (predicted) |
|---|---|---|
| FCP | ~0.15 s | ~0.12 s |
| LCP | ~0.20 s | ~0.18 s |
| CLS | ~0.03–0.08 | < 0.02 |
| INP | ~0 | ~0 |
| TBT | 0 ms | 0 ms |
| **Lighthouse Performance** | **~93–95** | **~97–99** |

The main current drag on the Lighthouse score is CLS from unsized table columns (OPT-2) and DOM size on MVP/Institutions pages (OPT-5). Fixing those two delivers the bulk of the remaining score gain. OPT-1 (OG image) is a correctness fix with no Lighthouse impact but significant real-world social-sharing impact.

**Priority order**: OPT-1 (correctness) → OPT-2 (CLS) → OPT-5 (DOM size) → OPT-4 (minification) → remainder.
