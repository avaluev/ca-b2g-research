---
type: "solopreneur_mvp"
id: "kg-mvp-047"
country: "KG"
category: "ai_tool"
sector: "Health"
confidence_tier: "B"
weighted_total: 6.3
linked_trend: "[[Trends/kg-trend-006-ehealth-kg|kg-trend-006-ehealth-kg]]"
linked_decree: "[[Decrees/kg-law-2025-178-digital-code|KG-LAW-2025-178-DIGITAL-CODE]]"
linked_donor: ""
linked_initiative: ""
verification: "INFERRED"
tags:
  - "country/kg"
  - "category/ai_tool"
  - "tier/B"
  - "sector/health"
---

# PrescriptionScannerKG

_Free Telegram tool turning photo of doctor's handwritten prescription into structured pharmacy-ready text in Russian/Kyrgyz_

## Pain point

Hand-written prescriptions illegible. Patients arrive at pharmacy unsure of dose. KG MoH transitioning to e-prescriptions but uneven.

**Evidence**: https://kaktus.media/


**Target customer**: Bishkek patients 30-55, especially elderly + visually impaired


## Monetization

- **Model**: freemium
- **Price point**: $1.00
- **Year-1 target**: $4,000
- **Year-3 target**: $35,000


## MVR plan (free_tool)

- **Build time**: 9 days
- **Build cost**: $100

**Steps:**
- [ ] Train CRNN OCR on 200 sample handwritten
- [ ] Telegram bot + GPT-4o clarification
- [ ] Output drug, dose, frequency Russian + Kyrgyz
- [ ] Free 5/mo, $1/mo unlimited
- [ ] Soft-launch via Mbank family + 24.kg health


## Validation

- **Signal target**: 200 scans + 25 paid in 60 days
- **Window**: 60 days
- **Channels**: Mbank family, 24.kg health, Bishkek senior Telegram


**Tech stack**: CRNN + GPT-4o, Telegram Bot, Mbank

**Capability required**: Russian + Kyrgyz, ML basics, medical partner


## Moat potential

Prescription dataset; partner with PharmacyShelfKG.

## Risks

- **Misreading liability** — _Mitigation_: Always show original + 'verify with pharmacist'
- **OCR fragility** — _Mitigation_: Hybrid + GPT vision
- **E-prescription replaces** — _Mitigation_: Pivot to e-prescription explainer


## Scoring (weighted total: **6.30**)

| Axis | Score |
|---|---|
| Demand clarity (30%) | 6/10 |
| Speed to MVR (15%) | 7/10 |
| Monetization path (20%) | 5/10 |
| Founder solo feasibility (20%) | 7/10 |
| Local market fit (15%) | 7/10 |

### Rationale

Real pain, transitional.
