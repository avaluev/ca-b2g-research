---
type: "solopreneur_mvp"
id: "uz-mvp-037"
country: "UZ"
category: "free_tool"
sector: "Health"
confidence_tier: "B"
weighted_total: 7.4
linked_trend: "[[Trends/uz-trend-010-telemedicine-ai-triage|uz-trend-010-telemedicine-ai-triage]]"
linked_decree: "[[Decrees/uz-pp-2023-415|UZ-PP-2023-415]]"
linked_donor: ""
linked_initiative: ""
verification: "L2_VERIFIED"
tags:
  - "country/uz"
  - "category/free_tool"
  - "tier/B"
  - "sector/health"
---

# MedReminderUZ

_Free Telegram bot reminding patients to take meds, with Russian/Uzbek voice prompts and family caregiver loop_

## Pain point

Chronic-disease patients (hypertension, diabetes) miss doses. Adult children manage parents' meds remotely. Existing reminder apps lack Uzbek and don't loop in family.

**Evidence**: https://kun.uz/ru/news/2024/06/12/zdorovie-uzbekistan


**Target customer**: Adult children 30-50 caring for elderly parents (60-85) with chronic conditions; patients themselves


## Monetization

- **Model**: freemium
- **Price point**: $2.00
- **Year-1 target**: $7,000
- **Year-3 target**: $60,000


## MVR plan (free_tool)

- **Build time**: 7 days
- **Build cost**: $60

**Steps:**
- [ ] Telegram bot intake: meds + schedule + caregiver phone
- [ ] Voice reminder via OpenAI TTS in Uzbek + Russian
- [ ] Family-loop SMS via Twilio when missed
- [ ] Free up to 2 patients, $2/mo unlimited
- [ ] Soft-launch via TBC family banking Telegram


## Validation

- **Signal target**: 300 reminders + 30 paid in 60 days
- **Window**: 60 days
- **Channels**: TBC family Telegram, Andijan parent groups, Tashkent caregiver communities


**Tech stack**: Telegram Bot, OpenAI TTS, Twilio SMS, Supabase

**Capability required**: Russian + Uzbek-Latin, TTS integration


## Moat potential

Adherence data becomes valuable to State Medical Insurance Fund + pharmaceutical companies (anonymized).

## Risks

- **HIPAA-equivalent compliance** — _Mitigation_: ЗРУ-547 review; minimal data retention
- **Adoption friction with elderly** — _Mitigation_: Caregiver-driven onboarding; voice-only mode
- **Low willingness to pay** — _Mitigation_: B2B pivot to clinics


## Scoring (weighted total: **7.40**)

| Axis | Score |
|---|---|
| Demand clarity (30%) | 7/10 |
| Speed to MVR (15%) | 9/10 |
| Monetization path (20%) | 6/10 |
| Founder solo feasibility (20%) | 8/10 |
| Local market fit (15%) | 8/10 |

### Rationale

Caregiver-driven adoption is the wedge; bilingual voice is differentiator.
