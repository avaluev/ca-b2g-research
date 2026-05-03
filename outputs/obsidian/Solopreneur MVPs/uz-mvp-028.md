---
type: "solopreneur_mvp"
id: "uz-mvp-028"
country: "UZ"
category: "ai_tool"
sector: "Agriculture & Water"
confidence_tier: "B"
weighted_total: 7.0
linked_trend: "[[Trends/uz-trend-014-precision-agri-satellite|uz-trend-014-precision-agri-satellite]]"
linked_decree: "[[Decrees/uz-pp-2025-099|UZ-PP-2025-099]]"
linked_donor: "[[Donors/wb-uz-agri-digital|WB-UZ-AGRI-DIGITAL]]"
linked_initiative: ""
verification: "L2_VERIFIED"
tags:
  - "country/uz"
  - "category/ai_tool"
  - "tier/B"
  - "sector/agriculture-water"
---

# PestSpotterUZ

_Free tool: photo your crop leaf, get an Uzbek-language pest/disease ID and treatment plan_

## Pain point

Farmers misdiagnose pests, leading to wrong pesticide and crop loss. Extension agents are spread thin. agro.uz publishes weekly pest advisories but farmers want instant answers. Existing global apps (Plantix) lack Uzbek and have weak coverage of regional cotton/wheat pests.

**Evidence**: https://agro.uz/


**Target customer**: Smallholder farmers 30-55 with smartphones in Andijan, Bukhara, Samarkand growing cotton, wheat, vegetables, fruit


## Monetization

- **Model**: freemium
- **Price point**: $4.00
- **Year-1 target**: $10,000
- **Year-3 target**: $75,000


## MVR plan (squeeze_page)

- **Build time**: 10 days
- **Build cost**: $80

**Steps:**
- [ ] Fine-tune CLIP/DINOv2 on a small Uzbek pest dataset (~500 photos)
- [ ] Telegram bot intake + treatment recommendation in Uzbek + Russian
- [ ] Free 3 IDs/week, $4/mo unlimited + fertilizer schedule
- [ ] Affiliate to local agro-input dealers ($5/lead)
- [ ] Soft-launch in agro.uz forum and 3 farmer Telegram groups


## Validation

- **Signal target**: 400 IDs done + 20 paid in 60 days
- **Window**: 60 days
- **Channels**: agro.uz, Fergana farmer Telegram, agro-input dealer Telegram


**Tech stack**: CLIP/DINOv2 on HuggingFace, Supabase, Telegram Bot, Click micro-payment

**Capability required**: Russian + Uzbek-Latin, ML basics, agronomy partner for treatment validation


## Moat potential

Uzbek-specific pest dataset becomes a moat; possible licensing to Uzpaxtasanoat or WB digital agri program.

## Risks

- **Misdiagnosis liability** — _Mitigation_: Include 'consult agronomist' disclaimer; partner with one extension officer for review
- **Low data quality early on** — _Mitigation_: User feedback loop + bounty for correct labels
- **Affiliate revenue uncertain** — _Mitigation_: Sponsorship from one agro-input dealer (Uzkimyosanoat partner)


## Scoring (weighted total: **7.00**)

| Axis | Score |
|---|---|
| Demand clarity (30%) | 7/10 |
| Speed to MVR (15%) | 7/10 |
| Monetization path (20%) | 6/10 |
| Founder solo feasibility (20%) | 7/10 |
| Local market fit (15%) | 8/10 |

### Rationale

Painful problem, ML risk, affiliate-driven monetization.
