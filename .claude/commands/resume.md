---
description: Resume pipeline from the next incomplete wave
---

You are resuming the Central Asia B2G research pipeline.

1. Read CLAUDE.md to refresh on the harness structure.

2. Check which COMPLETE markers exist (state/*/COMPLETE and outputs/playbook/COMPLETE).

3. Determine the next wave to run:
   - If state/blueprint/COMPLETE missing → run wave-0
   - Else if state/decrees/COMPLETE OR state/cases/COMPLETE missing → run wave-1
   - Else if any of state/institutions/, state/donors/, state/tenders/, state/trends/ COMPLETE missing → run wave-2
   - Else if state/people/COMPLETE missing → run wave-3
   - Else if state/initiatives/COMPLETE missing → run wave-4
   - Else if state/audit/COMPLETE missing → run wave-5
   - Else if outputs/playbook/COMPLETE missing → run wave-6
   - Else → render deliverables (`python3 scripts/render.py all`)

4. Tell the user which wave you're going to run and the command to execute it. DO NOT execute the wave yourself unless the user confirms.

Be concise.
