---
type: "solopreneur_mvp"
id: "uz-mvp-014"
country: "UZ"
category: "saas"
sector: "Public Administration & e-Gov"
confidence_tier: "A"
weighted_total: 8.0
linked_trend: "[[Trends/uz-trend-021-tax-fraud-detection-ai|uz-trend-021-tax-fraud-detection-ai]]"
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

# VATcheckUZ

_Free tool that scans an Uzbek SME's last 30 e-invoices and flags VAT errors before submission_

## Pain point

Soliq.uz's e-faktura system rejects ~5% of submissions for technical issues. SMEs find out days later when penalties accrue. UP-189 mandates AI tax fraud detection — SMEs face increased audit risk if errors are not caught pre-submission.

**Evidence**: https://soliq.uz/main


**Target customer**: Tashkent SMEs (15-50 employees) doing 50-300 e-invoices/month, especially trading and construction companies who file for monthly VAT cycles


## Monetization

- **Model**: subscription
- **Price point**: $29.00
- **Year-1 target**: $22,000
- **Year-3 target**: $180,000


## MVR plan (landing_page)

- **Build time**: 8 days
- **Build cost**: $60

**Steps:**
- [ ] Document e-faktura JSON schema and top 10 rejection patterns
- [ ] Build Streamlit app: upload XML, get error report
- [ ] Carrd landing page + 7-day free trial
- [ ] Click subscription billing at 360,000 UZS/mo
- [ ] Soft-launch in Buxgalter Plus and TBC SME Telegram


## Validation

- **Signal target**: 100 free signups, 15 paying subs in 60 days
- **Window**: 60 days
- **Channels**: Buxgalter Plus community, TBC SME Telegram, ICT Week 2026 SME track


**Tech stack**: Python + Streamlit, Supabase, Click subscription

**Capability required**: Russian, tax-domain familiarity, Python


## Moat potential

Library of common error patterns becomes proprietary; possible white-label to accounting SaaS.

## Risks

- **Soliq adds own validator** — _Mitigation_: Differentiate via AI-driven anomaly detection beyond schema check
- **Customer churn after onboarding** — _Mitigation_: Annual prepay discount + audit-protection bundle
- **Data privacy concerns** — _Mitigation_: Local processing only, no server storage


## Scoring (weighted total: **8.00**)

| Axis | Score |
|---|---|
| Demand clarity (30%) | 8/10 |
| Speed to MVR (15%) | 8/10 |
| Monetization path (20%) | 8/10 |
| Founder solo feasibility (20%) | 8/10 |
| Local market fit (15%) | 8/10 |

### Rationale

Clear pain, recurring revenue path, accountant ICP.
