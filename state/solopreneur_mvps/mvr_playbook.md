# MVR Playbook — Which Vehicle for Which Idea Category

> Operator's reference for matching the 8 HubSpot MVR vehicles to Central Asia idea categories. Built from the 200 MVPs in `state/solopreneur_mvps/`. Validated against the trends, decrees, and donor-program data in `state/knowledge_graph.json`.

## TL;DR — vehicle by category

| Idea Category | Best Vehicle | Second Choice | Why |
|---|---|---|---|
| Citizen-service helper (EPIGU/Tunduk) | **wizard_of_oz** | demo_video | Pay-per-use model; trust built one customer at a time |
| SaaS for SMEs (tax, payroll, e-faktura) | **landing_page** | squeeze_page | Subscription billing requires a sales page |
| Demand-validation for paid product | **squeeze_page** | landing_page | One-question email gate beats waitlist |
| AI tool with viral hook | **demo_video** | free_tool | Loom/Twitter-native shows the magic in 60s |
| Free utility (calculators, alerts) | **free_tool** | landing_page | Zero-friction adoption, monetize later |
| Aggregator (banks, scholarships, doctors) | **directory** | content | Structured listings sponsored by featured spots |
| Premium service (legal, advisory, education) | **wizard_of_oz** | manifesto | Manual fulfillment proves willingness to pay |
| Productized service (booking, errands) | **ad_booking** | wizard_of_oz | Direct booking via Telegram + Click/Mbank |
| Brand / authority play | **manifesto** | content | Long-form essay builds audience for newsletter |

---

## Vehicle 1 — landing_page

### When to use
- You are selling a subscription SaaS that will eventually require a $9–$49/mo charge.
- Customer needs to understand value before signing up (e.g., TenderRadar UZ, VATcheckUZ, PharmacyShelfUZ).
- You have the technical skills to build a small interactive demo.

### Day 1–7 build sequence
1. Domain + Carrd or Vercel + Next.js
2. Headline + subhead + 3 benefits + 1 testimonial (or "joining now" social proof)
3. Email capture as primary CTA; trial signup as secondary
4. One real demo screenshot or 30-second Loom embed
5. Click/Mbank/Stripe billing page with 14-day free trial
6. First 5 founder-founder customers via cold Telegram in IT Park / High Tech Park

### Local CA twist
- Tashkent and Bishkek SMEs trust badges from TBC, Anorbank, Mbank, Optima — show "Powered by Click" or "Mbank-integrated" prominently.
- Russian + Uzbek-Latin or Kyrgyz versions of the same page double conversion in oblast capitals.

### Examples in the dataset
- uz-mvp-004 TenderRadar UZ
- uz-mvp-014 VATcheckUZ
- uz-mvp-036 PharmacyShelfUZ
- kg-mvp-003 TenderRadarKG
- kg-mvp-039 PharmacyShelfKG

---

## Vehicle 2 — squeeze_page

### When to use
- You want pure email capture in exchange for a high-value lead magnet.
- You have a downloadable checklist, calculator output, or PDF.
- Customer pain is acute and time-bounded (permits, scholarships, deadlines).

### Day 1–7 build sequence
1. Carrd page with 3-question intake form
2. Mailerlite or Buttondown email automation
3. Auto-emailed PDF or Russian/Uzbek/Kyrgyz checklist
4. Upsell: $9–$30 paid 30-min call as the first paid offer
5. $50–$100 Instagram or Facebook ad targeting Tashkent/Bishkek 25–40

### Local CA twist
- Add a Telegram alternative ("get it on Telegram instead of email") — Telegram opens at 2–3× email rates.
- Lead magnets in three languages (RU + UZ-Latin + EN, or RU + KY + EN) signal credibility.

### Examples in the dataset
- uz-mvp-007 PermitPathfinder
- uz-mvp-008 EPIGUStatusBot
- uz-mvp-011 GovHotlineRouter
- kg-mvp-007 PermitFinderKG
- kg-mvp-012 GovHotlineRouterKG

---

## Vehicle 3 — demo_video

### When to use
- The product magic is visual or interactive (AI demos, screen-share walkthroughs).
- Your audience watches TikTok / YouTube Shorts / Reels.
- You have a clear "before/after" payoff in 60 seconds.

### Day 1–7 build sequence
1. CapCut or Loom for 90-second video
2. Russian voiceover + Uzbek-Latin or Kyrgyz subtitles
3. WhatsApp Business "DM us for help" CTA
4. YouTube + TikTok + Instagram Reels triple-post
5. Affiliate funnel to bank account or accounting partner ($5–$10/lead)

### Local CA twist
- TikTok UZ and TikTok KG audiences over-index on financial-literacy and government-form content. Cross-promote with one mid-size existing creator.
- ICT Week (UZ) and High Tech Park (KG) panels work as authority-stack — record at the venue, post the same week.

