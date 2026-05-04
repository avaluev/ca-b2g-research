# 01 — Reference Benchmark: Padel vs B2G

**Auditor role**: Reference Benchmarker  
**Date**: 2026-05-03  
**Reference site**: https://avaluev.github.io/padel-market-analysis/  
**Audit site**: https://avaluev.github.io/ca-b2g-research/

---

## Executive Summary

- The B2G site has dramatically more raw data (100 initiatives, 200 MVPs, 105 institutions, 117 people, 100 decrees, 49 donors, 50 tenders) but renders it as tables without editorial narrative — the reference site turns thinner data into a richer intellectual product through disciplined prose structure and a staged-argument architecture.
- The reference site uses inline confidence scores, model routing tables, and a grep-verifiable audit trail that transforms methodology claims into *checkable assertions*; the B2G site makes the same claims in prose without the same machine-verifiable anchors.
- Typography, heading cadence, and the "wow" signal — question-form H3s, numbered pipeline stages, blockquoted thesis statements, monospace schema references — are present in the reference and absent in the B2G site across every deep page sampled.

---

## Dimension Scores (1 = poor, 10 = excellent)

| Dimension | Reference (Padel) | Audit (B2G) | Delta | Notes |
|---|---|---|---|---|
| Information density | 7 | 9 | +2 B2G | B2G has far more raw data points and entity types |
| Voice quality | 9 | 6 | −3 | Padel: terse, audit-ready, active imperative. B2G: competent but generic third-person |
| Citation visibility | 9 | 7 | −2 | Padel: inline hyperlinked URL per claim, confidence scores, archived HTTP 200 checks. B2G: cited but less granular |
| Navigation depth | 8 | 9 | +1 B2G | B2G has 13 nav sections vs padel's 9; B2G wins on breadth |
| Typography hierarchy | 9 | 6 | −3 | Padel: numbered stages, monospace schema refs, blockquoted theses. B2G: flat heading style |
| Mobile friendliness signals | 8 | 7 | −1 | Padel documents 5-device audit with TTFB/FCP/LCP/CLS. B2G has mobile-responsive nav but no audited evidence |
| Evidence transparency | 9 | 8 | −1 | B2G's Honesty page is exceptional; padel edges it with grep-verifiable model provenance |
| Reproducibility framing | 9 | 7 | −2 | Padel: Makefile, `make audit`, HTTP 200 archival, explicit Python subprocess enforcement. B2G: described in prose but not gate-enforced in rendered output |
| Trust signals | 9 | 8 | −1 | Both strong; padel adds "declared but NOT invoked" model section and hiring-signal framing |
| "Wow" factor | 9 | 6 | −3 | Padel: moat kill verdicts, confidence thresholds, model routing table, stage labeling. B2G: data volume impresses, presentation does not |

**Overall**: Padel wins 8 of 10 dimensions on presentation quality. B2G leads on raw data volume and nav breadth.

---

## Reference Does This — B2G Does Not

1. **Question-form H3 headings.** Padel uses "How to read this map?" and interrogative H3s throughout. Every B2G deep page uses declarative headings. Question-form pulls AI citation and signals direct-answer content.

2. **Numbered pipeline stages with dot notation.** "Stage 1 · Plan", "Stage 2 · Fan-out" etc. gives methodology pages scannable structure. B2G methodology is prose paragraphs without stage labeling.

3. **Inline confidence scores.** Padel attaches "Confidence: 0.35" to individual soft-signal claims. B2G expresses uncertainty only in the Honesty page, not inline per claim.

4. **Model routing table (Stage × Model × Reason).** Padel's provenance page shows a structured table of which model handled which pipeline stage and why. B2G's provenance page lists models but not the per-artifact routing logic.

5. **"Declared but NOT invoked" transparency section.** Padel explicitly documents tools available but unused, preventing marketing conflation. B2G has no equivalent negative-space disclosure.

6. **Blockquoted thesis statements.** Padel uses `>` blockquotes to elevate the single most important idea per section. B2G has no typographic treatment that foregrounds key claims.

