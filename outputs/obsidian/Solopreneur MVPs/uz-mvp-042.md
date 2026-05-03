---
type: "solopreneur_mvp"
id: "uz-mvp-042"
country: "UZ"
category: "free_tool"
sector: "Health"
confidence_tier: "B"
weighted_total: 6.7
linked_trend: "[[Trends/uz-trend-008-ehealth-ai-diagnostics|uz-trend-008-ehealth-ai-diagnostics]]"
linked_decree: "[[Decrees/uz-pp-2023-415|UZ-PP-2023-415]]"
linked_donor: "[[Donors/unicef-uz-edtech-learning|UNICEF-UZ-EDTECH-LEARNING]]"
linked_initiative: ""
verification: "L2_VERIFIED"
tags:
  - "country/uz"
  - "category/free_tool"
  - "tier/B"
  - "sector/health"
---

# VaccineRecordUZ

_Free Telegram tool: upload child vaccine card, get next-due alerts and digital backup; family-friendly Russian/Uzbek_

## Pain point

Paper vaccination cards get lost. Parents miss boosters. Polikliniki schedules vary by region. UNICEF Uzbekistan supports immunization tracking.

**Evidence**: https://www.unicef.org/uzbekistan/


**Target customer**: Tashkent and Fergana parents 25-40 with under-5 children, especially first-time mothers and migrant returnees


## Monetization

- **Model**: donation
- **Price point**: $0.00
- **Year-1 target**: $5,000
- **Year-3 target**: $40,000


## MVR plan (free_tool)

- **Build time**: 8 days
- **Build cost**: $60

**Steps:**
- [ ] Use Tesseract OCR for vaccine card capture
- [ ] Telegram bot intake: photo + child DOB
- [ ] Push notification 7 days before next vaccine
- [ ] UNICEF grant pitch ($25K) for nationwide rollout
- [ ] Soft-launch in Tashkent parent Telegram groups


## Validation

- **Signal target**: 500 children registered in 60 days
- **Window**: 60 days
- **Channels**: Tashkent parent Telegram, Andijan parent groups, UNICEF Uzbekistan partners


**Tech stack**: Telegram Bot, Tesseract OCR, Supabase

**Capability required**: Russian + Uzbek-Latin, OCR engineering, child-health domain familiarity


## Moat potential

Donor-grant continuity (UNICEF, WHO); possible OEM to State Medical Insurance Fund + Ministry of Health.

## Risks

- **OCR accuracy varies** — _Mitigation_: Manual review for edge cases
- **Privacy concerns** — _Mitigation_: ЗРУ-547 review; minimal data retention
- **Government competitor** — _Mitigation_: Lean on UX speed and partner with one polikliniki for branding


## Scoring (weighted total: **6.70**)

| Axis | Score |
|---|---|
| Demand clarity (30%) | 7/10 |
| Speed to MVR (15%) | 8/10 |
| Monetization path (20%) | 4/10 |
| Founder solo feasibility (20%) | 7/10 |
| Local market fit (15%) | 8/10 |

### Rationale

Civic value, donor-grant viable, weak commercial.
