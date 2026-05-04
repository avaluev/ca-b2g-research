# GEO / AIO / AEO / LLMO Audit — Report 05

**Auditor**: GEO/AIO/AEO/LLMO Specialist
**Date**: 2026-05-03
**Site**: https://avaluev.github.io/ca-b2g-research/
**Scope**: Live assets + local `scripts/render_site.py` and `scripts/build_seo_assets.py`

---

## 1. Discovery-Asset Validation

| Asset | Exists | Spec compliance | Findings |
|---|---|---|---|
| `robots.txt` | PASS | PASS | All major AI crawlers explicitly allowed (GPTBot, ChatGPT-User, OAI-SearchBot, ClaudeBot, Claude-SearchBot, Claude-User, anthropic-ai, PerplexityBot, Perplexity-User, Google-Extended, GoogleOther, Applebot-Extended, Bingbot, DuckDuckBot, YandexBot). Missing: `cohere-ai`, `meta-externalagent`, `Bytespider`, `AwsBot`. |
| `sitemap.xml` | PASS | PASS | 17 canonical URLs, all dated `2026-05-03`. Missing `<changefreq>` and `<priority>` (optional but improves crawl scheduling). |
| `feed.xml` | PASS | WARN | Valid Atom 1.0 structure. All 17 entries share identical `<updated>` timestamp — should reflect actual per-page `dateModified`. HTML `<link rel="alternate">` uses `type="application/rss+xml"` — must be `application/atom+xml` for Atom 1.0 (RFC 5005 §4). |
| `llms.txt` | PASS | WARN | Valid llmstxt.org format (title, blockquote description, `## Pillar pages`). Titles for home and lenses pages are truncated to 60 chars with `...` — llms.txt should carry full titles. No `## Optional` section for secondary pages. |
| `llms-full.txt` | PASS | PASS | 17 pages concatenated, nav/footer/script stripped. Headings use `## URL:` format. |
| `humans.txt` | PASS | PASS | Present. |
| `.well-known/security.txt` | PASS | WARN | Missing `Policy:` field (RFC 9116 §2.5.3 recommends it). |
| `manifest.webmanifest` | PASS | WARN | Present but not linked from HTML `<head>` via `<link rel="manifest">`. |

**Missing AI crawlers to add to robots.txt**: `cohere-ai`, `meta-externalagent`, `Bytespider`.

---

## 2. JSON-LD `@graph` — Current vs Ideal

### Critical Bug: Duplicate WebSite node on Home page

The home page calls `render_page(..., page_type="WebSite")` which inserts a second `WebSite` node into the `@graph` alongside the shared `WebSite` already present in `jsonld_graph()`. This produces:

```
@graph types: ['Organization', 'Person', 'WebSite', 'BreadcrumbList', 'WebSite']
@id repeated: '#website' appears twice
```

Google's Rich Results validator treats duplicate `@id` as an error and may suppress the entire `@graph`.

### Current vs Ideal @graph per page type

| Page | Current `@type` for page node | Ideal `@type` |
|---|---|---|
| Home (`/`) | `WebSite` (duplicate — bug) | `CollectionPage` or `WebPage` |
| Methodology | `Article` | `HowTo` |
| Lenses | `Article` | `Article` (acceptable) |
| Scoring | `Article` | `Article` (acceptable) |
| Decrees UZ/KG | `Article` | `Dataset` or `Article` with `Dataset` sidecar |
| Institutions | `Article` | `Article` |
| Donors | `Article` | `Article` |
| People | `Article` | `ProfilePage` |
| Initiatives | `Article` | `ItemList` + `Article` |
| Provenance | `Article` | `Article` |
| Honesty | `Article` | `Article` |

### Missing schema nodes (all pages)

- `Dataset` node for knowledge_graph.json is absent from every page
- `SpeakableSpecification` absent — Google uses this for voice/Assistant
- `FAQPage` absent from Q&A-headed pages (home, decrees, methodology, people, provenance)
- `HowTo` absent from methodology page
- `Person` node lacks `jobTitle`, `worksFor`, `knowsAbout`, and Wikidata/ORCID `sameAs` entries

