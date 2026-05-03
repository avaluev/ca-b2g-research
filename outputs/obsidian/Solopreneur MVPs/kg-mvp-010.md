---
type: "solopreneur_mvp"
id: "kg-mvp-010"
country: "KG"
category: "free_tool"
sector: "Public Administration & e-Gov"
confidence_tier: "B"
weighted_total: 6.3
linked_trend: "[[Trends/kg-trend-025-open-data-ai|kg-trend-025-open-data-ai]]"
linked_decree: "[[Decrees/kg-law-2025-178-digital-code|KG-LAW-2025-178-DIGITAL-CODE]]"
linked_donor: "[[Donors/wb-kg-open-data-p160933|WB-KG-OPEN-DATA-P160933]]"
linked_initiative: ""
verification: "L2_VERIFIED"
tags:
  - "country/kg"
  - "category/free_tool"
  - "tier/B"
  - "sector/public-administration-e-gov"
---

# OpenBudgetKG

_Free Telegram bot answering 'how much did my district receive?' from open data of Ministry of Finance KG_

## Pain point

Ministry of Finance KG publishes budget Excel files. Plain-language access missing. WB Open Data project supports.

**Evidence**: https://www.minfin.kg/


**Target customer**: Civic-active KG citizens 25-50; secondary: investigative journalists, ayil okmotu staff


## Monetization

- **Model**: donation
- **Price point**: $0.00
- **Year-1 target**: $5,000
- **Year-3 target**: $35,000


## MVR plan (squeeze_page)

- **Build time**: 9 days
- **Build cost**: $40

**Steps:**
- [ ] Aggregate Ministry of Finance + Treasury 2023-2025
- [ ] Build pgvector retrieval + GPT-4o for Russian/Kyrgyz queries
- [ ] Telegram bot
- [ ] WB grant pitch ($20K)
- [ ] Soft-launch via kaktus.media journalists + 24.kg


## Validation

- **Signal target**: 300 users + 1 journalist mention in 60 days
- **Window**: 60 days
- **Channels**: kaktus.media community, 24.kg, WB Open Data partners


**Tech stack**: Python + pgvector, Supabase, OpenAI, Telegram Bot

**Capability required**: Russian + Kyrgyz, data wrangling, grant writing


## Moat potential

Donor-grant continuity.

## Risks

- **Data structure changes** — _Mitigation_: Schema-detection + re-parse
- **Politically sensitive** — _Mitigation_: Stay descriptive
- **Low traction** — _Mitigation_: Donor partner co-marketing


## Scoring (weighted total: **6.30**)

| Axis | Score |
|---|---|
| Demand clarity (30%) | 6/10 |
| Speed to MVR (15%) | 8/10 |
| Monetization path (20%) | 4/10 |
| Founder solo feasibility (20%) | 7/10 |
| Local market fit (15%) | 7/10 |

### Rationale

Donor-driven, modest commercial.
