---
type: "solopreneur_mvp"
id: "kg-mvp-001"
country: "KG"
category: "free_tool"
sector: "Public Administration & e-Gov"
confidence_tier: "A"
weighted_total: 8.25
linked_trend: "[[Trends/kg-trend-002-tunduk-modernization|kg-trend-002-tunduk-modernization]]"
linked_decree: "[[Decrees/kg-law-2025-178-digital-code|KG-LAW-2025-178-DIGITAL-CODE]]"
linked_donor: "[[Donors/wb-kg-p160230|WB-KG-P160230]]"
linked_initiative: ""
verification: "L2_VERIFIED"
tags:
  - "country/kg"
  - "category/free_tool"
  - "tier/A"
  - "sector/public-administration-e-gov"
---

# TundukExplainer

_Free Telegram bot explaining Tunduk e-services in Russian + Kyrgyz with deep links to forms_

## Pain point

Tunduk hosts 200+ e-services but UX is poor — citizens spend 30-60 min hunting. Digital Code mandates broader citizen-portal use. Kaktus.media and 24.kg routinely cover citizen frustration.

**Evidence**: https://kaktus.media/


**Target customer**: Bishkek and Osh citizens 25-55 navigating Tunduk for first time — passport renewals, marriage certificates, business registration


## Monetization

- **Model**: freemium
- **Price point**: $2.00
- **Year-1 target**: $12,000
- **Year-3 target**: $100,000


## MVR plan (free_tool)

- **Build time**: 7 days
- **Build cost**: $50

**Steps:**
- [ ] Crawl Tunduk service catalog and tag 50 most-used services
- [ ] Telegram bot intake in Russian + Kyrgyz
- [ ] Top-50 walkthrough with deep links
- [ ] Free, $2 voluntary tip via Optima/Mbank QR
- [ ] Soft-launch via kaktus.media community + High Tech Park Telegram


## Validation

- **Signal target**: 1,500 unique users + 20% repeat in 30 days
- **Window**: 30 days
- **Channels**: kaktus.media community, 24.kg Telegram, High Tech Park Telegram, Bishkek parents Telegram


**Tech stack**: Telegram Bot API, n8n, Supabase, OpenAI GPT-4o-mini, Optima QR / Mbank

**Capability required**: Russian + Kyrgyz, Telegram bot setup, civic-tech outreach


## Moat potential

Q&A logging produces a Kyrgyz-language service-intent dataset; possible OEM to UDP Digital Department or licensing for Tunduk official chatbot.

## Risks

- **UDP launches official chatbot post-MinCifry abolition** — _Mitigation_: Position as 'unofficial concierge' aggregating multiple portals
- **Tunduk URL changes after Infocom transfer** — _Mitigation_: Sitemap-detection fallback
- **Low monetization** — _Mitigation_: Donor-grant via WB Digital CASA


## Scoring (weighted total: **8.25**)

| Axis | Score |
|---|---|
| Demand clarity (30%) | 9/10 |
| Speed to MVR (15%) | 9/10 |
| Monetization path (20%) | 6/10 |
| Founder solo feasibility (20%) | 9/10 |
| Local market fit (15%) | 9/10 |

### Rationale

Digital Code drives demand; Japarov-concentration favors single point of entry.
