---
type: "solopreneur_mvp"
id: "kg-mvp-034"
country: "KG"
category: "ai_tool"
sector: "Agriculture & Water"
confidence_tier: "B"
weighted_total: 6.55
linked_trend: "[[Trends/kg-trend-010-agri-ai-naryn|kg-trend-010-agri-ai-naryn]]"
linked_decree: "[[Decrees/kg-law-2025-178-digital-code|KG-LAW-2025-178-DIGITAL-CODE]]"
linked_donor: ""
linked_initiative: ""
verification: "L2_VERIFIED"
tags:
  - "country/kg"
  - "category/ai_tool"
  - "tier/B"
  - "sector/agriculture-water"
---

# PestSpotterKG

_Free tool: photo your crop leaf, get a Kyrgyz-language pest/disease ID and treatment plan_

## Pain point

Farmers misdiagnose pests. Extension agents spread thin. Plantix lacks Kyrgyz + regional pest coverage.

**Evidence**: https://kaktus.media/


**Target customer**: Smallholder farmers 30-55 in Chui, Issyk-Kul, Naryn growing wheat, vegetables, fruit


## Monetization

- **Model**: freemium
- **Price point**: $4.00
- **Year-1 target**: $7,000
- **Year-3 target**: $50,000


## MVR plan (free_tool)

- **Build time**: 10 days
- **Build cost**: $80

**Steps:**
- [ ] Fine-tune CLIP/DINOv2 on small KG pest dataset
- [ ] Telegram bot intake + Russian/Kyrgyz treatment
- [ ] Free 3 IDs/wk, $4/mo unlimited
- [ ] Affiliate to local agro-input dealers
- [ ] Soft-launch in Chui + Issyk-Kul farmer Telegram


## Validation

- **Signal target**: 300 IDs + 15 paid in 60 days
- **Window**: 60 days
- **Channels**: Chui farmer Telegram, Issyk-Kul farmer, kaktus.media agri


**Tech stack**: CLIP/DINOv2, Supabase, Telegram Bot, Mbank

**Capability required**: Russian + Kyrgyz, ML basics, agronomy partner


## Moat potential

Kyrgyz-pest dataset moat.

## Risks

- **Misdiagnosis liability** — _Mitigation_: Disclaimer + agronomist review
- **Low data quality** — _Mitigation_: User feedback bounties
- **Affiliate uncertain** — _Mitigation_: Sponsorship from one dealer


## Scoring (weighted total: **6.55**)

| Axis | Score |
|---|---|
| Demand clarity (30%) | 6/10 |
| Speed to MVR (15%) | 7/10 |
| Monetization path (20%) | 5/10 |
| Founder solo feasibility (20%) | 7/10 |
| Local market fit (15%) | 8/10 |

### Rationale

Painful problem, ML risk.
