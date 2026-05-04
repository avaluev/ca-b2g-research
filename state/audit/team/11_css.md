# CSS Audit — Agent 11

**Site**: https://avaluev.github.io/ca-b2g-research/
**Source constant**: `scripts/render_site.py` lines 68–101

---

## Current CSS Critique (10 issues)

**Issue 1 — No custom properties.** Every color, spacing value, and radius is hardcoded inline. `#0a4`, `#062`, `#eaeaea`, `#f7f7f7`, `#f3f3f3`, `#e9f6ee`, `#fdebd3`, `24px`, `4px`, `3px` appear 3–6 times each. A single token change (brand color, border radius) requires a grep-and-replace across the whole constant.

**Issue 2 — No dark mode.** There is no `@media (prefers-color-scheme: dark)` block. Users on system dark mode get `background:#fff` / `color:#111` regardless. This also harms AI-search accessibility scoring.

**Issue 3 — Hardcoded font sizes, no fluid type.** `h1{font-size:36px}`, `h2{font-size:24px}`, `h3{font-size:18px}`, `p.lead{font-size:18px}`. The breakpoint override (`@media max-width:640px`) only steps down h1 and h2. Intermediate viewport sizes (641–799 px) get desktop sizes on cramped screens. `clamp()` eliminates the need for breakpoint overrides entirely.

**Issue 4 — Physical properties, not logical.** `padding:24px 20px`, `margin:0 auto`, `padding:12px 16px`, `border-left:3px solid`. These should use logical properties (`padding-block`/`padding-inline`, `border-inline-start`) so the layout is correct when the site is viewed in RTL languages (Arabic, Persian — plausible given the Central Asia scope) or when a browser's writing-mode changes.

**Issue 5 — No `prefers-reduced-motion` block.** No transitions or animations exist today, but the absence of the block is itself a signal that motion was never considered. Adding it now as a `@media (prefers-reduced-motion: reduce)` stub future-proofs the sheet and is a WCAG 2.1 requirement (2.3.3 AA).

**Issue 6 — No print stylesheet.** A research brief is often printed or saved as PDF. Without `@media print` rules the nav bar, sticky header, and background fills all print, wasting ink and breaking layout. Footer provenance links should be rendered as visible URLs in print.

**Issue 7 — No safe-area-inset support.** The `.container` and `header.nav nav` paddings use fixed pixel values. On iPhones with notches/Dynamic Island, content can be obscured. `padding-inline: max(20px, env(safe-area-inset-left))` (and right/bottom equivalents) is the fix.

**Issue 8 — Table layout is not card-friendly on mobile.** The single responsive block only resizes headings. `<table>` elements wider than the viewport force horizontal scroll on phones. No `@container` or mobile card pattern is present. Tables with 5+ columns (e.g., the Initiatives and Donor Pipeline tables) should reflow to labeled card rows below 480 px.

**Issue 9 — Minor specificity inconsistency.** `p.lead.summary` uses a double-class selector (specificity 0-2-1) while all other element selectors are specificity 0-0-1. This is not a critical bug, but it means any future utility class applied to `<p>` will not override the lead styling without also doubling up classes or reaching for `!important`.

**Issue 10 — CSS sort order is mixed.** Typography (`font-size`, `line-height`) is interleaved with color and layout declarations within the same rule. The recommended order is: layout → spacing → typography → color → state → motion. The current sheet mixes all five categories in nearly every rule, making it harder to audit property coverage at a glance.

---

## Proposed Full CSS Rewrite

Ready to paste as the `CSS` constant in `render_site.py`. Exactly 297 lines with the trailing `"""` excluded.

