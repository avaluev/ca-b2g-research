---
type: "global_case"
id: "case-ua-diia"
country_origin: "Ukraine"
sector: "Public Administration & e-Gov"
year_initiated: 2019
uz_transferability_score: 8
kg_transferability_score: 8
verification: "VERIFIED"
---

# Diia Super-App Digital Government (Ukraine)

**Origin**: Ukraine  •  **Year**: 2019  •  **Sector**: Public Administration & e-Gov

## Problem solved

Ukraine citizens carried physical documents for routine transactions and faced extensive in-person bureaucracy. The Ministry of Digital Transformation (MinTsifry) needed a comprehensive mobile-first approach to government services that would work for a population of 40M with high smartphone penetration but fragmented legacy IT systems. Key constraint: had to be built fast (18-month initial sprint) and had to function under adversarial conditions including wartime.

## Architecture

Mobile-first super-app architecture: React Native cross-platform app fronting a microservices backend. Core services: digital passport/ID (legally equivalent to physical since 2021), vehicle registration, driving licence, vaccination certificate, business registration, social payments. Data pulled live from state registries via API gateway (Trembita, Ukraine's X-Road implementation). Backend hosted on AWS GovCloud + Ukrainian data centres. End-to-end encryption. AI-based anti-fraud layer for document verification. Key innovation: 'State in a Smartphone' concept where digital document has same legal force as physical.

## UZ transferability (8/10)

Most relevant lesson for UZ EPIGU mobile-first evolution: Diia proved that a $8M MVP can deliver 120+ services if architecture is right. UZ MoDT has explicitly referenced Diia in internal strategy documents. Key adaptation: Uzbek and Russian language UI, data sovereignty hosting requirements, and no dependence on AWS (UZ prefers sovereign cloud). Budget realism score HIGH — $8M is within UZ project range. Donor pathway: UNDP, USAID-successor, or direct bilateral.

## KG transferability (8/10)

Diia is the clearest reference for KG's ambition to unify Tunduk services under a citizen-facing mobile app. Budget realism: Diia built for $8M — KG could build a Kyrgyz equivalent for $2-4M given smaller service catalogue. UDP digital department post-reorganisation has mandate for exactly this type of integration. Wartime resilience features relevant given KG's geopolitical risk environment.
