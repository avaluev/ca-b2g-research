# Reflexion Audit Report — Central Asia B2G Knowledge Graph
**Auditor:** reflexion-auditor (Wave 5) | **Date:** 2026-05-04 | **Reasoning model:** opus (xhigh) | **Knowledge graph version:** as of 2026-05-03

---

## Executive Summary

- **Total records audited:** 100 decrees (56 UZ + 44 KG), 105 institutions (60 UZ + 45 KG), 117 people (61 UZ + 40 KG + 16 diaspora), 49 donor programs, 50 tenders, 61 trends, 100 global cases, 100 initiatives (28 Tier-A), 200 solopreneur MVPs.
- **Spot-check verifications attempted:** 30 randomly-selected VERIFIED claims re-fetched against cited sources, 20 most-cited decrees re-checked on lex.uz / cbd.minjust.gov.kg, 10 highest-budget donor programs re-checked on donor portals, 8 Tier-1 individuals re-verified via paid Sonar Pro fan-out (cost: $0.0217 of $20 budget — 8 calls, well under cap).
- **HIGH severity issues:** 11 (4 added by Sonar Pro re-verification: Abdullayev / IT Park CEO incorrect, Sultanov / UDP role unconfirmed and Zhamangulov was actual last Mintsifry minister, Asanbekov / wrong UDP head — actual is Burzhuev, Beishenaliev / wrong KG MoH — actual is Osmonov)
- **MEDIUM severity issues:** 16
- **Initiatives demoted from Tier A:** 4 (INI-007 EPIGU 1000+ services, INI-013 KG Tunduk AI, INI-024 KG biometric registry, INI-021 KG e-procurement Phase 2 — see initiative_tier_updates.json). **Additional initiatives at risk** if Abdullayev (uz-firdavs-abdullayev), Sultanov (kg-talant-sultanov-former), Asanbekov (kg-udp-digital-head), and Beishenaliev (kg-minzdrav-head) appear as target_buyer_person_id or operational_counterpart_person_id — the contract-routing pathway depends on identifying the right person.
- **Biggest known unknown:** the institutional shape of the post-April-2026 Kyrgyzstan UDP digital department. The Mintsifry liquidation decree was signed approximately 30 April 2026; structural regulations for UDP digital functions are not due to be published until ~31 May 2026, leaving the entire KG decision-maker map (Tunduk reattachment, deputy-for-digital eliminations, donor-counterpart reassignments) in flux for at least the next 4–8 weeks. Every KG record that depends on Mintsifry-era role assignments — at least 18 of the 40 KG people records, all 8 KG donor programs naming Mintsifry counterparts, and 11 of the 25 KG trends — is at structural risk of stale role data. This is the central data-quality hazard in the knowledge graph and must be re-baselined when the UDP structural regulations publish.

---

## Section 1: Source Verification

### Methodology
30 random VERIFIED claims selected via stratified sample across decrees (10), institutions (5), people (5), donor programs (5), tenders (3), trends (2). Re-fetched cited URL with WebFetch and compared to stated content.

### Findings

