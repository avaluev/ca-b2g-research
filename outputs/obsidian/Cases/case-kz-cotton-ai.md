---
type: "global_case"
id: "case-kz-cotton-ai"
country_origin: "Kazakhstan"
sector: "Agriculture & Water"
year_initiated: 2020
uz_transferability_score: 9
kg_transferability_score: 6
verification: "L2_VERIFIED"
---

# Kazakhstan Crop Monitoring AI — Soy/Sunflower Yield Prediction

**Origin**: Kazakhstan  •  **Year**: 2020  •  **Sector**: Agriculture & Water

## Problem solved

Kazakhstan's oilseed sector (sunflower, soy) needed improved export commodity planning and subsidy targeting. Yield prediction based on satellite NDVI + weather variables allows Ministry of Agriculture to set export quotas 3 months ahead of harvest and target subsidy distribution to verified under-performing farms rather than blanket payments.

## Architecture

Machine learning pipeline: Sentinel-2 satellite imagery (free, 10m resolution, 5-day revisit) + MODIS for time-series, ERA5 weather reanalysis, soil property database. Model: gradient boosting (XGBoost) for yield prediction, trained on 5 years of historical yield data + satellite indices. Validation: against actual combine harvester yield data reported to GK (Grain Center). Output: oblast-level and rayon-level yield maps 3 months ahead of harvest. Ministry of Agriculture uses for export quota setting. Farmer-level: satellite-verified field area for subsidy eligibility. Built by local data science team at MoA.

## UZ transferability (9/10)

UZ is the world's 5th largest cotton exporter — satellite-verified cotton yield prediction and field area monitoring has DIRECT commercial and government value. This is potentially the highest-ROI application in the entire Agriculture batch: UZ spends $300M+/year in cotton subsidies; satellite verification could save $30-50M/year in fraud reduction. Budget: $2-4M for UZ cotton crop monitoring system. Kazakhstan MoA advisory available. World Bank NSDI project provides infrastructure foundation.

## KG transferability (6/10)

KG has smaller and more fragmented farms than KZ. Key crops: wheat, barley, potatoes. Yield prediction useful for wheat export quota management and subsidy targeting. Budget: $1.5-3M for KG crop monitoring. Main challenge: KG field fragmentation is extreme — many farms <1 hectare, below Sentinel-2 resolution threshold.
