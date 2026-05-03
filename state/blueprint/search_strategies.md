# Search Strategies for Downstream Agents
**Wave 0 output. Search ergonomics for Waves 1-6 of the Central Asia B2G Research Harness. Author: blueprint-architect. 2026-05-03.**

This document is a working manual. Every downstream agent must consult it before issuing search queries. The harness has tight verification rules (CLAUDE.md: ≥50% Russian-language sources; no fabrication of decree numbers or LinkedIn URLs). This document tells you how to satisfy those rules efficiently.

---

## 1 — Russian-language search ergonomics

### Choice of engine

| Engine | Best for | Notes |
|---|---|---|
| Google (with `lang=ru` and `cr=countryUZ` / `countryKG`) | Most reliable for breadth | Default |
| Yandex (yandex.ru) | Russian-language SEO content; sometimes uniquely indexes lex.uz, Tazabek, kaktus.media | Try when Google misses |
| DuckDuckGo + Bing | Useful when Google is rate-limited | Fallback |
| Tunduk / direct site search | Inside lex.uz, cbd.minjust.gov.kg, gov.uz built-in search is more reliable than Google site: queries for very recent material | Use after Google fails |

### High-yield operators

```
site:lex.uz "ПП-358"                        # exact decree number on official portal
site:lex.uz искусственный интеллект 2025    # AI-related material on lex.uz (in Russian)
site:cbd.minjust.gov.kg "Цифровой кодекс"   # KG digital code official
site:president.uz цифровая трансформация 2025
site:gazeta.uz инурьмации
"Шерзод Шерматов" "цифровых технологий" 2025
"УП-189" 22.10.2025 OR "от 22 октября 2025"
inurl:docs intext:"цифровой сом"
filetype:pdf инвестиции искусственный интеллект Узбекистан
"Стратегия Цифровой Узбекистан 2030" "целевые показатели"
"Концепция цифровой трансформации" 2024-2028 "Кыргызская Республика"
"Министерство цифровых технологий" заместитель министра
```

Use the **exact decree pattern** (`УП-` for Uzbek presidential, `ПП-` for Uzbek presidential resolution, `Указ Президента №` for KG). Searching for the verbose title rarely lands on the official portal.

### Source-tier hierarchy (when ranking sources)

1. **Tier 0 — Official primary**: lex.uz, cbd.minjust.gov.kg, president.uz, president.kg, gov.uz, gov.kg, ministry sites (mitc.uz, asr.gov.uz, mineconomy.gov.uz, nbkr.kg, fsa.gov.kg, etc.)
2. **Tier 1 — Aggregators of official**: norma.uz, online.toktom.kg, base.spinform.ru, NRM.uz
3. **Tier 2 — Quality national media in Russian**: gazeta.uz, kursiv.media (UZ edition), spot.uz, kaktus.media, 24.kg, akipress.org, tazabek.kg, economist.kg, time.kg, gazeta.kg
4. **Tier 3 — Regional/expert in Russian**: AzattyqAsia, Sputnik UZ/KG, podrobno.uz, daryo.uz, kun.uz, repost.uz, fergana.agency, eurasiatoday.ru
5. **Tier 4 — Industry/trade in Russian**: tadviser.ru, fintech-retail.com, banks.kg, plusworld.ru, cnews.ru
6. **Tier 5 — International English secondary**: timesca.com, eurasianet.org, worldbank.org press releases, adb.org news, biometricupdate.com
7. **Tier 6 — Wikipedia, blogs**: lowest priority; never primary citation

When citing, every claim should have at least one Tier 0–3 source. If only Tier 4–6 sources exist, mark `[INFERRED]` not `[VERIFIED]`.

---

## 2 — Uzbek-language search

UZ has a bilingual problem: older population reads Cyrillic, government documents are increasingly Latin, and public-facing sites mix both. A search must cover both scripts.

### Cyrillic vs Latin transliteration

Common terms double-form:
| Latin | Cyrillic | English |
|---|---|---|
| Raqamli | Рақамли | Digital |
| Sun'iy intellekt | Сунъий интеллект | Artificial intelligence |
| Vazirlik | Вазирлик | Ministry |
| Qaror | Қарор | Resolution |
| Farmon | Фармон | Decree |
| Davlat | Давлат | State |
| Idora | Идора | Agency |

When searching gov.uz / digital.uz / mitc.uz Uzbek pages, try the Latin first (current default per government policy), fall back to Cyrillic. Older lex.uz pages (pre-2023) are predominantly Cyrillic; newer ones are Latin.

