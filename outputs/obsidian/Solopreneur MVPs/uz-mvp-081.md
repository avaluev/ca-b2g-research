---
type: "solopreneur_mvp"
id: "uz-mvp-081"
country: "UZ"
category: "free_tool"
sector: "Transport & Urban"
confidence_tier: "B"
weighted_total: 6.55
linked_trend: "[[Trends/uz-trend-018-smart-traffic-tashkent|uz-trend-018-smart-traffic-tashkent]]"
linked_decree: "[[Decrees/uz-up-2025-189|UZ-UP-2025-189]]"
linked_donor: ""
linked_initiative: ""
verification: "INFERRED"
tags:
  - "country/uz"
  - "category/free_tool"
  - "tier/B"
  - "sector/transport-urban"
---

# TashkentParkingMap

_Free Telegram bot showing real-time legal parking availability across Tashkent, with violation-fine alerts_

## Pain point

Tashkent has 2M+ vehicles, parking enforcement uneven. Drivers fined 200K-500K UZS for unclear violations. Spot.uz transport publishes parking guide reactively.

**Evidence**: https://www.spot.uz/ru/category/biznes/transport/


**Target customer**: Tashkent drivers 25-55 — daily commuters + weekend shoppers; secondary: out-of-town visitors


## Monetization

- **Model**: freemium
- **Price point**: $3.00
- **Year-1 target**: $6,000
- **Year-3 target**: $50,000


## MVR plan (ad_booking)

- **Build time**: 7 days
- **Build cost**: $50

**Steps:**
- [ ] Scrape DDA traffic-violation data + parking signage rules
- [ ] Telegram bot intake: pin destination
- [ ] Output: closest legal parking + estimated fine if illegal
- [ ] $3/mo for unlimited + history
- [ ] Soft-launch in spot.uz + Tashkent drivers Telegram


## Validation

- **Signal target**: 300 free + 30 paid in 60 days
- **Window**: 60 days
- **Channels**: spot.uz transport, Tashkent drivers Telegram, TBC SME mobility


**Tech stack**: Python, Mapbox, Telegram Bot, Click

**Capability required**: Russian, GIS basics, scraping


## Moat potential

Parking + violation dataset; possible OEM to navigation apps.

## Risks

- **Data limited** — _Mitigation_: Crowdsource from users
- **Govt smart-traffic absorbs** — _Mitigation_: Lean on UX speed
- **Low conversion** — _Mitigation_: Bundle with TashkentTaxiRateCheck


## Scoring (weighted total: **6.55**)

| Axis | Score |
|---|---|
| Demand clarity (30%) | 6/10 |
| Speed to MVR (15%) | 8/10 |
| Monetization path (20%) | 5/10 |
| Founder solo feasibility (20%) | 8/10 |
| Local market fit (15%) | 7/10 |

### Rationale

Useful, modest demand.
