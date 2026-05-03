---
type: "solopreneur_mvp"
id: "uz-mvp-005"
country: "UZ"
category: "free_tool"
sector: "Public Administration & e-Gov"
confidence_tier: "A"
weighted_total: 7.35
linked_trend: "[[Trends/uz-trend-005-mahalla-digital-social-registry|uz-trend-005-mahalla-digital-social-registry]]"
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

# MahallaMonitor

_Anonymous Telegram channel where mahalla residents flag broken streetlights, garbage, water issues — feeds a city dashboard_

## Pain point

Mahalla-level service delivery is opaque to higher tiers of government. Citizens have no anonymous channel to report neighborhood issues; existing 1198 hotline is phone-only and Russian-biased. Spot.uz comments and Telegram threads are full of 'мой подъезд' complaints with no resolution path.

**Evidence**: https://kun.uz/ru/news/2025/03/10/mahalla-shikoyatlar


**Target customer**: Tashkent apartment-block residents 25-55 frustrated with utility outages and street infrastructure; secondary: mahalla raisi staff who get pre-aggregated reports without doing fieldwork


## Monetization

- **Model**: donation
- **Price point**: $0.00
- **Year-1 target**: $8,000
- **Year-3 target**: $60,000


## MVR plan (demo_video)

- **Build time**: 8 days
- **Build cost**: $50

**Steps:**
- [ ] Build Telegram bot: photo + geo-tag + category, posts to district-level public channel
- [ ] Standardize 8 issue categories (water, light, garbage, road, park, pet, noise, other)
- [ ] Auto-publish to public dashboard at mahalla-monitor.uz (Vercel + Supabase)
- [ ] Reach out to 3 progressive mahalla raisi via researcher contacts for pilot
- [ ] Add donate button (Click/Payme) and weekly impact report


## Validation

- **Signal target**: 500 reports submitted in 60 days from 3 pilot districts; 1 hokimiyat references the tool publicly
- **Window**: 60 days
- **Channels**: spot.uz Telegram readership, Tashkent district WhatsApp groups, Mahalla raisi pilot referrals, ICT Week 2026 civic tech panel


**Tech stack**: Telegram Bot API, Supabase + Postgres, Vercel + Next.js, Mapbox for geo display

**Capability required**: Russian + Uzbek written communication, Telegram bot, basic Next.js, civic tech network in Tashkent


## Moat potential

Geo-tagged citizen issue dataset becomes a paid product to hokimiyats and donor SDC governance program; possible licensing to State Targeted Social Assistance pilot under WB-UZ-P179108.

## Risks

- **Government considers tool subversive** — _Mitigation_: Pre-brief 1 mahalla raisi and partner with UNDP-UZ-DIGITAL-PUBADMIN team for cover
- **Trolling and false reports** — _Mitigation_: Manual moderation queue first 90 days; require Telegram phone-verified accounts
- **Personal data leakage in photos** — _Mitigation_: Auto-blur faces and license plates via cloud vision API


## Scoring (weighted total: **7.35**)

| Axis | Score |
|---|---|
| Demand clarity (30%) | 8/10 |
| Speed to MVR (15%) | 8/10 |
| Monetization path (20%) | 5/10 |
| Founder solo feasibility (20%) | 7/10 |
| Local market fit (15%) | 9/10 |

### Rationale

Clear citizen demand; donor monetization realistic by year 2; political risk modest if pre-briefed.
