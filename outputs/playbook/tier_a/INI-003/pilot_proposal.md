# INI-003 — Pilot Proposal
**Pilot:** EPIGU AI Chatbot — Top 50 Services (Russian + Uzbek-Latin)
**Duration:** 8 months
**Pilot contract value:** $2,800,000 (RFP UZ-T-2026-005, verify tender is live)

---

## Scope

**Phase A — Service Taxonomy + NLP Training (Months 1–3)**
- Map EPIGU's top-50 services: intent taxonomy, required data fields, escalation triggers
- Train bilingual NLP model: Uzbek-Latin (primary), Russian (mandatory), Uzbek-Cyrillic (legacy queries)
- Build EPIGU API adapter layer decoupling LLM from EPIGU backend versioning
- Integrate MyID for identity-bound personalized queries (e.g., "what is the status of my application?")

**Phase B — Production Deployment (Months 3–8)**
- Deploy LLM chatbot on EPIGU.uz and PSA mobile app
- Human-handoff: automatic routing to PSA contact center when intent confidence < threshold
- Audit-trail logging on UzCloud: every query, every answer, every handoff timestamped
- Monitoring dashboard: real-time containment rate, language distribution, handoff reasons

---

## Success Metrics (Binding)

| Metric | Target |
|---|---|
| Intent classification accuracy | ≥85% across top-50 services (Russian + Uzbek) |
| Query containment without handoff | ≥70% |
| Average response time | ≤3 seconds |
| MyID-bound personalization | Operational for ≥10 services |
| User satisfaction (pilot survey) | ≥4.0 / 5.0 |

---

## Deliverables

1. Bilingual EPIGU NLP model — weights, intent taxonomy, evaluation dataset
2. Production chatbot — deployed on EPIGU.uz and mobile app
3. EPIGU API adapter layer — decoupled from backend versioning
4. Operations manual — for PSA product team to manage and update
5. Pilot evaluation report — 8-month metrics vs. baseline rule-based bot

---

## Price

$2,800,000 — state budget (RFP UZ-T-2026-005)
WB P179108 potential co-financing: inclusion-metrics component (scope to be agreed with WB TTL)

---

## Scale-up Path

- **Phase 2 (2027):** Expand to full 350-service EPIGU catalog — anticipated under forthcoming tender
- **Phase 3 (2028):** 1,000+ services under UZ-TF-2026-004 ($9.5M) agentic expansion
- **Cross-sell:** Same NLP stack licenses to MoJ notary services, Mahalla social registry (INI-012), Tax Committee citizen portal
- **3-year total revenue:** $18,000,000
