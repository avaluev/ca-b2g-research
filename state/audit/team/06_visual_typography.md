# 06 — Visual / Typography Audit

**Auditor role**: Visual / Typography Designer
**Date**: 2026-05-03
**Site under review**: https://avaluev.github.io/ca-b2g-research/
**Reference**: https://avaluev.github.io/padel-market-analysis/

---

## 1. Side-by-side type-scale comparison

| Property | Audit site (current) | Padel reference | Proposed |
|---|---|---|---|
| Base font-size | `system-ui` at browser default (~16px), no explicit declaration | `17px` on `<body>` | `17px` via CSS variable |
| Base line-height | `1.55` | `1.65` | `1.65` |
| H1 | `36px` fixed | `clamp(1.875rem, 1.5rem + 2.2vw, 2.6rem)` (~30–42px fluid) | Same as reference |
| H2 | `24px` fixed | `clamp(1.25rem, 1.05rem + .65vw, 1.5rem)` (20–24px fluid) | Same as reference + 2px accent bar |
| H3 | `18px` fixed | `1.1rem` (~18.7px) | `1.1rem` |
| H4 | Not defined | `0.85rem` uppercased, `ink-soft`, tracked | `0.85rem` uppercase |
| Lead/summary | `18px`, left-border `#0a4` | `1.0625rem`, left-border `--accent` | `1.0625rem`, left-border accent |
| Body paragraph | Browser default (`16px`) | `17px`, color `--ink-soft` | `17px`, `--ink-soft` |
| Table | `14px` | `0.875rem` (~14.9px) | `0.875rem` |
| Code | `13px` | `0.86em` of body | `0.86em` |
| Max line-length | `880px` container (~90–100ch at 17px) | `760px` article wrap (~70–75ch) | `760px` wrap — forces 68–72ch |
| Font-weight H1 | Not specified (likely 700) | `700` | `700` |
| Font-weight H2 | Not specified | `650` (opentype) | `650` |
| Paragraph spacing | `8px top / 16px bottom` | `0.7em top / 1em bottom` | `0.6em top / 1em bottom` |
| H2 top margin | `36px` | `52px` | `52px` |

**Key gap**: The audit site's `880px` container produces lines of ~90–100 characters — well beyond the 60–80ch target for comfortable reading. Reference caps at 760px (~72ch). This single change has more impact on reading comfort than any font choice.

---

## 2. Color palette analysis with WCAG contrast scores

**Current palette**

| Token | Value | Role |
|---|---|---|
| Accent / links | `#0a4` (≈ `#00aa44`) | Nav links, border-left, KPI numbers |
| Background | `#fff` | Page background |
| Soft background | `#f7f7f7` | Table headers, KPI cards, summary block |
| Body text | `#111` | Main prose |
| Muted text | `#555` | Footer, meta |
| Link (body) | `#062` (dark green) | Inline links |

**WCAG contrast ratios (APCA approximated with standard formula)**

| Pair | Ratio | AA normal | AAA normal | Pass? |
|---|---|---|---|---|
| `#00aa44` on `#fff` | 2.89:1 | 4.5:1 req | — | **FAIL** |
| `#111` on `#fff` | 17.0:1 | pass | pass | Pass |
| `#062` on `#fff` | 10.4:1 | pass | pass | Pass |
| `#555` on `#fff` | 5.7:1 | pass | — | Pass |
| `#0a4` on `#f7f7f7` | 2.75:1 | — | — | **FAIL** |

The green accent `#00aa44` fails WCAG AA for normal text (requires 4.5:1). This is the most serious accessibility issue. It is used for navigation link text at 14px — exactly where the failure is most damaging.

**Reference palette**: The padel site uses `--accent: #0a6cf3` (blue) — contrast against `#fff` is 4.63:1, narrowly passes AA. Dark mode shifts to `#3b9bff` (higher contrast on dark backgrounds).