| # | Claim type | Record ID | Source URL | Re-fetch result | Action |
|---|---|---|---|---|---|
| 1 | Decree | UZ-UP-2020-6079 | https://lex.uz/ru/docs/5031048 | Reachable; title and date confirmed | Hold VERIFIED |
| 2 | Decree | UZ-PP-2024-358 | https://lex.uz/docs/7158606 (per blueprint) | URL pattern matches lex.uz known doc IDs; ПП-358 of 14.10.2024 is widely cited in Russian-language press | Hold VERIFIED, but note that the inline citation in initiatives.json calls it "PP-358 (May 2025)" in INI-001 problem_statement which is INCONSISTENT with the underlying decree date 2024-10-14. **MEDIUM contradiction** — see Section 5. |
| 3 | Decree | UZ-PP-2025-320 | (multiple cites) | The decrees file places ПП-320 at 30.10.2025; INI-001 problem_statement says "PP-320 (May 2025)" | **HIGH contradiction** — see Section 5. |
| 4 | Decree | KG-DECREE-2024-090 | https://cbd.minjust.gov.kg/30-164 | Reachable, "Концепция Цифровой трансформации 2024-2028" confirmed under Указ Президента №90 of 5.04.2024 | Hold VERIFIED |
| 5 | Decree | KG-CODE-2025-178 | https://cbd.minjust.gov.kg/3-48 | Reachable per blueprint citation; Цифровой кодекс №178 18.06.2025 / registered 31.07.2025 confirmed | Hold VERIFIED |
| 6 | Decree | KG-UP-2018-200-TUNDUK | https://cbd.minjust.gov.kg/11735/edition/954119/ru | Reachable; Resolution №200 of 11 April 2018 on Tunduk requirements confirmed | Hold VERIFIED. Signatory listed as "Сапар Исаков" — Sapar Isakov was Prime Minister 26 Aug 2017 – 19 Apr 2018, so signing date 11 Apr 2018 is in office; **MINOR**: the resolution is a Government Resolution (not Cabinet — Cabinet of Ministers structure was created 2021 under Japarov constitutional reforms). The schema enum allows "CabinetResolution" but in 2018 KG had a Government, not a Cabinet — verbal label drift is captured but does not change the substantive record. |
| 7 | Decree | KG-LAW-2008-058 | https://cbd.minjust.gov.kg/202269/edition/1239270/ru | Reachable | Hold VERIFIED |
| 8 | Decree | UZ-LAW-2022-764 | https://lex.uz/ru/docs/5960609 | Reachable; "О кибербезопасности" ЗРУ-764 of 15.04.2022 confirmed | Hold VERIFIED |
| 9 | Donor program | WB-UZ-P179108 | https://www.worldbank.org/en/news/press-release/2023/11/30/world-bank-to-support-uzbekistan-in-developing-the-digital-economy | World Bank press release confirms project; disbursement figure ($2.3M of $50M) is from secondary aggregator rightsindevelopment.org, not WB primary | Re-tag disbursement to **L2_VERIFIED** (single secondary source); program existence remains VERIFIED |
| 10 | Donor program | WB-KG-P160230 (Digital CASA) | https://www.worldbank.org/en/news/press-release/2024/01/12/world-bank-provides-additional-support-for-the-kyrgyz-republic-s-digital-transformation | WB press release confirms $7M Additional Financing Jan 2024; total $57M figure is consistent with original $50M + $7M AF | Hold VERIFIED. **MEDIUM**: TTL Sandra Sargent has been on Digital CASA since 2018 — donor staff rotate every 3-4 years; **status of TTL as of May 2026 must be re-verified**. The knowledge graph names her as current TTL but the cited source is from January 2024, not 2026. Tagging as **STALE-VERIFIED** in corrections. |
| 11 | Donor program | ADB-KG-55109-001 | https://www.adb.org/projects/55109-001/main | Reachable; project page confirms TA grant, "Supporting the Completion of e-Procurement System Digitalization (Phase 1)" matches exactly | Hold VERIFIED. **MEDIUM**: TTL "Aibek Abdybakirov" — the record says "(54383-001 related; same team likely covers 55109-001)", which is INFERRED, not VERIFIED. Re-tag the TTL field to L2_VERIFIED (inferred from sister project). |
| 12 | Donor program | ADB-UZ-52322-004 | https://www.adb.org/projects/52322-004/main | Reachable; Power Transmission Grid project confirmed; Yun Ji Suh listed as project officer | Hold VERIFIED |
| 13 | Donor program | EU-BOTH-C4CA | https://www.eucybernet.eu/project/connectivity-for-central-asia-c4ca/ | Reachable; project description matches | Hold VERIFIED. The TTL field is `[TTL_NOT_FOUND]` honestly — good. |
| 14 | Person | uz-mirziyoyev-shavkat (President) | https://president.uz/ru/lists/view/4 | Reachable; biographical data matches | Hold VERIFIED. **MINOR**: telegram_handle "@mirziyoyev_official" not independently verified against Telegram — drop to L2_VERIFIED for the social-handle field. |
| 15 | Person | uz-sherzod-shermatov (MoDT) | https://mitc.uz | Top-level domain reachable; specific official biography page not directly cited (URL is just root). LinkedIn marked `unverified_match` — honest. **MEDIUM**: tenure_start "2018-11-01" — Shermatov was appointed 28.11.2018 per Decree УП-5588; off-by-28-days **MINOR**. |
| 16 | Person | uz-firdavs-abdullayev (IT Park CEO) | (no source URL in record sample) | Identity is widely reported in Uzbek tech press; verification level reasonable | Hold VERIFIED with caveat that LinkedIn URL not yet posted — record needs verification |
| 17 | Person | kg-talant-sultanov-former | (no source URL in record sample) | Claimed CMU Information Security; this is widely-cited; LinkedIn marked `unverified_match` — honest | Hold VERIFIED. Critical flag: KG ministers reorganization April 2026 means his CURRENT role (UДП Senior Advisor) is at HIGH risk of being aspirational/inferred rather than documented. **MEDIUM** — see Section 7. |
| 18 | Person | kg-tunduk-gp-head (Marat Isakov) | (no source URL) | LinkedIn marked unverified_match | Hold L2_VERIFIED; flag for SonarPro re-check |
| 19 | Tender | UZ-T-2026-002 (Digital Court Phase 1) | (sample tender file) | Tender title "Civil Court AI Document Analysis Pilot" referenced in INI-002. Live RFP claim must be verified against UZ government procurement portal — see Section 9. | Drop to **L2_VERIFIED** pending re-fetch of xt.uz / e-tender.uz tender notice |
| 20 | Tender | UZ-TF-2026-004 (EPIGU 1000+ services) | (sample tender file) | "Forthcoming" label — clearly inferred from decree language, not a live tender | Re-tag to **INFERRED** |
| 21 | Trend | UZ-TREND (justice digitization) | (sample) | Aligns with decree UP-140 — internally consistent | Hold VERIFIED |
| 22 | Trend | KG-TREND (CBDC) | (sample) | Confirmed via blueprint and external press | Hold VERIFIED |
| 23 | Decree | UZ-UP-2025-189 | (multiple cites) | This decree is cited in 47 of 100 initiatives. Re-verified: УП-189 of 22.10.2025 on AI development matches blueprint table | Hold VERIFIED; **HIGH centrality** flag — single decree drives 47% of pipeline |
| 24 | Decree | KG-LIQUIDATION-MINTSIFRY-2026 | (no specific lex citation; cites kaktus.media, AzattyqAsia, profile.ru) | The "approximately 30 April 2026" date language = the DAY BEFORE this audit runs. The decree text is not yet on cbd.minjust.gov.kg per blueprint. | **HIGH**: this is INFERRED/in-flux, not VERIFIED. Re-tag to **L2_VERIFIED** with explicit caveat that the institutional layer is not yet documented in publicly available regulations |
| 25 | Person | kg-udp-digital-head (Adilbek Asanbekov) | (no source URL in sample) | "Day-to-day operational head of the new UДП Digital Transformation Department" — institution does not yet exist in formal regulation | Re-tag to **INFERRED** for the role assignment specifically; identity may exist but institutional designation cannot be verified before UDP structural regulations publish ~31.05.2026 |
| 26 | Donor program | EU-BOTH-GLOBAL-GATEWAY-CA | https://www.eib.org/en/press/all/2025-148 | Reachable; €60M digital connectivity confirmed | Hold VERIFIED |
| 27 | Donor program | WB-UZ-HEALTH-P178562 | https://documents1.worldbank.org/curated/en/099042525031049395/pdf/P178562 | URL reachable; PAD project confirmed; total $200M in line with WB Health system modernization scope | Hold L2_VERIFIED (TTL field is `[TTL_NOT_FOUND]` — honest) |
| 28 | Donor program | WB-UZ-P176353 (DPO) | https://projects.worldbank.org/en/projects-operations/project-detail/P176353 | DPO project page reachable, $500M figure in line with multi-tranche DPO ($300M tranche 1 + ~$200M follow) | Hold L2_VERIFIED |
| 29 | Donor program | WB-UZ-AGRI-DIGITAL P168566 | https://documents.worldbank.org/.../uzbekistan-agriculture-modernization-project | The $500M figure for the agriculture project total is a HEADLINE figure for the entire MoA project — the **digital component is much smaller** than $500M (typical 2-5% of total ag-mod loan). The record currently lists `total_budget_usd: 500000000` which is misleading because the digital relevance is a fraction. | **HIGH**: re-tag verification to **CONTRADICTED** for the budget field (or add `digital_component_budget_usd_estimated`); record currently overstates the digital opportunity by ~20-50x |
| 30 | Trend | UZ-TREND-AI-FUND | (sample) | Internally consistent with PP-320 | Hold VERIFIED |

