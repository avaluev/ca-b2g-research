# Trust & Brand Audit — Central Asia B2G Intelligence
**Auditor:** Trust & Brand specialist (agent 13)
**Date:** 2026-05-03
**Site:** https://avaluev.github.io/ca-b2g-research/
**Repo:** https://github.com/avaluev/ca-b2g-research

---

## 10-Second Test Result

**PASS with reservations.** The first scroll delivers: topic (Central Asia B2G AI/digital), scope (100 initiatives, 9 KPI tiles), method summary (11-agent pipeline, $20 budget, Claude + Perplexity), and purpose (typed, source-cited knowledge graph). The lead paragraph is sharp.

The reservations: the author is named only in JSON-LD (invisible to human readers), nowhere in rendered HTML. There is no photo. No author bio above the fold, no bio anywhere on the site. A first-time visitor has no answer to "who built this and why should I trust them?" beyond the GitHub link buried in the footer. The Honesty and Provenance pages are in the nav but not highlighted as differentiating assets — they sit equal to Procurement and Trends. That hierarchy is wrong; Honesty is the trust anchor.

---

## Trust Surface Inventory

| Signal | Present | Quality | Recommendation |
|---|---|---|---|
| Author name (visible HTML) | No | — | Add to home page H1 section and footer |
| Author name (JSON-LD) | Yes | Good | Retained, but insufficient alone |
| LinkedIn link | JSON-LD only | Invisible | Render as visible link in footer + home |
| GitHub link | Footer text | Minimal | Add nav-level GitHub icon + star count |
| Author photo | No | — | Add to home page and author bio page |
| Author bio (background, why CA) | No | — | Create `/about/` page, link from home |
| Apache 2.0 badge | Text only | Weak | Replace with SVG badge in footer |
| License file | Yes (repo) | Good | Surface link in footer |
| "How built" / Methodology | Yes | Good | Already prominent in nav |
| Prompts public (GH) | GH agents exist | Buried | Surface "every prompt is public" on home |
| "Last updated" visible date | No | — | Add visible date string below H1 |
| Methodology reviewed date | No | — | Add to `/methodology/` page |
| Refresh schedule | No | — | Declare quarterly cadence explicitly |
| Honesty page | Yes, excellent | Strong | Promote to home-page callout box |
| Provenance page | Yes | Strong | Promote; link from Honesty |
| Contact mechanism | Email in JSON-LD only | Hidden | Add to footer, About page, home |
| GitHub Issues / Discussions | Not surfaced | — | Link "Found an error? Open an issue" |
| Versioning / semver | No | — | Adopt date-based versioning |
| "Reproduce yourself" CTA | No | — | Add to home and methodology |
| Acknowledgments page | No | — | Create or add section to methodology |
| Ethics / PII partition note | Buried in CLAUDE.md | Invisible | Surface on honesty or about page |
| Marketing claim audit | Clean | Pass | No banned phrases found in rendered HTML |
| Citation of this site | Not tracked | — | Future placeholder; add section to provenance |

---

## 12 Specific Additions

