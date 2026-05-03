---
type: "global_case"
id: "case-in-aadhaar"
country_origin: "India"
sector: "Cross-cutting"
year_initiated: 2009
uz_transferability_score: 8
kg_transferability_score: 7
verification: "VERIFIED"
---

# India Aadhaar Digital Identity — DPI Foundation

**Origin**: India  •  **Year**: 2009  •  **Sector**: Cross-cutting

## Problem solved

India had 400M+ citizens without any government-issued identity document, making service delivery, subsidy targeting, and financial inclusion impossible. Duplicate identities enabled $10B+/year in subsidy fraud. Aadhaar created a biometric digital identity for all 1.4B citizens, enabling a federated digital public infrastructure used by every government and private sector service.

## Architecture

UIDAI (Unique Identification Authority of India) operates the Aadhaar database: 12-digit unique identity number linked to biometrics (fingerprints x10, iris x2, face). Authentication API: government/private services can verify identity via eKYC API (returns verified demographic data with citizen consent). Virtual ID: privacy-preserving 16-digit temporary ID that doesn't expose Aadhaar number. Data vault: citizen can see every authentication event via MyAadhaar portal. Seeding: Aadhaar linked to bank accounts, SIM cards, government schemes (DBT — Direct Benefit Transfer). Offline verification: XML-based offline verification without internet. ABHA, AgriStack, e-Shram all use Aadhaar as root identity.

## UZ transferability (8/10)

UZ MyID (by Uzinfocom) is already a functional biometric ID system — Aadhaar is the reference for WHAT IT SHOULD EVOLVE INTO: an open API layer that any government service or private sector company can query with citizen consent. The key gap: UZ MyID authentication API is restricted to government use only. Opening it to regulated private sector (banks, insurers, fintechs) with consent framework would unlock massive economic value. Budget: $5-8M for API layer + consent framework on existing MyID. World Bank Digital Economy project.

## KG transferability (7/10)

KG GRS biometric ID is the foundation. Expanding to an Aadhaar-equivalent open API for NBKR digital som wallet verification, private bank KYC, and social payment targeting would be the next layer. Budget: $3-5M for API layer. Key lesson: don't mandate Aadhaar-linking to all services (India's Supreme Court overturned that) — keep consent-based.
