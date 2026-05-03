---
type: "global_case"
id: "case-kz-damumed"
country_origin: "Kazakhstan"
sector: "Health"
year_initiated: 2019
uz_transferability_score: 9
kg_transferability_score: 8
verification: "L2_VERIFIED"
---

# Kazakhstan Damumed AI Diagnostic Platform

**Origin**: Kazakhstan  •  **Year**: 2019  •  **Sector**: Health

## Problem solved

Kazakhstan rural districts had acute radiologist and pathologist shortages — 70% of districts had no specialist radiology interpretation services, creating 3-6 week delays for chest X-ray and CT readings. AI diagnostic assistance for tuberculosis (high-burden country), pneumonia, and chest oncology screening would reduce diagnostic backlog and enable remote screening at district polyclinics without full-time radiologist presence.

## Architecture

Cloud-deployed AI diagnostic platform integrated into Kazakhstan national EPSD (Electronic Population State Database) health system. Three AI modules: (1) Chest X-ray TB/pneumonia screening — convolutional neural network trained on 250,000+ KZ radiological images, calibrated to local TB strain prevalence; (2) CT lung nodule detection — classification of nodule characteristics for oncology referral; (3) ECG interpretation — automated arrhythmia detection for district-level GPs. API integration with district polyclinic PACS (Picture Archiving and Communication Systems). Results streamed to remote radiologist for confirmation. Local cloud hosting at NIT data centres in Nur-Sultan.

## UZ transferability (9/10)

UZ TB burden is among the highest in CIS (18,000+ new cases/year). District polyclinic X-ray shortage is identical to KZ pattern. Damumed is ALREADY in UZ pilot as of 2023. Ministry of Health e-prescription decree (ПП-415, 2023) creates procurement pathway. Most directly actionable health AI case in the entire tournament. Budget: $3-6M for national rollout on existing health infrastructure. Donor pathway: World Bank Health project, WHO, Global Fund.

## KG transferability (8/10)

KG TB burden is severe (Kyrgyzstan has highest TB rate in CIS per WHO). District polyclinic infrastructure is sparse, X-ray quality is variable. Damumed's KZ architecture directly applicable. Budget at KG scale: $1.5-3M. Donor pathway: Global Fund (TB programme), WHO, ADB health projects. KG Ministry of Health already in dialogue with AI health vendors per ADB project documents.
