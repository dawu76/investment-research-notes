---
title: "Akamai Technologies ($AKAM): Investment Memo"
created: 2026-10-15
updated: 2026-10-22
type: entity
tags: [company, thesis, valuation, risk, cybersecurity, cloud, infrastructure]
sources: [investing-fundamentals/company-analyses/akam-1-document-sources.md, investing-fundamentals/company-analyses/akam-2-equity-report.md, investing-fundamentals/company-analyses/reports/akam-morgan-stanley-20260925.pdf, investing-fundamentals/company-analyses/reports/akam-morningstar-20260925.pdf, https://www.sec.gov/Archives/edgar/data/0001086222/000108622226000086/akam-20260630.htm, https://www.sec.gov/Archives/edgar/data/0001086222/000119312526228949/d123781dex101.htm]
confidence: medium
contested: false
---

# Akamai Technologies ($AKAM): Investment Memo

**Price:** $90.65 (intraday October 15, 2026; the close was $92.32), down 45% from the $165.45 high of May 13, 2026, and 8% on October 14 alone with no company news. That day CoreWeave fell ~16% after a scare in its bonds, and AI-infrastructure stocks fell with it (see [[docn-3-investment-memo]], October 16 update). **Market cap** ~$13.0B; **EV** ~$16.1B excluding leases ($7.64B convert principal less $4.62B cash at June 30). **Next catalyst:** Q3 2026 results on November 5.
**Focus:** what the price assumes, the risks, and what a bear case looks like. Business background: [[akam-2-equity-report]].
**Updated October 15, 2026** with the Morgan Stanley (September 29) and Morningstar (September 25) reports in `reports/`, both written after the Anthropic deal at prices of $108.99-113.94. The CFRA file in that folder holds no report text (a saved browser PDF viewer) and is not used. This memo's bear case disagrees with both reports on how much margin of safety the compute contracts carry.

## Update, October 16, 2026: sell-off, a $65 reverse valuation, and liquidity

### The week of October 12-16

AKAM fell **17.7%** ($106.95 on October 9 to ~$88.06 intraday October 16; Yahoo Finance closes). There was no company news, guidance change or new downgrade. Its down days matched the neocloud sell-off described in [[docn-3-investment-memo]]:

| | Oct 12 | Oct 13 | Oct 14 | Oct 15 | Oct 16 | Week |
|---|---|---|---|---|---|---|
| AKAM | -5.0% | -1.7% | -8.2% | +0.7% | -4.6% | -17.7% |
| DOCN | -2.5% | -2.4% | -14.8% | +0.2% | -11.0% | -27.8% |
| CoreWeave | -2.2% | -3.1% | -15.5% | +5.9% | -11.1% | -24.6% |
| Cloudflare | -2.8% | -0.9% | -6.7% | -2.4% | -7.7% | -19.1% |

The business did not change. The market repriced the two risks this memo ranks highest:
* **Funding cost for AI compute.** CoreWeave's bonds hit 15% yields (October 14 and 16), and CDS spreads on tech bonds reached record highs (October 15). Akamai needs ~$2-3B of new money by end-2027, and the deal's ~3-point IRR cushion over a 7.6% cost of capital (Section 2) shrinks if that cost rises.
* **Anthropic as counterparty.** Reuters (October 1), citing Anthropic's confidential IPO prospectus, reported at least $518B of infrastructure commitments over about a decade, ~80% non-cancellable or owed regardless of usage. That compares with a revenue run-rate of ~$47B (May 2026) and an operating loss above $8B in 2025. Akamai's $11.6B is ~2% of those commitments, yet ~90% of Akamai's compute bookings. Anthropic reportedly signed another multiyear deal with IREN on October 12. Nscale's S-1 (September 18) shows Anthropic can cancel late tranches without liability. Akamai has not disclosed whether its contract has similar terms.
* Gartner's forecast (October 15) that over 80% of neoclouds will not survive independently by 2030, and rates (10-year above 5%, Warsh leaving a hike open), weighed on the whole group. Cloudflare, which has no compute debt, fell 19%.

HSBC has a Hold rating and a $123 target (cut from Buy and $171), citing compute margins, EPS growth of 8.5% a year over 2026-28, and capex. Its date is unconfirmed, so it is not treated as this week's driver.

At ~$88 the stock is ~12.8x MS 2027 EPS, 17% below this memo's base case, 47% above the bear case, and below the Anthropic warrant strike ($111.33).

### What a $65 price would assume (this update's arithmetic)

| Measure | At $65 | At ~$88 |
|---|---|---|
| Market cap / EV ex-leases (June 30 net debt ~$3.0B) | ~$9.3B / ~$12.4B | ~$12.7B / ~$15.7B |
| EV / 2026 revenue ($4.49B) | ~2.8x | ~3.5x |
| P/E: MS 2026 / 2027 / 2028 | ~9.7x / 9.4x / 8.6x | ~13.1x / 12.8x / 11.7x |
| P/E: Morningstar 2028 ($10.08) | ~6.4x | ~8.7x |
| Price / Morningstar fair value ($150) | 0.43x (below its $75 five-star level) | 0.59x |

Three readings fit $65:
* **This memo's bear case:** Anthropic ramp late or renegotiated (2028 compute revenue ~$1.2B), security +5%, delivery -8%, 22% margin. 2028 EPS ~$6.03 at ~10.8x.
* **Compute worth zero:** the core business earns roughly $6.70 a share (2026 revenue excluding compute, ~$4.07B, at the FY2025 ~30% margin; rough). $65 is ~9.7x that. Compute earns about its cost of capital (IRR ~7.6%), which matches the one-year-delay (~5.7%) and higher-cost (~7.9%) stress cases in Section 2.
* **A fair core with compute losing money:** core at 12x (~$80 a share) and compute destroying ~$2.2B (~$15 a share). That fits a deal IRR near 0-5%, as with 15-30% less Anthropic revenue.

$65 would not imply the core business breaking or Anthropic walking away (the deep bear case, ~$40). From $65 this memo's cases run -38% (deep bear), -8% (bear), +63% (base), +65% (weighted) and +172% (bull). That is a better risk-reward than DOCN at the same price (-25% to bear, +49% to base). How the stock gets there matters. Sector drift with the plan intact would make it undervalued. Company news would require revising the weights: Anthropic cancellation rights for late delivery, financing at a high coupon or secured on compute assets, security growth below 7%, or a FY2027 EPS guide below ~$6.50.

### Liquidity and the revolver covenant

**Funding through the September 2027 maturity (this update's arithmetic):**

| | Amount |
|---|---|
| Cash and marketable securities, June 30, 2026 | $4.62B |
| Year-end 2026 cash after H2 capex (incl. ~$1.7B Anthropic in Q4) and LayerX | ~$1.5-2.2B |
| 2027 free cash flow (Morningstar) | -$2.29B |
| 2027 notes due September 1, 2027 | -$1.15B |
| Usable year-end cash, keeping ~$0.5B to operate (assumption) | ~$1.0-1.7B |
| Gap before the revolver | ~$1.7-2.4B |
| Revolver ($1.0B committed) + uncommitted secured line ($150M) | up to ~$1.15B |
| Gap after the revolver | ~$0.6-1.3B |

**The covenant.** The 2022 credit agreement (amended May 18, 2026) caps Consolidated Total Indebtedness ÷ Consolidated EBITDA at **4.75x for the June and September 2026 quarters, then 3.50x from December 31, 2026**. A 4.00x step-up is allowed for four quarters after an acquisition over $100M; LayerX (~$205M) may qualify. Indebtedness is gross: the definition includes notes and does not subtract cash. EBITDA adds back stock compensation and one-off charges.
* **Estimated position:** debt of $7.64B against EBITDA of ~$1.8-1.9B (FY2025 ~$1.81B at a 43% margin; 2026 margins lower) is about **4.0-4.2x** (this update's estimate; the company's covenant EBITDA is not disclosed).
* **To reach 3.50x**, debt has to fall to ~$6.3-6.6B or EBITDA rise to ~$2.2B. In practice: retire the 2027 notes early (cash needed in the same quarter as ~$1.7B of Anthropic capex), use the 4.00x step-up with early repayment, or amend again (it would be the third amendment since May 2025).
* **Test mechanics (2022 agreement §6.04):** tested at each fiscal quarter-end on trailing four-quarter Consolidated EBITDA. The 4.00x step-up after a qualifying acquisition can be used on no more than two occasions over the agreement's life.
* **Consequence of a breach (checked October 22, 2026 against the credit agreement and all five note indentures):**
  * **Under the credit agreement:** a breach of the leverage covenant is an immediate event of default (Article VII, clause (d)). The 30-day cure that applies to other covenant breaches excludes it, and the agreement has no equity cure. Lenders holding more than 50% of exposures and unused commitments (Required Lenders) can terminate the $1.0B commitment and declare any loans due. While the default continues, Akamai cannot borrow (§4.02(b)).
  * **With the revolver undrawn (today):** nothing is owed, so nothing is accelerated and the notes are unaffected. The cost is losing the backstop the funding table above counts on (up to ~$1.15B with the secured line), plus a negative signal while both ratings carry negative outlooks.
  * **With the revolver drawn:** lenders can accelerate the loans, and that reaches the notes. Each indenture has a cross-acceleration clause (§6.01(g)). If other borrowed-money debt above a threshold is accelerated, or not paid at maturity, and that is not cured, waived or rescinded within 30 days after notice from the trustee or holders of 25% of a series, those holders can declare the series due. The threshold is **$150M for the 2027 notes** and $300M for the 2029, 2030, 2032 and 2033 notes. A covenant breach alone does not trigger the notes; acceleration of more than $150M of revolver loans could put all ~$7.6B at risk.
  * **The timing problem:** the revolver is most likely to be drawn in the same window the covenant tightens (Q4 2026 to Q3 2027; see the funding table).
  * **Likely outcome:** a waiver or amendment before the December 31, 2026 test (the third amendment since May 2025), at the cost of a fee, a higher margin and possibly limits on buybacks, M&A or new debt. Alternatives: use the 4.00x step-up, retire 2027 notes early, or terminate the revolver, which removes both the covenant and the backstop.
* The 10-Q's statement that liquidity is "sufficient… for at least the next 12 months" was written before the September Anthropic deal added ~$5.5B of capex.

**Ratings:** Moody's Baa2, outlook cut to negative in May 2026 (gross debt/EBITDA above 5x at close). S&P cut to BBB in March 2026, outlook negative, two notches above junk.

**Assessment:** a funding squeeze, not a crunch, in the base case. Akamai is investment grade, pays ~$40M a year of interest on $7.6B of notes, and its core business generated ~$1.5B of operating cash flow in FY2025. It can also slow non-Anthropic capex (~$1.8B in 2026), keep buybacks paused, or finance equipment against the take-or-pay contract. A crunch would need several things to happen together between Q4 2026 and Q3 2027: AI-compute credit staying closed, an Anthropic delay or renegotiation leading to rating cuts, the covenant unresolved, and the stock below every conversion price ($93-201) so new converts are very dilutive. The more likely cost is in earnings: each $1B refinanced at ~6.5% instead of ~0.3% costs about $0.35 of EPS after tax, so $2.5B would cost ~$0.85 (~12% of MS's 2027 EPS; not checked against MS's model).

**Watch:** Q3 on November 5 (year-end cash outlook, capex, any 2027-note repurchase or financing); any Q4 8-K amending the credit agreement; any revolver draw before the covenant is resolved; a first straight bond or equipment financing; a downgrade to Baa3 or BBB-; the FY2027 funding plan in February.

Sources for this update: [Q2 2026 10-Q](https://www.sec.gov/Archives/edgar/data/0001086222/000108622226000086/akam-20260630.htm); [credit agreement Amendment No. 3](https://www.sec.gov/Archives/edgar/data/0001086222/000119312526228949/d123781dex101.htm); [2022 credit agreement](https://www.sec.gov/Archives/edgar/data/1086222/000119312522292004/d271055dex101.htm); note indentures: [2027](https://www.sec.gov/Archives/edgar/data/1086222/000119312519223514/d794476dex41.htm), [2029](https://www.sec.gov/Archives/edgar/data/1086222/000119312523215943/d525419dex41.htm), [2030](https://www.sec.gov/Archives/edgar/data/0001086222/000119312526237084/d144441dex41.htm), [2032](https://www.sec.gov/Archives/edgar/data/0001086222/000119312526237084/d144441dex42.htm), [2033](https://www.sec.gov/Archives/edgar/data/1086222/000119312525122451/d948474dex41.htm); [Moody's outlook change (Investing.com)](https://www.investing.com/news/stock-market-news/moodys-affirms-akamai-rating-but-cuts-outlook-on-debt-93CH-4699000); [S&P downgrade (cbonds)](https://cbonds.com/news/3849163/); [Anthropic $518B commitments (Cloud Computing News)](https://www.cloudcomputing-news.net/news/anthropic-ai-infrastructure-518-billion/); [Nscale S-1](https://www.sec.gov/Archives/edgar/data/0002110365/000119312526395475/ck0002110365-20260918.htm); [Anthropic-IREN deal (Dataconomy)](https://dataconomy.com/2026/10/12/anthropic-reportedly-signs-multiyear-cloud-deal-with-iren/); [HSBC downgrade](https://startupmap.iamsterdam.com/news/feed/hsbc-downgrades-akamai-to-hold-cuts-target-to-123-on-cloud-margin-pressure); prices from the Yahoo Finance chart API.

## 1. Executive Summary

**Thesis.** At ~13.5x 2026 non-GAAP EPS guidance and ~13x Morgan Stanley's 2027 EPS, the market values Akamai roughly as a no-growth legacy security and CDN business with a balance-sheet problem attached. Both sell-side reports see more value ($150-165), and both agree on the mechanics: Akamai is spending ~$5.5B to serve an $11.6B, seven-year Anthropic contract, plus ~$1.8B of earlier Anthropic and other CIS commitments, with the money going out before the revenue arrives (2H 2027). Where this memo parts from them is the margin of safety in the deal returns. Morgan Stanley's ~11% IRR holds only if revenue starts on time, at full value, and the servers last at least seven years. Small slips take it to 5-8%, at or below Morningstar's 7.6% cost of capital. With ~90% of recent compute bookings tied to one customer, the stock needs both execution and counterparty durability. The price already discounts a lot of failure, which keeps the bear case from being much lower than ~$60.

* **Bull case:** Contracted CIS revenue lifts growth to the high teens in 2027-28 (Morningstar models +18% and +24%). EPS reaches ~$10 by 2028, investors pay ~17-24x, and the stock returns to $150-177.
* **Bear case:** The Anthropic ramp slips or is renegotiated, colocation and depreciation run ahead of revenue, and security fades to mid-single-digit growth. 2028 EPS stalls near $6, the stock de-rates to ~10x (~$60, -34%), and Akamai adds ~$2-3B of debt to fund 2027.
* **Target investor:** special-situation or value investors who can underwrite capex returns and counterparty risk over 2-3 years. Not for income investors (no dividend, buyback paused), or for anyone seeking clean AI-growth exposure (CIS is 9% of revenue today).

### What the Street assumes vs. this memo

| | Morgan Stanley (Sept 29) | Morningstar (Sept 25) | This memo |
|---|---|---|---|
| Rating / value | Overweight, $165 target | 4 stars, $150 fair value | base ~$106, bear ~$60, weighted ~$107 |
| Method | ~24x CY2027 EPS of $6.89 | DCF: WACC 7.6%, cost of equity 8.5%, 91% of firm value in the terminal stage | 2028 EPS × scenario multiple |
| 2026 / 2027 / 2028 EPS | $6.72 / $6.89 / $7.53 | $6.34 / $8.36 / $10.08 (adjusted) | 2028: $6.03 bear, $8.15 base, $10.42 bull |
| Consensus (Refinitiv, via MS) | $6.67 / $6.71 / $7.93 | | |
| Anthropic deal economics | ~11% cash IRR; ~30%+ steady operating margin | 30-35% gross margin; revenue/capex 1/3 vs. a usual 1/2 | IRR falls to 5-8% under modest slips (Section 2) |
| Moat | not rated | **none** (cut from narrow in May 2026) | thin in compute; real in security |
| Funding | "increasingly likely" Akamai raises capital, most likely debt | FCF to the firm -$2.70B (2026), -$2.29B (2027); net debt/EBITDA 5.1x and 5.0x | 2026 FCF -$2.0B to -$2.7B; 2027 need ~$2-3B incl. the $1.15B notes |

At $90.65 the stock trades at **13.2x MS's 2027 EPS** versus the ~24x MS applies, and at **0.60x Morningstar's fair value** (Morningstar's 5-star buy threshold is $75; its 1-star level is $262.50). The two reports differ sharply on earnings: Morningstar's 2027 EPS ($8.36) is 21% above MS ($6.89) and 25% above consensus ($6.71). That gap is mostly about when the depreciation and colocation costs of the new capacity hit the P&L.

## 2. Business Model & Unit Economics

**Revenue mix (Q2 2026, $1.100B, +5%):** Security $604M (55%, +10%), Delivery and other cloud apps $396M (36%, -6%), CIS $99M (9%, +39%). FY2025: $4.208B (+5%).

**Compute contract economics (Morgan Stanley's disclosure-based framework):**

| Item | Figure |
|---|---|
| Signed CIS commitments | ~$14.4B, of which ~90% of recent bookings tie to Anthropic (two deals, $13.3B) |
| Power needed | 95-105 MW |
| Fully ramped annual revenue | ~$2.2B (~$22M per MW) |
| Annual costs at scale | ~$1.0B capex/depreciation, ~$350M colocation, ~$150M operating expense → ~30%+ operating margin |
| Anthropic September deal | capex ~$1.7B (Q4 2026), ~$3.1B (2027), ~$0.7B (2028); revenue from 2H 2027: $150-300M in 2027, ~$1.7B run-rate by end-2028 |
| MS deal IRR | ~11% after adding back depreciation, with no hardware refresh needed over seven years and upside if servers run longer or the contract renews |

**Stress-testing the ~11% IRR (this memo's arithmetic on MS's Exhibit 1 cash flows).** Reproducing the exhibit gives **10.6%**. Then:

| Change to MS's case | Deal IRR |
|---|---|
| MS base case | ~10.6% |
| Assets run two extra years at half the cash flow (MS's renewal upside) | ~12.9% |
| Steady-state operating margin 22% instead of 30% (cash costs 8 points higher) | ~7.9% |
| Revenue ramp starts one year later (capex unchanged) | ~5.7% (approximate) |
| Revenue 15% lower (renegotiation or under-delivery) | ~5.5% |
| Revenue 30% lower | ~-0.2% |

The base IRR clears Morningstar's 7.6% WACC by about 3 points. Every plausible slip in timing or price erases that margin. The renewal case is the only one that widens it.

**The depreciation question, resolved.** The earlier version of this memo could not reconcile management's 20-30% margin range with a $5.5B buildout. MS's exhibit answers it: the model depreciates the capex over **seven years** (~$786M a year, 47% of steady revenue), leaving cash costs of ~$374M (23%) and a 30% operating margin. The accounting margin depends heavily on that life:

| Depreciation life | Annual depreciation | Operating margin on ~$1.66B revenue | After-tax return on $5.5B |
|---|---|---|---|
| 5 years | $1.10B | ~11% | ~2.7% |
| 6 years | $0.92B | ~22% | ~5.4% |
| 7 years (MS) | $0.79B | ~30% | ~7.3% |
| 8 years | $0.69B | ~36% | ~8.8% |

Cash IRR is barely affected by the depreciation choice; reported EPS and ROIC are. That explains why the stock trades on EPS fear while MS argues the cash economics are fine. It also explains why MS's 2027 EPS ($6.89) is barely above 2026 despite revenue growth. Morningstar's ROIC path (6.0% in 2026, 5.8% in 2027, 8.9% by 2030, against a 7.6% WACC) says the same thing in accounting terms: value-neutral for years.

**Operating leverage is negative near term:** non-GAAP operating margin falls from 30% (FY2025) to 25-26% (2026 guide). Non-GAAP EPS fell 8% in Q2 on +5% revenue.

**Cash conversion:** OCF was 36% of revenue in FY2025. The problem is capex. This memo estimates 2026 FCF at -$2.0B to -$2.2B; Morningstar's free cash flow to the firm is **-$2.70B (2026) and -$2.29B (2027)**, breaking even only in 2028. From $4.62B of cash at June 30, that leaves roughly **$1.5-2.2B at year-end 2026** before any new financing.

## 3. Competitive Position & Moat

* **Market position:** one of three global CDN and edge-security platforms with Cloudflare and AWS CloudFront. Akamai is strongest in large regulated enterprises; Cloudflare is growing far faster (Q2 2026 revenue $696M, +36%). Morningstar estimates 20-30% of global internet traffic passes through Akamai's network.
* **Moat classification:**
  * *Security:* real network effects (traffic data trains detection for WAF, API, bot and DDoS) and switching costs (Guardicore and Zero Trust integration). Security is 53% of revenue, up from 12% a decade ago (Morningstar).
  * *Delivery:* commoditized and shrinking. Media companies keep insourcing, Cloudflare and Fastly compete on price, and hyperscalers bundle CDN.
  * *Compute:* Morningstar rates it no-moat. Today's attractive unit economics reflect supply lagging demand, "not of a maintainable market structure," and customers multi-home workloads. MS's counter: Akamai sells software and network value on top of capacity, and its distributed CIS footprint already serves all three hyperscalers as customers.
* **Durability assessment:** Morningstar cut the whole company to **no moat** in May 2026 because the compute investment could destroy more value than security creates. This memo treats the security moat as intact, and the compute moat as unproven until contracts beyond Anthropic arrive at similar terms.
* **Key competitors:** Cloudflare (see [[net-3-investment-memo]]), Zscaler and Palo Alto (Zero Trust), F5 and Imperva/Thales (application security), AWS/Azure/GCP, and in compute CoreWeave, IREN and Blackstone-backed builders, which Morningstar describes as better funded.

## 4. Top 3 Growth Drivers & Sensitivities

| Driver | Description | TAM effect | Probability-weighted view |
|---|---|---|---|
| 1. Contracted CIS ramp | ~$14.4B signed; Anthropic $13.3B (up to ~$20.6B with expansion); revenue from 2H 2027 | Morningstar models compute growth averaging 93% a year over 2027-29 and 36% over its forecast | Revenue is contracted (take-or-pay once delivered); timing and returns are the uncertainty |
| 2. Security mix shift | Guardicore + API Security ($293M FY2025, +43%), LayerX browser security | Morningstar assumes 10% a year through 2035 | 60% holds high-single-digit growth; 40% slides to mid-single digit |
| 3. Delivery decline rate | Consolidation (Edgio exit, CrowdStrike) vs. price compression | Morningstar models roughly flat; MS lists steeper declines as a downside risk | Base -5% a year; bear -8%; bull -3% |

**Scenario model for 2028 (this memo's assumptions; 2026 base from guidance midpoint, $4.49B):**

| | Bear (30%) | Base (50%) | Bull (20%) |
|---|---|---|---|
| Security growth, 2026-28 | +5% a year | +8% a year | +10% a year |
| Delivery and other, 2026-28 | -8% a year | -5% a year | -3% a year |
| CIS revenue, 2028 | $1.2B (Anthropic ramp late) | $2.2B (MS's fully ramped contract base) | $3.0B (expansion option exercised) |
| Total revenue, 2028 | $5.18B | $6.42B | $7.38B |
| Cross-check | | Morningstar 2028 revenue: $6.51B | |
| Non-GAAP operating margin | 22% | 24% | 27% |
| Non-GAAP EPS (19% tax; 153-155M shares incl. warrant dilution) | ~$6.03 | ~$8.15 | ~$10.42 |
| Street 2028 EPS for reference | MS $7.53; consensus $7.93 | | Morningstar $10.08 |
| P/E applied | 10x | 13x | 17x |
| Implied value | **~$60 (-34%)** | ~$106 (+17%) | ~$177 (+95%) |

Probability-weighted value: **~$107.** Morningstar's 5-star (buy) threshold of $75 sits between this memo's bear and current price.

**Deep-bear tail (not in the weights):** Anthropic reduces, delays or renegotiates (its compute spending is reported above $500B within a year, and it is preparing an IPO). Revenue arrives 15-30% below contract, so the deal IRR is ~0-5%, and Akamai holds $3-4B of CPU capacity it must re-market as supply catches up (Morningstar's pricing-compression case). Margin falls toward 18%, 2028 EPS ~$4.50, and at 9x the stock is ~$40 (-55%). MS's partial mitigant: capacity is spread across many colocation sites, and the hardware is in demand and could be reused or resold.

**Timeline and milestones:**
* **November 5, 2026 (Q3):** CIS growth vs. the ≥50% FY guide; Q3 capex vs. $475-525M and the Q4 Anthropic spend (~$1.7B per MS); RPO including the $11.6B.
* **February 2027 (FY2027 guide):** MS calls this "the first important proof point." Watch revenue vs. "low teens," the capex plan (~$3.1B for Anthropic alone), EPS vs. consensus $6.71, and the financing plan.
* **2H 2027:** Anthropic September-deal revenue starts; MS expects $150-300M in FY2027.
* **September 1, 2027:** $1.15B of 0.375% notes mature (stock below the $116.18 conversion price).
* **End of 2028:** ~$1.7B annualized run-rate from the September deal (MS). Missing it is the clearest bear trigger.

## 5. Risk Framework with Failure Modes

Ranked by severity × probability.

| # | Risk | Trigger | Impact | Mitigation |
|---|---|---|---|---|
| 1 | **Counterparty concentration** | Anthropic delays, under-uses or renegotiates; AI-lab funding tightens | ~90% of recent CIS bookings and ~$13.3B of contracts tied to one private company; IRR to 0-5% at 15-30% lower revenue | Take-or-pay once capacity is delivered; warrants (7.7M shares at $111.33; 40% vested) align Anthropic with Akamai's stock; distributed, reusable capacity |
| 2 | **Returns below cost of capital** | One-year ramp delay, or cash costs 8 points above plan | Deal IRR ~5.7-7.9% vs. 7.6% WACC; ROIC ~6% through 2027 (Morningstar) | Contracted pricing; MS's renewal upside (~12.9% IRR with two extra years) |
| 3 | **Funding and leverage** | FCF -$2.7B (2026) and -$2.3B (2027) per Morningstar; $1.15B notes due Sept 2027 | New debt of ~$2-3B; net debt/EBITDA ~5x (Morningstar); buybacks stay paused; MS notes the "natural shareholder base" may change as Akamai becomes a debt-funded capex story | $4.6B cash at June 30; $1.0B undrawn revolver (availability depends on the 3.50x gross leverage covenant from December 31, 2026; see the October 16 update); low-coupon converts; management rules out equity issuance for now |
| 4 | **EPS trap from accounting** | Depreciation life shorter than seven years; colocation ahead of revenue | Reported EPS flat through 2027 (MS $6.72 → $6.89); every new CIS win cuts near-term EPS again (MS) | Cash IRR barely affected by depreciation choice |
| 5 | **Core erosion** | Security below 7% growth; delivery worse than -8% | Removes the cash engine that funds compute | Guardicore/API/LayerX growth; CrowdStrike-type consolidation wins |

**Other risks:** GAAP vs. non-GAAP gap (Morningstar 2026 GAAP EPS $2.46 vs. adjusted $6.34); 13.4% short interest; terminal-value dependence in DCF fair values (91% of Morningstar's firm value); the AI-compute cycle described in [[ai-compute-commencement-wall-and-refinancing-trap]].

**Pre-mortem.** If this investment fails by 2029, the most likely reason is that the Anthropic capacity went live late or at a lower effective price. Akamai had then spent $5.5B at a single-digit return, borrowed $2-3B to bridge 2027, and saw security growth slow, so the market kept pricing it as a levered legacy CDN at ~10x earnings.

**Assumptions that must hold:**
1. Anthropic revenue starts in 2H 2027 and reaches ~$1.7B by end-2028 at contracted value.
2. Servers stay productive for at least seven years (MS's model), so accounting margins approach 30%.
3. Security grows at least high-single digits through 2028.
4. 2027 funding (notes plus capex) is raised as low-cost debt, not equity or an expensive convert.
5. Additional CIS customers sign at similar terms, diluting the concentration (MS says inbound interest rose after the large deals).

## 6. 12-Month KPI Watch List

| KPI | Current value | Target range | Red flag | Frequency / source |
|---|---|---|---|---|
| CIS revenue growth (cc) | +39% (Q2 2026) | ≥50% for FY2026, accelerating in Q4 | Below 40% in Q4 2026 | Quarterly release |
| Security revenue growth (cc) | +9% (Q2 2026) | High single digits | Below 7% | Quarterly release |
| Delivery and other cloud apps | -5% cc (Q2 2026) | -3% to -6% | Worse than -8% | Quarterly release |
| Non-GAAP operating margin | 25% (Q2 2026) | 24-26% | Below 23% | Quarterly release |
| Capex | $347M (Q2); Q3 guide $475-525M; ~$1.7B Anthropic in Q4 (MS) | ~$3.1B Anthropic in 2027 (MS) | Overrun without matching RPO growth | Quarterly release |
| Cash and marketable securities | $4.62B (June 30, 2026) | ~$1.5-2.2B at YE 2026 before financing | Below $1.5B with no refinancing plan | Quarterly balance sheet |
| RPO | $7.6B (June 30, pre-Anthropic) | Rises by ~$11.6B with the September deal | Anthropic not reflected, or RPO falls | 10-Q / 10-K |
| FY2027 guidance (February 2027) | Mgmt: growth "low teens"; consensus EPS $6.71 | EPS ≥ consensus; revenue ≥ low teens | EPS guide below ~$6.50 | Q4 release |
| Capacity delivered vs. 95-105 MW plan | Some capacity already secured (MS) | On-schedule power for a 2H 2027 start | Any delay disclosure | Calls / 10-Q |
| Financing activity | $7.64B converts; buybacks paused | Refinancing of 2027 notes at a low coupon | High-coupon issuance or equity | 8-K |

**Valuation reference points:** Morgan Stanley target $165 (Overweight); Morningstar fair value $150 (5-star below $75, 1-star above $262.50); stockanalysis.com consensus target ~$159 (24 analysts). One analyst cut to hold on October 8, 2026, citing compute margins and capex (firm not verified). Short interest 13.4%.

## Related

* [[akam-1-document-sources]], [[akam-2-equity-report]]
* Analyst reports (local PDFs): `reports/akam-morgan-stanley-20260925.pdf`, `reports/akam-morningstar-20260925.pdf`
* [[net-3-investment-memo]]: Cloudflare, the closest public competitor.
* [[ai-capex-financing-risk-semianalysis-2026-10]] and [[ai-compute-commencement-wall-and-refinancing-trap]]: how AI compute buildouts get financed and where they break.
* [[market-newsletter-digest-2026-09-25]]: the Anthropic deal and the market's reaction.
* [[valuations]]: multiple and discount-rate framework.