Useful operators:
```
site:lex.uz sunʼiy intellekt
site:digital.uz raqamli
site:gov.uz/digital vazirlik rahbariyati
site:gazeta.uz "цифровизация" OR "raqamlashtirish"
```

---

## 3 — Kyrgyz-language search

Kyrgyz government uses both Russian and Kyrgyz. Kyrgyz has a Cyrillic-only script with three additional letters (ң, ү, ө). Many official portals are bilingual; the Russian version is usually more comprehensive than the Kyrgyz version. Some local-government sites are Kyrgyz-only.

Useful Kyrgyz terms:
| Kyrgyz | Russian/English |
|---|---|
| Санариптик | Цифровой / Digital |
| Сүний интеллект | Искусственный интеллект / AI |
| Министрлик | Министерство |
| Жарлык | Указ |
| Токтом | Постановление |
| Президент Аппарат | Аппарат Президента |
| Айыл аймагы | Сельское муниципалитет |
| Ишкана | Предприятие / Enterprise |

For grass-roots / municipal-level material:
```
site:gov.kg санариптик
site:cbd.minjust.gov.kg токтом санариптик
site:mkk.gov.kg айыл аймагы
"санариптик трансформация" Кыргызстан 2026
```

---

## 4 — LinkedIn search for CA officials

LinkedIn presence is **sparse** for both UZ and KG senior officials, especially Tier 1-2. The deeper into the agency / SOE / working-group hierarchy you go, the more likely the person is on LinkedIn (often because they previously worked at a foreign company or studied abroad).

### Strategies that work

1. **Pivot via diaspora**. Search the diaspora list (Moscow, Almaty, Istanbul, Seoul, London, San Francisco, Dubai, Berlin) for `IT Park Uzbekistan`, `UDP Kyrgyzstan`, `World Bank Tashkent`, `ADB Bishkek`. Diaspora often connects you to in-country officials they advise informally.

2. **Pivot via current employer page**. Visit the LinkedIn company page (e.g., `IT Park Uzbekistan`, `Министерство цифровых технологий Узбекистан`, `World Bank Group / Tashkent`). The "People" tab lists current employees often more reliably than direct name search.

3. **Use Boolean with role and country**. `"Deputy Minister" AND ("Uzbekistan" OR "Republic of Uzbekistan") AND digital`. Then triangulate with Russian-language press releases announcing the appointment.

4. **Korean Hangul fallback for KOICA partners**. Many UZ technocrats studied in Korea; Korean-language LinkedIn entries (in 한국어) sometimes surface their alumni profiles.

5. **Cross-check with Crunchbase / Wikipedia / org. site**. Confirm name spelling first, then match LinkedIn.

### Strategies that DON'T work (and lead to fabrication)

- **Pattern-completing `linkedin.com/in/{firstname}-{lastname}`**. The harness MUST NOT do this. Verify by visiting.
- **Trusting LinkedIn search "Connect to..." stub matches**. These often confuse two people with similar names.
- **Trusting Sales Navigator export results without manual verification**. Often stale.

If after 4 search strategies a person has no findable LinkedIn, set `linkedin_status: "not_found"` and provide alternative contact (Twitter/X, Telegram, Facebook, official email pattern guess via `@gmail.com → @{ministry}.uz` heuristic).

---

## 5 — Decree number lookup

### lex.uz (Uzbekistan)

URL patterns:
```
https://lex.uz/ru/docs/{numeric_id}      # Russian
https://lex.uz/uz/docs/{numeric_id}      # Uzbek
https://lex.uz/ru/docs/{id}?ONDATE=DD.MM.YYYY  # historical version on a date
```

The `numeric_id` for verified examples:
- `7158606` = ПП-358 of 14.10.2024 (AI Strategy 2030)
- `7790236` = УП-189 of 22.10.2025 (AI additional measures)
- `7804404` = ПП-320 of 30.10.2025 (AI funding $100M)
- `7696571` = УП-140 of 21.08.2025 (AI in courts)
- `5031048` = УП-6079 of 05.10.2020 (Digital Uzbekistan-2030)
- `5015117` = УП-6065 of 22.09.2020 (ID-card)

Search lex.uz by year + decree-type prefix:
```
https://lex.uz/ru/docs?q=ПП-{number}
https://lex.uz/ru/docs?q=УП-{number}
```

Also useful: `https://nrm.uz/contentf?doc={id}_...` (NRM is a private-sector wrapper of lex.uz; sometimes more readable).

### cbd.minjust.gov.kg (Kyrgyzstan)

URL pattern:
```
https://cbd.minjust.gov.kg/{rubric}/edition/{eid}/ru
https://cbd.minjust.gov.kg/act/view/ru-ru/{id}
```