### Examples in the dataset
- uz-mvp-003 MyID Onboarding Coach
- uz-mvp-010 DigitalSignWalker
- uz-mvp-022 AzbukaGosUslug
- uz-mvp-057 MigrantBankSetup
- kg-mvp-022 CitizenServiceUZK (KG)
- kg-mvp-040 MedReminderKG
- kg-mvp-059 MigrantBankSetupKG
- kg-mvp-067 AcademicTranslatorKG

---

## Vehicle 4 — free_tool

### When to use
- You can solve a single micro-problem with a no-login Telegram bot or web utility.
- Underlying data already exists publicly (lex.uz, openbudget.uz, ECMWF weather, USGS earthquakes).
- Monetization is freemium (premium tier $2–$10/mo) or affiliate.

### Day 1–7 build sequence
1. Pick the data source; verify open-access terms
2. Telegram Bot API + Supabase + GPT-4o-mini classification
3. Output in Russian + Uzbek-Latin / Kyrgyz
4. Click or Mbank micro-payment for premium tier
5. Soft-launch in 3 specific community Telegrams (no spamming)

### Local CA twist
- Voluntary tipping via Click QR / Mbank QR converts at 1–3% of weekly active users — modest but real.
- Always include a "report data error" button — fixes the largest reputational risk for civic tools.

### Examples in the dataset
- uz-mvp-001 EPIGU Companion
- uz-mvp-005 MahallaMonitor
- uz-mvp-006 UZBudgetView
- uz-mvp-051 TaxScannerUZ
- uz-mvp-087 WeatherFarmAlertUZ
- kg-mvp-001 TundukExplainer
- kg-mvp-026 LivestockTrackKG (originally ai_tool, mapped to free_tool)
- kg-mvp-051 TaxScannerKG
- kg-mvp-086 AirQualityKG

---

## Vehicle 5 — directory

### When to use
- The category has 50–500 listings (gyms, doctors, pharmacies, scholarships, tenders).
- Customers shop comparatively before deciding (medical, tutoring, financial).
- Supply side will pay for featured listings ($15–$80/mo).

### Day 1–7 build sequence
1. Carrd or Notion CMS for the 30–50 highest-value listings
2. Telegram bot for mobile-first browsing + alerts
3. Free for consumers; charge supply side $15–$80/mo for featured slots
4. Affiliate revenue from related transactions (booking, account opening)
5. SEO target: bilingual keywords + reviews

### Local CA twist
- Visit and photograph venues/businesses yourself for the first 30. Authenticity is the moat — competitors who scrape databases have stale data.
- "Verified" badges (credentials checked, photos current) command 2–3× the listing fee.

### Examples in the dataset
- uz-mvp-012 EPIGUForBusiness
- uz-mvp-019 GovHireUZ
- uz-mvp-029 DairyMarketUZ
- uz-mvp-039 DocLookupUZ
- uz-mvp-079 SamarkandRestoFinder
- kg-mvp-019 GovHireKG
- kg-mvp-030 DairyMarketKG
- kg-mvp-044 DocLookupKG
- kg-mvp-079 BishkekRestoFinder

---

## Vehicle 6 — wizard_of_oz

### When to use
- The pain is acute and customers will pay $3–$200 for an outcome.
- Automation is hard but human fulfillment is feasible.
- You want to learn customer language + objections before building software.

### Day 1–7 build sequence
1. Telegram bot intake (photo + voice or photo + form)
2. Notion fulfillment dashboard (you + 1 part-time student or paralegal)
3. Click/Mbank payment, ideally pre-pay before fulfillment
4. Define a 2–24h SLA and stick to it
5. Cap volume to 30 customers/week initially — quality first

### Local CA twist
- One part-time AUCA / Westminster Tashkent / NUUz student at $200–$300/mo can handle 50–80 fulfillment events per week.
- Mahalla aksakal partnerships add credibility and field reach. Pay an honorarium ($30–$50/month) for cooperation.

### Examples in the dataset
- uz-mvp-002 FormFiller UZ
- uz-mvp-017 OneStopComplaint
- uz-mvp-025 OneTouchPensionUZ
- uz-mvp-034 VetCallUZ
- uz-mvp-053 MigrantWageGuard
- uz-mvp-066 SchoolEnrollerUZ
- kg-mvp-002 FormFillerKG
- kg-mvp-014 OneStopComplaintKG
- kg-mvp-016 OneTouchPensionKG
- kg-mvp-027 VetCallKG
- kg-mvp-038 MountainTelemed
- kg-mvp-053 MigrantWageGuardKG

---

## Vehicle 7 — ad_booking

### When to use
- You sell a productized service (one defined deliverable, fixed price).
- Customer has urgent cash-flow trigger (passport appointment, fine alert, taxi rate).
- You can drive cold traffic via Facebook/Instagram/TikTok ads at $1–$3 CPL.

### Day 1–7 build sequence
1. Single-page offer with one CTA + Telegram booking
2. $80–$150 Facebook + Instagram ad spend in pilot week
3. Click/Mbank pre-payment locked into booking flow
4. Calendar (Calendly + Telegram) confirms within 4h
5. SMS or WhatsApp follow-up + review request after fulfillment

