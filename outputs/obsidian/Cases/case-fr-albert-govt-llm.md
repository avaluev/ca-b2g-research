---
type: "global_case"
id: "case-fr-albert-govt-llm"
country_origin: "France"
sector: "Cross-cutting"
year_initiated: 2023
uz_transferability_score: 9
kg_transferability_score: 8
verification: "VERIFIED"
---

# France Albert — Government LLM for Civil Servants

**Origin**: France  •  **Year**: 2023  •  **Sector**: Cross-cutting

## Problem solved

French civil servants used commercial LLMs (ChatGPT, Claude) for drafting documents, summarising reports, and answering policy questions — but this created data sovereignty issues (government documents sent to US servers) and inconsistent quality (commercial models don't know French administrative law and procedures). Albert is France's sovereign LLM for public servants, hosted on French government cloud.

## Architecture

Albert (DINUM — Interministerial Direction for Digital Government): Mistral-based LLM fine-tuned on French public administration corpus (legal texts, ministerial circulars, administrative procedures). Hosted on HBS (Health and Social Security Base) sovereign cloud infrastructure. Access: API for government developers, chat interface for civil servants via albert.etalab.studio. Open-source: weights published under permissive licence. Data pipeline: regular fine-tuning on new government documents. Use cases: policy memo drafting, legal text analysis, citizen inquiry summarisation, code generation for government developers.

## UZ transferability (9/10)

УП-189 explicitly mandates a UZ AI Cluster — a sovereign Uzbek/Russian government LLM is the PRIMARY USE CASE for that cluster. France Albert is the architecture reference: Mistral open-source base + UZ administrative corpus fine-tuning + UZ sovereign cloud hosting. Key datasets: lex.uz (all decrees), gov.uz (administrative documents), court decisions (sud.uz). Budget: $3-6M for UZ government LLM. New Uzbekistan University AI Cluster is the logical host. This is potentially the highest-value convergent opportunity in the entire tournament.

## KG transferability (8/10)

KG needs a Kyrgyz/Russian government LLM for: parliamentary drafting assistance, Tunduk service chatbot, ministry memo drafting. KG could either (1) join the UZ government LLM effort as a bilingual extension (Russian shared, Kyrgyz separate), or (2) build independently. Budget: $2-4M. The joint UZ+KG approach (shared Russian layer + separate national language layers) is more cost-effective.
