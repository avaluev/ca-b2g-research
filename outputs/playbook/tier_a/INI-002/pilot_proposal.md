# INI-002 — Pilot Proposal
**Pilot:** Civil Court AI Document Analysis — Tashkent City Civil Court Phase 1
**Duration:** 12 months
**Pilot contract value:** $8,000,000 (RFP UZ-T-2026-002)

---

## Scope

**Phase 1A — Legal Corpus Preparation (Months 1–3)**
- Ingest and normalize the Supreme Court's Tashkent City civil-court archive (10,000+ cases minimum)
- Triple-script normalization: Uzbek-Cyrillic, Uzbek-Latin, Russian — consistent internal encoding
- PII redaction pipeline for training corpus (names, personal ID numbers, addresses)
- Statute citation extraction: build initial Uzbek legal NLP taxonomy from the court's case catalog

**Phase 1B — Judge-Facing Workflow (Months 2–9)**
- SALME-adapted case summarization: auto-generated judge-facing brief per case (200-300 words)
- Statute citation extractor: flags cited articles and links to Lex.uz reference
- Inconsistency detector: flags logical gaps in pleadings vs. cited statutes
- Decision template recommender: suggests templates from similar historical rulings
- Integration with Sud.uz via IT Park resident local partner (Soliton or equivalent)

**Phase 1C — Citizen Legal Aid Chatbot (UNDP co-financing component, Months 4–9)**
- Russian-Uzbek bilingual intake chatbot for civil procedure entry points
- Covers: filing a claim, responding to a claim, understanding a judgment, statute lookup
- Routes to court clerk human-handoff for complex queries
- MyID integration for identity-bound procedure tracking

---

## Success Metrics (Binding)

| Metric | Target |
|---|---|
| Judge document-review time reduction | ≥30% vs. baseline (averaged over 50 judges) |
| Citation extraction accuracy | ≥90% on Uzbek-Cyrillic + Latin + Russian legal text |
| Judge satisfaction score | ≥4.0 / 5.0 across Tashkent civil court bench |
| PII leakage incidents | Zero (UzCloud audit trail monthly review) |
| Case summary generation time | ≤15 seconds per case file |
| Citizen chatbot containment | ≥65% without clerk handoff |

---

## Deliverables

1. Triple-script legal NLP pipeline — normalized corpus + model weights
2. Judge-facing SALME-adapted case summarization module — deployed on UzCloud
3. Sud.uz integration layer — API adapter with IT Park local partner
4. Citizen legal aid chatbot (UNDP co-financing component)
5. Training dataset + evaluation protocol — open-licensed co-publication with NUU
6. Pilot evaluation report — validated by Supreme Court IT Department

---

## Price

$8,000,000 — covered by RFP UZ-T-2026-002 (UP-140 state budget)
$2,000,000 UNDP-UZ-AI-COURTS co-financing for citizen chatbot component
**Total pilot investment: $10,000,000**

---

## Conversion Path to Multi-Year Contract

- **Year 2:** Scale to all 14 oblast civil courts (UP-140 Phase 2) — estimated $7M extension
- **Year 2:** Adapt legal NLP stack for MoJ notary digitization (natural cross-sell)
- **Year 3:** Criminal procedure adaptation under UP-140 Phase 3
- **Long-term:** License Uzbek legal NLP stack to Prosecutor's Office, Anti-Monopoly Committee, Mahalla Foundation legal registry
- **3-year total revenue:** $22,000,000
