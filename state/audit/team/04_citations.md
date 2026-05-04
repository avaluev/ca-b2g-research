# Citation / Provenance Audit — Report 04
**Auditor:** Citation/Provenance (Slot 04) | **Date:** 2026-05-03 | **Site:** https://avaluev.github.io/ca-b2g-research/

---

## 1. Source-Language Distribution

Knowledge graph contains **718 source records** across decrees, institutions, people, donor programs, tenders, trends, global cases, and initiatives.

| Language | Count | Share |
|---|---|---|
| Russian (`ru`) | 381 | 53.1% |
| English (`en`) | 317 | 44.2% |
| Uzbek-Latin (`uz-latn`) | 9 | 1.3% |
| Other (fr, pt, tr, ko, mn, nl, pl, id, lv) | 11 | 1.5% |
| **Total** | **718** | — |

**Verdict: PASSES the ≥30% Russian/Uzbek/Kyrgyz threshold.** Regional languages (ru + uz-latn) account for 54.4% of sources. However, Kyrgyz-language sources are not tagged independently — they are folded into the `ru` bucket via the `ky_or_ru` compound label in the link checker. Separating the Kyrgyz tag in `state_schema.json` would improve traceability.

Link-report URL-level breakdown (716 URLs, separate from source records): English 346 (48.3%), Uzbek/Russian mixed 222 (31.0%), Kyrgyz/Russian mixed 140 (19.6%), Russian-only 8 (1.1%). Regional share at URL level: 51.7%.

---

## 2. Top 20 Cited Domains

| Rank | Domain | Count | Language | Tier |
|---|---|---|---|---|
| 1 | lex.uz | 103 | ru | official |
| 2 | cbd.minjust.gov.kg | 63 | ru | official |
| 3 | www.worldbank.org | 26 | en | international_org |
| 4 | president.uz | 21 | ru | official |
| 5 | www.adb.org | 17 | en | international_org |
| 6 | www.undp.org | 13 | en | international_org |
| 7 | 24.kg | 11 | ru | media_primary |
| 8 | mitc.uz | 11 | ru | official |
| 9 | president.kg | 9 | ru | official |
| 10 | projects.worldbank.org | 7 | en | international_org |
| 11 | e-estonia.com | 7 | en | expert_commentary |
| 12 | gov.uz | 5 | ru | official |
| 13 | ssv.uz | 5 | ru | official |
| 14 | kun.uz | 5 | uz/ru | media_primary |
| 15 | digital.gov.kz | 5 | ru | official |
| 16 | www.gov.kz | 5 | ru | official |
| 17 | ec.europa.eu | 4 | en | international_org |
| 18 | www.nbkr.kg | 4 | ru | official |
| 19 | gov.kg | 4 | ru | official |
| 20 | it-park.uz | 4 | uz/ru | official |

Source-tier distribution: official 518 (72.1%), international_org 129 (18.0%), media_primary 44 (6.1%), media_secondary 17 (2.4%), expert_commentary 10 (1.4%). No `social` tier used.

**Notable single-outlet risk:** `e-estonia.com` accounts for 7 of 10 expert_commentary citations. `kaktus.media` (KG media) is heavily cited in the raw data but does not surface in the top-20 because records reference its articles rather than its domain root — the audit_report.md flags this as single-outlet over-reliance for KG-specific claims.

---

## 3. Thirty Sampled Numeric Claims

Source URLs verified against the link_report.json; verification tags from the knowledge graph.

