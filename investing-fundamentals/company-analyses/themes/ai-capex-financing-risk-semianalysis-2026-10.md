---
title: "AI Capex, Financing, and Financial Risk: The SemiAnalysis View (October 2026)"
created: 2026-10-09
updated: 2026-10-09
type: concept
tags: [thesis, framework, infrastructure, cloud, credit, bonds, risk, valuation, positioning]
sources: ["https://youtu.be/XlnyFCviN4o", "https://youtu.be/NcqHQmpNjr0", "https://youtu.be/LwMtHI7BHWI", "investing-macro/podcasts/sa-whos-funding-the-11-trillion-ai-buildout-20261009.md", "investing-macro/podcasts/sa-fight-for-fast-tokens-tpu-v7-vera-rubin-engrams-20261002.md", "investing-macro/podcasts/btp-can-ai-keep-growing-exponentially-semianalysis-20261009.md"]
confidence: medium
contested: true
---

# AI Capex, Financing, and Financial Risk: The SemiAnalysis View (October 2026)

An industry theme built from three SemiAnalysis discussions recorded between October 2 and October 9, 2026:

| Short name | Episode | Speakers | Focus |
|---|---|---|---|
| **Ep. 034** | [[sa-fight-for-fast-tokens-tpu-v7-vera-rubin-engrams-20261002]] | Nanos with the InferenceX team (Quilici, Shan, Ibarra) | Serving costs, margins, and hardware |
| **Ep. 037** | [[sa-whos-funding-the-11-trillion-ai-buildout-20261009]] | Daniel Nishball, Jordan Nanos | Debt markets, backstops, residual values |
| **BTP** | [[btp-can-ai-keep-growing-exponentially-semianalysis-20261009]] | Dylan Patel, Jordan Nanos (with Alex Kantrowitz) | Scale, revenue needed, company-level risk |

All three come from one firm that sells data, ratings, and models to the companies and lenders it describes. Read this page as a well-informed bull case to test, not as a neutral survey. The bear views it argues against are listed in §8.

---

## Bottom line

1. **The constraint has moved from chips to data centers to money.** Memory (HBM) is still tight, and data-center capacity should balance by 2027–28. Financing is the new limit: ~$7T of AI debt by 2029, against a US high-yield market that issues ~$400B a year.
2. **SemiAnalysis's case on demand and unit economics is strong.** Four-year-old H100s rent for more than they did a year ago. API serving runs ~75–90% gross margins. Anthropic is said to cover its compute costs. These are the firm's own models, but they agree across three teams.
3. **The bull and bear revenue math is closer than the rhetoric.** Patel's own rule of thumb ($1T of capex needs ~$250B a year of revenue) applied to SemiAnalysis's $11.3T capex estimate gives ~$2.8T a year. Patel says $3T of AI revenue in 2031 would mean "big problems." Brookings puts the requirement at ~$3.7T by 2032. Both sides are arguing about whether ~$3T of annual AI revenue shows up around 2031, from low hundreds of billions today.
4. **The GPU rental price ties the risk together.** Neocloud margins, lender IRRs, residual values, and Nvidia's rent-back guarantees all assume today's high rents roughly hold. A fall in rents would hit every one of them at the same time.
5. **The losses, if they come, land on specific companies before the system.** In order: leveraged neoclouds and the long tail, Oracle (fixed margins, debt, delays), Nvidia's contingent book, then hyperscaler multiples. Meta, Amazon, and Microsoft can stop spending and stay solvent.
6. **Backstops are a bridge with a known length.** Nvidia's balance sheet can guarantee ~46GW against ~240GW coming. Lenders must learn to take AI risk without a hyperscaler or Nvidia standing behind it. Nishball calls this "the biggest question of our time."

---

## 1. The organizing frame: willingness vs ability

Nishball (Ep. 037) splits the debate in two:

- **Willingness:** do end users get enough value, and are margins high enough, that someone will pay for the capacity?
- **Ability:** can the capital markets supply the money fast enough?

