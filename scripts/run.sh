#!/usr/bin/env bash
set -euo pipefail

# Run a single subagent
# Usage: bash scripts/run.sh <agent-name>

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

AGENT="${1:-}"

if [[ -z "$AGENT" ]]; then
    echo "Usage: bash scripts/run.sh <agent-name>"
    echo ""
    echo "Available agents:"
    ls -1 .claude/agents/*.md | xargs -n1 basename | sed 's/\.md$//' | sed 's/^/  - /'
    exit 1
fi

AGENT_SPEC=".claude/agents/${AGENT}.md"
if [[ ! -f "$AGENT_SPEC" ]]; then
    echo "❌ Agent spec not found: $AGENT_SPEC"
    exit 1
fi

echo "═══════════════════════════════════════════════════════════"
echo "Running agent: $AGENT"
echo "Spec: $AGENT_SPEC"
echo "Started: $(date -Iseconds)"
echo "═══════════════════════════════════════════════════════════"

# Use Claude Code with the agent spec as the task
# The agent spec is read by Claude as the system prompt for this run
TASK_PROMPT="You are running as the '${AGENT}' subagent. Read your full specification at .claude/agents/${AGENT}.md and execute it. Read all referenced input files. Produce all required output files. Adhere to all MUST and MUST NOT constraints. When complete, write the COMPLETE marker file specified in the spec."

# Execute via Claude Code CLI in non-interactive mode
# Adjust model based on agent requirements
case "$AGENT" in
    "blueprint-architect"|"initiative-synthesizer"|"reflexion-auditor")
        MODEL_FLAG="--model opus"
        ;;
    *)
        MODEL_FLAG="--model sonnet"
        ;;
esac

# Run the agent
claude \
    --print \
    --dangerously-skip-permissions \
    $MODEL_FLAG \
    "$TASK_PROMPT" \
    2>&1 | tee "state/audit/${AGENT}_$(date +%Y%m%d_%H%M%S).log"

# Verify completion marker
COMPLETE_MARKER=""
case "$AGENT" in
    "blueprint-architect") COMPLETE_MARKER="state/blueprint/COMPLETE" ;;
    "legal-cartographer") COMPLETE_MARKER="state/decrees/COMPLETE" ;;
    "case-tournament") COMPLETE_MARKER="state/cases/COMPLETE" ;;
    "institution-mapper") COMPLETE_MARKER="state/institutions/COMPLETE" ;;
    "donor-pipeline") COMPLETE_MARKER="state/donors/COMPLETE" ;;
    "procurement-harvester") COMPLETE_MARKER="state/tenders/COMPLETE" ;;
    "trend-triangulator") COMPLETE_MARKER="state/trends/COMPLETE" ;;
    "people-intelligence") COMPLETE_MARKER="state/people/COMPLETE" ;;
    "initiative-synthesizer") COMPLETE_MARKER="state/initiatives/COMPLETE" ;;
    "reflexion-auditor") COMPLETE_MARKER="state/audit/COMPLETE" ;;
    "pitch-artificer") COMPLETE_MARKER="outputs/playbook/COMPLETE" ;;
esac

if [[ -n "$COMPLETE_MARKER" && -f "$COMPLETE_MARKER" ]]; then
    echo ""
    echo "✅ Agent $AGENT completed successfully."
    echo "   Marker: $COMPLETE_MARKER"
    echo "   Summary:"
    cat "$COMPLETE_MARKER" | sed 's/^/     /'
else
    echo ""
    echo "⚠️  Agent $AGENT did not write completion marker."
    echo "   Expected: $COMPLETE_MARKER"
    echo "   Check log for issues."
    echo "$(date -Iseconds) - Agent $AGENT did not complete - missing marker $COMPLETE_MARKER" >> state/audit/errors.log
    exit 1
fi

echo "═══════════════════════════════════════════════════════════"
echo "Agent $AGENT finished at $(date -Iseconds)"
echo "═══════════════════════════════════════════════════════════"
