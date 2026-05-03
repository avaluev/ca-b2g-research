---
type: "solopreneur_mvp"
id: "uz-mvp-036"
country: "UZ"
category: "saas"
sector: "Health"
confidence_tier: "A"
weighted_total: 7.65
linked_trend: "[[Trends/uz-trend-009-eprescription-fraud|uz-trend-009-eprescription-fraud]]"
linked_decree: "[[Decrees/uz-pp-2023-415|UZ-PP-2023-415]]"
linked_donor: "[[Donors/wb-uz-health-p178562|WB-UZ-HEALTH-P178562]]"
linked_initiative: ""
verification: "L2_VERIFIED"
tags:
  - "country/uz"
  - "category/saas"
  - "tier/A"
  - "sector/health"
---

# PharmacyShelfUZ

_SaaS for independent Uzbek pharmacies: photograph your shelf, get OCR-based stock list and reorder alerts_

## Pain point

12,000+ independent pharmacies in Uzbekistan track stock manually. State Medical Insurance (PP-415, UP-088) requires e-prescription compliance starting 2026 — pharmacies need stock-tracking software but enterprise solutions cost $500+/mo.

**Evidence**: https://www.gazeta.uz/ru/list/health/


**Target customer**: Independent pharmacy owners 35-55 in Tashkent, Samarkand, Andijan with 1-3 outlets, currently using paper or Excel


## Monetization

- **Model**: subscription
- **Price point**: $25.00
- **Year-1 target**: $25,000
- **Year-3 target**: $250,000


## MVR plan (landing_page)

- **Build time**: 10 days
- **Build cost**: $150

**Steps:**
- [ ] Build OCR pipeline (Tesseract + EasyOCR) for Russian + Uzbek-Latin labels
- [ ] Mobile-friendly web app for stock tracking + reorder
- [ ] Carrd landing page + 14-day free trial
- [ ] Click subscription billing 300,000 UZS/mo
- [ ] Soft-launch via Apteka Plus distributor partner Telegram


## Validation

- **Signal target**: 20 pharmacies on free trial, 5 paid in 60 days
- **Window**: 60 days
- **Channels**: pharmacy distributor Telegram, TBC SME health-vertical Telegram, ICT Week 2026 health track


**Tech stack**: Python OCR, Next.js + Vercel, Supabase, Click subscription

**Capability required**: Russian + Uzbek-Latin, OCR engineering, B2B sales


## Moat potential

Stock + sales data is monetizable to pharma distributors and State Medical Insurance Fund; possible white-label to large distributor.

## Risks

- **OCR accuracy on local labels** — _Mitigation_: Manual correction layer; user feedback loop
- **Pharmacy chains pull customers** — _Mitigation_: Focus on independents + small groups
- **Compliance shifts** — _Mitigation_: Stay close to State Medical Insurance Fund updates


## Scoring (weighted total: **7.65**)

| Axis | Score |
|---|---|
| Demand clarity (30%) | 8/10 |
| Speed to MVR (15%) | 7/10 |
| Monetization path (20%) | 8/10 |
| Founder solo feasibility (20%) | 7/10 |
| Local market fit (15%) | 8/10 |

### Rationale

Decree + insurance tailwind, B2B SaaS path, OCR is solvable.