### Ideal `@graph` for home page

```json
{
  "@context": "https://schema.org",
  "@graph": [
    { "@type": "Organization", "@id": "#organization", ... },
    { "@type": "Person", "@id": "#operator", "jobTitle": "B2G Research Analyst",
      "knowsAbout": ["Central Asia", "B2G", "AI in government", "Uzbekistan", "Kyrgyzstan"],
      "sameAs": ["https://www.linkedin.com/in/avaluev/", "https://github.com/avaluev"] },
    { "@type": "WebSite", "@id": "#website", ... },
    { "@type": "BreadcrumbList", ... },
    { "@type": "CollectionPage", "@id": "#collectionpage", ... },
    { "@type": "Dataset", "@id": "#dataset",
      "name": "Central Asia B2G Knowledge Graph",
      "description": "...", "license": "https://apache.org/licenses/LICENSE-2.0",
      "creator": { "@id": "#operator" },
      "url": "https://github.com/avaluev/ca-b2g-research",
      "distribution": [{ "@type": "DataDownload", "encodingFormat": "application/json",
        "contentUrl": "https://github.com/avaluev/ca-b2g-research/blob/main/state/knowledge_graph.json" }]
    },
    { "@type": "FAQPage", "mainEntity": [
        { "@type": "Question", "name": "What is in this research?",
          "acceptedAnswer": { "@type": "Answer", "text": "100 deployable AI/digital government initiatives..." } },
        { "@type": "Question", "name": "How was it produced?",
          "acceptedAnswer": { "@type": "Answer", "text": "An eleven-agent multi-wave pipeline..." } }
    ]}
  ]
}
```

---

## 3. Per-Page GEO/AIO Compliance Score (1–10)

| Page | H1 | Lead words | Question H2s | Section summaries | Meta complete | dateModified | Schema type | Score |
|---|---|---|---|---|---|---|---|---|
| Home `/` | 1 | 48 | 4/4 | Absent | PASS | Current | WebSite (dupe bug) | **6/10** |
| Initiatives | 1 | 49 | 1/2 | Absent | PASS | Current | Article | **6/10** |
| Decrees UZ | 1 | 41 | 1/2 | Absent | PASS | Current | Article | **5/10** |
| People | 1 | 51 | 2/2 | Absent | PASS | Current | Article | **6/10** |
| Provenance | 1 | 53 | 2/2 | Absent | PASS | Current | Article | **7/10** |
| Methodology | 1 | 53 | 3/3 | Absent | PASS | Current | Article (should be HowTo) | **6/10** |

**Common deductions**: no FAQPage schema (-1), no section summaries (-1), no speakable spec (-0.5), no expert quotes (-0.5).

---

## 4. Eight Specific Schema Additions

1. **FAQPage on home** — The 4 Q&A headings (`What is in this research?`, `How was it produced?`, `Who is this for?`, `Where to start`) are exactly the FAQPage format. Markup them as `@type: FAQPage` with `acceptedAnswer` from the paragraph text following each H2. Prerequisite: content must be DOM-visible (it is).

2. **HowTo on methodology** — Replace `page_type="Article"` with `page_type="HowTo"`. Add `HowTo.step[]` array mapping each wave row in the table to a `HowToStep` with `name` (wave description) and `text` (agent details).

3. **Dataset on home (and knowledge graph link)** — Add a `Dataset` node to the home page `@graph` pointing to the GitHub JSON export. Minimal required fields: `name`, `description`, `license`, `creator`, `url`, `distribution`.

4. **ItemList on initiatives** — The initiative table is a natural `ItemList`. Add an `ItemList` node wrapping the top-10 Tier-A items with `ListItem` → `name`, `url`, `description`, and `position`.

5. **SpeakableSpecification on home** — Add `"speakable": { "@type": "SpeakableSpecification", "cssSelector": ["h1", ".lead.summary"] }` to the home `Article`/`CollectionPage` node. This tells Google Assistant which sentences to read aloud.

6. **ProfilePage on people** — The people page is a directory of named persons. Use `page_type="ProfilePage"` (or `CollectionPage`) to signal that intent to Google.

