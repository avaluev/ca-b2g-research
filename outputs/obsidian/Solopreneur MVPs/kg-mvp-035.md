---
type: "solopreneur_mvp"
id: "kg-mvp-035"
country: "KG"
category: "ai_tool"
sector: "Agriculture & Water"
confidence_tier: "B"
weighted_total: 7.15
linked_trend: "[[Trends/kg-trend-024-sovereign-llm-kyrgyz|kg-trend-024-sovereign-llm-kyrgyz]]"
linked_decree: "[[Decrees/kg-law-2025-178-digital-code|KG-LAW-2025-178-DIGITAL-CODE]]"
linked_donor: "[[Donors/wb-kg-p160230|WB-KG-P160230]]"
linked_initiative: ""
verification: "L2_VERIFIED"
tags:
  - "country/kg"
  - "category/ai_tool"
  - "tier/B"
  - "sector/agriculture-water"
---

# FarmRecordsKG

_Voice-to-text Telegram bot turning Kyrgyz voice notes into structured farm records (planting, spraying, harvest)_

## Pain point

Smallholder farmers don't keep records — limits credit + traceability for export. WB Digital CASA pushes record-keeping. Kyrgyz STT now feasible.

**Evidence**: https://www.worldbank.org/en/country/kyrgyzrepublic


**Target customer**: Smallholder farmers 30-55 across KG (livestock, wheat, vegetables) wanting bank credit or export contracts


## Monetization

- **Model**: freemium
- **Price point**: $3.00
- **Year-1 target**: $7,000
- **Year-3 target**: $55,000


## MVR plan (free_tool)

- **Build time**: 9 days
- **Build cost**: $80

**Steps:**
- [ ] Whisper or Yandex SpeechKit for Kyrgyz STT
- [ ] Telegram bot voice → structured table
- [ ] Auto-export PDF for bank/credit
- [ ] Free up to 20 records/mo, $3/mo unlimited
- [ ] Soft-launch via Mbank rural agriculture Telegram


## Validation

- **Signal target**: 200 free + 30 paid in 60 days
- **Window**: 60 days
- **Channels**: Mbank agri Telegram, Naryn farmer Telegram, kaktus.media


**Tech stack**: Whisper / Yandex SpeechKit, Telegram Bot, Supabase, PDF generator

**Capability required**: Russian + Kyrgyz, STT integration


## Moat potential

Bank-credit data; possible exit to Mbank, Optima.

## Risks

- **Kyrgyz STT accuracy** — _Mitigation_: Yandex primary + Whisper fallback
- **Low adoption** — _Mitigation_: Bank-channel cross-promo
- **Privacy** — _Mitigation_: On-device option


## Scoring (weighted total: **7.15**)

| Axis | Score |
|---|---|
| Demand clarity (30%) | 7/10 |
| Speed to MVR (15%) | 7/10 |
| Monetization path (20%) | 7/10 |
| Founder solo feasibility (20%) | 7/10 |
| Local market fit (15%) | 8/10 |

### Rationale

Bank-credit unlock; STT risk modest.
