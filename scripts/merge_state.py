#!/usr/bin/env python3
"""
Merge per-agent JSON outputs into the unified knowledge graph at state/knowledge_graph.json.

This is read by the initiative-synthesizer (Wave 4) and pitch-artificer (Wave 6),
plus the rendering pipeline.

Usage:
    python3 scripts/merge_state.py
    python3 scripts/merge_state.py --apply-corrections
"""
import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Source files → knowledge_graph keys
MERGE_MAP = {
    "decrees": [
        "state/decrees/uz_decrees.json",
        "state/decrees/kg_decrees.json",
    ],
    "institutions": [
        "state/institutions/uz_institutions.json",
        "state/institutions/kg_institutions.json",
    ],
    "people": [
        "state/people/uz_people.json",
        "state/people/kg_people.json",
        "state/people/diaspora_bridge.json",
    ],
    "donor_programs": [
        "state/donors/programs.json",
    ],
    "tenders": [
        "state/tenders/uz_tenders.json",
        "state/tenders/kg_tenders.json",
    ],
    "trends": [
        "state/trends/uz_trends.json",
        "state/trends/kg_trends.json",
    ],
    "global_cases": [
        "state/cases/cases.json",
    ],
    "initiatives": [
        "state/initiatives/initiatives.json",
    ],
    "solopreneur_mvps": [
        "state/solopreneur_mvps/uz_mvps.json",
        "state/solopreneur_mvps/kg_mvps.json",
    ],
}


def load_json_array(path: Path):
    if not path.exists():
        return []
    try:
        with path.open() as f:
            data = json.load(f)
        if not isinstance(data, list):
            print(f"⚠️  {path.relative_to(ROOT)}: not a list, skipping")
            return []
        return data
    except json.JSONDecodeError as e:
        print(f"⚠️  {path.relative_to(ROOT)}: invalid JSON: {e}, skipping")
        return []


def deduplicate_by_id(records):
    seen = {}
    for r in records:
        rid = r.get("id")
        if not rid:
            # Records without IDs pass through unchanged
            seen[id(r)] = r
        else:
            # Last write wins (audit corrections override originals)
            seen[rid] = r
    return list(seen.values())


def apply_corrections(graph, corrections_path: Path):
    if not corrections_path.exists():
        print("ℹ️  No corrections file found at state/audit/corrections.json — skipping")
        return graph

    try:
        with corrections_path.open() as f:
            corrections = json.load(f)
    except json.JSONDecodeError as e:
        print(f"⚠️  Could not parse corrections.json: {e}")
        return graph

    applied = 0
    for record_type, changes in corrections.items():
        if record_type not in graph:
            continue
        existing_by_id = {r.get("id"): r for r in graph[record_type] if r.get("id")}
        for change in changes:
            rid = change.get("id")
            if not rid:
                continue
            if rid in existing_by_id:
                existing_by_id[rid].update(change)
                applied += 1
        graph[record_type] = list(existing_by_id.values()) + [r for r in graph[record_type] if not r.get("id")]

    # Tier updates from audit
    tier_updates_path = ROOT / "state/audit/initiative_tier_updates.json"
    if tier_updates_path.exists():
        try:
            with tier_updates_path.open() as f:
                tier_updates = json.load(f)
            init_by_id = {r.get("id"): r for r in graph.get("initiatives", []) if r.get("id")}
            for ini_id, new_tier in tier_updates.items():
                if ini_id in init_by_id:
                    init_by_id[ini_id]["confidence_tier"] = new_tier
                    applied += 1
        except json.JSONDecodeError:
            pass

    print(f"✅ Applied {applied} correction(s)")
    return graph


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply-corrections", action="store_true",
                        help="Apply state/audit/corrections.json after merge")
    args = parser.parse_args()

    print("═" * 60)
    print("Merging state into knowledge_graph.json")
    print("═" * 60)

    # Load weights
    weights_path = ROOT / "state/weights.json"
    weights = {}
    if weights_path.exists():
        with weights_path.open() as f:
            weights = json.load(f)

    graph = {
        "metadata": {
            "schema_version": "1.0.0",
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "weights": weights,
        }
    }

    for graph_key, source_paths in MERGE_MAP.items():
        merged = []
        for rel_path in source_paths:
            full_path = ROOT / rel_path
            records = load_json_array(full_path)
            merged.extend(records)
            print(f"  + {rel_path}: {len(records)} record(s)")
        deduped = deduplicate_by_id(merged)
        graph[graph_key] = deduped
        if len(deduped) != len(merged):
            print(f"    (deduplicated {len(merged) - len(deduped)} duplicate(s) for {graph_key})")

    if args.apply_corrections:
        corrections_path = ROOT / "state/audit/corrections.json"
        graph = apply_corrections(graph, corrections_path)

    out_path = ROOT / "state/knowledge_graph.json"
    with out_path.open("w") as f:
        json.dump(graph, f, indent=2, ensure_ascii=False)

    print()
    print("═" * 60)
    print("Knowledge graph summary:")
    for key in MERGE_MAP:
        print(f"  • {key}: {len(graph.get(key, []))}")
    print("═" * 60)
    print(f"✅ Wrote {out_path.relative_to(ROOT)}")


if __name__ == "__main__":
    sys.exit(main() or 0)
