---
description: Show pipeline status — which waves complete, what's pending
---

You are running a status check on the Central Asia B2G research harness.

Read the following files and report:

1. List which COMPLETE marker files exist in:
   - state/blueprint/COMPLETE
   - state/decrees/COMPLETE
   - state/cases/COMPLETE
   - state/institutions/COMPLETE
   - state/donors/COMPLETE
   - state/tenders/COMPLETE
   - state/trends/COMPLETE
   - state/people/COMPLETE
   - state/initiatives/COMPLETE
   - state/audit/COMPLETE
   - outputs/playbook/COMPLETE

2. For each COMPLETE marker found, print its contents (the agent's summary).

3. Run `python3 scripts/audit.py` and print the summary.

4. List the next wave to run based on what's complete:
   - If blueprint missing → "Run wave-0"
   - If wave-1 markers missing → "Run wave-1"
   - etc.

Report concisely. No bullet points unless listing the markers themselves.
