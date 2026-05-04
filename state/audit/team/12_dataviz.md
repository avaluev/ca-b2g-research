# Data Visualization Audit — CA B2G Research Site
Auditor: 12_dataviz | Date: 2026-05-03

---

## 1. Current Visual Primitive Inventory

| Page | Tables | ~Rows | Cols | Sortable | Filterable | SVG | Chart.js | KPI Grid |
|---|---|---|---|---|---|---|---|---|
| Home (`/`) | 0 | — | — | — | — | 0 | No | Yes |
| Decrees UZ | 1 | 56 | 7 | No | No | 0 | No | — |
| Decrees KG | 1 | 44 | 7 | No | No | 0 | No | — |
| Institutions | 1 | 105 | 6 | No | No | 0 | No | Yes |
| Donors | 1 | 49 | 6 | No | No | 0 | No | Yes |
| Procurement | 1 | 50 | 6 | No | No | 0 | No | Yes |
| Trends | 2 | 61 | 8 | No | No | 0 | No | Yes |
| People | 1 | 68 | 6 | No | No | 0 | No | Yes |
| Initiatives | 1 | 100 | 7 | No | No | 0 | No | Yes |
| MVPs | 1 | 200 | 8 | No | No | 0 | No | Yes |
| Lenses | 0 | — | — | — | — | 0 | No | Yes |
| Methodology | 1 | 7 | 3 | No | No | 0 | No | — |
| Scoring | 0 | — | — | — | — | 0 | No | — |
| Honesty | 0 | — | — | — | — | 0 | No | — |
| Provenance | 0 | — | — | — | — | 0 | No | — |

**Finding**: Zero charts anywhere. No sortable tables. Five tables exceed 50 rows (critical usability gap). No inline SVG, no Mermaid rendered on-page, no sparklines.

---

## 2. Charts That Should Exist (Priority Order)

| # | Page | Chart | Type | What It Communicates |
|---|---|---|---|---|
| C1 | Home | "What's in the data" | Horizontal bar (counts) | 9 entity types: Decrees 100, Cases 100, MVPs 200, Initiatives 100, Institutions 105, People 117, Trends 61, Donors 49, Tenders 50 |
| C2 | Home | Donor pipeline total | Single stat + donut | $2.55B total; WB 54%, ADB 11%, EBRD 10%, IsDB 9%, EU 4%, others |
| C3 | Decrees UZ+KG | Decree volume by year | Bar (2015–2026) | Acceleration pattern: 1–4/yr pre-2022, 9→24→30→8 from 2022–2026 |
| C4 | Decrees UZ+KG | Half-life status | Donut | Implementing 69%, Active Window 18%, Amended 12%, Expired 1% |
| C5 | Donors | Budget by organization | Horizontal bar | WB $1.37B, ADB $270M, EBRD $250M, IsDB $220M, EU $104M, AIIB $100M |
| C6 | Trends | Lens-tag distribution | Bar | donor_co_financed 38, decree_half_life_active 31, russian_cis_substitution 28, karimov_inversion 15, japarov_concentration 13 |
| C7 | Trends | Sector × maturity | Heatmap grid | 10 sectors × 3 maturity levels — shows emerging vs. accelerating concentration |
| C8 | Initiatives | 5-axis score radar | Radar (avg per country) | UZ vs KG mean scores on speed/moat/defensibility/capital/cis_fit |
| C9 | Initiatives | Score distribution | Mini histogram (10 bins) | Spread of weighted_total across 100 initiatives |
| C10 | MVPs | Category distribution | Donut | free_tool 66, content 48, managed_service 44, ai_tool 21, saas 11 |
| C11 | MVPs | Confidence tier per country | Stacked bar | UZ/KG × A/B/C tiers showing quality split |
| C12 | Procurement | Pipeline value by country | Bar + total label | UZ $312.6M vs KG $34.9M — 9:1 ratio communicates market asymmetry |

**ASCII sketch — C3 (Decree volume bar):**
```
2022 |████████ 9
2023 |████████ 9
2024 |████████████████████████ 24
2025 |██████████████████████████████ 30
2026 |████████ 8 (YTD)
```

**ASCII sketch — C7 (Sector × maturity heatmap):**
```
              | emerging | accelerating | mainstream
Public Admin  |    4     |      5       |     0
Finance       |    6     |      8       |     0
AI Infra      |    5     |      7       |     1
Health        |    3     |      2       |     0
Education     |    4     |      1       |     0
```

---

## 3. Inline SVG Generator Pattern (Python helpers for `render_site.py`)

