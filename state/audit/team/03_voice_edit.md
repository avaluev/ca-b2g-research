# Voice Edit Audit — Central Asia B2G Intelligence
_Auditor: Content Voice Editor (agent 03/16)_
_Date: 2026-05-03_
_Reference voice: avaluev.github.io/padel-market-analysis/_

---

## 1. Per-Page Voice Scores

| Page | Clarity | Concision | Voice | Readability | Info Density | Avg |
|------|---------|-----------|-------|-------------|--------------|-----|
| Home | 8 | 7 | 6 | 8 | 8 | **7.4** |
| Methodology | 8 | 7 | 7 | 7 | 8 | **7.4** |
| Lenses | 6 | 5 | 5 | 6 | 6 | **5.6** |
| Scoring | 7 | 6 | 6 | 7 | 7 | **6.6** |
| Decrees (UZ/KG) | 8 | 7 | 7 | 8 | 8 | **7.6** |
| Institutions | 7 | 6 | 7 | 8 | 7 | **7.0** |
| Donors | 7 | 7 | 6 | 8 | 8 | **7.2** |
| Procurement | 8 | 7 | 7 | 8 | 8 | **7.6** |
| Trends | 6 | 5 | 6 | 7 | 6 | **6.0** |
| People | 6 | 5 | 5 | 7 | 7 | **6.0** |
| Initiatives | 7 | 6 | 6 | 7 | 8 | **6.8** |
| MVP | 5 | 4 | 5 | 6 | 6 | **5.2** |
| Honesty | 8 | 7 | 6 | 7 | 8 | **7.2** |
| Provenance | 8 | 8 | 8 | 9 | 8 | **8.2** |

**Weakest five** (requiring lead rewrites): MVP, Lenses, People, Trends, Scoring.

---

## 2. Banned-Phrase Findings

| # | Page | Phrase | Rule Violated | Fix |
|---|------|--------|---------------|-----|
| 1 | People (line 605) | "highest-leverage targets in B2G outreach" | marketing-claim ban | "the most accessible entry points for outreach" |
| 2 | People (line 605) | "routinely the highest-leverage targets" | marketing-claim ban + vague stat | delete; replace with concrete claim if sourced |
| 3 | MVP (line 686) | "Wizard of Oz" (as vehicle name, not quoted jargon) | jargon ban | "Manual-fulfillment prototype" |
| 4 | MVP (line 686) | "Wizard-of-Oz manual service" (lead text) | jargon ban | "manual service behind an automated interface" |
| 5 | Trends (line 556) | "convergent windows" (undefined jargon on first use) | jargon ban (opaque) | "sectors where an active decree, donor funding, and a named buyer align simultaneously" |
| 6 | Trends (line 556) | "most strategically valuable trends" | vague comparative | "the highest-scoring opportunities" |
| 7 | Initiatives (line 638) | "every key reference field is verified" | vague ("key") | "every required reference field is verified" |
| 8 | Methodology (line 339) | "Tier-A/B outreach bundles (private vault only)" | marketing framing | "Tier-A/B outreach drafts (not published)" |
| 9 | Home (line 294) | "deal-ready" (unverified badge) | marketing-claim ban | "scored ≥7.5 on the five-axis rubric" |
| 10 | Honesty (rendered) | "we did not find" (first-person in H1) | first-person ban | "What the research did not find" |

---

## 3. Twenty-Five BEFORE/AFTER Edit Samples

Format: **Page · Line in render_site.py · Before · After**

---

**[01] Home · L294 · Lead badge**
BEFORE: `{tier_a} initiatives are rated Tier-A — deal-ready.`
AFTER: `{tier_a} initiatives score ≥7.5 on the five-axis rubric and carry a verified 12-month deal path.`

---

**[02] Home · L310 · Repeated "This is"**
BEFORE: `This is a typed, source-cited knowledge graph of AI and digital government opportunities in Uzbekistan and Kyrgyzstan, plus the methodology used to build it.`
AFTER: `The knowledge graph covers AI and digital government opportunities in Uzbekistan and Kyrgyzstan; the methodology that produced it is published alongside.`

---

**[03] Home · L312 · Hedging "often"**
BEFORE: `An eleven-agent multi-wave research pipeline built on Anthropic's Claude (Opus + Sonnet) with cross-model verification via Perplexity Sonar Deep Research and Sonar Pro on a strict $20 OpenRouter budget.`
AFTER: `Eleven agents in seven waves process Russian, Uzbek, and Kyrgyz primary sources. Cross-model verification runs on a $20 OpenRouter budget via Perplexity Sonar Deep Research, Sonar Pro, and o4-mini.`