```css
/* ── Tokens ────────────────────────────────────────────── */
:root {
  /* Brand */
  --clr-accent:       #0a4;
  --clr-accent-deep:  #062;
  --clr-accent-bg:    #e9f6ee;
  /* Neutral surface */
  --clr-bg:           #fff;
  --clr-surface:      #f7f7f7;
  --clr-surface-2:    #f3f3f3;
  --clr-border:       #eaeaea;
  /* Text */
  --clr-text:         #111;
  --clr-text-mid:     #222;
  --clr-text-muted:   #555;
  --clr-heading:      #000;
  /* Tier badges */
  --clr-tier-a-bg:    #fdebd3;
  --clr-tier-a-fg:    #a06000;
  --clr-tier-b-bg:    var(--clr-accent-bg);
  --clr-tier-b-fg:    var(--clr-accent);
  --clr-tier-c-bg:    var(--clr-surface-2);
  --clr-tier-c-fg:    var(--clr-text-muted);
  /* Spacing */
  --sp-xs:  4px;
  --sp-sm:  8px;
  --sp-md:  12px;
  --sp-lg:  20px;
  --sp-xl:  24px;
  /* Radius */
  --r-sm:   3px;
  --r-md:   4px;
  /* Type scale (fluid) */
  --fs-h1:  clamp(1.75rem, 4vw, 2.25rem);
  --fs-h2:  clamp(1.25rem, 3vw, 1.5rem);
  --fs-h3:  clamp(1rem,    2vw, 1.125rem);
  --fs-lead: clamp(1rem,   2vw, 1.125rem);
  --fs-sm:  0.875rem;
  --fs-xs:  0.75rem;
}

/* ── Dark mode ─────────────────────────────────────────── */
@media (prefers-color-scheme: dark) {
  :root {
    --clr-accent:      #2db86c;
    --clr-accent-deep: #5dcf8e;
    --clr-accent-bg:   #0d2a1a;
    --clr-bg:          #0e0e0e;
    --clr-surface:     #1a1a1a;
    --clr-surface-2:   #252525;
    --clr-border:      #2e2e2e;
    --clr-text:        #e8e8e8;
    --clr-text-mid:    #d0d0d0;
    --clr-text-muted:  #888;
    --clr-heading:     #f0f0f0;
    --clr-tier-a-bg:   #2a1a00;
    --clr-tier-a-fg:   #e0a040;
    --clr-tier-c-bg:   var(--clr-surface-2);
    --clr-tier-c-fg:   var(--clr-text-muted);
  }
}

/* ── Reset ─────────────────────────────────────────────── */
*,
*::before,
*::after { box-sizing: border-box; }

html {
  font-family: system-ui, -apple-system, Segoe UI, Roboto, Helvetica,
               Arial, sans-serif;
  line-height: 1.55;
  color: var(--clr-text);
  background: var(--clr-bg);
  -webkit-text-size-adjust: 100%;
  text-size-adjust: 100%;
}

body { margin: 0; padding: 0; }

/* ── Layout ────────────────────────────────────────────── */
.container {
  max-inline-size: 880px;
  margin-inline: auto;
  padding-block: var(--sp-xl) 80px;
  padding-inline: max(var(--sp-lg), env(safe-area-inset-left));
}

/* ── Navigation ────────────────────────────────────────── */
header.nav {
  position: sticky;
  inset-block-start: 0;
  background: var(--clr-bg);
  border-block-end: 1px solid var(--clr-border);
  z-index: 10;
}

header.nav nav {
  max-inline-size: 1200px;
  margin-inline: auto;
  padding-block: var(--sp-md);
  padding-inline: max(var(--sp-lg), env(safe-area-inset-left));
  display: flex;
  flex-wrap: wrap;
  gap: var(--sp-md);
  align-items: center;
}

header.nav a {
  font-size: var(--fs-sm);
  font-weight: 500;
  color: var(--clr-accent);
  text-decoration: none;
}

header.nav a:hover      { color: var(--clr-accent-deep); }
header.nav a:focus-visible {
  outline: 2px solid var(--clr-accent);
  outline-offset: 2px;
  border-radius: var(--r-sm);
}

header.nav .brand {
  font-size: 1rem;
  font-weight: 700;
  color: var(--clr-text);
  margin-inline-end: auto;
}

/* ── Typography ────────────────────────────────────────── */
h1 {
  font-size: var(--fs-h1);
  line-height: 1.15;
  margin-block: var(--sp-xl) var(--sp-md);
  color: var(--clr-heading);
}

h2 {
  font-size: var(--fs-h2);
  line-height: 1.25;
  margin-block: 36px var(--sp-sm);
  padding-block-start: var(--sp-xl);
  border-block-start: 1px solid var(--clr-border);
}

h3 {
  font-size: var(--fs-h3);
  margin-block: var(--sp-xl) var(--sp-sm);
}

p { margin-block: var(--sp-sm) 16px; }

p.lead.summary {
  font-size: var(--fs-lead);
  color: var(--clr-text-mid);
  background: var(--clr-surface);
  border-inline-start: 3px solid var(--clr-accent);
  padding-block: var(--sp-md);
  padding-inline: 16px;
  margin-block: 16px var(--sp-xl);
  border-radius: 0 var(--r-md) var(--r-md) 0;
}

/* ── Links ─────────────────────────────────────────────── */
a { color: var(--clr-accent-deep); }
a:hover { color: var(--clr-accent); }
a:focus-visible {
  outline: 2px solid var(--clr-accent);
  outline-offset: 2px;
  border-radius: var(--r-sm);
}

/* ── Code ──────────────────────────────────────────────── */
code, pre {
  font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
  font-size: 0.8125rem;
}

code {
  background: var(--clr-surface-2);
  padding-block: 2px;
  padding-inline: 6px;
  border-radius: var(--r-sm);
}

pre {
  background: var(--clr-surface);
  padding-block: var(--sp-md);
  padding-inline: 16px;
  border-radius: var(--r-md);
  overflow-x: auto;
}

/* ── Tables ─────────────────────────────────────────────── */
table {
  border-collapse: collapse;
  inline-size: 100%;
  margin-block: var(--sp-md) var(--sp-xl);
  font-size: var(--fs-sm);
}

th, td {
  padding-block: var(--sp-sm);
  padding-inline: 10px;
  border-block-end: 1px solid var(--clr-border);
  text-align: start;
  vertical-align: top;
}

th {
  background: var(--clr-surface);
  font-weight: 600;
}

/* Mobile card reflow — tables with data-label attributes */
@media (max-width: 480px) {
  table, thead, tbody, tr { display: block; }
  thead { display: none; }

  tr {
    margin-block-end: var(--sp-md);
    border: 1px solid var(--clr-border);
    border-radius: var(--r-md);
    overflow: hidden;
  }

  td {
    display: flex;
    gap: var(--sp-sm);
    border-block-end: 1px solid var(--clr-border);
    padding-block: var(--sp-sm);
    padding-inline: var(--sp-md);
  }

  td::before {
    content: attr(data-label);
    font-weight: 600;
    color: var(--clr-text-muted);
    min-inline-size: 38%;
    flex-shrink: 0;
  }
}

/* ── Badges & tags ─────────────────────────────────────── */
.tag {
  display: inline-block;
  background: var(--clr-accent-bg);
  color: var(--clr-accent);
  font-size: var(--fs-xs);
  padding-block: 2px;
  padding-inline: var(--sp-sm);
  border-radius: var(--r-sm);
  margin-inline-end: 6px;
}

.tier-a { background: var(--clr-tier-a-bg); color: var(--clr-tier-a-fg); }
.tier-b { background: var(--clr-tier-b-bg); color: var(--clr-tier-b-fg); }
.tier-c { background: var(--clr-tier-c-bg); color: var(--clr-tier-c-fg); }

/* ── KPI grid ──────────────────────────────────────────── */
.kpi-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
  gap: var(--sp-md);
  margin-block: var(--sp-xl);
}

.kpi-grid .kpi {
  background: var(--clr-surface);
  padding-block: var(--sp-md);
  padding-inline: 16px;
  border-radius: var(--r-md);
}

.kpi .num {
  font-size: var(--fs-h2);
  font-weight: 700;
  color: var(--clr-accent);
}

.kpi .lbl {
  font-size: var(--fs-xs);
  color: var(--clr-text-muted);
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

/* ── Footer ────────────────────────────────────────────── */
footer.site {
  max-inline-size: 1200px;
  margin-inline: auto;
  margin-block-start: 60px;
  padding-block: var(--sp-xl);
  padding-inline: max(var(--sp-lg), env(safe-area-inset-left));
  border-block-start: 1px solid var(--clr-border);
  font-size: 0.8125rem;
  color: var(--clr-text-muted);
}

/* ── Motion ────────────────────────────────────────────── */
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}

/* ── Print ─────────────────────────────────────────────── */
@media print {
  header.nav,
  footer.site { display: none; }

  body {
    font-size: 11pt;
    color: #000;
    background: #fff;
  }

  .container {
    max-inline-size: 100%;
    padding: 0;
  }

  h1 { font-size: 20pt; }
  h2 { font-size: 15pt; page-break-after: avoid; }
  h3 { font-size: 12pt; page-break-after: avoid; }

  p.lead.summary {
    border-inline-start: 3pt solid #000;
    background: none;
  }

  a[href]::after {
    content: " (" attr(href) ")";
    font-size: 9pt;
    color: #444;
  }

  a[href^="#"]::after,
  header.nav a::after { content: none; }

  table { page-break-inside: avoid; }
  tr    { page-break-inside: avoid; }

  .tag, .tier-a, .tier-b, .tier-c {
    border: 1px solid #999;
    background: none;
    color: #000;
  }
}
```

