#!/usr/bin/env python3
"""
Quick audit summary script. Reads state/audit/audit_report.md and
state/initiatives/initiatives.json to produce a one-glance status.

Usage:
    python3 scripts/audit.py
"""
import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main():
    print("═" * 60)
    print("Audit Summary")
    print("═" * 60)

    # Initiative tier distribution
    init_path = ROOT / "state/initiatives/initiatives.json"
    if init_path.exists():
        with init_path.open() as f:
            inits = json.load(f)
        tier_counts = Counter(i.get("confidence_tier", "?") for i in inits)
        verification_counts = Counter(i.get("verification", "?") for i in inits)
        country_counts = Counter(i.get("country", "?") for i in inits)
        sector_counts = Counter(i.get("sector", "?") for i in inits)

        print(f"\nInitiatives total: {len(inits)}")
        print(f"\n  By confidence tier:")
        for t in ("A", "B", "C", "D", "?"):
            if tier_counts.get(t):
                print(f"    Tier {t}: {tier_counts[t]}")

        print(f"\n  By verification:")
        for v, c in sorted(verification_counts.items(), key=lambda x: -x[1]):
            print(f"    {v}: {c}")

        print(f"\n  By country:")
        for c, n in sorted(country_counts.items()):
            print(f"    {c}: {n}")

        print(f"\n  By sector (top 12):")
        for s, n in sorted(sector_counts.items(), key=lambda x: -x[1])[:12]:
            print(f"    {s}: {n}")

        # Top 10 by weighted total
        print(f"\n  Top 10 by weighted_total:")
        scored = sorted(inits, key=lambda i: i.get("scoring", {}).get("weighted_total", 0), reverse=True)[:10]
        for i, ini in enumerate(scored, 1):
            wt = ini.get("scoring", {}).get("weighted_total", 0)
            tier = ini.get("confidence_tier", "?")
            country = ini.get("country", "?")
            sector = ini.get("sector", "?")
            short = ini.get("short_name", ini.get("id", "?"))
            print(f"    {i:2d}. [{tier}] [{country}] [{sector}] {short} — {wt:.2f}")
    else:
        print("⏭️  No initiatives.json yet — run wave 4 first")

    # Audit report
    print()
    audit_path = ROOT / "state/audit/audit_report.md"
    if audit_path.exists():
        print(f"📄 Audit report: state/audit/audit_report.md")
        # Print first ~30 lines as a glimpse
        with audit_path.open() as f:
            head = "".join(f.readlines()[:30])
        print()
        print(head)
        print("    ... (truncated, see full report)")
    else:
        print("⏭️  No audit_report.md yet — run wave 5 first")

    # Honesty section
    honesty_path = ROOT / "state/audit/honesty_section.md"
    if honesty_path.exists():
        print()
        print(f"📄 Honesty section: state/audit/honesty_section.md")
        with honesty_path.open() as f:
            head = "".join(f.readlines()[:20])
        print()
        print(head)

    # Errors log
    errors_path = ROOT / "state/audit/errors.log"
    if errors_path.exists() and errors_path.stat().st_size > 0:
        print()
        print(f"⚠️  Errors logged in state/audit/errors.log:")
        with errors_path.open() as f:
            print(f.read()[-2000:])

    print()
    print("═" * 60)


if __name__ == "__main__":
    sys.exit(main() or 0)
