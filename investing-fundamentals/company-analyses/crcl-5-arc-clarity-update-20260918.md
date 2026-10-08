---
title: "CRCL — Post-Catalyst Update: Clarity Act Failure, Arc Mainnet, Fed Hike"
created: 2026-09-18
type: analysis
tags: [company, fintech, crypto, valuation, catalyst-review]
parent: investing-fundamentals/company-analyses/CRCL.md
supersedes_assumptions_in: [crcl-3-investment-memo.md, crcl-4-stress-test.md]
confidence: medium-high on facts, medium on Arc quantification
---

# CRCL — Post-Catalyst Update (Sept 18, 2026)

```
Price: $91.75 (+7.8% on 9/18)   Mkt cap: $23.3B   Shares: 253.9M out / ~270M dil
52-wk: $49.90 – $159.47          TTM rev $2.91B   TTM EPS $1.80   P/E 51x  Fwd P/E 74x
Consensus PT: $104.07 (28 analysts)   Range: $37 – $243
```

> **The mid-September catalyst window flagged in `crcl-3-investment-memo.md` (line 169) resolved 2-for-3 in Circle's favor, but not the way the memo framed it.** The CLARITY Act died (bearish, but small direct impact). Arc mainnet launched with a marquee validator set (bullish, unquantified). And the Fed **hiked** 25bp to 3.75%–4.00% on Sept 16 — the first hike since 2023 — which directly contradicts the single largest assumption in the Stage-4 bear case ("unhedged 150bp easing cycle strips ~$495M in net revenue"). That bear leg needs to be re-underwritten, not merely re-weighted.

---

## 1. Revenue and earnings by business line

Circle reports **one revenue line split two ways**: reserve income and "other revenue." There are no reportable segments, so any business-line build is a reconstruction.

### Q2 2026 actuals ($M)

| Line | Q2'26 | Q2'25 | YoY | % of rev |
|---|---:|---:|---:|---:|
| Reserve income | 668 | 637 | +5% | 95.2% |
| Other revenue (subscription & services) | 34 | 24 | +41% | 4.8% |
| **Total revenue & reserve income** | **701** | **655** | **+7%** | 100% |
| Distribution, transaction & other costs | (412) | (408) | +1% | — |
| **Net retained revenue** | **289** | **247** | +17% | **41.3% take rate** |
| Adjusted opex | (146) | (119) | +23% | — |
| **Adjusted EBITDA** | **143** | **132** | +8% | 49.5% of net rev |
| GAAP opex | (254) | (579) | −56% | SBC normalization post-IPO |
| **GAAP net income** | **48** | **(482)** | +$530M | — |

### The economics that actually matter

**Reserve income is a rate × float product with a 61.5% revenue-share leak.**
- Float: $73.3B USDC in circulation (+19% YoY); average balances grew ~25% YoY.
- Yield: 3.48% reserve return rate in Q2'26, down 66bp YoY from 4.14%.
- The spread compression is why **average USDC grew 25.4% but revenue grew 6.6%**.
- Distribution and transaction costs were $410–412M, or **61.5% of reserve income**. Coinbase takes **100% of reserve income on USDC held on the Coinbase platform** plus roughly half the residual on balances held elsewhere; Binance and other distribution partners take the rest.
- Net effect: Circle retains roughly **38.5 cents of each marginal reserve dollar**, pre-tax.

**Annualizing Q2 as a run-rate:**

| | $M |
|---|---:|
| Reserve income | 2,672 |
| Other revenue | 136 |
| Total revenue | 2,808 |
| Distribution & transaction costs | (1,648) |
| **Net retained revenue** | **1,160** |
| Adjusted opex | (584) |
| **Adjusted EBITDA** | **572** |

At $23.3B market cap, that is **~20x annualized net retained revenue** and ~41x annualized adjusted EBITDA. Note this is close to the ~38x net-retained-revenue figure in the CRCL hub note at $71.50 — the multiple has *compressed* on the share price rise because net retained revenue grew faster than the stock.

**"Other revenue" is the hockey stick everyone is arguing about.** H1'26 actual was $37M ($17M Q1 + $20M Q2). FY26 guidance was raised from $150–170M to **$310–330M**. That raise is almost entirely the **Arc token presale**: ~$222M raised, with roughly 75% of presale milestone revenue recognized in 2026 (~$165–180M). Strip the presale out and the organic platform/software line is guided to roughly $130–165M for the year — consistent with the $120–160M FY26E range in `crcl-3-investment-memo.md` (line 34), and *not* the 8x organic quarterly ramp the Stage-4 stress test characterized it as. **This is a material correction to the bear case: the guidance raise is a one-time financing-adjacent item, not a claim of organic software inflection.** Both readings are unflattering in different ways — the bear was wrong about the ramp being an organic promise, but the bull can't count $180M of presale recognition as recurring platform revenue either.

