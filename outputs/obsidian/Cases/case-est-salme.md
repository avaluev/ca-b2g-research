---
type: "global_case"
id: "case-est-salme"
country_origin: "Estonia"
sector: "Justice & Rule of Law"
year_initiated: 2019
uz_transferability_score: 8
kg_transferability_score: 7
verification: "L2_VERIFIED"
---

# SALME AI-Assisted Court Document Analysis (Estonia)

**Origin**: Estonia  •  **Year**: 2019  •  **Sector**: Justice & Rule of Law

## Problem solved

Estonian courts faced backlogs of complex commercial and civil cases requiring judges to manually review large volumes of documents including contracts, financial statements, and expert opinions. Judges spent 40-60% of their time on document review rather than substantive legal reasoning. SALME (System for Automated Legal and Managerial E-work) was piloted to automate document classification, extract key legal facts, and generate case summaries to reduce judge preparation time.

## Architecture

NLP pipeline built on Estonian legal corpus: document ingestion (PDF/Word), legal entity extraction (parties, dates, claims, amounts), semantic search across case law database, draft summary generation. Deployed on Ministry of Justice cloud infrastructure. Integration with Riigi Teataja (state legal gazette) and court information system (KOTIS). Human-in-the-loop: judges review AI summaries, corrections feed into retraining. Vendor: local Estonian AI company with Ministry co-development. Model: fine-tuned BERT-class for Estonian legal language.

## UZ transferability (8/10)

This is the reference case for UZ УП-140 'Digital Court / AI in Courts' programme. UZ court backlog is severe — Supreme Court handles 200,000+ cases annually. Russian-language legal corpus exists (UZ court decisions published on sud.uz). Key: UZ needs to develop Uzbek-language legal NLP capability alongside Russian. Political mandate is explicit (УП-140 signed 2025). Budget: $2-4M initial deployment is realistic under UZ government or EU/UNDP donor funding.

## KG transferability (7/10)

KG court system processes 150,000+ cases annually with chronic backlogs. Russian-language legal corpus exists. Kyrgyz-language NLP is underdeveloped but Russian-language tools immediately deployable. GIZ digital justice programme in KG provides donor pathway. Key concern: judicial independence questions — AI tools in KG courts require strong 'advisory only' governance to avoid executive branch pressure via AI-mediated court summaries.
