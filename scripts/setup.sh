#!/usr/bin/env bash
set -euo pipefail

# Setup script for Central Asia B2G Research Harness
# Idempotent: safe to re-run

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

echo "═══════════════════════════════════════════════════════════"
echo "Central Asia B2G Research Harness — Setup"
echo "═══════════════════════════════════════════════════════════"

# 1. Verify Claude Code installed
if ! command -v claude &> /dev/null; then
    echo "❌ Claude Code CLI not found."
    echo "   Install: https://docs.claude.com/en/docs/claude-code/quickstart"
    exit 1
fi
echo "✅ Claude Code CLI found: $(claude --version 2>&1 | head -1)"

# 2. Verify Python 3.10+
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 not found."
    exit 1
fi
PYTHON_VERSION=$(python3 -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')
echo "✅ Python found: $PYTHON_VERSION"

# 3. Install Python dependencies
echo "📦 Installing Python dependencies..."
pip3 install --break-system-packages --quiet jsonschema pyyaml pandas openpyxl 2>&1 | tail -5 || true
echo "✅ Python dependencies ready"

# 4. Verify directory structure
REQUIRED_DIRS=(
    ".claude/agents"
    ".claude/commands"
    ".claude/hooks"
    "scripts"
    "state/blueprint"
    "state/decrees"
    "state/institutions"
    "state/people"
    "state/donors"
    "state/tenders"
    "state/trends"
    "state/cases"
    "state/initiatives"
    "state/solopreneur_mvps"
    "state/external"
    "state/audit"
    "outputs/crm"
    "outputs/memo"
    "outputs/playbook"
    "outputs/obsidian"
    "outputs/site"
    "docs"
    "prompts"
)
for dir in "${REQUIRED_DIRS[@]}"; do
    mkdir -p "$dir"
done
echo "✅ Directory structure verified"

# 5. Verify required documentation files
REQUIRED_DOCS=(
    "CLAUDE.md"
    "README.md"
    "docs/state_schema.json"
    "docs/lenses.md"
    "docs/scoring_rubric.md"
)
for doc in "${REQUIRED_DOCS[@]}"; do
    if [[ ! -f "$doc" ]]; then
        echo "❌ Missing required file: $doc"
        exit 1
    fi
done
echo "✅ Documentation files verified"

# 6. Verify all subagent specs
REQUIRED_AGENTS=(
    "blueprint-architect"
    "legal-cartographer"
    "case-tournament"
    "institution-mapper"
    "donor-pipeline"
    "procurement-harvester"
    "trend-triangulator"
    "people-intelligence"
    "initiative-synthesizer"
    "solopreneur-mvp-synthesizer"
    "reflexion-auditor"
    "pitch-artificer"
)
for agent in "${REQUIRED_AGENTS[@]}"; do
    if [[ ! -f ".claude/agents/${agent}.md" ]]; then
        echo "❌ Missing agent spec: .claude/agents/${agent}.md"
        exit 1
    fi
done
echo "✅ All ${#REQUIRED_AGENTS[@]} subagent specs present"

# 7. Initialize default weights file
if [[ ! -f "state/weights.json" ]]; then
    cat > state/weights.json <<'EOF'
{
  "speed_to_contract": 0.25,
  "strategic_moat": 0.20,
  "defensibility": 0.20,
  "capital_access": 0.20,
  "russian_cis_fit": 0.15
}
EOF
    echo "✅ Default scoring weights written to state/weights.json"
fi

# 8. Initialize empty knowledge graph state if first run
if [[ ! -f "state/knowledge_graph.json" ]]; then
    cat > state/knowledge_graph.json <<'EOF'
{
  "metadata": {
    "schema_version": "1.0.0",
    "generated_at": null,
    "weights": null
  },
  "decrees": [],
  "institutions": [],
  "people": [],
  "donor_programs": [],
  "tenders": [],
  "trends": [],
  "global_cases": [],
  "initiatives": []
}
EOF
    echo "✅ Empty knowledge graph initialized"
fi

# 9. Initialize error log
touch state/audit/errors.log

echo ""
echo "═══════════════════════════════════════════════════════════"
echo "Setup complete. Next steps:"
echo "═══════════════════════════════════════════════════════════"
echo ""
echo "  1. Run blueprint wave (sequential):"
echo "     bash scripts/run.sh blueprint-architect"
echo ""
echo "  2. Run Wave 1 (parallel):"
echo "     bash scripts/run-parallel.sh wave-1"
echo ""
echo "  3. Or run everything:"
echo "     bash scripts/run-all.sh"
echo ""
echo "  4. Validate state at any point:"
echo "     python3 scripts/validate_state.py"
echo ""
echo "  5. Render deliverables after Wave 6:"
echo "     python3 scripts/render.py crm"
echo "     python3 scripts/render.py memo"
echo "     python3 scripts/render.py playbook"
echo ""
