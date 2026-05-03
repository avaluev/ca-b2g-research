---
type: "solopreneur_mvp"
id: "uz-mvp-008"
country: "UZ"
category: "free_tool"
sector: "Public Administration & e-Gov"
confidence_tier: "A"
weighted_total: 7.65
linked_trend: "[[Trends/uz-trend-002-epigu-workflow-automation|uz-trend-002-epigu-workflow-automation]]"
linked_decree: "[[Decrees/uz-pp-2025-286|UZ-PP-2025-286]]"
linked_donor: ""
linked_initiative: ""
verification: "INFERRED"
tags:
  - "country/uz"
  - "category/free_tool"
  - "tier/A"
  - "sector/public-administration-e-gov"
---

# EPIGUStatusBot

_Telegram bot that pings you when your EPIGU application moves status; auto-detects delays beyond legal SLA_

## Pain point

EPIGU does not push status notifications. Citizens log in repeatedly to check. Service-level SLAs (per Public Services Agency standards) are ignored without enforcement. Forum threads on spot.uz show 50+ daily 'статус не меняется' complaints.

**Evidence**: https://my.gov.uz/ru


**Target customer**: EPIGU power users — university applicants checking diploma certifications, real-estate agents tracking land registration, returning migrants applying for documents


## Monetization

- **Model**: freemium
- **Price point**: $1.00
- **Year-1 target**: $10,000
- **Year-3 target**: $70,000


## MVR plan (squeeze_page)

- **Build time**: 6 days
- **Build cost**: $30

**Steps:**
- [ ] Reverse-engineer EPIGU public-status URL pattern
- [ ] Telegram bot intake: paste application reference + phone
- [ ] Poll status every 4 hours, push delta to user in Russian/Uzbek
- [ ] Add 'SLA exceeded' alert with Public Services Agency complaint form link
- [ ] Soft-launch in spot.uz comments and IT Park UZ


## Validation

- **Signal target**: 800 active applications tracked in 30 days
- **Window**: 30 days
- **Channels**: spot.uz Telegram, kun.uz Telegram, uzCloud Slack, IT Park UZ Telegram


**Tech stack**: Python + Playwright, Supabase, Telegram Bot API

**Capability required**: Russian + Uzbek, scraping with Playwright, Telegram bot


## Moat potential

Aggregated SLA data becomes leverage with Public Services Agency for paid integration; likely acquisition target by EPIGU itself.

## Risks

- **EPIGU adds anti-bot protection** — _Mitigation_: Pivot to user-pasted screenshots with OCR
- **TOS-violation accusation** — _Mitigation_: Use the citizen's own credentials only, request explicit authorization, publish T&Cs
- **Low monetization** — _Mitigation_: Premium SLA-complaint auto-filer at $5/case


## Scoring (weighted total: **7.65**)

| Axis | Score |
|---|---|
| Demand clarity (30%) | 8/10 |
| Speed to MVR (15%) | 9/10 |
| Monetization path (20%) | 5/10 |
| Founder solo feasibility (20%) | 8/10 |
| Local market fit (15%) | 9/10 |

### Rationale

Real pain, modest monetization, valuable data.
