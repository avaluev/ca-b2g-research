---
type: "solopreneur_mvp"
id: "uz-mvp-080"
country: "UZ"
category: "free_tool"
sector: "Transport & Urban"
confidence_tier: "B"
weighted_total: 6.65
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

# TashkentTaxiRateCheck

_Free tool: get fair Yandex Go and local taxi rates for Tashkent routes, exposing surge pricing rip-offs_

## Pain point

Yandex Go and Maxim use surge pricing — locals + tourists overpay. Spot.uz has covered driver overcharging. No transparent rate calculator.

**Evidence**: https://www.spot.uz/ru/category/biznes/transport/


**Target customer**: Tashkent commuters 25-50 + tourists making 10+ taxi trips/month


## Monetization

- **Model**: ad
- **Price point**: $50.00
- **Year-1 target**: $5,000
- **Year-3 target**: $40,000


## MVR plan (ad_booking)

- **Build time**: 6 days
- **Build cost**: $30

**Steps:**
- [ ] Reverse-engineer Yandex Go API or use scraping
- [ ] Web app + Telegram bot: enter origin + destination, get price quote
- [ ] Sponsored slot for one taxi alternative (Tap, Pulsar)
- [ ] Soft-launch in spot.uz transport chat + Tashkent commuter Telegram
- [ ] Add tip jar


## Validation

- **Signal target**: 2,000 visits + 1 sponsor in 60 days
- **Window**: 60 days
- **Channels**: spot.uz transport, Tashkent commuter Telegram, Tashkent expat WhatsApp


**Tech stack**: Python scraper, Telegram Bot, Carrd, Click for tip

**Capability required**: Russian, scraping, B2B sales


## Moat potential

Rate-history dataset + alternative-taxi sponsorship.

## Risks

- **Yandex blocks scraping** — _Mitigation_: User-side browser extension
- **Niche** — _Mitigation_: Bundle with TashkentDayPlanner
- **Low ad demand** — _Mitigation_: Tip jar baseline


## Scoring (weighted total: **6.65**)

| Axis | Score |
|---|---|
| Demand clarity (30%) | 6/10 |
| Speed to MVR (15%) | 9/10 |
| Monetization path (20%) | 5/10 |
| Founder solo feasibility (20%) | 8/10 |
| Local market fit (15%) | 7/10 |

### Rationale

Niche utility, modest revenue.
