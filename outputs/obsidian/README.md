---
type: "vault_index"
generated_at: "2026-05-04"
---
# Central Asia B2G Intelligence — Obsidian Vault

A typed, source-cited knowledge graph of AI/digital government opportunities in Uzbekistan and Kyrgyzstan. 100 initiatives, 117 decision-makers, 100 decrees, 105 institutions, 49 donor programs.

> [!tip] How to use
> Open the **Graph view** (`Ctrl+G`) to see the full relationship network. Open **Briefs/Top 100 Initiatives** to find Tier-A deals to chase. Use the Dataview queries below to slice the data however you need.

## Counts

- 100 Decrees · 105 Institutions · 117 People · 49 Donor programs
- 50 Tenders · 61 Trends · 100 Global cases · 100 Initiatives

## Top initiatives (by weighted total)

```dataview
TABLE
  weighted_total AS "Score",
  confidence_tier AS "Tier",
  country AS "C",
  sector AS "Sector",
  target_buyer AS "Buyer"
FROM "Initiatives"
WHERE confidence_tier = "A"
SORT weighted_total DESC
LIMIT 30
```

## Decrees in active implementation window

```dataview
TABLE country, decree_type, number, date, signatory
FROM "Decrees"
WHERE half_life_status = "active_window"
SORT date DESC
```

## Tier-1 priority people

```dataview
TABLE country, current_role, linkedin_status, diaspora_advisor_flag
FROM "People"
WHERE priority_tier = 1
SORT country
```

## Donor programs by status

```dataview
TABLE donor, country, status, total_budget_usd, ttl_pm_name
FROM "Donors"
SORT total_budget_usd DESC
```

## Top solopreneur MVPs

```dataview
TABLE
  weighted_total AS "Score",
  confidence_tier AS "Tier",
  country AS "C",
  category AS "Cat",
  sector AS "Sector"
FROM "Solopreneur MVPs"
WHERE confidence_tier = "A"
SORT weighted_total DESC
LIMIT 30
```

## Methodology

See [[00 Methodology]] for the 7-wave research pipeline. See [[01 Lenses]] for the 5+1 analytical lenses applied across every record. See [[02 Scoring]] for the weighted scoring rubric.