**Other revenue components (approximate, not separately disclosed):**
- CCTP / cross-chain transfer fees
- Circle Mint subscription and minting/redemption fees
- Programmable wallets and developer APIs
- Circle Payments Network (CPN) — $14.7B annualized transaction volume, 175 FIs enrolled, +76% QoQ; **monetization only began in H2'26**
- Arc token presale milestone recognition (2026 only)
- Tazapay (~$400M acquisition) cross-border payments, once closed

### Rate sensitivity — the single most important number

On the current $73.3B float, holding circulation constant:

| Fed move | Gross reserve income | Net retained (38.5%) | After-tax @25% | EPS impact |
|---|---:|---:|---:|---:|
| ±25bp | ±$183M | ±$71M | ±$53M | **±$0.20** |
| ±50bp | ±$366M | ±$141M | ±$106M | ±$0.39 |
| ±100bp | ±$733M | ±$282M | ±$212M | ±$0.78 |
| ±150bp | ±$1,100M | ±$423M | ±$317M | ±$1.18 |

Against 2026E consensus EPS of **$1.20**, a single 25bp move is **~17% of earnings**. The Sept 16 hike is worth roughly **+$0.20 in annualized EPS** on current float, and explains most of the +7.8% move on Sept 18 alongside the Arc launch. A 150bp easing cycle wipes out essentially all of consensus EPS — the Stage-4 bear arithmetic was right even if its direction call has now gone the other way.

---

## 2. CLARITY Act failure — effect on business and valuation

**What happened:** The Digital Asset Market CLARITY Act failed a Senate cloture vote **49–50 on Sept 15**, short of the 60 needed and short of even a simple majority, with multiple Republicans defecting. The binding constraint was ethics provisions restricting senior officials' crypto business ties, compounded by pre-midterm politics. CRCL fell ~7% on the news before recovering on the Fed hike and Arc launch.

**Direct impact on Circle: modest, and arguably net-positive on one axis.**

1. **Circle's own regulatory basis is unaffected.** Stablecoin issuance is governed by the **GENIUS Act (2025)**, which passed and stands. Circle's OCC national trust bank charter, EU MiCA authorization, and state licenses all derive from frameworks already in force. CLARITY was market-structure legislation for *digital asset securities/commodities* — it was never Circle's enabling statute.

2. **The yield loophole survives — and this cuts both ways.** GENIUS bans issuers from paying interest directly. CLARITY's **Section 404** would have closed the exchange-level workaround, under which platforms pay "activity-based membership rewards" on stablecoin balances that are functionally identical to deposit interest. With CLARITY dead, that loophole stays open.
   - **Positive for USDC circulation:** Coinbase and other distributors can keep paying 4%-ish rewards on USDC balances, which is a primary driver of float growth. Float growth is Circle's revenue.
   - **Negative for Circle's margin:** the rewards are funded out of Circle's revenue share. The loophole is precisely the mechanism by which Coinbase extracts 100% of on-platform reserve income. Keeping it alive **entrenches the 61.5% distribution cost** rather than creating an opening to renegotiate it.
   - The American Bankers Association lobbied hard against §404's absence, arguing yield-bearing stablecoins could take the market from ~$300B to $2T by pulling bank deposits. Circle wins the TAM argument; Coinbase wins the economics.

3. **Durability risk is the real cost.** Without statute, the framework rests on the March 2026 SEC–CFTC joint interpretation plus the SEC's pending "Regulation Crypto Assets." Post-*Loper Bright*, agency interpretations get no mandatory judicial deference — a court can vacate them, and a future SEC/CFTC can withdraw them without legislation. SEC Chair Atkins has publicly conceded the rules "lack durability without congressional backing." For a company whose entire bull case is *regulatory moat*, the moat is now administrative rather than statutory on everything except issuance itself.

4. **Institutional adoption timing slips.** The validator cohort Circle just recruited (BlackRock, DTCC, ICE, Visa, Mastercard, State Street, BNY, HSBC, Standard Chartered) are regulated entities whose committed capital and volume decisions are gated on legal certainty about tokenized securities. CLARITY's failure doesn't stop them from validating; it slows the migration of *actual assets* onto Arc. This is the channel through which the failure most plausibly hurts the Arc revenue ramp — a timing delay of perhaps 2–4 quarters, not a structural kill.

