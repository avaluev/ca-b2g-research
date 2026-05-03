---
type: "solopreneur_mvp"
id: "uz-mvp-030"
country: "UZ"
category: "free_tool"
sector: "Agriculture & Water"
confidence_tier: "B"
weighted_total: 7.05
linked_trend: "[[Trends/uz-trend-014-precision-agri-satellite|uz-trend-014-precision-agri-satellite]]"
linked_decree: "[[Decrees/uz-pp-2025-099|UZ-PP-2025-099]]"
linked_donor: ""
linked_initiative: ""
verification: "INFERRED"
tags:
  - "country/uz"
  - "category/free_tool"
  - "tier/B"
  - "sector/agriculture-water"
---

# FertilizerCalc

_Free Telegram calculator giving precise fertilizer dosages by crop and field area, in Uzbek and Russian_

## Pain point

Smallholder farmers under- or over-apply fertilizer due to lack of crop-specific calculators in Uzbek. Result: yield loss + soil degradation. Existing online calculators are Russian-only and weight-based.

**Evidence**: https://agro.uz/


**Target customer**: Smallholder farmers 30-55 across Uzbekistan growing cotton, wheat, vegetables; secondary: agronomy students


## Monetization

- **Model**: ad
- **Price point**: $30.00
- **Year-1 target**: $6,000
- **Year-3 target**: $40,000


## MVR plan (free_tool)

- **Build time**: 5 days
- **Build cost**: $30

**Steps:**
- [ ] Compile fertilizer formula tables for top 12 crops
- [ ] Telegram bot intake: crop + area + soil type
- [ ] Output: NPK in kg + cost + nearest dealer (sponsor)
- [ ] Sell sponsored slot to one fertilizer dealer ($30/mo)
- [ ] Soft-launch in agro.uz forum


## Validation

- **Signal target**: 1,500 calculations + 1 sponsor in 45 days
- **Window**: 45 days
- **Channels**: agro.uz, Fergana farmer Telegram


**Tech stack**: Telegram Bot, Supabase, Notion (data)

**Capability required**: Russian + Uzbek, agronomy basics or partner agronomist


## Moat potential

Sponsor relationship + per-region database compounds.

## Risks

- **Low ad demand** — _Mitigation_: Run 3 dealers as sponsors split
- **Region-specific accuracy** — _Mitigation_: User feedback + agronomist review
- **Free clone** — _Mitigation_: Lean on bilingual UX + sponsor exclusivity


## Scoring (weighted total: **7.05**)

| Axis | Score |
|---|---|
| Demand clarity (30%) | 6/10 |
| Speed to MVR (15%) | 10/10 |
| Monetization path (20%) | 5/10 |
| Founder solo feasibility (20%) | 9/10 |
| Local market fit (15%) | 8/10 |

### Rationale

Cheap to build, modest revenue, real utility.
