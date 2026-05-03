# CLAUDE.md — Central Asia B2G Research Harness

## Purpose
Parallel multi-agent deep-research system. Produces a normalized knowledge graph of AI/digital B2G opportunities in Uzbekistan and Kyrgyzstan, then renders three deliverable surfaces (CRM, strategic memo, operating playbook).

## Tooling (mandatory commands)
- `bash scripts/setup.sh` — bootstrap dependencies and verify state directory
- `bash scripts/run.sh <agent-name>` — invoke a single subagent
- `bash scripts/run-parallel.sh <wave>` — fan out a wave of subagents in parallel
- `python3 scripts/validate_state.py` — schema-validate every JSON in `state/`
- `python3 scripts/render.py crm|memo|playbook` — render a deliverable from the knowledge graph
- `python3 scripts/audit.py` — run the reflexion verification pass

## Wave structure (execution order)
- **Wave 0**: blueprint-architect (sequential, must complete first)
- **Wave 1**: legal-cartographer, case-tournament (parallel, independent)
- **Wave 2**: institution-mapper, donor-pipeline, procurement-harvester, trend-triangulator (parallel, depend on Wave 1)
- **Wave 3**: people-intelligence (depends on institution-mapper)
- **Wave 4**: initiative-synthesizer (sequential, depends on all prior)
- **Wave 5**: reflexion-auditor (sequential, max-compute verification)
- **Wave 6**: pitch-artificer (sequential, renders artifacts)

Run `bash scripts/run-parallel.sh wave-N` to launch each wave.

## Architectural Boundaries
- All agent outputs MUST write to `state/<agent>/output.json` per `docs/state_schema.json`
- Agents MUST NOT read from each other's directories directly — use `state/knowledge_graph.json` (the merged read view)
- Agents MUST NOT write to `outputs/` — only `scripts/render.py` writes there
- Source verification tags are non-optional: every claim is `[VERIFIED]`, `[L2_VERIFIED]`, `[INFERRED]`, or `[UNVERIFIED]`

## Verification (Definition of Done)
- `python3 scripts/validate_state.py` passes with zero errors
- `python3 scripts/audit.py` returns < 5% unverified claims in tier-1 records
- Every `person` record has `linkedin_url` populated OR explicit `linkedin_status: "not_found"` with alternative contact
- Every `decree` record has been verified on the official source (lex.uz / cbd.minjust.gov.kg)
- Every `donor_program` record has at minimum: TTL/PM name, government counterpart name, current status

## Security / MUST NOT
- MUST NOT include personal contact details (private mobile, home address, personal email) for any named individual
- MUST NOT speculate about personal political loyalties — only documented public positions admissible
- MUST NOT fabricate decree numbers, budget figures, or LinkedIn URLs — explicit "not found" beats fabrication
- MUST NOT use English-only sources — every country claim must be cross-referenced against at least one Russian-language source minimum, ideally also Uzbek or Kyrgyz native source

## Source Priority (per country)
**Uzbekistan**: lex.uz, gov.uz, president.uz, norma.uz, spot.uz, gazeta.uz, kun.uz, daryo.uz, podrobno.uz, repost.uz
**Kyrgyzstan**: president.kg, gov.kg, kabmin.kg, cbd.minjust.gov.kg, 24.kg, kaktus.media, akipress.org, azattyk.org, economist.kg
**Donors**: documents.worldbank.org, projects.worldbank.org, adb.org/projects, ec.europa.eu/international-partnerships, undp.org

## Canonical Documentation
- `docs/state_schema.json` — JSON schema all agents conform to
- `docs/scoring_rubric.md` — 5-axis scoring with weights
- `docs/lenses.md` — the 5 non-obvious analytical lenses applied to every initiative
- `docs/agents/<agent-name>.md` — per-agent specification

## Stabilization Cycle
When an agent produces an error:
1. Log to `state/audit/errors.log`
2. Add a new MUST/MUST NOT to the relevant agent spec under `.claude/agents/`
3. Add a verification test to `scripts/validate_state.py`
4. Re-run the agent

The harness improves through use. Every error becomes a constraint.