5. **Next window:** new Congress in January 2027. If Democrats take either chamber in November, crypto market-structure priorities shift materially and the bill likely restarts from a worse baseline.

**Valuation effect:** I'd size this at **−5% to −10% on fair value**, concentrated in the terminal-multiple assumption rather than near-term estimates. It removes essentially nothing from 2026–27 numbers and does not touch GENIUS. What it removes is the argument for valuing Circle on a *statutory-monopoly* multiple. TD Cowen's response — reiterate Buy, raise PT $87→$92 — is the right shape of reaction: the failure matters less than the Fed hike that landed the next morning.

---

## 3. Arc / BlackRock / Visa — financial implications

**What launched (Sept 16, 2026):**
- USDC-native Layer 1; **fees paid in USDC**, no volatile native gas token; sub-second deterministic finality.
- **Founding validators:** BlackRock, DTCC, Galaxy, ICE, Mastercard, MoneyGram, SBI Group, Standard Chartered, Sumitomo, Visa, Worldpay (Global Payments).
- **100+ day-one partners** across banks (BNY, HSBC, SocGen, State Street, BTG Pactual), exchanges (Binance, Coinbase, Kraken, OKX, Bybit), DeFi (Aave, Morpho, Uniswap), custody (Fireblocks, BitGo, Anchorage), infra (Alchemy, Chainlink, QuickNode).
- **10B ARC tokens minted** — first network token minted by a US-listed company. Allocation: **60% ecosystem / 25% Circle (validator ops + staking income) / 15% long-term reserve**. Explicitly *not* a commitment to a public token launch; PoS transition targeted 2027.
- Presale: **$222M at $3B FDV**, led by a16z crypto ($75M), with BlackRock, Apollo, ICE, SBI, Janus Henderson, Standard Chartered Ventures, General Catalyst, Marshall Wace, ARK, Haun, Bullish.
- Testnet: 700M+ transactions, 1,200+ projects, 75k Arc House developers. StableFX supports 29 stablecoins.

**Four distinct monetization channels — of very different quality:**

| Channel | Mechanism | Margin | Durability |
|---|---|---|---|
| Gas fees | USDC-denominated network fees | ~85%+ | Structurally low-value; L1 fee markets commoditize |
| CPN / StableFX | Cross-border settlement + FX spread | 60–80% | Best revenue quality; real substitute for correspondent banking |
| ARC staking | Circle's 2.5B tokens staked post-PoS (2027+) | high but reflexive | Depends on token price existing |
| **USDC float pull-through** | Arc adoption → more USDC → reserve income | 38.5% net | **The actual prize** |

**The critical insight for modeling: Arc's direct fee revenue is almost irrelevant next to its effect on float.** A blockchain doing extraordinary volume — say 5B transactions/year at a cent each — generates $50M. Fifteen billion dollars of incremental USDC circulation at a 3.75% reserve rate generates **$563M gross / $217M net-retained**. Arc is a *distribution strategy for USDC*, financed by a token sale, dressed as an infrastructure business. That is also why the validator list matters more than the tech: BlackRock, DTCC, ICE and State Street don't bring gas fees, they bring tokenized collateral that has to settle in something.

**Strategic subtlety — Arc is partly a Coinbase hedge.** Coinbase takes 100% of on-platform reserve income and operates Base, a competing L2. Every dollar of USDC that lives on Arc rather than on Coinbase is a dollar on which Circle keeps ~38.5% instead of 0%. If Arc shifts even 10% of float off Coinbase rails, the *blended* take rate rises without renegotiating a single contract. **This mix-shift effect is under-modeled by both the bulls and the bears** and is worth more than Arc's gas fees by an order of magnitude. It is also the reason the channel conflict flagged at line 130 of the investment memo is a feature, not just a risk.

**Balance sheet option value:** Circle's 2.5B ARC tokens at the $3B presale FDV are worth ~$750M, or **$2.78/share** — pre-tax, illiquid, and not marked. At a $10B FDV it's $9.26/share; at $25B, $23.15/share. Given the $3B FDV was set by a16z/BlackRock in a negotiated round, treat $2.78–$9.26/share as the defensible range and anything above as speculation. This is genuinely *not* in most sell-side models.

---

