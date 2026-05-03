---
type: "initiative"
id: "KG-INI-010"
country: "KG"
sector: "Public Administration & e-Government"
confidence_tier: "A"
weighted_total: 8.55
speed_to_contract: 8
strategic_moat: 8
defensibility: 9
capital_access: 10
russian_cis_fit: 9
target_buyer: "[[People/kg-minsoc-head|kg-minsoc-head]]"
lead_institution: "[[Institutions/kg-minlabor|KG-MINLABOR]]"
authorizing_decrees:
  - "[[Decrees/kg-law-2008-058|KG-LAW-2008-058]]"
  - "[[Decrees/kg-law-2025-178-digital-code|KG-LAW-2025-178-DIGITAL-CODE]]"
  - "[[Decrees/kg-cabinet-2024-023-digital-services|KG-CABINET-2024-023-DIGITAL-SERVICES]]"
  - "[[Decrees/kg-up-2024-090-concept|KG-UP-2024-090-CONCEPT]]"
precedent_case: "[[Cases/case-kz-smart-social|case-kz-smart-social]]"
verification: "VERIFIED"
tags:
  - "tier/A"
  - "country/kg"
  - "sector/public-administration-e-government"
---

# KG Identity & Social Protection AI Registry (WB P155198)

_Deliver AI-augmented identity and social protection registry for Ministry of Labor & Social Protection under World Bank Project P155198 ($20M), replicating Kazakhstan e-Otinish and India e-Shram._

## Problem

WB-KG-IDENTITY-P155198 ($20M) is the active World Bank Identity and Targeting for Social Protection Project. Ministry of Labor and Social Protection (KG-MINLABOR / kg-minsoc-head) is implementing partner. Existing Kyrgyz social registry has data quality gaps and lacks AI-assisted targeting. KG-LAW-2008-058 (personal information) and Digital Code provide regulatory frame. case-kz-smart-social Kazakhstan e-Otinish, case-in-e-shram India e-Shram informal labor registry, and case-pl-mobywatel Poland mObywatel (Soviet-bloc evolution reference) are precedents. The system is a foundation for cash-transfer targeting, child protection, labor market matching, and post-pandemic resilience.

## Solution concept

Three-layer AI registry: (1) data-quality AI engine — entity resolution, deduplication, and gap detection across existing social registry, civil registry (KG-GRS), tax (KG-GNS), and Tunduk identity records, with named uncertainty for each record; (2) targeting AI — proxy means testing model for cash-transfer eligibility, with explainable scores and human-review workflow; (3) caseworker assistant — Russian-Kyrgyz bilingual conversational interface for social workers in 7 oblast offices to query the registry, draft case notes, and route applications. Architectural anchor: Kazakhstan e-Otinish social registry + India e-Shram unorganized worker pattern. Adapted for KG centralized social fund administration, Russian-Kyrgyz bilingual UX, Tunduk-bound identity, and AKDN/SDC rural inclusion overlap.

## Pitch hook

> [!quote] Hook
> WB Project P155198 ($20M) is active and procuring AI augmentation now. Kazakhstan e-Otinish proves the architecture; India e-Shram proves the scale model. Naryn and Osh oblasts have KG's highest poverty rate. We deliver Russian-Kyrgyz bilingual sntz.ai-grade data quality + targeting + caseworker assistant on Tunduk integration in 12 months.

## Next 30 days

- [ ] LinkedIn message to kg-minsoc-piu-head (Aziz Dzhaksybekov, WB PIU coordinator) on AI augmentation architecture.
- [ ] Schedule meeting with kg-minsoc-head (Gulnara Baatyrbekova) via WB PIU intro.
- [ ] Brief WB Digital CASA TTL (kg-sandra-sargent) on cross-program integration with Tunduk and identity.
- [ ] Reach out to AKDN-KG-DIGITAL-SCHOOLS2030 PIU on rural outreach partnership.
- [ ] Build Russian-Kyrgyz bilingual caseworker assistant MVR for demo.

## Risk register

- **commercial**: Kazakhstan e-Otinish vendor bids with regional precedent and Russian-language native capability. — _Mitigation_: Differentiate on Kyrgyz language coverage (Kazakhstan vendor is Russian/Kazakh, not Kyrgyz), AKDN rural integration, and Tunduk inference fabric native deployment.
- **political**: MoLSP minister rotation; cash-transfer targeting is politically sensitive (denial of benefits triggers blowback). — _Mitigation_: Frame system as decision support not auto-decision; preserve human-in-the-loop. Anchor at WB PIU which is donor-side and stable across ministerial rotation.
- **technical**: Existing social registry data quality is uneven; entity resolution at scale is hard. — _Mitigation_: Phase 1 of pilot scoped to oblast where data quality is strongest; build data-quality scoring and gap reporting as part of deliverable so gaps are visible and addressable.


## Scoring (weighted total: **8.55**)

| Axis | Score |
|---|---|
| Speed-to-Contract | 8/10 |
| Strategic Moat | 8/10 |
| Defensibility | 9/10 |
| Capital Access | 10/10 |
| Russian/CIS Fit | 9/10 |

### Rationale

Speed 8: WB P155198 active, Phase 2 tender forthcoming. Moat 8: Kazakhstan vendor competition limits moat. Defensibility 9: social registry multi-year SLAs, caseworker workflow lock-in. Capital 10: WB $20M + state. Russian/CIS Fit 9: Russian-Kyrgyz bilingual mandatory.
