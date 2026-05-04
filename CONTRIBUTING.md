# Contributing to Central Asia B2G Intelligence

Thank you for considering a contribution. This research lives or dies by accuracy. The most valuable contributions are corrections, additions, and verification of the data, not engineering.

## Two ways to help

1. **Research correction** — you spotted wrong data on a decree, person, donor programme, institution, or initiative. Open a [research-correction issue](.github/ISSUE_TEMPLATE/research-correction.md). This is by far the highest-leverage contribution.
2. **Code/infrastructure** — improve a renderer, add a quality gate, refine an agent prompt, fix a bug. Open a PR per the workflow below.

## Research-correction workflow

1. Find the wrong record. Use `/decrees/`, `/people/`, `/donors/`, `/institutions/`, or `/initiatives/` on the live site, or browse `state/*.json` in the repo.
2. Open an issue with the [research-correction template](.github/ISSUE_TEMPLATE/research-correction.md). Provide:
   - Record type and ID (e.g. `decree UZ-PP-2024-403` or `person uz-saidov-sherzod`)
   - Field path (e.g. `head_person_id`, `linkedin_url`, `signatory`)
   - Current value
   - Correct value
   - Source URL — primary government source preferred, with publication date
   - Verification level you can attest to (VERIFIED / L2_VERIFIED / INFERRED)
3. We label, triage, and either patch the JSON directly (small fixes) or queue for the next quarterly refresh (large changes).

## Code-contribution workflow

### Before you touch anything

1. Read `CLAUDE.md` for the architectural boundaries (every agent reads/writes through `state/`, no direct cross-agent access).
2. Read `docs/state_schema.json` — the typed data model is the single source of truth.
3. Read `docs/scoring_rubric.md` if you are touching anything that scores initiatives.

### Local checks before opening a PR

```bash
pip install -e .
python3 scripts/validate_state.py        # JSON schema validation must pass
python3 scripts/check_quality.py         # 12 content quality gates
python3 scripts/verify_links.py          # ≥97% links healthy or annotated
make audit                               # full pre-merge sweep
```

PRs that break `validate_state.py` will not merge.

### Commit messages

Conventional Commits style with the wave or surface as scope:

```
feat(wave3): add Latin transliteration to people records
fix(render-site): table-scroll wrapper for narrow viewports
docs(readme): add reproducing instructions
chore(ci): bump python from 3.11 to 3.12
```

Common scopes: `wave0..wave6`, `wave4b`, `render-site`, `render-obsidian`, `check-quality`, `verify-links`, `state-schema`, `agents`, `ci`, `docs`.

### Adding a new agent

Agents are markdown files at `.claude/agents/<agent-name>.md`. Required frontmatter:

```yaml
---
name: agent-name
description: One-sentence purpose, names the wave it runs in.
tools: Read, Write, WebSearch, WebFetch
model: sonnet  # or opus for synthesis/audit waves
---
```

The body must include: Mode, Inputs, Outputs (with file paths), Coverage requirements, Per-record protocol, MUST and MUST NOT lists, Verification cascade, Definition of Done. Mirror the existing 12 agents.

Add the agent to `scripts/run.sh` (`COMPLETE_MARKER` mapping + model tier), `scripts/run-parallel.sh` (which wave it joins), and `scripts/setup.sh` (`REQUIRED_AGENTS` list).

### Adding a new record type

1. Add the type to `docs/state_schema.json`.
2. Add a merge entry in `scripts/merge_state.py`.
3. Add a render function in `scripts/render_obsidian.py` and `scripts/render_site.py`.
4. Add a quality gate if appropriate (anti-fabrication on IDs).

## Code of Conduct

Be civil. Disagreements about facts are welcome — disagreements about people are not. We follow the [Contributor Covenant 2.1](https://www.contributor-covenant.org/version/2/1/code_of_conduct/).

## License

By contributing you agree your contribution is licensed under Apache 2.0 (the same license as the project). No CLA required.

## Acknowledgments

This research is built on Anthropic's Claude (Opus + Sonnet) and OpenRouter (Perplexity Sonar Deep Research, Sonar Pro, Owl Alpha, Gemma). The methodology is inspired by the Princeton GEO paper and Eric Ries's Lean Startup, distilled through HubSpot's $1M Solopreneur MVR framework for the Wave 4b solopreneur track.

If you find this research valuable, the best way to say thanks is to open a research-correction issue.