## 4. Why analyst targets diverge from $37 to $243

A **6.6x spread** across 28 analysts (11 strong buy / 2 buy / 12 hold / 3 strong sell) is extreme for a $23B company. Consensus $104.07 is a near-meaningless average of two incompatible theories.

**Known positioning:**

| Firm | PT | Stance |
|---|---:|---|
| Needham | ~$250 | Bull |
| Seaport Global | $235 | Bull |
| Bernstein | $140 (Aug 6, Outperform; earlier $190) | Bull |
| KBW | $105 | Market Perform |
| Mizuho (Dolev) | $85→$100 | Neutral |
| Goldman Sachs | $83 | Neutral |
| TD Cowen (Bergin) | $92 (raised from $87) | Buy |
| JPMorgan | $80 | Bear |
| **Morgan Stanley** | **$38 (Aug, downgrade to UW)** | Bear |

**The five assumptions that generate the spread:**

**(1) What kind of company is this? — the dominant driver.**
Bears model a **levered money-market fund**: 95% of revenue is reserve interest, 61.5% of it leaks to a single counterparty, so value it on net interest income at a specialty-finance multiple of 10–15x earnings. Bulls model a **payments network**: reserve income is the current monetization of a settlement network with 175 FIs, $14.8T quarterly on-chain volume (+151%) and Visa/Mastercard/DTCC as validators, deserving 30–50x. The same 2027 EPS of ~$1.36 gives you $14–20 (bear) or $41–68 (bull) from the multiple choice *alone*, before any estimate difference. **Roughly 60–70% of the $37–$243 spread is the multiple, not the forecast.**

**(2) Terminal reserve rate.** Bears underwrite 2.0–2.5% terminal Fed funds; bulls 3.5–4.0%. That's a 150bp gap = **$1.18 of EPS** on current float — more than 2026 consensus EPS in its entirety. Every model is a rates model wearing a fintech costume. Note that the Sept 16 hike moved the near-term reality decisively toward the bull assumption, and the Sept 2026 dot plot points to low-4% funds in 2027.

**(3) USDC circulation trajectory to 2028.** Bear: stagnation at $70–80B as yield-bearing tokenized MMFs (BUIDL), USDG, Stripe/Bridge and the 21-bank consortium capture institutional float. Base: ~$125B (19% CAGR). Bull: $180B+. At 38.5% retention and 3.75%, each **$10B of float is ~$144M of net retained revenue** — roughly $0.40/share after tax. The $110B gap between bear and bull is ~$4.40/share of annual EPS.

**(4) Distribution cost trajectory — the most under-discussed variable.** Bears assume 61.5% goes to 65%+ as distributors (Coinbase, Binance, and now banks) extract more — the August Coinbase renewal through 2029 gave Coinbase *more* economics, which is the empirical trend. Bulls assume Arc, CPN and direct Circle Mint relationships pull the blend down toward 50–55%. A 10-point move in distribution costs on $2.7B of reserve income is **$267M pre-tax, ~$0.74/share** — comparable to a 100bp rate move, and far more controllable by management. Whoever is right about this is right about the stock.

**(5) Arc credibility.** Bears assign zero — pre-revenue, no disclosed fee model, gas markets commoditize, and the guidance raise was a token sale. Bulls capitalize a $450M–$1.0B platform business at software multiples. This is the newest and least anchored variable, and it's where the $243 target lives.

**A structural point:** because reserve income is ~95% of revenue and distribution costs are ~62% of that, Circle's earnings are a **doubly-levered residual** — small errors in rate, float, or distribution percentage compound multiplicatively into large EPS errors. A 10% miss on each of three inputs in the same direction is a ~30–40% EPS miss. The target dispersion is an honest reflection of the business's operating leverage, not analyst sloppiness.

---

## 5. Arc incremental revenue/EPS range and implied stock impact

Steady-state 2028 estimates. Direct revenue at ~85% contribution margin; Arc-driven reserve income at 38.5% retention and ~55% contribution margin; 25% tax; 270M diluted shares.

| Scenario | Gas | CPN/FX | Staking | Direct rev | Arc-driven USDC | Reserve rev (net) | Total rev | EBIT | Net income | **EPS** |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **Bear** | $10M | $40M | $25M | $75M | $0 | $0 | **$75M** | $64M | $48M | **+$0.18** |
| **Base** | $60M | $150M | $90M | $300M | +$15B | $217M | **$517M** | $374M | $281M | **+$1.04** |
| **Bull** | $250M | $450M | $300M | $1,000M | +$50B | $722M | **$1,722M** | $1,247M | $935M | **+$3.46** |