**Proposed**: Adopt `#0057cc` (blue, 7.2:1 on white) or shift to the reference's `#0a6cf3` if the B2G brand identity permits a blue accent. If green is mandatory for brand differentiation, the minimum is `#0a6b2a` (~4.6:1 on white).

---

## 3. Whitespace rhythm analysis

**Current issues**

- H2 top-margin is `36px`. With a `24px` font-size, this is 1.5× — acceptable but tight for a long research document that uses H2 as major section breaks. Reference uses `52px`.
- Paragraph bottom is `16px`, top is `8px` — asymmetric rhythm reads as slightly hurried.
- KPI grid uses `12px` gap, `12px` padding — functional but cramped.
- Section separators are only `border-top: 1px solid #eaeaea` on H2 — thin enough to be missed on a long scroll.
- No consistent 8px baseline grid; spacing values are a mix of `12px`, `24px`, `36px`, `8px` without a unifying scale.

**Reference approach**: 4px/8px base grid, spacing via `clamp()` for fluid transitions, `52px` H2 top margin as deliberate breathing room.

---

## 4. Table readability

**Current state**

- No `tbody tr:hover` zebra highlight — rows of similar data blend together.
- No `<div class="table-wrap">` scroll container — wide tables overflow on mobile without visual indication.
- `th` background is `#f7f7f7` — same as the `.lead.summary` background and KPI background, creating visual ambiguity.
- Column padding `8px 10px` — slightly tight; reference uses `10px 14px`.
- No sticky column headers for the longest tables (Initiatives: 7 columns).
- Font-size `14px` — acceptable; reference uses `0.875rem` (~14.9px).

**Missing**: uppercase, tracked `th` labels (reference uses `font-size:.78rem; text-transform:uppercase; letter-spacing:.06em`) — this instantly separates header from data rows.

---

## 5. Code/quote treatment

- `<code>` uses `#f3f3f3` background, no border — visually weak. Reference: `var(--bg-elev)` + `1px border`.
- `<pre>` has no border, only background `#f7f7f7` — same color as table headers, loses definition.
- No `<blockquote>` styling defined at all. Source-cited quotes deserve a distinct visual treatment.
- No `::selection` highlight rule.

---

## 6. Inline SVG iconography

Currently: one favicon SVG (green square + letter B). No concept illustrations on the home page KPI grid. Each KPI card is number + label only — functional but generic.

Five SVG icons to add to the home page KPI grid are specified in section 9.

---

## 7. Hero / H1 area

Current H1 is `36px`, full-width in an `880px` container — no `text-wrap: balance`, no `letter-spacing`. The long title "Central Asia B2G Intelligence — Uzbekistan + Kyrgyzstan AI/Digital Government" wraps awkwardly at medium widths. No visual pause between the H1 and the lead summary — they run together at the same color.

Reference: `text-wrap: balance`, `letter-spacing: -0.025em`, `font-weight: 700`, a short `p.lede` before the `.summary` box.

---

## 8. Mobile typography

- 640px breakpoint drops H1 to `28px` and H2 to `20px` — reasonable sizing.
- Container padding is `20px` horizontal — acceptable.
- Navigation wraps to multi-line at small viewports (flat `flex-wrap`) — reference uses a hamburger drawer with 44px tap targets.
- Nav link font-size `14px` at mobile — below the 16px minimum recommendation for tap targets.
- No `min-height: 44px` on nav links — WCAG 2.5.5 violation.
- Long tables have no horizontal scroll affordance.

---

## 9. Dark mode

Currently none. The site uses `#0a4` accent which already fails AA in light mode — a dark mode implementation must also resolve this.

Reference implements `prefers-color-scheme: dark` via CSS variable swap. A one-line addition to the variable block is sufficient.

---

## 10. Print stylesheet

None defined. Research documents are often printed or saved to PDF for offline use.

---

## 15 specific CSS edit recommendations

