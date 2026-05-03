---
type: "global_case"
id: "case-sg-singpass"
country_origin: "Singapore"
sector: "Public Administration & e-Gov"
year_initiated: 2003
uz_transferability_score: 7
kg_transferability_score: 5
verification: "VERIFIED"
---

# Singpass National Digital Identity

**Origin**: Singapore  •  **Year**: 2003  •  **Sector**: Public Administration & e-Gov

## Problem solved

Singapore citizens had multiple government login credentials across 70+ agencies, creating friction and security vulnerabilities. Private-sector services (banking, insurance, property) required separate identity verification processes causing redundant KYC costs. The government needed a single federated identity that would work across government and private sector, supporting both citizen access and business-to-government authentication.

## Architecture

Three-layer NDI (National Digital Identity) stack: Singpass identity provider (OIDC/OAuth2 based, eIDAS equivalent), MyInfo data-sharing layer (consent-based attribute sharing from government registries to private sector), and Verify app (face verification for high-assurance transactions). Singpass Face Verification uses NIST-ranked biometric matching. MyInfo allows 700+ private-sector companies to pre-fill application forms with government-verified data (income tax, CPF balances, vehicle ownership). Hosted on GCC (Government Commercial Cloud) with AWS/Azure/GCP footprint. GovTech Singapore builds and operates the stack.

## UZ transferability (7/10)

MyInfo's consent-based attribute-sharing model is the most transferable component for UZ. UZ MyID already provides authentication; the gap is the MyInfo-equivalent layer allowing banks and private services to pre-fill forms with government-verified data. This is achievable for $5-10M on top of existing MyID infrastructure. Budget realism for UZ: MODERATE (UZ population is 36M vs SG 5.5M, scaling costs differently). Donor pathway: World Bank Digital Economy project.

## KG transferability (5/10)

Singpass full stack is over-engineered and over-priced for KG ($40M for 6M population). The MyInfo concept — consent-based data sharing — is transferable at a much lighter implementation level via Tunduk's existing API layer. KG's smaller private sector (300 banks + major companies vs SG's 2200+) means the business case needs to be built differently. Score 5: high conceptual relevance, low budget realism for full implementation.
