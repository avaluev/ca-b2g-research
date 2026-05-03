# INI-003 — Objection Handling

---

## Objection 1: "Soliton or Uzinfocom can build this cheaper — they know EPIGU's APIs"

**Response:** "Soliton and Uzinfocom excel at EPIGU systems integration — which is exactly why we want one of them as our IT Park local partner. The question is not whether they can integrate with EPIGU's backend; they absolutely can. The question is whether they can deliver LLM-grade bilingual natural language understanding that resolves 70%+ of citizen queries without a human agent. That requires a different capability stack. We bring the AI intelligence layer; they bring the integration expertise. Together, this is a stronger bid than either of us submitting alone."

---

## Objection 2: "ChatGPT already exists — why build our own?"

**Response:** "ChatGPT is a foreign API — every citizen query, every answer, every piece of data leaves Uzbekistan's sovereign boundary. УП-2024-132 specifically commits to AI-first services that respect data sovereignty. Bürokratt solved this for Estonia in 2022 using open-source components. Our adaptation runs the entire inference stack on UzCloud — no foreign API calls, full audit trail, MyID binding. The citizen experience is comparable to ChatGPT; the data architecture is compliant."

---

## Objection 3: "EPIGU's API documentation is incomplete — we will have integration problems"

**Response:** "We have already analyzed EPIGU's public API layer and designed a decoupling adapter that isolates the LLM stack from EPIGU's backend. Phase 1 deliberately covers only the 50 services with the best-documented APIs. We expand as API coverage improves. This phased approach means you see results in 8 months, not at the end of a 2-year integration project."

---

## Objection 4: "We are worried about the chatbot giving citizens wrong information"

**Response:** "This is the most important design constraint we addressed. The system uses a 'low-confidence handoff' rule: any query where intent confidence falls below threshold is automatically routed to a human PSA contact center agent. The AI handles the high-confidence queries (70%+ of volume); humans handle the rest. Citizens always have a clear escalation path. Audit logs record every interaction for quality review. We can demonstrate the confidence-threshold tuning live — you set the bar."

---

## Objection 5: "Russian language is declining in UZ government services — is bilingual still needed?"

**Response:** "EPIGU's own analytics show a significant share of queries arriving in Russian — particularly from urban users, older citizens, and members of the Russian-speaking minority community. The Uzbek-Russian bilingual requirement is explicitly written into both the decree mandate and the $2.8M tender TOR. Beyond current users, the bilingual capability is a quality signal: a model that handles both scripts well is more reliable on Uzbek queries too, because it has been trained on a richer linguistic corpus. We are not investing in Russian because we think it will grow — we are investing because real citizens are still using it today."
