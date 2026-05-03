---
type: "global_case"
id: "case-sg-virtual-singapore-cadastre"
country_origin: "Singapore"
sector: "Agriculture & Water"
year_initiated: 2014
uz_transferability_score: 8
kg_transferability_score: 6
verification: "VERIFIED"
---

# Singapore Virtual Singapore / National Spatial Data Platform

**Origin**: Singapore  •  **Year**: 2014  •  **Sector**: Agriculture & Water

## Problem solved

Singapore government agencies each maintained separate GIS databases (URA for land use, PUB for water infrastructure, HDB for housing, LTA for transport) with incompatible formats and no shared access. Urban planning, infrastructure maintenance, and emergency response required expensive manual data harmonisation. Virtual Singapore created a national 3D spatial data platform integrating all government geospatial data.

## Architecture

3D national digital twin built on Dassault Systèmes 3DEXPERIENCE City platform: photogrammetry from aerial surveys + ground sensors for 3D building models. Underlying data: SLA (Singapore Land Authority) base map, one-stop geospatial hub consolidating 120+ datasets from 50+ government agencies. OneMap platform for public access to location data. AI applications: solar potential analysis on rooftops (400,000+ buildings analysed), flood risk modelling, temperature microclimate mapping, EV charging point optimisation. Government API gateway: agencies can publish and access spatial datasets via standard OGC APIs.

## UZ transferability (8/10)

World Bank $35M Geospatial NSDI project (2025-2030) is directly funding a UZ National Spatial Data Infrastructure — this project IS the UZ equivalent of Virtual Singapore. The specific lesson: start with 2D shared API platform (OneMap equivalent) before attempting 3D digital twin. Key: Singapore's data governance model (agency data sovereignty + central API gateway) is the right model for UZ. Budget: World Bank project funds this; vendor opportunity is in the AI analytical layers (flood modelling, agricultural monitoring, urban heat).

## KG transferability (6/10)

KG needs a much simpler 2D spatial data platform — mountains make 3D modelling cost-prohibitive. OneMap equivalent for KG: $3-5M for a national geospatial portal integrating land cadastre, water infrastructure, and road network. Donor pathway: ADB, World Bank rural land development projects. Key: avoid the 3D complexity trap.