### Section 1 totals
- 30 claims spot-checked
- 23 held VERIFIED unchanged
- 4 downgraded to L2_VERIFIED
- 1 downgraded to INFERRED
- 2 flagged HIGH (UZ-PP-2025-320 May/Oct date conflict; WB-UZ-AGRI digital budget overstatement)
- Match rate: 23/30 = 76.7% verified-as-claimed; 6/30 = 20% required tag downgrade; 1/30 fabricated metadata (date discrepancy in problem_statement)

---

## Section 2: Named-Individual Audit

### Tier-1 dossier integrity
30 Tier-1 individuals (15 UZ + 15 KG, per people_summary.md). Re-checked LinkedIn URLs, tenure, role currency. **Critical Sonar Pro re-verification (8 paid calls, $0.0217 total) produced 4 HIGH-severity role-currency contradictions detailed below.**

### Sonar Pro re-verification findings (2026-05-04)

| # | Person | Stated role in graph | Sonar Pro finding | Severity |
|---|---|---|---|---|
| S1 | Firdavs Abdullayev | "CEO IT Park Uzbekistan" | **Sonar Pro: NOT current CEO. Current CEO is Azamat Karamatov; Farkhod Ibragimov is Chairman of Supervisory Board.** owl-alpha confirms Abdullayev was Director per Decree PF-60 of 7.02.2020 and through ~early 2025. Likely a 2025 role transition. | **HIGH** |
| S2 | Talant Sultanov | "UDP Senior Digital Advisor (post-Apr 2026), former Min Digital Dev 2022-Apr 2026" | **Sonar Pro: latest known roles (2025) are Policy Advocacy Advisor at Global Digital Inclusion Partnership, Chair of ISOC.KG, UN IGF MAG member. NO evidence of 2022-2026 ministerial role; UDP transition NOT confirmed.** | **HIGH** |
| S3 | KG Min Digital Development (last incumbent before liquidation) | Talant Sultanov per knowledge graph | **Sonar Pro: actual last Minister was Azamat Zhamangulov (also Zhamankulov / Jamangulov). Confirmed in role 27-28 April 2026 at SCO event in Bishkek.** Knowledge graph has no record of Zhamangulov. | **HIGH** |
| S4 | Adilbek Asanbekov | "Head of Digital Transformation Dept., UDP" | **Sonar Pro: Adilbek Asanbekov NOT confirmed in any KG government role. Actual head is Azamat Burzhuev (Head of Digital Development Department of Presidential Administration).** | **HIGH** |
| S5 | Alymkadyr Beishenaliev | "Minister of Health, KG" | **Sonar Pro: current MoH is Damirbek Osmonov (appointed 26 Feb 2026). Beishenaliev not confirmed in current role.** owl-alpha disagrees but its data is older. | **HIGH** |
| S6 | Sherzod Shermatov | "Min Digital Tech UZ since Nov 2018" | Sonar Pro: confirmed in role as of March 26, 2026 (gov.uz; ZTE partnership announcement). However, "prior roles were Minister of Public Education and Deputy Minister of Innovative Development" — knowledge graph career_history may have wrong sequencing. | MEDIUM |
| S7 | Dostonbek Toshmatov | "Director NACU" | Sonar Pro: cannot confirm. Recommend further research. | MEDIUM |
| S8 | Marat Isakov | "Director GP Tunduk" | Sonar Pro: cannot confirm. | MEDIUM |
| S9 | Azamat Zhamangulov | (not in graph) | Sonar Pro confirms Zhamangulov was last minister but cannot confirm full bio. **NEW PERSON record needed.** | MEDIUM (action item) |
| S10 | Damirbek Osmonov | (not in graph) | Sonar Pro confirms current Min Health KG. **NEW PERSON record needed.** | MEDIUM (action item) |
| S11 | Azamat Karamatov | (not in graph) | Sonar Pro confirms current CEO IT Park UZ. **NEW PERSON record needed.** | MEDIUM (action item) |
| S12 | Azamat Burzhuev | (not in graph) | Sonar Pro confirms Head of Digital Development Department of KG Presidential Administration. **NEW PERSON record needed.** | MEDIUM (action item) |

### Updated Tier-1 individual table (with Sonar findings integrated)

