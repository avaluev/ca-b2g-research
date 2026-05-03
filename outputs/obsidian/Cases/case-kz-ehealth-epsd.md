---
type: "global_case"
id: "case-kz-ehealth-epsd"
country_origin: "Kazakhstan"
sector: "Health"
year_initiated: 2012
uz_transferability_score: 9
kg_transferability_score: 7
verification: "VERIFIED"
---

# Kazakhstan EPSD Electronic Health Record System

**Origin**: Kazakhstan  •  **Year**: 2012  •  **Sector**: Health

## Problem solved

Kazakhstan had 17+ regional health MIS systems with no interoperability, preventing care coordination across regional boundaries. National statistics were manually aggregated with 6-month delays, preventing effective disease surveillance. A national Electronic Population State Database (EPSD) health module was needed to provide real-time patient data access across all regions.

## Architecture

National Health Information System built by NIT Kazakhstan: Patient Registration System (PRS) as central identifier, Electronic Medical Record (EMR) aggregated from regional MIS via FHIR-based API gateway. Key module: Digital Polyclinic tracking GP visits, referrals, and chronic disease management. Integration with OSMS (compulsory health insurance) for billing. E-prescription: integrated with national drug registry and pharmacy POS systems. Telemedicine added 2021. AI layer: predictive analytics for disease burden forecasting added 2022.

## UZ transferability (9/10)

KZ EPSD is the direct reference for UZ E-Health (ПП-415). Regional MIS integration lessons — particularly the connector strategy for legacy systems — are directly applicable given UZ's similar mix of Soviet-era and modern hospital software. E-prescription integration with pharmacy POS is the Phase 1 module UZ should replicate. Budget: KZ spent $55M over 7 years; UZ could achieve equivalent in 4 years for $20-30M leveraging KZ architecture. NIT advisory available.

## KG transferability (7/10)

KG health system scale is 1/3 of KZ. EPSD architecture principles directly applicable. Key: GP-level EMR integration (Digital Polyclinic equivalent) is the highest-impact module for KG's primary care. Budget at KG scale: $8-15M. NIT advisory could accelerate by 2 years vs building from scratch.
