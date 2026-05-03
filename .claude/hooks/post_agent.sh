#!/usr/bin/env bash
# Post-agent hook: runs validation after every subagent completes
# This file is referenced by .claude/settings.json (or invoked manually)

set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$ROOT"

echo "[hook] post-agent validation"
python3 scripts/validate_state.py || {
    echo "[hook] ⚠️ validation flagged issues — logged to state/audit/errors.log"
    echo "$(date -Iseconds) - post-agent validation flagged issues" >> state/audit/errors.log
}
