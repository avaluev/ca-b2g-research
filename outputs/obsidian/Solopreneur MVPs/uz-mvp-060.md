---
type: "solopreneur_mvp"
id: "uz-mvp-060"
country: "UZ"
category: "free_tool"
sector: "Finance & Fiscal"
confidence_tier: "B"
weighted_total: 7.65
linked_trend: "[[Trends/uz-trend-023-aml-ai-state-banks|uz-trend-023-aml-ai-state-banks]]"
linked_decree: "[[Decrees/uz-pp-2024-038-cybersec-banking|UZ-PP-2024-038-CYBERSEC-BANKING]]"
linked_donor: ""
linked_initiative: ""
verification: "L2_VERIFIED"
tags:
  - "country/uz"
  - "category/free_tool"
  - "tier/B"
  - "sector/finance-fiscal"
---

# AMLAlertUZ

_Free Telegram tool sending Uzbek SME owners weekly digest of new AML/Sanctions list updates affecting their business partners_

## Pain point

Uzbek SMEs deal with Russian/Kazakh counterparts post-2022 sanctions; bank scrutiny is rising. State Bank AML compliance (PP-038) flags transfers; SMEs caught flat-footed.

**Evidence**: https://www.spot.uz/ru/category/biznes/finance/


**Target customer**: Tashkent and Samarkand SMEs trading with Russia, Kazakhstan, China, especially logistics and electronics importers


## Monetization

- **Model**: freemium
- **Price point**: $12.00
- **Year-1 target**: $8,000
- **Year-3 target**: $70,000


## MVR plan (free_tool)

- **Build time**: 6 days
- **Build cost**: $40

**Steps:**
- [ ] Scrape OFAC, EU, OFSI sanctions lists daily
- [ ] Telegram bot intake: list of business-partner names/INNs
- [ ] Push alerts on matches
- [ ] Free 3 partners, $12/mo for unlimited
- [ ] Soft-launch in TBC SME importer + uzcloud Slack


## Validation

- **Signal target**: 100 free + 15 paid in 60 days
- **Window**: 60 days
- **Channels**: TBC SME importer, uzcloud Slack, ICT Week 2026 fintech


**Tech stack**: Python scraping, Telegram Bot, Click

**Capability required**: Russian + English, Python, compliance domain familiarity


## Moat potential

Sanctions data + UZ company database compounds; possible licensing to state banks AML units.

## Risks

- **False positives** — _Mitigation_: Confidence-scoring + human review for premium
- **Compliance liability** — _Mitigation_: Educational disclaimer
- **Government competitor** — _Mitigation_: Lean on speed + Telegram-native


## Scoring (weighted total: **7.65**)

| Axis | Score |
|---|---|
| Demand clarity (30%) | 7/10 |
| Speed to MVR (15%) | 9/10 |
| Monetization path (20%) | 7/10 |
| Founder solo feasibility (20%) | 8/10 |
| Local market fit (15%) | 8/10 |

### Rationale

Russian-CIS substitution play, B2B SME audience.
