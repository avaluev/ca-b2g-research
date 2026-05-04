# HubSpot $1M Solopreneur MVR Framework — Encoded Into Wave 4b

> Source: HubSpot's "$1M Solopreneur MVP" framework (lean validation distilled
> into "build a Minimum Viable Representation, validate in 7 days, not 12
> months"). Encoded into the Wave 4b agent at
> `prompts/pipeline/09-solopreneur-mvp-synthesizer.md`.

## Why a separate solopreneur track?

The institutional B2G pipeline (Wave 4) produces enterprise plays for
USD 500K–10M contracts that take 12–36 months. That's the right scale for
vendors with capital, sales teams, and government affairs leads. It's the
wrong scale for a solo founder bootstrapping in Tashkent or Bishkek.

Wave 4b runs in **parallel** to Wave 4, consuming the same merged
knowledge graph but applying a different lens: every record becomes a
"how could one person ship a Minimum Viable Representation in seven days
that converts a frontier-market pain point into USD 0–1M ARR?"

## Definition (per the framework)

> "An MVR is a Minimum Viable Representation — a landing page, demo
> video, free tool, directory, manifesto, or Wizard-of-Oz manual service.
> Not a finished product. Validate in 7 days, not 12 months."

## Eight MVR vehicles

The framework specifies eight vehicles. The Wave 4b schema enforces that
every MVP record cites exactly one:

| Vehicle | When it fits | Example |
|---|---|---|
| `landing_page` | SaaS demand signaling | TenderRadar UZ — waitlist for live-tender alert digest |
| `squeeze_page` | Pure email-capture, lead magnet | Diaspora Investor Newsletter — "first 100 deals" mailing list |
| `demo_video` | AI-tool category, especially | EPIGU Companion — Loom screen-record of a chatbot answering a real `gov.uz` workflow |
| `free_tool` | One micro-problem, no login | DigitalSignWalker — step-by-step ECP enrolment guide |
| `directory` | Content + ad / listing-fee | Bishkek IT-park alumni directory |
| `wizard_of_oz` | Manual fulfillment masquerading | FormFiller UZ — Telegram bot routes form to human filler |
| `ad_booking` | Productized service | MigrantWageGuard — FB ad → Calendly booking → manual case |
| `manifesto` | Audience-building, viral-leaning | "Why every UZ ministry should publish its API by 2027" blog post |

## 5-axis scoring (per spec, distinct from B2G rubric)

```
weighted_total = 0.30 * demand_clarity
                + 0.15 * speed_to_mvr
                + 0.20 * monetization_path
                + 0.20 * founder_solo_feasibility
                + 0.15 * local_market_fit
```

- **Demand clarity (30%)**: how specific and verifiable is the underlying demand signal? Is there a named user group hurting today? — Highest weight because faking demand is the #1 failure mode.
- **Speed to MVR (15%)**: days to ship the first MVR. Cap 14, target 7.
- **Monetization path (20%)**: clear $0 → $50K → $250K → $1M trajectory.
- **Founder solo feasibility (20%)**: can one person realistically run build + market + support + fulfill?
- **Local market fit (15%)**: price point matches local purchasing power (UZ avg $300/mo, KG ~$250/mo); payment rails accessible (UZ Click/Payme, KG Mbank/Optima).

## Tier mapping

```
Tier A: weighted_total ≥ 7.5  (top ~25%)
Tier B: weighted_total ≥ 6.0
Tier C: weighted_total ≥ 4.5
Tier D: < 4.5  (drop)
```

## Idea-generation strategy

The agent walks the knowledge graph in this order to generate 100 MVPs per
country:

1. **Trend-anchored** (40% of ideas): for each Trend record, brainstorm 2–4 solopreneur products
2. **Decree-anchored** (20%): for active-window decrees, brainstorm what a solo founder could build to help citizens or businesses comply
3. **Donor-program-anchored** (15%): donor programmes create RFP gaps that solopreneurs can fill
4. **Diaspora-bridge-anchored** (15%): solopreneurs serving Uzbek/Kyrgyz diaspora abroad (remittance, document translation, OFW services)
5. **Pure local-niche** (10%): not anchored to a specific record but obvious from local market gaps

## Hard constraints (must)

- Every idea cites at least one URL evidencing demand
- Concrete local target customer (not "small businesses" but "Andijan-based wedding photographers booking via Instagram")
- Price point grounded in local purchasing power
- `build_time_days ≤ 14`
- Russian / Uzbek / Kyrgyz language anchor in target customer or validation channel
- For UZ: validation channels include at least one local (spot.uz Telegram, IT Park, ICT Week)
- For KG: validation channels include at least one local (24.kg Telegram, kaktus.media, High Tech Park)

## Hard constraints (must not)

- Generate "AI for X" without a specific local pain point cited
- Recommend price points unaffordable to the local market
- Recommend ideas requiring full-stack engineering teams or > USD 5K capex
- Recommend ideas requiring physical inventory > USD 1K
- Recommend ideas in surveillance / facial-recognition / authoritarian-leaning domains
- Duplicate B2G initiatives — these are SOLOPRENEUR MVPs, not enterprise vendor plays
- Hallucinate decree numbers, donor programmes, or trend IDs

## What v1.0.0 produced

- 200 MVPs total (100 UZ + 100 KG)
- 51 Tier-A across both countries
- All eight MVR vehicles represented ≥ 8× per country
- 6 mirror pairs (Tier-A in BOTH countries): FormFiller, TenderRadar,
  TaxScanner, RemittanceCalc, OneTouchPension, MigrantWageGuard
- 8 of top 10 anchor on a 2025-or-later decree
- Wizard-of-Oz wins for week-1 cash (8 of top 25)
- Bilingual local-language UX is the moat versus Western tools

The full record set lives at `state/solopreneur_mvps/{uz,kg}_mvps.json`
and renders to <https://avaluev.github.io/ca-b2g-research/mvp/>.
