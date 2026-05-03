---
type: "global_case"
id: "case-est-ehealth"
country_origin: "Estonia"
sector: "Health"
year_initiated: 2008
uz_transferability_score: 8
kg_transferability_score: 7
verification: "VERIFIED"
---

# Estonia National E-Health Platform (e-terviseportaal)

**Origin**: Estonia  •  **Year**: 2008  •  **Sector**: Health

## Problem solved

Estonia's fragmented health IT systems — each hospital had separate EHR systems with no interoperability — meant patient histories were invisible to treating physicians outside the originating hospital, creating duplicate tests, adverse drug interactions, and care gaps. A national digital health record platform was needed to aggregate patient data from all care providers and make it accessible to authorised clinicians and patients.

## Architecture

TEHIK (Health and Welfare Information Systems Centre) operates the national e-Health system: Patient Portal (patsiendoportaal.ee) for citizen access, Clinical Portal for clinicians, X-Road integration connecting all hospitals and GP practices, and central data repositories (e-prescription, digital registration, laboratory results, radiological images). All data access logged and auditable — patients can see who accessed their records. e-Prescription: 99% of prescriptions electronic since 2010. FHIR-based API layer added 2021 for modern app integrations.

## UZ transferability (8/10)

UZ is building E-Health platform under ПП-415 (2023). Estonia's architecture — X-Road integration of existing hospital systems, central data repository, e-prescription — is the blueprint. Key lesson to embed in UZ implementation: incentivise GP adoption with fee-for-digital-services payments in early years. Patient portal adds political visibility (citizens see their records). Budget: $8-15M for UZ national E-Health at Estonian-equivalent scope. World Bank Health project donor pathway.

## KG transferability (7/10)

KG has a fragmented health IT landscape similar to Estonia in 2008. Key constraint: KG hospital systems include some Russian-made software (МИС, old Soviet-era systems). X-Road (Tunduk) is already the integration layer. TEHIK advisory could deploy KG national e-Health in 3-5 years. Budget: $5-8M leveraging existing Tunduk infrastructure. Donor pathway: World Bank, ADB, AKDN.