SemiAnalysis answers "yes" on willingness with data (§3) and "not yet clear" on ability (§4–§5). Most of the public bubble debate mixes the two. Klement, for example, argues from depleted free cash flow and debt costs (ability) to a conclusion that returns won't arrive (willingness). Keeping the two apart makes it clearer which data would change the view.

**How the constraint moved** (Ep. 037):

| Phase | Binding constraint | Status, October 2026 |
|---|---|---|
| 2024–25 | Chips, especially memory | Still tight. AI takes ~70% of DRAM wafers; Nvidia "despec'd" Vera Rubin to ship racks at all (Ep. 037). HBM shapes model design itself (Ep. 034). |
| 2025–26 | Powered data-center sites | Easing. Site activations, refurbishments, behind-the-meter power; "much more balanced" by 2027–28. Site-specific delays persist (Oracle New Mexico). |
| 2026 onward | Financing | Binding. "A constraint people have learned about in just the last few months." |

---

## 2. How big is the buildout?

| Measure | Figure | Source | Scope note |
|---|---|---|---|
| Cumulative AI capex, 2024–2029 | **$11.3T** | Ep. 037 | Chips and racks (incl. TPU, Trainium) plus data centers; excludes power plants and fabs; includes neoclouds and developers |
| US capex next year | **~$2T, 5–6% of GDP** | BTP (Patel) | Full supply chain |
| Popular chart | 3.6% of GDP for AI vs 2.2% for railroads | BTP (cited) | Median annual share |
| Brookings / Van Nieuwerburgh | $10.3T, 3.63% of GDP | [[brookings-financing-ai-buildout-van-nieuwerburgh-2026-09]] | Project-level capacity model |
| Hyperscaler capex growth | **+116% YoY in Q3 2026**; consensus <100% in Q4, ~70% in Q1 2027 | BTP | Growth rate, not level |
| Global data-center capacity added | ~40GW a year now, ~60GW a year by 2029 | Ep. 037 | |

**What to take from this:**
- The cumulative estimates converge (~$10–11T), so scale isn't the main disagreement. The GDP share differs because Patel counts the supply chain and next year's run rate, while the 3.6% figure is a multi-year median.
- **US capex serves foreign demand** (BTP). Most of Anthropic's and OpenAI's European inference runs in US data centers. Comparisons with railroads, which served domestic traffic, overstate how much US GDP has to support the buildout.
- **Capex growth slowing is consensus.** Going from +116% to ~70% is arithmetic, not a demand break. Nanos expects real limits late in 2027: organizing another gigawatt on top of existing projects, and raising trillions.

---

## 3. Willingness: the return side

### 3a. Prices are rising, not falling

- **H100 one-year rentals** bottomed near **~$1.30/hr** in fall 2025. Some renewed at ~$2.50, and one-year terms now sit near **~$3/hr**, close to H1 2023 signing levels (Ep. 037).
- SemiAnalysis's theoretical rental curve, which assumes rents fall as newer chips arrive, tracked actual prices within ~2% for 18 months and then broke in September–October 2025. Sold-out GB300 and B200/B300 capacity pushed demand down to older Hopper chips.
- **Token prices** are rising on a blended dollars-per-million-tokens basis (Ep. 037). Throughput per GPU is rising too, so margins widen even at flat prices.
- Nanos expects four-year-old H100s to rent for *more* next year.

### 3b. Margins at each layer

The three episodes quote several margin figures. They measure different things and fit together:

| Figure | What it measures | Source |
|---|---|---|
| ~90% | Frontier-lab **API gross margin**: ~$38/hr of token revenue per GB300 vs ~$2.80/hr cost of ownership | Ep. 037 |
| ~75%, higher on frontier models | **Anthropic inference gross margin** (compare Salesforce ~75%) | BTP |
| ~80% | **Gross margin serving Chinese open models** on GB300 NVL72 | Ep. 037 |
| ~40–50% | **Profit margin serving open models** after a 30% model license fee and 60% utilization (Kimi K3: ~40.7% on GB200, ~50% on GB300) | Ep. 034 |
| 50–60% | Margin on **flat-rate subscriptions** (heavy users lose money) | Ep. 037 |
| ~9% | **Server OEMs**, still in a price war | Ep. 037 |

