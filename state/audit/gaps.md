# Coverage Gaps — Reflexion Auditor Report
**Auditor:** reflexion-auditor (Wave 5) | **Date:** 2026-05-04

This file enumerates coverage gaps in the knowledge graph as of audit date. Each gap specifies what additional research is needed to close it.

---

## Section A: Sector × Lens Coverage Matrix

Coverage scores 1-10 (10 = comprehensive, 1 = essentially absent). Cells in **bold** flag scores ≤ 4.

| Sector \ Lens | Karimov-Mirziyoyev (UZ) | Japarov-Concentration (KG) | Decree Half-Life | Donor Co-Financing | Diaspora Bridge | Russian/CIS |
|---|---|---|---|---|---|---|
| Public Administration | 8 | 7 | 9 | 8 | 6 | 7 |
| Justice & Rule of Law | 9 | 5 | 9 | 6 | **4** | 8 |
| Health | 7 | 5 | 7 | 9 | **4** | 6 |
| Education | 8 | 6 | 7 | 7 | 5 | 6 |
| Agriculture | 5 | **4** | 5 | 6 | **3** | 5 |
| Energy | 6 | **3** | 6 | 8 | **3** | 5 |
| Transport | **4** | **4** | **4** | 5 | **2** | **4** |
| Finance/Banking | 7 | 8 | 8 | 7 | 5 | 7 |
| **Security/Defense** | **3** | **3** | **3** | **2** | **1** | **3** |
| Environment/Climate | **4** | **3** | **4** | 5 | **2** | **4** |
| Tourism | 5 | **4** | 5 | **4** | **2** | **4** |
| Labor/Social | 6 | 5 | 6 | 7 | **3** | 5 |

**Key takeaways:**
- **Security/Defense is essentially uncovered** across all 6 lenses. This is partly justified (opaque procurement, classified budgets) but creates a strategic blindspot.
- **Diaspora Bridge** lens is below 5 in 9 of 12 sectors. Diaspora coverage is concentrated in digital/finance, missing applications in agriculture, energy, environment.
- **Transport, Tourism, Environment** are systematically light across multiple lenses.
- **Japarov Concentration** lens scores low in agriculture, energy, environment, transport, tourism — consistent with KG's smaller economic footprint in those sectors but also reflecting limited research depth.

---

## Section B: Sector-by-Sector Specific Gaps

### B.1 Public Administration
- **GAP**: Few records on EPIGU/MyID API ecosystem incumbents (3rd-party integrators)
- **GAP**: UZ Public Services Agency (multifunctional centers) leadership not deeply mapped
- **What's needed**: One-pass crawl of EPIGU developer portal + IT Park resident company list

### B.2 Justice & Rule of Law
- **GAP**: Diaspora coverage weak — Uzbek-trained lawyers at international law firms (Allen & Overy, Baker McKenzie Moscow/London) not mapped
- **GAP**: Prosecutor General's office digital initiatives separate from Supreme Court — limited records
- **What's needed**: Targeted search for "узбекский юрист" + international firms

### B.3 Health
- **GAP**: KG Health digitalization post-Mintsifry-liquidation has unclear procurement authority
- **GAP**: Diaspora — Uzbek/Kyrgyz physicians at major US hospitals could be diaspora-bridge but not mapped
- **What's needed**: Cross-check post-UDP institutional health digital responsibilities

### B.4 Education
- **GAP**: KG ed-tech vendor landscape light
- **GAP**: AI in education (УП-189 mandate) has 15 university labs but lab leadership not mapped
- **What's needed**: Per-university lab director identification

### B.5 Agriculture
- **GAP**: Major agriculture donor projects have minor digital components but presented as significant donor pipeline (see correction C-002, C-003 — WB-UZ-AGRI-DIGITAL P168566 actually P158372 with $500M total but small digital component)
- **GAP**: Diaspora agronomists / agtech founders not searched
- **GAP**: Both UZ and KG agriculture ministries have weak digital governance baseline
- **What's needed**: Filter donor records to "digital component" budget where possible; rescore russian_cis_fit downward

### B.6 Energy
- **GAP**: Beyond ADB UZ NEGU power grid, energy sector digitalization is thin
- **GAP**: Renewables AI/grid integration (which is hot in KG given hydropower) — limited initiatives
- **What's needed**: Energy ministries' digitalization roadmaps, off-grid/renewables analytics opportunities

### B.7 Transport
- **GAP**: Both countries have intelligent transport systems (ITS) initiatives — barely covered
- **GAP**: Logistics/border digital corridor (China BRI / Middle Corridor) intersects digital — not mapped
- **What's needed**: Roadmap of UZ/KG transport ministry digital strategies

