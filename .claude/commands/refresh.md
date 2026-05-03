---
description: Monthly refresh — re-run perishable agents (procurement, people verification, donor status)
---

You are running a monthly refresh of the Central Asia B2G research harness. The full pipeline has already run; now we update only the data that changes month-to-month.

Refresh sequence:

1. Re-run procurement-harvester (live RFPs change weekly):
   `bash scripts/run.sh procurement-harvester`

2. Re-run people-intelligence with focus on Tier-1 individuals (roles change quarterly):
   `bash scripts/run.sh people-intelligence`

3. Re-run donor-pipeline focusing on status changes (TTL/PM rotations, new approvals):
   `bash scripts/run.sh donor-pipeline`

4. Re-run reflexion-auditor to audit the changes:
   `bash scripts/run.sh reflexion-auditor`

5. Re-merge state with corrections:
   `python3 scripts/merge_state.py --apply-corrections`

6. Re-render deliverables:
   `python3 scripts/render.py all`

7. Generate a "what changed" diff report by comparing today's outputs/ to the previous archive (if user has git versioning).

Tell the user which steps will run and the estimated time/cost. Wait for confirmation before executing.