Drop these functions into `render_site.py` above the page builders. Zero external dependencies.

```python
def svg_bar_h(data: list[tuple[str, float]], *, width=420, bar_h=20,
               color="#0a4", title="") -> str:
    """Horizontal bar chart. data = [(label, value), ...]. ≤25 lines."""
    if not data: return ""
    max_v = max(v for _, v in data) or 1
    gap, pad_l = 6, 110
    h = len(data) * (bar_h + gap) + 30
    rows = []
    for i, (label, val) in enumerate(data):
        y = 24 + i * (bar_h + gap)
        bw = int((val / max_v) * (width - pad_l - 8))
        rows.append(
            f'<text x="{pad_l-4}" y="{y+bar_h-6}" text-anchor="end" '
            f'font-size="11" fill="#333">{label[:18]}</text>'
            f'<rect x="{pad_l}" y="{y}" width="{bw}" height="{bar_h}" '
            f'fill="{color}" rx="2"/>'
            f'<text x="{pad_l+bw+4}" y="{y+bar_h-6}" font-size="11" fill="#555">'
            f'{val:,.0f}</text>'
        )
    title_el = f'<text x="0" y="14" font-size="12" font-weight="600" fill="#111">{title}</text>' if title else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{h}" '
            f'role="img" aria-label="{title}">{title_el}{"".join(rows)}</svg>')


def svg_donut(slices: list[tuple[str, float]], *, r=70, title="") -> str:
    """Donut chart. slices = [(label, value), ...]. ≤28 lines."""
    import math
    if not slices: return ""
    total = sum(v for _, v in slices) or 1
    colors = ["#0a4","#5bc47c","#a3dbb5","#d4edda","#b2dfdb","#80cbc4","#4db6ac"]
    cx = cy = r + 10
    w = h = (r + 10) * 2
    legend_y = h + 10
    arcs, legend = [], []
    angle = -math.pi / 2
    for i, (label, val) in enumerate(slices):
        frac = val / total
        a2 = angle + frac * 2 * math.pi
        x1, y1 = cx + r * math.cos(angle), cy + r * math.sin(angle)
        x2, y2 = cx + r * math.cos(a2), cy + r * math.sin(a2)
        ri = r * 0.55
        xi1, yi1 = cx + ri * math.cos(a2), cy + ri * math.sin(a2)
        xi2, yi2 = cx + ri * math.cos(angle), cy + ri * math.sin(angle)
        lf = 1 if frac > 0.5 else 0
        clr = colors[i % len(colors)]
        arcs.append(f'<path d="M{x1:.1f},{y1:.1f} A{r},{r} 0 {lf},1 {x2:.1f},{y2:.1f} '
                    f'L{xi1:.1f},{yi1:.1f} A{ri},{ri} 0 {lf},0 {xi2:.1f},{yi2:.1f} Z" fill="{clr}"/>')
        legend.append(f'<rect x="0" y="{legend_y+i*16}" width="10" height="10" fill="{clr}"/>'
                      f'<text x="14" y="{legend_y+i*16+9}" font-size="11" fill="#333">'
                      f'{label[:20]} {val/total*100:.0f}%</text>')
        angle = a2
    title_el = (f'<text x="{cx}" y="{cy+4}" text-anchor="middle" font-size="11" '
                f'font-weight="600" fill="#111">{title}</text>') if title else ""
    total_h = h + 10 + len(slices) * 16 + 4
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w+120}" height="{total_h}" '
            f'role="img" aria-label="{title}">{"".join(arcs)}{title_el}{"".join(legend)}</svg>')


def svg_sparkline(values: list[float], *, width=80, height=24, color="#0a4") -> str:
    """Inline sparkline. values = list of floats (e.g., monthly counts). ≤12 lines."""
    if len(values) < 2: return ""
    mn, mx = min(values), max(values)
    rng = (mx - mn) or 1
    xs = [i * (width - 2) / (len(values) - 1) + 1 for i in range(len(values))]
    ys = [height - 2 - (v - mn) / rng * (height - 4) for v in values]
    pts = " ".join(f"{x:.1f},{y:.1f}" for x, y in zip(xs, ys))
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
            f'role="img" aria-label="trend sparkline">'
            f'<polyline points="{pts}" fill="none" stroke="{color}" stroke-width="1.5"/></svg>')


def svg_histogram(values: list[float], *, bins=10, width=300, height=120,
                  color="#0a4", xlabel="Score") -> str:
    """Mini histogram for score distributions. ≤28 lines."""
    if not values: return ""
    mn, mx = min(values), max(values)
    step = (mx - mn) / bins or 1
    counts = [0] * bins
    for v in values:
        idx = min(int((v - mn) / step), bins - 1)
        counts[idx] += 1
    max_c = max(counts) or 1
    bw = (width - 20) / bins
    pad_b = 30
    bars = []
    for i, c in enumerate(counts):
        bh = int(c / max_c * (height - pad_b))
        x = 10 + i * bw
        y = height - pad_b - bh
        bars.append(f'<rect x="{x:.1f}" y="{y}" width="{bw-1:.1f}" height="{bh}" fill="{color}" rx="1"/>')
    # x-axis labels at min and max
    axis = (f'<line x1="10" y1="{height-pad_b}" x2="{width-10}" y2="{height-pad_b}" '
            f'stroke="#ccc" stroke-width="1"/>'
            f'<text x="10" y="{height-14}" font-size="10" fill="#777">{mn:.1f}</text>'
            f'<text x="{width-10}" y="{height-14}" font-size="10" fill="#777" text-anchor="end">{mx:.1f}</text>'
            f'<text x="{width//2}" y="{height-4}" font-size="10" fill="#777" text-anchor="middle">{xlabel}</text>')
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
            f'role="img" aria-label="{xlabel} distribution">{"".join(bars)}{axis}</svg>')
```

