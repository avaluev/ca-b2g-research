---
type: "global_case"
id: "case-in-aarogya-setu"
country_origin: "India"
sector: "Health"
year_initiated: 2020
uz_transferability_score: 8
kg_transferability_score: 7
verification: "VERIFIED"
---

# India Aarogya Setu + CoWIN Health Platform

**Origin**: India  •  **Year**: 2020  •  **Sector**: Health

## Problem solved

India needed national health ID, COVID contact tracing, and vaccine certificate infrastructure simultaneously during the pandemic. CoWIN became the world's largest vaccine management platform: citizen registration, appointment booking, dose tracking, and certificate issuance for 2.2 billion doses administered. The certificate infrastructure later extended to all health events under Ayushman Bharat Digital Mission (ABDM), creating a universal health ID backbone.

## Architecture

Three-component stack: (1) CoWIN — open-source vaccine management (beneficiary registration, slot booking, dose tracking, digital certificate generation); (2) Aarogya Setu — contact tracing app using Bluetooth + GPS; (3) ABDM — universal health ID linking CoWIN, eSanjeevani, and hospital EHRs. CoWIN architecture: microservices on NIC GovCloud, ABHA (Ayushman Bharat Health Account) as the universal health ID, FHIR-based health records, verifiable credentials (W3C VC standard) for certificates. Open-sourced by India under DPI (Digital Public Infrastructure) framework; deployed in 50+ countries.

## UZ transferability (8/10)

UZ E-Health platform (ПП-415) needs a universal health ID layer — ABHA/CoWIN architecture is the cost-effective foundation. UZ is SCO member with active India DPI dialogue. ABDM's FHIR-based approach maps to international health data standards. Key: CoWIN is free to fork and deploy. Donor pathway: India-bilateral technical assistance, World Bank Digital Development, WHO. Budget: $3-5M for UZ national health ID deployment.

## KG transferability (7/10)

KG can fork CoWIN for its mandatory vaccination registry (already maintained by MoH). ABHA health ID concept — linking all health events across the lifecycle — is the right architectural direction for KG's fragmented health record landscape. Donor pathway: WHO, India bilateral, World Bank. Cost: $1.5-2.5M for KG-scale deployment.
