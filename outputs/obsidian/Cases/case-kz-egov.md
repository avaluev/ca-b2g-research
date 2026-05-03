---
type: "global_case"
id: "case-kz-egov"
country_origin: "Kazakhstan"
sector: "Public Administration & e-Gov"
year_initiated: 2006
uz_transferability_score: 9
kg_transferability_score: 7
verification: "VERIFIED"
---

# eGov.kz National Citizen Portal

**Origin**: Kazakhstan  •  **Year**: 2006  •  **Sector**: Public Administration & e-Gov

## Problem solved

Kazakhstan citizens had to visit multiple physical windows across different ministries to obtain routine government services. Long queues, corruption at service counters, lack of transparency in processing status, and high travel cost for rural citizens. The government needed a single digital front door that would aggregate 700+ government services from 80+ agencies behind one authenticated portal.

## Architecture

Three-layer architecture: front-end citizen portal (e.gov.kz) plus mobile app, a government service bus (Electronic Government Gateway, EGG) handling 80+ connected agencies, and a unified registry layer. Single Sign-On via ECP (Electronic Digital Signature Certificate) issued by NCA (National Certification Authority). Service requests flow from citizen portal through EGG to agency back-end systems, with status returned asynchronously. Monitoring dashboards for MCI (Ministry of Digital Development). Oracle SOA Suite used for initial integration layer; modernised with microservices from 2018. Hosted on NIT (National Information Technologies) sovereign data centres.

## UZ transferability (9/10)

This is the single most directly replicable case for UZ EPIGU evolution. Kazakhstan is 8 years ahead of UZ on portal development. Political economy fit: both are post-Soviet authoritarian-modernising states with similar ministry structures, budget flows, and citizen expectations. UZ officials actively reference KZ model. Specific lessons: stage EGG integration by agency tier, invest in MCI-equivalent monitoring dashboards. Budget: KZ spent $180M over 15 years; UZ needs ~$30-50M for equivalent build leveraging existing MyID and EPIGU foundation.

## KG transferability (7/10)

KG has Tunduk as service-bus analog. The KZ portal architecture is directly replicable but KG budget is 1/20th of KZ. Key insight: KG can leapfrog the Oracle/heavy-middleware phase by adopting open-source service bus (X-Road + modern API gateway). UDP digital department should hire KZ civil servants as advisors for 3-6 month secondments. Target: 200 services online by 2027 (vs KZ 800 today).