---

## 4. Sortable Table Progressive Enhancement (vanilla JS, ≤30 lines)

Inject once before `</body>` on all pages with large tables. Targets any `<table data-sort>`.

```html
<script>
(function(){
  document.querySelectorAll('table[data-sort]').forEach(function(tbl){
    var th=tbl.querySelectorAll('thead th'),tbody=tbl.querySelector('tbody');
    var dir={};
    th.forEach(function(h,ci){
      h.style.cursor='pointer';h.title='Click to sort';
      h.addEventListener('click',function(){
        var rows=Array.from(tbody.querySelectorAll('tr'));
        dir[ci]=dir[ci]==='asc'?'desc':'asc';
        rows.sort(function(a,b){
          var av=(a.cells[ci]||{}).textContent||'';
          var bv=(b.cells[ci]||{}).textContent||'';
          var an=parseFloat(av.replace(/[^0-9.\-]/g,'')),bn=parseFloat(bv.replace(/[^0-9.\-]/g,''));
          var cmp=isNaN(an)||isNaN(bn)?av.localeCompare(bv):an-bn;
          return dir[ci]==='desc'?-cmp:cmp;
        });
        rows.forEach(function(r){tbody.appendChild(r);});
        th.forEach(function(x,i){x.textContent=x.textContent.replace(/ [▲▼]$/,'');});
        h.textContent+=(dir[ci]==='asc'?' ▲':' ▼');
      });
    });
  });
  // Pure-CSS pagination: hide rows after 25 via nth-child
  document.querySelectorAll('table[data-paginate]').forEach(function(tbl){
    var rows=tbl.querySelectorAll('tbody tr');
    var n=25;
    if(rows.length<=n)return;
    rows.forEach(function(r,i){if(i>=n)r.style.display='none';});
    var btn=document.createElement('button');
    btn.textContent='Show all '+rows.length+' rows';
    btn.style.cssText='margin:8px 0;padding:6px 14px;cursor:pointer;font-size:13px';
    btn.onclick=function(){rows.forEach(function(r){r.style.display='';});btn.remove();};
    tbl.insertAdjacentElement('afterend',btn);
  });
})();
</script>
```

Usage in `render_site.py`: emit `<table data-sort data-paginate>` for any table with ≥10 rows.

---

## 5. Mermaid Org Chart Inclusion Plan

`state/institutions/org_charts.md` contains two `graph TD` diagrams (UZ and KG org charts). Both are already written and L2_VERIFIED.

In `render_site.py`, inside the `build_institutions_page()` function, add after the table:

```python
# Read raw mermaid blocks from state file
import re as _re
_org_md = (ROOT / "state/institutions/org_charts.md").read_text()
_blocks = _re.findall(r'```mermaid\n(.*?)```', _org_md, _re.DOTALL)
mermaid_html = ""
for blk in _blocks:
    mermaid_html += f'<pre class="mermaid">{escape(blk.strip())}</pre>\n'
```

Then inject into the page HTML before `</body>`:

```html
{mermaid_html}
<script type="module">
  import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
  mermaid.initialize({startOnLoad:true,theme:'default'});
</script>
```

One CDN script tag, no build step, renders client-side. The `<pre class="mermaid">` elements are readable as plain text if JS fails (graceful degradation). This surfaces the two org charts on `/institutions/` with zero additional data authoring.