**1. Visible author block on home page**
*Page:* `index.html`, immediately below the lead summary paragraph.
*Proposed copy:*
> Research by **Alexandr Valuev** — [LinkedIn](https://www.linkedin.com/in/avaluev/) · [GitHub](https://github.com/avaluev) · valuev.alexandr@gmail.com

*Why:* author name exists only in machine-readable JSON-LD. Human readers see no name.

**2. Honesty callout box on home**
*Page:* `index.html`, after "Where to start" section.
*Proposed copy:*
> **What this research did not find.** Four named contacts are wrong as of audit date. Defense procurement is absent. The post-April 2026 Kyrgyz institutional structure is partially unconfirmed. Read [Honesty](/honesty/) before acting on any Tier-A recommendation.

*Why:* Honesty page is the single strongest differentiator. It is currently listed only in the nav, equal to all other nav items. It needs a visual call-to-action.

**3. "Every prompt is public" sentence on home**
*Page:* `index.html`, in the "How was it produced?" section.
*Proposed addition:* Append to existing paragraph: "Every agent prompt is public at [github.com/avaluev/ca-b2g-research/.claude/agents](https://github.com/avaluev/ca-b2g-research/tree/main/.claude/agents)."

**4. Visible "Last updated" date below H1**
*Page:* All pages. Current `dateModified` exists in meta only.
*Proposed copy:* Add `<p class="updated">Last updated: 3 May 2026</p>` with muted styling, immediately below the H1 on every page.

**5. Methodology review date + refresh schedule**
*Page:* `/methodology/`
*Proposed copy:* Add to end of page: "Methodology last reviewed: 3 May 2026. Quarterly refresh cadence: next update planned August 2026."

**6. "Reproduce this report yourself" CTA**
*Page:* `index.html` bottom, and `/methodology/`.
*Proposed copy:*
> **Reproduce this report.** Clone the repo, set your OpenRouter key to $20, and run `bash scripts/run-parallel.sh wave-1` through `wave-6`. Total cost: approximately $20. Total time: 3–6 hours depending on model latency. All agent prompts, schemas, and gate scripts are included.
> [Clone on GitHub →](https://github.com/avaluev/ca-b2g-research)

**7. Author bio page (`/about/`)**
*Page:* New page `/about/`.
*Content outline:* Who Alexandr Valuev is (background, domain expertise, motivation for CA focus), link to LinkedIn, GitHub, professional context. Link from footer and from the author block on home page. No photo is required day one, but the page establishes a location for it.

**8. Ethics / PII note surfaced in Honesty**
*Page:* `/honesty/`, add a new H2 section.
*Proposed copy:*
> **What was deliberately not published.** Private mobile numbers, home addresses, and personal email addresses for any named individual were excluded even where available. Political-loyalty speculation was excluded. The outreach bundles (Tier-A/B pitch materials) are in a private vault, not in this public knowledge graph. This boundary reflects the MUST NOT constraints in the research protocol.

**9. GitHub "Found an error?" link**
*Page:* Footer of all pages.
*Proposed copy:* Add after the Apache 2.0 line: "Found an error? [Open an issue →](https://github.com/avaluev/ca-b2g-research/issues)"

**10. Acknowledgments section on `/methodology/`**
*Page:* `/methodology/`, new H2 "AI tools used".
*Proposed copy:*
> This research used Anthropic Claude Opus 4 and Sonnet 4 for the eleven research agents, Perplexity Sonar Deep Research and Sonar Pro for cross-model verification, and the OpenRouter API to route between models on a $20 budget. No proprietary data sources were used. All source URLs are in the knowledge graph. The agent definitions are open-source in `.claude/agents/`.

**11. Apache 2.0 SVG badge in footer**
*Page:* All pages (footer).
*Proposed change:* Replace plain text "Apache 2.0" with `<img src="https://img.shields.io/badge/License-Apache%202.0-green.svg" alt="Apache 2.0 license" height="20">` linking to the LICENSE file.

**12. Citations of this site (placeholder)**
*Page:* `/provenance/`.
*Proposed copy:* Add H2 "External citations": "This section will track any external publications, newsletters, or research that have cited this work. As of May 2026: none recorded. If you have cited or referenced this research, open an issue or email the author."

---

## Marketing Claims Audit

No banned phrases from `content-quality-gates.md` were found in rendered HTML. The following borderline phrases are fine as written:
- "Every claim is typed, verifiable, and cross-referenced" — specific and defensible, not a badge claim.
- "28 initiatives are rated Tier-A — deal-ready" — grounded in the scoring rubric, not an unverified marketing claim.

No "100% link-verified", "Zero LLM arithmetic", "12 specialist agents", or similar badges found. Pass.

---

## Versioning Scheme Proposal

**Recommendation: date-based, not semantic.**

Semantic versioning (`v1.2.3`) implies a software interface contract — breaking changes in major, additions in minor, patches for bugs. Research data has no stable API that users depend on. A bug fix to a wrong minister name is not a "patch" in any meaningful sense; it can change a user's entire strategy.

**Proposed scheme:** `YYYY-MM` data vintage, appended to every record's `last_verified_date` and surfaced as a site-level badge.

- Footer: "Data vintage: 2026-05"
- Every page `<meta name="dateModified">`: already present, already accurate.
- On Provenance page: a changelog table by month listing what changed.
- Next update: "2026-08 vintage" when the quarterly refresh runs.

This scheme is self-explanatory to non-technical readers and directly answers "how stale is this?"

---

## "Reproduce Yourself" CTA — Wording and Placement

**Placement:** Two locations.
1. Home page — after the KPI grid, before "What is in this research?"
2. Bottom of `/methodology/` page.

**Wording:**

> **Run this research yourself.**
> The full pipeline is open-source. Clone the repo, add an OpenRouter API key (budget: $20), and run six waves of parallel agents. Every prompt, schema, gate script, and quality check is included.
>
> `git clone https://github.com/avaluev/ca-b2g-research`
> `bash scripts/setup.sh && bash scripts/run-parallel.sh wave-1`
>
> Expected cost: ~$20. Expected time: 3–6 hours. [Full instructions →](/methodology/)

---

## Footer Redesign

**Current footer (all pages):**
```
Open research on AI/digital government opportunities in Uzbekistan + Kyrgyzstan.
Apache 2.0 — github.com/avaluev/ca-b2g-research. Built 2026-05-04.
```

**Proposed footer:**
```
Open research on AI/digital government opportunities in Uzbekistan + Kyrgyzstan.
By Alexandr Valuev — LinkedIn · GitHub · valuev.alexandr@gmail.com
[Apache 2.0 badge] Data vintage: 2026-05 · Found an error? Open an issue
```

Changes: author name visible, LinkedIn clickable, email visible, Apache badge not plain text, data vintage replaces "Built" timestamp, GitHub Issues CTA added.

---

## Author Bio and Photo Plan

**Immediate (no photo required):**
- Create `/about/` with: name, domain expertise, motivation for this specific research, links to LinkedIn and GitHub.
- Add author line to home page below lead paragraph.
- Add author name to footer.

**Photo (recommended, not blocking):**
- A professional headshot or even a GitHub avatar improves trustworthiness for non-technical readers.
- Add as `<img>` on `/about/` page with descriptive `alt` text, explicit `width` and `height`.
- If a headshot is unavailable, a GitHub-rendered avatar from `https://github.com/avaluev.png` is acceptable as a placeholder.

**Minimum viable bio (proposed):**
> Alexandr Valuev is an independent researcher focused on B2G technology markets in frontier emerging economies. This research was produced in May 2026 using a multi-agent AI pipeline on a $20 compute budget, with all sources and methods published openly under Apache 2.0.

---

## Acknowledgments Page Outline

Merge into `/methodology/` as a final H2 rather than a standalone page (reduces nav complexity).

**Section: "What built this"**
- Anthropic Claude Opus 4 — adversarial audit and synthesis agents
- Anthropic Claude Sonnet 4 — research and extraction agents
- Perplexity Sonar Deep Research + Sonar Pro — cross-model verification (8 paid calls)
- OpenRouter — model routing, $20 total budget cap
- GitHub Actions — CI/CD for quality gate enforcement
- GitHub Pages — hosting

**Section: "What this research cost"**
- Compute: ~$20 OpenRouter credits
- Time: approximately 40 hours of agent run time across six parallel waves
- Human editorial: approximately 4 hours of prompt engineering and gate tuning

**Section: "What this research deliberately excluded"**
- Cross-reference to Honesty page ethics section (item 8 above)

---

## Summary Priority Stack

High impact, low effort:
1. Add author name and email to rendered footer and home page (30 min)
2. Add Honesty callout box to home page (1 hour)
3. Add "every prompt is public" sentence to home page (15 min)
4. Add visible "Last updated" date below H1 on all pages (30 min)

Medium impact, medium effort:
5. Create `/about/` author bio page (2 hours)
6. Add "Reproduce yourself" CTA to home and methodology (1 hour)
7. Add ethics/PII section to Honesty page (1 hour)
8. Add acknowledgments section to Methodology (1 hour)

Lower urgency:
9. Replace Apache text with badge (30 min)
10. Add "Found an error? Open an issue" to footer (15 min)
11. Add citations placeholder to Provenance (30 min)
12. Add methodology review date and refresh schedule (30 min)
