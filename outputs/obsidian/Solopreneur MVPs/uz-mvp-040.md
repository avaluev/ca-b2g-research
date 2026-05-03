---
type: "solopreneur_mvp"
id: "uz-mvp-040"
country: "UZ"
category: "ai_tool"
sector: "Health"
confidence_tier: "B"
weighted_total: 6.7
linked_trend: "[[Trends/uz-trend-008-ehealth-ai-diagnostics|uz-trend-008-ehealth-ai-diagnostics]]"
linked_decree: "[[Decrees/uz-pp-2023-415|UZ-PP-2023-415]]"
linked_donor: "[[Donors/wb-uz-health-p178562|WB-UZ-HEALTH-P178562]]"
linked_initiative: ""
verification: "L2_VERIFIED"
tags:
  - "country/uz"
  - "category/ai_tool"
  - "tier/B"
  - "sector/health"
---

# SymptomCheckerUZ

_Free Uzbek-language symptom checker delivering triage levels (self-care / GP / ER) and nearest clinic_

## Pain point

Lack of Uzbek-language symptom-checker forces patients to either over-use ERs or under-treat. WB-UZ-HEALTH-P178562 supports digital health; PP-415 mandates digital diagnostic tools. ChatGPT use is rising but unsafe without clinical guardrails.

**Evidence**: https://kun.uz/ru/news/2024/06/12/zdorovie-uzbekistan


**Target customer**: Adult Uzbeks 25-55 with symptoms but no immediate access to GP, especially urban working parents


## Monetization

- **Model**: freemium
- **Price point**: $2.00
- **Year-1 target**: $9,000
- **Year-3 target**: $80,000


## MVR plan (free_tool)

- **Build time**: 12 days
- **Build cost**: $200

**Steps:**
- [ ] Use Infermedica or open MedQA dataset + Uzbek translation layer
- [ ] Telegram bot + voice input via Whisper
- [ ] Free 3 checks/week, $2/mo unlimited + clinic referral
- [ ] Affiliate to ClinicAppointmentUZ
- [ ] Soft-launch in TBC family Telegram + spot.uz health chat


## Validation

- **Signal target**: 500 checks + 30 paid in 60 days
- **Window**: 60 days
- **Channels**: TBC family Telegram, spot.uz health, Andijan parent groups


**Tech stack**: Infermedica API or Med-Llama, Whisper, Telegram Bot, Click

**Capability required**: Russian + Uzbek-Latin, medical-content review (partner doctor), API integration


## Moat potential

Symptom data + outcome feedback compounds; clinic-referral network; partner with State Medical Insurance.

## Risks

- **Medical liability** — _Mitigation_: ЗРУ-1115 AI Law compliance; disclaimer; partner doctor review
- **Inaccurate triage** — _Mitigation_: Conservative defaults; always-recommend ER for red flags
- **Trust gap** — _Mitigation_: Position with clinic partner; verified-doctor endorsements


## Scoring (weighted total: **6.70**)

| Axis | Score |
|---|---|
| Demand clarity (30%) | 7/10 |
| Speed to MVR (15%) | 6/10 |
| Monetization path (20%) | 7/10 |
| Founder solo feasibility (20%) | 6/10 |
| Local market fit (15%) | 7/10 |

### Rationale

Big upside, regulatory + medical risk requires careful build.
