#!/usr/bin/env bash
set -euo pipefail

# Run the full 7-wave research pipeline end-to-end
# Usage: bash scripts/run-all.sh

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

START_TIME=$(date +%s)
START_ISO=$(date -Iseconds)

echo "╔═══════════════════════════════════════════════════════════╗"
echo "║  Central Asia B2G Research Harness — Full Pipeline Run   ║"
echo "╠═══════════════════════════════════════════════════════════╣"
echo "║  Start: $START_ISO              ║"
echo "║  Estimated wall-clock: ~10 hours                          ║"
echo "║  Estimated API cost: ~\$70-120                             ║"
echo "╚═══════════════════════════════════════════════════════════╝"
echo ""

# Pre-flight: ensure setup has run
if [[ ! -f "state/weights.json" ]] || [[ ! -f "state/knowledge_graph.json" ]]; then
    echo "Running setup first..."
    bash scripts/setup.sh
    echo ""
fi

# Wave 0: Blueprint (sequential, must succeed before anything else)
echo "▶▶▶  WAVE 0: Blueprint Architect (Opus xhigh)"
bash scripts/run-parallel.sh wave-0

# Wave 1: Legal + Cases (parallel, both depend only on blueprint)
echo ""
echo "▶▶▶  WAVE 1: Legal Cartographer + Case Tournament (parallel)"
bash scripts/run-parallel.sh wave-1

# Wave 2: Institutions + Donors + Tenders + Trends (parallel, depend on wave-1)
echo ""
echo "▶▶▶  WAVE 2: Institution Mapper + Donor Pipeline + Procurement Harvester + Trend Triangulator (parallel)"
bash scripts/run-parallel.sh wave-2

# Wave 3: People (sequential, depends on institutions)
echo ""
echo "▶▶▶  WAVE 3: People Intelligence (sequential)"
bash scripts/run-parallel.sh wave-3

# Wave 4: Synthesis (sequential, Opus xhigh, depends on everything)
echo ""
echo "▶▶▶  WAVE 4: Initiative Synthesizer (Opus xhigh)"
bash scripts/run-parallel.sh wave-4

# Wave 5: Audit (sequential, Opus xhigh, max-compute verification)
echo ""
echo "▶▶▶  WAVE 5: Reflexion Auditor (Opus xhigh)"
bash scripts/run-parallel.sh wave-5

# Wave 6: Pitch artifacts (sequential, depends on audit)
echo ""
echo "▶▶▶  WAVE 6: Pitch Artificer"
bash scripts/run-parallel.sh wave-6

# Final rendering: produce CRM, memo, and playbook deliverables
echo ""
echo "▶▶▶  RENDERING DELIVERABLES"
python3 scripts/render.py crm
python3 scripts/render.py memo
python3 scripts/render.py playbook

END_TIME=$(date +%s)
END_ISO=$(date -Iseconds)
DURATION_SEC=$((END_TIME - START_TIME))
DURATION_HM=$(printf '%dh %dm' $((DURATION_SEC / 3600)) $(((DURATION_SEC % 3600) / 60)))

echo ""
echo "╔═══════════════════════════════════════════════════════════╗"
echo "║  PIPELINE COMPLETE                                        ║"
echo "╠═══════════════════════════════════════════════════════════╣"
echo "║  Started:  $START_ISO              ║"
echo "║  Finished: $END_ISO              ║"
echo "║  Duration: $DURATION_HM                                  ║"
echo "╚═══════════════════════════════════════════════════════════╝"
echo ""
echo "Deliverables:"
echo "  • CRM:      outputs/crm/"
echo "  • Memo:     outputs/memo/"
echo "  • Playbook: outputs/playbook/"
echo ""
echo "Audit findings: state/audit/audit_report.md"
echo "Honesty notes: state/audit/honesty_section.md"
echo ""
echo "If errors were logged, see: state/audit/errors.log"
