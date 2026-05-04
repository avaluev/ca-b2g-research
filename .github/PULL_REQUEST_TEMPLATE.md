<!-- One-paragraph summary of what this PR does and why. -->

## Type of change

- [ ] Research correction (data fix)
- [ ] New record / new agent
- [ ] Renderer / output improvement
- [ ] Quality gate / verification improvement
- [ ] Documentation
- [ ] Build / CI / dependency
- [ ] Other (describe):

## Pre-merge checklist

- [ ] `python3 scripts/validate_state.py` passes
- [ ] `python3 scripts/check_quality.py` reports zero new errors
- [ ] `python3 scripts/verify_links.py --internal-only` clean
- [ ] If touching the schema, `docs/state_schema.json` updated
- [ ] If touching an agent, the corresponding `.claude/agents/*.md` updated
- [ ] If adding new records, foreign keys resolve to existing records
- [ ] Commit messages follow conventional-commits scope (`feat(wave3):`, etc.)
- [ ] No private contact details added (CLAUDE.md security rule)
- [ ] No fabricated decree numbers or LinkedIn URLs

## Sources for new claims

<!-- Every numeric or named claim must cite a source. List URL + publication date for new entries. -->

## Screenshots / before-after

<!-- If a renderer change, paste screenshots of before and after. -->
