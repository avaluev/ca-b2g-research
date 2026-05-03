---
type: "solopreneur_mvp"
id: "uz-mvp-048"
country: "UZ"
category: "free_tool"
sector: "Health"
confidence_tier: "B"
weighted_total: 6.7
linked_trend: "[[Trends/uz-trend-009-eprescription-fraud|uz-trend-009-eprescription-fraud]]"
linked_decree: "[[Decrees/uz-pp-2024-311|UZ-PP-2024-311]]"
linked_donor: ""
linked_initiative: ""
verification: "INFERRED"
tags:
  - "country/uz"
  - "category/free_tool"
  - "tier/B"
  - "sector/health"
---

# OxygenPriceWatch

_Telegram alerts when oxygen, insulin, or chronic-care drug prices rise across Tashkent — for patients on long-term meds_

## Pain point

Drug prices fluctuate; patients on diabetes/asthma meds buy at peak. PP-311 will reimburse via SMI Fund but list price still matters for non-covered drugs.

**Evidence**: https://www.spot.uz/ru/category/biznes/health/


**Target customer**: Chronic-disease patients 35-70 in Tashkent on insulin, asthma inhalers, hypertension meds


## Monetization

- **Model**: freemium
- **Price point**: $2.00
- **Year-1 target**: $5,000
- **Year-3 target**: $40,000


## MVR plan (free_tool)

- **Build time**: 7 days
- **Build cost**: $40

**Steps:**
- [ ] Scrape 5 major pharmacy chain price lists daily
- [ ] Telegram bot intake: drugs to watch
- [ ] Push price-drop alerts
- [ ] $2/mo for unlimited drugs + SMS alerts
- [ ] Soft-launch in spot.uz health + Tashkent senior Telegram


## Validation

- **Signal target**: 200 users + 20 paid in 60 days
- **Window**: 60 days
- **Channels**: spot.uz health, Tashkent senior Telegram, TBC family


**Tech stack**: Python + scraping, Telegram Bot, Twilio SMS, Click

**Capability required**: Russian, scraping, domain familiarity


## Moat potential

Price-history dataset becomes a benchmark; possible licensing to SMI Fund.

## Risks

- **Pharmacies block scrapers** — _Mitigation_: Rotate user agents; partner with PharmacyShelfUZ
- **Low willingness to pay** — _Mitigation_: Bundle with PharmacyDirectoryUZ
- **Government competitor** — _Mitigation_: Lean on Telegram-native UX


## Scoring (weighted total: **6.70**)

| Axis | Score |
|---|---|
| Demand clarity (30%) | 6/10 |
| Speed to MVR (15%) | 8/10 |
| Monetization path (20%) | 5/10 |
| Founder solo feasibility (20%) | 8/10 |
| Local market fit (15%) | 8/10 |

### Rationale

Niche but useful, low cost build.
