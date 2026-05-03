---
type: "solopreneur_mvp"
id: "uz-mvp-054"
country: "UZ"
category: "free_tool"
sector: "Finance & Fiscal"
confidence_tier: "B"
weighted_total: 7.6
linked_trend: "[[Trends/uz-trend-021-tax-fraud-detection-ai|uz-trend-021-tax-fraud-detection-ai]]"
linked_decree: "[[Decrees/uz-up-2025-189|UZ-UP-2025-189]]"
linked_donor: ""
linked_initiative: ""
verification: "L2_VERIFIED"
tags:
  - "country/uz"
  - "category/free_tool"
  - "tier/B"
  - "sector/finance-fiscal"
---

# InvoiceCheckerUZ

_Free Telegram tool that validates an Uzbek e-faktura invoice (BIN, VAT, formats) in 5 seconds before submission_

## Pain point

e-faktura submissions get rejected for typos in BIN, mismatched VAT. Accountants do this manually. Buxgalter Plus forum has constant 'почему отклонили инвойс?' threads.

**Evidence**: https://soliq.uz/


**Target customer**: SME accountants 30-50 in Tashkent and oblast capitals processing 50-300 e-faktura invoices/month


## Monetization

- **Model**: freemium
- **Price point**: $4.00
- **Year-1 target**: $8,000
- **Year-3 target**: $60,000


## MVR plan (free_tool)

- **Build time**: 5 days
- **Build cost**: $30

**Steps:**
- [ ] Document e-faktura schema + top 20 rejection patterns
- [ ] Telegram bot intake: paste XML or upload
- [ ] Output: pass/fail + specific fix
- [ ] Free 10/mo, $4/mo unlimited
- [ ] Soft-launch in Buxgalter Plus Telegram


## Validation

- **Signal target**: 200 users + 30 paid in 45 days
- **Window**: 45 days
- **Channels**: Buxgalter Plus, TBC SME, IT Park UZ


**Tech stack**: Python, Telegram Bot, Click

**Capability required**: Russian, Python + XML, tax-domain familiarity


## Moat potential

Lighter version of VATcheckUZ but standalone; possible bundle.

## Risks

- **Schema changes** — _Mitigation_: Subscribe to Soliq updates
- **Cannibalize VATcheckUZ** — _Mitigation_: Different ICP — accountants vs business owners
- **Free competition** — _Mitigation_: Bundle with VAT-validator at premium tier


## Scoring (weighted total: **7.60**)

| Axis | Score |
|---|---|
| Demand clarity (30%) | 7/10 |
| Speed to MVR (15%) | 10/10 |
| Monetization path (20%) | 6/10 |
| Founder solo feasibility (20%) | 9/10 |
| Local market fit (15%) | 8/10 |

### Rationale

Cheap tool, accountant ICP, complements VATcheckUZ.
