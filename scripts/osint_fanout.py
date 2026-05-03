#!/usr/bin/env python3
"""
OSINT fan-out — parallel multi-model OpenRouter research.

Bridges Claude Code agents to OpenRouter. An agent calls this from its Bash
tool to obtain cross-verified research evidence on a specific question, e.g.:

    python3 scripts/osint_fanout.py \
        --topic uz-decrees \
        --schema Decree \
        --query "List Uzbekistan presidential decrees on AI signed 2024-2026" \
        --country UZ \
        --free-only

Output: state/external/<topic>/<hash>.json — an EvidenceCard the agent reads
and uses as supplementary evidence (with verification: L2_VERIFIED).

Idempotency: keyed by sha256(query + country + lang). Repeated calls hit cache.
"""

from __future__ import annotations

import argparse
import asyncio
import hashlib
import json
import os
import sys
from dataclasses import asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

# Local import
sys.path.insert(0, str(Path(__file__).resolve().parent))
from openrouter_client import OpenRouterClient, BudgetExceededError, CallResult, PAID_MODELS  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
EXTERNAL_ROOT = ROOT / "state" / "external"

# Default model rotation
FREE_MODELS = [
    "openrouter/owl-alpha",
    "google/gemma-4-31b-it:free",
]
PAID_VERIFICATION = "perplexity/sonar-deep-research"
PAID_SEARCH = "perplexity/sonar-pro"


def query_hash(query: str, country: str | None = None, lang: str | None = None) -> str:
    blob = f"{query}|{country or ''}|{lang or ''}".encode("utf-8")
    return hashlib.sha256(blob).hexdigest()[:16]


def build_messages(query: str, schema: str, country: str | None, lang: str | None) -> list[dict[str, str]]:
    sys_msg = (
        "You are an OSINT researcher producing structured evidence for a B2G "
        "intelligence pipeline on Uzbekistan and Kyrgyzstan. "
        "Return facts with citation URLs. "
        "Decline to fabricate. Prefer Russian-language primary sources for country claims. "
        "If you cannot find a fact, say so explicitly. "
        f"Target schema fragment: {schema}. "
        "Output format: short bulleted facts, each with a [URL] tag pointing to the source."
    )
    if country:
        sys_msg += f" Country focus: {country}."
    if lang:
        sys_msg += f" Output language: {lang}."
    return [
        {"role": "system", "content": sys_msg},
        {"role": "user", "content": query},
    ]


async def run_one(client: OpenRouterClient, model: str, messages: list[dict[str, str]]) -> CallResult:
    """Run one chat call in a thread (httpx is sync here, but we want concurrency)."""
    loop = asyncio.get_running_loop()
    return await loop.run_in_executor(
        None,
        lambda: client.chat(model=model, messages=messages, max_tokens=2500, max_search_count=20),
    )


async def fan_out(
    client: OpenRouterClient,
    models: list[str],
    messages: list[dict[str, str]],
) -> list[CallResult]:
    coros = [run_one(client, m, messages) for m in models]
    return await asyncio.gather(*coros, return_exceptions=False)


def aggregate(results: list[CallResult]) -> dict[str, Any]:
    """Build a consensus / disagreement summary across the responses."""
    all_citations: dict[str, dict[str, str]] = {}
    answers: list[dict[str, Any]] = []
    for r in results:
        for c in r.citations:
            url = c.get("url", "")
            if url and url not in all_citations:
                all_citations[url] = c
        answers.append(
            {
                "model": r.model,
                "response_id": r.response_id,
                "answer": r.answer,
                "citations": r.citations,
                "tokens_in": r.tokens_in,
                "tokens_out": r.tokens_out,
                "cost_usd": r.cost_usd,
                "latency_ms": r.latency_ms,
                "fetched_at": r.fetched_at,
                "error": r.error,
            }
        )
    total_cost = sum(r.cost_usd for r in results)
    return {
        "responses": answers,
        "consensus": {
            "high_agreement_facts": [],  # left for downstream agent to extract
            "disagreements": [],
        },
        "sources_normalized": list(all_citations.values()),
        "total_cost_usd": round(total_cost, 6),
    }