7. **Person node enrichment** — Add `jobTitle`, `knowsAbout` array, and `worksFor` to the shared `#operator` Person node so AI citation engines have richer context about the author's expertise domain.

8. **Dataset schema in provenance page JSON-LD** — The provenance page describes the research corpus. Embed a `Dataset` node here citing `state/knowledge_graph.json` as a `DataDownload`, with `measurementTechnique` describing the multi-model verification method. This makes the research citable as a dataset by Google Scholar and AI engines that index datasets.

---

## 5. llms.txt Enhancement Plan

Current state: valid but thin — titles are truncated, no `Optional` section, no explicit content-type tags per llmstxt.org extended spec.

**Enhancements (in `build_seo_assets.py → write_llms_txt`):**

```
# Add before writing:
1. Pass full (untruncated) titles to llms.txt — the 60-char cap only applies to <title> HTML tag
2. Add "## Optional" section listing methodology, scoring, lenses, honesty pages
3. Move data-heavy pages (initiatives, decrees, people, donors) under "## Data pages"
4. Add a "## Contact" section: "- Contact: valuev.alexandr@gmail.com"
5. Add "## License": "- Apache 2.0: https://github.com/avaluev/ca-b2g-research/blob/main/LICENSE"
```

Proposed structure:
```
# Central Asia B2G Intelligence

> [blockquote — keep as is]

## Pillar pages          ← research outputs, keep
## Data pages            ← NEW: decrees, people, donors, procurement, institutions
## Methodology           ← NEW section for methodological pages
## Optional              ← lenses, scoring, mvp, trends, honesty, provenance
## Contact               ← NEW
## License               ← NEW
```

---

## 6. Ten Question-Form Heading Rewrites (five weakest pages)

**Initiatives** (score: 6/10):
1. `Initiatives` → `Which B2G initiatives are ready to deploy now?`
2. `How is each initiative grounded?` — keep but add 40-word summary paragraph below

**Decrees UZ** (score: 5/10):
3. `Decrees` → `Which Uzbekistan decrees are in their active implementation window?`
4. `What is the decree half-life?` — keep; add 40-word summary below it

**Decrees KG** (same issues as UZ):
5. `Decrees` → `Which Kyrgyzstan decrees create active procurement authority now?`

**Home** (score: 6/10 due to schema bug):
6. `Where to start` → `Where should a B2G operator start with this research?`

**People** (score: 6/10):
7. `Tier-1 / Tier-2 decision-makers` → `Which decision-makers control AI and digital procurement in Uzbekistan and Kyrgyzstan?`
8. `What is the diaspora bridge?` — keep; add 40-word summary below it

**Methodology** (schema type wrong but headings are good):
9. `What does each wave do?` — keep; add 40-word section summary below
10. `What is the source priority?` — keep; add 40-word section summary below

---

## 7. Bot Reference Table

| Bot name | robots.txt | Notes |
|---|---|---|
| GPTBot | Allowed | OpenAI web crawl bot |
| ChatGPT-User | Allowed | ChatGPT browsing plugin |
| OAI-SearchBot | Allowed | OpenAI search bot |
| ClaudeBot | Allowed | Anthropic web index |
| Claude-SearchBot | Allowed | Anthropic search |
| Claude-User | Allowed | Anthropic user-triggered |
| anthropic-ai | Allowed | Anthropic legacy identifier |
| PerplexityBot | Allowed | Perplexity web crawl |
| Perplexity-User | Allowed | Perplexity user-triggered |
| Google-Extended | Allowed | Gemini/Google AI training |
| GoogleOther | Allowed | Google experimental |
| Applebot-Extended | Allowed | Apple Intelligence |
| Bingbot | Allowed | Bing/Copilot |
| DuckDuckBot | Allowed | DuckDuckGo |
| YandexBot | Allowed | Yandex |
| cohere-ai | **MISSING** | Add |
| meta-externalagent | **MISSING** | Meta AI |
| Bytespider | **MISSING** | ByteDance/TikTok AI |

---

## 8. Twelve Prioritized Fixes

