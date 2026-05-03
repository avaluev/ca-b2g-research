#!/usr/bin/env python3
"""
render_obsidian — emit an Obsidian-compatible vault from the knowledge graph.

Vault structure:
    outputs/obsidian/
    ├── README.md                  (vault entry point with Dataview index)
    ├── 00 Methodology.md
    ├── 01 Lenses.md
    ├── 02 Scoring.md
    ├── Decrees/<slug>.md
    ├── Institutions/<slug>.md
    ├── People/<slug>.md
    ├── Donors/<slug>.md
    ├── Tenders/<slug>.md
    ├── Trends/<slug>.md
    ├── Cases/<slug>.md
    ├── Initiatives/<slug>.md
    └── Briefs/{Strategic Memo, Week 1 Action List, Top 100 Initiatives}.md

Frontmatter conforms to Obsidian Properties + Dataview. Wikilinks use
folder-prefixed lowercase-kebab-case slugs to survive case-sensitive FS.

Usage:
    python3 scripts/render_obsidian.py
"""

from __future__ import annotations

import json
import re
import shutil
from datetime import date
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
GRAPH_PATH = ROOT / "state" / "knowledge_graph.json"
VAULT = ROOT / "outputs" / "obsidian"
DOCS = ROOT / "docs"

PRIVATE_SUBFOLDERS = (
    "Briefs/Outreach Kits/_personal",
    "Briefs/Diaspora Bridge/_discreet",
)


def slugify(s: str) -> str:
    s = s or ""
    s = s.lower().strip()
    s = re.sub(r"[^\w\s\-/]", "", s, flags=re.UNICODE)
    s = re.sub(r"[\s_]+", "-", s)
    s = re.sub(r"-+", "-", s)
    return s.strip("-")


def yaml_value(v: Any) -> str:
    if v is None:
        return "null"
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, (int, float)):
        return str(v)
    if isinstance(v, list):
        if not v:
            return "[]"
        return "[" + ", ".join(yaml_value(x) for x in v) + "]"
    s = str(v).replace("\\", "\\\\").replace('"', '\\"')
    return f'"{s}"'


def frontmatter(d: dict[str, Any]) -> str:
    lines = ["---"]
    for k, v in d.items():
        if isinstance(v, list) and v and isinstance(v[0], str):
            lines.append(f"{k}:")
            for item in v:
                lines.append(f"  - {yaml_value(item)}")
        else:
            lines.append(f"{k}: {yaml_value(v)}")
    lines.append("---\n")
    return "\n".join(lines)