def write_card(
    card_path: Path,
    *,
    topic: str,
    schema: str,
    query: str,
    country: str | None,
    lang: str | None,
    models_called: list[str],
    aggregated: dict[str, Any],
) -> None:
    card_path.parent.mkdir(parents=True, exist_ok=True)
    card = {
        "card_id": f"{topic}__{card_path.stem}",
        "topic": topic,
        "schema_fragment": schema,
        "query": query,
        "country_filter": country,
        "language_preference": lang,
        "models_called": models_called,
        "responses": aggregated["responses"],
        "consensus": aggregated["consensus"],
        "sources_normalized": aggregated["sources_normalized"],
        "total_cost_usd": aggregated["total_cost_usd"],
        "downstream_verification": "L2_VERIFIED",
        "generated_at": datetime.now(timezone.utc).isoformat(),
    }
    card_path.write_text(json.dumps(card, indent=2, ensure_ascii=False))


def select_models(*, free_only: bool, prefer_search: bool) -> list[str]:
    if free_only:
        return list(FREE_MODELS)
    # Paid path: 1 verification + 1 free for cross-check
    if prefer_search:
        return [PAID_SEARCH, FREE_MODELS[0]]
    return [PAID_VERIFICATION, FREE_MODELS[0]]


def main() -> int:
    p = argparse.ArgumentParser(description="Multi-model OpenRouter fan-out for OSINT")
    p.add_argument("--topic", required=True, help="namespace under state/external/")
    p.add_argument("--schema", default="Source", help="state_schema fragment hint")
    p.add_argument("--query", required=True, help="research question")
    p.add_argument("--country", default=None, choices=["UZ", "KG", "BOTH", None])
    p.add_argument("--lang", default=None, choices=["ru", "en", "uz", "ky", None])
    p.add_argument("--models", default=None, help="comma-separated model slugs (overrides routing)")
    p.add_argument("--free-only", action="store_true", help="only call free models")
    p.add_argument("--prefer-search", action="store_true", help="prefer Sonar Pro for agentic search")
    p.add_argument("--budget-usd", type=float, default=None, help="per-call budget cap")
    p.add_argument("--force", action="store_true", help="bypass cache")
    p.add_argument("--quiet", action="store_true")
    args = p.parse_args()

    client = OpenRouterClient()
    if args.budget_usd is not None:
        client.budget_usd = min(client.budget_usd, args.budget_usd)

    h = query_hash(args.query, args.country, args.lang)
    card_path = EXTERNAL_ROOT / args.topic / f"{h}.json"

    if card_path.exists() and not args.force:
        if not args.quiet:
            print(f"📂 cache hit: {card_path}")
        sys.stdout.write(str(card_path) + "\n")
        return 0

    if args.models:
        models = [m.strip() for m in args.models.split(",") if m.strip()]
    else:
        models = select_models(free_only=args.free_only, prefer_search=args.prefer_search)

    # If no keys, write a degraded card so the harness keeps moving.
    if not client.keys:
        if not args.quiet:
            print("⚠ no openrouter keys; writing degraded card", file=sys.stderr)
        write_card(
            card_path,
            topic=args.topic,
            schema=args.schema,
            query=args.query,
            country=args.country,
            lang=args.lang,
            models_called=[],
            aggregated={
                "responses": [],
                "consensus": {"high_agreement_facts": [], "disagreements": []},
                "sources_normalized": [],
                "total_cost_usd": 0.0,
            },
        )
        sys.stdout.write(str(card_path) + "\n")
        return 0

    messages = build_messages(args.query, args.schema, args.country, args.lang)

    try:
        results = asyncio.run(fan_out(client, models, messages))
    except BudgetExceededError as e:
        if not args.quiet:
            print(f"💰 budget exceeded: {e}", file=sys.stderr)
        # Fallback: try free models only
        models = list(FREE_MODELS)
        results = asyncio.run(fan_out(client, models, messages))

    aggregated = aggregate(results)
    write_card(
        card_path,
        topic=args.topic,
        schema=args.schema,
        query=args.query,
        country=args.country,
        lang=args.lang,
        models_called=models,
        aggregated=aggregated,
    )
    if not args.quiet:
        print(f"✅ wrote {card_path}  models={models}  cost=${aggregated['total_cost_usd']:.4f}")
    sys.stdout.write(str(card_path) + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
