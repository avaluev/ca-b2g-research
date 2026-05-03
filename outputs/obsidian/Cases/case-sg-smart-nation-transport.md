---
type: "global_case"
id: "case-sg-smart-nation-transport"
country_origin: "Singapore"
sector: "Transport & Urban"
year_initiated: 2014
uz_transferability_score: 6
kg_transferability_score: 5
verification: "VERIFIED"
---

# Singapore Smart Nation Transport — MyTransport.SG

**Origin**: Singapore  •  **Year**: 2014  •  **Sector**: Transport & Urban

## Problem solved

Singapore needed to integrate multi-modal transport planning (MRT, bus, taxi, private hire, cycling) into a single citizen-facing application while providing transport operators with real-time passenger demand data for optimising services. The goal was to reduce car dependency by making public transport planning seamless.

## Architecture

LTA (Land Transport Authority) Datamall API platform: open data for bus arrival times, MRT status, taxi availability, cycling paths. MyTransport.SG app: multi-modal journey planning, real-time disruption alerts, carpool matching. AI backend: bus arrival prediction using ML on real-time GPS feed from 5,400 buses; demand forecasting for rail capacity planning; incident detection on MRT using vibration sensors + NLP analysis of social media mentions. Autonomous vehicle pilot zones (one-north, Jurong Lake District) use LTA's geofenced zone management system.

## UZ transferability (6/10)

Tashkent metro + bus system lacks any digital journey planning. Bus GPS tracking deployment ($2-5M) is the foundational step enabling everything else. MyTransport.SG's journey planner architecture is technically replicable using GTFS open standard. Donor pathway: ADB urban transport project in Tashkent (active). Budget: $5-10M for Tashkent multi-modal transport app.

## KG transferability (5/10)

Bishkek bus network needs GPS tracking before any AI can help. The foundational investment (bus GPS + GTFS data standard) costs $1-2M and enables both journey planning apps and demand analysis. Singapore's AI components come after this foundation. Budget reality: Bishkek transport is much simpler than SG — 2 tram lines + 80+ bus routes. $3-5M for digital backbone.
