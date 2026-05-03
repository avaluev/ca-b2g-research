---
type: "doc"
title: "Scoring Rubric"
---
# Scoring Rubric — 5-Axis Initiative Prioritization

Every initiative is scored 1–10 on five axes, then weighted-summed for ranking. Default weights are below; override via `weights.json`.

## Default weights

| Axis | Weight | Notes |
|---|---|---|
| Speed-to-contract | 25% | Highest weight — selected as priority |
| Strategic moat | 20% | Selected as priority |
| Defensibility | 20% | Selected as priority |
| Capital access | 20% | Selected as priority |
| Russian/CIS delivery fit | 15% | Selected as priority |

`weighted_total = 0.25*speed + 0.20*moat + 0.20*defensibility + 0.20*capital + 0.15*russian_cis_fit`

## Axis 1: Speed-to-Contract (1–10)

How fast can this initiative produce billable revenue?

- **10**: Live RFP exists, submission window open, your offer is competitive, decision within 90 days
- **9**: RFP imminent (next 60 days), pre-qualification possible
- **8**: Decree implementation deadline within 6 months, budget allocated, procurement designer is reachable
- **7**: Donor program disbursement schedule active in next 6 months, government counterpart identified
- **6**: 6–12 month window, named decision-maker, no live RFP yet
- **5**: 12–18 month window, decree in active phase, budget pathway clear
- **4**: 18–24 month window, requires policy advocacy
- **3**: Multi-year horizon, requires market education
- **2**: Speculative, dependent on next political cycle
- **1**: No clear pathway, theoretical

**Verifiers**: live tender URL, decree implementation deadline date, donor disbursement schedule

## Axis 2: Strategic Moat (1–10)

How protected is this opportunity from competition?

- **10**: Presidential decree explicitly priorities the use case, named in Uzbekistan-2030 / Digital KG strategy, ≤2 incumbents, your capability is uniquely positioned
- **9**: Top-3 government KPI, low foreign vendor presence
- **8**: Sectoral priority, 2–3 incumbents but you have differentiated positioning
- **7**: Visible government priority, moderate competition
- **6**: Standard market opportunity with some defensible angle
- **5**: Competitive market, win on execution
- **4**: Highly competitive, commodity-style
- **3**: Crowded with global incumbents
- **2**: Saturated market, marginal differentiation
- **1**: No moat, race to the bottom

**Verifiers**: presence in Uzbekistan-2030 or Digital Kyrgyzstan strategies, count of vendor incumbents in segment, presidential mention frequency

## Axis 3: Defensibility (1–10)

Once you win, how hard is it to be displaced?

- **10**: Multi-year SLA structure standard, data ownership clause achievable, network effects activate, switching cost is enormous (citizen-facing platform with adoption lock-in)
- **9**: 3+ year contracts standard, data lock-in, integration depth
- **8**: Multi-year structure, moderate switching cost
- **7**: Annual renewal but high incumbency advantage
- **6**: Standard renewal patterns, some lock-in
- **5**: Annual renewal, modest stickiness
- **4**: Project-based, no recurring component
- **3**: One-shot deliverable, no incumbency advantage
- **2**: Hardware/commodity, easily replaced
- **1**: Pure transactional, no relationship moat

**Verifiers**: contract length norms in segment, data ownership clause negotiability, integration depth required, regulatory capture potential (e.g., becoming the standard the regulator references)

## Axis 4: Capital Access (1–10)

How well-funded is this opportunity from non-state-budget sources?

- **10**: Active donor program co-financing > $5M, TTL/PM identified and reachable, disbursement schedule includes the relevant tender window
- **9**: Active donor program $1–5M, named PM
- **8**: Pipeline donor program in appraisal, expected award in 12 months
- **7**: Multi-donor convergence (e.g., WB + EU on same problem)
- **6**: State budget line confirmed, no donor co-financing but stable funding
- **5**: State budget line probable, awaiting next budget cycle
- **4**: Aspirational state allocation, no donor backing
- **3**: PPP-only pathway, requires capital from your side
- **2**: Revenue-share only, slow ramp
- **1**: No clear funding pathway

**Verifiers**: World Bank Documents portal, ADB project database, EU NDICI plan, disbursement reports

## Axis 5: Russian/CIS Delivery Fit (1–10)

How well does this match your sntz.ai infrastructure and Russian-language distribution muscle?

- **10**: Russian-language UX mandatory/preferred, data localization required (CIS-friendly cloud beneficial), buyer wants non-Western non-sanctions-exposed vendor, payment rails compatible (MIR/SBP/Paddle), use case maps to your existing platform capabilities (image/video/text generation, agentic workflows)
- **9**: Russian-language strongly preferred, your stack is direct fit
- **8**: Multi-language but Russian is primary working language
- **7**: Local language (Uzbek/Kyrgyz) primary but your team can deliver via partners
- **6**: English/local mix, your stack adapts
- **5**: Multi-language with no strong Russian/CIS preference
- **4**: Local-language-only mandate, your stack needs heavy localization
- **3**: Western-vendor-preferred segment (e.g., banking core systems with regulatory pressure for Western brand)
- **2**: Active US/EU vendor preference, geopolitically sensitive
- **1**: Anti-Russian-vendor sentiment in segment, your positioning is liability

**Verifiers**: language requirements in past tenders, data localization rules, sanctioned-vendor exclusions, payment rail requirements

## Confidence Tier Mapping

After scoring, initiatives are bucketed into tiers based on `weighted_total` AND `verification` quality:

- **Tier A** (`weighted_total >= 7.5` AND all key fields VERIFIED): go now, deal-ready
- **Tier B** (`weighted_total >= 6.0` AND most fields VERIFIED or L2_VERIFIED): develop, missing one piece
- **Tier C** (`weighted_total >= 4.5`): backlog, requires more research
- **Tier D** (`weighted_total < 4.5` OR significant UNVERIFIED gaps): reconsider or drop

The CRM exports Tier A and B by default. Tiers C and D are available in the full knowledge graph for periodic re-evaluation.

## Slice views (CRM rendering)

The render pipeline produces these views by sorting on a single axis:
- `top_speed.csv` — sorted by speed-to-contract DESC
- `top_moat.csv` — sorted by strategic_moat DESC
- `top_defensibility.csv` — sorted by defensibility DESC
- `top_capital.csv` — sorted by capital_access DESC
- `top_russian_cis.csv` — sorted by russian_cis_fit DESC
- `top_overall.csv` — sorted by weighted_total DESC
- `convergent_windows.csv` — initiatives scoring ≥7 on at least 4 axes

The convergent_windows view is the most strategically valuable: opportunities where multiple lenses align simultaneously.
