---
type: "solopreneur_mvp"
id: "uz-mvp-004"
country: "UZ"
category: "saas"
sector: "Public Administration & e-Gov"
confidence_tier: "A"
weighted_total: 8.45
linked_trend: "[[Trends/uz-trend-003-ai-procurement-system|uz-trend-003-ai-procurement-system]]"
linked_decree: "[[Decrees/uz-up-2025-189|UZ-UP-2025-189]]"
linked_donor: ""
linked_initiative: ""
verification: "L2_VERIFIED"
tags:
  - "country/uz"
  - "category/saas"
  - "tier/A"
  - "sector/public-administration-e-gov"
---

# TenderRadar UZ

_Daily Telegram digest of new xt-xarid.uz tenders relevant to your business sector — first daily AI procurement filter for SMEs_

## Pain point

xt-xarid.uz publishes 200+ tenders per day. SMEs have no time to filter, no English/local-language alerts. UP-189 mandates AI procurement starting Jan 1 2026 — a flood of new IT tenders is incoming. Most SMEs hear about a tender 2 days before deadline.

**Evidence**: https://xt-xarid.uz/


**Target customer**: Tashkent and Samarkand IT consultancies and equipment suppliers (5-50 employees) with revenue $200K-2M/year who currently win 1-3 government tenders/year and want to double


## Monetization

- **Model**: subscription
- **Price point**: $19.00
- **Year-1 target**: $28,000
- **Year-3 target**: $200,000


## MVR plan (landing_page)

- **Build time**: 7 days
- **Build cost**: $80

**Steps:**
- [ ] Scrape xt-xarid.uz daily, classify tenders by GPT-4o-mini into 12 sector tags
- [ ] Carrd landing page with email + sector picker + first-week-free CTA
- [ ] Daily Telegram + email digest using Buttondown
- [ ] Click/Stripe subscription billing at 240,000 UZS/month ($19)
- [ ] Soft-launch in IT Park UZ Telegram and uzcloud.uz partner Slack


## Validation

- **Signal target**: 200 free signups in 30 days, 25 paying subs by day 60
- **Window**: 60 days
- **Channels**: IT Park UZ Telegram, spot.uz business reader Telegram, ICT Week 2026 booth swap with vendor friends, LinkedIn UZ IT founders group


**Tech stack**: Python + BeautifulSoup, Supabase, OpenAI, Buttondown email, Telegram Bot API, Click subscription

**Capability required**: Python scraping, Russian fluency, B2B sales via Telegram


## Moat potential

Tender + outcome database (winner names + bid prices for closed tenders) becomes a benchmark dataset; sell anonymized 'win price' analytics to bidders at premium tier; possible white-label to chambers of commerce.

## Risks

- **xt-xarid.uz blocks scraping** — _Mitigation_: Switch to RSS feed if available, or partner with one chamber for paid feed access
- **State competitor offers AI alerts free** — _Mitigation_: Add bid-writing AI assistant as paid layer; lean into faster delivery + better UX
- **Misclassification frustrates customers** — _Mitigation_: Human-in-loop review for first 30 days; user feedback loop to retrain


## Scoring (weighted total: **8.45**)

| Axis | Score |
|---|---|
| Demand clarity (30%) | 9/10 |
| Speed to MVR (15%) | 8/10 |
| Monetization path (20%) | 8/10 |
| Founder solo feasibility (20%) | 8/10 |
| Local market fit (15%) | 9/10 |

### Rationale

Strong revenue path, clear ICP, defensible data moat in year 2.
