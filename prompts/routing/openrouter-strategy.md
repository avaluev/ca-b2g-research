# OpenRouter Routing Strategy

> Anthropic Claude (Opus + Sonnet) does the reasoning and authoring.
> OpenRouter is the cross-model verification layer.
> A hard USD 20 paid budget per run keeps the audit honest without breaking
> the bank.

## Layered model assignment

```
┌─────────────────────────────────────────────────────────────────────┐
│  Reasoning + authoring  │  Anthropic Claude (your subscription)     │
│                         │  - Opus xhigh: Wave 0, 4, 4b, 5           │
│                         │  - Sonnet:     Waves 1, 2, 3, 6 + audit   │
├─────────────────────────────────────────────────────────────────────┤
│  Cross-model            │  OpenRouter PAID (capped at USD 20/run)   │
│  verification           │  - perplexity/sonar-deep-research          │
│  (Tier-1 only)          │    Wave 5 reflexion: re-fetch sources       │
│                         │  - perplexity/sonar-pro                   │
│                         │    Wave 3 people-intelligence:             │
│                         │    LinkedIn URL re-verification            │
│                         │  - openai/o4-mini-deep-research           │
│                         │    Auditor cross-checks (different model) │
├─────────────────────────────────────────────────────────────────────┤
│  Volume / non-critical  │  OpenRouter FREE (50 calls/day per key,   │
│                         │  three keys = ~150/day)                   │
│                         │  - openrouter/owl-alpha (1M context)      │
│                         │  - google/gemma-4-31b-it:free             │
│                         │  - minimax/minimax-m2.5:free              │
└─────────────────────────────────────────────────────────────────────┘
```

## Decision matrix

| Task type | Model class | Why |
|---|---|---|
| Wave 0 strategic plan, lens application | Opus xhigh | Reasoning quality cascades into 7 downstream agents |
| Wave 1 legal corpus from lex.uz / cbd.minjust.gov.kg | Sonnet | Comprehensive cataloguing with rigorous verification |
| Wave 2 four parallel sub-agents | Sonnet | Independent surface harvesting |
| Wave 3 LinkedIn URL re-verification (Tier-1 only) | **Sonar Pro (paid)** | Highest-stakes data — false matches destroy outreach |
| Wave 4 initiative synthesis with foreign-key integrity | Opus xhigh | Cross-doc reasoning under hard schema constraints |
| Wave 4b solopreneur MVPs grounded in HubSpot framework | Opus | Synthesis + framework application |
| Wave 5 reflexion audit on Tier-A claims | **Sonar Deep Research (paid) + Sonnet auditor** | Different model than original agent — breaks echo chamber |
| Wave 6 outreach drafting | Sonnet | Pattern-rich, format-heavy, lower per-call risk |
| Audit Team (16 specialists) | Sonnet | Public web + local file analysis, no paid OpenRouter needed |

## Hard caps

```python
# scripts/openrouter_client.py
class OpenRouterClient:
    BUDGET_USD_DEFAULT = 20.0      # per-run hard cap
    MAX_SEARCH_COUNT = 30          # Sonar DR per-call cap
    MAX_TOKENS_OUT = 4000
    REASONING_EFFORT = "medium"    # not "high" (avoids 100+ search blowout)
```

## Cost reality (v1.0.0 release)

```
Anthropic (your subscription):
  Wave 0  Opus     ~30 min, ~$2-4
  Wave 1  Sonnet   ~90 min, ~$15-25
  Wave 2  Sonnet   ~90 min, ~$25-40
  Wave 3  Sonnet   ~60 min, ~$15-25
  Wave 4  Opus     ~60 min, ~$5-10
  Wave 4b Opus     ~60 min, ~$5-10
  Wave 5  Opus     ~90 min, ~$5-8
  Wave 6  Sonnet   ~60 min, ~$5-10
  Audit (16 spec)  ~30 min, ~$4-8
  ─────────────────────────────
  Anthropic subtotal: ~$80-140 (subscription-included)

OpenRouter paid:
  Wave 3 LinkedIn re-verification (≤15 Sonar Pro calls): ~$3-6
  Wave 5 Tier-A claim re-check (≤20 Sonar DR calls):     ~$5-12
  ─────────────────────────────
  OpenRouter paid subtotal:  $0.025 actual / $20 cap
                             (we used 8 paid + 13 free OpenRouter calls)

OpenRouter free (volume layer):  $0
```

## Why we don't use Sonar Deep Research everywhere

Sonar Deep Research is brilliant — and dangerous. Each call can issue
100+ web searches at $5/1000 surcharge. A naïve high-effort call can
spend $0.50–$1.00 in 30 seconds. The wrapper at
`scripts/openrouter_client.py` enforces:

- `max_search_count: 30` per Sonar DR call
- `reasoning_effort: medium` (not "high")
- Pre-call cost estimation against the `state/external/_quota.json` ledger
- Auto-fallback to free models when the per-run budget would be exceeded

## Why a different model for the auditor

The reflexion-auditor must NOT call the same model that produced the
original claim. Same model = echo chamber = false-positive verification.
The Wave 5 spec explicitly routes:

```
Wave 4 synthesizer   uses: Anthropic Opus + Owl Alpha (free)
Wave 5 auditor       uses: Anthropic Opus + perplexity/sonar-deep-research (paid)
                                              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                                              different vendor + different
                                              architecture = independent grounding
```

This is how Wave 5 caught four wrong Tier-1 identities in v1.0.0
(IT Park UZ CEO, KG UDP head, KG Min Health, KG last Минцифры minister).
A same-model auditor would have re-confirmed all four wrong.

## How to extend

To add a new model to the routing layer:

1. Add an entry in `RATE_CARD` in `scripts/openrouter_client.py` with input,
   output, and (if applicable) per-search pricing.
2. Add it to `PAID_MODELS` if it bills per call, otherwise leave it out
   (it will be treated as free).
3. Update the routing decision in the relevant agent spec under
   `prompts/pipeline/`.
4. Re-run `scripts/openrouter_client.py --self-test` to confirm key
   rotation and cost estimation work.
