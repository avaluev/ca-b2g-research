# INI-002 — Objection Handling

---

## Objection 1: "We have an existing relationship with Havelsan (Turkey)"

**Why they raise it:** Havelsan has worked across Turkic markets and is sanctions-clean. The Supreme Court IT team may have already had technical conversations with Havelsan representatives.

**Response:** "Havelsan has strong Turkic-market presence and is absolutely a credible infrastructure vendor. What they lack is production-scale Uzbek-Russian bilingual legal NLP — their legal AI work has been in Turkish, not in the Uzbek-Cyrillic + Latin + Russian triple-script environment the Supreme Court's case archive requires. We can demonstrate the difference on a real corpus in 30 minutes. We are also open to a partnership model where Havelsan handles the Sud.uz integration layer and we deliver the NLP intelligence — reducing integration risk for the Supreme Court."

---

## Objection 2: "Data sovereignty — judicial records cannot go to foreign servers"

**Why they raise it:** Personal-data law UZ-LAW-2019-547 mandates data localization for judicial PII. This is a genuine legal constraint, not just political posturing.

**Response:** "We designed the architecture specifically for this requirement. The entire stack — LLM weights, inference layer, case corpus, audit trails — runs on UzCloud with no foreign API calls during inference. We have architectural documentation confirming zero data egress. The Estonia SALME deployment model is locally-hosted for the same reason; we inherit that design principle. We are happy to share the UzCloud deployment architecture before the tender submission so the IT team can validate it technically."

---

## Objection 3: "Local law UZ-LAW-2026-1125 imposes additional requirements we need to assess"

**Why they raise it:** The initiatives.json references this law. However, its existence is UNVERIFIED (Correction C-004).

**Response (internal instruction — do NOT mention the law's uncertain status):** "We have reviewed UZ-LAW-2019-547 (the verified 2019 personal-data law) and our deployment complies fully. If there are additional 2026 regulatory requirements the court's legal team has identified, we would welcome a technical session to review our compliance architecture against those specific provisions."

---

## Objection 4: "Your company does not have a UZ reference"

**Why they raise it:** Standard CIS procurement objection. Government buyers prefer local references or CIS references.

**Response:** "Our most relevant reference is Estonia — not because it is CIS, but because it is the exact same legal architecture: continental civil law, supreme court-level deployment, judge-facing workflow, data localization requirement. The Estonian e-Governance Academy will provide a written endorsement of the architecture for our submission. For CIS context, we can also reference Kazakhstan's e-Court modernization, which uses comparable NLP components. We are happy to arrange a direct call between your IT team and eGA Tallinn to validate the technology."

---

## Objection 5: "Budget constraints — $8M feels high for Phase 1"

**Why they raise it:** UZ-T-2026-002 at $8M is significant. Budget committee scrutiny is possible.

**Response:** "The $15M allocated by UP-140 makes the $8M Phase 1 very defensible from a budget perspective — it represents 53% of the total allocation for a system that directly affects 150,000+ cases per year. Our pilot scope starts at Tashkent City civil court (highest volume, clearest ROI) and demonstrates value before the $7M Phase 2 expansion. The UNDP-UZ-AI-COURTS co-financing ($2M) is additionally available to reduce the net state budget exposure. The comparable Estonia deployment cost was significantly higher on a per-case basis because Estonia paid first-mover costs; we transfer those learnings at no charge."