**Per megawatt** (Ep. 037): frontier-token revenue can reach ~$100M per MW per year at optimistic utilization, against ~$40M per MW to build. Neoclouds were renting GB300s at ~$12M per MW a few months ago. Nishball calls the $100M figure "a little optimistic."

### 3c. Lab revenue and profitability (BTP)

- Anthropic grew from **under $10B to over $100B** of revenue this year (~10x).
- Patel forecasts **$600–700B combined run rate for OpenAI plus Anthropic by December 2027**, possibly higher.
- Anthropic covers training plus inference compute today; OpenAI gets there in "two or three" quarters.
- Customer acquisition cost is near zero (vs up to ~30% of revenue at SaaS companies). R&D grows slower than revenue.
- Amazon's AI infrastructure is "profitable today"; Bedrock lifted gross margin last quarter.

### 3d. The revenue requirement: where bulls and bears actually differ

| View | Revenue needed | Basis |
|---|---|---|
| Bain | $6T a year by 2031 | Hyperscaler break-even |
| Brookings / Van Nieuwerburgh | ~$3.5–3.7T a year by 2032 (8.8–9.2% of GDP) | 10% required return, 50% operating cash-flow margin, 6-year IT life |
| Patel rule of thumb | ~$250B a year per $1T of capex | $1.5T of revenue over 6 years, back-loaded |
| **Patel's rule × $11.3T** | **~$2.8T a year** | This page's arithmetic, not a figure he gave. Overstates the need slightly because data centers last ~15 years, not 6 |
| Patel's danger line | "If AI revenue is only $3 trillion in 2031… big problems" | BTP |

Patel's danger line sits close to what his own rule implies and not far below Brookings. The disagreement is mostly about **pace**: whether revenue that went up ~10x this year compounds fast enough to reach ~$3T by 2031. Patel's December 2027 forecast ($600–700B for two labs) would put the industry about a quarter of the way there with four years left. If lab revenue misses that path by a wide margin in 2027, the bull case loses its main support.

**Where the money comes from** (BTP): corporate R&D and COGS budgets moving to AI, and capital taking share from labor. Patel's example is US chip-design headcount, flat for 20 years while the industry's value exploded.

---

## 4. Ability: the financing side

### 4a. How much debt, against which markets

| Item | Figure | Source |
|---|---|---|
| AI debt outstanding by 2029 | **~$7T** | Ep. 037 |
| Net new AI debt in 2026 | **~$1T** (~$500B through June; ~$400B June 1–Oct 7) | Ep. 037 |
| US IG issuance | ~$3T a year | Ep. 037 |
| US high yield | ~$400B a year | Ep. 037 |
| US leveraged loans | ~$400B a year | Ep. 037 |
| Total US issuance | ~$12.7T, incl. ~$5–6T Treasuries | Ep. 037 |
| AI debt share of issuance | "2026 is the last year it is under 10%" | Ep. 037 |
| AI debt vs other US asset-backed credit | Passed auto loans and student loans in 2026; second only to agency MBS | Ep. 037 |

A new borrower class raising ~$1T a year, more than the whole high-yield market, competes with Treasuries and corporates for the same buyers. That is the supply mechanism behind [[ax-brij-khurana-wellington-ai-capex-crowding-out-bonds-20261001]] and [[bond-supply-tsunami-2026]].

### 4b. "Balance sheet as a service"

Lenders will finance a cluster only against a **five-year offtake from an investment-grade buyer**. OpenAI and Anthropic aren't rated, so a hyperscaler or Nvidia sits in the middle (Ep. 037):

- **Example:** Nscale sells capacity to Microsoft, which resells it to OpenAI. If OpenAI doesn't pay, Microsoft does, so Nscale can borrow against Microsoft's credit.
- **Accounting:** many such deals are booked as service contracts (ASC 606) instead of leases (ASC 842), so they stay off the balance sheet. Nishball expects rating agencies to "see through this stuff."
- **Cost passes to buyers:** GB300 capacity requires picking a provider six months ahead and **prepaying 30–50%** of contract value.

### 4c. The credit market is already charging for it