Verified examples:
- `30-164/edition/6414/ru` = Концепция цифровой трансформации КР 2024-2028 (Указ №90 of 5.04.2024)
- `3-48/edition/35412/ru` = Цифровой Кодекс КР №178 of 31.07.2025
- `159155` = Положение Кабмина №245 of 30.04.2022 (ГП "Тундук")
- `158713/edition/1288196/ru` = Положение о Министерстве цифрового развития КР

For browsing by year/type:
```
https://cbd.minjust.gov.kg/poisk?...
```

`tunduk.gov.kg` has its own document repository for inter-agency interaction documents.

### Verification rule

Every decree record in the knowledge graph MUST include the lex.uz or cbd.minjust.gov.kg URL in `sources[]`. If you cannot find the URL, either the decree number is wrong or the document is in a non-standard location. **Tag as `[UNVERIFIED]` rather than guessing.**

---

## 6 — Donor portal search ergonomics

### World Bank

| Portal | Use for | URL pattern |
|---|---|---|
| Documents | Project documents, ICR, PAD, ISR | `documents.worldbank.org` (search by country + sector) |
| Projects | Project status, dates, lending instrument | `projects.worldbank.org/en/projects-operations/projects-list?countrycode_exact=UZ&sectorcode_exact=digital` |
| Procurement | STEP, contract awards | `projects.worldbank.org/en/projects-operations/procurement` |
| Press | Recent announcements | `worldbank.org/en/news/press-release/{year}/{date}/...` |

Search examples:
```
site:projects.worldbank.org Uzbekistan digital
site:documents.worldbank.org "Cadastre" Uzbekistan 2025 PAD
site:worldbank.org Uzbekistan GovTech
"P number" Uzbekistan Digital  # P-numbers are WB project IDs, e.g. P176689
```

### ADB

| Portal | URL |
|---|---|
| Project pages by country | `adb.org/projects/country/uzbekistan` and `adb.org/projects/country/kyrgyz-republic` |
| Project search | `adb.org/projects` with filters |
| Procurement | `adb.org/projects/tenders` |

Project IDs are like `55109-001` (the e-Procurement KG project we identified). Search:
```
site:adb.org Uzbekistan digital project 2024 2025
"55109-001" Kyrgyzstan
```

### EU / Capacity4Dev / Connectivity for Central Asia

| Portal | URL |
|---|---|
| Team Europe Tracker | `capacity4dev.europa.eu/resources/team-europe-tracker/` |
| EU Delegation UZ | `eeas.europa.eu/delegations/uzbekistan` |
| EU Delegation KG | `eeas.europa.eu/delegations/kyrgyzstan` |
| C4CA initiative | `d4dhub.eu/initiatives/c4ca` |
| Tenders | `funding-tenders.ec.europa.eu/opportunities/portal` |

```
site:capacity4dev.europa.eu Central Asia digital
site:international-partnerships.ec.europa.eu Uzbekistan
"Connectivity for Central Asia" tender 2025 2026
```

### KOICA, JICA

Both publish project pages and country-strategy PDFs in English; KOICA also Korean. Use:
```
site:koica.go.kr Uzbekistan
site:jica.go.jp Kyrgyz
"KOICA" "Uzbekistan" "IT Education" 14
```

### UNDP

```
site:undp.org/uzbekistan
site:undp.org/kyrgyzstan
```

UNDP project detail pages often have implementing partner — that's the government counterpart (a key data point).

---

## 7 — Procurement portals

### Uzbekistan

- **xt.xarid.uz / xarid.uz** — main state procurement portal
- **etender.gov.uz** — tender announcement portal
- **dxt.uz** — government procurement
- **rasm.uz** — supply portal

```
site:xt.xarid.uz искусственный интеллект
site:dxt.uz цифровизация
"Министерство цифровых технологий" тендер 2025
```

### Kyrgyzstan

- **zakupki.gov.kg** — main e-procurement portal (the one ADB is digitizing further under project 55109-001)
- **eprocurement.gov.kg** — current iteration
- **op.zakupki.gov.kg** — open data on procurement

```
site:zakupki.gov.kg цифровизация
site:eprocurement.gov.kg ИИ AI
```

### Donor procurement

- **WB STEP** (Systematic Tracking of Exchanges in Procurement) — `https://projects.worldbank.org/en/projects-operations/procurement`
- **ADB CSRN** (Consultant Services Recruitment Notice) — visible on each project page
- **EU TED** (Tenders Electronic Daily) — `ted.europa.eu`
- **UN Global Marketplace** — `ungm.org`

---

