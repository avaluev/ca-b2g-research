---
type: "global_case"
id: "case-in-esanjeevani"
country_origin: "India"
sector: "Health"
year_initiated: 2019
uz_transferability_score: 8
kg_transferability_score: 9
verification: "VERIFIED"
---

# eSanjeevani National Telemedicine Platform (India)

**Origin**: India  •  **Year**: 2019  •  **Sector**: Health

## Problem solved

India's 1.4 billion population faced a massive urban-rural healthcare divide — rural areas had 1 doctor per 10,000 population vs WHO standard of 1 per 1,000. Specialist consultations required expensive multi-day travel. eSanjeevani created a national telemedicine platform allowing rural patients to access specialists at district, state, and national levels via video consultation, integrated with national health ID and EMR systems.

## Architecture

Government-built (C-DAC and MoHFW) web + mobile telemedicine platform. Two modes: (1) HWC (Health and Wellness Centre) to hospital hub-and-spoke — rural HWC staff initiate consultation on patient's behalf to district/state specialists; (2) OPD (Outpatient) direct patient access via mobile app. Integration with Ayushman Bharat Digital Mission health ID, national drug formulary, e-prescription standards (HL7 FHIR). Video calls via WebRTC. AI triage module added 2022: symptom-based pre-consultation questionnaire routes patient to appropriate specialty. Hosted on NIC Government Cloud.

## UZ transferability (8/10)

UZ faces exact same urban-rural healthcare divide — Tashkent concentration of specialists vs Ferghana/Karakalpakstan district shortages. eSanjeevani hub-and-spoke model maps to UZ district polyclinic (poliklinika) → tuman → viloyat → national hierarchy. UZ E-Health platform (ПП-415) provides the integration foundation. Cost: $3-5M national telemedicine deployment leveraging open-source eSanjeevani code. Donor pathway: World Bank Health, ADB, KOICA.

## KG transferability (9/10)

KG has the most severe urban-rural health divide in the dataset: Bishkek has specialists, Issyk-Kul/Naryn/Batken have near-zero specialists. eSanjeevani's small-budget ($15M) for massive scale is compelling for KG. Adaptation: Russian/Kyrgyz language interface, integration with MHIF (Mandatory Health Insurance Fund) billing. Donor pathway: WHO, World Bank, ADB, AKDN (rural connectivity).