| Name | Spread signal | Source |
|---|---|---|
| Amazon | $25B six-tranche July deal priced "well wide" of its curve; 10-year Z-spread ~100bp at issue, now ~100–110bp | Ep. 037 |
| Oracle | Whole curve +30–50bp since summer; 10-year ~250bp Z-spread | Ep. 037 |
| CoreWeave | ~400bp on SemiAnalysis's chart | Ep. 037 |
| CoreWeave–Meta project loan | SOFR + 225bp vs Meta 5-year ~97bp; the ~100bp gap is the price of execution risk | Ep. 037 |

Spread widening appeared at Oracle and on Amazon's new issues before any sign of weaker demand. On SemiAnalysis's reading, AI stress is showing up first as a **funding-cost** problem, not a revenue problem.

---

## 5. Nvidia as financier

Nvidia now guarantees much of the debt that buys its own chips.

| Item | Figure | Source |
|---|---|---|
| Off-balance-sheet commitments tracked | **$497B** (early Sept) → **$588B** (Oct 9) | Ep. 037; BTP |
| Pace of new backstops | ~$100B a month | Ep. 037 |
| AICP rent-back floor | ~$3.25/GPU-hr average over six years; Nvidia takes **50%** of revenue above the floor | Ep. 037 |
| AICP floor in July | $2.33–2.36/hr with a 40% share | [[semianalysis-research-2026-07]] |
| Ports Pike residual-value guarantees | $105B, tied to 4.25GW (up to ~9GW) | Ep. 037 |
| Capacity Nvidia's balance sheet can support | **~46GW**, vs ~240GW coming | Ep. 037 |
| Nvidia revenue | Nearing ~$500B (~2.5% of US M2) | BTP |

**The bull reading** (Nanos, BTP): Nvidia signs as the creditworthy buyer so neoclouds can borrow. When capacity comes online someone else usually wants it at a higher price, so Nvidia resells and moves on. It also wants customers beyond three or four hyperscalers.

**The risk reading:** the structure works while rents exceed the floor. The floor rose ~40% since July as rents rose, so Nvidia is underwriting at higher prices. If rents fall below the floor, Nvidia pays the difference and gets no revenue share, and residual-value guarantees become liabilities. Nvidia's earnings would then fall at the same time as its guarantee payments rise. When valuing NVDA, the $588B belongs next to its balance sheet, not in a footnote.

---

## 6. Who holds the risk: contract structure

### 6a. Binding vs flexible commitments (BTP)

- **Neocloud offtakes** run **5–6 years**, take the full capacity at fixed hourly rates, and can't be cancelled at will. They are binding.
- **Self-built hyperscaler campuses** are flexible. Meta can leave a shell empty for years because the building is a small share of total cost.

So when demand slows, hyperscalers can cut their *own* builds first and still owe the neoclouds. That pushes the first losses to neocloud lenders and equity, and it means the 2027–28 take-or-pay obligations in [[ai-compute-commencement-wall-and-refinancing-trap]] are firmer on the neocloud side than on the self-build side.

### 6b. Lenders underwrite to zero residual value

Most projects are underwritten to a **20–30%+ IRR over 5–6 years with no residual value** (Ep. 037). Value after year five "is like a bonus." This protects senior lenders more than the headline scale suggests: their losses come from rents falling *during* the contract or from a counterparty failing, not from GPUs being worth less at the end.

### 6c. Contract length decides who gains from rising rents (BTP)

| Provider | Contract profile | Effect |
|---|---|---|
| Nebius | Shortest average contracts of the top clouds | Able to "really jack up pricing" |
| CoreWeave | Long-term contracts | Captured less of the rent increase |
| Oracle | Fixed-margin OpenAI deals signed ~a year ago | Can't benefit from higher rents |

The same structure works in reverse: if rents fall, long fixed contracts protect CoreWeave and Oracle, and Nebius reprices down. Contract length is a bet on the direction of rents.

### 6d. Execution is where single names break

