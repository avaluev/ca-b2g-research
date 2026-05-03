---
type: "doc"
title: "5+1 Analytical Lenses"
---
# The Five Lenses — Non-Obvious Analytical Models

Every research output passes through these five lenses. They distinguish this harness from generic "AI in Central Asia" research that produces useless platitudes.

## Lens 1: The Karimov-to-Mirziyoyev Inversion (Uzbekistan-specific)

**The pattern.** Pre-2016 Uzbekistan was institutionally frozen. Post-2016 Uzbekistan is in a once-in-a-generation institutional rewrite — every ministry, agency, and SOE has either been created, restructured, or rebranded since 2017.

**Operational implication.** Org charts published before 2020 are 80%+ stale. Most B2G consultancies still cite them. Russian-language Wikipedia is particularly unreliable here — Uzbek government structures change faster than volunteer editors update.

**Where the alpha is.**
- New agencies created post-2017 (Agency for Strategic Reforms, Agency for Cadastre, Public Services Agency, IT Park, Innovation Agency, etc.) tend to have:
  - Younger, often Western-educated leadership
  - Hungry leadership that wants visible wins
  - Less procurement orthodoxy
  - More tolerance for direct vendor engagement
- Renamed/restructured ministries (e.g. Ministry of Digital Technologies — formerly Ministry of Information Technologies and Communications) often have:
  - New scope they don't yet have vendors for
  - Fresh budget allocations tied to the renaming decree

**Application rule.** When an institution is mentioned, check its founding decree date. If post-2017, flag it as `karimov_inversion` lens-tagged and prioritize its leaders in the people-intelligence sweep.

## Lens 2: The Japarov Concentration (Kyrgyzstan-specific)

**The pattern.** Post-2021 Kyrgyzstan has consolidated executive power, abolished some ministries, restructured the Cabinet of Ministers (Кабинет Министров), and runs through the Presidential Administration as the real decision layer.

**Operational implication.** Smaller country = fewer gatekeepers = faster contracts but smaller budgets. The Ministry of Digital Development (Министерство цифрового развития) is the single highest-leverage target for AI vendors because it consolidates functions that used to span multiple agencies.

**Where the alpha is.**
- Abolished or merged entities: their staff still exist as named individuals but now operate inside the merged body — they retain expertise and network but their public roles are stale. Find them.
- The President's Office Digital Development Department often has more decision authority than the formal ministry on big-ticket items.
- The State Agency for Information Resources and Technologies under the President operates as a parallel implementation arm.

**Application rule.** When mapping KG institutions, always check both the formal ministry AND the parallel Presidential Administration unit. The latter often has the budget; the former has the public profile.

## Lens 3: The Decree Half-Life

**The pattern.** A presidential decree announcing an AI/digital strategy creates a 6–18 month implementation window where:
1. Budgets get allocated (months 0–3)
2. Working groups form, terms of reference drafted (months 1–6)
3. Procurement opens, RFPs publish (months 3–12)
4. Contracts award (months 6–18)

After month 18, implementation freezes until the next decree.

**Operational implication.** The window between decree signing and procurement publication is the highest-leverage window for vendor positioning. After RFPs publish, specs are usually written for an incumbent. Before implementation begins, the spec is open.

**Where the alpha is.** Decrees signed in the last 6–12 months that have NOT yet had their RFPs published. These are the "pre-procurement" windows where vendor input still shapes the spec.

**Application rule.** Every decree gets a `half_life_status` tag:
- `active_window`: signed within last 6 months, no procurement yet — HIGHEST PRIORITY
- `implementing`: 6–18 months old, procurement underway — bid on tenders
- `expired`: >18 months, no follow-up decree — backlog, low priority
- `amended`: superseded — check the amending decree
- `repealed`: dead — drop

## Lens 4: Donor Co-Financing (the hidden customer)

**The pattern.** 60–90% of "government" AI/digital budgets in UZ and KG are donor budgets channeled through ministries via PIUs (Project Implementation Units). The donor program manager (TTL at World Bank, project officer at ADB, etc.) is often the *real* customer — they wrote the TOR, they approve the procurement, they evaluate the bids.

