---
type: "global_case"
id: "case-est-digital-id"
country_origin: "Estonia"
sector: "Public Administration & e-Gov"
year_initiated: 2002
uz_transferability_score: 7
kg_transferability_score: 6
verification: "VERIFIED"
---

# Estonian Digital ID & Mobile-ID

**Origin**: Estonia  •  **Year**: 2002  •  **Sector**: Public Administration & e-Gov

## Problem solved

Citizens needed a single verifiable digital identity usable across all government services, banking, voting, and private-sector interactions. Paper-based identity processes created friction, fraud risk, and exclusion of rural populations. Estonia needed a foundation that would allow legally-binding digital signatures and encrypted online access without physical presence.

## Architecture

Two-tier architecture: physical ID card with PKI chip (ESTEID standard) plus Mobile-ID (SIM-based) plus Smart-ID (app-based, certified to eIDAS Level of Assurance Substantial/High). Central Population Register (RAHVASTIKUREGISTER) is the authoritative identity source. ID card contains two RSA key pairs: one for authentication, one for digital signatures. Certificate lifecycle managed by SK ID Solutions (formerly AS Sertifitseerimiskeskus). Mobile-ID issued by SK in partnership with all telecom operators. Smart-ID is pure software solution that reached 2 million users in 3 countries.

## UZ transferability (7/10)

UZ MyID (by Uzinfocom) is already an operational analogue — biometric ID card with mobile verification. Key learning: UZ needs to extend MyID to support qualified electronic signature (QES) standard that would allow legally-binding contracts. The 2017 ROCA vulnerability lesson is critical for UZ chip procurement decisions. Donor pathway via World Bank Digital Economy project.

## KG transferability (6/10)

KG has biometric ID cards via GRS (State Registration Service) but no mobile-ID equivalent at scale. Budget reality check: full Smart-ID deployment requires telecom operator cooperation and PKI infrastructure costing $3-8M. KG can realistically start with mobile app-based solution (Smart-ID model). UDP digital department is the procurement anchor. Budget rated moderate because KG's smaller population makes per-capita investment achievable.
