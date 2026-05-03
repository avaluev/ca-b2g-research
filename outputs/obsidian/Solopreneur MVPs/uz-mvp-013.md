---
type: "solopreneur_mvp"
id: "uz-mvp-013"
country: "UZ"
category: "ai_tool"
sector: "Public Administration & e-Gov"
confidence_tier: "A"
weighted_total: 8.05
linked_trend: "[[Trends/uz-trend-004-digital-id-mobile-myid|uz-trend-004-digital-id-mobile-myid]]"
linked_decree: "[[Decrees/uz-pp-2025-286|UZ-PP-2025-286]]"
linked_donor: ""
linked_initiative: ""
verification: "INFERRED"
tags:
  - "country/uz"
  - "category/ai_tool"
  - "tier/A"
  - "sector/public-administration-e-gov"
---

# PassportAppointmentBuddy

_Telegram alert when a Tashkent passport-issuance appointment slot opens within 7 days at your nearest office_

## Pain point

Internal-passport and biometric-passport appointments often have 3-6 week wait. Cancellations are constant but invisible. Citizens manually refresh the booking page. Forum threads on spot.uz request a 'cancellation alert' often.

**Evidence**: https://www.spot.uz/ru/2024/06/12/biometric-passport/


**Target customer**: Tashkent professionals 25-45 needing urgent passport for work travel, returning migrants, and university students applying for foreign exchange


## Monetization

- **Model**: one_time
- **Price point**: $5.00
- **Year-1 target**: $12,000
- **Year-3 target**: $80,000


## MVR plan (ad_booking)

- **Build time**: 6 days
- **Build cost**: $30

**Steps:**
- [ ] Reverse-engineer the booking-page slot endpoint via DevTools
- [ ] Cron-poll every 5 min, push delta via Telegram bot
- [ ] Offer free tier (1 office, 7-day window) and $5 premium (multi-office, 30-day window)
- [ ] Click micro-payment integration
- [ ] Soft-launch in spot.uz comments and Tashkent commuter Telegram


## Validation

- **Signal target**: 500 Telegram subscribers + 30 premium upgrades in 30 days
- **Window**: 30 days
- **Channels**: spot.uz, TBC SME Telegram, Tashkent commuter Telegram


**Tech stack**: Python + Playwright, Supabase, Telegram Bot API, Click acquiring

**Capability required**: scraping, Russian fluency


## Moat potential

Network effect via Telegram referrals; can extend to driver-license, marriage-registration appointments.

## Risks

- **Booking system anti-bot** — _Mitigation_: Switch to 'submit your booking page URL' user-driven model
- **Government bans third-party scrapers** — _Mitigation_: Re-position as 'browser extension' user owns
- **Low monetization** — _Mitigation_: Premium tier with multi-office support


## Scoring (weighted total: **8.05**)

| Axis | Score |
|---|---|
| Demand clarity (30%) | 9/10 |
| Speed to MVR (15%) | 9/10 |
| Monetization path (20%) | 7/10 |
| Founder solo feasibility (20%) | 8/10 |
| Local market fit (15%) | 8/10 |

### Rationale

Painful problem, fast build, decent monetization.