---

## 6. Inline SVG Map of UZ + KG

Simplified country outlines with major city dots. Uses approximate SVG coordinates (viewBox-scaled, not projection-accurate but visually correct for this use case).

```python
def svg_map_uz_kg(inst_by_city: dict | None = None) -> str:
    """
    Inline SVG map of Uzbekistan + Kyrgyzstan with city overlays.
    inst_by_city: optional {city_name: count} for dot sizing.
    ~75 lines total incl. city defs.
    """
    cities = [
        # (name, cx, cy, country)
        ("Tashkent",   188, 112, "UZ"),
        ("Samarkand",  148, 148, "UZ"),
        ("Namangan",   222, 105, "UZ"),
        ("Fergana",    232, 118, "UZ"),
        ("Bukhara",    112, 148, "UZ"),
        ("Nukus",       52, 108, "UZ"),
        ("Bishkek",    278, 100, "KG"),
        ("Osh",        242, 136, "KG"),
        ("Jalal-Abad", 230, 128, "KG"),
    ]
    # Approximate simplified outline paths (viewBox 0 0 380 240)
    uz_path = ("M50,80 L60,68 L80,62 L110,58 L140,52 L170,50 L200,54 "
               "L230,58 L255,65 L265,75 L268,90 L260,105 L248,115 "
               "L235,125 L220,135 L200,145 L175,155 L150,160 "
               "L125,158 L100,155 L80,148 L60,138 L45,125 L40,110 Z")
    kg_path = ("M248,80 L265,75 L285,72 L310,74 L330,78 L345,85 "
               "L350,95 L345,108 L330,118 L310,128 L290,135 "
               "L268,138 L252,132 L242,120 L240,108 L245,92 Z")
    dot_els = []
    for name, cx, cy, country in cities:
        cnt = (inst_by_city or {}).get(name, 0)
        r = max(4, min(10, 4 + cnt // 3))
        clr = "#0a4" if country == "UZ" else "#2563eb"
        dot_els.append(
            f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{clr}" opacity="0.8"/>'
            f'<text x="{cx}" y="{cy - r - 2}" text-anchor="middle" '
            f'font-size="9" fill="#333">{name}</text>'
        )
    labels = ('<text x="140" y="110" font-size="13" font-weight="600" '
              'fill="#0a4" opacity="0.7">Uzbekistan</text>'
              '<text x="295" y="100" font-size="13" font-weight="600" '
              'fill="#2563eb" opacity="0.7">Kyrgyzstan</text>')
    legend = ('<rect x="10" y="210" width="10" height="10" fill="#0a4"/>'
              '<text x="24" y="219" font-size="10" fill="#333">UZ institution</text>'
              '<rect x="110" y="210" width="10" height="10" fill="#2563eb"/>'
              '<text x="124" y="219" font-size="10" fill="#333">KG institution</text>'
              '<text x="220" y="219" font-size="10" fill="#777">dot size = institution count</text>')
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 380 230" '
        'width="100%" style="max-width:560px;height:auto" role="img" '
        'aria-label="Uzbekistan and Kyrgyzstan institution density map">'
        f'<path d="{uz_path}" fill="#e9f6ee" stroke="#0a4" stroke-width="1.5"/>'
        f'<path d="{kg_path}" fill="#dbeafe" stroke="#2563eb" stroke-width="1.5"/>'
        f'{labels}{"".join(dot_els)}{legend}'
        '</svg>'
    )
```

Add to institutions page: `svg_map_uz_kg({"Tashkent": 38, "Bishkek": 28, "Samarkand": 8, ...})`.

---

## Implementation Priority

1. **Immediate** (one `render_site.py` edit): add `data-sort data-paginate` attributes to all large tables + inject the JS snippet. Unblocks 200-row MVP table and 100-row initiatives table.
2. **High** (add helpers): `svg_bar_h` and `svg_donut` cover C1, C2, C5, C12 with real KG data.
3. **Medium**: Decree year bar (C3) and status donut (C4) — data is clean (`date` field, `half_life_status` field).
4. **Medium**: `svg_histogram` for initiatives scoring (C9) and MVP scores — 200 real `weighted_total` values available.
5. **Lower**: Mermaid org charts on `/institutions/` (one CDN tag, zero data work).
6. **Lower**: SVG map — good for home page hero; requires manual city-to-institution mapping.

Sparklines require `recent_decisions_12mo` data which is populated on institution records; wire to `svg_sparkline` once confirmed non-null.
