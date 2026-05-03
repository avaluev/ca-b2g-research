---
type: "initiative"
id: "KG-INI-004"
country: "KG"
sector: "Health"
confidence_tier: "A"
weighted_total: 8.7
speed_to_contract: 9
strategic_moat: 8
defensibility: 9
capital_access: 9
russian_cis_fit: 9
target_buyer: "[[People/kg-minzdrav-head|kg-minzdrav-head]]"
lead_institution: "[[Institutions/kg-minhealth|KG-MINHEALTH]]"
authorizing_decrees:
  - "[[Decrees/kg-up-2024-090-concept|KG-UP-2024-090-CONCEPT]]"
  - "[[Decrees/kg-law-2025-178-digital-code|KG-LAW-2025-178-DIGITAL-CODE]]"
  - "[[Decrees/kg-law-2025-179-digital-code-enactment|KG-LAW-2025-179-DIGITAL-CODE-ENACTMENT]]"
  - "[[Decrees/kg-cabinet-2024-023-digital-services|KG-CABINET-2024-023-DIGITAL-SERVICES]]"
precedent_case: "[[Cases/case-est-ehealth|case-est-ehealth]]"
verification: "VERIFIED"
tags:
  - "tier/A"
  - "country/kg"
  - "sector/health"
---

# KG eHealth EHR & AI Diagnostic Platform

_Deliver electronic health record and AI diagnostic suite for the Ministry of Health under live RFP KG-T-2026-006 ($4.03M), replicating Estonia e-Health and Kazakhstan Damumed precedents._

## Problem

KG-MINHEALTH lacks national EHR; existing data is fragmented across hospital systems. Live tender KG-T-2026-006 ($4.03M, digital health: EHR + AI diagnostic support) is open. Constitutional commitment to digital governance (KG-UP-2024-090-CONCEPT) and Digital Code (KG-LAW-2025-178) mandate health-data interoperability via Tunduk. AKDN-KG-DIGITAL-SCHOOLS2030 ($15M, AKDN) and UNICEF-KG-DIGITAL-EARLY ($1.5M) provide co-financing pathway for child and rural health. Estonia E-Health (case-est-ehealth), Kazakhstan Damumed (case-kz-damumed), and Bangladesh a2i Telemedicine (case-bd-a2i-health) are precedent cases. KG mountain geography (>90% mountainous, scattered population) makes telemedicine + AI triage especially high-value.

## Solution concept

Three-layer platform: (1) National EHR core with Tunduk-bound identity (KGz citizen ID), patient data store, and clinician-facing UX in Russian-Kyrgyz bilingual; (2) AI diagnostic suite — radiology image triage (chest X-ray TB screening priority, given KG TB burden), retinal screening for diabetic retinopathy, ECG arrhythmia detection — running as inference services on Tunduk inference fabric (linked to KG-INI-003); (3) Telemedicine triage for mountain communities (linked to KG-INI-006), AKDN co-financed, with offline-capable mobile app for ayil ambulatories. Architectural anchor: Estonia e-terviseportaal (case-est-ehealth) + Damumed clinical decision support (case-kz-damumed) + a2i community-clinic delivery model (case-bd-a2i-health). Adapted for KG's centralized procurement, Russian-Kyrgyz bilingual UX, Tunduk integration, and mountain telemedicine field constraints.

## Pitch hook

> [!quote] Hook
> Estonia e-Health serves 1.3M citizens with X-Road; Kazakhstan Damumed proves the regional Russian-language clinical UX. KG-T-2026-006 ($4.03M) is open now to deliver KG's first integrated EHR + AI diagnostic + mountain telemedicine stack. AKDN co-finances the mountain rollout. We bring Russian-Kyrgyz bilingual sntz.ai radiology AI ready to deploy on Tunduk inference fabric.

## Next 30 days

- [ ] Submit pre-qualification documentation for KG-T-2026-006 ($4.03M) before submission deadline.
- [ ] LinkedIn message to kg-minzdrav-head (Alymkadyr Beishenaliev) referencing AKDN partnership and Estonia e-Health architecture.
- [ ] Schedule meeting with AKDN-KG-DIGITAL-SCHOOLS2030 PIU (kg-akdn-piu) for endorsement letter.
- [ ] Brief Estonia eGA's KG advisor (kg-tonis-mae) on EHR architecture and request Estonia e-Health reference letter.
- [ ] Reach out to UNICEF-KG-DIGITAL-EARLY TTL for child/early-learning health overlap alignment letter.

## Risk register

- **commercial**: Damumed bids with Kazakhstan precedent and Russian-language UX directly comparable. They are the natural regional incumbent. — _Mitigation_: Differentiate on Kyrgyz-language clinical UX (Damumed is Russian-only at scale), AI diagnostic depth, AKDN mountain telemedicine integration, and Tunduk inference fabric native deployment (not just bolted-on).
- **political**: MoH leadership (Alymkadyr Beishenaliev) tenure not guaranteed; ministerial rotation in KG averages 18 months. — _Mitigation_: Build dual relationship at MoH minister level and at clinical lead level (Bishkek Republican Hospital director — pre-identify and brief). Anchor parallel relationship at AKDN PIU which is donor-side.
- **technical**: Mountain telemedicine connectivity is unreliable; offline-first design is required and rarely delivered well by EHR vendors. — _Mitigation_: Engineer offline-first sync layer with explicit conflict resolution; partner with KG-MEGACOM (state mobile operator, KG-MEGACOM institution) for connectivity SLAs in pilot zones.


## Scoring (weighted total: **8.70**)

| Axis | Score |
|---|---|
| Speed-to-Contract | 9/10 |
| Strategic Moat | 8/10 |
| Defensibility | 9/10 |
| Capital Access | 9/10 |
| Russian/CIS Fit | 9/10 |

### Rationale

Speed 9: live RFP, decision within 90 days. Moat 8: Damumed competition limits moat. Defensibility 9: EHR multi-year SLAs, clinical workflow lock-in. Capital 9: AKDN $15M + UNICEF $1.5M + state budget. Russian/CIS Fit 9: Russian-Kyrgyz bilingual mandatory, sntz.ai radiology AI fits.
