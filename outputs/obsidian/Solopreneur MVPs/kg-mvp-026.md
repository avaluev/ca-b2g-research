---
type: "solopreneur_mvp"
id: "kg-mvp-026"
country: "KG"
category: "ai_tool"
sector: "Agriculture & Water"
confidence_tier: "A"
weighted_total: 7.65
linked_trend: "[[Trends/kg-trend-010-agri-ai-naryn|kg-trend-010-agri-ai-naryn]]"
linked_decree: "[[Decrees/kg-law-2025-178-digital-code|KG-LAW-2025-178-DIGITAL-CODE]]"
linked_donor: "[[Donors/wb-kg-p160230|WB-KG-P160230]]"
linked_initiative: ""
verification: "L2_VERIFIED"
tags:
  - "country/kg"
  - "category/ai_tool"
  - "tier/A"
  - "sector/agriculture-water"
---

# LivestockTrackKG

_Telegram-based livestock head + vaccination tracker for Kyrgyz smallholders, with bank-credit export_

## Pain point

Naryn, Issyk-Kul, Talas livestock farmers (200K+ households) track stock manually. Banks require records for credit. Veterinary services request vaccination history.

**Evidence**: https://kaktus.media/


**Target customer**: Smallholder livestock farmers 35-60 in Naryn, Issyk-Kul, Talas with 20-200 sheep/cattle


## Monetization

- **Model**: freemium
- **Price point**: $4.00
- **Year-1 target**: $10,000
- **Year-3 target**: $80,000


## MVR plan (landing_page)

- **Build time**: 9 days
- **Build cost**: $100

**Steps:**
- [ ] Telegram bot intake: voice for animal entries (Whisper Kyrgyz)
- [ ] Auto-export PDF for bank/vet
- [ ] Free up to 50 head, $4/mo unlimited
- [ ] Mbank/Optima subscription
- [ ] Soft-launch via Mbank rural agriculture Telegram + ayil okmotu


## Validation

- **Signal target**: 150 free + 30 paid in 60 days
- **Window**: 60 days
- **Channels**: Mbank agri Telegram, Naryn farmer Telegram, EU-GIZ ayil okmotu network


**Tech stack**: Whisper, Telegram Bot, Supabase, PDF generator, Mbank

**Capability required**: Russian + Kyrgyz, STT integration


## Moat potential

Bank credit unlock; possible exit to Mbank or Optima.

## Risks

- **Whisper Kyrgyz quality** — _Mitigation_: Yandex SpeechKit fallback + correction loop
- **Low adoption** — _Mitigation_: Bank-channel cross-promo
- **Privacy** — _Mitigation_: On-device option


## Scoring (weighted total: **7.65**)

| Axis | Score |
|---|---|
| Demand clarity (30%) | 8/10 |
| Speed to MVR (15%) | 7/10 |
| Monetization path (20%) | 7/10 |
| Founder solo feasibility (20%) | 7/10 |
| Local market fit (15%) | 9/10 |

### Rationale

Bank-credit wedge, KG-specific livestock focus.