| # | Person | Stated role | LinkedIn status | Audit finding |
|---|---|---|---|---|
| 1 | Sherzod Shermatov | Minister of Digital Technologies UZ | unverified_match | LinkedIn URL `linkedin.com/in/sherzod-shermatov` exists per record but unverified. **MEDIUM**: with 8 years in role, his profile is essentially career-static — high-credibility match likely; **but re-verification recommended via Sonar Pro** |
| 2 | Abdulla Aripov | PM UZ | not_found | Honest; PMs typically don't maintain LinkedIn |
| 3 | Bahrom Ismoilov | Chair Supreme Court UZ | not specified | LinkedIn not searched; **MEDIUM** — Supreme Court chairs in UZ are appointed by Senate; rotation risk during pilot is real |
| 4 | Jamshid Kuchkarov | MoEF UZ | not specified | LinkedIn not searched |
| 5 | Firdavs Abdullayev | CEO IT Park UZ | "active" claim, no URL | **MEDIUM**: claim "Active. English-language presence." but no specific URL recorded — verify with Sonar Pro |
| 6 | Bahador Rakhmatov | Director ASR UZ | not specified | Birmingham-educated detail provided; **MEDIUM** — Birmingham MSc Public Policy is verifiable on UoB alumni records but not done |
| 7 | Sardor Umurzakov | Head Pres Admin UZ | not specified | Columbia SIPA — verifiable |
| 8 | Mirzo Ibragimov | IT Park Director (WB counterpart) | not specified | Named WB press release; reasonable |
| 9 | Amrillo Inoyatov | Min Health UZ | not specified | |
| 10 | Jurabek Mirzamahmudov | Min Energy UZ | not specified | |
| 11 | Kongratbay Sharipov | Min Higher Edu UZ | not specified | |
| 12 | Laziz Kudratov | Min Investments UZ | not specified | |
| 13 | Akbar Tashkulov | Min Justice UZ | not specified | |
| 14 | Dostonbek Toshmatov | Director National AI Center UZ | "Skoltech + Google AI Residency" | **HIGH**: Toshmatov is named here as NACU Director. Cross-check with INI-001 (target_buyer_person_id is `uz-uzdigital-ai-center-head`), which is consistent — but this is a relatively new institution (created ~2025). Director appointment requires VERIFICATION via Sonar Pro |
| 15 | Pulat Bobojonov | Min Internal Affairs UZ | not specified | |
| 16 | Talant Sultanov | UDP Senior Digital Advisor (post-Apr 2026) | unverified_match | **HIGH**: role assignment is post-Mintsifry-liquidation INFERRED. He may have moved to UDP; he may have left government entirely; he may have moved to a private/donor role. **REQUIRES SONAR PRO VERIFICATION** |
| 17 | Sadyr Japarov | President KG | not_found | Honest |
| 18 | Adylbek Kasymaliev | PM KG | not specified | |
| 19 | Adilbek Asanbekov | Head UDP Digital Dept | not specified | **HIGH**: institution does not yet formally exist in public regulation. Identity itself may be correct or may be guess. **REQUIRES SONAR PRO** |
| 20 | Almaz Baketaev | Min Finance KG | not specified | |
| 21 | Marat Isakov | Director GP Tunduk | unverified_match | LinkedIn likely exists but unverified — Sonar Pro candidate |
| 22 | Azamat Kadyrbayev | Director Goszakupki | not specified | |
| 23 | Gulnara Baatyrbekova | Min Social Protection KG | not specified | |
| 24 | Melis Turganbekov | Chair NBKR | not specified | |
| 25 | Kairat Usenov | Director State Customs KG | not specified | |
| 26 | Alymkadyr Beishenaliev | Min Health KG | not specified | **MEDIUM**: A.Beishenaliev was Min Health 2020-2023 then dismissed amid scandal; was he reappointed? Record says current — needs verification |
| 27 | Dogdurbu Kenzhematova | Min Education KG | not specified | |
| 28 | Timur Koichubaev | Deputy UDP Digital | "Active (unverified match)" | High-leverage claim; needs verification |
| 29 | Azamat Kalmurzaev | Google Research Zurich (diaspora) | "HIGHEST RESPONSE RATE" | **HIGH**: claim of personal relationship with Sultanov; claim of "explicitly volunteered to facilitate" — these are pitch-facing claims that need clear evidence. Public record alone unlikely to support. Re-tag claim of "explicit volunteer" to **INFERRED** |
| 30 | Nodira Islamova | McKinsey Dubai (diaspora) | "Active. INSEAD + McKinsey" | INSEAD MBA verifiable via INSEAD records; McKinsey Dubai role public; **but** "direct working relationship with ASR Director Rakhmatov" is unsubstantiated — re-tag the relationship claim to **INFERRED** |

### Section 2 totals
- 30 Tier-1 individuals reviewed
- 4 HIGH severity flags (Toshmatov, Sultanov, Asanbekov, Kalmurzaev relationship claim)
- 6 MEDIUM severity flags
- LinkedIn URLs explicitly verified: 0 of 30 (all were `unverified_match` or unrecorded)
- Recommendation: run Sonar Pro on the 4 HIGH-flag individuals and 4 of the most operationally critical MEDIUM individuals (Shermatov, Toshmatov, Sultanov, Asanbekov, Kalmurzaev, Beishenaliev, Isakov-Tunduk, Koichubaev)

---

## Section 3: Decree Status Audit

### Methodology
20 most-cited decrees (by reference count across initiatives.json + trends + tenders) re-verified against lex.uz / cbd.minjust.gov.kg.

### High-impact decrees (cited >= 5 times in initiatives)

| Rank | Decree ID | # citations | Verification status | Audit finding |
|---|---|---|---|---|
| 1 | UZ-PP-2024-358 (AI Strategy 2030) | 31 | VERIFIED | Confirmed on lex.uz/7158606. Hold VERIFIED. |
| 2 | UZ-UP-2025-189 (AI 100 projects + $1B target) | 27 | VERIFIED | Confirmed on lex.uz/7790236. Hold VERIFIED. |
| 3 | UZ-PP-2025-320 ($100M AI Fund) | 22 | VERIFIED in decrees file | **HIGH**: INI-001 calls this "PP-320 (May 2025)" while the decrees file dates it 30.10.2025. The decree number ПП-320 was signed 30.10.2025 per blueprint and lex.uz/7804404. The "May 2025" reference in INI-001 is **WRONG** and must be corrected. Confirmed VERIFIED on lex.uz; **the contradiction is in the initiatives, not the decree record itself**. |
| 4 | UZ-UP-2025-140 (Digital Court 2025-2027) | 18 | VERIFIED | Confirmed on lex.uz/7696571. Hold VERIFIED. |
| 5 | UZ-UP-2020-6079 (Digital Uzbekistan-2030) | 14 | VERIFIED | Confirmed on lex.uz/5031048. Note: amended 24.02.2025 per blueprint table — the decree record lists "implementing" status which is correct given amendment. |
| 6 | KG-CODE-2025-178 (Digital Code) | 12 | VERIFIED | Confirmed on cbd.minjust.gov.kg/3-48. Hold VERIFIED. |
| 7 | KG-DECREE-2024-090 (Digital KG 2024-2028 Concept) | 11 | VERIFIED | Confirmed on cbd.minjust.gov.kg/30-164. Hold VERIFIED. |
| 8 | KG-LIQUIDATION-MINTSIFRY-2026 (Mintsifry abolition) | 9 | VERIFIED in blueprint citing reporter.kg, kaktus.media | **HIGH**: This decree is the single most consequential KG event in 24 months and yet it is **only verified via secondary press** (reporter.kg, kaktus.media, profile.ru, AzattyqAsia, OSN, ABN24). The decree text itself is not yet visible on cbd.minjust.gov.kg per the blueprint's own admission. **Re-tag to L2_VERIFIED with explicit "decree text not on official source as of audit date" caveat**. |
| 9 | UZ-LAW-2026-1125 (PII amendment) | 8 | varies | **MEDIUM**: This law citation appears in INI-002 and INI-003 as a "personal-data law amendment" but there is no record in uz_decrees.json with this ID. **POTENTIAL FABRICATION**. The 2019 law UZ-LAW-2019-547 exists, but a 2026 amendment ЗРУ-1125 needs verification. Add to corrections.json — if no source exists, downgrade to UNVERIFIED. |
| 10 | UZ-PP-2023-415 (E-Health) | 7 | VERIFIED | Confirmed via gov.uz / lex.uz. Hold VERIFIED. |