| # | Claim | Source URL (truncated) | Lang | Status |
|---|---|---|---|---|
| 1 | $50M budget — Decree ПП-358 (AI Strategy 2030) | lex.uz/ru/docs/7158606 | ru | VERIFIED |
| 2 | $100M — Decree УП-189 (AI 100 projects) | lex.uz/ru/docs/7790236 | ru | VERIFIED |
| 3 | $100M AI Fund — Decree ПП-320 | lex.uz/ru/docs/7804404 | ru | VERIFIED (date conflict in INI-001: "May 2025" vs actual 30.10.2025 — HIGH) |
| 4 | $7.1M — KG Digital Concept Decree 90/2024 | cbd.minjust.gov.kg/5-10577/... | ru | VERIFIED |
| 5 | $50M — WB Digital Inclusion UZ P179108 | worldbank.org/...press-release/2023-11 | en | L2_VERIFIED (disbursement figure from secondary aggregator) |
| 6 | $40.7M — WB Geospatial NSDI UZ P506803 | worldbank.org/...press-release/2025-05 | en | VERIFIED |
| 7 | $57M — WB Digital CASA KG P160230 | worldbank.org/...press-release/2024-01 | en | VERIFIED (TTL Sandra Sargent: STALE since 2018) |
| 8 | $200M — WB Health UZ P178562 | documents1.worldbank.org/.../P178562 | en | L2_VERIFIED |
| 9 | $20M — WB Identity KG P155198 | projects.worldbank.org/P155198 | en | L2_VERIFIED |
| 10 | $5M — WB Digital GovTech TA | documents.worldbank.org/... | en | INFERRED |
| 11 | $500M — WB Agri Digital UZ | documents.worldbank.org/... | en | INFERRED (HIGH: $500M is total project; digital component is ~2–5% of this figure) |
| 12 | $500M — WB DPO UZ P176353 | projects.worldbank.org/P176353 | en | L2_VERIFIED |
| 13 | $650K — ADB KG e-procurement TA 55109 | adb.org/projects/55109-001 | en | VERIFIED |
| 14 | $125M — ADB UZ Power Grid 52322 | adb.org/projects/52322-004 | en | VERIFIED |
| 15 | $21.6M — EU C4CA digital connectivity | eucybernet.eu/project/c4ca/ | en | VERIFIED |
| 16 | $65M — EU Global Gateway CA digital | eeas.europa.eu/delegations/uzbekistan/... | en | VERIFIED |
| 17 | $5.39M — EU/UNDP Public Service UZ | undp.org/uzbekistan/projects/... | en | VERIFIED |
| 18 | $12.42M — EU/GIZ UZ Governance | giz.de/en/worldwide/129655 | en | VERIFIED |
| 19 | $33M — FCDO Central Asia Governance | devtracker.fcdo.gov.uk/GB-GOV-1-300961 | en | VERIFIED |
| 20 | $200M — EBRD UZ Digital Strategy | ebrd.com/news/2024/... | en | L2_VERIFIED |
| 21 | $4.9M — UNDP UZ Digital PubAdmin | undp.org/uzbekistan/projects/... | en | VERIFIED |
| 22 | $15M commitment — Decree UP-140 Digital Courts | lex.uz/7696571 | ru | L2_VERIFIED (specific $15M needs PAD-level cross-check) |
| 23 | $8M tender UZ-T-2026-002 (AI Courts pilot) | etender.uzex.uz (inferred) | uz/ru | L2_VERIFIED → INFERRED if no live tender notice |
| 24 | 100 AI implementations by end-2026 (УП-189 target) | lex.uz/7790236 | ru | VERIFIED (decree target, not achieved count — HIGH conflation risk) |
| 25 | $2.3M disbursed of $50M WB Digital Inclusion | rightsindevelopment.org (secondary) | en | L2_VERIFIED (single secondary aggregator source) |
| 26 | $1.5B Uzbekistan AI market opportunity (trend) | spot.uz / secondary | ru/en | L2_VERIFIED (secondary outlet, no independent cross-check) |
| 27 | KG Min Digital Development last minister: Sultanov | kaktus.media, reporter.kg | ru | CONTRADICTED (audit S3: actual last minister is Zhamangulov — HIGH) |
| 28 | IT Park CEO: Firdavs Abdullayev | president.uz decree PF-60/2020 | ru | CONTRADICTED (audit S1: current CEO is Azamat Karamatov — HIGH) |
| 29 | KG MoH: Alymkadyr Beishenaliev | (no source URL in record) | — | CONTRADICTED (Sonar Pro: current is Damirbek Osmonov since Feb 2026 — HIGH) |
| 30 | Decree ПП-320 signed "30.10.2025" but INI-001 cites "May 2025" | lex.uz/7804404 | ru | VERIFIED decree; CONTRADICTED in initiative record |