Priority order: P1 = blocks correct indexing now; P2 = significant citation uplift; P3 = incremental.

### P1 — Fix duplicate WebSite node (Critical)
**File**: `scripts/render_site.py`
**Fix**: Change `page_type="WebSite"` to `page_type="CollectionPage"` in the home page `render_page()` call. The `jsonld_graph()` function already emits a shared `WebSite` node — the page-level node must be a different type.

### P1 — Fix Atom feed `<link rel="alternate">` type
**File**: `scripts/render_site.py`, line ~235
**Fix**: Change `type="application/rss+xml"` to `type="application/atom+xml"`.

### P1 — Add `<link rel="manifest">` to HTML head
**File**: `scripts/render_site.py`, in `render_page()` head block
**Fix**: Add `<link rel="manifest" href="/manifest.webmanifest">` to the `<head>` template.

### P2 — Add FAQPage schema to home page
**File**: `scripts/render_site.py`, in `homepage()` function
**Fix**: Pass `extra_head` containing an additional `<script type="application/ld+json">` with `FAQPage` schema extracting Q/A from the 4 H2 sections. (Separate `<script>` block avoids touching the shared `@graph`.)

### P2 — Change methodology to `page_type="HowTo"` with steps
**File**: `scripts/render_site.py`, methodology render call
**Fix**: Pass `page_type="HowTo"` and add `extra_head` with a HowTo JSON-LD block mapping each wave to a `HowToStep`.

### P2 — Add Dataset node to home and provenance pages
**File**: `scripts/render_site.py`
**Fix**: Add a `Dataset` JSON-LD block in `extra_head` on both the home page and the provenance page, pointing to the GitHub knowledge_graph.json.

### P2 — Add SpeakableSpecification to home page
**File**: `scripts/render_site.py`
**Fix**: Add `"speakable": { "@type": "SpeakableSpecification", "cssSelector": ["h1", ".lead.summary"] }` to the home `CollectionPage` node.

### P2 — Enrich Person node with `jobTitle` and `knowsAbout`
**File**: `scripts/render_site.py`, in `jsonld_graph()`
**Fix**: Add `"jobTitle": "B2G Market Research"` and `"knowsAbout": ["Central Asia", "B2G", "AI in government", "Uzbekistan", "Kyrgyzstan", "digital procurement"]` to the Person block.

### P2 — Add section summary paragraphs under each H2
**File**: `scripts/render_site.py`, per-page body functions
**Fix**: Each H2 heading should be followed by a 40–50 word direct-answer paragraph before any tables or lists. Currently the decrees, initiatives, and home pages jump directly to tables or generic descriptions. Add a `<p class="section-summary">` after each `<h2>`.

### P3 — Add missing AI bots to robots.txt
**File**: `scripts/build_seo_assets.py`, `write_robots()`
**Fix**: Add `cohere-ai`, `meta-externalagent`, `Bytespider` blocks.

### P3 — Fix llms.txt truncated titles and add Optional/Data sections
**File**: `scripts/build_seo_assets.py`, `write_llms_txt()`
**Fix**: Use untruncated titles in llms.txt lines. Split pages into `## Pillar pages`, `## Data pages`, and `## Optional` sections.

### P3 — Add `<link rel="alternate" type="application/atom+xml">` to head and security.txt Policy field
**File**: `scripts/render_site.py` (feed type) and `scripts/build_seo_assets.py` (security.txt)
**Fix**: Correct the feed MIME type and add `Policy: https://github.com/avaluev/ca-b2g-research` to security.txt.

---

## Summary

The site has strong bones: all major AI crawlers are allowed, every page has a single H1, question-form H2s are present on all 5 audited pages, lead summaries are in the 40–60 word range, all required meta tags are present, and `dateModified` is current. The critical gap is the duplicate `WebSite` node on the home page (a schema validator error), the absence of `FAQPage`, `HowTo`, and `Dataset` schema types that directly boost AI citation rates, and missing `SpeakableSpecification` for voice search. Applying P1 fixes takes under 30 minutes; P2 fixes add the schema richness that causes AI Overviews to cite specific passages.
