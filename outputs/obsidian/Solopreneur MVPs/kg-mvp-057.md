---
type: "solopreneur_mvp"
id: "kg-mvp-057"
country: "KG"
category: "free_tool"
sector: "Finance & Fiscal"
confidence_tier: "B"
weighted_total: 7.6
linked_trend: "[[Trends/kg-trend-016-tax-ai-gns|kg-trend-016-tax-ai-gns]]"
linked_decree: "[[Decrees/kg-law-2025-178-digital-code|KG-LAW-2025-178-DIGITAL-CODE]]"
linked_donor: ""
linked_initiative: ""
verification: "L2_VERIFIED"
tags:
  - "country/kg"
  - "category/free_tool"
  - "tier/B"
  - "sector/finance-fiscal"
---

# InvoiceCheckerKG

_Free Telegram tool that validates a Kyrgyz e-invoice (BIN, VAT, formats) in 5 seconds before submission_

## Pain point

KG e-invoice submissions get rejected for typos. Accountants do this manually. Forum threads on 24.kg show demand.

**Evidence**: https://salyk.kg/


**Target customer**: KG SME accountants 30-50 processing 50-300 e-invoices/month


## Monetization

- **Model**: freemium
- **Price point**: $4.00
- **Year-1 target**: $6,000
- **Year-3 target**: $50,000


## MVR plan (free_tool)

- **Build time**: 5 days
- **Build cost**: $30

**Steps:**
- [ ] Document KG e-invoice schema + top 20 rejection patterns
- [ ] Telegram bot intake paste XML or upload
- [ ] Output pass/fail + fix
- [ ] Free 10/mo, $4/mo unlimited
- [ ] Soft-launch in Bishkek accountant + High Tech Park


## Validation

- **Signal target**: 150 users + 25 paid in 45 days
- **Window**: 45 days
- **Channels**: Bishkek accountant Telegram, High Tech Park, 24.kg business


**Tech stack**: Python, Telegram Bot, Mbank

**Capability required**: Russian, Python + XML, tax-domain familiarity


## Moat potential

Cross-promo with TaxScannerKG; complementary product.

## Risks

- **Schema changes** — _Mitigation_: Subscribe to Salyk updates
- **Cannibalize TaxScannerKG** — _Mitigation_: Different ICP — accountants vs owners
- **Free competition** — _Mitigation_: Bundle premium tier


## Scoring (weighted total: **7.60**)

| Axis | Score |
|---|---|
| Demand clarity (30%) | 7/10 |
| Speed to MVR (15%) | 10/10 |
| Monetization path (20%) | 6/10 |
| Founder solo feasibility (20%) | 9/10 |
| Local market fit (15%) | 8/10 |

### Rationale

Cheap tool, accountant ICP, complementary.