**Summary of 30 samples:** 17 VERIFIED, 8 L2_VERIFIED, 2 INFERRED, 3 CONTRADICTED (HIGH severity). Contradiction rate: 10%.

---

## 4. Dead-Link Breakdown by Category

Total 716 URLs checked; 345 live (48.2%), 371 broken (51.8%).

| Kind | OK | Dead | Dead % | Likely cause |
|---|---|---|---|---|
| decree_source | 68 | 40 | 37% | cbd.minjust.gov.kg 403 anti-bot (39 of 40 dead) |
| institution_website | 40 | 41 | 51% | Network errors + 403; gov portals blocking scrapers |
| institution_source | 46 | 47 | 51% | Mixed 403/network; mitc.uz and similar blocking |
| person_source | 39 | 32 | 45% | Network errors; ministry bio pages |
| linkedin | 0 | 45 | 100% | 429 (rate-limit) + HTTP 999 (anti-bot) — all are anti-bot, not genuine 404s |
| donor_source | 37 | 18 | 33% | 403 (14) + network (2); worldbank and adb mostly live |
| tender_source | 20 | 12 | 38% | 403 (6) + exception (5) |
| tender_url | 6 | 4 | 40% | 403 (2) + 404 (1) + network (1) |
| trend_source | 15 | 8 | 35% | 403 (7); news aggregators |
| case_source | 74 | 124 | 63% | True 404s: 55 of 124 (e-estonia, bilimland, diia, etc.) |

**Anti-bot vs genuine 404 split:**
- HTTP 403: 115 URLs — overwhelmingly anti-bot (cbd.minjust.gov.kg, mitc.uz, LinkedIn). Not true dead links.
- HTTP 404: 59 URLs — genuine dead pages. 55 of 59 are `case_source` (e-estonia solution pages, bilimland, Ukrainian govt sites).
- HTTP 429/999: 45 LinkedIn — anti-bot rate limiting, not dead.
- Network error / None: 149 — mostly institution websites behind firewalls.

**Wayback fallback coverage:**
- Decree 403s: 12 of 39 have a Wayback URL in `link_report.json`. 27 decree dead links have no Wayback substitution recorded.
- All other kinds: 0 Wayback URLs recorded (case_source, institution, person, donor, tender, trend all missing).
- **Critical gap:** 359 of 371 dead links have no `wayback_url` populated.

**Recommended Wayback substitutions (priority order):**
1. 27 decree dead links on cbd.minjust.gov.kg without Wayback — run `wayback_machine_downloader` for each URL pattern `/act/view/ru-ru/NNNNNN`.
2. 55 case_source true 404s — e-estonia.com page changes are the main driver; archive.org snapshots exist for most e-estonia URLs (last crawled 2024-09).
3. 14 donor_source 403s (mostly worldbank.org project pages) — worldbank PDF mirrors often available via `documents.worldbank.org`.

---

## 5. "Provenance Page" Gap Analysis

Current `/provenance/` page (8,721 chars) is minimal. It correctly states ~402 references exist and links to the GitHub repo and `audit_report.md`. Gaps:

