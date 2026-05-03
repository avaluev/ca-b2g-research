#!/usr/bin/env python3
"""
State validator. Schema-checks every JSON file in state/ against docs/state_schema.json.

Usage:
    python3 scripts/validate_state.py

Exit code 0 = clean, 1 = errors found.
"""
import json
import sys
from pathlib import Path
from collections import defaultdict

try:
    from jsonschema import Draft7Validator
except ImportError:
    print("❌ jsonschema not installed. Run: pip3 install --break-system-packages jsonschema")
    sys.exit(1)

ROOT = Path(__file__).resolve().parent.parent
SCHEMA_PATH = ROOT / "docs" / "state_schema.json"

# Map state files to the schema definition each must conform to
STATE_FILE_SCHEMAS = {
    "state/decrees/uz_decrees.json": "Decree",
    "state/decrees/kg_decrees.json": "Decree",
    "state/institutions/uz_institutions.json": "Institution",
    "state/institutions/kg_institutions.json": "Institution",
    "state/people/uz_people.json": "Person",
    "state/people/kg_people.json": "Person",
    "state/people/diaspora_bridge.json": "Person",
    "state/donors/programs.json": "DonorProgram",
    "state/tenders/uz_tenders.json": "Tender",
    "state/tenders/kg_tenders.json": "Tender",
    "state/trends/uz_trends.json": "Trend",
    "state/trends/kg_trends.json": "Trend",
    "state/cases/cases.json": "GlobalCase",
    "state/initiatives/initiatives.json": "Initiative",
}


def load_schema():
    with SCHEMA_PATH.open() as f:
        return json.load(f)


def get_definition_validator(schema, def_name):
    """Build a validator for a single $def from the schema."""
    sub_schema = {
        "$schema": schema.get("$schema"),
        "definitions": schema["definitions"],
        "$ref": f"#/definitions/{def_name}",
    }
    return Draft7Validator(sub_schema)


def validate_file(path: Path, def_name: str, schema):
    errors = []
    if not path.exists():
        return [{"level": "missing", "msg": f"File does not exist: {path.relative_to(ROOT)}"}]

    try:
        with path.open() as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        return [{"level": "json", "msg": f"Invalid JSON: {e}"}]

    if not isinstance(data, list):
        return [{"level": "shape", "msg": "Expected JSON array of records"}]

    validator = get_definition_validator(schema, def_name)
    for i, record in enumerate(data):
        for err in validator.iter_errors(record):
            errors.append({
                "level": "schema",
                "msg": f"Record {i} ({record.get('id', '<no id>')}): {err.message} at {'.'.join(str(p) for p in err.absolute_path)}",
            })
    return errors


def cross_reference_check():
    """Check that ID references across files actually resolve."""
    issues = []

    def load_ids(path):
        if not (ROOT / path).exists():
            return set()
        try:
            with (ROOT / path).open() as f:
                data = json.load(f)
            return {r.get("id") for r in data if r.get("id")}
        except (json.JSONDecodeError, ValueError):
            return set()

    institution_ids = load_ids("state/institutions/uz_institutions.json") | load_ids("state/institutions/kg_institutions.json")
    person_ids = load_ids("state/people/uz_people.json") | load_ids("state/people/kg_people.json") | load_ids("state/people/diaspora_bridge.json")
    decree_ids = load_ids("state/decrees/uz_decrees.json") | load_ids("state/decrees/kg_decrees.json")
    case_ids = load_ids("state/cases/cases.json")
    program_ids = load_ids("state/donors/programs.json")

    # Initiatives must reference real records
    init_path = ROOT / "state/initiatives/initiatives.json"
    if init_path.exists():
        try:
            with init_path.open() as f:
                inits = json.load(f)
            for ini in inits:
                ini_id = ini.get("id", "<unknown>")
                if ini.get("target_buyer_person_id") and ini["target_buyer_person_id"] not in person_ids:
                    issues.append(f"Initiative {ini_id}: target_buyer_person_id '{ini['target_buyer_person_id']}' not in people records")
                if ini.get("operational_counterpart_person_id") and ini["operational_counterpart_person_id"] not in person_ids:
                    issues.append(f"Initiative {ini_id}: operational_counterpart_person_id '{ini['operational_counterpart_person_id']}' not in people records")
                if ini.get("lead_institution_id") and ini["lead_institution_id"] not in institution_ids:
                    issues.append(f"Initiative {ini_id}: lead_institution_id '{ini['lead_institution_id']}' not in institution records")
                if ini.get("precedent_case_id") and ini["precedent_case_id"] not in case_ids:
                    issues.append(f"Initiative {ini_id}: precedent_case_id '{ini['precedent_case_id']}' not in case records")
                for did in ini.get("authorizing_decree_ids", []):
                    if did not in decree_ids:
                        issues.append(f"Initiative {ini_id}: authorizing_decree_id '{did}' not in decree records")
                if ini.get("secondary_funding_donor_program_id") and ini["secondary_funding_donor_program_id"] not in program_ids:
                    issues.append(f"Initiative {ini_id}: secondary_funding_donor_program_id '{ini['secondary_funding_donor_program_id']}' not in donor records")
        except json.JSONDecodeError:
            issues.append("Could not parse initiatives.json for cross-reference check")

    return issues


def main():
    schema = load_schema()
    total_errors = 0
    summary = defaultdict(lambda: {"checked": 0, "errors": 0})

    print("═" * 60)
    print("State Validation")
    print("═" * 60)

    for rel_path, def_name in STATE_FILE_SCHEMAS.items():
        full_path = ROOT / rel_path
        errors = validate_file(full_path, def_name, schema)
        if not full_path.exists():
            print(f"⏭️  {rel_path}: not yet generated (skipping)")
            continue
        record_count = 0
        try:
            with full_path.open() as f:
                record_count = len(json.load(f))
        except (json.JSONDecodeError, ValueError):
            pass
        summary[def_name]["checked"] += record_count
        if errors:
            summary[def_name]["errors"] += len(errors)
            total_errors += len(errors)
            print(f"❌ {rel_path}: {len(errors)} error(s) across {record_count} record(s)")
            for err in errors[:10]:
                print(f"      [{err['level']}] {err['msg']}")
            if len(errors) > 10:
                print(f"      ... and {len(errors) - 10} more")
        else:
            print(f"✅ {rel_path}: {record_count} record(s) valid")

    print()
    print("Cross-reference integrity check:")
    xref_issues = cross_reference_check()
    if xref_issues:
        print(f"❌ {len(xref_issues)} cross-reference issue(s):")
        for issue in xref_issues[:20]:
            print(f"      {issue}")
        if len(xref_issues) > 20:
            print(f"      ... and {len(xref_issues) - 20} more")
        total_errors += len(xref_issues)
    else:
        print("✅ All cross-references resolve")

    print()
    print("═" * 60)
    print("Summary by record type:")
    for def_name, counts in sorted(summary.items()):
        status = "✅" if counts["errors"] == 0 else "❌"
        print(f"  {status} {def_name}: {counts['checked']} checked, {counts['errors']} errors")
    print("═" * 60)

    if total_errors == 0:
        print(f"✅ All clean.")
        return 0
    else:
        print(f"❌ {total_errors} total issue(s) found.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