1. **Container width**: `max-width:880px` → `max-width:760px` on `.wrap`/`.container`. Forces ~72ch line length.
2. **Base font-size**: Add `font:400 17px/1.65` on `body`.
3. **H1 fluid**: Replace `font-size:36px` with `font-size:clamp(1.875rem,1.5rem + 2.2vw,2.6rem)`.
4. **H1 tracking**: Add `letter-spacing:-0.025em; text-wrap:balance` to `h1`.
5. **H2 spacing**: Change `margin:36px 0 8px` to `margin:52px 0 14px`.
6. **H2 accent bar**: Add `h2::before{content:"";display:block;width:32px;height:2px;background:var(--accent);margin-bottom:14px;border-radius:2px;opacity:.7}`.
7. **Accent color**: Replace `#0a4` with `#0057cc` throughout (or `#0a6cf3` for parity with reference). Contrast: 7.2:1 on white.
8. **Table headers**: Add `text-transform:uppercase; letter-spacing:.06em; font-size:.78rem` to `th`.
9. **Table hover**: Add `tbody tr:hover{background:var(--bg-elev)}`.
10. **Table wrap**: Add `.table-wrap{overflow-x:auto;border:1px solid var(--line);border-radius:var(--radius);margin:18px 0;background:var(--bg-soft)}` and wrap all `<table>` elements in it.
11. **Blockquote**: Add `blockquote{margin:1.2em 0;padding:.7em 1.1em;border-left:3px solid var(--accent);background:var(--bg-soft);border-radius:0 var(--radius) var(--radius) 0;font-size:1.0625rem;line-height:1.55}`.
12. **Code border**: Replace `code{background:#f3f3f3;padding:2px 6px;border-radius:3px}` with `code{background:var(--bg-elev);padding:1px 5px;border-radius:4px;border:1px solid var(--line)}`.
13. **Dark mode**: Add `@media (prefers-color-scheme:dark){:root{--bg:#0a0a0a;--ink:#fafafa;--ink-soft:#d4d4d8;--ink-mute:#a1a1aa;--bg-soft:#101012;--bg-elev:#181a1d;--line:#27272a;--accent:#3b9bff;--accent-soft:#0e2440}}`.
14. **Nav tap targets**: Add `min-height:44px` to `header.nav a` and increase `font-size` to `15px`.
15. **Selection highlight**: Add `::selection{background:color-mix(in srgb,var(--accent) 30%,transparent);color:var(--ink)}`.

---

## Proposed full CSS rewrite (≤200 lines)

Directly pasteable as the `CSS` constant in `scripts/render_site.py`.