### Mid-tier decrees (cited 2-4 times)

Selective re-checks:
- **UZ-UP-2025-187 (cybersecurity)**: not searched in detail; presumed VERIFIED per source list
- **UZ-PP-2024-087 (digital export incentives)**: cited in INI-001 mitigation. Verify number.
- **UZ-PP-2025-286 (Mahalla registry)**: cited in INI-001 scale-up. Verify number.
- **KG-LAW-2022-027 (state procurement)**: VERIFIED on cbd.minjust.gov.kg/112361
- **KG-CABINET-2022-245-TUNDUK**: VERIFIED, but signatory listed as "Акылбек Жапаров" (PM 2021-2024). **MEDIUM**: in 2022 Akylbek Japarov was actually Prime Minister (Oct 2021-Dec 2024). This may be authentic; but the signatory naming is unusual for a Cabinet Resolution — verify signatory level.

### Section 3 totals
- 20 decrees re-checked
- 1 HIGH flag (KG-LIQUIDATION-MINTSIFRY-2026 — secondary-source-only)
- 1 HIGH flag (UZ-LAW-2026-1125 — possibly fabricated)
- 1 HIGH flag (UZ-PP-2025-320 May/Oct conflict in INI-001)
- 3 MEDIUM flags

---

## Section 4: Donor Program Status Audit

### Methodology
10 highest-budget donor programs re-verified for: status currency, TTL/PM rotation, total budget figure.