- **Oracle:** high service quality (second ClusterMAX tier) but heavy debt, fixed margins, and the **New Mexico site delayed potentially years** for lack of gas pipelines, with force majeure declared. Wisconsin is delayed too (BTP; see [[burry-ai-capital-cycle-oracle-jupiter-2026-09]]).
- **Neocloud security** (BTP): Chinese open models such as GLM 5.3 "can just hack dozens of the neoclouds." SemiAnalysis saw another tenant's jobs on one cloud, including a foreign government security agency's. A breach at a provider with sovereign customers could cost it contracts, and a cancelled contract weakens the collateral its lenders rely on.
- **Long tail:** SemiAnalysis tracks 323 providers. The "not recommended" group has more names than the top four tiers combined.

---

## 7. Technology shifts that change the financing math

Hardware and software changes feed straight into depreciation lives, residual values, and which suppliers win.

- **Vera Rubin ~3x Blackwell** at ~100 tokens/sec per user, ~1.4x at max throughput, at less than 2x the price (Ep. 034). That gives operators a clear reason to upgrade. It also argues for **faster economic obsolescence of Blackwell**, which cuts against the rising-H100-rent evidence. So far scarcity has outweighed obsolescence. Once supply catches up, the 3x gain will push older-chip rents down.
- **TPU v7 posts the lowest cost per token** against B200/B300, PyTorch-on-TPU is coming, and TPUs are entering neoclouds (Ep. 034). Over time that is a second supplier for lenders and a pricing check on Nvidia.
- **Google sells compute at DeepMind's expense** (BTP). DeepMind will have the least compute of the three frontier labs by year end, while OpenAI and Anthropic each add 5–10GW next year. Alphabet looks increasingly like an infrastructure seller.
- **HBM shapes model design** (Ep. 034). Engrams and KV-cache offloading move work to DRAM and SSD, raising memory and flash content per server.
- **Fast tokens are a niche** (Ep. 034). Tool calls, not decoding speed, slow agents down, and GPU mega-kernels (TileRT, ~200–500 tokens/sec) compete with specialist silicon. Specialist chipmakers are financed on the shortage, not on a proven long-term edge.

---

## 8. Where SemiAnalysis disagrees with the bears

| Bear view | Their claim | SemiAnalysis response | Still unresolved |
|---|---|---|---|
| [[klement-ai-bubble-2027-forecast-20261008]] | FCF depleted, debt "prohibitive"; bubble bursts 2027–28; S&P 5,000 | Agrees financing is the constraint; disagrees on ability to pay because unit economics are strong | Whether equity investors keep paying for it while spreads widen |
| [[brookings-financing-ai-buildout-van-nieuwerburgh-2026-09]] | ~$3.7T of annual revenue needed by 2032 | Patel calls the numbers too low, but his own danger line is ~$3T in 2031 | Revenue path 2027–31 (§3d) |
| [[ubp-financing-ai-build-out-2026-09]] | ~$2.9T off balance sheet; ~12x commitments to lab ARR; Oracle the weak link | Agrees on Oracle and on accounting; sees lab revenue growing into commitments | Whether rating agencies treat take-or-pay as debt |
| [[burry-ai-capital-cycle-oracle-jupiter-2026-09]] | Write-offs 2028–29; Oracle stress | Agrees on Oracle execution; sees rising rents as evidence against write-offs | Depreciation lives once supply catches up (§7) |
| Ed Zitron (BTP, cited) | Nvidia funds its own demand | Backstops are resold at higher prices; internal use is tiny | Guarantee exposure if resale prices fall |
| [[ai-compute-commencement-wall-and-refinancing-trap]] | 2027–28 payment wall; losses on neoclouds and private credit | Neocloud offtakes are binding; demand exceeds supply | Same direction on who bears losses |

Every bear view and SemiAnalysis's view converge on where stress shows up first: Oracle, neoclouds, and private credit. They differ on how likely it is and how big.

---

## 9. Risk framework

Ranked by severity × probability over the next 2–3 years. This ranking is this page's judgment, built from the three episodes.

