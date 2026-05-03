---
type: "global_case"
id: "case-sg-pair-govt-llm"
country_origin: "Singapore"
sector: "Cross-cutting"
year_initiated: 2023
uz_transferability_score: 9
kg_transferability_score: 8
verification: "VERIFIED"
---

# Singapore PAIR Government LLM Platform

**Origin**: Singapore  •  **Year**: 2023  •  **Sector**: Cross-cutting

## Problem solved

GovTech Singapore needed to deploy LLMs to 150,000 civil servants while maintaining data security, preventing hallucinations in official communications, and enabling government-specific customisation that commercial ChatGPT/Claude APIs could not provide. PAIR (Personal AI Assistant for the Public Service) is Singapore's whole-of-government AI assistant.

## Architecture

PAIR platform on Government Commercial Cloud (GCC): RAG (Retrieval Augmented Generation) architecture — LLM backend (multiple commercial models via API, with data residency on GCC) + government knowledge base (SharePoint, internal databases, policy documents). Guardrails: output scoring for factual claims, automatic citation requirement for claims about policy. Sensitive data handling: classified material NOT allowed in PAIR (ring-fenced), only RESTRICTED and below data. Human-in-the-loop: PAIR outputs are drafts only — officer must review before sending to citizens. Analytics: agency-level LLM usage dashboards for productivity tracking. Open framework: agencies can add their own RAG knowledge bases.

## UZ transferability (9/10)

PAIR architecture is the most directly replicable for UZ government LLM deployment. RAG on lex.uz + gov.uz would create a UZ civil servant AI assistant that can answer questions about decree requirements, administrative procedures, and government services with citation. This is the product that UZ AI Centre should deploy alongside the government LLM infrastructure. Budget: $5-8M for PAIR-equivalent on UZ sovereign cloud with Russian/Uzbek RAG knowledge base.

## KG transferability (8/10)

KG civil service (25,000+ staff) would benefit from PAIR-equivalent for: Tunduk service automation, ministry document drafting, parliamentary briefing assistant. RAG on cbd.minjust.gov.kg + gov.kg would create KG-specific knowledge base. Budget: $2-4M for KG government LLM assistant. Can reuse Russian-language layer from UZ implementation.
