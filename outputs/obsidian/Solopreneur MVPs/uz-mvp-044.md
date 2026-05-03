---
type: "solopreneur_mvp"
id: "uz-mvp-044"
country: "UZ"
category: "ai_tool"
sector: "Health"
confidence_tier: "B"
weighted_total: 6.45
linked_trend: "[[Trends/uz-trend-009-eprescription-fraud|uz-trend-009-eprescription-fraud]]"
linked_decree: "[[Decrees/uz-pp-2023-415|UZ-PP-2023-415]]"
linked_donor: "[[Donors/wb-uz-health-p178562|WB-UZ-HEALTH-P178562]]"
linked_initiative: ""
verification: "INFERRED"
tags:
  - "country/uz"
  - "category/ai_tool"
  - "tier/B"
  - "sector/health"
---

# PrescriptionScannerUZ

_Free Telegram tool that turns photo of doctor's handwritten prescription into structured pharmacy-ready text in Russian/Uzbek_

## Pain point

Hand-written prescriptions are illegible. Patients arrive at pharmacy unsure of dose. PP-415 pushes e-prescriptions but rollout is uneven; transitional confusion creates demand for OCR helpers.

**Evidence**: https://kun.uz/ru/news/2024/06/12/zdorovie-uzbekistan


**Target customer**: Tashkent and Samarkand patients 30-55, especially elderly and visually-impaired who need read-aloud


## Monetization

- **Model**: freemium
- **Price point**: $1.00
- **Year-1 target**: $6,000
- **Year-3 target**: $50,000


## MVR plan (free_tool)

- **Build time**: 9 days
- **Build cost**: $100

**Steps:**
- [ ] Train CRNN OCR on 200 sample handwritten prescriptions
- [ ] Telegram bot intake + GPT-4o for clarification
- [ ] Output: drug, dose, frequency in Russian + Uzbek
- [ ] Free 5 prescriptions/mo, $1/mo unlimited
- [ ] Soft-launch via spot.uz health + Tashkent senior Telegram


## Validation

- **Signal target**: 300 scans + 30 paid in 60 days
- **Window**: 60 days
- **Channels**: spot.uz health, Tashkent senior Telegram, TBC family Telegram


**Tech stack**: CRNN + GPT-4o, Telegram Bot, Click

**Capability required**: Russian + Uzbek-Latin, ML basics, medical-content review partner


## Moat potential

Prescription dataset + medication intent compounds; partner with PharmacyShelfUZ.

## Risks

- **Misreading liability** — _Mitigation_: Always-show original photo + 'verify with pharmacist' disclaimer
- **OCR fragility on handwriting** — _Mitigation_: Hybrid OCR + GPT vision
- **E-prescription replaces need** — _Mitigation_: Position transitional; pivot to e-prescription explainer


## Scoring (weighted total: **6.45**)

| Axis | Score |
|---|---|
| Demand clarity (30%) | 6/10 |
| Speed to MVR (15%) | 7/10 |
| Monetization path (20%) | 5/10 |
| Founder solo feasibility (20%) | 7/10 |
| Local market fit (15%) | 8/10 |

### Rationale

Real pain, transitional opportunity.