| # | Risk | Trigger | What breaks first | Early signal |
|---|---|---|---|---|
| 1 | **Financing capacity outruns backstops** | Debt need passes what hyperscalers and Nvidia can guarantee (~46GW of Nvidia capacity vs ~240GW coming) | Non-IG neocloud raises, convert-heavy funding, wider spreads | New-issue concessions; CoreWeave and Oracle spreads; share of deals without a backstop |
| 2 | **GPU rental prices reverse** | Rubin and TPU supply catch up with demand; 3x per-chip gain hits older-chip rents | Nebius-style short-contract margins, AICP floors, residual-value guarantees | One-year H100 and GB300 rental indices; OpenRouter token prices |
| 3 | **Execution and delays** | Power, gas pipelines, moratoriums, construction | Single names: Oracle New Mexico and Wisconsin; project loans serviced from reserves | Force majeure notices; energization dates vs contract |
| 4 | **Lab counterparty concentration** | OpenAI or Anthropic revenue misses the $600–700B path | Hyperscalers' resale guarantees; Oracle's OpenAI backlog | Lab run-rate disclosures; Anthropic IPO filing |
| 5 | **Accounting re-rating** | Agencies treat ASC 606 service deals and take-or-pay as debt | Hyperscaler leverage metrics and multiples, Oracle first | Rating-agency methodology notes |
| 6 | **Security incident at a neocloud** | Model-assisted breach or tenant data exposure | Provider contracts with sovereign and enterprise customers | Disclosed incidents; ClusterMAX security scores |
| 7 | **Enterprise adoption stalls** | Fortune 500 "lack of imagination" (Nishball) persists | Revenue path beyond coding and consumer | Enterprise seat and API spend data |
| 8 | **Political backlash over distribution of gains** | Capital share rises fast, labor income stagnates (Patel's own worry) | Regulation, taxes, or permitting | Policy proposals on AI rents and data-center permits |

**Pre-mortem.** If this theme is wrong in three years, the most likely reason is risk 2 setting off risk 1. Rubin and TPU capacity arrive in volume in 2027 and rents fall. Neocloud margins and Nvidia's rent-back floors come under pressure together, and lenders who had been relying on backstops stop extending new credit right when the 2027–28 payment wall arrives. Demand could keep growing through all of this. The problem would be that prices fall faster than the debt was underwritten to allow.

**What must hold for the bull case:**
- Rents stay above underwriting levels through 2028.
- OpenAI plus Anthropic reach roughly $600–700B of run rate by end-2027.
- Credit markets learn to underwrite neocloud execution risk without a guarantor.
- No major lab defaults on a backstopped offtake.

---

## 10. Public-market positioning by layer

| Layer | Names | View | Why | Main risk |
|---|---|---|---|---|
| Memory | SK Hynix, Samsung, Micron (MU) | Bullish | HBM binding; DRAM/SSD content per server rising (Ep. 034, 037) | Memory cycle turns once despec'd products catch up |
| Accelerators | Nvidia (NVDA) | Bullish, with rising contingent exposure | Rubin 3x at <2x price; revenue ~$500B; 50% share above floors | $588B of backstops become liabilities if rents fall |
| Custom silicon | Alphabet (GOOGL), Broadcom (AVGO) | Bullish | TPU v7 cost lead; neocloud distribution; $24B + $6B TPU financing | DeepMind's falling compute share weakens Google's own model position |
| Hyperscalers | Amazon (AMZN) | Bullish | AI infrastructure already profitable | Lab counterparty risk; new-issue spreads |
| Hyperscalers | Meta (META), Microsoft (MSFT) | Neutral, watch credit | Solvent and can stop buying; backstopping others' deals | Off-balance-sheet re-rating |
| Cloud | Oracle (ORCL) | Cautious on the stock | Good service | Fixed margins, debt, New Mexico force majeure; widest IG curve |
| Neoclouds | Nebius (NBIS) | Bullish while rents rise | Short contracts reprice upward | Same contracts reprice down if rents fall |
| Neoclouds | CoreWeave (CRWV) | Neutral | Top-tier quality; long contracts protect downside | Convert dilution; ~400bp spreads; capped upside |
| Long-tail neoclouds, bitcoin-miner hosts | Hut 8 (HUT), others | Bearish to mixed | Seller's market hides weak security and reliability | Need IG offtake to borrow |
| Server OEMs | — | Bearish on margins | ~9% margins in a price war | — |
| Fast-inference silicon | Cerebras, others | Cautious | Funded by shortage | GPU software closes the speed gap |
| Credit / duration | IG tech credit, long Treasuries | Cautious | ~$1T a year of new AI supply; AI debt heading above 10% of issuance | Spread widening spreading from Oracle to AA names |

**Portfolio implications:**
- Treat **credit spreads as the early warning** for AI equities. On this evidence, funding costs will move before demand does.
- **Contract length** is the main way to distinguish neocloud equities. Pick based on your view of where rents go.
- Value **Nvidia partly as a lender**. Track the backstop total every quarter against revenue and cash.
- Be careful adding **long duration** while AI issuance is growing toward 10% of US issuance.

---

## 11. Dashboard: what to track

Current values come from the three episodes. The red-flag levels are this page's proposals, not SemiAnalysis figures.

| Indicator | Current (Oct 2026) | Red flag | Frequency / source |
|---|---|---|---|
| One-year H100 rental | ~$3/hr | Back toward ~$2/hr | Monthly; SemiAnalysis GPU rental index |
| AICP rent-back floor | ~$3.25/hr, 50% share | Spot GB-class rents near the floor | Per program; Nvidia disclosures, SemiAnalysis |
| Nvidia tracked backstops | $588B | Growth faster than revenue for several quarters, or first payout | Monthly; SemiAnalysis; NVDA 10-Q footnotes |
| Net new AI debt | ~$1T in 2026 | Rising issuance with widening concessions | Monthly; deal flow |
| Oracle 10-year Z-spread | ~250bp | Further widening while peers hold | Daily; TRACE/Bloomberg |
| Amazon 10-year Z-spread | ~100–110bp | Sustained >130bp | Daily |
| CoreWeave spread | ~400bp | >600bp | Daily |
| Hyperscaler capex growth | +116% YoY (Q3) | Level of capex falling, not just growth rate | Quarterly earnings |
| OpenAI + Anthropic run rate | Anthropic >$100B | Combined well short of $600–700B by Dec 2027 | Company disclosures; Anthropic IPO filing |
| Blended token prices | Rising | Sustained declines on frontier and open models | OpenRouter |
| Data-center energization | Site-specific delays | More force majeure notices | Company filings, local permits |

---

## Caveats

- **One firm, three teams.** The views agree partly because they draw on the same SemiAnalysis models (TCO, tokenomics, rental index). They don't confirm each other independently.
- **Commercial incentives.** SemiAnalysis sells ClusterMAX, TCO models, and data to lenders and operators, and is launching a credit group. Patel calls himself "extremely bullish" on Anthropic.
- **Model-dependent figures.** Lab revenue forecasts, margins, and the 46GW backstop limit are SemiAnalysis estimates, not company disclosures.
- **The ~$2.8T figure in §3d** is this page's application of Patel's rule to Ep. 037's capex total, not something either speaker said.
- **Transcript quality.** All three sources are YouTube auto-captions. Product names and a few numbers were reconciled against the speakers' own arithmetic; see each episode note's caveats.

## Cross-references

- Episode notes: [[sa-whos-funding-the-11-trillion-ai-buildout-20261009]], [[sa-fight-for-fast-tokens-tpu-v7-vera-rubin-engrams-20261002]], [[btp-can-ai-keep-growing-exponentially-semianalysis-20261009]]
- Payment timing: [[ai-compute-commencement-wall-and-refinancing-trap]]
- Bear and academic views: [[klement-ai-bubble-2027-forecast-20261008]], [[brookings-financing-ai-buildout-van-nieuwerburgh-2026-09]], [[ubp-financing-ai-build-out-2026-09]], [[burry-ai-capital-cycle-oracle-jupiter-2026-09]]
- Bond supply: [[ax-brij-khurana-wellington-ai-capex-crowding-out-bonds-20261001]], [[bond-supply-tsunami-2026]]
- Earlier SemiAnalysis coverage: [[semianalysis-research-2026-07]], [[semianalysis-research-2026-06]]
- Hardware: [[deepseek-v4-1-flash-memory-bottlenecks]], [[ai-inference-costs-accounting]]