### Local CA twist
- Russian-language ad copy with Uzbek/Kyrgyz subtitles outperforms single-language by 2×.
- Free first call ("get answers in 15 min, no payment") improves conversion 3–5×.

### Examples in the dataset
- uz-mvp-013 PassportAppointmentBuddy
- uz-mvp-080 TashkentTaxiRateCheck
- uz-mvp-081 TashkentParkingMap
- uz-mvp-082 BorderWaitUZ
- uz-mvp-085 BusScheduleUZ
- kg-mvp-080 BishkekTaxiRateCheck
- kg-mvp-081 BishkekParkingMap
- kg-mvp-082 BorderWaitKG
- kg-mvp-085 BusScheduleKG
- kg-mvp-086 AirQualityKG

---

## Vehicle 8 — manifesto

### When to use
- You want to build a long-term content brand (newsletter, audience, authority).
- Your topic is policy, investment, AI, or research-grade.
- You have writing capability + a strong opinion.

### Day 1–7 build sequence
1. Substack or self-hosted Ghost/Beehiiv
2. Founder thesis: 3,000–5,000 word manifesto explaining "why now"
3. Cross-post on LinkedIn + Habr UZ/KG + Hacker News + Twitter X
4. Free first 5 issues, then $12–$99/mo paywall
5. Quarterly 1:1 briefing call as premium-tier upsell

### Local CA twist
- Diaspora audiences (LinkedIn "Uzbeks Abroad" / "Kyrgyz Abroad" groups) are ready-built premium audiences.
- Eurasianet, Spot.uz, Kaktus.media editors will feature you if your manifesto cites primary sources rigorously — write for cross-promotion.

### Examples in the dataset
- uz-mvp-018 PolicyDigestUZ
- uz-mvp-024 ProcurementCoach
- uz-mvp-050 ParentingExpertUZ
- uz-mvp-097 OutsourceToUZ
- uz-mvp-098 DiasporaInvestorUZ
- uz-mvp-100 WhyUzbekistan
- kg-mvp-008 KGProcurementCoach
- kg-mvp-018 PolicyDigestKG
- kg-mvp-054 DigitalSomGuide
- kg-mvp-094 OutsourceToKG
- kg-mvp-095 DiasporaInvestorKG
- kg-mvp-097 WhyKyrgyzstan

---

## Sequencing — what to launch first as a solo founder

### Profile A — coding founder (no capital, 4 weeks)
1. Week 1: free_tool MVP (e.g., TaxScannerUZ/KG) — gets first 200 free users
2. Week 2: directory or wizard_of_oz layer for monetization
3. Week 3: landing_page conversion to subscription
4. Week 4: paid ad layer ($100 budget) to validate CAC

### Profile B — non-technical operator (small capital $300–500)
1. Week 1: wizard_of_oz (FormFiller / OneTouchPension) — manual fulfillment
2. Week 2: $80 Instagram ad + Telegram bot intake
3. Week 3: hire 1 part-time student fulfillment helper
4. Week 4: productize template library

### Profile C — content creator / writer
1. Week 1: manifesto (PolicyDigest / DiasporaInvestor)
2. Week 2: cross-post LinkedIn + Habr + Twitter X
3. Week 3: paid Substack at $12/mo, free first 5 issues
4. Week 4: 1:1 briefing call upsell at $99/mo

### Profile D — diaspora-bridge founder (English fluent, abroad)
1. Week 1: GovDocTranslator / KyrgyzDecreeSummary — daily decree feed in EN/RU/UZ-Latin or KY
2. Week 2: WhyUzbekistan or WhyKyrgyzstan manifesto, paid Substack
3. Week 3: Diaspora investor club ($89/mo)
4. Week 4: Outsource-to-UZ or -KG talent directory

---

## Cross-cutting principles (CA specifics)

1. **Local payments first.** Never launch with Stripe-only. Click/Payme (UZ) or Mbank/Optima (KG) at minimum, alongside any international acquirer.
2. **Russian + local.** Always two languages minimum; English is optional except for diaspora-bridge plays.
3. **Telegram-native.** Even SaaS products need a Telegram presence. Notifications, support, community.
4. **Donor partnerships are the unfair advantage.** Half the Tier-A MVPs reference an active donor program. Pitch UNDP, EU-GIZ, AKDN, World Bank, ADB, UNICEF, KOICA early.
5. **Data is the moat.** Every Wizard-of-Oz must log structured data from day 1. After 3–6 months, the dataset becomes a defensible product.

---

## Cross-references

- See `state/trends/` for the underlying market signals.
- See `state/decrees/` for decree-half-life timing windows.
- See `state/donor_programs/` for program officer contact pathways.
- See `state/initiatives/` for the parallel B2G enterprise plays (where solopreneur MVPs may eventually feed in as feeder products).