### B.8 Finance/Banking
- **GAP**: AML/KYC AI vendor landscape (despite list of state-controlled banks) light
- **GAP**: SOE bank IT directors not mapped
- **What's needed**: Per-bank IT director identification

### B.9 Security/Defense ⚠️
- **HIGH GAP**: Defense ministry AI procurement is opaque in both countries
- **HIGH GAP**: Internal security (МВД, СНБ) digital/biometric procurement separate from public-facing — minimal records
- **HIGH GAP**: CST Treaty (CSTO) digital cooperation not mapped — KG is CSTO member, intersects with Russian-CIS substitution lens
- **What's needed**: This is a known unknown. Unlikely to be closed via open-source research. Acknowledge in honesty section.

### B.10 Environment/Climate
- **GAP**: Climate finance digital MRV (monitoring, reporting, verification) — small but growing
- **GAP**: Forestry, water resources digital governance — minimal coverage
- **What's needed**: Climate-financed program cross-reference (UNFCCC, GCF projects in CA)

### B.11 Tourism
- **GAP**: Both countries' tourism digital strategies (Uzbekistan-2026 tourism, KG ecotourism) — minimal coverage
- **GAP**: e-Visa systems integration not mapped
- **What's needed**: Tourism agency / state committee digital initiatives

### B.12 Labor/Social
- **GAP**: KG biometric social registry (P155198) post-Mintsifry-liquidation institutional ownership unclear (see C-022, INI-024 demotion)
- **GAP**: Migration/labor exchange digital systems (UZ-Russia migrant workers) — sensitive but high-leverage
- **What's needed**: Labor/Migration ministry digital pipeline mapping

---

## Section C: Lens-by-Lens Specific Gaps

### C.1 Karimov-to-Mirziyoyev Inversion (UZ)
- **MEDIUM GAP**: Innovation Agency leadership not deeply mapped
- **GAP**: Agency for Strategic Reforms (ASR) Tier-2 staff (analysts, project leads) not mapped — these are the actual decree drafters
- **GAP**: Saida Mirziyoyeva (presidential daughter, ICT-adjacent role) not separately profiled
- **What's needed**: ASR senior staff mapping, Saida Mirziyoyeva profile

### C.2 Japarov Concentration (KG)
- **HIGH GAP**: Post-Mintsifry-liquidation institutional layer (UDP Digital Department, GP Infocom + Tunduk) not yet documented in publicly available regulations
- **GAP**: Parallel Presidential Administration units beyond Digital Transformation Dept (e.g., State Agency for Information Resources and Technologies) not separately mapped
- **GAP**: Bishkek City government digitalization (smart city, e-municipality) — minimal
- **What's needed**: Wait for ~31 May 2026 UDP regulations; then re-baseline. Bishkek municipal mapping.

### C.3 Decree Half-Life
- **GAP**: Aspirational decrees (e.g., "AI national strategy" referenced as expected but not signed) not always flagged separately
- **GAP**: Cabinet Resolutions vs Presidential Decrees — half-life dynamics differ; not distinguished in records
- **What's needed**: Tag aspirational/expected decrees with `half_life_status: "aspirational"` (not in current schema enum)

### C.4 Donor Co-Financing
- **HIGH GAP**: 17 of 49 donor programs missing dyad pairs (see C-016)
- **GAP**: Chinese Digital Silk Road footprint (Huawei Smart City, ZTE backbone) — opaque
- **GAP**: Russian co-financing channels (EDB, EFSD) — geopolitically sensitive, undercovered
- **GAP**: USAID-successor entity ambiguity post-2025 reorganization — multiple project handover paths unclear
- **What's needed**: Targeted research on China DSR projects in CA; honest acknowledgment of USAID gap

### C.5 Diaspora Bridge
- **HIGH GAP**: Concentration in 4 hub cities — Istanbul, Frankfurt, Seoul, Almaty (KG natural) underrepresented
- **GAP**: Many "explicit volunteer to facilitate" claims need INFERRED tagging (see C-010, C-011)
- **GAP**: Diaspora at Big Tech (FAANG, but also Microsoft, Apple, Amazon, Tesla SpaceX) — partial coverage
- **GAP**: Diaspora in Big Consulting (BCG, Bain, Deloitte, EY, McKinsey) — partial coverage
- **What's needed**: Systematic LinkedIn/Crunchbase scrape with Sonar Pro for missing hub cities

### C.6 Russian/CIS Substitution
- **HIGH GAP**: russian_cis_fit scoring inflation (see C-009, audit_report Section 10)
- **GAP**: Anti-Russian-vendor sentiment in segments — not always identified (e.g., in Western donor-financed programs)
- **GAP**: Chinese alternative (Huawei Cloud, Alibaba) presence in CA — undercovered
- **What's needed**: Recompute russian_cis_fit scores; map Chinese vendor presence

