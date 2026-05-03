---
type: "solopreneur_mvp"
id: "uz-mvp-033"
country: "UZ"
category: "ai_tool"
sector: "Agriculture & Water"
confidence_tier: "B"
weighted_total: 7.15
linked_trend: "[[Trends/uz-trend-033-speech-uzbek-asr|uz-trend-033-speech-uzbek-asr]]"
linked_decree: "[[Decrees/uz-pp-2025-099|UZ-PP-2025-099]]"
linked_donor: "[[Donors/wb-uz-agri-digital|WB-UZ-AGRI-DIGITAL]]"
linked_initiative: ""
verification: "L2_VERIFIED"
tags:
  - "country/uz"
  - "category/ai_tool"
  - "tier/B"
  - "sector/agriculture-water"
---

# FarmRecordsUZ

_Voice-to-text Telegram bot turning Uzbek-language voice notes into structured farm records (planting, spraying, harvest)_

## Pain point

Smallholder farmers don't keep records — limits credit access (banks require 2 years of records) and traceability for export buyers. They have phones but don't type. WB-UZ-AGRI-DIGITAL pushes for record-keeping. Speech-to-Uzbek ASR is now feasible per UP-189 sovereign LLM trend.

**Evidence**: https://www.worldbank.org/en/country/uzbekistan/projects


**Target customer**: Smallholder farmers 30-55 across Uzbekistan (cotton, wheat, vegetables) wanting bank credit or export contracts


## Monetization

- **Model**: freemium
- **Price point**: $3.00
- **Year-1 target**: $8,000
- **Year-3 target**: $60,000


## MVR plan (free_tool)

- **Build time**: 9 days
- **Build cost**: $80

**Steps:**
- [ ] Use Whisper or Yandex SpeechKit for Uzbek STT
- [ ] Telegram bot intake voice → structured table
- [ ] Auto-export PDF for bank/credit applications
- [ ] Free up to 20 records/mo, $3/mo unlimited
- [ ] Soft-launch via TBC Bank SME farm-credit Telegram


## Validation

- **Signal target**: 200 free + 30 paid users in 60 days
- **Window**: 60 days
- **Channels**: TBC Agri Telegram, agro.uz, Anorbank farmer Telegram


**Tech stack**: Whisper or Yandex SpeechKit, Telegram Bot, Supabase, PDF generator

**Capability required**: Russian + Uzbek-Latin + Cyrillic, STT API integration


## Moat potential

Bank-partnership integration (TBC, Anorbank, Hayot) for credit decisioning data; possible exit to one of them.

## Risks

- **Uzbek STT accuracy** — _Mitigation_: Use Yandex SpeechKit primary + Whisper fallback; correction loop
- **Low farmer adoption** — _Mitigation_: Bank-channel cross-promo with credit-line discount for users
- **Data privacy** — _Mitigation_: Customer-owned data, on-device option


## Scoring (weighted total: **7.15**)

| Axis | Score |
|---|---|
| Demand clarity (30%) | 7/10 |
| Speed to MVR (15%) | 7/10 |
| Monetization path (20%) | 7/10 |
| Founder solo feasibility (20%) | 7/10 |
| Local market fit (15%) | 8/10 |

### Rationale

Bank-credit unlock is the wedge; STT risk modest.