The Base case is consistent with Daloopa's 2027 other-revenue estimate of $603M and the ">$450M+ by FY2028" platform figure in `crcl-3-investment-memo.md` (line 34). The Bull case is close to the memo's "$1.0B in annual software/gas fees."

### Implied per-share value at business-line multiples

Arc's revenue is a **blend**, so a single multiple is wrong. Applying differentiated multiples:

| Component | Multiple used | Rationale |
|---|---|---|
| Gas fees | 8–12x earnings | Commoditizing; L1 fee markets compress |
| CPN / StableFX | 20–30x | Payments network economics (V/MA trade 25–32x; cross-border fintech 20–25x) |
| Staking income | 6–10x | Reflexive, token-price dependent |
| Arc-driven reserve income | 10–14x | Same quality as base reserve income; rate-cyclical |

| Scenario | Blended multiple | **Implied $/share from Arc** | % of $91.75 |
|---|---:|---:|---:|
| Bear | 8x | **+$1.40** | 1.5% |
| Base | 15x | **+$15.60** | 17% |
| Bull | 25x | **+$86.60** | 94% |
| *Plus ARC token stake* | — | *+$2.80 to +$9.30* | 3–10% |

**Read-through:** Arc is worth roughly **$4 to $96 per share**, centered near **$18** ($15.60 operating + ~$2.80 token). At $91.75 with a $104 consensus, the market is embedding something close to the Base case with partial credit — the stock's +7.8% move on launch day (~$7/share) is consistent with the market marking Arc from "optionality" to "early Base."

**The asymmetry is real but backloaded.** Bull-case Arc alone roughly doubles the stock, which is why the $243 targets exist and are not absurd. But the Bull case requires *simultaneously*: institutional tokenized assets migrating on-chain at scale (gated on the market-structure legislation that just died), CPN monetizing at 3–5x current volume, and a public ARC token in 2027. Those aren't independent bets — they share a common regulatory dependency that just got materially weaker. **Correlated conditionality is the thing to underwrite here, and it argues for weighting Bear/Base more heavily than a naive probability tree would.**

---

## 6. Implications for the existing position framework

The Stage-4 arbitrator verdict (Underweight / 0.5–1.0% speculative, at $71.50) rested on three legs. Post-catalyst status:

| Bear leg | Status | Assessment |
|---|---|---|
| "150bp easing cycle strips ~$495M net revenue" | **Invalidated in direction** | Fed *hiked* 25bp Sept 16, first since 2023, unanimous 12–0; dot plot points to low-4% funds in 2027. Worth +$0.20 EPS. The arithmetic was sound; the macro call was wrong. |
| "$310–330M guidance is an 8x organic ramp off $37M H1" | **Partially invalidated** | ~$165–180M of the guide is Arc presale milestone recognition, not organic software. The guide is less aggressive than characterized — but it's also lower-quality revenue than bulls credit. |
| "21-bank consortium + BUIDL capture institutional float" | **Weakened** | BlackRock (BUIDL's sponsor), DTCC, ICE, State Street, BNY, HSBC and Standard Chartered are now **Arc validators**. Co-option is not capitulation, but it's not the displacement the bear case assumed. |
| *New:* Regulatory moat is administrative, not statutory | **New bear leg** | CLARITY's failure leaves market structure resting on a *Loper Bright*-vulnerable SEC/CFTC interpretation. Argues for a lower terminal multiple. |

**Net:** the bear case has lost its strongest leg (rates) and gained a weaker one (regulatory durability). The 0.5–1.0% sizing was calibrated to a macro view that has now inverted. This warrants a re-run of the sensitivity matrix at 3.75–4.00% terminal funds rather than a sizing change made on this note alone — the stock is also 28% higher than when that verdict was written, which absorbs some of the improvement.

**KPIs to watch (updated from memo line 155):**
- **Arc daily gas burn** — the memo's ≥$250k/day bull threshold is now measurable on Arc Explorer. Note: gas burn is a *volume proxy*, not the revenue driver. Watch USDC-on-Arc balances instead.
- **Q3 other revenue ex-presale** — needs to clear $45–50M/quarter organic to validate the platform thesis. Strip the presale recognition manually; the reported number will flatter.
- **Distribution costs as % of reserve income** — if this breaks below 60%, the mix-shift thesis is working and it's worth more than any Arc fee line.
- **USDC circulation** — two consecutive quarters of contraction remains the thesis-invalidation trigger.
- **Validator defections** — loss of ≥2 founding nodes.

---

## Sources

- [Circle Reports Second Quarter 2026 Results](https://www.circle.com/pressroom/circle-reports-second-quarter-2026-results) — Q2 P&L, USDC circulation, CPN metrics
- [Circle Q2 2026 8-K](https://www.sec.gov/Archives/edgar/data/1876042/000187604226000246/augustepr-circle_q22026f.htm) — SEC filing
- [Daloopa: Circle Q2 2026 — Building the Model Before Arc Launches](https://daloopa.com/blog/analyst-pov/circle-crcl-q2-2026-earnings-arc-launch-model) — distribution cost %, reserve yield, 2027 estimates
- [Circle Q2 2026 earnings call guidance detail](https://finance.biggo.com/news/US_CRCL_2026-08-05) — $310–330M other revenue guide, presale recognition
- [Seeking Alpha: Circle outlines $310M–$330M 2026 other revenue](https://seekingalpha.com/news/4626342-circle-outlines-310m-330m-2026-other-revenue-as-arc-mainnet-targets-september-16-launch)
- [CoinDesk: Crypto Clarity Act flames out in failed U.S. Senate vote](https://www.coindesk.com/policy/2026/09/15/crypto-clarity-act-flames-out-in-failed-u-s-senate-vote) — 49–50 vote
- [CNBC: Senate cloture vote on Clarity Act fails](https://www.cnbc.com/2026/09/15/senate-cloture-vote-on-clarity-act-fails-dealing-regulatory-setback-to-crypto-industry.html)
- [NYDIG: What Happens if CLARITY Fails](https://www.nydig.com/research/what-happens-if-clarity-fails) — Loper Bright durability analysis, §404
- [crypto.news: The stablecoin yield loophole — Banks vs the CLARITY Act](https://crypto.news/the-stablecoin-yield-loophole-banks-vs-the-clarity-act/) — §404, ABA position
- [Circle Launches Arc Mainnet](https://www.circle.com/pressroom/circle-launches-arc-mainnet-an-economic-operating-system-for-the-internet) — validators, 10B ARC mint, USDC gas
- [The Block: Circle launches Arc mainnet with BlackRock and Visa among validators](https://www.theblock.co/news/ecosystems/2026-09-16-circle-launches-arc-mainnet-with-blackrock-and-visa-among-validators-mints-10-billion-arc-tokens-415250)
- [The Block: Circle raises $222M in Arc token presale at $3B FDV](https://www.theblock.co/post/400709/circle-raises-222m-in-arc-token-presale-at-3b-fdv-from-a16z-crypto-blackrock-and-others-q1-revenue-up-20) — allocation 60/25/15
- [CNBC: Fed rate decision September 2026 — rates rise to 3.75%–4%](https://www.cnbc.com/2026/09/16/fed-rate-decision-september-2026.html)
- [NPR: The Fed raises interest rates for the first time in over three years](https://www.npr.org/2026/09/16/nx-s1-5968724/federal-reserve-interest-rates-inflation-economy)
- [StockAnalysis: CRCL forecast and price targets](https://stockanalysis.com/stocks/crcl/forecast/) — 28 analysts, $37–$243
- [MarketScreener: CRCL consensus](https://www.marketscreener.com/quote/stock/CIRCLE-INTERNET-GROUP-INC-189646796/consensus/) — Morgan Stanley $38 UW, KBW $105
- [Benzinga: The Curious Case Of Circle Stock](https://benzinga.com/z/46322945) — bull/bear firm targets
- [CoinCentral: Circle stock drops 7% after Senate kills crypto bill](https://coincentral.com/circle-crcl-stock-drops-7-after-senate-kills-crypto-bill-but-analysts-stay-bullish) — TD Cowen $92
- [TheStreet: Bernstein says Circle investors are focusing on wrong risks](https://www.thestreet.com/crypto/markets/bernstein-says-circle-investors-are-focusing-on-wrong-risks) — $140 PT
- [Decrypt: Coinbase takes 50% share of Circle's residual USDC reserve revenue](https://decrypt.co/312757/coinbase-circles-residual-usdc-reserve-revenue-filing)
- [CoinReporter: Coinbase and Circle expand USDC revenue-sharing](https://www.coinreporter.io/2026/08/coinbase-and-circle-expand-usdc-revenue-sharing-arrangement/)
