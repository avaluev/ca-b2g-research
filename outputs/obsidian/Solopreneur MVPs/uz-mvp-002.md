---
type: "solopreneur_mvp"
id: "uz-mvp-002"
country: "UZ"
category: "managed_service"
sector: "Public Administration & e-Gov"
confidence_tier: "A"
weighted_total: 8.85
linked_trend: "[[Trends/uz-trend-001-epigu-ai-chatbot|uz-trend-001-epigu-ai-chatbot]]"
linked_decree: "[[Decrees/uz-pp-2025-286|UZ-PP-2025-286]]"
linked_donor: ""
linked_initiative: ""
verification: "L2_VERIFIED"
tags:
  - "country/uz"
  - "category/managed_service"
  - "tier/A"
  - "sector/public-administration-e-gov"
---

# FormFiller UZ

_Wizard-of-Oz service: send a photo of a Russian/Uzbek government form, get it back filled and ready for EPIGU upload in 4 hours_

## Pain point

Mahalla-level digitization (PP-286) is forcing 7M+ rural Uzbeks into EPIGU forms, but most cannot fill PDF forms in Russian-language administrative jargon. Currently they pay neighborhood notaries 50-100K UZS ($4-8) to retype data. There is no online equivalent.

**Evidence**: https://kun.uz/ru/news/2025/09/15/elektronnoe-pravitelstvo-mahalla


**Target customer**: Rural Fergana Valley adults aged 35-65 with smartphones but limited form-filling literacy, applying for pensions, land registration, and child allowances; secondary persona: Tashkent migrant workers returning from Russia who lost paper documents


## Monetization

- **Model**: services
- **Price point**: $3.00
- **Year-1 target**: $24,000
- **Year-3 target**: $150,000


## MVR plan (wizard_of_oz)

- **Build time**: 5 days
- **Build cost**: $200

**Steps:**
- [ ] Build Telegram bot intake: photo of form + photo of passport + voice description of need
- [ ] Set up Notion-based fulfillment dashboard, hire 1 part-time university student in Tashkent at $300/mo
- [ ] Stripe-style price card: 30,000 UZS for form-fill, 60,000 UZS for full submission to EPIGU
- [ ] Accept Click and Payme via Octobank acquiring
- [ ] Run $80 Instagram ad targeting Andijan/Namangan women 30-55 'oilamning hujjatlari'


## Validation

- **Signal target**: 30 paid orders in 21 days at $3-5 ACV; CAC < $1 via Telegram word-of-mouth
- **Window**: 30 days
- **Channels**: Andijan Telegram parent groups, Instagram Andijan women community, Mahalla WhatsApp networks via researcher contacts, spot.uz reader Telegram


**Tech stack**: Telegram Bot API, Notion, Click acquiring (octobank.uz), Google Drive for form library

**Capability required**: Russian + Uzbek-Latin, manage 1-2 part-time fulfillment ops, Click/Payme acquiring setup


## Moat potential

Library of 200+ pre-filled form templates becomes a productized SaaS in year 2; brand recognition with mahalla-level customers becomes referral moat.

## Risks

- **Notary lobby pushback or local police harassment** — _Mitigation_: Position as 'digital assistant' not legal service; partner with one mahalla aksakal as advisor
- **EPIGU API closes off third-party submission** — _Mitigation_: Pivot to form-filling-only and customer self-uploads
- **Personal data handling under ЗРУ-547** — _Mitigation_: Auto-delete forms 7 days after delivery; publish privacy policy in Russian


## Scoring (weighted total: **8.85**)

| Axis | Score |
|---|---|
| Demand clarity (30%) | 9/10 |
| Speed to MVR (15%) | 10/10 |
| Monetization path (20%) | 8/10 |
| Founder solo feasibility (20%) | 8/10 |
| Local market fit (15%) | 10/10 |

### Rationale

Cash-paying customers from day 1; 5-day Wizard-of-Oz build; mahalla decree creates urgency; price aligned with notary substitute.
