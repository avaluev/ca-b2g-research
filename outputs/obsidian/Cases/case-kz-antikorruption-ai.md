---
type: "global_case"
id: "case-kz-antikorruption-ai"
country_origin: "Kazakhstan"
sector: "Justice & Rule of Law"
year_initiated: 2020
uz_transferability_score: 8
kg_transferability_score: 7
verification: "L2_VERIFIED"
---

# Kazakhstan Anti-Corruption Agency AI Monitoring System

**Origin**: Kazakhstan  •  **Year**: 2020  •  **Sector**: Justice & Rule of Law

## Problem solved

Kazakhstan's Agency for Financial Monitoring (AFM) and Anti-Corruption Agency (Adildik Alany) needed tools to detect patterns of corruption in public procurement, government asset declarations, and bank transaction flows. Manual review of 500,000+ public procurement transactions/year was impossible at scale. AI-based anomaly detection and network analysis tools were needed to identify suspicious patterns, conflicts of interest, and unexplained wealth.

## Architecture

Three analytical modules: (1) Procurement Anomaly Detector — ML classifier on public procurement data (samruk-kazyna.kz + goszakup.gov.kz) flagging suspicious patterns (single bidder, off-hours submissions, entity relationship networks suggesting cartel); (2) Declaration Cross-Check — comparing official asset declarations of civil servants against property registry, vehicle registry, and business ownership data; (3) Transaction Monitoring — AI-assisted AML for SOE banking transactions. Data sources: Open data portals + secure agency integrations. Vendor: Alem IT (KZ) plus Oracle Analytics Cloud.

## UZ transferability (8/10)

UZ procurement portal (xarid.uz) provides data source. Anti-Corruption Agency (Korrupsiyaga qarshi kurashish agentligi) has political mandate and presidential priority. AI procurement anomaly detection directly applicable. Key lesson: maintain human-in-the-loop on investigation decisions — AI flags, humans investigate. Budget: $3-8M replication on UZ infrastructure is realistic. Donor pathway: UNDP anti-corruption programme, World Bank.

## KG transferability (7/10)

KG has public procurement portal (zakupki.gov.kg) with structured data. Procurement corruption is a documented challenge. Anti-corruption analytics tool at KG scale ($2-4M) is achievable. Political risk: KG has had anti-corruption agency leadership changes that could affect programme continuity. Donor pathway: UNDP, EU anti-corruption governance grants.
