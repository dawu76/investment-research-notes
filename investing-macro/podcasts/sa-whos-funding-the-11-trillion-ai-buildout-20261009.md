---
title: "Who's Funding the $11 Trillion AI Buildout? (Capital Markets) | SemiAnalysis Weekly Ep. 037"
created: 2026-10-09
updated: 2026-10-09
type: concept
tags: [macro, credit, bonds, rates, infrastructure, cloud, valuation, risk]
sources: ["https://youtu.be/XlnyFCviN4o"]
confidence: medium
contested: true
---

# Who's Funding the $11 Trillion AI Buildout? | SemiAnalysis Weekly Ep. 037

**Speakers:** Daniel Nishball (SemiAnalysis; leads its new Compute Capital Markets group) and Jordan Nanos (SemiAnalysis; ClusterMAX ratings and GPU rental data). Released October 9, 2026; 83 minutes. Recorded around October 7, per Nishball.

## I. Executive Summary

SemiAnalysis argues that the binding constraint on AI infrastructure has moved from chips (memory) to data centers and now to **financing**. They estimate **$11.3T of cumulative AI IT and data-center capex from 2024 to 2029**, about **$7T of it debt-funded**. Today almost all of that debt is underwritten against investment-grade backstops from hyperscalers and Nvidia, whose off-balance-sheet commitments now total **$497B**. They are bullish on demand and profitability: H100 rental prices are *rising* on four-year-old chips, and frontier-model API serving runs at ~90% gross margin. Their worry is whether lenders can learn to take AI risk *without* a backstop, because Nvidia's balance sheet can support ~46GW against ~240GW of capacity coming.

**Sentiment:** bullish on demand, cautious on credit-market capacity. Note that SemiAnalysis sells data and ratings to lenders and is hiring a credit team. Read the "lenders need better tools" conclusion with that in mind.

## The questions the speakers are trying to answer

1. **Who is funding the $11T buildout, and can the debt markets absorb it?** This is the "funding wall."
2. **Why are Nvidia and the hyperscalers backstopping other companies' debt, and how far can that go?** This is "balance sheet as a service."
3. **How should lenders price credit risk for a neocloud whose customer is investment grade?** Their answer: the gap is execution risk, which ClusterMAX ratings can help measure.
4. **What is a GPU worth after its five-year life, and why did H100 rental prices *rise*?** This is the residual-value problem that lenders can't yet model.
5. **Is each token profitable?** Nishball frames the whole debate as **willingness** (do end users get enough value, are margins high enough) versus **ability** (can the capital markets supply the money).
6. **Will lenders take AI risk outside of backstops before the backstops run out?**

## II. Timestamps & Agenda

- **0:00 Cold open.** Launch of SemiAnalysis's Compute Capital Markets group and credit-analyst hiring.
- **1:48 Nvidia's backstop universe.** Constraints migrating from compute to data center to financing; the "AI project trinity" of capital, offtake, and data center.
- **6:22 The $11T funding wall.** How $1T a year of hyperscaler capex becomes $11.3T; $7T of debt by 2029; who is raising what since June.
- **17:25 Balance sheet as a service.** Why Microsoft or Meta backstops a neocloud deal; ASC 606 service contracts vs ASC 842 leases; Amazon and Oracle spreads.
- **26:27 ClusterMAX as credit risk.** Breaking a CoreWeave–Meta project loan into Meta credit risk plus execution risk.
- **31:51 Why H100 prices rose.** One-year H100 rentals back near $3/hr; the theoretical depreciation curve broke in late 2025.
- **43:09 Token profitability.** The income statement from lab to neocloud to chip; ~90% API gross margin; token prices rising, not falling.
- **58:05 You can't go back.** Consumer and agent adoption; enterprise adoption as the open question.
- **1:07:25 AI debt vs auto loans.** AI debt passed auto and student loans in 2026; 2026 is the last year it is under 10% of all US issuance.
- **1:11:14 Inside Nvidia's backstops.** The AICP rent-back program, the Lambda lease, Ports Pike residual-value guarantees, a $500B tranched capital partnership; Nvidia can support ~46GW of the ~240GW coming.

## III. Detailed Key Takeaways

### 1. The constraint has moved to financing

