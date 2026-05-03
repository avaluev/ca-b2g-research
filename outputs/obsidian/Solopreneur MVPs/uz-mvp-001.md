---
type: "solopreneur_mvp"
id: "uz-mvp-001"
country: "UZ"
category: "free_tool"
sector: "Public Administration & e-Gov"
confidence_tier: "A"
weighted_total: 8.25
linked_trend: "[[Trends/uz-trend-001-epigu-ai-chatbot|uz-trend-001-epigu-ai-chatbot]]"
linked_decree: "[[Decrees/uz-pp-2025-286|UZ-PP-2025-286]]"
linked_donor: ""
linked_initiative: ""
verification: "L2_VERIFIED"
tags:
  - "country/uz"
  - "category/free_tool"
  - "tier/A"
  - "sector/public-administration-e-gov"
---

# EPIGU Companion

_Telegram bot that explains 1000+ EPIGU services in plain Uzbek and Russian; routes users to the right form on epigu.uz_

## Pain point

EPIGU.uz hosts 1000+ services but the menu structure is opaque. Citizens spend 30-60 minutes hunting for the right service or call the agency directly. Mahalla-level rollout (PP-286) is forcing rural users into the portal who have never used it. Local Telegram groups (e.g. spot.uz news threads) routinely get 10-30 questions a day on which form to use for marriage certificates, driver-license renewal, child allowance applications. The state chatbot pilot is delayed.

**Evidence**: https://www.spot.uz/ru/2025/10/22/epigu/


**Target customer**: Tashkent and Andijan working-class adults 25-50 navigating EPIGU for the first time, especially women applying for child allowance and rural users now mandated by mahalla decree to use the portal


## Monetization

- **Model**: freemium
- **Price point**: $2.00
- **Year-1 target**: $18,000
- **Year-3 target**: $180,000


## MVR plan (free_tool)

- **Build time**: 7 days
- **Build cost**: $60

**Steps:**
- [ ] Crawl epigu.uz public service catalog and tag each service with 5-10 Uzbek/Russian intent phrases
- [ ] Build Telegram bot in n8n + Supabase using OpenAI GPT-4o-mini as the routing brain
- [ ] Seed 50 most-asked services with hand-written walkthroughs in Russian and Uzbek (Latin)
- [ ] Add 'submit a question' button — log unanswered queries to Airtable for daily improvement
- [ ] Cross-post bot link in 5 Tashkent and 3 Fergana Telegram parent/community groups
- [ ] Add Click/Payme micro-tip jar (50,000 UZS = $4 voluntary tip)


## Validation

- **Signal target**: 1,500 unique bot users in 30 days, 20% repeat usage week 2
- **Window**: 30 days
- **Channels**: spot.uz Telegram chat, @toshkent_oilalari Tashkent parents Telegram group, IT Park UZ Telegram, Mahalla WhatsApp groups via researcher contacts, kun.uz Telegram


**Tech stack**: Telegram Bot API, n8n, Supabase Postgres, OpenAI GPT-4o-mini, Click micro-payments

**Capability required**: Uzbek + Russian fluency, basic prompt engineering, Telegram bot setup, Airtable / Supabase admin


## Moat potential

Continuous Q&A logging produces a proprietary Uzbek-language service-intent dataset; first 100K logs can be sold to UZINFOCOM as fine-tune data when official EPIGU chatbot procurement publishes (window: 2026-2027 per UP-189).

## Risks

- **Government launches official chatbot and outcompetes free alternative** — _Mitigation_: Position as 'unofficial concierge' that aggregates EPIGU + 5 sector portals (justice, tax, customs); maintain Telegram-native UX state app cannot match
- **EPIGU URL structure changes break crawler** — _Mitigation_: Build crawler with sitemap-detection fallback; weekly diff alerts
- **OpenAI API blocked or expensive at scale** — _Mitigation_: Migrate routing to local Yandex GPT or Llama-3 8B on Vast.ai; cache common queries at 80%+ rate


## Scoring (weighted total: **8.25**)

| Axis | Score |
|---|---|
| Demand clarity (30%) | 9/10 |
| Speed to MVR (15%) | 9/10 |
| Monetization path (20%) | 6/10 |
| Founder solo feasibility (20%) | 9/10 |
| Local market fit (15%) | 9/10 |

### Rationale

Demand verified by mahalla decree + EPIGU traffic; 7-day build; freemium tipping limited but data-moat to enterprise sale is real.
