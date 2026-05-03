---
type: "solopreneur_mvp"
id: "uz-mvp-027"
country: "UZ"
category: "free_tool"
sector: "Agriculture & Water"
confidence_tier: "B"
weighted_total: 7.05
linked_trend: "[[Trends/uz-trend-014-precision-agri-satellite|uz-trend-014-precision-agri-satellite]]"
linked_decree: "[[Decrees/uz-pp-2025-099|UZ-PP-2025-099]]"
linked_donor: "[[Donors/adb-uz-water-digital|ADB-UZ-WATER-DIGITAL]]"
linked_initiative: ""
verification: "L2_VERIFIED"
tags:
  - "country/uz"
  - "category/free_tool"
  - "tier/B"
  - "sector/agriculture-water"
---

# WaterScheduleUZ

_SMS + Telegram alerts for irrigation-water release schedules from regional water associations, in Uzbek and Russian_

## Pain point

Water-user associations announce releases verbally or in WhatsApp groups. Farmers miss windows, fields suffer. ADB-UZ-WATER-DIGITAL is digitizing schedules but rollout is slow. Forum chatter on agro.uz shows persistent demand.

**Evidence**: https://www.adb.org/projects/country/uzb


**Target customer**: Smallholder farmers 30-65 in Bukhara, Khorezm, Karakalpakstan dependent on canal water, especially women-run plots with limited mobility


## Monetization

- **Model**: donation
- **Price point**: $0.00
- **Year-1 target**: $6,000
- **Year-3 target**: $50,000


## MVR plan (squeeze_page)

- **Build time**: 8 days
- **Build cost**: $100

**Steps:**
- [ ] Onboard 5 water-user associations as schedule sources via local researcher contacts
- [ ] Build Telegram + SMS bot using Twilio + UZ Mobiuz aggregator
- [ ] Per-canal pin and alert rule
- [ ] ADB grant pitch ($25K) for scaling to 50 WUAs
- [ ] Soft-launch in Khorezm farmer Telegram groups


## Validation

- **Signal target**: 500 farmer registrations across 3 oblasts in 60 days
- **Window**: 60 days
- **Channels**: Khorezm farmer Telegram, Karakalpakstan local activists, agro.uz forum


**Tech stack**: Telegram Bot, Twilio SMS, Supabase, Notion (WUA database)

**Capability required**: Russian + Uzbek-Latin, field outreach to WUAs, SMS aggregator setup


## Moat potential

Direct relationships with WUAs; donor scaling pathway; possible commercial tier for input dealers wanting to reach scheduled farmers.

## Risks

- **WUA cooperation inconsistent** — _Mitigation_: Volunteer mahalla aksakals + small honorarium for accurate input
- **Connectivity gaps in remote villages** — _Mitigation_: SMS fallback for non-Telegram users
- **Donor-grant timing** — _Mitigation_: Self-fund with input-dealer ads if grant delayed


## Scoring (weighted total: **7.05**)

| Axis | Score |
|---|---|
| Demand clarity (30%) | 8/10 |
| Speed to MVR (15%) | 7/10 |
| Monetization path (20%) | 5/10 |
| Founder solo feasibility (20%) | 6/10 |
| Local market fit (15%) | 9/10 |

### Rationale

Real impact, donor-grant viable, fulfillment requires field network.
