# Auditor AI Team — 16 Specialists

> Sixteen parallel specialists audit every release. Each runs as an independent
> Claude sub-agent against the live site + the local repo. Reports land in
> `state/audit/team/*.md`. Re-run any specialist by passing its dispatch prompt
> to a fresh Claude session.

## Why a 16-specialist team?

A single reviewer always misses dimensions outside their lane. A research site
serves vendors, donors, investors, government officials, journalists,
contributors, and AI search crawlers — each judges different things. The
specialists below are organised so each pair of dimensions has at least one
dedicated auditor.

## The team

| # | Specialist | Mandate | Output | Dispatch prompt |
|---|---|---|---|---|
| **01** | Reference Benchmarker | Score audit site vs `padel-market-analysis` reference dimension-by-dimension | `state/audit/team/01_reference_benchmark.md` | [01_reference_benchmark.md](01_reference_benchmark.md) |
| **02** | Information Architect | Page hierarchy, nav, breadcrumbs, internal-link graph, scent of information | `state/audit/team/02_information_architecture.md` | [02_information_architect.md](02_information_architect.md) |
| **03** | Content Voice Editor | Humanise voice, kill jargon, plain English, FK grade ≤ 10 | `state/audit/team/03_voice_edit.md` | [03_content_voice.md](03_content_voice.md) |
| **04** | Citation / Provenance Auditor | Numeric-claim traceability, RU/UZ/KY share, dead-link health, Wayback fallback | `state/audit/team/04_citations.md` | [04_citation_provenance.md](04_citation_provenance.md) |
| **05** | GEO / AIO / AEO / LLMO Specialist | llms.txt, JSON-LD `@graph`, FAQPage, Dataset, HowTo, citable summary leads, AI-crawler robots.txt | `state/audit/team/05_geo_aio_aeo_llmo.md` | [05_geo_aio_aeo_llmo.md](05_geo_aio_aeo_llmo.md) |
| **06** | Visual / Typography Designer | Type scale, line length 60–80ch, color contrast, whitespace rhythm | `state/audit/team/06_visual_typography.md` | [06_visual_typography.md](06_visual_typography.md) |
| **07** | Mobile-First QA | 320–1440 px, tap targets ≥ 44 px, no horizontal scroll, sticky-nav UX | `state/audit/team/07_mobile.md` | [07_mobile_first_qa.md](07_mobile_first_qa.md) |
| **08** | Accessibility (WCAG 2.2 AA) Auditor | Skip-link, focus-visible, scope=col, lang attribution, 4.5:1 contrast, keyboard parity | `state/audit/team/08_accessibility.md` | [08_accessibility_wcag_aa.md](08_accessibility_wcag_aa.md) |
| **09** | Performance Engineer | Core Web Vitals, FCP < 0.4 s, CLS < 0.05, INP < 100 ms, bundle size, Lighthouse ≥ 97 | `state/audit/team/09_performance.md` | [09_performance.md](09_performance.md) |
| **10** | HTML Code Quality | Semantic HTML5, W3C-valid, landmarks, `<thead>/<tbody>`, `<abbr>`, `<time>`, `<cite>`, `<figure>` | `state/audit/team/10_html_quality.md` | [10_html_code_quality.md](10_html_code_quality.md) |
| **11** | CSS Architect | Custom properties, `clamp()` fluid type, logical props, `prefers-color-scheme`, print | `state/audit/team/11_css.md` | [11_css_architect.md](11_css_architect.md) |
| **12** | Data Visualization | Charts justify text, sortable tables, inline SVG, no chartjunk, mermaid for org charts | `state/audit/team/12_dataviz.md` | [12_data_visualization.md](12_data_visualization.md) |
| **13** | Trust & Brand | Author surface, license badge, "every prompt is public" signal, refresh cadence, ethics | `state/audit/team/13_trust_brand.md` | [13_trust_brand.md](13_trust_brand.md) |
| **14** | Conversion / CTA | One primary action per page, persona routing, cite-this-research widget, share row | `state/audit/team/14_conversion.md` | [14_conversion_cta.md](14_conversion_cta.md) |
| **15** | Internationalization | RU/UZ/KY name handling, Cyrillic font fallbacks, `<span lang>` attribution, hreflang | `state/audit/team/15_i18n.md` | [15_internationalization.md](15_internationalization.md) |
| **16** | Dev-Ex / Reproducibility | README clarity, mermaid architecture, CONTRIBUTING, issue templates, CI badges, citation | `state/audit/team/16_devex.md` | [16_devex_reproducibility.md](16_devex_reproducibility.md) |

## How to re-run the full audit

```bash
# 1. Fan out 16 specialists in parallel (one Claude session per specialist).
#    Each reads the live site at https://avaluev.github.io/ca-b2g-research/
#    plus the repo at /path/to/ca-b2g-research/.
for spec in .claude/audit-team/*.md; do
  echo "Dispatch: $spec"
done

# 2. Each specialist writes to state/audit/team/<NN>_*.md
# 3. Synthesise the reports into a remediation plan
# 4. Apply patches; re-render; re-deploy; verify
```

In practice we use Claude Code's `Agent` tool with `subagent_type=general-purpose`
and `run_in_background=true`, dispatching all 16 in a single message. Total
wall-clock per audit pass: ≈ 30 minutes. Estimated cost (Anthropic): ≈ USD 4–8
on Sonnet (no paid OpenRouter calls used by the audit team itself — they read
public web + local files).

## What the audit caught in the v1.0.0 release

- 17 HIGH severity issues + 16 MEDIUM + 2 LOW
- 4 wrong Tier-1 identities corrected via paid Sonar Pro re-verification
- WCAG contrast failure (`#00aa44` at 2.89:1) before the audit; replaced with
  `#005c27` at 4.5:1 after
- OG image referenced `.png` but only `.svg` existed — every social share card
  was broken until this audit caught it
- 169 Cyrillic cells without `lang=` attribution; auto-wrapped via the new
  `ru()` helper
- Nav buried H1 below the fold at 320 px — fixed with a CSS-only hamburger
  pattern and tap targets ≥ 44 px

Reports for every specialist are public under `state/audit/team/`. Each one
names what it found, the priority (P0/P1/P2), and pasteable patches.
