# QUICKSTART

## What you have

A deployable Claude Code research harness that produces an AI-first B2G pipeline for Uzbekistan and Kyrgyzstan.

**Inputs**: nothing. The harness self-bootstraps from public sources.
**Outputs**: 100+ initiatives × named decision-makers × decree anchors × donor pathways × global precedents, rendered as CRM + memo + playbook.
**Time**: ~10 hours wall-clock for a full run.
**Cost**: ~$70-120 in Anthropic API consumption.

## 5-minute setup

```bash
# Extract
tar -xzf ca-b2g-research.tar.gz
cd ca-b2g-research

# Bootstrap
bash scripts/setup.sh
```

`setup.sh` verifies Claude Code CLI, Python 3.10+, installs jsonschema/pandas, and initializes state directories.

## First run

You have two paths:

### Path A: one-shot full pipeline
```bash
bash scripts/run-all.sh
```
Runs all 7 waves sequentially, with parallel fan-out within each wave.
Logs stream to `state/audit/`. Final deliverables in `outputs/`.

### Path B: wave-by-wave (recommended for first run)
```bash
bash scripts/run-parallel.sh wave-0   # blueprint (sequential, ~30 min)
bash scripts/run-parallel.sh wave-1   # legal + cases (parallel, ~2 hr)
bash scripts/run-parallel.sh wave-2   # institutions + donors + tenders + trends (~3 hr)
bash scripts/run-parallel.sh wave-3   # people intelligence (~2 hr)
bash scripts/run-parallel.sh wave-4   # initiative synthesis (Opus xhigh, ~1 hr)
bash scripts/run-parallel.sh wave-5   # reflexion audit (Opus xhigh, ~45 min)
bash scripts/run-parallel.sh wave-6   # pitch artificer (~1 hr)
```

After each wave: validation runs automatically. If any agent fails, errors land in `state/audit/errors.log`.

## Status check at any point

```bash
python3 scripts/audit.py            # current pipeline status + tier distribution
python3 scripts/validate_state.py   # schema + cross-reference integrity
```

## Render deliverables

Render scripts read `state/knowledge_graph.json` (built automatically in waves 4 and 6):

```bash
python3 scripts/render.py crm        # outputs/crm/*.csv
python3 scripts/render.py memo       # outputs/memo/strategic_memo.md
python3 scripts/render.py playbook   # outputs/playbook/{tier_a,tier_b}/*/
python3 scripts/render.py all        # all three
```

## Three deliverables you'll get

### 1. `outputs/crm/`
Sortable CSVs for direct CRM import (Salesforce, HubSpot, Notion, Airtable):
- `master.csv` — all initiatives, sorted by weighted score
- `top_speed.csv`, `top_moat.csv`, `top_defensibility.csv`, `top_capital.csv`, `top_russian_cis.csv` — single-axis sorted slices
- `convergent_windows.csv` — initiatives scoring ≥7 on at least 4 of 5 axes (the strategic prizes)
- `tier_a_only.csv` — deal-ready set
- `uz_only.csv`, `kg_only.csv` — country-segmented
- `people_master.csv` — full contact list with LinkedIn URLs

### 2. `outputs/memo/strategic_memo.md`
Big-4-style strategic memo: executive summary, sector deep-dives, decision-maker map, donor pipeline, convergent windows, and an honesty section documenting what the research did *not* find.

Render to PDF if needed: `pandoc outputs/memo/strategic_memo.md -o memo.pdf`

### 3. `outputs/playbook/`
Per-initiative artifact bundles:
- `pipeline_master.csv` — top initiatives with status/owner fields ready for tracking
- `week1_action_list.md` — top 20 messages to send Monday morning
- `tier_a/INI-XXX/one_pager.md` — PDF-ready brief
- `tier_a/INI-XXX/outreach_kit.md` — cold outreach with decree/precedent/donor anchors
- `tier_a/INI-XXX/risks.md` — risk register