**Operational implication.** Pitching only to the minister and ignoring the donor PM is the #1 reason foreign vendors fail in CA government markets. The donor PM has procurement orthodoxy (must use Bank rules), has prior vendor preferences (consultants they've worked with elsewhere), and has political cover the ministry doesn't.

**Where the alpha is.** Identifying the donor-government dyad for each program. The dyad is:
- The donor TTL/PM (named individual at WB/ADB/EU/etc.)
- The government counterpart (named individual at ministry, often a deputy minister or PIU director)
Both are stakeholders. Both must be sold.

**Application rule.** Every donor program record must have BOTH `ttl_pm_name` AND `government_counterpart_person_id`. Programs missing one are incomplete records. Initiatives funded via a donor program must include outreach to BOTH parties.

## Lens 5: The Diaspora Bridge

**The pattern.** Both UZ and KG have powerful tech diasporas (London, Dubai, Istanbul, Moscow, San Francisco, Seoul, Almaty) who:
- Often hold senior positions at major tech companies abroad
- Maintain personal relationships with current ministers (school friends, university classmates, family connections)
- Serve as informal advisors to digital ministries
- Are almost always uncredited co-architects of digital strategies
- Are often the source of the global precedents the ministries try to copy

**Operational implication.** Finding diaspora advisors on LinkedIn is the fastest unlock. They:
- Will accept LinkedIn connection requests (unlike ministers)
- Can introduce you to the named decision-maker with high warmth
- Often welcome partnership conversations (they want their home country to succeed)
- Sometimes formalize as "honorary advisors" or "presidential council members"

**Where the alpha is.** The diaspora-bridge research phase looks for:
- Uzbeks/Kyrgyz at FAANG, top consulting firms, top global banks, central banks abroad, top universities
- People with .uz / .kg roots who co-authored papers or talks with ministers
- People mentioned in ministerial speeches as "respected diaspora colleague"
- People on Presidential Advisory Councils (Совет старейшин, etc. — though these are formal; informal advisors are higher-leverage)

**Application rule.** Every people-intelligence sweep includes a dedicated diaspora-bridge subroutine. Diaspora advisors get `diaspora_advisor_flag: true` and are often higher-leverage targets than the formal officials they advise.

## Lens 6 (bonus): Russian/CIS Substitution Window

**The pattern.** Post-2022 sanctions accelerated a shift in CA government markets:
- Western vendors (US/EU) became risk-averse on the region
- Russian vendors faced sanctions exposure for their CA partners
- This created a pricing and positioning vacuum
- Filled increasingly by: Chinese vendors (Huawei, ZTE, Alibaba), Indian vendors (TCS, Infosys), Korean vendors (Samsung SDS, LG CNS), Turkish vendors (Havelsan, ASELSAN civilian arms), and importantly — local champions backed by national-friendly capital

**Operational implication.** A Russian-CIS-friendly delivery model (sntz.ai-style: Russian-language UX, local payment rails, no Western dependency) has outsized appeal IF positioned as "neither side" — neither US-aligned nor a Russian-sanctions-exposed vendor. This is your strategic position.

**Where the alpha is.** Initiatives where:
- Russian-language UX is mandatory or strongly preferred (justice, social services, internal admin)
- Data localization is required (impossible to deliver via Western SaaS)
- Speed-to-deploy matters more than blue-chip vendor brand
- The buyer wants "sovereign" alternatives to OpenAI/Google/Microsoft

**Application rule.** Every initiative gets a `russian_cis_fit` score (1–10) reflecting how well it matches your distribution moat. High scores get prioritized in the CRM "fast pipeline" view.

---

## How the lenses combine

The most valuable initiatives score high on multiple lenses simultaneously:

- **Karimov Inversion + Decree Half-Life Active**: a new UZ agency created in last 24 months with a fresh decree mandate AND budget — bluest of blue-water opportunities
- **Donor Co-Financed + Diaspora Bridge**: World Bank program with a diaspora advisor on the donor side AND the government side — warm intro to both
- **Russian/CIS Substitution + Defensibility**: government data sovereignty mandate + multi-year SLA potential — your highest-margin moat play

These combinations are flagged in the initiative-synthesizer output as "convergent windows."
