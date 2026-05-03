---
type: "global_case"
id: "case-uk-govuk-verify-cautionary"
country_origin: "UK"
sector: "Justice & Rule of Law"
year_initiated: 2014
uz_transferability_score: 2
kg_transferability_score: 2
verification: "VERIFIED"
---

# GOV.UK Verify Digital Identity Programme (CAUTIONARY)

**Origin**: UK  •  **Year**: 2014  •  **Sector**: Justice & Rule of Law

## Problem solved

The UK Government Digital Service (GDS) attempted to build a federated identity verification system for government services — allowing citizens to use private-sector identity providers (banks, credit agencies) to verify their identity for government services, avoiding a centralised government identity database.

## Architecture

Hub-and-spoke federated identity architecture: GDS operated a central hub, multiple certified identity providers (Barclays, Experian, Royal Mail, etc.) verified identities using their own processes, hub issued assertions to relying parties (HMRC, DWP, etc.). OpenID Connect with SAML assertions. Designed to avoid a single government identity database on civil liberties grounds. Separate from UK Passport Office or DVLA databases.

## UZ transferability (2/10)

Score 2 = this is the anti-pattern for UZ MyID. UZ should NOT replicate the federated approach — it already has the authoritative national register (civil registry + biometric ID) that UK Verify tried to work around. UZ's centralised MyID + government mandate is actually the CORRECT architecture that UK Verify failed to implement. Key lesson: authoritative government identity register is essential; private-sector federation without it is failure.

## KG transferability (2/10)

Same cautionary rating. KG should not replicate federated identity without authoritative register. GRS biometric ID + Tunduk is the right architecture direction.
