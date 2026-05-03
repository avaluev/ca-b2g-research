---
type: "global_case"
id: "case-kz-smart-agri"
country_origin: "Kazakhstan"
sector: "Agriculture & Water"
year_initiated: 2017
uz_transferability_score: 9
kg_transferability_score: 8
verification: "VERIFIED"
---

# Kazakhstan Smart Agriculture System (National Agroinfo)

**Origin**: Kazakhstan  •  **Year**: 2017  •  **Sector**: Agriculture & Water

## Problem solved

Kazakhstan is among the top 10 global wheat exporters with 22M+ hectares of farmland, but agricultural productivity was limited by poor crop monitoring, inefficient water usage in irrigated zones, and delayed disease/pest detection. Subsidy distribution was opaque. The Ministry of Agriculture needed a national agricultural information system integrating satellite imagery, soil sensor data, and weather stations to improve monitoring and subsidy targeting.

## Architecture

National agromonitoring platform (agromonitoring.kz): satellite image analysis (Sentinel-2 + Landsat) for crop classification and NDVI monitoring; IoT sensor network for soil moisture and temperature in irrigated zones; weather station API integration from KazHydroMet. AI modules: crop disease early warning (image classification of field photos via mobile app), yield prediction model (random forest + weather variables), subsidy eligibility verification (cross-checking declared vs satellite-measured field area). Platform built by local company with ESRI Kazakhstan; hosted on NIT cloud. Mobile app for farmers: field registration, subsidy application, advisory alerts.

## UZ transferability (9/10)

UZ agriculture: cotton (world's 5th largest exporter), wheat, fruits. Both satellite monitoring and subsidy fraud detection are HIGHEST priority applications. World Bank $35M Geospatial NSDI project (2025-2030) specifically funds cadastre + agricultural land monitoring integration. Donor pathway: World Bank Agricultural Competitiveness Project, ADB. This is one of the best-aligned cases with active UZ procurement. Budget: $5-10M on top of World Bank project for agricultural AI layer.

## KG transferability (8/10)

KG agriculture: wheat, barley, potatoes, livestock. Mountain terrain makes satellite monitoring even more valuable (fewer field inspection options). KG subsidy distribution has documented irregularities — AI fraud detection has political support. Budget: $3-6M for KG national agromonitoring leveraging free Sentinel-2 data. Donor pathway: ADB agriculture projects, World Bank, EBRD agritech.
