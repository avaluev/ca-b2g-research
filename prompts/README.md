# Prompts — every system prompt that built this research, in one place

> Most B2G market reports treat the prompt set as the proprietary moat. This
> repository treats it as the seventh wave of evidence. If the data is wrong,
> the prompts are how you find out why and fix it.

This directory is the public flat-file index of every prompt that produced
the research at <https://avaluev.github.io/ca-b2g-research>. The same prompts
live as Claude sub-agent specifications under `.claude/agents/` and
`.claude/audit-team/` — the directory you are reading is the human-friendly
mirror.

## How to read this

Two production teams + one publication team:

```
prompts/
├── pipeline/         The 12-agent research pipeline (Wave 0 → Wave 6)
│                     produces the knowledge graph.
├── audit-team/       16 specialists audit the rendered site after every
│                     release.
└── routing/          OpenRouter routing strategy + the HubSpot $1M MVR
                      framework encoding for the solopreneur track.
```

## Pipeline (Wave 0 → Wave 6, 12 agents)

| Wave | Agent | Model | Purpose | Spec |
|---|---|---|---|---|
| 0 | blueprint-architect | Opus xhigh | Strategic plan, target lists, constraint inventory | [`pipeline/00-blueprint-architect.md`](pipeline/00-blueprint-architect.md) |
| 1 | legal-cartographer | Sonnet | Decree corpus on lex.uz / cbd.minjust.gov.kg | [`pipeline/01-legal-cartographer.md`](pipeline/01-legal-cartographer.md) |
| 1 | case-tournament | Sonnet | 100 global B2G AI cases, tournament-bracketed | [`pipeline/02-case-tournament.md`](pipeline/02-case-tournament.md) |
| 2 | institution-mapper | Sonnet | 8-tier institution taxonomy | [`pipeline/03-institution-mapper.md`](pipeline/03-institution-mapper.md) |
| 2 | donor-pipeline | Sonnet | Donor programmes with named TTL/PM | [`pipeline/04-donor-pipeline.md`](pipeline/04-donor-pipeline.md) |
| 2 | procurement-harvester | Sonnet | Live + forthcoming tenders | [`pipeline/05-procurement-harvester.md`](pipeline/05-procurement-harvester.md) |
| 2 | trend-triangulator | Sonnet | Sector trends + convergent windows | [`pipeline/06-trend-triangulator.md`](pipeline/06-trend-triangulator.md) |
| 3 | people-intelligence | Sonnet + paid Sonar Pro | Decision-makers + diaspora bridges | [`pipeline/07-people-intelligence.md`](pipeline/07-people-intelligence.md) |
| 4 | initiative-synthesizer | Opus xhigh | 100 B2G initiatives, 5-axis scoring | [`pipeline/08-initiative-synthesizer.md`](pipeline/08-initiative-synthesizer.md) |
| 4b | solopreneur-mvp-synthesizer | Opus | 200 solopreneur MVPs (HubSpot $1M MVR framework) | [`pipeline/09-solopreneur-mvp-synthesizer.md`](pipeline/09-solopreneur-mvp-synthesizer.md) |
| 5 | reflexion-auditor | Opus xhigh + paid Sonar | Adversarial re-verification, ≥ 3 HIGH issues | [`pipeline/10-reflexion-auditor.md`](pipeline/10-reflexion-auditor.md) |
| 6 | pitch-artificer | Sonnet | Tier-A / Tier-B outreach bundles | [`pipeline/11-pitch-artificer.md`](pipeline/11-pitch-artificer.md) |

## Auditor AI Team (post-publication, 16 specialists)

After every release, sixteen specialists audit the live site in parallel.
Each specialist has a single mandate, scores its dimension 1–10, and
produces P0 / P1 / P2 patches. See
[`../.claude/audit-team/README.md`](../.claude/audit-team/README.md) for the
full table.