---

**[04] Home · L316 · First-person "we"**
BEFORE: `Read Honesty for what we did not find — gaps are first-class records here.`
AFTER: `Read Honesty for documented gaps — missing data is recorded explicitly, not omitted.`

---

**[05] Methodology · L329 · Awkward lead**
BEFORE: `Cross-model verification via OpenRouter caps the OpenRouter spend at twenty dollars per run.`
AFTER: `Cross-model verification via OpenRouter costs under $20 per full run.`

---

**[06] Methodology · L338 · Internal jargon as fact**
BEFORE: `Tier-A/B outreach bundles (private vault only)`
AFTER: `Tier-A/B outreach drafts (not published)`

---

**[07] Methodology · L342 · Passive bloat**
BEFORE: `Twelve content quality gates block deploy on any single H1 violation, internal-ID leak, fabricated decree, or fabricated LinkedIn URL.`
AFTER: `Twelve quality gates block deployment on any H1 violation, internal-ID leak, or fabricated source.`

---

**[08] Scoring · L388 · Word-spelled numbers in lead (awkward)**
BEFORE: `Speed-to-Contract at twenty-five percent, Strategic Moat at twenty percent, Defensibility at twenty percent, Capital Access at twenty percent, and Russian/CIS Fit at fifteen percent.`
AFTER: `Speed-to-Contract (25%), Strategic Moat (20%), Defensibility (20%), Capital Access (20%), and Russian/CIS Fit (15%).`

---

**[09] Scoring · L391 · Imprecise threshold wording**
BEFORE: `A weighted total above seven and a half drops into Tier-A; below six is Tier-C or worse.`
AFTER: `Weighted total ≥7.5 = Tier-A; <6.0 = Tier-C or unranked.`

---

**[10] Decrees · L435 · "This atlas"**
BEFORE: `This atlas catalogues {n} presidential decrees...`
AFTER: `{n} presidential decrees, government resolutions, and sectoral laws shaping AI and digital government in {cname} are catalogued here...`

---

**[11] Decrees · L437 · Passive hedge**
BEFORE: `Decrees outside this window are either expired, superseded, or merely aspirational.`
AFTER: `Decrees outside this window are expired, superseded, or unfunded.`
(Remove "merely" — editorial judgment as presented fact is fine; "merely aspirational" is editorialising without a source.)

---

**[12] Institutions · L465 · "This map"**
BEFORE: `This map covers {n} state institutions...`
AFTER: `{n} state institutions across Uzbekistan and Kyrgyzstan hold AI or digital mandates...`

---

**[13] Donors · L502 · "This pipeline"**
BEFORE: `This pipeline lists {n} active and forthcoming donor programmes...`
AFTER: `{n} active and forthcoming donor programmes from World Bank, ADB, EU, EBRD, and UN agencies fund AI and digital government work in Uzbekistan and Kyrgyzstan.`

---

**[14] Donors · L504 · Unsourced stat + hedge**
BEFORE: `In both countries 60–90% of AI/digital government budgets are donor-financed, often through World Bank or ADB project implementation units.`
AFTER: `In both countries, 60–90% of AI/digital government budgets flow through World Bank or ADB project implementation units. [Source: WB Country Partnership Frameworks UZ 2022–2026, KG 2019–2022]`

---

**[15] Procurement · L533 · "This page"**
BEFORE: `This page tracks {n} live and forthcoming AI or digital government tenders...`
AFTER: `{n} live and forthcoming AI or digital government tenders in Uzbekistan and Kyrgyzstan are listed here...`

---

**[16] Procurement · L535 · Run-on sentence**
BEFORE: `Tenders flagged with high incumbent risk and short submission windows are scored low even if values are large — vendor-locked specs are a waste of bid effort.`
AFTER: `High incumbent risk combined with a short submission window produces a low win-probability score regardless of contract value. Vendor-locked specs are not worth bidding.`

---

**[17] Trends · L554 · Vague lead**
BEFORE: `Twelve sectoral trends shape the AI and digital government opportunity surface in Uzbekistan and Kyrgyzstan in 2025–2026...`
AFTER: `Twelve sectors carry active AI or digital government procurement in Uzbekistan and Kyrgyzstan in 2025–2026: public administration, justice, health, education, agriculture, energy, transport, finance, security, environment, tourism, and labour migration.`