| Gap | Impact | Proposed addition |
|---|---|---|
| No dead-link rate disclosed | Readers cannot assess source reliability | Add KPI: "51.8% of URLs return anti-bot 403 or are dead; Wayback substitutes available for 12 of 371." |
| No Wayback usage shown | Users cannot find archived versions | Add table: "Links where Wayback archive is used as primary fallback" with count by category. |
| No verification-tag legend | VERIFIED / L2_VERIFIED / INFERRED / UNVERIFIED not explained on the page | Add a 4-row legend table above the main content. |
| No source-language breakdown | Cannot verify the ≥30% regional-language requirement | Add KPI grid: ru 53.1%, en 44.2%, uz-latn 1.3%. |
| No link-report stats table | 716 checked / 345 ok / 371 broken is not surfaced | Add one-sentence summary with link to raw `state/audit/link_report.json`. |
| No "last verified" dates on public pages | Decrees, people, donor pages show no `fetched_at` or `verified_at` dates | Render `sources[0].fetched_at` on each record's public-facing card. |
| No foreign-key chain rendering | People page has institution links but decree→institution→person→donor chain not navigable as a path | Add "chain" breadcrumb on initiative pages: Decree → Institution → Contact → Donor program. |
| OpenRouter cards not linked from page | Cards exist under `state/external/` but no table enumerates them | Add table: model / call date / record ID / verdict / cost. |

---

## 6. Foreign-Key Surfacing Assessment

- **Decree → Institution:** Decrees list `responsible_agency_ids`; institution pages exist and are linked from nav. Decrees UZ page renders 55 clickable lex.uz source links. **OK.**
- **Institution → Person:** People page references institution IDs; rendered as text, not hyperlinks. **Partial.**
- **Person → Donor:** Donor page shows TTL names and counterpart names. Not linked to person record. **Partial.**
- **Initiative chain:** Initiative page does not render the full `decree → institution → person → donor` provenance chain inline. Users must cross-reference manually across 4 pages. **Gap.**
- **Verification tags on public pages:** `decrees/uz/index.html` renders no VERIFIED badge. `people/index.html` renders no VERIFIED badge. `donors/index.html` renders no VERIFIED badge. Only `initiatives/index.html` contains "VERIFIED" text. **Inconsistent.**

---

## 7. Ten Prioritized Fixes

| # | Fix | Severity | Effort |
|---|---|---|---|
| F-01 | Correct IT Park CEO from Firdavs Abdullayev to Azamat Karamatov in all records; update `target_buyer_person_id` in linked initiatives | HIGH | 1h |
| F-02 | Add Azamat Zhamangulov as new person record (last KG Min Digital); remove or demote Talant Sultanov from "last minister" role | HIGH | 2h |
| F-03 | Remove UZ-LAW-2026-1125 citation from INI-002 and INI-003 until a source URL on lex.uz is confirmed; downgrade those regulatory_hurdles fields to UNVERIFIED | HIGH | 30min |
| F-04 | Fix INI-001 date reference: "PP-320 (May 2025)" → "ПП-320 (30.10.2025)"; propagate to all initiatives referencing this decree | HIGH | 30min |
| F-05 | Replace WB-UZ-AGRI-DIGITAL `total_budget_usd: 500000000` with `digital_component_budget_usd_estimated: ~10000000`; re-tag verification to CONTRADICTED for the headline figure | HIGH | 1h |
| F-06 | Populate `wayback_url` for 27 remaining decree dead links on cbd.minjust.gov.kg; add Wayback fallback for top 55 case_source 404s | MEDIUM | 3h (scripted) |
| F-07 | Add to `/provenance/`: dead-link stats, Wayback usage count, source-language KPI grid, verification-tag legend, link-report raw link | MEDIUM | 2h |
| F-08 | Render `sources[0].fetched_at` as "Last verified: YYYY-MM-DD" on decree, people, and donor record cards in the site renderer | MEDIUM | 2h |
| F-09 | Render verification badge (VERIFIED / L2_VERIFIED / INFERRED) consistently on all public record pages, not only initiatives | MEDIUM | 1h |
| F-10 | Add Damirbek Osmonov (KG MoH since Feb 2026) and Azamat Burzhuev (KG UDP Digital Dept head) as new person records; remove Beishenaliev and Asanbekov from current-role positions | HIGH | 2h |

---

*All data sourced from `state/audit/link_report.json` (checked 2026-05-03), `state/knowledge_graph.json`, `state/audit/audit_report.md`, and local HTML render in `outputs/site/`.*
