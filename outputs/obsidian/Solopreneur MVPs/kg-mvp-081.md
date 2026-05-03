---
type: "solopreneur_mvp"
id: "kg-mvp-081"
country: "KG"
category: "free_tool"
sector: "Transport & Urban"
confidence_tier: "C"
weighted_total: 6.05
linked_trend: "[[Trends/kg-trend-013-smart-traffic-bishkek|kg-trend-013-smart-traffic-bishkek]]"
linked_decree: "[[Decrees/kg-law-2025-178-digital-code|KG-LAW-2025-178-DIGITAL-CODE]]"
linked_donor: ""
linked_initiative: ""
verification: "INFERRED"
tags:
  - "country/kg"
  - "category/free_tool"
  - "tier/C"
  - "sector/transport-urban"
---

# BishkekParkingMap

_Free Telegram bot showing real-time legal parking + violation-fine alerts in Bishkek_

## Pain point

Bishkek has 300K+ vehicles, parking enforcement uneven. Drivers fined for unclear violations.

**Evidence**: https://kaktus.media/


**Target customer**: Bishkek drivers 25-55


## Monetization

- **Model**: freemium
- **Price point**: $3.00
- **Year-1 target**: $4,000
- **Year-3 target**: $35,000


## MVR plan (ad_booking)

- **Build time**: 7 days
- **Build cost**: $50

**Steps:**
- [ ] Scrape DDA + parking signage rules
- [ ] Telegram bot intake pin destination
- [ ] Output closest legal parking + fine estimate
- [ ] $3/mo unlimited
- [ ] Soft-launch in kaktus.media transport + Bishkek drivers


## Validation

- **Signal target**: 200 free + 25 paid in 60 days
- **Window**: 60 days
- **Channels**: kaktus.media transport, Bishkek drivers Telegram


**Tech stack**: Python, Mapbox, Telegram Bot, Mbank

**Capability required**: Russian, GIS basics


## Moat potential

Parking dataset; OEM to navigation.

## Risks

- **Data limited** — _Mitigation_: Crowdsource
- **Govt smart-traffic** — _Mitigation_: UX speed
- **Conversion** — _Mitigation_: Bundle BishkekTaxiRateCheck


## Scoring (weighted total: **6.05**)

| Axis | Score |
|---|---|
| Demand clarity (30%) | 5/10 |
| Speed to MVR (15%) | 8/10 |
| Monetization path (20%) | 4/10 |
| Founder solo feasibility (20%) | 8/10 |
| Local market fit (15%) | 7/10 |

### Rationale

Useful, weak demand.
