#!/usr/bin/env python3
"""
Render deliverables from the unified knowledge graph.

Three modes:
    crm      → outputs/crm/        sortable CSVs + master pipeline
    memo     → outputs/memo/       Big 4-style strategic memo (markdown)
    playbook → outputs/playbook/   per-initiative artifact bundles

Usage:
    python3 scripts/render.py crm
    python3 scripts/render.py memo
    python3 scripts/render.py playbook
    python3 scripts/render.py all
"""
import argparse
import csv
import json
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GRAPH_PATH = ROOT / "state/knowledge_graph.json"
OUTPUTS = ROOT / "outputs"


def load_graph():
    if not GRAPH_PATH.exists():
        print(f"❌ Knowledge graph not found at {GRAPH_PATH.relative_to(ROOT)}")
        print("   Run: python3 scripts/merge_state.py")
        sys.exit(1)
    with GRAPH_PATH.open() as f:
        return json.load(f)


def index_by_id(records):
    return {r.get("id"): r for r in records if r.get("id")}


# ─── CRM RENDER ────────────────────────────────────────────────────

def render_crm(graph):
    """Render CRM views: sortable CSVs by each scoring axis + master."""
    crm_dir = OUTPUTS / "crm"
    crm_dir.mkdir(parents=True, exist_ok=True)

    inits = graph.get("initiatives", [])
    people = index_by_id(graph.get("people", []))
    institutions = index_by_id(graph.get("institutions", []))
    cases = index_by_id(graph.get("global_cases", []))
    decrees = index_by_id(graph.get("decrees", []))
    programs = index_by_id(graph.get("donor_programs", []))

    if not inits:
        print("⏭️  No initiatives to render")
        return

    # Build flat rows
    rows = []
    for ini in inits:
        scoring = ini.get("scoring", {})
        target = people.get(ini.get("target_buyer_person_id"), {})
        op = people.get(ini.get("operational_counterpart_person_id"), {})
        institution = institutions.get(ini.get("lead_institution_id"), {})
        precedent = cases.get(ini.get("precedent_case_id"), {})
        decree = next((decrees.get(d) for d in ini.get("authorizing_decree_ids", []) if d in decrees), {}) or {}
        program = programs.get(ini.get("secondary_funding_donor_program_id"), {})

        rows.append({
            "id": ini.get("id"),
            "short_name": ini.get("short_name"),
            "country": ini.get("country"),
            "sector": ini.get("sector"),
            "confidence_tier": ini.get("confidence_tier"),
            "weighted_total": scoring.get("weighted_total"),
            "speed_to_contract": scoring.get("speed_to_contract"),
            "strategic_moat": scoring.get("strategic_moat"),
            "defensibility": scoring.get("defensibility"),
            "capital_access": scoring.get("capital_access"),
            "russian_cis_fit": scoring.get("russian_cis_fit"),
            "target_person_id": ini.get("target_buyer_person_id"),
            "target_person_name": target.get("full_name_latin", ""),
            "target_person_role": target.get("current_role", ""),
            "target_person_linkedin": target.get("linkedin_url", ""),
            "target_person_priority_tier": target.get("priority_tier", ""),
            "operational_counterpart_id": ini.get("operational_counterpart_person_id"),
            "operational_counterpart_name": op.get("full_name_latin", ""),
            "lead_institution_id": ini.get("lead_institution_id"),
            "lead_institution": institution.get("name_en", ""),
            "decree_id": decree.get("id", ""),
            "decree_number": decree.get("number", ""),
            "decree_title_en": decree.get("title_en", ""),
            "donor_program_id": ini.get("secondary_funding_donor_program_id"),
            "donor": program.get("donor", ""),
            "donor_program_name": program.get("program_name", ""),
            "ttl_pm_name": program.get("ttl_pm_name", ""),
            "precedent_case_id": ini.get("precedent_case_id"),
            "precedent_case": precedent.get("case_name", ""),
            "precedent_country": precedent.get("country_origin", ""),
            "procurement_pathway": ini.get("procurement_pathway"),
            "estimated_initial_contract_usd": ini.get("estimated_initial_contract_usd"),
            "estimated_3yr_revenue_usd": ini.get("estimated_3yr_revenue_usd"),
            "pitch_hook": ini.get("pitch_hook", ""),
            "next_30_day_actions": " | ".join(ini.get("next_30_day_actions", [])),
            "verification": ini.get("verification"),
        })

    fieldnames = list(rows[0].keys()) if rows else []

    def write_csv(filename, sorted_rows):
        path = crm_dir / filename
        with path.open("w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(sorted_rows)
        print(f"  ✅ {path.relative_to(ROOT)}: {len(sorted_rows)} rows")

    # Master sorted by weighted total
    write_csv("master.csv", sorted(rows, key=lambda r: -(r["weighted_total"] or 0)))

    # Per-axis slices
    write_csv("top_speed.csv", sorted(rows, key=lambda r: -(r["speed_to_contract"] or 0)))
    write_csv("top_moat.csv", sorted(rows, key=lambda r: -(r["strategic_moat"] or 0)))
    write_csv("top_defensibility.csv", sorted(rows, key=lambda r: -(r["defensibility"] or 0)))
    write_csv("top_capital.csv", sorted(rows, key=lambda r: -(r["capital_access"] or 0)))
    write_csv("top_russian_cis.csv", sorted(rows, key=lambda r: -(r["russian_cis_fit"] or 0)))

    # Convergent windows: ≥7 on at least 4 axes
    def convergent(r):
        axes = ["speed_to_contract", "strategic_moat", "defensibility", "capital_access", "russian_cis_fit"]
        high = sum(1 for a in axes if (r.get(a) or 0) >= 7)
        return high >= 4
    convergent_rows = [r for r in rows if convergent(r)]
    write_csv("convergent_windows.csv", sorted(convergent_rows, key=lambda r: -(r["weighted_total"] or 0)))

    # By country
    write_csv("uz_only.csv", sorted([r for r in rows if r["country"] in ("UZ", "BOTH")], key=lambda r: -(r["weighted_total"] or 0)))
    write_csv("kg_only.csv", sorted([r for r in rows if r["country"] in ("KG", "BOTH")], key=lambda r: -(r["weighted_total"] or 0)))

    # Tier A only (the deal-ready set)
    tier_a = [r for r in rows if r["confidence_tier"] == "A"]
    write_csv("tier_a_only.csv", sorted(tier_a, key=lambda r: -(r["weighted_total"] or 0)))

    # People master (CRM contact list)
    people_rows = []
    for p in graph.get("people", []):
        people_rows.append({
            "id": p.get("id"),
            "full_name_latin": p.get("full_name_latin"),
            "full_name_ru": p.get("full_name_ru"),
            "country": p.get("country"),
            "current_role": p.get("current_role"),
            "current_institution_id": p.get("current_institution_id"),
            "linkedin_url": p.get("linkedin_url"),
            "linkedin_status": p.get("linkedin_status"),
            "telegram_handle": p.get("telegram_handle"),
            "email_pattern_guess": p.get("email_pattern_guess"),
            "priority_tier": p.get("priority_tier"),
            "diaspora_advisor_flag": p.get("diaspora_advisor_flag"),
            "diaspora_location": p.get("diaspora_location"),
            "pitch_hook": p.get("pitch_hook"),
            "last_verified_date": p.get("last_verified_date"),
        })
    if people_rows:
        path = crm_dir / "people_master.csv"
        with path.open("w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=list(people_rows[0].keys()))
            writer.writeheader()
            writer.writerows(people_rows)
        print(f"  ✅ {path.relative_to(ROOT)}: {len(people_rows)} rows")


# ─── MEMO RENDER ───────────────────────────────────────────────────

def render_memo(graph):
    """Render Big 4-style strategic memo as markdown."""
    memo_dir = OUTPUTS / "memo"
    memo_dir.mkdir(parents=True, exist_ok=True)

    inits = graph.get("initiatives", [])
    people = index_by_id(graph.get("people", []))
    institutions = index_by_id(graph.get("institutions", []))
    decrees = index_by_id(graph.get("decrees", []))
    cases = index_by_id(graph.get("global_cases", []))
    programs = index_by_id(graph.get("donor_programs", []))
    trends = graph.get("trends", [])

    out = memo_dir / "strategic_memo.md"

    sections = []
    sections.append(f"# Central Asia B2G AI Pipeline — Strategic Memo\n")
    sections.append(f"_Generated: {datetime.now(timezone.utc).isoformat()}_\n")
    sections.append(f"_Knowledge graph version: {graph.get('metadata', {}).get('schema_version', 'unknown')}_\n")

    # Executive summary
    tier_a = [i for i in inits if i.get("confidence_tier") == "A"]
    tier_b = [i for i in inits if i.get("confidence_tier") == "B"]
    uz_inits = [i for i in inits if i.get("country") in ("UZ", "BOTH")]
    kg_inits = [i for i in inits if i.get("country") in ("KG", "BOTH")]

    sections.append("## Executive Summary\n")
    sections.append(f"This memo synthesizes a B2G pipeline of **{len(inits)} initiatives** across Uzbekistan and Kyrgyzstan, derived from primary research on **{len(decrees)} decrees**, **{len(institutions)} government institutions**, **{len(people)} named decision-makers**, **{len(programs)} donor programs**, and **{len(cases)} global precedent cases**.\n")
    sections.append(f"- **Tier A (deal-ready)**: {len(tier_a)} initiatives")
    sections.append(f"- **Tier B (develop)**: {len(tier_b)} initiatives")
    sections.append(f"- **Uzbekistan focus**: {len(uz_inits)} initiatives")
    sections.append(f"- **Kyrgyzstan focus**: {len(kg_inits)} initiatives\n")

    # Top 10 overall
    sections.append("## Top 10 Initiatives (by weighted score)\n")
    sections.append("| # | Tier | Country | Sector | Initiative | Weighted Total | Buyer |")
    sections.append("|---|------|---------|--------|------------|----------------|-------|")
    top10 = sorted(inits, key=lambda i: -i.get("scoring", {}).get("weighted_total", 0))[:10]
    for i, ini in enumerate(top10, 1):
        target_id = ini.get("target_buyer_person_id", "")
        target = people.get(target_id, {})
        wt = ini.get("scoring", {}).get("weighted_total", 0)
        sections.append(f"| {i} | {ini.get('confidence_tier','?')} | {ini.get('country','?')} | {ini.get('sector','?')} | {ini.get('short_name','?')} | {wt:.2f} | {target.get('full_name_latin','?')} ({target.get('current_role','?')}) |")
    sections.append("")

    # Sector deep-dives
    sections.append("## Sector Deep-Dives\n")
    by_sector = defaultdict(list)
    for ini in inits:
        by_sector[ini.get("sector", "Unknown")].append(ini)
    for sector in sorted(by_sector.keys()):
        sections.append(f"### {sector}")
        sector_inits = sorted(by_sector[sector], key=lambda i: -i.get("scoring", {}).get("weighted_total", 0))
        sections.append(f"_{len(sector_inits)} initiative(s) in this sector._\n")
        for ini in sector_inits[:5]:
            target = people.get(ini.get("target_buyer_person_id"), {})
            wt = ini.get("scoring", {}).get("weighted_total", 0)
            sections.append(f"- **[{ini.get('confidence_tier','?')}] {ini.get('short_name','?')}** ({ini.get('country','?')}) — {ini.get('one_liner','')} — Target: {target.get('full_name_latin','?')} — Score: {wt:.2f}")
        if len(sector_inits) > 5:
            sections.append(f"  _... and {len(sector_inits) - 5} more (see CRM)_")
        sections.append("")

    # Decision-maker map (top 30 priority tier 1)
    sections.append("## Decision-Maker Map\n")
    tier1_people = sorted(
        [p for p in graph.get("people", []) if p.get("priority_tier") == 1],
        key=lambda p: (p.get("country", ""), p.get("full_name_latin", ""))
    )
    sections.append(f"_{len(tier1_people)} Tier-1 decision-makers identified._\n")
    by_country = defaultdict(list)
    for p in tier1_people:
        by_country[p.get("country", "?")].append(p)
    for country in sorted(by_country.keys()):
        sections.append(f"### {country}")
        for p in by_country[country][:25]:
            ll = p.get("linkedin_url", "")
            li_segment = f" • [LinkedIn]({ll})" if ll else ""
            diaspora = " • _Diaspora advisor_" if p.get("diaspora_advisor_flag") else ""
            sections.append(f"- **{p.get('full_name_latin','?')}** — {p.get('current_role','?')}{li_segment}{diaspora}")
            if p.get("pitch_hook"):
                sections.append(f"  - _Hook_: {p['pitch_hook']}")
        sections.append("")

    # Donor pipeline
    sections.append("## Donor Pipeline\n")
    by_donor = defaultdict(list)
    for prog in graph.get("donor_programs", []):
        by_donor[prog.get("donor", "Unknown")].append(prog)
    for donor in sorted(by_donor.keys()):
        active_count = sum(1 for p in by_donor[donor] if p.get("status") == "active")
        pipeline_count = sum(1 for p in by_donor[donor] if p.get("status") in ("pipeline", "appraisal"))
        total_budget = sum(p.get("total_budget_usd") or 0 for p in by_donor[donor])
        sections.append(f"### {donor}")
        sections.append(f"- {len(by_donor[donor])} programs ({active_count} active, {pipeline_count} pipeline)")
        sections.append(f"- Total committed: ~${total_budget:,.0f}")
        for p in sorted(by_donor[donor], key=lambda x: -(x.get("total_budget_usd") or 0))[:5]:
            sections.append(f"  - **{p.get('program_name','?')}** ({p.get('country','?')}) — ${p.get('total_budget_usd') or 0:,.0f} — TTL/PM: {p.get('ttl_pm_name','—')}")
        sections.append("")

    # Convergent windows
    sections.append("## Convergent Windows (Strategic Prizes)\n")
    sections.append("_Initiatives scoring ≥7 on at least 4 of 5 axes — multi-lens alignment._\n")
    def convergent(ini):
        s = ini.get("scoring", {})
        axes = ["speed_to_contract", "strategic_moat", "defensibility", "capital_access", "russian_cis_fit"]
        return sum(1 for a in axes if (s.get(a) or 0) >= 7) >= 4
    convergents = sorted([i for i in inits if convergent(i)], key=lambda i: -i.get("scoring", {}).get("weighted_total", 0))
    for ini in convergents[:15]:
        target = people.get(ini.get("target_buyer_person_id"), {})
        wt = ini.get("scoring", {}).get("weighted_total", 0)
        sections.append(f"### {ini.get('short_name','?')} ({ini.get('country','?')} • {ini.get('sector','?')})")
        sections.append(f"- _One-liner_: {ini.get('one_liner','')}")
        sections.append(f"- _Target_: {target.get('full_name_latin','?')} ({target.get('current_role','?')})")
        sections.append(f"- _Score_: {wt:.2f} (Tier {ini.get('confidence_tier','?')})")
        sections.append(f"- _Pitch hook_: {ini.get('pitch_hook','')}")
        sections.append("")

    # Honesty section
    honesty_path = ROOT / "state/audit/honesty_section.md"
    if honesty_path.exists():
        sections.append("## Research Honesty: What This Did NOT Find\n")
        with honesty_path.open() as f:
            sections.append(f.read())

    out.write_text("\n".join(sections), encoding="utf-8")
    print(f"  ✅ {out.relative_to(ROOT)}: {len(sections)} sections")


# ─── PLAYBOOK RENDER ───────────────────────────────────────────────

def render_playbook(graph):
    """Render the operational playbook (per-initiative cards)."""
    playbook_dir = OUTPUTS / "playbook"
    playbook_dir.mkdir(parents=True, exist_ok=True)

    inits = graph.get("initiatives", [])
    people = index_by_id(graph.get("people", []))
    institutions = index_by_id(graph.get("institutions", []))
    decrees = index_by_id(graph.get("decrees", []))
    cases = index_by_id(graph.get("global_cases", []))
    programs = index_by_id(graph.get("donor_programs", []))

    # Tier A and top 20 Tier B get full bundles
    tier_a = sorted([i for i in inits if i.get("confidence_tier") == "A"],
                    key=lambda i: -i.get("scoring", {}).get("weighted_total", 0))
    tier_b_top = sorted([i for i in inits if i.get("confidence_tier") == "B"],
                        key=lambda i: -i.get("scoring", {}).get("weighted_total", 0))[:20]

    def render_card(ini, tier_dir):
        ini_id = ini.get("id", "unknown")
        card_dir = tier_dir / ini_id
        card_dir.mkdir(parents=True, exist_ok=True)

        target = people.get(ini.get("target_buyer_person_id"), {})
        op = people.get(ini.get("operational_counterpart_person_id"), {})
        institution = institutions.get(ini.get("lead_institution_id"), {})
        precedent = cases.get(ini.get("precedent_case_id"), {})
        decree_list = [decrees.get(d) for d in ini.get("authorizing_decree_ids", []) if d in decrees]
        program = programs.get(ini.get("secondary_funding_donor_program_id"), {})

        # one_pager.md
        op_text = []
        op_text.append(f"# {ini.get('short_name','?')}")
        op_text.append(f"_{ini.get('country','?')} • {ini.get('sector','?')} • Tier {ini.get('confidence_tier','?')}_\n")
        op_text.append(f"## Target")
        op_text.append(f"**{target.get('full_name_latin','?')}** — {target.get('current_role','?')}")
        if target.get('linkedin_url'):
            op_text.append(f"LinkedIn: {target['linkedin_url']}")
        op_text.append(f"\nInstitution: {institution.get('name_en','?')} ({institution.get('name_ru','')})\n")
        op_text.append(f"## Problem\n{ini.get('problem_statement','')}\n")
        op_text.append(f"## Solution\n{ini.get('solution_concept','')}\n")
        op_text.append(f"## Why now\n")
        for d in decree_list[:3]:
            op_text.append(f"- Decree {d.get('number','?')} ({d.get('date','?')}): {d.get('title_en','')}")
            op_text.append(f"  - Half-life status: {d.get('half_life_status','?')}")
            op_text.append(f"  - Implementation deadline: {d.get('implementation_deadline','?')}")
        if program:
            op_text.append(f"- Donor: **{program.get('donor','?')}** — {program.get('program_name','?')}")
            op_text.append(f"  - TTL/PM: {program.get('ttl_pm_name','?')} • Status: {program.get('status','?')}")
        op_text.append(f"\n## Precedent\n**{precedent.get('case_name','?')}** ({precedent.get('country_origin','?')})")
        op_text.append(f"- {precedent.get('problem_solved','')}")
        op_text.append(f"- Outcome: {precedent.get('outcome_metrics','')}")
        op_text.append(f"- Adapt: {ini.get('what_adapted','')}\n")
        op_text.append(f"## Pitch hook\n> {ini.get('pitch_hook','')}\n")
        op_text.append(f"## Ask\n- Pilot scope: {ini.get('pilot_scope','')}")
        op_text.append(f"- Duration: {ini.get('pilot_duration_months','?')} months")
        op_text.append(f"- Initial contract value: ${ini.get('estimated_initial_contract_usd') or 0:,.0f}")
        op_text.append(f"- 3-year revenue potential: ${ini.get('estimated_3yr_revenue_usd') or 0:,.0f}\n")
        op_text.append(f"## Scoring")
        s = ini.get("scoring", {})
        op_text.append(f"| Axis | Score |")
        op_text.append(f"|---|---|")
        op_text.append(f"| Speed-to-contract | {s.get('speed_to_contract','?')}/10 |")
        op_text.append(f"| Strategic moat | {s.get('strategic_moat','?')}/10 |")
        op_text.append(f"| Defensibility | {s.get('defensibility','?')}/10 |")
        op_text.append(f"| Capital access | {s.get('capital_access','?')}/10 |")
        op_text.append(f"| Russian/CIS fit | {s.get('russian_cis_fit','?')}/10 |")
        op_text.append(f"| **Weighted total** | **{s.get('weighted_total','?')}** |\n")
        op_text.append(f"## Next 30-day actions")
        for a in ini.get("next_30_day_actions", []):
            op_text.append(f"- {a}")
        (card_dir / "one_pager.md").write_text("\n".join(op_text), encoding="utf-8")

        # outreach (template stubs — pitch-artificer may overwrite with full variants)
        outreach = []
        outreach.append(f"# Cold Outreach Kit — {ini.get('short_name','?')}")
        outreach.append(f"_Target: {target.get('full_name_latin','?')} ({target.get('current_role','?')})_\n")
        outreach.append(f"## Pitch hook\n{ini.get('pitch_hook','')}\n")
        outreach.append(f"## Suggested anchors\n")
        if decree_list:
            outreach.append(f"- **Decree-anchor**: reference {decree_list[0].get('number','?')} ({decree_list[0].get('title_en','')})")
        if precedent:
            outreach.append(f"- **Precedent-anchor**: reference {precedent.get('case_name','?')} ({precedent.get('country_origin','?')})")
        if program:
            outreach.append(f"- **Donor-anchor**: reference {program.get('donor','?')} {program.get('program_name','?')} (TTL/PM: {program.get('ttl_pm_name','?')})")
        outreach.append(f"\n_Note: pitch-artificer fills full RU/EN/UZ/KY variants in Wave 6._")
        (card_dir / "outreach_kit.md").write_text("\n".join(outreach), encoding="utf-8")

        # risks
        risks = ["# Risk Register", ""]
        for r in ini.get("risk_register", []):
            risks.append(f"## {r.get('risk_type','?')}")
            risks.append(f"- _Description_: {r.get('description','')}")
            risks.append(f"- _Mitigation_: {r.get('mitigation','')}\n")
        (card_dir / "risks.md").write_text("\n".join(risks), encoding="utf-8")

    print("  Rendering Tier A bundles...")
    tier_a_dir = playbook_dir / "tier_a"
    for ini in tier_a:
        render_card(ini, tier_a_dir)
    print(f"  ✅ {len(tier_a)} Tier A bundles in {tier_a_dir.relative_to(ROOT)}")

    print("  Rendering Tier B bundles...")
    tier_b_dir = playbook_dir / "tier_b"
    for ini in tier_b_top:
        render_card(ini, tier_b_dir)
    print(f"  ✅ {len(tier_b_top)} Tier B bundles in {tier_b_dir.relative_to(ROOT)}")

    # pipeline_master.csv (with status fields for CRM)
    pm_path = playbook_dir / "pipeline_master.csv"
    fieldnames = [
        "initiative_id", "short_name", "country", "sector",
        "target_person_name", "target_person_linkedin",
        "priority_tier", "weighted_total",
        "speed_to_contract", "strategic_moat", "defensibility", "capital_access", "russian_cis_fit",
        "lead_institution", "primary_funding_pathway",
        "estimated_initial_contract_usd", "estimated_3yr_revenue_usd",
        "status", "last_action", "next_action", "owner",
    ]
    with pm_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for ini in tier_a + tier_b_top:
            target = people.get(ini.get("target_buyer_person_id"), {})
            inst = institutions.get(ini.get("lead_institution_id"), {})
            s = ini.get("scoring", {})
            actions = ini.get("next_30_day_actions") or []
            writer.writerow({
                "initiative_id": ini.get("id"),
                "short_name": ini.get("short_name"),
                "country": ini.get("country"),
                "sector": ini.get("sector"),
                "target_person_name": target.get("full_name_latin", ""),
                "target_person_linkedin": target.get("linkedin_url", ""),
                "priority_tier": ini.get("confidence_tier"),
                "weighted_total": s.get("weighted_total"),
                "speed_to_contract": s.get("speed_to_contract"),
                "strategic_moat": s.get("strategic_moat"),
                "defensibility": s.get("defensibility"),
                "capital_access": s.get("capital_access"),
                "russian_cis_fit": s.get("russian_cis_fit"),
                "lead_institution": inst.get("name_en", ""),
                "primary_funding_pathway": ini.get("primary_funding", ""),
                "estimated_initial_contract_usd": ini.get("estimated_initial_contract_usd"),
                "estimated_3yr_revenue_usd": ini.get("estimated_3yr_revenue_usd"),
                "status": "not_started",
                "last_action": "",
                "next_action": actions[0] if actions else "",
                "owner": "",
            })
    print(f"  ✅ {pm_path.relative_to(ROOT)}: {len(tier_a) + len(tier_b_top)} rows")

    # week1_action_list.md
    wk1 = ["# Week 1 Action List", "_Top 20 outreach moves to send Monday morning._\n"]
    week1 = sorted(
        [i for i in tier_a if i.get("scoring", {}).get("speed_to_contract", 0) >= 7],
        key=lambda i: (-i.get("scoring", {}).get("speed_to_contract", 0),
                       -i.get("scoring", {}).get("russian_cis_fit", 0))
    )[:20]
    for n, ini in enumerate(week1, 1):
        target = people.get(ini.get("target_buyer_person_id"), {})
        decree_obj = None
        for d in ini.get("authorizing_decree_ids", []):
            if d in decrees:
                decree_obj = decrees[d]
                break
        anchor = "decree" if decree_obj else ("donor" if ini.get("secondary_funding_donor_program_id") else "precedent")
        wk1.append(f"## {n}. {target.get('full_name_latin','?')} — {ini.get('short_name','?')}")
        wk1.append(f"- _Country_: {ini.get('country','?')} • _Sector_: {ini.get('sector','?')}")
        wk1.append(f"- _LinkedIn_: {target.get('linkedin_url','—')}")
        wk1.append(f"- _Recommended anchor_: **{anchor}**")
        wk1.append(f"- _Recommended language_: Russian (default for senior officials)")
        wk1.append(f"- _Subject line_: see card outreach_kit.md")
        wk1.append(f"- _Hook_: {ini.get('pitch_hook','')}")
        wk1.append(f"- _Speed-to-contract_: {ini.get('scoring',{}).get('speed_to_contract','?')}/10")
        wk1.append("")
    (playbook_dir / "week1_action_list.md").write_text("\n".join(wk1), encoding="utf-8")
    print(f"  ✅ outputs/playbook/week1_action_list.md")


# ─── ENTRY POINT ──────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=["crm", "memo", "playbook", "all"])
    args = parser.parse_args()

    graph = load_graph()

    print("═" * 60)
    print(f"Render mode: {args.mode}")
    print("═" * 60)

    if args.mode in ("crm", "all"):
        print("\n📊 Rendering CRM...")
        render_crm(graph)
    if args.mode in ("memo", "all"):
        print("\n📄 Rendering memo...")
        render_memo(graph)
    if args.mode in ("playbook", "all"):
        print("\n📚 Rendering playbook...")
        render_playbook(graph)

    print("\n" + "═" * 60)
    print("✅ Render complete")
    print("═" * 60)


if __name__ == "__main__":
    sys.exit(main() or 0)