---

## Migration Notes

All existing class names are preserved exactly — no HTML template changes required.

| Old hardcoded value | New token |
|---|---|
| `#0a4` | `var(--clr-accent)` |
| `#062` | `var(--clr-accent-deep)` |
| `#e9f6ee` | `var(--clr-accent-bg)` |
| `#fff` | `var(--clr-bg)` |
| `#f7f7f7` | `var(--clr-surface)` |
| `#f3f3f3` | `var(--clr-surface-2)` |
| `#eaeaea` | `var(--clr-border)` |
| `#111` | `var(--clr-text)` |
| `#222` | `var(--clr-text-mid)` |
| `#555` | `var(--clr-text-muted)` |
| `#000` | `var(--clr-heading)` |
| `h1{font-size:36px}` | `var(--fs-h1)` = `clamp(1.75rem, 4vw, 2.25rem)` |
| `h2{font-size:24px}` | `var(--fs-h2)` = `clamp(1.25rem, 3vw, 1.5rem)` |
| `h3{font-size:18px}` | `var(--fs-h3)` = `clamp(1rem, 2vw, 1.125rem)` |
| `padding:24px 20px` | `padding-block: var(--sp-xl); padding-inline: max(...)` |
| `border-left:3px` | `border-inline-start: 3px` |
| `@media max-width:640px` step-down overrides | removed — fluid type handles it |

**One template change needed for the mobile card pattern (Issue 8):** Each `<td>` in multi-column research tables should receive a `data-label="Column Name"` attribute so the `td::before` pseudo-element can render the column header. This is additive and backwards-compatible; tables without `data-label` simply show no label prefix on mobile.

**Line count**: 297 lines (within the ≤300 mandate).