Nishball's sequence: compute was the first pinch point, especially memory. AI was set to take ~70% of DRAM wafers, and Nvidia "despec'd" Vera Rubin, cutting memory to contain cost and, more importantly, to have enough memory to ship racks at all. Data-center capacity was the next worry, but powered-site activation, refurbishments, and behind-the-meter generation mean that "by 2027–28 it's much more balanced." The new constraint is money, "a constraint people have learned about in just the last few months."

- **$11.3T** is cumulative 2024–2029 capex: GPU and XPU shipments (including TPUs and Trainium) multiplied by full rack cost, plus data-center construction. Much of that capex sits with independent data-center developers and neoclouds, not the hyperscalers. That is how ~$1T a year of hyperscaler capex becomes $11T in total. It excludes power plants and fab equipment.
- **~$7T of AI debt outstanding by 2029.** About **$1T of net new AI debt in 2026**: ~$500B raised through June, then **~$400B from June 1 to October 7** (~$260B documented, ~$150B reported but not yet documented). "I would expect that this estimate will probably creep up."
- **Scale against existing markets:** US investment-grade issuance is ~$3T a year, high-yield bonds ~$400B, leveraged loans ~$400B. Total US issuance is ~$12.7T, including ~$5–6T of Treasuries. **"2026 is the last year that AI debt is going to be less than 10% of all issuance."**