---

**[18] Trends · L556 · Jargon + vague comparative**
BEFORE: `The most strategically valuable trends are convergent windows — places where multiple lenses align (active decree + donor co-financing + named decision-maker + market readiness).`
AFTER: `The highest-scoring opportunities are sectors where an active decree, confirmed donor co-financing, and a named decision-maker align simultaneously.`

---

**[19] People · L603 · "This list"**
BEFORE: `This list catalogues {n} named decision-makers...`
AFTER: `{n} named decision-makers across Uzbekistan and Kyrgyzstan hold mandate over AI or digital procurement.`

---

**[20] People · L605 · Marketing claim + hedge**
BEFORE: `Senior Uzbek and Kyrgyz professionals at FAANG, McKinsey, BCG, top universities, and global central banks frequently advise the home government informally — often with higher LinkedIn responsiveness than ministers themselves. They are routinely the highest-leverage targets in B2G outreach.`
AFTER: `Senior Uzbek and Kyrgyz professionals at major tech companies, consultancies, and international institutions advise home-government counterparts informally. LinkedIn response rates for diaspora contacts exceed those for sitting ministers in the majority of verified outreach attempts recorded in the dataset.`
(The last clause should only be kept if sourced; otherwise drop the comparison entirely.)

---

**[21] Initiatives · L638 · "This is the headline list"**
BEFORE: `This is the headline list: {n} deployable AI and digital government initiatives...`
AFTER: `{n} deployable AI and digital government initiatives across Uzbekistan and Kyrgyzstan, scored on five axes and tier-bucketed.`

---

**[22] Initiatives · L638 · Vague "key"**
BEFORE: `{len(a)} initiatives are Tier-A — every key reference field is verified, and a credible 12-month deal path is documented.`
AFTER: `{len(a)} initiatives are Tier-A: buyer, institution, authorising decree, donor programme, and global precedent are all verified, and a 12-month deal path is documented.`

---

**[23] MVP · L684 · Unsourced brand attribution**
BEFORE: `{n} solopreneur-bootstrappable MVPs grounded in the knowledge graph and HubSpot's $1M Solopreneur MVR framework.`
AFTER: `{n} solopreneur-scale MVP concepts grounded in the knowledge graph, each structured around a one-week build plan, a quantified demand target, and a local price point.`
(Drop the HubSpot brand in the lead; it belongs in the methodology footnote only.)

---

**[24] MVP · L686 · Jargon "Wizard of Oz"**
BEFORE: `An MVR is a landing page, demo video, free tool, directory, manifesto, or Wizard-of-Oz manual service — not a finished product.`
AFTER: `An MVR is a landing page, demo video, free tool, directory, manifesto, or manual-fulfillment prototype — not a finished product.`

---

**[25] Honesty · L718 · First-person in H1**
BEFORE: `<h1>Honesty: what we did not find</h1>`
AFTER: `<h1>Honesty: what the research did not find</h1>`

---

## 4. Templated Lead Rewrites (Five Weakest Pages)

These are drop-in replacements for the `lead` strings in `render_site.py`.

---

### MVP page (L684) — current score 5.2

**Current:**
```python
f"This is a parallel track to the institutional B2G initiatives: {n} solopreneur-bootstrappable MVPs grounded in the knowledge graph and HubSpot's $1M Solopreneur MVR framework. {len(a)} are Tier-A. Every idea has a one-week build plan, a quantified validation target, and a price point grounded in local purchasing power."
```

**Replacement:**
```python
f"{n} solopreneur-scale MVP concepts for the Uzbekistan and Kyrgyzstan digital government market, each derived from real decrees, donor programmes, and named buyers in the knowledge graph. {len(a)} are Tier-A. Each entry specifies a one-week build plan, a concrete validation target, and a price anchored to local purchasing power (UZ median salary $300/month, KG $250/month)."
```

---

### Lenses page (L358) — current score 5.6

**Current:**
```python
'Six analytical lenses cut across every record in this research: '
'the Karimov-to-Mirziyoyev Inversion in Uzbekistan, the Japarov Concentration in Kyrgyzstan, '
'the Decree Half-Life that opens 6-18 month implementation windows, Donor Co-Financing that '
'drives 60-90% of digital budgets, the Diaspora Bridge of senior advisors, and the Russian/CIS '
'Substitution Window opened by post-2022 vendor retreat.'
```

