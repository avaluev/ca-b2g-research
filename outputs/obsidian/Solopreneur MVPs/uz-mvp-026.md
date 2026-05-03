---
type: "solopreneur_mvp"
id: "uz-mvp-026"
country: "UZ"
category: "free_tool"
sector: "Agriculture & Water"
confidence_tier: "A"
weighted_total: 7.75
linked_trend: "[[Trends/uz-trend-014-precision-agri-satellite|uz-trend-014-precision-agri-satellite]]"
linked_decree: "[[Decrees/uz-pp-2025-099|UZ-PP-2025-099]]"
linked_donor: "[[Donors/wb-uz-agri-digital|WB-UZ-AGRI-DIGITAL]]"
linked_initiative: ""
verification: "L2_VERIFIED"
tags:
  - "country/uz"
  - "category/free_tool"
  - "tier/A"
  - "sector/agriculture-water"
---

# CottonYieldBot

_Telegram bot delivering 7-day cotton yield + weather forecast for Uzbek farmers using free Sentinel-2 satellite data_

## Pain point

Cotton (1.1M ha) is Uzbekistan's most managed crop yet smallholders lack micro-localized yield forecasts. Existing services target large clusters. Local agronomists publish in Russian on agro.uz forums. PP-099 mandates digital agriculture tools but state platforms target large farms.

**Evidence**: https://www.gazeta.uz/ru/list/economy/agriculture/


**Target customer**: Mid-size cotton farmers 35-60 in Fergana, Bukhara, Khorezm with 50-200 ha and a smartphone, who currently rely on word-of-mouth and weather radio


## Monetization

- **Model**: freemium
- **Price point**: $5.00
- **Year-1 target**: $14,000
- **Year-3 target**: $110,000


## MVR plan (landing_page)

- **Build time**: 9 days
- **Build cost**: $60

**Steps:**
- [ ] Pull Sentinel-2 NDVI imagery via Sentinel Hub free tier
- [ ] Telegram bot intake: pin location of farm
- [ ] Daily NDVI delta + ECMWF weather + simple yield model
- [ ] Free 1 farm, $5/mo for 5 farms + irrigation alerts
- [ ] Soft-launch with one regional farmers' union in Fergana


## Validation

- **Signal target**: 300 free users + 30 paid in 60 days
- **Window**: 60 days
- **Channels**: Fergana farmers Telegram groups, agro.uz forum cross-post, uzdjm.uz cooperative bulletin


**Tech stack**: Sentinel Hub API, ECMWF Open Data, Python, Supabase, Telegram Bot API

**Capability required**: Russian + Uzbek, basic GIS / Sentinel Hub, Python


## Moat potential

Per-field yield history + farmer-segment behavior data is monetizable to insurance, Uzpaxtasanoat, WB project; possible OEM to a state agtech platform.

## Risks

- **Cloud cover seasonality** — _Mitigation_: Combine optical with Sentinel-1 SAR fallback
- **Low willingness to pay** — _Mitigation_: Cooperative-level subscription via Uzdjm.uz
- **Government bundles a free competitor** — _Mitigation_: Lean on Uzbek-Latin UX + Telegram-native delivery


## Scoring (weighted total: **7.75**)

| Axis | Score |
|---|---|
| Demand clarity (30%) | 8/10 |
| Speed to MVR (15%) | 8/10 |
| Monetization path (20%) | 7/10 |
| Founder solo feasibility (20%) | 7/10 |
| Local market fit (15%) | 9/10 |

### Rationale

Decree-anchored, clear use case, cooperative monetization wedge.