| # | Specialist | Concern |
|---|---|---|
| 01 | Reference Benchmarker | Score audit site vs the padel reference |
| 02 | Information Architect | Nav, hierarchy, breadcrumbs, internal-link graph |
| 03 | Content Voice Editor | Plain English, anti-jargon, FK grade ≤ 10 |
| 04 | Citation / Provenance | Numeric-claim traceability, RU/UZ/KY share |
| 05 | GEO / AIO / AEO / LLMO | llms.txt, JSON-LD, FAQPage, AI-crawler robots |
| 06 | Visual / Typography | Type scale, contrast, whitespace |
| 07 | Mobile-First QA | 320–1440 px, ≥ 44 px tap, no horizontal scroll |
| 08 | Accessibility (WCAG 2.2 AA) | Skip-link, focus-visible, lang attribution |
| 09 | Performance Engineer | Core Web Vitals, Lighthouse ≥ 97 |
| 10 | HTML Code Quality | Semantic HTML5, W3C-valid, landmarks |
| 11 | CSS Architect | Custom props, fluid clamp(), dark mode, print |
| 12 | Data Visualization | Charts justify text, sortable tables |
| 13 | Trust & Brand | Author surface, license, methodology openness |
| 14 | Conversion / CTA | One primary action per page, persona routing |
| 15 | Internationalization | Cyrillic lang attribution, hreflang |
| 16 | Dev-Ex / Reproducibility | README, mermaid arch, CI badges, citation |

## Routing strategy

How the pipeline decides which model to use for which task — Anthropic
Claude (Opus, Sonnet) for reasoning + authoring, OpenRouter (Perplexity
Sonar Deep Research, Sonar Pro, o4-mini-deep-research) for cross-model
verification, free OpenRouter (Owl Alpha 1M, Gemma 4-31b) for volume —
all under a hard USD 20 paid-OpenRouter cap.

See [`routing/openrouter-strategy.md`](routing/openrouter-strategy.md) and
[`routing/hubspot-mvr-encoding.md`](routing/hubspot-mvr-encoding.md).

## Quality gates that block deploy

Twelve content gates, ported from `padel-market-analysis` and extended for
B2G:

1. Single `<h1>` per page
2. No internal-ID leak (`(?:VM|CH|RL|FM|DG|SEG|INI|DEC|PER|INST|PROG|TND|TRD|CASE)-\d{1,5}`) outside `<code>` / frontmatter
3. No run-ID leak (`\d{8}T\d{6}Z`)
4. Decree-fabrication: every cited decree slug resolves to a `state/decrees/*.json` entry (WARN-level: slug-format mismatches)
5. LinkedIn-fabrication: every `linkedin.com/in/...` URL must HEAD-200 + match a Person record
6. Required meta: `<title>` ≤ 60c, description, canonical, OG, Twitter Card, robots
7. JSON-LD valid + `Organization + WebSite + BreadcrumbList + page-type`
8. 40–60 word citable summary lead in first `<p>` after `<h1>`
9. No hidden FAQ (no `display:none` / `hidden` on FAQ blocks)
10. `dateModified` ≤ 90 days
11. Country claim: every `country: UZ|KG` page cites ≥ 1 source from RU/UZ/KY priority domain list
12. No personal contact details (regex sweep for `+998\d{9}`, `+996\d{9}`, personal-domain emails)

Source: [`scripts/check_quality.py`](../scripts/check_quality.py).

## How to fork the prompts and run your own

```bash
# 1. Fork on GitHub
git clone https://github.com/<your-name>/ca-b2g-research.git
cd ca-b2g-research

# 2. Configure your OpenRouter key (paid budget capped at $20 inside the
#    osint_fanout.py wrapper)
cp .env.example .env
$EDITOR .env

# 3. Install deps and run setup
pip install -e .
make setup

# 4. Run the full 12-agent pipeline (~10h wall-clock)
make run

# 5. Render all output surfaces (Obsidian vault + HTML site + CRM CSVs)
make render

# 6. Run the 16-specialist audit team (~30 min wall-clock)
make audit
```

The pipeline targets Uzbekistan + Kyrgyzstan B2G. To re-target a different
country pair, edit two files:

- `prompts/pipeline/00-blueprint-architect.md` — change the **Inputs** + **Source priority** sections
- `docs/lenses.md` — replace the country-specific lenses

Everything else generalises. The schema, scoring rubric, and audit team
are country-agnostic.