7. **Monospace schema field references inline.** `` `_source` ``, `` `calculation_method == "python_subprocess_executed"`` appear in prose as machine-readable anchors. B2G uses internal codes (PP-320, UZ-T-2026-003) but not inline schema paths.

8. **`make audit` / Makefile reproducibility entry point.** Padel has a single command to re-run the entire verification harness locally. B2G has scripts but no documented single-command re-run for the *rendered* site.

9. **Five-device mobile audit with captured metrics.** Padel documents iPhone 13, Pixel 7, iPhone SE, iPad Mini, and desktop 1280 with TTFB, FCP, LCP, CLS values. B2G has no equivalent audited performance record.

10. **Cross-file claim traceability to JSON.** Every padel claim traces to a specific path (`evidence/<run-id>/04_peer_cards/playtomic.json`). B2G's 402 references point to URLs but not to a local structured-data graph that can be diffed.

11. **Moat verdict cadence.** Padel publishes "kill verdicts" on competitive moats — forced negative conclusions per section. B2G's Tier classifications are positive-biased with no equivalent kill discipline.

12. **"Hiring signal" framing of transparency.** Padel reframes methodology openness as competence evidence for a reader who might hire the author. B2G's transparency is framed as research hygiene, missing the personal authority angle.

---

## B2G Does This — Reference Does Not

1. **Dual-country comparative atlas.** No padel equivalent of side-by-side UZ/KG decree corpora (56 + 44 entries) with cross-referenced legal status.

2. **Five dedicated transparency pages.** Honesty, Provenance, Lenses, Scoring, and Methodology as separate rendered pages. Padel combines these into fewer pages.

3. **Quantified self-correction.** B2G's Honesty page admits "four of approximately twelve operationally-critical identities are wrong" with severity tags and remediation roadmap. This level of numeric self-audit has no padel equivalent.

4. **People intelligence layer.** 117 named decision-makers with verification status (including explicit "linkedin_status: not_found" discipline). Padel has no person-level data.

5. **Solo MVP corpus.** 200 solopreneur-viable MVP concepts as a separate deliverable. Padel has no equivalent second-order product layer.

6. **Live tender / procurement tracking.** 50 live tenders with procurement pathway classification. Padel is market research, not procurement intelligence.

---

## Top 10 Copyable Patterns from Reference

| # | Pattern | Exact Implementation |
|---|---|---|
| 1 | Numbered stage labels | H3: "Stage N · Name" for every methodology step |
| 2 | Question-form H3s | At least one interrogative H3 per major section ("What does this mean for pricing?") |
| 3 | Blockquoted thesis | Single `>` blockquote per page elevating the headline claim |
| 4 | Inline confidence | Append "(Confidence: 0.N)" after any soft-signal claim |
| 5 | Model routing table | Three-column table: Stage / Model / Reason on Provenance page |
| 6 | Negative-space disclosure | "Declared but not invoked" section listing available tools that saw zero usage |
| 7 | Monospace schema anchors | Backtick-wrap field names and file paths appearing in prose |
| 8 | Moat/kill verdict section | Per tier: force at least one explicit demotion verdict with reasoning |
| 9 | Single-command reproducibility | `make audit` or equivalent with output piped to a log file, linked from Methodology |
| 10 | Device audit record | Publish TTFB/FCP/LCP/CLS for 3+ device profiles; link from Methodology |

---

## Prioritized Remediation List

### P0 — Blocks trust parity with reference

- **P0-A**: Add inline confidence scores to every soft-signal or inferred claim across initiative, people, and donor pages. Format: `(Confidence: 0.N, basis: desk-research|verified|inferred)`.
- **P0-B**: Restructure Methodology page with numbered Stage N · Name headings. Current prose is descriptive; it needs scannable stage labels.
- **P0-C**: Add a model routing table to Provenance — Stage × Model × Artifact produced. Currently lists models but not the per-artifact assignment.

### P1 — Structural quality gap

- **P1-A**: Convert at least one H3 per deep page to question form. Start with Scoring ("What does a Tier-A score mean?"), Lenses ("Which lens predicts deal velocity?"), Initiatives ("How were Tier-A thresholds set?").
- **P1-B**: Add a blockquoted thesis statement (single `>` callout) to every deep page's lead section.
- **P1-C**: Add "Declared but NOT invoked" section to Provenance — document tools available in the harness that generated zero output artifacts.
- **P1-D**: Add a kill-verdict discipline to initiative tier descriptions — for each tier, require at least one documented reason a candidate was *demoted*, not just why top entries qualify.

### P2 — Polish and authority signals

- **P2-A**: Wrap all schema field names and file paths in monospace within prose (e.g., `verification_status`, `state/initiatives/output.json`).
- **P2-B**: Publish a 3-device performance audit (mobile, tablet, desktop) with FCP and LCP values on the Methodology page.
- **P2-C**: Add `make audit` or equivalent single-command re-run entry point to README and Methodology, linking to the rendered output log.
- **P2-D**: Reframe the Honesty page's closing paragraph as a competence signal — the transparency is currently defensive; reposition it as "this is what rigorous research looks like."