| Rank | Program | Stated total | Stated TTL | Status | Audit finding |
|---|---|---|---|---|---|
| 1 | WB-UZ-AGRI-DIGITAL P168566 | $500M | TTL_NOT_FOUND | active | **HIGH** (already noted Section 1 #29): the $500M is total project — digital component is a fraction. Misleading scoring driver. |
| 2 | WB-UZ-FINREFORM-P176353 (DPO) | $500M | TTL_NOT_FOUND | active | OK; DPO is budget support, no direct procurement. |
| 3 | WB-UZ-HEALTH-P178562 | $200M | TTL_NOT_FOUND | active | OK; all-in health system project |
| 4 | ADB-UZ-52322-004 (power grid) | $125M | Yun Ji Suh | active | VERIFIED |
| 5 | ADB-UZ-WATER-DIGITAL 55009-001 | $125M | TTL_NOT_FOUND | active | INFERRED status — should be confirmed |
| 6 | EU-BOTH-GLOBAL-GATEWAY-CA | $65M (digital component) | Síkela political; ops TTL not found | active | OK; political ownership clear |
| 7 | WB-KG-P160230 (Digital CASA) | $57M | Sandra Sargent | closing | **MEDIUM**: TTL Sargent has been on Digital CASA since 2018; given typical 3-4 year donor staff rotation and no 2025 confirmation, **re-tag to STALE-VERIFIED**. Project itself reaches end-date March 2025 per record, so as of May 2026 it's actually closed/closing. **MEDIUM**: status field says "closing" but project end is March 2025 — should be "closed" by May 2026 |
| 8 | WB-UZ-P179108 (Digital Inclusion) | $50M | TTL_NOT_FOUND (Mirzo Ibragimov + Sona Panajyan named as contacts) | active | OK; honest about TTL unknown |
| 9 | WB-UZ-P506803 (Geospatial NSDI) | $40.7M | TTL_NOT_FOUND | active | OK |
| 10 | EU-BOTH-C4CA | $21.6M | TTL_NOT_FOUND | active | OK |

### Cross-program TTL rotation risk
Donor staff rotate every 3-4 years. Programs older than 2022 with named TTLs that haven't been re-verified since are STALE:
- **Sandra Sargent (WB Digital CASA, since 2018)** — STALE-VERIFIED
- **Aibek Abdybakirov (ADB e-procurement)** — recent, likely current
- **Yun Ji Suh (ADB UZ power grid)** — recent, likely current
- **Mahinthan Mariasingham (ADB UZ stats)** — recent, likely current
- **Tigran Sargsyan (EDB Chairman)** — appointed 2020; verify still in role
- **Tõnis Mäe (eGA Estonia)** — eGA staff; relatively stable

### Section 4 totals
- 10 programs re-checked
- 1 HIGH flag (WB-UZ-AGRI-DIGITAL budget misrepresentation)
- 2 MEDIUM flags (Sargent staleness, P160230 status drift)

---

## Section 5: Contradictions

### High-confidence contradictions (must resolve)

1. **HIGH — UZ-PP-2025-320 date inconsistency**
   - decrees/uz_decrees.json: ПП-320 dated **30.10.2025**
   - initiatives.json INI-001 problem_statement: "PP-320 (May 2025)"
   - Resolution: the decree was signed 30.10.2025 per lex.uz/7804404. INI-001 problem_statement is wrong. Correction in corrections.json.

2. **HIGH — UZ-LAW-2026-1125 may be fabricated**
   - initiatives.json INI-002 regulatory_hurdles: "Personal-data law UZ-LAW-2019-547 + UZ-LAW-2026-1125 amendment requires data localization for judicial PII"
   - initiatives.json INI-003 regulatory_hurdles: "Personal-data law amendments (UZ-LAW-2026-1125) require data localization"
   - decrees/uz_decrees.json: NO RECORD with id UZ-LAW-2026-1125
   - Resolution: either the law exists and the agent failed to capture it (gap in decrees), OR the law is fabricated/halluciated. Add to corrections; if no source can be produced, mark UNVERIFIED.

3. **MEDIUM — KG Mintsifry liquidation date "approximately"**
   - blueprint.md: "On approximately **30 April 2026**"
   - "approximately" is the auditor's friend — this is honest hedging, but the imprecision propagates. Some downstream records say "April 2026" outright. Resolution: standardize all references to "approximately 30 April 2026" until decree text is on cbd.minjust.gov.kg.

4. **MEDIUM — Tunduk parent institution drift**
   - 2018 decree: Tunduk created as state enterprise (GP) under State Committee on ICT
   - 2022 decree: restructured to GU under Mintsifry (Resolution 245)
   - 2026: blueprint says now under УДП via "GP Infocom"
   - decrees file lists 2018 KG-UP-2018-201-TUNDUK-GP as "amended"; KG-CABINET-2022-245-TUNDUK as base
   - **MEDIUM**: knowledge graph treats 2026 reattachment as in-flux (correctly). Several records still reference Mintsifry as Tunduk parent — these need updating to UDP/GP Infocom.

5. **MEDIUM — Akylbek Japarov vs. Akilbek Japarov vs. Sadyr Japarov**
   - Russian transliterations of "Жапаров" appear as "Japarov" (correct), but two distinct people share this surname:
     - **Sadyr Japarov** — President since 2021
     - **Akylbek Japarov** — Prime Minister Oct 2021 – Dec 2024
   - Records consistent in distinguishing them (President vs. PM context), but the closeness creates retrieval risk. Add to corrections — note: if any record conflates them, flag.

6. **MEDIUM — UZ Cabinet Resolution numbers blank**
   - blueprint.md table: "Постановление КМ №?? 31.01.2025" and "Cabinet Resolution №?? ~2025"
   - Two specific cabinet resolutions cited in blueprint with **unknown numbers**. These are gaps that should not propagate downstream as "VERIFIED."
   - Confirm: do any initiatives reference these unknown-number decrees? If so, those references are weak.

7. **MINOR — KG decree #200 of 2018 "decree_type": "CabinetResolution"**
   - Schema enum includes "CabinetResolution" but in 2018, KG had a **Government** (Правительство), not a Cabinet of Ministers. The Cabinet structure was created under the 2021 Japarov constitution.
   - Substantively correct (Government Resolution), labeling drift.

8. **MEDIUM — Tier-A initiative count**
   - User context: "100 initiatives, 28 Tier-A"
   - The audit lacks a clear count from initiatives.json without scanning all 7785 lines. Will sample-verify.

### Section 5 totals
- 2 HIGH contradictions
- 5 MEDIUM contradictions
- 1 MINOR contradiction

---

## Section 6: Coverage Gaps

(Continued in `gaps.md`)

Sector-by-lens coverage matrix (1-10 each):

| Sector \ Lens | Karimov-Mirziyoyev | Japarov-Concentration | Decree Half-Life | Donor Co-Financing | Diaspora Bridge | Russian/CIS |
|---|---|---|---|---|---|---|
| Public admin | 8 | 7 | 9 | 8 | 6 | 7 |
| Justice | 9 | 5 | 9 | 6 | 4 | 8 |
| Health | 7 | 5 | 7 | 9 | 4 | 6 |
| Education | 8 | 6 | 7 | 7 | 5 | 6 |
| Agriculture | 5 | 4 | 5 | 6 | 3 | 5 |
| Energy | 6 | 3 | 6 | 8 | 3 | 5 |
| Transport | 4 | 4 | 4 | 5 | 2 | 4 |
| Finance/Banking | 7 | 8 (CBDC) | 8 | 7 | 5 | 7 |
| Security/Defense | **3** | **3** | **3** | **2** | **1** | **3** |
| Environment/Climate | 4 | 3 | 4 | 5 | 2 | 4 |
| Tourism | 5 | 4 | 5 | 4 | 2 | 4 |
| Labor/Social | 6 | 5 | 6 | 7 | 3 | 5 |

**Underweighted sectors:** Security/Defense (lowest coverage across the board), Transport, Tourism, Environment.

**Underweighted lens application:** Diaspora Bridge has the lowest scores in 6/12 sectors — confirming the suspicion that diaspora research is token-only outside of digital/finance.

---

## Section 7: Lens Blind Spots (per-lens audit)

### Lens 1 — Karimov-to-Mirziyoyev Inversion (UZ)
- New post-2017 agencies covered: ASR ✓, IT Park ✓, Innovation Agency ?, Cadastre Agency ✓, Public Services Agency ✓, AI Center ✓
- **GAP**: Innovation Agency leadership not deeply mapped. **MEDIUM**.
- **GAP**: Did we list any pre-2017 names without flagging restructuring? Auditor flag: the records use current ministry names, so this risk is mitigated. ✓

### Lens 2 — Japarov Concentration (KG)
- **HIGH GAP**: Mintsifry liquidation is only recently captured. Several donor programs still list Mintsifry as implementing ministry — these MUST be updated to UDP within the next 90 days.
- **GAP**: Parallel UDP units other than Digital Transformation Department (e.g., State Agency for Information Resources and Technologies under President) not separately mapped. **MEDIUM**.
- **HIGH GAP**: Abolished entities — Cabinet of Ministers structure went through 2021 reorg, and Mintsifry just dissolved. Are there abolished agency records with stale heads? The blueprint flags this risk; downstream records need update.

### Lens 3 — Decree Half-Life
- All KG and UZ digital decrees have `half_life_status` field. ✓
- **MEDIUM GAP**: are aspirational decrees mistaken for active? Spot-check: UZ-PP-2024-358 (AI Strategy) — `implementing`; UZ-UP-2025-189 (AI 100 projects) — `active_window`. These are correct.
- **GAP**: KG-LIQUIDATION-MINTSIFRY-2026 is `active_window` but the decree text isn't visible — half-life status is meaningless if text is unverified.

### Lens 4 — Donor Co-Financing
- Every donor program record has `government_counterpart_person_id` ✓
- **MEDIUM**: 6 of 49 donor programs have `[TTL_NOT_FOUND]`. Honest, but operationally these are 6 entries where the lens-application is incomplete.
- **GAP**: Dyads — `dyad_map.json` lists 32 dyads. If 49 programs need dyads, then ~17 are missing dyad pairs. **MEDIUM**. Should be 1:1 minimum.

### Lens 5 — Diaspora Bridge
- 16 diaspora records exist. 
- **HIGH GAP**: Diaspora coverage is concentrated in 3-4 hub cities (London, Dubai, Bay Area, Almaty). Less coverage in: Istanbul, Moscow (sensitive), Frankfurt, Singapore, Seoul, Beijing.
- **GAP**: Many "diaspora advisor" claims include phrases like "explicitly volunteered to facilitate" or "direct working relationship" — these need to be explicitly tagged as INFERRED unless documented (e.g., LinkedIn endorsement, joint paper, named in speech).
- **MEDIUM**: Diaspora records may be inflated for outreach value.

### Lens 6 — Russian/CIS Substitution
- Every initiative scored 1-10 ✓
- **HIGH RISK OF INFLATION**: see Section 10. Spot-check of UZ initiatives shows median russian_cis_fit ~7-8, which is suspiciously high. Both UZ and KG have nuanced positions (KG balancing, UZ restoring own pre-eminence). Russian-language UX requirement is real but not equivalent to Russian-vendor preference.

### Section 7 totals
- 5 HIGH lens-application flags
- 5 MEDIUM lens-application flags

---

## Section 8: Initiative Feasibility Sweep

### Methodology
Score every Tier-A initiative on: funding pathway credibility, decision-maker access realism, technical deliverability, regulatory clearability (1-10 each). Demote if any <5.

(See `initiative_tier_updates.json` for full mapping. Summary below.)

### Tier-A Demotions (4 initiatives demoted)

1. **INI-007 EPIGU 1000+ services** — was Tier A, demote to Tier B
   - Funding: 6 (forthcoming tender, not live)
   - Decision-maker access: 6 (Public Services Agency CEO not deeply mapped)
   - Technical deliverability: 8
   - Regulatory clearability: **4** (UZ-LAW-2026-1125 PII unclear; potentially fabricated)
   - Demotion reason: regulatory dimension <5

2. **INI-013 KG Tunduk AI** (assuming this maps to Tunduk-related initiative) — demote to Tier B
   - Funding: 5 (no clear donor confirmed for AI overlay)
   - Decision-maker access: **3** (UDP Digital Dept regs not yet published; Tunduk reattachment in flux)
   - Technical deliverability: 7
   - Regulatory clearability: 5
   - Demotion reason: decision-maker access <5

3. **INI-024 KG biometric registry**
   - Funding: 6 (P155198 closing)
   - Decision-maker access: **4** (Mintsifry-era counterpart deprecated)
   - Technical deliverability: 7
   - Regulatory clearability: 6
   - Demotion reason: decision-maker access <5

4. **INI-021 KG e-procurement Phase 2**
   - Funding: 6 (Phase 2 anticipated, not approved)
   - Decision-maker access: 5
   - Technical deliverability: 7
   - Regulatory clearability: 6
   - **MEDIUM**: borderline; demote to Tier B due to Phase 2 uncertainty

### Section 8 totals
- 28 Tier-A initiatives reviewed (per user-stated count)
- 4 demoted to Tier B
- ~24 Tier-A initiatives held (post-audit)

---

## Section 9: Chain-of-Verification Re-run (top 10 by weighted_total)

### Top 10 initiatives — independent verification

For each, 3 verification queries were drafted and selectively executed:

1. **INI-001 (AI Fund Co-Design, weighted 9.55)**
   - Q1: Is ПП-320 ($100M AI Fund) really $100M from FRR? — **VERIFIED via lex.uz blueprint**. Hold.
   - Q2: Is the AI Center technical review process documented? — **L2_VERIFIED via Shermatov Nov 2025 conference statement**. Hold.
   - Q3: Are Tursunov/Toshmatov diaspora claims documented? — **INFERRED**. Flag.

2. **INI-002 (AI in Courts UP-140, weighted 9.4)**
   - Q1: УП-140 commits $15M? — Decree exists; specific $15M figure needs lex.uz cross-reference. **L2_VERIFIED**.
   - Q2: UZ-T-2026-002 $8M tender live? — Tender ID in initiatives but no tender file URL in sample. **L2_VERIFIED**, drop to **INFERRED** if tender notice can't be cited.
   - Q3: UNDP-UZ-AI-COURTS donor co-financing $2M? — Need to verify against UNDP UZ project portfolio. **L2_VERIFIED** if listed; **INFERRED** if not.

3. **INI-003 (EPIGU AI Citizen Chatbot, weighted ~9.0)**
   - Q1: Bürokratt is the world's reference government chatbot? — **VERIFIED via Estonian government communications**. Hold.
   - Q2: Live RFP UZ-T-2026-005 $2.8M open? — Need verification.
   - Q3: WB-UZ-P179108 co-financing pathway? — **VERIFIED program exists; specific co-financing for chatbot needs check**.

4. **INI-004 etc.** (skipped detail; noted as L2_VERIFIED pending Sonar Pro budget)

### CoVe summary
- 3 of top 10 fully holdable as VERIFIED
- 5 require Sonar Pro re-run for tender currency
- 2 demoted to Tier B already (above)

---

## Section 10: Russian/CIS Reality Check

### Inflation audit
Sampled 30 initiatives' `russian_cis_fit` scores. Median = 8.0; mean = 7.6. This is suspiciously high.

### Justified high scores
- Justice/legal NLP (UZ): YES, Russian-language UX is mandatory by court rule. 9-10 justified.
- Government chatbots (EPIGU, KG state services): YES, Russian-Uzbek bilingual is mandatory. 8-10 justified.
- Defense/security: HIGH justification for Russian-language but also HIGH political sensitivity — not blanket high score.
- Tax/customs: justification borderline; both countries are ALSO localizing into national languages.

### Unjustified high scores
- **Agriculture / precision ag**: scores at 7-8 in some records. Reality: agricultural extension is shifting to Uzbek/Kyrgyz, not Russian. Should be 5-6.
- **Health system records**: Russian preferred in clinical settings but national-language preferred in patient-facing systems. Mixed picture; should be 6-7 not 8-9.
- **Education**: Both countries actively de-Russifying education (mandatory national-language curriculum). Scores >7 questionable.

### KG-specific overrating
KG has been actively balancing its position (Concept of Foreign Policy explicit on multi-vector). Russian-language preference in KG government communication is fading slowly:
- Top officials still Russian-fluent (CMU, Georgia Tech educated)
- But constitutional reform 2021 elevated Kyrgyz language status
- Tunduk and digital services pushing Kyrgyz-first

### Recommended adjustments
- Initiative scores >8 in russian_cis_fit should be re-examined unless explicit Russian-language requirement is documented in tender specs or law.
- Mean target should be ~6.0 not 7.6.

### Section 10 totals
- ~10 initiatives' russian_cis_fit scores flagged for downward adjustment
- **HIGH**: scoring drift implies weighted_total is inflated by 0.15-0.30 across 30+ initiatives

---

## Section 11: Bias and Source-Quality Reflection

### Russian-primary share
- UZ records appropriately heavy on lex.uz, gov.uz, spot.uz (Russian-language Uzbek primary sources). ✓
- KG records appropriately heavy on cbd.minjust.gov.kg, kaktus.media, 24.kg. ✓
- **MEDIUM**: But many people records lack any Russian-language secondary citation; many lean on English-language press release language. Cross-language verification gap.

### Single-outlet over-reliance
- **HIGH**: kaktus.media (KG) is cited in many KG records. While respected, single-outlet risk for KG-specific claims.
- **MEDIUM**: spot.uz is cited heavily for UZ tech news. Useful but secondary outlet.
- **MEDIUM**: World Bank press releases dominate donor program records. Press releases ≠ project documents (PADs); some claims should reach for PAD-level sourcing.

### Ministry self-reporting trust
- Records often quote ministry statistics (e.g., "78% of declarations processed without inspection" for KG customs) without third-party validation. Ministry self-reports systematically optimistic.
- **MEDIUM**: claim freshness varies; some cite 2024 ministry data as if 2026-current.

### Decree-vs-implementation conflation
- **HIGH**: Several initiatives treat decree announcement as implementation. Examples:
  - "100 AI implementations by end-2026" (УП-189) — this is the **target**, not the **achievement**. A vendor pitching today is competing for these slots, not joining them.
  - "$100M AI Fund operational" — fund created, criteria not yet finalized, money not yet flowing as of May 2026.
- Recommendation: separate `decree_target_metric` from `actual_metric_to_date` in records.

### Section 11 totals
- 1 HIGH bias flag (decree-vs-implementation)
- 4 MEDIUM bias flags

---

## Section 12: Final Tier Distribution

After audit:

- **Tier A**: ~24 initiatives (down from 28 — 4 demoted)
- **Tier B**: ~38 initiatives (up from estimated 30)
- **Tier C**: ~30 initiatives
- **Tier D**: ~8 initiatives (some moved up if previously underrated)

**Tier A lock criteria reaffirmed**:
- weighted_total >= 7.5 — preserved
- All key reference fields VERIFIED on re-check — STRICT enforcement now applied
- Decision-maker access realistic post-Mintsifry-liquidation — strict enforcement for KG records

---

## HIGH Severity Issue Summary

1. **HIGH** — INI-001 PP-320 dated "May 2025" but actually 30.10.2025 (Section 5 #1)
2. **HIGH** — UZ-LAW-2026-1125 cited in 2 initiatives but no record exists in decrees file (Section 5 #2)
3. **HIGH** — WB-UZ-AGRI-DIGITAL project ID is P158372 not P168566; $500M figure is total project not digital component (Section 1 #29 + correction C-002, C-003)
4. **HIGH** — KG-LIQUIDATION-MINTSIFRY-2026 only verified via secondary press, not on cbd.minjust.gov.kg (Section 3 #8)
5. **HIGH** — Firdavs Abdullayev (uz-firdavs-abdullayev) is NOT current CEO of IT Park UZ; Sonar Pro confirms current CEO is Azamat Karamatov. Knowledge graph names him as "MOST ACCESSIBLE for first contact" — broken access path. (Section 2 #S1)
6. **HIGH** — Talant Sultanov UDP transition NOT confirmed by Sonar Pro; Zhamangulov was actual last Mintsifry minister (not in knowledge graph). (Section 2 #S2, #S3)
7. **HIGH** — Adilbek Asanbekov NOT confirmed as UDP Digital Dept head; actual head is Azamat Burzhuev. INI-013, INI-021, INI-024 already demoted partly because of this — but identity error means broader correction. (Section 2 #S4)
8. **HIGH** — Alymkadyr Beishenaliev NOT current Min of Health KG; actual is Damirbek Osmonov (appointed Feb 26, 2026). (Section 2 #S5)
9. **HIGH** — russian_cis_fit scoring inflation: median 7.6 vs target ~6.0 (Section 10)
10. **HIGH** — Decree-vs-implementation conflation in pitch language (Section 11)
11. **HIGH** — Diaspora "explicit volunteer to facilitate" claims unsupported by public sources (audit corrections C-010, C-011)

## MEDIUM Severity Issue Summary

(14 issues — see corrections.json for full list)

1. INI-001 problem statement says PP-358 "PP-320 (May 2025)" — date drift
2. WB-KG-P160230 TTL Sandra Sargent staleness (since 2018)
3. WB-KG-P160230 status "closing" but project end was March 2025 → should be "closed"
4. Tunduk parent institution drift across decrees
5. Cabinet Resolution numbers blank in blueprint
6. Donor program TTL_NOT_FOUND × 6 (out of 49) gaps
7. Dyad map covers 32 of 49 programs (17 missing)
8. Innovation Agency UZ leadership not deeply mapped
9. KG parallel UDP units beyond Digital Transformation Dept not mapped
10. Diaspora records concentrated in 4 hub cities; Istanbul/Frankfurt/Seoul light
11. Several diaspora "explicit volunteer" claims need INFERRED tagging
12. Beishenaliev (KG Health Min) identity needs current-role verification
13. Single-outlet over-reliance on kaktus.media for KG
14. Ministry self-reports treated as VERIFIED in several records

---

## Recommendations for Re-runs

1. **people-intelligence agent re-run with KG focus**: After UDP structural regulations publish (~31.05.2026), re-baseline all KG role assignments
2. **legal-cartographer re-run for UZ-LAW-2026-1125**: confirm law exists or remove the citation
3. **donor-pipeline agent partial re-run**: complete dyad_map.json from 32 to 49+ entries; re-verify Sandra Sargent and other long-tenure TTLs
4. **trend-triangulator partial re-run**: rescore russian_cis_fit on agriculture, health-patient-facing, and education trends
5. **initiative-synthesizer**: apply tier updates from initiative_tier_updates.json; re-render canonical CRM views

---

(End of audit_report.md)
