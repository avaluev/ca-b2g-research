#!/usr/bin/env bash
set -euo pipefail

# Run a wave of subagents in parallel
# Usage: bash scripts/run-parallel.sh <wave>
# Waves: wave-1, wave-2, wave-3, wave-4, wave-5, wave-6

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

WAVE="${1:-}"

if [[ -z "$WAVE" ]]; then
    echo "Usage: bash scripts/run-parallel.sh <wave>"
    echo ""
    echo "Available waves:"
    echo "  wave-1: legal-cartographer + case-tournament (parallel)"
    echo "  wave-2: institution-mapper + donor-pipeline + procurement-harvester + trend-triangulator (parallel)"
    echo "  wave-3: people-intelligence (sequential, depends on wave-2)"
    echo "  wave-4: initiative-synthesizer (sequential, depends on all prior)"
    echo "  wave-5: reflexion-auditor (sequential, max-compute audit)"
    echo "  wave-6: pitch-artificer (sequential, renders playbook)"
    exit 1
fi

declare -a AGENTS

case "$WAVE" in
    "wave-0")
        AGENTS=("blueprint-architect")
        ;;
    "wave-1")
        AGENTS=("legal-cartographer" "case-tournament")
        ;;
    "wave-2")
        AGENTS=("institution-mapper" "donor-pipeline" "procurement-harvester" "trend-triangulator")
        ;;
    "wave-3")
        AGENTS=("people-intelligence")
        ;;
    "wave-4")
        # Merge all upstream state into the unified knowledge graph before synthesis
        echo "🔄 Merging upstream state for wave-4..."
        python3 scripts/merge_state.py
        AGENTS=("initiative-synthesizer")
        ;;
    "wave-4b")
        # Solopreneur MVP synthesis — runs after Wave 4, before Wave 5 audit
        echo "🔄 Re-merging state for wave-4b (solopreneur MVPs)..."
        python3 scripts/merge_state.py
        AGENTS=("solopreneur-mvp-synthesizer")
        ;;
    "wave-5")
        AGENTS=("reflexion-auditor")
        ;;
    "wave-6")
        # Re-merge with audit corrections applied before rendering pitches
        echo "🔄 Re-merging state with audit corrections for wave-6..."
        python3 scripts/merge_state.py --apply-corrections
        AGENTS=("pitch-artificer")
        ;;
    *)
        echo "❌ Unknown wave: $WAVE"
        exit 1
        ;;
esac

echo "═══════════════════════════════════════════════════════════"
echo "Running $WAVE in parallel"
echo "Agents: ${AGENTS[*]}"
echo "Started: $(date -Iseconds)"
echo "═══════════════════════════════════════════════════════════"

# Track PIDs for parallel execution
declare -a PIDS=()
declare -a AGENT_NAMES=()

# Fan out
for agent in "${AGENTS[@]}"; do
    echo "  → Launching: $agent"
    bash scripts/run.sh "$agent" > "state/audit/${WAVE}_${agent}.out" 2>&1 &
    PIDS+=($!)
    AGENT_NAMES+=("$agent")
done

# Wait for all and collect exit codes
echo ""
echo "Waiting for ${#PIDS[@]} agent(s) to complete..."
echo "(Output streamed to state/audit/${WAVE}_*.out)"
echo ""

FAILED=0
for i in "${!PIDS[@]}"; do
    pid="${PIDS[$i]}"
    name="${AGENT_NAMES[$i]}"
    if wait "$pid"; then
        echo "  ✅ $name completed"
    else
        echo "  ❌ $name FAILED — see state/audit/${WAVE}_${name}.out"
        echo "$(date -Iseconds) - $WAVE/$name failed with exit code $?" >> state/audit/errors.log
        FAILED=$((FAILED + 1))
    fi
done

echo ""
echo "═══════════════════════════════════════════════════════════"
echo "$WAVE finished at $(date -Iseconds)"
if [[ $FAILED -gt 0 ]]; then
    echo "⚠️  $FAILED agent(s) failed. Inspect state/audit/${WAVE}_*.out and state/audit/errors.log"
    echo "═══════════════════════════════════════════════════════════"
    exit 1
fi
echo "✅ All ${#AGENTS[@]} agent(s) completed successfully."

# Validate state after each wave
echo ""
echo "🔍 Validating state..."
if python3 scripts/validate_state.py; then
    echo "✅ State validation passed"
else
    echo "⚠️  State validation flagged issues — see output above"
fi

echo "═══════════════════════════════════════════════════════════"