def write_file(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def link_for(folder: str, id_: str | None, fallback: str | None = None) -> str:
    if not id_:
        return fallback or ""
    return f"[[{folder}/{slugify(id_)}|{id_}]]"


def index_by_id(arr: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    return {r.get("id"): r for r in arr if isinstance(r, dict) and r.get("id")}


# ────────────────────────────────────────────────────────────────────────────
# Per-type renderers
# ────────────────────────────────────────────────────────────────────────────


def render_decree(d: dict[str, Any], institutions: dict, people: dict) -> str:
    fm = {
        "type": "decree",
        "id": d.get("id"),
        "country": d.get("country"),
        "decree_type": d.get("decree_type"),
        "number": d.get("number"),
        "date": d.get("date"),
        "signatory": d.get("signatory"),
        "half_life_status": d.get("half_life_status"),
        "verification": d.get("verification"),
        "tags": [
            f"country/{(d.get('country') or '').lower()}",
            f"decree/{(d.get('decree_type') or '').lower()}",
            f"verification/{(d.get('verification') or '').lower()}",
        ],
        "aliases": [d.get("number") or "", d.get("title_en") or ""],
    }
    body = [frontmatter(fm)]
    body.append(f"# {d.get('title_en') or d.get('title_original') or d.get('id')}")
    body.append("")
    body.append(f"_{d.get('title_original') or ''}_")
    body.append("")
    if d.get("ai_digital_provisions"):
        body.append("## Provisions on AI / digital")
        body.append("")
        body.append(d["ai_digital_provisions"])
        body.append("")
    if d.get("responsible_agency_ids"):
        body.append("## Responsible institutions")
        body.append("")
        for aid in d["responsible_agency_ids"]:
            body.append(f"- {link_for('Institutions', aid)}")
        body.append("")
    if d.get("responsible_person_ids"):
        body.append("## Responsible persons")
        body.append("")
        for pid in d["responsible_person_ids"]:
            body.append(f"- {link_for('People', pid)}")
        body.append("")
    if d.get("sources"):
        body.append("## Sources")
        body.append("")
        for s in d["sources"]:
            body.append(
                f"- [{s.get('title') or s.get('url')}]({s.get('url')}) ({s.get('language', 'en')}, {s.get('publisher', '')})"
            )
        body.append("")
    body.append(f"\n*Last verified: {d.get('status_as_of', '')}*")
    return "\n".join(body)


def render_institution(i: dict[str, Any], people: dict) -> str:
    fm = {
        "type": "institution",
        "id": i.get("id"),
        "country": i.get("country"),
        "tier": i.get("tier"),
        "status": i.get("status"),
        "verification": i.get("verification"),
        "tags": [
            f"country/{(i.get('country') or '').lower()}",
            f"tier/{i.get('tier')}",
            f"status/{i.get('status')}",
        ],
        "aliases": [i.get("name_ru") or "", i.get("name_local") or ""],
    }
    body = [frontmatter(fm)]
    body.append(f"# {i.get('name_en') or i.get('id')}")
    body.append("")
    body.append(f"**RU**: {i.get('name_ru') or ''}  ")
    if i.get("name_local"):
        body.append(f"**Local**: {i.get('name_local')}  ")
    if i.get("ai_digital_mandate"):
        body.append("\n## Mandate (AI / digital)\n\n" + i["ai_digital_mandate"] + "\n")
    head = i.get("head_person_id")
    if head:
        body.append(f"**Head**: {link_for('People', head)}\n")
    if i.get("deputy_person_ids"):
        body.append("**Deputies**:")
        for pid in i["deputy_person_ids"]:
            body.append(f"  - {link_for('People', pid)}")
        body.append("")
    parent = i.get("reports_to_id")
    if parent:
        body.append(f"**Reports to**: {link_for('Institutions', parent)}\n")
    if i.get("recent_decisions_12mo"):
        body.append("## Recent decisions (12 months)\n")
        for r in i["recent_decisions_12mo"]:
            body.append(f"- {r}")
        body.append("")
    if i.get("sources"):
        body.append("## Sources\n")
        for s in i["sources"]:
            body.append(f"- [{s.get('title') or s.get('url')}]({s.get('url')}) ({s.get('language', 'en')})")
        body.append("")
    body.append(f"\n*Last verified: {i.get('last_verified_date', '')}*")
    return "\n".join(body)


def render_person(p: dict[str, Any]) -> str:
    fm = {
        "type": "person",
        "id": p.get("id"),
        "country": p.get("country"),
        "current_role": p.get("current_role"),
        "current_institution": link_for("Institutions", p.get("current_institution_id"))
        if p.get("current_institution_id")
        else None,
        "linkedin_status": p.get("linkedin_status"),
        "linkedin_url": p.get("linkedin_url"),
        "diaspora_advisor_flag": p.get("diaspora_advisor_flag", False),
        "diaspora_location": p.get("diaspora_location"),
        "priority_tier": p.get("priority_tier"),
        "verification": p.get("verification"),
        "tags": [
            f"country/{(p.get('country') or '').lower()}",
            f"tier/{p.get('priority_tier')}",
            f"verification/{(p.get('verification') or '').lower()}",
        ],
        "aliases": [
            p.get("full_name_latin") or "",
            p.get("full_name_ru") or "",
            p.get("full_name_local") or "",
        ],
    }
    body = [frontmatter(fm)]
    body.append(f"# {p.get('full_name_latin') or p.get('id')}")
    body.append("")
    body.append(f"**Role**: {p.get('current_role') or ''} at "
                f"{link_for('Institutions', p.get('current_institution_id'))}\n")
    if p.get("linkedin_url") and p.get("linkedin_status") == "verified":
        body.append(f"**LinkedIn (verified)**: <{p['linkedin_url']}>\n")
    elif p.get("linkedin_status"):
        body.append(f"**LinkedIn**: status={p['linkedin_status']}\n")
    if p.get("languages"):
        body.append(f"**Languages**: {', '.join(p['languages'])}\n")
    if p.get("education"):
        body.append("## Education\n")
        for e in p["education"]:
            body.append(f"- {e.get('degree', '')} — {e.get('institution', '')} ({e.get('year', '')})")
        body.append("")
    if p.get("career_history"):
        body.append("## Career\n")
        for c in p["career_history"]:
            body.append(f"- {c.get('role', '')} at {c.get('institution', '')} ({c.get('from', '')}–{c.get('to', '')})")
        body.append("")
    if p.get("public_statements_ai_digital"):
        body.append("## Public statements (AI/digital)\n")
        for s in p["public_statements_ai_digital"]:
            body.append(f"- {s.get('date', '')} — {s.get('venue', '')}: {s.get('summary', '')} ([source]({s.get('url', '')}))")
        body.append("")
    if p.get("pitch_hook"):
        body.append("> [!info] Pitch hook")
        body.append(f"> {p['pitch_hook']}\n")
    body.append(f"\n*Last verified: {p.get('last_verified_date', '')}*")
    return "\n".join(body)


def render_donor(d: dict[str, Any]) -> str:
    fm = {
        "type": "donor_program",
        "id": d.get("id"),
        "donor": d.get("donor"),
        "country": d.get("country"),
        "status": d.get("status"),
        "total_budget_usd": d.get("total_budget_usd"),
        "ttl_pm_name": d.get("ttl_pm_name"),
        "verification": d.get("verification"),
        "tags": [
            f"donor/{(d.get('donor') or '').lower()}",
            f"country/{(d.get('country') or '').lower()}",
            f"status/{d.get('status')}",
        ],
    }
    body = [frontmatter(fm)]
    body.append(f"# {d.get('program_name') or d.get('id')}")
    body.append("")
    body.append(f"**Donor**: {d.get('donor')}  •  **Country**: {d.get('country')}  •  **Status**: {d.get('status')}\n")
    if d.get("ai_digital_relevance"):
        body.append("## AI / digital relevance\n\n" + d["ai_digital_relevance"] + "\n")
    if d.get("ttl_pm_name"):
        body.append(f"**TTL/PM**: {d['ttl_pm_name']}\n")
    counterpart = d.get("government_counterpart_person_id")
    if counterpart:
        body.append(f"**Government counterpart**: {link_for('People', counterpart)}\n")
    if d.get("pipeline_tenders"):
        body.append("## Pipeline tenders\n")
        for t in d["pipeline_tenders"]:
            body.append(f"- {t.get('title', '')} ({t.get('expected_date', '')}) — ${t.get('estimated_value_usd', 0):,.0f}")
        body.append("")
    if d.get("sources"):
        body.append("## Sources\n")
        for s in d["sources"]:
            body.append(f"- [{s.get('title') or s.get('url')}]({s.get('url')})")
        body.append("")
    return "\n".join(body)


def render_tender(t: dict[str, Any], institutions: dict) -> str:
    fm = {
        "type": "tender",
        "id": t.get("id"),
        "country": t.get("country"),
        "category": t.get("category"),
        "status": t.get("status"),
        "estimated_value_usd": t.get("estimated_value_usd"),
        "submission_deadline": t.get("submission_deadline"),
        "win_probability": t.get("win_probability"),
        "incumbent_risk": t.get("incumbent_risk"),
        "verification": t.get("verification"),
        "tags": [f"country/{(t.get('country') or '').lower()}", f"status/{t.get('status')}"],
    }
    body = [frontmatter(fm)]
    body.append(f"# {t.get('title_en') or t.get('title') or t.get('id')}")
    body.append("")
    body.append(f"**Issuer**: {link_for('Institutions', t.get('issuing_entity_id'))}  •  "
                f"**Deadline**: {t.get('submission_deadline')}  •  "
                f"**Value**: ${(t.get('estimated_value_usd') or 0):,.0f}\n")
    if t.get("ai_digital_scope"):
        body.append("## Scope\n\n" + t["ai_digital_scope"] + "\n")
    if t.get("win_probability_rationale"):
        body.append(f"**Win probability ({t.get('win_probability')})**: {t['win_probability_rationale']}\n")
    if t.get("tender_url"):
        body.append(f"[Open tender]({t['tender_url']})\n")
    return "\n".join(body)


def render_trend(t: dict[str, Any]) -> str:
    fm = {
        "type": "trend",
        "id": t.get("id"),
        "country": t.get("country"),
        "sector": t.get("sector"),
        "maturity": t.get("maturity"),
        "lens_tags": t.get("lens_tags", []),
        "verification": t.get("verification"),
        "tags": [f"country/{(t.get('country') or '').lower()}", f"sector/{(t.get('sector') or '').lower()}"],
    }
    body = [frontmatter(fm)]
    body.append(f"# {t.get('name') or t.get('id')}")
    body.append("")
    if t.get("killer_app_description"):
        body.append("> [!important] Killer app")
        body.append(f"> {t['killer_app_description']}\n")
    if t.get("drivers"):
        body.append("## Drivers\n")
        for d in t["drivers"]:
            body.append(f"- {d}")
        body.append("")
    if t.get("linked_decree_ids"):
        body.append("## Linked decrees\n")
        for did in t["linked_decree_ids"]:
            body.append(f"- {link_for('Decrees', did)}")
        body.append("")
    if t.get("linked_donor_program_ids"):
        body.append("## Linked donor programs\n")
        for did in t["linked_donor_program_ids"]:
            body.append(f"- {link_for('Donors', did)}")
        body.append("")
    return "\n".join(body)


def render_case(c: dict[str, Any]) -> str:
    fm = {
        "type": "global_case",
        "id": c.get("id"),
        "country_origin": c.get("country_origin"),
        "sector": c.get("sector"),
        "year_initiated": c.get("year_initiated"),
        "uz_transferability_score": c.get("uz_transferability_score"),
        "kg_transferability_score": c.get("kg_transferability_score"),
        "verification": c.get("verification"),
    }
    body = [frontmatter(fm)]
    body.append(f"# {c.get('case_name') or c.get('id')}")
    body.append("")
    body.append(f"**Origin**: {c.get('country_origin')}  •  **Year**: {c.get('year_initiated')}  •  **Sector**: {c.get('sector')}\n")
    if c.get("problem_solved"):
        body.append("## Problem solved\n\n" + c["problem_solved"] + "\n")
    if c.get("architecture_summary"):
        body.append("## Architecture\n\n" + c["architecture_summary"] + "\n")
    if c.get("uz_transferability_rationale"):
        body.append(f"## UZ transferability ({c.get('uz_transferability_score', 0)}/10)\n\n" + c["uz_transferability_rationale"] + "\n")
    if c.get("kg_transferability_rationale"):
        body.append(f"## KG transferability ({c.get('kg_transferability_score', 0)}/10)\n\n" + c["kg_transferability_rationale"] + "\n")
    return "\n".join(body)


def render_mvp(m: dict[str, Any]) -> str:
    sc = m.get("scoring", {})
    fm = {
        "type": "solopreneur_mvp",
        "id": m.get("id"),
        "country": m.get("country"),
        "category": m.get("category"),
        "sector": m.get("sector"),
        "confidence_tier": m.get("confidence_tier"),
        "weighted_total": sc.get("weighted_total"),
        "linked_trend": link_for("Trends", (m.get("underlying_demand") or {}).get("trend_id")),
        "linked_decree": link_for("Decrees", (m.get("underlying_demand") or {}).get("decree_id")),
        "linked_donor": link_for("Donors", (m.get("underlying_demand") or {}).get("donor_program_id")),
        "linked_initiative": link_for("Initiatives", m.get("linked_initiative_id")),
        "verification": m.get("verification"),
        "tags": [
            f"country/{(m.get('country') or '').lower()}",
            f"category/{m.get('category')}",
            f"tier/{m.get('confidence_tier')}",
            f"sector/{slugify(m.get('sector') or '')}",
        ],
    }
    body = [frontmatter(fm)]
    body.append(f"# {m.get('short_name') or m.get('id')}")
    body.append("")
    if m.get("tagline"):
        body.append(f"_{m['tagline']}_\n")
    demand = m.get("underlying_demand") or {}
    body.append(f"## Pain point\n\n{demand.get('pain_point', '')}\n")
    if demand.get("evidence"):
        body.append(f"**Evidence**: {demand['evidence']}\n")
    body.append(f"\n**Target customer**: {m.get('target_customer', '')}\n")
    mon = m.get("monetization") or {}
    body.append("\n## Monetization\n")
    body.append(f"- **Model**: {mon.get('model')}")
    body.append(f"- **Price point**: ${mon.get('price_point_usd', 0):.2f}")
    body.append(f"- **Year-1 target**: ${mon.get('year_1_revenue_target_usd', 0):,.0f}")
    body.append(f"- **Year-3 target**: ${mon.get('year_3_revenue_target_usd', 0):,.0f}")
    body.append("")
    plan = m.get("mvr_plan") or {}
    body.append(f"\n## MVR plan ({plan.get('vehicle')})\n")
    body.append(f"- **Build time**: {plan.get('build_time_days')} days")
    body.append(f"- **Build cost**: ${plan.get('build_cost_usd', 0):.0f}")
    body.append("\n**Steps:**")
    for s in plan.get("build_steps", []) or []:
        body.append(f"- [ ] {s}")
    body.append("")
    val = m.get("validation") or {}
    body.append(f"\n## Validation\n")
    body.append(f"- **Signal target**: {val.get('signal_target', '')}")
    body.append(f"- **Window**: {val.get('validation_window_days')} days")
    body.append(f"- **Channels**: {', '.join(val.get('channels', []) or [])}")
    body.append("")
    if m.get("tech_stack"):
        body.append(f"\n**Tech stack**: {', '.join(m['tech_stack'])}\n")
    if m.get("founder_capability_required"):
        body.append(f"**Capability required**: {', '.join(m['founder_capability_required'])}\n")
    if m.get("moat_potential"):
        body.append(f"\n## Moat potential\n\n{m['moat_potential']}\n")
    if m.get("risk_register"):
        body.append("## Risks\n")
        for r in m["risk_register"]:
            body.append(f"- **{r.get('risk', '')}** — _Mitigation_: {r.get('mitigation', '')}")
        body.append("")
    body.append(f"\n## Scoring (weighted total: **{sc.get('weighted_total', 0):.2f}**)\n")
    body.append("| Axis | Score |")
    body.append("|---|---|")
    body.append(f"| Demand clarity (30%) | {sc.get('demand_clarity', 0)}/10 |")
    body.append(f"| Speed to MVR (15%) | {sc.get('speed_to_mvr', 0)}/10 |")
    body.append(f"| Monetization path (20%) | {sc.get('monetization_path', 0)}/10 |")
    body.append(f"| Founder solo feasibility (20%) | {sc.get('founder_solo_feasibility', 0)}/10 |")
    body.append(f"| Local market fit (15%) | {sc.get('local_market_fit', 0)}/10 |")
    body.append("")
    if sc.get("scoring_rationale"):
        body.append("### Rationale\n\n" + sc["scoring_rationale"] + "\n")
    return "\n".join(body)


def render_initiative(i: dict[str, Any]) -> str:
    sc = i.get("scoring", {})
    fm = {
        "type": "initiative",
        "id": i.get("id"),
        "country": i.get("country"),
        "sector": i.get("sector"),
        "confidence_tier": i.get("confidence_tier"),
        "weighted_total": sc.get("weighted_total"),
        "speed_to_contract": sc.get("speed_to_contract"),
        "strategic_moat": sc.get("strategic_moat"),
        "defensibility": sc.get("defensibility"),
        "capital_access": sc.get("capital_access"),
        "russian_cis_fit": sc.get("russian_cis_fit"),
        "target_buyer": link_for("People", i.get("target_buyer_person_id")),
        "lead_institution": link_for("Institutions", i.get("lead_institution_id")),
        "authorizing_decrees": [link_for("Decrees", d) for d in (i.get("authorizing_decree_ids") or [])],
        "precedent_case": link_for("Cases", i.get("precedent_case_id")),
        "verification": i.get("verification"),
        "tags": [
            f"tier/{i.get('confidence_tier')}",
            f"country/{(i.get('country') or '').lower()}",
            f"sector/{slugify(i.get('sector') or '')}",
        ],
    }
    body = [frontmatter(fm)]
    body.append(f"# {i.get('short_name') or i.get('id')}")
    body.append("")
    if i.get("one_liner"):
        body.append(f"_{i['one_liner']}_\n")
    body.append("## Problem\n\n" + (i.get("problem_statement") or "") + "\n")
    body.append("## Solution concept\n\n" + (i.get("solution_concept") or "") + "\n")
    body.append("## Pitch hook\n")
    body.append(f"> [!quote] Hook\n> {i.get('pitch_hook', '')}\n")
    if i.get("next_30_day_actions"):
        body.append("## Next 30 days\n")
        for a in i["next_30_day_actions"]:
            body.append(f"- [ ] {a}")
        body.append("")
    if i.get("risk_register"):
        body.append("## Risk register\n")
        for r in i["risk_register"]:
            body.append(f"- **{r.get('risk_type', '')}**: {r.get('description', '')} — _Mitigation_: {r.get('mitigation', '')}")
        body.append("")
    body.append(f"\n## Scoring (weighted total: **{sc.get('weighted_total', 0):.2f}**)\n")
    body.append("| Axis | Score |")
    body.append("|---|---|")
    body.append(f"| Speed-to-Contract | {sc.get('speed_to_contract', 0)}/10 |")
    body.append(f"| Strategic Moat | {sc.get('strategic_moat', 0)}/10 |")
    body.append(f"| Defensibility | {sc.get('defensibility', 0)}/10 |")
    body.append(f"| Capital Access | {sc.get('capital_access', 0)}/10 |")
    body.append(f"| Russian/CIS Fit | {sc.get('russian_cis_fit', 0)}/10 |")
    body.append("")
    if sc.get("scoring_rationale"):
        body.append("### Rationale\n\n" + sc["scoring_rationale"] + "\n")
    return "\n".join(body)


# ────────────────────────────────────────────────────────────────────────────
# Vault index + briefs
# ────────────────────────────────────────────────────────────────────────────


def render_readme(graph: dict[str, Any]) -> str:
    today = date.today().isoformat()
    counts = {
        "decrees": len(graph.get("decrees", []) or []),
        "institutions": len(graph.get("institutions", []) or []),
        "people": len(graph.get("people", []) or []),
        "donor_programs": len(graph.get("donor_programs", []) or []),
        "tenders": len(graph.get("tenders", []) or []),
        "trends": len(graph.get("trends", []) or []),
        "global_cases": len(graph.get("global_cases", []) or []),
        "initiatives": len(graph.get("initiatives", []) or []),
        "solopreneur_mvps": len(graph.get("solopreneur_mvps", []) or []),
    }
    fm = frontmatter({"type": "vault_index", "generated_at": today})
    return fm + f"""# Central Asia B2G Intelligence — Obsidian Vault

A typed, source-cited knowledge graph of AI/digital government opportunities in Uzbekistan and Kyrgyzstan. {counts['initiatives']} initiatives, {counts['people']} decision-makers, {counts['decrees']} decrees, {counts['institutions']} institutions, {counts['donor_programs']} donor programs.

> [!tip] How to use
> Open the **Graph view** (`Ctrl+G`) to see the full relationship network. Open **Briefs/Top 100 Initiatives** to find Tier-A deals to chase. Use the Dataview queries below to slice the data however you need.

## Counts

- {counts['decrees']} Decrees · {counts['institutions']} Institutions · {counts['people']} People · {counts['donor_programs']} Donor programs
- {counts['tenders']} Tenders · {counts['trends']} Trends · {counts['global_cases']} Global cases · {counts['initiatives']} Initiatives

## Top initiatives (by weighted total)

```dataview
TABLE
  weighted_total AS "Score",
  confidence_tier AS "Tier",
  country AS "C",
  sector AS "Sector",
  target_buyer AS "Buyer"
FROM "Initiatives"
WHERE confidence_tier = "A"
SORT weighted_total DESC
LIMIT 30
```

## Decrees in active implementation window

```dataview
TABLE country, decree_type, number, date, signatory
FROM "Decrees"
WHERE half_life_status = "active_window"
SORT date DESC
```

## Tier-1 priority people

```dataview
TABLE country, current_role, linkedin_status, diaspora_advisor_flag
FROM "People"
WHERE priority_tier = 1
SORT country
```

## Donor programs by status

```dataview
TABLE donor, country, status, total_budget_usd, ttl_pm_name
FROM "Donors"
SORT total_budget_usd DESC
```

## Top solopreneur MVPs

```dataview
TABLE
  weighted_total AS "Score",
  confidence_tier AS "Tier",
  country AS "C",
  category AS "Cat",
  sector AS "Sector"
FROM "Solopreneur MVPs"
WHERE confidence_tier = "A"
SORT weighted_total DESC
LIMIT 30
```

## Methodology

See [[00 Methodology]] for the 7-wave research pipeline. See [[01 Lenses]] for the 5+1 analytical lenses applied across every record. See [[02 Scoring]] for the weighted scoring rubric.
"""


def render_lenses_doc(lenses_md: str) -> str:
    return frontmatter({"type": "doc", "title": "5+1 Analytical Lenses"}) + lenses_md


def render_scoring_doc(rubric_md: str) -> str:
    return frontmatter({"type": "doc", "title": "Scoring Rubric"}) + rubric_md


def render_methodology() -> str:
    return frontmatter({"type": "doc", "title": "Methodology"}) + """# Methodology

This vault is rendered from `state/knowledge_graph.json` — the merged read view of 11 specialised research agents that work in 7 waves.

| Wave | Agent(s) | Output |
|---|---|---|
| 0 | blueprint-architect | Strategic plan, target lists |
| 1 | legal-cartographer, case-tournament | Decrees, global cases |
| 2 | institution-mapper, donor-pipeline, procurement-harvester, trend-triangulator | Institutions, donor programs, tenders, trends |
| 3 | people-intelligence | Decision-makers, diaspora bridges |
| 4 | initiative-synthesizer | Scored initiatives |
| 5 | reflexion-auditor | Adversarial re-verification |
| 6 | pitch-artificer | Outreach bundles (private vault only) |

Every claim carries a **verification tag**: VERIFIED, L2_VERIFIED, L3_VERIFIED, INFERRED, UNVERIFIED, or CONTRADICTED. See `state/audit/audit_report.md` for the adversarial review of the data.

Source priority is hierarchical and includes ≥1 Russian-language source per country claim.
"""


# ────────────────────────────────────────────────────────────────────────────
# Top-level renderer
# ────────────────────────────────────────────────────────────────────────────


def render_all(graph: dict[str, Any]) -> None:
    if VAULT.exists():
        # Preserve .obsidian if it exists
        for child in VAULT.iterdir():
            if child.name == ".obsidian":
                continue
            if child.is_dir():
                shutil.rmtree(child)
            else:
                child.unlink()
    VAULT.mkdir(parents=True, exist_ok=True)

    institutions_idx = index_by_id(graph.get("institutions", []) or [])
    people_idx = index_by_id(graph.get("people", []) or [])

    # Top-level docs
    write_file(VAULT / "README.md", render_readme(graph))
    write_file(VAULT / "00 Methodology.md", render_methodology())
    if (DOCS / "lenses.md").exists():
        write_file(VAULT / "01 Lenses.md", render_lenses_doc((DOCS / "lenses.md").read_text()))
    if (DOCS / "scoring_rubric.md").exists():
        write_file(VAULT / "02 Scoring.md", render_scoring_doc((DOCS / "scoring_rubric.md").read_text()))

    # Per-record files
    counts: dict[str, int] = {}
    for d in graph.get("decrees", []) or []:
        write_file(VAULT / "Decrees" / f"{slugify(d.get('id') or '')}.md", render_decree(d, institutions_idx, people_idx))
    counts["decrees"] = len(graph.get("decrees", []) or [])

    for i in graph.get("institutions", []) or []:
        write_file(VAULT / "Institutions" / f"{slugify(i.get('id') or '')}.md", render_institution(i, people_idx))
    counts["institutions"] = len(graph.get("institutions", []) or [])

    for p in graph.get("people", []) or []:
        write_file(VAULT / "People" / f"{slugify(p.get('id') or '')}.md", render_person(p))
    counts["people"] = len(graph.get("people", []) or [])

    for d in graph.get("donor_programs", []) or []:
        write_file(VAULT / "Donors" / f"{slugify(d.get('id') or '')}.md", render_donor(d))
    counts["donor_programs"] = len(graph.get("donor_programs", []) or [])

    for t in graph.get("tenders", []) or []:
        write_file(VAULT / "Tenders" / f"{slugify(t.get('id') or '')}.md", render_tender(t, institutions_idx))
    counts["tenders"] = len(graph.get("tenders", []) or [])

    for t in graph.get("trends", []) or []:
        write_file(VAULT / "Trends" / f"{slugify(t.get('id') or '')}.md", render_trend(t))
    counts["trends"] = len(graph.get("trends", []) or [])

    for c in graph.get("global_cases", []) or []:
        write_file(VAULT / "Cases" / f"{slugify(c.get('id') or '')}.md", render_case(c))
    counts["global_cases"] = len(graph.get("global_cases", []) or [])

    for i in graph.get("initiatives", []) or []:
        write_file(VAULT / "Initiatives" / f"{slugify(i.get('id') or '')}.md", render_initiative(i))
    counts["initiatives"] = len(graph.get("initiatives", []) or [])

    for m in graph.get("solopreneur_mvps", []) or []:
        write_file(VAULT / "Solopreneur MVPs" / f"{slugify(m.get('id') or '')}.md", render_mvp(m))
    counts["solopreneur_mvps"] = len(graph.get("solopreneur_mvps", []) or [])

    # Briefs
    write_file(VAULT / "Briefs" / "README.md", frontmatter({"type": "section_index"}) + "# Briefs\n\nStrategic memo, week-1 action list, and top-100 initiative cards.\n")

    print("Vault written:", VAULT)
    for k, v in counts.items():
        print(f"   {k}: {v}")


def main() -> int:
    if not GRAPH_PATH.exists():
        print(f"⚠ {GRAPH_PATH} not found — rendering empty vault skeleton")
        graph: dict[str, Any] = {}
    else:
        graph = json.loads(GRAPH_PATH.read_text())
    render_all(graph)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
