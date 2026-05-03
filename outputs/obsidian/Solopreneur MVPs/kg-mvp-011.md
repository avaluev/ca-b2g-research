---
type: "solopreneur_mvp"
id: "kg-mvp-011"
country: "KG"
category: "ai_tool"
sector: "Public Administration & e-Gov"
confidence_tier: "A"
weighted_total: 7.65
linked_trend: "[[Trends/kg-trend-002-tunduk-modernization|kg-trend-002-tunduk-modernization]]"
linked_decree: "[[Decrees/kg-law-2025-178-digital-code|KG-LAW-2025-178-DIGITAL-CODE]]"
linked_donor: ""
linked_initiative: ""
verification: "INFERRED"
tags:
  - "country/kg"
  - "category/ai_tool"
  - "tier/A"
  - "sector/public-administration-e-gov"
---

# PassportSlotKG

_Telegram alert when a Bishkek passport-issuance appointment slot opens within 7 days at your nearest office_

## Pain point

Bishkek passport offices (GRS) have 3-5 week wait. Cancellations invisible. 24.kg readers request cancellation alerts.

**Evidence**: https://grs.gov.kg/


**Target customer**: Bishkek and Osh professionals 25-45 needing urgent passport for work travel; returning migrants


## Monetization

- **Model**: one_time
- **Price point**: $4.00
- **Year-1 target**: $9,000
- **Year-3 target**: $60,000


## MVR plan (ad_booking)

- **Build time**: 6 days
- **Build cost**: $30

**Steps:**
- [ ] Reverse-engineer GRS booking page
- [ ] Cron-poll every 5 min, push delta
- [ ] Free 1 office, $4 multi-office
- [ ] Mbank micro-payment
- [ ] Soft-launch in kaktus.media + 24.kg


## Validation

- **Signal target**: 400 subs + 25 premium in 30 days
- **Window**: 30 days
- **Channels**: kaktus.media, 24.kg, Bishkek commuter Telegram


**Tech stack**: Python + Playwright, Supabase, Telegram Bot, Mbank

**Capability required**: Russian, scraping


## Moat potential

Network effect via referrals; extend to driver-license, marriage-registration.

## Risks

- **Anti-bot** — _Mitigation_: User-driven model
- **Govt bans third-party** — _Mitigation_: Browser-extension model
- **Low monetization** — _Mitigation_: Premium multi-office tier


## Scoring (weighted total: **7.65**)

| Axis | Score |
|---|---|
| Demand clarity (30%) | 8/10 |
| Speed to MVR (15%) | 9/10 |
| Monetization path (20%) | 6/10 |
| Founder solo feasibility (20%) | 8/10 |
| Local market fit (15%) | 8/10 |

### Rationale

Painful problem, fast build.
