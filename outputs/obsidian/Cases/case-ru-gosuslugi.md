---
type: "global_case"
id: "case-ru-gosuslugi"
country_origin: "Russia"
sector: "Public Administration & e-Gov"
year_initiated: 2009
uz_transferability_score: 8
kg_transferability_score: 7
verification: "VERIFIED"
---

# Gosuslugi (Госуслуги) Federal Services Portal

**Origin**: Russia  •  **Year**: 2009  •  **Sector**: Public Administration & e-Gov

## Problem solved

Russian citizens faced fragmented government service delivery across 80+ federal agencies with no unified entry point, requiring physical visits, complex paper document preparation, and corruption at service windows. The federal government needed a single digital portal aggregating all federal and regional services in Russian language, compatible with Russian-language IT literacy levels and existing Russian administrative structures.

## Architecture

Monolithic-then-microservices architecture: portal (gosuslugi.ru) fronts an SMEV (System of Inter-Agency Electronic Interaction) service bus. ESIA (Единая Система Идентификации и Аутентификации) provides SSO with multiple assurance levels (simplified, standard, confirmed). 80M+ registered accounts. Services span: passport replacement, tax returns, benefits, court filings, vehicle registration, pension queries. Backend integrations with FNS (tax), FMS (migration), PFRF (pension), Rosreestr (cadastre), and 80+ more agencies. Mobile app released 2018, redesigned 2021 with modern UX.

## UZ transferability (8/10)

Gosuslugi is the IMPLICIT reference architecture for UZ EPIGU — most UZ government IT staff studied Russian administrative IT models. The SMEV/ESIA architecture is directly replicable. Key difference: UZ wants to avoid Russian vendor dependency post-2022 while maintaining Russian-language UX. Score 8 reflects high architectural transferability but with important adaptation: use open-source equivalents instead of Rostelecom/1C implementations.

## KG transferability (7/10)

Same implicit reference as UZ — KG government IT professionals trained on Russian models, SMEV concepts familiar. Key note: Tunduk is conceptually SMEV-equivalent (though technically X-Road-forked). Gosuslugi citizen portal model (Russian-language, post-Soviet administrative categories) is the most culturally-intuitive reference for KG's own portal development. Post-2022 political sensitivity means official reference will be softened, but practical influence is deep.