> "It's like a zombie apocalypse but you don't know how many waves of zombies are coming… you don't know whether you're on wave five or wave 50." (Nishball, on the credit market's view of AI issuance)

**Why it matters:** this sizes the duration supply behind [[ax-brij-khurana-wellington-ai-capex-crowding-out-bonds-20261001]]'s crowding-out thesis. A new borrower class issuing ~$1T a year, more than the whole high-yield market, competes with Treasuries and corporates for the same buyers.

### 2. Deal flow since June (examples cited)

| Borrower / deal | Size | Structure | Backstop / note |
|---|---|---|---|
| Broadcom–Google–Anthropic TPU deal ("Blue Sky") | $24B | plus $6B delayed-draw term loan | Hyperscaler-linked |
| Meta–BlackRock El Paso JV | $12.5B | Project financing | Meta residual-value guarantee |
| Anthropic | $15B | Revolver | Not IG-rated |
| Hut 8 | $4.25B | Debt | Bitcoin miner turned AI host |
| CoreWeave | $4.2B convert; $2.6B DDTL (Aug) | Convert + term loan | High yield |
| Nebius (NBIS) | $3.5B | Convertible | — |
| Asian neocloud | $3B | Term loan | "One of the first in Asia" |

Names of some deals are garbled in the auto-captions; sizes are as spoken.

### 3. "Balance sheet as a service": why hyperscalers and Nvidia backstop

Lenders will only finance a cluster against a **five-year offtake from an investment-grade counterparty**. OpenAI and Anthropic aren't rated, so the hyperscaler stands in the middle. In a Microsoft–Nscale–OpenAI deal, Nscale sells capacity to Microsoft, which resells it to OpenAI. If OpenAI doesn't pay, Microsoft is on the hook, and Nscale can raise a construction loan against Microsoft's credit.

- **Accounting:** many of these arrangements are booked as service contracts under **ASC 606** rather than leases under **ASC 842**, so they stay off the balance sheet. "If it talks like a duck, quacks like a duck, it's a duck." Rating agencies and investors "will see through this stuff," and there is a limit: "how are you going to backstop $3 trillion?"
- **The market is already pricing it:**
  - Amazon's six-tranche **$25B** July deal priced "well wide" of its curve. It was the "canary in the coal mine." Amazon's 10-year Z-spread was ~100bp at issue (5-year ~65bp), widened 10–20bp over the summer, and sits ~100–110bp now.
  - **Oracle's whole curve is up ~30–50bp since summer**, with its 10-year near ~250bp Z-spread. Their chart shows Oracle +105bp and CoreWeave ~400bp.
- **Buyers pay for suppliers' cost of capital.** Getting GB300 capacity means picking a provider six months before delivery and **prepaying 30–50% of contract value**. That pushes labs toward self-builds until their own balance sheets max out, then back to backstopped third-party deals. Nanos compares this to an early-stage startup's behavior.

### 4. Pricing neocloud credit: customer risk plus execution risk

In a CoreWeave capacity deal with Meta, the lender is really taking **Meta credit risk plus execution risk**. Meta's 5-year Z-spread was ~97bp; the CoreWeave project loan priced at **SOFR + 225bp** (just under ~200bp Z-spread). The **~100bp difference is the price of execution**: standing the cluster up on time and keeping the contract from being cancelled.

Nishball argues SemiAnalysis's **ClusterMAX** operational ratings work as a credit signal; lenders on his New York and Singapore roadshow said it helped. Nanos pushes back: ClusterMAX rates *managed clusters*, while most debt finances *bare-metal* sites, and execution varies site by site. Neoclouds increasingly put each site in its own SPV, which he thinks is the right unit of analysis.

### 5. The residual-value puzzle: H100 rents went *up*

Banks lend against assets whose residual value they can model, like cars and property. GPUs break that model.

- SemiAnalysis's theoretical H100 rental curve, which falls as newer chips add capacity (GB300 has ~7x the inference throughput and ~3x the FLOPs), **tracked within ~2% for about 18 months**. Then it **dislocated in September–October 2025**.
- One-year H100 rentals bottomed near **~$1.30/hr** in fall 2025, with weaker providers weighing one year at $1.30 vs two years at $1.25. Some of those contracts have since **renewed at ~$2.50**, and one-year terms are now near **~$3/hr, close to H1 2023 signing levels**.
- **Why:** GB300 and B200/B300 are sold out with six-month waits, so demand "cascades down" to Hoppers. Some researchers also prefer H100s for numerical stability in training (BF16 vs FP8/FP4).
- Reading demand from price, the implied supply–demand balance "blew out completely in late 2025 and it's never looked back."
- Nanos expects four-year-old H100s to rent for *more* next year. Beyond better models, he cites data-center delays and moratoriums constraining supply, and more consumer usage even if models stop improving.

**For lenders:** most projects are underwritten to a **20–30%+ IRR over 5–6 years with no residual value assumed**. Any value after year five "is like a bonus."

> "Four-year-old H100s going into next year are going to be selling for likely higher prices than they are today if the trend continues." (Nanos)

### 6. Willingness: is each token profitable?

Nishball builds an income statement for a frontier lab:

| Layer | Per GB300 GPU-hour |
|---|---|
| Lab revenue (~$1.85 per million tokens blended, cache hits included) | ~$38/hr |
| Cost to rent from a neocloud | ~$4.50–5/hr |
| Cost to own (TCO) | ~$2.80/hr (~$2.13 capital, ~$0.66 operating) |
| Implied API gross margin | ~90% |

- **Per megawatt:**
  - Frontier-token revenue can reach **~$100M per MW per year** on GB300 at optimistic utilization.
  - That compares with **~$40M per MW to stand up** (GB300 IT ~$31–33M per MW plus data center ~$10M+ per MW), so payback is around half a year.
  - Neoclouds were renting GB300s at **~$12M per MW** a few months ago.
  - The **~$48M per MW** that SpaceX and Google reportedly paid "makes sense" given what the capacity earns.
- **Capex vs cost of ownership:** chips depreciate over 5 years and data centers over 15. Chips are ~75% of the cost of ownership but only ~60% of upfront capex, so data centers need more funding up front than TCO suggests.
- **Open models are profitable too:** providers serving Chinese open models (DeepSeek V4.x, GLM 5.3, Kimi K3) earn **~80% gross margins on GB300 NVL72**. Sparse attention and modest parameter growth let throughput per GPU rise while tokens become more valuable.
- **Token prices are rising, not falling,** on a blended dollars-per-million-tokens basis. Even flat prices mean expanding margins as throughput per GPU rises. Indices that track token spending don't adjust for the changing basket or for cache-heavy agentic usage.
- **Subscriptions:** their model assumes 50–60% margins on flat-rate plans versus ~90% on the API. Heavy users of flat-rate plans lose money for the provider (the "Planet Fitness" model), and in China, consumer plans are resold as gray-market API access.
- **Profit by layer:** Nvidia has durable margins, neocloud profitability has improved as rents rose against fixed costs, and labs' margins are expanding. Server OEMs are the exception, still in a price war at ~9% margins.

> "I don't view this as like an AI fast takeoff, but it seems to be like a revenue and profitability fast takeoff for a lot of these labs." (Nanos)

**Adoption:** both are convinced on AI-native users and expect Meta's Muse to prove the consumer case. Nishball calls **enterprise** the unknown: at Fortune 500 dinners he hears "a lack of discovery… and lack of imagination," with executives asking "how do I fire people." Nanos's answer is that legacy companies get replaced by AI-native ones. He notes 9 of the 10 largest companies by market cap are AI, semiconductor, or data-center related, and an Anthropic IPO at ~$2T would be a top-25 company.

### 7. Ability: the Nvidia backstop machine and its limit

Nvidia's **$497B of off-balance-sheet commitments** fall into seven categories: AI cloud agreements, data-center leases, guarantees and LP guarantees (energy), cloud services agreements, data-center leases for its own use, supply and capacity commitments (memory), and residual-value guarantees. SemiAnalysis assigns no value to the last category. New backstops are being announced at roughly **$100B a month**.

- **AICP rent-back program** (SharonAI and Firmus first, then GMI and others): Nvidia promises to rent a neocloud's cluster if it can't find customers, for **six years at an average floor of ~$3.25/GPU-hr** (the floor varies by year). In return it takes **50% of revenue above the floor**: at a $6.25 rent, $1.50 of every hour goes to Nvidia. The floor lets non-IG neoclouds borrow ("I'm really lending to Nvidia plus execution risk") and sell inference-as-a-service instead of only five-year offtakes. It is meant as a bridge while lenders learn churn and cancellation data.
- **Lambda:** Nvidia supports a data-center lease so Lambda can finance capacity for Anthropic, which isn't yet IG, and takes a revenue share.
- **Ports Pike:** **$105B of residual-value guarantees** in exchange for locking in Nvidia GPUs on 4.25GW, up to ~9GW across two phases. Part of the motive is a land grab.
- **$500B capital partnership (SemiAnalysis's model of how it could work):** a non-IG lab borrower; tranches of equity, a B-piece with no guarantee, and senior A1/A2 pieces; a **25% Nvidia residual-value guarantee** attached to chosen tranches. The structure creates separate risk products for banks and insurers, private credit, and private equity.
- **The limit:** on SemiAnalysis's projection of Nvidia's balance sheet, it can backstop **up to ~46GW**, versus **~240GW of capacity coming**. Hyperscaler capacity hasn't been modeled yet. "The lending market has to evolve to take risk outside of backstops… it's really the biggest question of our time."

**Context on scale:**
- **AI debt passed US auto loans and student loans in 2026** and is now second only to agency MBS among US asset-backed credit markets.
- Global data-center capacity was ~40GW when SemiAnalysis started tracking it; the world is now adding ~40GW a year, rising to ~60GW of incremental capacity in 2029.
- $500B of Nvidia revenue would equal ~2.5% of US M2.

**Change since July:** [[semianalysis-research-2026-07]] recorded the AICP floor at **$2.33–2.36/hr with a 40% revenue share**. This episode cites **~$3.25 average with 50%**. Whether that is a newer program vintage, a different GPU generation, or rising rents isn't stated. Either way, the guarantee floor has risen ~40% alongside spot rents.

## IV. Portfolio Positioning & Action Items

- **Treat financing as the gating variable for AI equities.** Demand evidence (rising H100 rents, 80–90% serving margins) is strong. The risk to AI infrastructure stocks runs through credit capacity and spreads, not end demand.
- **Watch hyperscaler and Oracle credit as the early warning.** Oracle is the most levered IG name (~250bp 10-year Z-spread, curve +30–50bp since summer). Further widening in ORCL or Amazon/Meta new-issue concessions would signal the funding wall arriving before demand weakens.
- **Count Nvidia's $497B of off-balance-sheet commitments when valuing NVDA.** The revenue-share structures (50% above the floor) add upside if rents stay high. The residual-value guarantees and rent-back floors become liabilities if rents fall. NVDA is part financier now.
- **Expect dilution at neoclouds.** CoreWeave and Nebius are funding with converts, and Hut 8 with new paper. Their equity risk is tied to execution spreads (~100bp over the anchor tenant for CoreWeave/Meta) and to site-level SPV structures.
- **Duration:** ~$1T a year of AI issuance adds to Treasury and corporate supply. That supports a cautious long-duration stance; see [[bond-supply-tsunami-2026]].
- **Memory remains a constraint.** Despec'd Rubin and ~70% of DRAM wafers going to AI keep memory suppliers' pricing power intact.

**Indicators to monitor:**
- One-year H100 rental rates (~$3/hr now; a fall back toward ~$2 would undercut residual values and backstop floors)
- ORCL, AMZN, META, and CRWV spreads and new-issue concessions
- Monthly AI debt issuance (~$100B a month of announced backstops; ~$1T a year of net new debt)
- Nvidia's disclosed purchase obligations and guarantees in 10-Q footnotes
- Lab API pricing per million tokens
- Data-center moratoriums and delays

## V. Asset Class & Sector Breakdown Table

| Asset Class / Sector | Stock / ETF | View | Rationale / Catalyst |
| :--- | :--- | :--- | :--- |
| AI accelerators | Nvidia (NVDA) | Bullish on demand, rising contingent risk | $497B of off-balance-sheet backstops; 50% revenue share above AICP floors; can support ~46GW of the ~240GW pipeline |
| IG tech credit | Oracle (ORCL) | Cautious | 10-year ~250bp Z-spread; curve +30–50bp since summer; most levered hyperscaler-tier issuer |
| IG tech credit | Amazon (AMZN), Meta (META), Microsoft (MSFT) | Neutral, watch spreads | $25B Amazon deal priced wide in July; Meta residual-value guarantees; Microsoft backstopping Nscale/OpenAI |
| Neoclouds | CoreWeave (CRWV), Nebius (NBIS) | Mixed | Rising rents help profitability; converts dilute equity; execution-risk premium ~100bp |
| AI hosting / bitcoin miners | Hut 8 (HUT) | Mixed | $4.25B raise; pivot to AI hosting depends on IG offtake |
| Custom silicon | Broadcom (AVGO), Google (GOOGL) | Bullish | $24B + $6B TPU financing tied to Anthropic |
| Memory | DRAM suppliers | Bullish | ~70% of DRAM wafers to AI; memory was the binding chip constraint, forcing Rubin despec |
| Server OEMs | — | Bearish margins | Price war at ~9% margins, the one layer not gaining |
| Treasuries / long duration | — | Cautious | AI debt approaching 10% of all US issuance from 2027; long-end yields and spreads already rising |

## VI. Cross-References

- [[ai-compute-commencement-wall-and-refinancing-trap]]: the 2027–28 take-or-pay payment framework. This episode supplies the lender-side view, Nvidia's backstop capacity (~46GW), and the residual-value problem.
- [[semianalysis-research-2026-07]]: earlier SemiAnalysis coverage of the AICP backstop ($2.33–2.36 floor, 40% revenue share then).
- [[klement-ai-bubble-2027-forecast-20261008]]: Klement argues debt costs become "prohibitive" for hyperscalers. SemiAnalysis agrees financing is the constraint but sees strong unit economics. They disagree on the *ability to pay*, not on where the strain shows up.
- [[ax-brij-khurana-wellington-ai-capex-crowding-out-bonds-20261001]]: AI capex crowding out the bond market.
- [[bond-supply-tsunami-2026]]: Treasury supply backdrop for ~$1T a year of AI issuance.
- [[brookings-financing-ai-buildout-van-nieuwerburgh-2026-09]] and [[ubp-financing-ai-build-out-2026-09]]: academic and private-bank views of the same financing question.
- [[ai-inference-costs-accounting]]: token cost and inference economics behind the ~90% margin claim.

## Caveats

- **Incentives:** SemiAnalysis sells ClusterMAX, its GPU rental index, and data to lenders, and is launching a credit group. Their conclusion that lenders need better tools is self-interested even if it is right.
- **Optimistic unit economics:** the ~$100M per MW and ~90% margin figures assume high utilization and frontier pricing. Nishball calls the per-MW figure "a little optimistic."
- **Transcript quality:** figures come from YouTube auto-captions; some company names and a few numbers are garbled. Where the speech was ambiguous, numbers were reconciled with the speakers' own arithmetic: TCO of $2.80/hr with $2.13 capital, and the $6.25 rent example (the captions read "$668").