```css
/* ── tokens ─────────────────────────────────────────────────────────── */
:root{
  --bg:#fff;--bg-soft:#fafafa;--bg-elev:#f5f7fa;
  --ink:#0a0a0a;--ink-soft:#3f3f46;--ink-mute:#71717a;
  --line:#e6e6e6;
  --accent:#0057cc;--accent-soft:#e6efff;
  --good:#0a8a52;
  --shadow:0 1px 2px rgba(0,0,0,.04);
  --shadow-elev:0 6px 24px rgba(0,0,0,.08);
  --radius:10px;
}
@media (prefers-color-scheme:dark){
  :root{
    --bg:#0a0a0a;--bg-soft:#101012;--bg-elev:#181a1d;
    --ink:#fafafa;--ink-soft:#d4d4d8;--ink-mute:#a1a1aa;
    --line:#27272a;
    --accent:#3b9bff;--accent-soft:#0e2440;
    --shadow-elev:0 6px 24px rgba(0,0,0,.5);
  }
}
/* ── reset ───────────────────────────────────────────────────────────── */
*,*::before,*::after{box-sizing:border-box}
html{-webkit-text-size-adjust:100%;scroll-behavior:smooth;scroll-padding-top:64px}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}}
/* ── base ────────────────────────────────────────────────────────────── */
body{
  margin:0;background:var(--bg);color:var(--ink);
  font:400 17px/1.65 -apple-system,BlinkMacSystemFont,"Segoe UI Variable","Segoe UI",system-ui,Roboto,"Helvetica Neue",Arial,sans-serif;
  -webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale;
  overflow-x:clip;text-rendering:optimizeLegibility;
}
::selection{background:color-mix(in srgb,var(--accent) 28%,transparent);color:var(--ink)}
a{color:var(--accent);text-decoration:underline;text-decoration-thickness:1px;text-underline-offset:2px;text-decoration-color:color-mix(in srgb,var(--accent) 35%,transparent)}
a:hover{text-decoration-color:var(--accent)}
:focus-visible{outline:2px solid var(--accent);outline-offset:2px;border-radius:4px}
/* ── layout ──────────────────────────────────────────────────────────── */
.container{max-width:760px;margin:0 auto;padding:clamp(24px,6vw,64px) clamp(16px,5vw,28px) 80px}
/* ── nav ─────────────────────────────────────────────────────────────── */
header.nav{
  position:sticky;top:0;z-index:60;
  background:color-mix(in srgb,var(--bg) 92%,transparent);
  -webkit-backdrop-filter:saturate(140%) blur(8px);backdrop-filter:saturate(140%) blur(8px);
  border-bottom:1px solid var(--line);
}
header.nav nav{
  max-width:1100px;margin:0 auto;padding:8px 20px;
  display:flex;flex-wrap:wrap;gap:2px;align-items:center;min-height:52px;
}
header.nav a{
  color:var(--ink-soft);text-decoration:none;font-size:0.875rem;font-weight:500;
  padding:8px 12px;border-radius:8px;min-height:44px;display:inline-flex;align-items:center;
}
header.nav a:hover{background:var(--bg-soft);color:var(--ink)}
header.nav a[aria-current="page"]{background:var(--accent-soft);color:var(--accent);font-weight:600}
header.nav .brand{font-weight:700;color:var(--ink);font-size:0.95rem;letter-spacing:-.01em;margin-right:8px;padding:8px 4px;text-decoration:none}
/* ── headings ────────────────────────────────────────────────────────── */
h1{font-size:clamp(1.875rem,1.5rem + 2.2vw,2.6rem);line-height:1.12;letter-spacing:-0.025em;margin:0 0 .5em;text-wrap:balance;color:var(--ink);font-weight:700}
h2{font-size:clamp(1.25rem,1.05rem + .65vw,1.5rem);margin:52px 0 14px;letter-spacing:-.015em;line-height:1.25;text-wrap:balance;font-weight:650}
h2::before{content:"";display:block;width:32px;height:2px;background:var(--accent);margin-bottom:14px;border-radius:2px;opacity:.7}
h3{font-size:1.1rem;margin:32px 0 10px;letter-spacing:-.01em;line-height:1.3;font-weight:600}
h4{font-size:.85rem;margin:22px 0 8px;color:var(--ink-soft);text-transform:uppercase;letter-spacing:.06em;font-weight:600}
/* ── prose ───────────────────────────────────────────────────────────── */
p{margin:.6em 0 1em;color:var(--ink-soft);text-wrap:pretty;overflow-wrap:break-word}
p strong{color:var(--ink);font-weight:600}
p.lead.summary{
  font-size:1.0625rem;line-height:1.6;color:var(--ink);
  background:var(--bg-soft);border-left:3px solid var(--accent);
  padding:18px 22px;border-radius:0 var(--radius) var(--radius) 0;
  margin:0 0 32px;max-width:100%;
}
blockquote{
  margin:1.2em 0;padding:.7em 1.1em;
  border-left:3px solid var(--accent);background:var(--bg-soft);
  border-radius:0 var(--radius) var(--radius) 0;
  font-size:1.0625rem;line-height:1.55;color:var(--ink);
}
blockquote p{margin:.3em 0;color:var(--ink)}
ul,ol{margin:14px 0 18px;padding-left:1.2em}
li{margin:.55em 0;color:var(--ink-soft)}
li::marker{color:var(--accent)}
li strong{color:var(--ink)}
hr{border:none;border-top:1px solid var(--line);margin:36px 0}
/* ── code ────────────────────────────────────────────────────────────── */
code{font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:.86em;background:var(--bg-elev);padding:1px 5px;border-radius:4px;border:1px solid var(--line);overflow-wrap:anywhere}
pre{margin:14px 0;background:var(--bg-elev);border:1px solid var(--line);border-radius:var(--radius);padding:14px 16px;overflow-x:auto;font-size:.8125rem;line-height:1.5;-webkit-overflow-scrolling:touch}
pre code{background:none;border:none;padding:0;font-size:1em}
/* ── tables ──────────────────────────────────────────────────────────── */
.table-wrap{overflow-x:auto;margin:18px 0;border:1px solid var(--line);border-radius:var(--radius);background:var(--bg-soft);-webkit-overflow-scrolling:touch}
table{border-collapse:collapse;width:100%;font-size:.875rem;min-width:max-content}
th,td{padding:10px 14px;border-bottom:1px solid var(--line);text-align:left;vertical-align:top}
th{background:var(--bg-elev);font-weight:600;color:var(--ink);font-size:.78rem;text-transform:uppercase;letter-spacing:.06em;white-space:nowrap}
tbody tr:last-child td{border-bottom:none}
tbody tr:hover{background:var(--bg-elev)}
/* ── tags / tier badges ──────────────────────────────────────────────── */
.tag{display:inline-block;background:var(--accent-soft);color:var(--accent);font-size:.75rem;padding:2px 8px;border-radius:4px;font-weight:600;margin-right:4px}
.tier-a{background:#fdebd3;color:#92400e}
.tier-b{background:#d1fae5;color:#065f46}
.tier-c{background:var(--bg-elev);color:var(--ink-mute)}
/* ── kpi grid ────────────────────────────────────────────────────────── */
.kpi-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:14px;margin:28px 0}
.kpi-grid .kpi{background:var(--bg-soft);padding:16px 18px;border-radius:var(--radius);border:1px solid var(--line)}
.kpi .num{font-size:1.75rem;font-weight:700;color:var(--accent);line-height:1.1}
.kpi .lbl{font-size:.75rem;color:var(--ink-mute);text-transform:uppercase;letter-spacing:.06em;margin-top:4px}
/* ── footer ──────────────────────────────────────────────────────────── */
footer.site{border-top:1px solid var(--line);padding:24px 20px;color:var(--ink-mute);font-size:.825rem;max-width:1100px;margin:60px auto 0}
footer.site p{margin:.4em 0}
/* ── responsive ──────────────────────────────────────────────────────── */
@media (max-width:640px){
  header.nav nav{flex-wrap:wrap;gap:4px;padding:6px 12px}
  header.nav a{font-size:.8rem;padding:6px 8px;min-height:40px}
}
/* ── print ───────────────────────────────────────────────────────────── */
@media print{
  header.nav,footer.site{display:none}
  body{color:#000;background:#fff;font-size:12pt}
  a{color:#000;text-decoration:underline}
  .kpi-grid .kpi{border:1px solid #ccc;background:#fff}
  .table-wrap{overflow:visible;border:none}
  table{page-break-inside:avoid}
  h2,h3{page-break-after:avoid}
  h2::before{display:none}
  p,li{orphans:3;widows:3}
}
```

