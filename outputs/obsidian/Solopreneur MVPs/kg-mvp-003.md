---
type: "solopreneur_mvp"
id: "kg-mvp-003"
country: "KG"
category: "saas"
sector: "Public Administration & e-Gov"
confidence_tier: "A"
weighted_total: 8.45
linked_trend: "[[Trends/kg-trend-004-eprocurement-adb|kg-trend-004-eprocurement-adb]]"
linked_decree: "[[Decrees/kg-law-2025-178-digital-code|KG-LAW-2025-178-DIGITAL-CODE]]"
linked_donor: "[[Donors/adb-kg-55109-001|ADB-KG-55109-001]]"
linked_initiative: ""
verification: "L2_VERIFIED"
tags:
  - "country/kg"
  - "category/saas"
  - "tier/A"
  - "sector/public-administration-e-gov"
---

# TenderRadarKG

_Daily Telegram digest of new zakupki.gov.kg tenders relevant to your business sector_

## Pain point

Zakupki.gov.kg publishes 50+ tenders/day. KG SMEs lack alerts; ADB e-procurement project will add complexity. Most SMEs hear of tender 1-2 days before deadline.

**Evidence**: https://zakupki.gov.kg/


**Target customer**: Bishkek and Osh IT consultancies, equipment suppliers (5-30 employees) with revenue $100K-1M/year


## Monetization

- **Model**: subscription
- **Price point**: $15.00
- **Year-1 target**: $22,000
- **Year-3 target**: $150,000


## MVR plan (landing_page)

- **Build time**: 7 days
- **Build cost**: $80

**Steps:**
- [ ] Scrape zakupki.gov.kg daily, classify with GPT-4o-mini
- [ ] Carrd landing + email + sector picker
- [ ] Daily Telegram + email digest
- [ ] Mbank subscription billing 1300 KGS/mo ($15)
- [ ] Soft-launch in High Tech Park Telegram + 24.kg business community


## Validation

- **Signal target**: 150 free + 20 paid in 60 days
- **Window**: 60 days
- **Channels**: High Tech Park Telegram, 24.kg business, Bishkek IT founders Telegram


**Tech stack**: Python + BeautifulSoup, Supabase, OpenAI, Buttondown, Mbank billing

**Capability required**: Python, Russian fluency, B2B sales


## Moat potential

Tender + outcome data is monetizable to State Procurement Agency, white-label to Chamber of Commerce.

## Risks

- **Zakupki blocks scraping** — _Mitigation_: Partner with one Chamber of Commerce
- **State competitor** — _Mitigation_: Lean on faster delivery + better UX
- **Misclassification** — _Mitigation_: Human review for first 30 days


## Scoring (weighted total: **8.45**)

| Axis | Score |
|---|---|
| Demand clarity (30%) | 9/10 |
| Speed to MVR (15%) | 8/10 |
| Monetization path (20%) | 8/10 |
| Founder solo feasibility (20%) | 8/10 |
| Local market fit (15%) | 9/10 |

### Rationale

Strong revenue path, ADB-aligned, defensible data moat.
