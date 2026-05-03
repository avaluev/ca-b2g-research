---
type: "solopreneur_mvp"
id: "uz-mvp-015"
country: "UZ"
category: "ai_tool"
sector: "Public Administration & e-Gov"
confidence_tier: "B"
weighted_total: 7.2
linked_trend: "[[Trends/uz-trend-004-digital-id-mobile-myid|uz-trend-004-digital-id-mobile-myid]]"
linked_decree: "[[Decrees/uz-pp-2025-286|UZ-PP-2025-286]]"
linked_donor: ""
linked_initiative: ""
verification: "INFERRED"
tags:
  - "country/uz"
  - "category/ai_tool"
  - "tier/B"
  - "sector/public-administration-e-gov"
---

# MyGovDocsUZ

_Encrypted Telegram vault where citizens store digital copies of all government documents, with AI search in Uzbek and Russian_

## Pain point

Uzbeks accumulate 20-50 documents (passport, tax certificates, child certificates, real estate) and lose them when phones break. EPIGU does not aggregate. Banks demand fresh copies routinely.

**Evidence**: https://www.spot.uz/ru/2024/03/22/digital-documents/


**Target customer**: Tashkent professionals 30-50 with 2+ kids, a property, and a small business — they handle multiple documents weekly


## Monetization

- **Model**: subscription
- **Price point**: $4.00
- **Year-1 target**: $18,000
- **Year-3 target**: $140,000


## MVR plan (landing_page)

- **Build time**: 10 days
- **Build cost**: $100

**Steps:**
- [ ] Build Telegram mini-app with E2E encryption (libsodium)
- [ ] OCR via Tesseract for Cyrillic + Uzbek-Latin
- [ ] AI search 'when does my passport expire?'
- [ ] Carrd page with privacy-first messaging
- [ ] Soft-launch via TBC families and IT Park UZ Telegram


## Validation

- **Signal target**: 300 signups + 25 paying in 60 days
- **Window**: 60 days
- **Channels**: TBC SME Telegram, Anorbank parents Telegram, spot.uz tech reader chat


**Tech stack**: Telegram Mini App, Supabase storage with E2E encryption, Tesseract OCR, OpenAI

**Capability required**: Telegram mini-app dev, encryption basics, Russian + Uzbek-Latin


## Moat potential

Document-vault network effect; partner integration with banks and notaries (instant fetch).

## Risks

- **Privacy law (ЗРУ-547) compliance complexity** — _Mitigation_: E2E encryption + no server-side decryption; pre-clear with privacy lawyer
- **User mistrust** — _Mitigation_: Open-source the encryption layer
- **Telegram-native limits** — _Mitigation_: Web fallback at mygovdocs.uz


## Scoring (weighted total: **7.20**)

| Axis | Score |
|---|---|
| Demand clarity (30%) | 7/10 |
| Speed to MVR (15%) | 7/10 |
| Monetization path (20%) | 7/10 |
| Founder solo feasibility (20%) | 7/10 |
| Local market fit (15%) | 8/10 |

### Rationale

Privacy is a heavy lift but real demand.