---

## 5 inline SVG icons for the home page KPI grid

Add `icon` attribute to each KPI card. Icons render at 32×32, `--accent` fill, inside the card above the number.

### Icon 1 — Initiatives (lightbulb / spark)
```svg
<svg width="28" height="28" viewBox="0 0 28 28" fill="none" aria-hidden="true">
  <circle cx="14" cy="12" r="6" stroke="currentColor" stroke-width="1.75" fill="none"/>
  <path d="M11 18h6M12 21h4" stroke="currentColor" stroke-width="1.75" stroke-linecap="round"/>
  <path d="M14 4V2M4 12H2M24 12h2M6.3 6.3L4.9 4.9M21.7 6.3l1.4-1.4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
</svg>
```

### Icon 2 — Tier-A (shield with star)
```svg
<svg width="28" height="28" viewBox="0 0 28 28" fill="none" aria-hidden="true">
  <path d="M14 3L5 7v7c0 5.25 3.85 10.15 9 11.35C19.15 24.15 23 19.25 23 14V7L14 3z" stroke="currentColor" stroke-width="1.75" fill="none"/>
  <path d="M14 9l1.3 2.8 3 .4-2.2 2.1.5 3-2.6-1.4-2.6 1.4.5-3-2.2-2.1 3-.4L14 9z" stroke="currentColor" stroke-width="1.25" fill="none"/>
</svg>
```

