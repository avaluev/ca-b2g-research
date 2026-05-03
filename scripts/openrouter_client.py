#!/usr/bin/env python3
"""
OpenRouter client — thin OpenAI-compatible wrapper.

Responsibilities:
- Multi-key rotation (paid -> free_1 -> free_2 -> legacy fallback)
- Tenacity retry with exponential backoff on 429/503/timeout
- Per-call cost estimation + persistent quota ledger
- Hard $20 budget cap (configurable via OPENROUTER_BUDGET_USD)
- Sonar citation passthrough

Usage:
    python3 scripts/openrouter_client.py --self-test
    python3 scripts/openrouter_client.py --model openrouter/owl-alpha --prompt "Hello"

As a library:
    from openrouter_client import OpenRouterClient
    client = OpenRouterClient()
    resp = client.chat(model="openrouter/owl-alpha", messages=[...])
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
from dataclasses import dataclass, field
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any

import httpx
from dotenv import load_dotenv
from tenacity import (
    retry,
    retry_if_exception_type,
    stop_after_attempt,
    wait_exponential,
)

ROOT = Path(__file__).resolve().parent.parent
QUOTA_PATH = ROOT / "state" / "external" / "_quota.json"
ENV_PATH = ROOT / ".env"

# Approximate rate card (USD per 1M tokens), sourced from OpenRouter as of 2026-05.
# Only models we actually call are listed; missing models default to "free".
RATE_CARD: dict[str, dict[str, float]] = {
    "perplexity/sonar-deep-research": {"in": 2.0, "out": 8.0, "search_per_1k": 5.0},
    "perplexity/sonar-pro": {"in": 3.0, "out": 15.0, "search_per_1k": 0.0},
    "perplexity/sonar-pro-search": {"in": 3.0, "out": 15.0, "search_per_1k": 0.0},
    "openai/o4-mini-deep-research": {"in": 2.0, "out": 8.0, "search_per_1k": 0.0},
    # Free models — zero rate
    "openrouter/owl-alpha": {"in": 0.0, "out": 0.0, "search_per_1k": 0.0},
    "google/gemma-4-31b-it:free": {"in": 0.0, "out": 0.0, "search_per_1k": 0.0},
    "google/gemma-4-26b-a4b-it:free": {"in": 0.0, "out": 0.0, "search_per_1k": 0.0},
    "minimax/minimax-m2.5:free": {"in": 0.0, "out": 0.0, "search_per_1k": 0.0},
    "poolside/laguna-m.1:free": {"in": 0.0, "out": 0.0, "search_per_1k": 0.0},
}

PAID_MODELS = {
    "perplexity/sonar-deep-research",
    "perplexity/sonar-pro",
    "perplexity/sonar-pro-search",
    "openai/o4-mini-deep-research",
}


@dataclass
class CallResult:
    model: str
    response_id: str | None
    answer: str
    citations: list[dict[str, str]] = field(default_factory=list)
    tokens_in: int = 0
    tokens_out: int = 0
    cost_usd: float = 0.0
    latency_ms: int = 0
    fetched_at: str = ""
    raw: dict[str, Any] | None = None
    error: str | None = None


class BudgetExceededError(RuntimeError):
    pass


class NoKeyAvailableError(RuntimeError):
    pass


class OpenRouterClient:
    """Thin wrapper. Auto-rotates between paid + free keys."""

    BASE_URL = "https://openrouter.ai/api/v1"

    def __init__(self, env_path: Path = ENV_PATH, quota_path: Path = QUOTA_PATH) -> None:
        load_dotenv(env_path, override=False)
        self.budget_usd = float(os.getenv("OPENROUTER_BUDGET_USD", "20.0"))
        self.keys: dict[str, str] = {}
        for slot in ("PAID", "FREE_1", "FREE_2", "LEGACY"):
            v = os.getenv(f"OPENROUTER_KEY_{slot}", "").strip()
            if v and v != "sk-or-v1-replace-me":
                self.keys[slot] = v
        if not self.keys:
            print(
                "❌ No OpenRouter keys found. Configure .env with OPENROUTER_KEY_PAID etc.",
                file=sys.stderr,
            )
        self.quota_path = quota_path
        self.quota_path.parent.mkdir(parents=True, exist_ok=True)
        self._quota = self._load_quota()
        self.attribution_headers = {
            "HTTP-Referer": os.getenv("SITE_BASE_URL", "https://github.com/avaluev/ca-b2g-research"),
            "X-Title": "Central Asia B2G Research",
        }

    def _load_quota(self) -> dict[str, Any]:
        if self.quota_path.exists():
            try:
                return json.loads(self.quota_path.read_text())
            except Exception:
                pass
        return {
            "total_spend_usd": 0.0,
            "calls_today": {},
            "calls_total": 0,
            "started_at": datetime.now(timezone.utc).isoformat(),
        }

    def _save_quota(self) -> None:
        self.quota_path.write_text(json.dumps(self._quota, indent=2))

    def _key_for(self, model: str) -> tuple[str, str]:
        """Return (slot_name, key) for the given model. Paid models prefer PAID slot;
        free models prefer FREE_1 then FREE_2 (round-robin by call count)."""
        is_paid = model in PAID_MODELS
        order = ["PAID", "FREE_1", "FREE_2", "LEGACY"] if is_paid else ["FREE_1", "FREE_2", "LEGACY", "PAID"]
        today = date.today().isoformat()
        today_calls = self._quota["calls_today"].get(today, {})
        # Within preferred slots, prefer the slot with fewer calls today
        order = sorted(order, key=lambda s: today_calls.get(s, 0))
        for slot in order:
            if slot in self.keys:
                return slot, self.keys[slot]
        raise NoKeyAvailableError(f"No key available for model {model}")

    def _track_call(self, slot: str, cost_usd: float) -> None:
        today = date.today().isoformat()
        self._quota["calls_today"].setdefault(today, {})
        self._quota["calls_today"][today][slot] = self._quota["calls_today"][today].get(slot, 0) + 1
        self._quota["total_spend_usd"] = round(self._quota["total_spend_usd"] + cost_usd, 4)
        self._quota["calls_total"] += 1
        self._save_quota()

    def _estimate_cost(self, model: str, tokens_in: int, tokens_out: int, searches: int = 0) -> float:
        rate = RATE_CARD.get(model, {"in": 0.0, "out": 0.0, "search_per_1k": 0.0})
        return round(
            (tokens_in / 1_000_000) * rate["in"]
            + (tokens_out / 1_000_000) * rate["out"]
            + (searches / 1_000) * rate["search_per_1k"],
            6,
        )

    def remaining_budget(self) -> float:
        return max(0.0, self.budget_usd - self._quota["total_spend_usd"])

    def _check_budget(self, model: str, est_cost: float) -> None:
        if model in PAID_MODELS:
            if self._quota["total_spend_usd"] + est_cost > self.budget_usd:
                raise BudgetExceededError(
                    f"Budget cap ${self.budget_usd:.2f} would be exceeded "
                    f"(spent ${self._quota['total_spend_usd']:.4f}, this call ~${est_cost:.4f})"
                )

    @retry(
        retry=retry_if_exception_type((httpx.TimeoutException, httpx.HTTPStatusError, httpx.NetworkError)),
        wait=wait_exponential(multiplier=1, min=2, max=30),
        stop=stop_after_attempt(4),
        reraise=True,
    )
    def _post(
        self,
        url: str,
        api_key: str,
        payload: dict[str, Any],
        timeout: float = 120.0,
    ) -> httpx.Response:
        with httpx.Client(timeout=timeout) as client:
            resp = client.post(
                url,
                headers={
                    "Authorization": f"Bearer {api_key}",
                    "Content-Type": "application/json",
                    **self.attribution_headers,
                },
                json=payload,
            )
            if resp.status_code in (429, 502, 503, 504):
                resp.raise_for_status()
            return resp

    def chat(
        self,
        model: str,
        messages: list[dict[str, str]],
        max_tokens: int = 4000,
        temperature: float = 0.2,
        max_search_count: int | None = 30,
        extra: dict[str, Any] | None = None,
    ) -> CallResult:
        """Single chat completion call. Auto-rotates keys, tracks budget."""
        # Pre-budget check (rough estimate before we know real token counts)
        rough_in = sum(len(m.get("content", "")) for m in messages) // 3  # ~3 chars/token
        rough_out = max_tokens
        est = self._estimate_cost(model, rough_in, rough_out, searches=max_search_count or 0)
        self._check_budget(model, est)

        slot, key = self._key_for(model)
        payload: dict[str, Any] = {
            "model": model,
            "messages": messages,
            "max_tokens": max_tokens,
            "temperature": temperature,
        }
        # Sonar-specific: cap search budget
        if "perplexity/sonar" in model and max_search_count is not None:
            payload["max_search_count"] = max_search_count
            payload["reasoning_effort"] = "medium"
        if extra:
            payload.update(extra)

        url = f"{self.BASE_URL}/chat/completions"
        t0 = time.monotonic()
        result = CallResult(
            model=model,
            response_id=None,
            answer="",
            fetched_at=datetime.now(timezone.utc).isoformat(),
        )
        try:
            resp = self._post(url, key, payload)
            result.latency_ms = int((time.monotonic() - t0) * 1000)
            if resp.status_code != 200:
                result.error = f"HTTP {resp.status_code}: {resp.text[:500]}"
                return result
            data = resp.json()
            result.raw = data
            result.response_id = data.get("id")
            choice = (data.get("choices") or [{}])[0]
            msg = choice.get("message", {})
            result.answer = msg.get("content", "") or ""
            # Sonar citations may live in message.citations or top-level
            cites = msg.get("citations") or data.get("citations") or []
            for c in cites or []:
                if isinstance(c, str):
                    result.citations.append({"url": c, "title": ""})
                elif isinstance(c, dict):
                    result.citations.append(
                        {"url": c.get("url", ""), "title": c.get("title", "")}
                    )
            usage = data.get("usage", {}) or {}
            result.tokens_in = int(usage.get("prompt_tokens", 0) or 0)
            result.tokens_out = int(usage.get("completion_tokens", 0) or 0)
            num_searches = 0
            if "perplexity/sonar" in model:
                num_searches = int(usage.get("num_search_queries", 0) or 0)
            result.cost_usd = self._estimate_cost(
                model, result.tokens_in, result.tokens_out, num_searches
            )
            self._track_call(slot, result.cost_usd)
        except httpx.HTTPStatusError as e:
            result.error = f"HTTPStatusError: {e}"
        except Exception as e:  # noqa: BLE001
            result.error = f"{type(e).__name__}: {e}"
        return result


# ────────────────────────────────────────────────────────────────────────────
# CLI
# ────────────────────────────────────────────────────────────────────────────


def _self_test(client: OpenRouterClient) -> int:
    print(f"Configured keys: {sorted(client.keys.keys())}")
    print(f"Budget cap: ${client.budget_usd:.2f}")
    print(f"Spent so far: ${client._quota['total_spend_usd']:.4f}")
    print(f"Remaining: ${client.remaining_budget():.4f}")
    print()
    if not client.keys:
        print("❌ No keys configured. Cannot self-test.", file=sys.stderr)
        return 1
    free_model = "openrouter/owl-alpha"
    print(f"Pinging free model {free_model} ...")
    resp = client.chat(
        model=free_model,
        messages=[
            {"role": "system", "content": "Reply in 1 short sentence."},
            {"role": "user", "content": "Say 'OpenRouter live' and nothing else."},
        ],
        max_tokens=20,
    )
    if resp.error:
        print(f"❌ Error: {resp.error}", file=sys.stderr)
        return 1
    print(f"✅ Response: {resp.answer.strip()[:200]}")
    print(f"   Tokens: in={resp.tokens_in} out={resp.tokens_out}  Cost: ${resp.cost_usd:.6f}")
    return 0


def main() -> int:
    p = argparse.ArgumentParser(description="OpenRouter wrapper")
    p.add_argument("--self-test", action="store_true", help="ping a free model and exit")
    p.add_argument("--model", default=None)
    p.add_argument("--prompt", default=None)
    p.add_argument("--system", default=None)
    p.add_argument("--max-tokens", type=int, default=2000)
    p.add_argument("--budget", type=float, default=None)
    args = p.parse_args()

    client = OpenRouterClient()
    if args.budget is not None:
        client.budget_usd = args.budget

    if args.self_test:
        return _self_test(client)
    if not args.model or not args.prompt:
        p.print_help()
        return 1
    msgs: list[dict[str, str]] = []
    if args.system:
        msgs.append({"role": "system", "content": args.system})
    msgs.append({"role": "user", "content": args.prompt})
    resp = client.chat(model=args.model, messages=msgs, max_tokens=args.max_tokens)
    if resp.error:
        print(f"❌ {resp.error}", file=sys.stderr)
        return 1
    out = {
        "model": resp.model,
        "answer": resp.answer,
        "citations": resp.citations,
        "tokens_in": resp.tokens_in,
        "tokens_out": resp.tokens_out,
        "cost_usd": resp.cost_usd,
        "latency_ms": resp.latency_ms,
    }
    print(json.dumps(out, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
