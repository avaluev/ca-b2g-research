---
type: "global_case"
id: "case-in-agristack"
country_origin: "India"
sector: "Agriculture & Water"
year_initiated: 2021
uz_transferability_score: 8
kg_transferability_score: 7
verification: "VERIFIED"
---

# India AgriStack Unified Farmer Database

**Origin**: India  •  **Year**: 2021  •  **Sector**: Agriculture & Water

## Problem solved

India had 120M+ farm households with fragmented data across land records (state revenue departments), crop insurance (PMFBY), agricultural credit (banks/NABARD), and PM-Kisan subsidy scheme. This fragmentation caused: subsidy leakage (fake farmer registrations), inability to target credit to genuine farmers, and no analytical capability for yield prediction or risk assessment. AgriStack created a federated Farmer Digital Identity linking all agricultural data to a Unified Farmer's Registry (UFR).

## Architecture

India DPI architecture: Unified Farmer's Registry (UFR) as central farmer identity store linked to Aadhaar. Geo-referenced land parcel data from state Bhu-Aadhaar (unique land IDs). Crop Sown Registry: real-time crop declaration database. Federated API layer: lending institutions, insurance companies, market platforms can query UFR with farmer consent. AI applications built on UFR: crop insurance claim fraud detection, credit scoring for PM-KISAN beneficiaries, satellite-verified crop declaration. Open architecture: private agritech companies (BigHaat, Dehaat, AgroStar) access UFR to target services to verified farmers.

## UZ transferability (8/10)

UZ has an analogue problem: 4M+ farm parcels, fragmented subsidy administration (Dehqon qo'mitasi), and no unified farmer digital identity. AgriStack's farmer ID + land parcel linkage is directly applicable. UZ land cadastre reform (World Bank $35M project) provides the GIS foundation. Budget: $10-15M for UZ Unified Farmer Registry on top of existing cadastre investment. Key lesson: start with land parcels geo-referencing before trying to link subsidy databases.

## KG transferability (7/10)

KG has 370,000+ farm households — much more manageable than India's 120M. UFR equivalent for KG could be built in 18 months for $3-5M. Land parcels: KG land cadastre digitisation is ongoing (ADB project). Subsidy targeting: KG government wants to improve agricultural subsidy efficiency. Key lesson from India: don't link to biometric ID before land records are clean.