## 8 — Diaspora search ergonomics

For diaspora identification, the fastest unlocks are:

1. **University alumni networks**. Search for Uzbek and Kyrgyz alumni at: KAIST (Korea), Seoul National, MIT, Stanford, Oxford, Cambridge, MGIMO, MGU, ETH Zurich, IE Business School, INSEAD. Diaspora-bridge people often went through these.

2. **Conference/keynote pivot**. Search for who gave a keynote at:
   - Innopolis Tashkent
   - PLAS Forum Bishkek
   - Tashkent Innoweek
   - Issyk-Kul Forum
   - GovTech Forum events
   - World Bank ICT4Gov events
   - SCO digital summits

3. **Co-authorship search**. Use Google Scholar with country names + tech terms, then check author affiliations:
   ```
   "Uzbekistan" digital identity author:* affiliation:abroad
   ```

4. **Major-tech-employer alumni search**. LinkedIn → `Past company: Yandex` AND `Past company: Mininfocom`, etc.

5. **Presidential council membership**. Both countries publish Presidential Advisory Council membership lists (in Russian); search:
   ```
   "Совет при Президенте" "цифровая" состав 2024 2025
   ```

---

## 9 — Verification workflow (every claim, every time)

1. **Find primary source**. Tier 0 official, ideally.
2. **Find one Russian-language corroboration**. Tier 1-3 RU-language source.
3. **Find one English / native-language corroboration** (optional but valuable).
4. **Tag**:
   - `[VERIFIED]` if Tier 0 + at least one corroboration in another tier
   - `[L2_VERIFIED]` if only one Tier 1-3 source available, no Tier 0
   - `[INFERRED]` if reasoned from indirect evidence and the agent is calling out the inference
   - `[UNVERIFIED]` if no source found — still record the hypothesis but flag clearly
5. **Record `last_verified_date`**. ISO date, when the agent visited the source.
6. **Record `Source` object** in `sources[]`: url, title, language, fetched_at, publisher, source_tier.

A single "ru" Wikipedia citation is **NOT verification**. Never cite Wikipedia as primary.

---

## 10 — Anti-patterns to avoid

- **English-only search for country claims**. Banned by CLAUDE.md.
- **Pattern-completing decree numbers**. Banned by CLAUDE.md. If you can't find `УП-189`, do not write `УП-189`. Find it or mark UNVERIFIED.
- **Pattern-completing LinkedIn URLs**. Banned by CLAUDE.md. Visit the URL or mark `not_found`.
- **Speculating about political loyalties or personal networks**. Banned by CLAUDE.md.
- **Citing pre-2024 institutional structures as current**. R-001 risk; always verify post-restructuring name.
- **Conflating UZ and KG**. CLAUDE.md explicit MUST. Each country gets separate treatment.
- **Treating donor press releases as procurement schedule**. R-003 risk.
- **Ignoring native-language sources because they're harder to read**. R-004 risk.

---

## 11 — Recommended search budget per agent

| Agent | Searches per record | Notes |
|---|---|---|
| legal-cartographer | 3-5 per decree | Each must include lex.uz/cbd.minjust.gov.kg verification |
| institution-mapper | 5-8 per institution | Russian + Uzbek/Kyrgyz + leadership names |
| donor-pipeline | 4-6 per program | Donor portal + recent press + counterpart name |
| people-intelligence | 8-12 per person | LinkedIn pivot + role announcement + speeches + diaspora cross-check |
| case-tournament | 3-5 per global case | At least one technical / architectural source |
| trend-triangulator | 2-4 per trend | Cross-check between official decree and media coverage |
| procurement-harvester | 2-3 per tender | Tender portal + announcement + RFP doc if available |

---

## 12 — Final note on rate-limiting and resilience

- Web searches via LLM tools have variable rate limits. Batch your searches across logical groupings rather than one-at-a-time.
- WebFetch is more expensive per call than WebSearch. Use WebFetch sparingly: only when you need to extract specific structured data (e.g., a decree's text, a person's exact role title) from a known URL. Use WebSearch for discovery.
- If a primary source (lex.uz, cbd.minjust.gov.kg) is unreachable on a given day, fall back to NRM.uz / online.toktom.kg mirrors. Mark the source as `secondary_official` in the source object.
- Cache your verifications. Re-verifying the same decree URL across multiple agents is wasteful — reflexion-auditor will re-verify a sample, not the universe.

---

**End of search_strategies.md**

Total approximate word count: ~2400 words. Document is intended as a living reference. When a search pattern fails repeatedly, the failure becomes a new note in this document (per CLAUDE.md stabilization cycle).