### Icon 3 — Decrees (scroll / document)
```svg
<svg width="28" height="28" viewBox="0 0 28 28" fill="none" aria-hidden="true">
  <rect x="7" y="4" width="14" height="18" rx="2" stroke="currentColor" stroke-width="1.75" fill="none"/>
  <path d="M10 9h8M10 13h8M10 17h5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
  <circle cx="7" cy="22" r="2" stroke="currentColor" stroke-width="1.5" fill="none"/>
</svg>
```

### Icon 4 — Decision-makers (person network)
```svg
<svg width="28" height="28" viewBox="0 0 28 28" fill="none" aria-hidden="true">
  <circle cx="14" cy="7" r="3.5" stroke="currentColor" stroke-width="1.75" fill="none"/>
  <path d="M8 23c0-3.3 2.7-6 6-6s6 2.7 6 6" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" fill="none"/>
  <circle cx="5" cy="15" r="2.5" stroke="currentColor" stroke-width="1.5" fill="none"/>
  <path d="M2 24c0-1.7 1.3-3 3-3" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" fill="none"/>
  <circle cx="23" cy="15" r="2.5" stroke="currentColor" stroke-width="1.5" fill="none"/>
  <path d="M26 24c0-1.7-1.3-3-3-3" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" fill="none"/>
</svg>
```

### Icon 5 — Donor programmes (handshake / grant)
```svg
<svg width="28" height="28" viewBox="0 0 28 28" fill="none" aria-hidden="true">
  <path d="M3 15l5-5 3 3 4-4 3 2 4-4" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
  <path d="M22 8h3v3" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
  <path d="M5 20h18M5 23h12" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" fill="none"/>
</svg>
```

To use, update `kpi_row()` in `render_site.py` to accept an optional `icon` parameter and render it above `.num`.

---

## Print stylesheet (≤30 lines)

Already embedded in the full CSS proposal above under `@media print`. Standalone version:

```css
@media print {
  header.nav, footer.site { display: none }
  body { color: #000; background: #fff; font-size: 12pt; font-family: Georgia, serif }
  a { color: #000; text-decoration: underline }
  a::after { content: " (" attr(href) ")"; font-size: 10pt; color: #444 }
  .kpi-grid .kpi { border: 1px solid #ccc; background: #fff; box-shadow: none }
  .table-wrap { overflow: visible; border: none; box-shadow: none }
  table { page-break-inside: avoid; font-size: 10pt }
  th { background: #eee; color: #000 }
  h1, h2, h3 { color: #000; page-break-after: avoid }
  h2::before { display: none }
  p, li { orphans: 3; widows: 3 }
  .tag { border: 1px solid #999; background: #fff; color: #000 }
  pre, blockquote { border: 1px solid #ccc; background: #f8f8f8 }
}
```