---

## Section D: Cross-Reference Gaps

### D.1 Decree-Person bidirectional links
- decree records: `responsible_person_ids` mostly empty
- person records: `decree_authorship_ids` populated for some Tier-1 only
- **What's needed**: Bidirectional link sweep via merge_state.py

### D.2 Decree-Institution bidirectional links
- decrees often list `responsible_agency_ids` but institutions don't reverse-cite founding decrees
- **What's needed**: Add `decrees_implementing` field to institutions

### D.3 Initiative-Tender links
- initiatives reference tender IDs but several tenders are INFERRED (see C-018, C-019)
- **What's needed**: Per-initiative confirmation that referenced tender exists

### D.4 Donor-Tender pipeline
- donor programs list `pipeline_tenders` but few of these map to actual tender records
- **What's needed**: Cross-check donor pipeline tenders against tender records; create stub tender records where pipeline is documented

---

## Section E: Linguistic Source Gaps

### E.1 Uzbek-language sources
- Many UZ records lean on Russian-language Uzbek media (spot.uz, gazeta.uz Russian section)
- **GAP**: Uzbek-language native sources (kun.uz Uzbek, daryo.uz Uzbek, Davron.uz) underused
- **What's needed**: Uzbek-language cross-checks on all UZ Tier-1 records

### E.2 Kyrgyz-language sources
- Many KG records lean on Russian-language Kyrgyz media (24.kg, kaktus.media)
- **GAP**: Kyrgyz-language native sources (azattyk.org Kyrgyz, super.kg, kabar.kg Kyrgyz) underused
- **What's needed**: Kyrgyz-language cross-checks; particularly for Tunduk, UDP-related claims

### E.3 English-language donor sources
- WB and ADB press releases are English. PADs (Project Appraisal Documents) are also primarily English.
- **GAP**: Russian-language local versions of donor announcements often have additional context
- **What's needed**: Cross-check donor announcements in Russian-language press for any divergent details

---

## Section F: Time-Series / Freshness Gaps

### F.1 Stale records (last_verified > 60 days for Tier-1)
- Audit didn't run a full freshness sweep, but spot-checks suggest most Tier-1 person records have last_verified_date 2026-05-03 or 2026-05-04 — fresh as of audit
- **GAP**: After audit, freshness drops; need quarterly re-verification cadence

### F.2 Decree status freshness
- All decrees re-verified to "implementing" or "active_window" but specific status changes (amendments, repeals) may not be captured for older decrees (2018-2022)
- **What's needed**: Quarterly lex.uz / cbd.minjust.gov.kg amendment scan

### F.3 Donor program disbursement freshness
- Disbursed_usd is rarely populated (ttl=null)
- **What's needed**: Quarterly disbursement check via ewsdata.rightsindevelopment.org or projects.worldbank.org Implementation Status Reports

---

## Section G: Methodological Gaps

### G.1 No defense / classified procurement coverage
- **GAP**: Defense ministry digital procurement (UZ MoD, KG MoD) is opaque. Both countries have biometric/AI capabilities procured for defense and internal security separately from civilian procurement.
- **What's needed**: Open-source research will not close this. Honest acknowledgment is the only path.

### G.2 No Chinese vendor footprint depth
- **GAP**: Huawei, ZTE, Alibaba presence in CA digital infrastructure is opaque. Press releases exist but project-level data is limited.
- **What's needed**: Specialist Chinese-language research; sntz.ai may have insights via partner networks.

### G.3 No private-sector procurement crossover
- **GAP**: Some "B2G" opportunities are actually B2B with state-controlled enterprises (SOE banks, telcos, utility SOEs). The boundary is fuzzy. This research focused on direct ministry procurement.
- **What's needed**: SOE procurement tracking (separate exercise).

---

## Section H: Recommended Closure Priority

**Top 5 gaps to close before next deliverable:**

1. **UDP structural regulations baseline (KG)** — wait until ~31 May 2026, then re-baseline 18+ KG records that depend on Mintsifry-era role assignments.
2. **UZ-LAW-2026-1125 verification** — confirm law existence or remove citations.
3. **Donor dyad completion** — 17 missing dyad pairs.
4. **russian_cis_fit recomputation** — apply downward correction across ~30 initiatives.
5. **Tier-1 LinkedIn URL Sonar Pro pass** — verify top 8 most operationally critical individuals.

**Top 3 known-unknown gaps to acknowledge in honesty section:**

1. Defense / internal security digital procurement (both countries)
2. Chinese vendor (Huawei/Alibaba/ZTE) footprint depth
3. Post-UDP-restructuring KG digital institutional shape (~3-month uncertainty window)

---

(End of gaps.md)