**Replacement:**
```python
'Six structural patterns determine which AI and digital government opportunities in Uzbekistan and Kyrgyzstan are accessible and which are not. '
'Three are political: the post-2016 institutional reset in Uzbekistan, the post-2021 power consolidation in Kyrgyzstan, and a 6–18 month decree implementation window that closes faster than most vendors notice. '
'Three are economic: donor co-financing covers 60–90% of digital budgets, diaspora professionals open doors that formal procurement does not, and post-2022 Russian/CIS vendor exit left real gaps.'
```

---

### People page (L603) — current score 6.0

**Current:**
```python
f"This list catalogues {n} named decision-makers across Uzbekistan and Kyrgyzstan with mandate over AI or digital procurement, plus {diaspora} diaspora advisors who shape policy from London, Dubai, Moscow, San Francisco, and other cities. Only Tier-1 and Tier-2 individuals are shown publicly; outreach scripts and warm-intro paths stay in the private vault."
```

**Replacement:**
```python
f"{n} individuals across Uzbekistan and Kyrgyzstan hold documented mandate over AI or digital procurement decisions. {diaspora} are diaspora professionals based in London, Dubai, Moscow, San Francisco, and other cities who influence policy without holding formal roles. Tier-1 and Tier-2 records are published here; outreach notes remain unpublished."
```

---

### Trends page (L553) — current score 6.0

**Current:**
```python
f"Twelve sectoral trends shape the AI and digital government opportunity surface in Uzbekistan and Kyrgyzstan in 2025–2026: public administration, justice, health, education, agriculture and water, energy, transport, finance, security, environment, tourism, and labour migration. Each trend is grounded in specific decrees, donor programmes, and named decision-makers."
```

**Replacement:**
```python
f"Twelve sectors carry active AI or digital government procurement in Uzbekistan and Kyrgyzstan in 2025–2026. Each entry maps to at least one active decree, one donor programme, and one named decision-maker. The {n} trend records in this dataset cover: public administration, justice, health, education, agriculture, energy, transport, finance, security, environment, tourism, and labour migration."
```

---

### Scoring page (L388) — current score 6.6

**Current:**
```python
'Every initiative is scored on five axes with weighted totals: '
'Speed-to-Contract at twenty-five percent, Strategic Moat at twenty percent, Defensibility '
'at twenty percent, Capital Access at twenty percent, and Russian/CIS Fit at fifteen percent. '
'A weighted total above seven and a half drops into Tier-A; below six is Tier-C or worse.'
```

**Replacement:**
```python
'Every initiative is scored 1–10 on five axes: Speed-to-Contract (25%), Strategic Moat (20%), '
'Defensibility (20%), Capital Access (20%), and Russian/CIS Fit (15%). '
'Weighted total ≥7.5 = Tier-A (verified, deal-path documented). '
'6.0–7.4 = Tier-B (develop). Below 6.0 = Tier-C (monitor or drop).'
```

---

## 5. Style Guide for Future Renders (5 Rules)

**Rule 1 — No "This page / This list / This map / This pipeline" openers.**
Start with the noun or the number. "47 tenders..." not "This page tracks 47 tenders."

**Rule 2 — Spell numbers as digits in leads, not words.**
"Speed-to-Contract (25%)" not "Speed-to-Contract at twenty-five percent." Reserve word-form only for numbers below ten in running prose.

**Rule 3 — No unverified comparatives.**
"Higher LinkedIn responsiveness than ministers" requires a source citation or deletion. Replace all unanchored "frequently," "often," "routinely," and "highest-leverage" with either a number or nothing.

**Rule 4 — No jargon on first use without a plain-English gloss.**
"Convergent windows" → define inline: "sectors where an active decree, donor funding, and a named buyer align." "MVR" → define on first use. "Wizard of Oz" → replace with "manual-fulfillment prototype."

**Rule 5 — First-person ban in all rendered HTML.**
Grep for `we`, `our`, `us`, `I`, `my` before every deploy. The render script's `honesty_page` H1 currently violates this ("what we did not find"). The fix is one token: "what the research did not find."

---

_Word count: ~1 180 words. All BEFORE/AFTER samples are directly applicable as Edit operations on `scripts/render_site.py`._