## Monthly refresh

The harness is built for monthly updates as decrees, tenders, and personnel rotate:

```bash
# Re-run only the perishable agents
bash scripts/run.sh procurement-harvester  # ~30 min
bash scripts/run.sh people-intelligence    # ~2 hr (Tier-1 verification only)
bash scripts/run.sh donor-pipeline         # ~1 hr (status changes only)
bash scripts/run.sh reflexion-auditor      # ~45 min (audit the diff)
python3 scripts/merge_state.py --apply-corrections
python3 scripts/render.py all
```

## Stabilization workflow

When an agent produces an error:
1. The error is logged to `state/audit/errors.log`
2. Edit the agent spec at `.claude/agents/<agent>.md` to add a new MUST/MUST NOT
3. (Optional) Add a verification test to `scripts/validate_state.py`
4. Re-run that agent: `bash scripts/run.sh <agent-name>`

The harness improves through use. Every error becomes a constraint.

## Architecture at a glance

```
┌──────────────────────────────────────────────────────────────────┐
│  WAVE 0  blueprint-architect (Opus xhigh, sequential)             │
│  ─────────────────────────────────────────────────                │
│  WAVE 1  legal-cartographer  ▶◀  case-tournament (parallel)       │
│  ─────────────────────────────────────────────────                │
│  WAVE 2  institution-mapper ▶◀ donor-pipeline ▶◀                  │
│          procurement-harvester ▶◀ trend-triangulator (parallel)   │
│  ─────────────────────────────────────────────────                │
│  WAVE 3  people-intelligence (sequential, depends on Wave 2)      │
│  ─────────────────────────────────────────────────                │
│  WAVE 4  initiative-synthesizer (Opus xhigh, sequential)          │
│  ─────────────────────────────────────────────────                │
│  WAVE 5  reflexion-auditor (Opus xhigh, max-compute audit)        │
│  ─────────────────────────────────────────────────                │
│  WAVE 6  pitch-artificer (sequential, renders artifacts)          │
└──────────────────────────────────────────────────────────────────┘
```

**Reasoning sandwich**: Opus xhigh on the bookends (planning + verification), Sonnet on the data-gathering middle.

## Read the policy gateway

`CLAUDE.md` is the harness's policy gateway — every constraint, MUST, and verification rule lives there. Read it once before running, especially if customizing.

`docs/lenses.md` documents the 5 analytical lenses (Karimov-to-Mirziyoyev Inversion, Japarov Concentration, Decree Half-Life, Donor Co-Financing, Diaspora Bridge, plus Russian/CIS Substitution). Every output is shaped by these.

`docs/scoring_rubric.md` documents the 5-axis weighted scoring. Adjust weights in `state/weights.json` to reprioritize.

`docs/state_schema.json` is the canonical data model. Every agent reads/writes records conforming to it.

## When to suspect bad data

Tier A initiatives with `verification: VERIFIED` and recent `last_verified_date` (≤30 days) should be deal-ready. If you get one and the LinkedIn doesn't match, the role has rotated since the harness ran or the people-intelligence agent matched the wrong profile. Check Tier B first if you don't recognize a name in Tier A — name disambiguation is the most error-prone task in the pipeline.

## Quick troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| Agent doesn't write COMPLETE marker | Hit token budget or web search rate limit | Check `state/audit/<agent>_*.log`, re-run agent |
| validate_state.py reports schema errors | Agent produced malformed JSON | Re-run that single agent: `bash scripts/run.sh <agent>` |
| Cross-reference integrity errors | Person/decree/case ID typo | Look at validator output, edit source JSON, re-run merge |
| Render shows empty CSVs | Knowledge graph not yet merged | Run `python3 scripts/merge_state.py` |
| Tier-A count too low | Audit was too strict OR research was too thin | Check audit_report.md, decide whether to relax thresholds or extend research |

You're set. Start with `bash scripts/setup.sh`.
