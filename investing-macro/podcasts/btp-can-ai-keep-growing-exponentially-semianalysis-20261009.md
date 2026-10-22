---
title: "Can AI Keep Growing Exponentially? Let's Ask SemiAnalysis — With Dylan Patel and Jordan Nanos | Big Technology Podcast"
created: 2026-10-09
updated: 2026-10-09
type: concept
tags: [macro, infrastructure, cloud, valuation, credit, risk]
sources: ["https://youtu.be/LwMtHI7BHWI"]
confidence: medium
contested: true
---

# Can AI Keep Growing Exponentially? Dylan Patel and Jordan Nanos | Big Technology Podcast

**Speakers:** Alex Kantrowitz (host), Dylan Patel (founder and CEO, SemiAnalysis), Jordan Nanos (SemiAnalysis technical staff, author of ClusterMAX 3.0). Released October 9, 2026; 60 minutes.

## I. Executive Summary

Patel argues the AI buildout is **bigger than the popular charts show**: ~$2T of US capex next year, or **5–6% of GDP**, not 2–4%. He also argues that **revenue projections used to call it a bubble are too low**. He expects OpenAI plus Anthropic to reach a **$600–700B combined revenue run rate by December 2027**, possibly **$1–1.5T by end of 2027**, and says both labs already cover their compute costs or will within a few quarters. Capex growth will have to slow from triple digits, and the stress points are company-specific. Oracle has fixed-margin contracts and a delayed New Mexico site. Most neoclouds fail basic security. Google DeepMind is falling behind on compute. Labs are keeping their best models internal.

**Sentiment:** very bullish on AI demand and lab economics; skeptical of bubble arithmetic; selective on which companies capture the upside.

## The questions the speakers are trying to answer

1. **How big is the AI buildout relative to the economy and to past buildouts?**
2. **Will capex growth decelerate the way Wall Street expects?**
3. **Can AI revenue grow enough to justify the spending, and where does that money come from?**
4. **Are hyperscaler commitments to neoclouds binding, and what would derail demand?**
5. **How should investors think about an Anthropic IPO at ~$2T?**
6. **Is Nvidia's backstopping of neoclouds propping up a bubble?**
7. **Which providers are actually good (ClusterMAX), and what does that say about Oracle, Google, and the long tail?**
8. **Will frontier labs keep their best models for themselves?**

## II. Timestamps & Agenda

Approximate, from the transcript.

- **0:00 Scale of the buildout.** The railroad comparison chart (3.6% vs 2.2% of GDP); Patel's 5–6% figure; US capex serving foreign demand.
- **4:00 Capex growth path.** Hyperscaler capex +116% YoY in Q3 2026; consensus deceleration; supply-chain and capital limits.
- **8:00 Revenue needed.** Bain's $6T, Van Nieuwerburgh's $3.5T (8.8% of GDP); depreciation math; OpenAI/Anthropic revenue forecasts; Meta solvency.
- **14:40 Where the money comes from.** R&D and COGS budgets, capital vs labor share, chip-design productivity.
- **19:50 Derailment risk.** Neocloud contract terms vs self-build flexibility; demand still exceeds supply.
- **24:20 Anthropic IPO.** The "$2T could be zero or $20T" post; multiples; distribution of gains.
- **29:00 Lab economics.** ~75% inference gross margin vs Salesforce; near-zero customer acquisition cost; stickiness; "pacing the frontier."
- **34:10 Nvidia backstops.** $588B tracked; why Nvidia does it.
- **39:00 Neocloud security.** Ilya Sutskever's tweet; open-source models hacking neoclouds; a foreign government's workloads exposed.
- **43:10 ClusterMAX tiers.** CoreWeave/Nebius top; Oracle and Google Cloud second; Oracle's three risks; Nebius's pricing power; 323 providers.
- **51:25 Google and DeepMind.** Shrinking share of Google compute; DeepMind now has the least compute of the three frontier labs.
- **54:55 Labs keeping models internal.** Mythos/Fable, Astra; release "minimum viable models."

## III. Detailed Key Takeaways

### 1. The buildout is bigger than the charts say

A chart circulating on X put the AI buildout's median annual share of GDP at **3.6%**, against **2.2% for railroads**. Patel says "people's numbers are too low." **US capex next year will be on the order of $2 trillion**, counting the full supply chain and not just chips and data centers. Against **~$30T+ of US GDP**, that is **5–6%**.

**Why the US share is so high:** railroads and fiber were built where they were used, but AI capex in America serves the world. Training happens in the US, and **most of Anthropic's and OpenAI's European inference runs in American data centers**, as does much of Asia's. US capex therefore understates the global demand it serves and overstates the domestic share.

### 2. Capex growth must slow, but the buildout keeps going

- Kantrowitz cites ClusterMAX data showing **hyperscaler capex up 116% YoY in Q3 2026**. Consensus has growth falling **below 100% in Q4** and to the **~70% range in Q1 2027**, declining from there.
- **Nanos:** "We're definitely going to hit limits towards the end of next year." The two limits are organizational (marshalling resources to build *another* gigawatt on top of current projects) and financial (raising trillions "even though there's incredible returns").
- **Patel:** deceleration is arithmetic. Anthropic went from **sub-$10B to over $100B of revenue this year (~10x)**, but "they're just not going to have a trillion dollars of revenue by the end of next year." Nvidia's revenue still grows ~2x year over year, below earlier peaks.

**Investor read:** a slowdown in the *growth rate* of capex is consensus and expected. It is not, on its own, evidence of a demand break. Watch whether the dollar level of capex keeps rising.

### 3. Revenue requirements: the bear math is too conservative, per Patel

**Bear benchmarks cited:**
- **Bain:** hyperscalers need **$6T of annual revenue by 2031** to break even.
- **Stijn Van Nieuwerburgh (Columbia):** the US must spend **~$3.5T a year on AI services by 2032 (8.8% of GDP)** to justify today's investment; see [[brookings-financing-ai-buildout-van-nieuwerburgh-2026-09]].
- A viral post that Meta "committed corporate suicide" with debt.

**Patel's rebuttal:**
- **Depreciation math:** $1T of capex depreciated over six years (GPUs; data centers last 15) needs roughly **$1.5T of revenue over six years, ~$250B a year**, back-loaded rather than front-loaded. Revenue always trails capex, because today's revenue runs on capacity built in prior years.
- **Lab revenue forecast:** **$600–700B combined run rate for OpenAI plus Anthropic by December 2027**. On the "1.5 trillion" end-2027 figure he is less certain.
- **Lab profitability:** Anthropic is **already profitable on revenue minus compute (training and inference combined)**. OpenAI gets there "within the next couple of quarters, maybe two or three," per SemiAnalysis's tokenomics model.
- **Amazon:** "All of their AI infrastructure investments are profitable today," and Bedrock lifted gross margin last quarter. The counterparty risk is that its customers, the labs, could fail.
- **Meta solvency:** Meta "at any point can just stop buying new stuff and their cash flow can easily pay for all the stuff that they've signed."
- **His threshold:** "If AI revenue is only $3 trillion in 2031, then yeah, we'll have big problems."

**Nanos:** future "AI revenue" won't be limited to per-token pricing and Claude Code subscriptions. Labs with models capable of most knowledge work can enter drug discovery, robotics, self-driving, and life sciences, the way GLP-1s rewarded Lilly's research.

> "Capex is not going up at 10x a year, but inference revenue just went up 10x year on year for the AI labs." (Patel)

**Contrast:** this is the opposite of [[klement-ai-bubble-2027-forecast-20261008]], which treats depleted hyperscaler FCF and rising debt costs as signs that returns won't arrive in time.

### 4. Where the money comes from: capital takes share from labor

Kantrowitz cites a chart of 2025 spending as a share of GDP: health 18%, food 9.1%, and **AI services 8.8%**, which he expects to pass food in 2026. Patel's sources:

- **Corporate budgets:** a rising share of R&D and COGS goes to AI.
- **Labor:** AI accelerates the decades-long fall in labor's share of GDP since the 1970s, because "AI tokens are basically just capital… creating labor." His hope, which he admits may be irrational, is that the economy grows fast enough that **labor income in dollars stays flat or grows slowly** while capital's share balloons.
- **Productivity without headcount:** US chip-design engineers have been **flat for 20 years** while the value of the industry exploded (Nvidia, Broadcom, Google). AI-assisted design extends that pattern: the same people, more revenue, higher margins.

On knowledge work: in the next few years, "the most high agency people are going to be able to do the coolest stuff." Only if AI becomes better than humans "in most every way" is "knowledge work screwed."

### 5. Contract risk: neocloud deals vs self-builds

Nanos separates two kinds of hyperscaler commitments:

- **Neocloud offtakes** are generally **5–6-year, take-the-full-capacity contracts** with fixed hourly rates and no arbitrary cancellation rights. Neoclouds sign them after securing land, power, and sometimes chips. They are binding.
- **Self-build campuses** are where flexibility exists. Meta can leave a shell empty for years, since construction is a small share of total project cost compared with HBM, optics, and GPUs.

**What would derail demand:** a slowdown in end demand, which hasn't appeared. Supply is hard-constrained by chips, data centers, and energization timelines, and "all of the modeling we can do basically shows that demand outstrips supply… is it 10%, is it 50%, is it infinite? We don't get to answer that question." Scale cited: billions of Meta users, nearly 1B ChatGPT monthly users, and hundreds of millions for Claude Code.

### 6. The Anthropic IPO: "$2T could be zero or $20T"

Patel's post: you can't invest at $2T because it could be zero, or $20T, "but at $20T we're all f***ed." He calls it a joke, but explains it:

- He is "extremely bullish." Anthropic "could even be the first $10 trillion company."
- **Multiples have to compress:** Anthropic raised at ~30x revenue. An IPO at ~$100B of revenue would be ~20x. A $10T value probably needs ~$1T of revenue (possible in 2028–29). A $20T value at a ~5x multiple implies **$2–4T of revenue**.
- **At that scale,** AI capabilities are "freaking insane." The gains accrue to a narrow set of shareholders and the supply chain, which could "tear the fabric of society apart." That is the pessimistic case for a world where the bull case comes true.

**Lab economics:**
- **Anthropic's inference gross margin is ~75%, "a little bit higher even" on frontier models.** That matches **Salesforce's ~75%**, which took Salesforce years after its IPO to reach.
- **Customer acquisition cost is near zero,** against up to ~30% of revenue at SaaS companies.
- **R&D is growing slower than revenue.**
- **Customers are sticky:** better Chinese models haven't shifted spending share much.
- Patel's conclusion: an AI lab is "arguably a better business than software."

**"Pacing the frontier" is mostly signaling.** Neither Dario Amodei nor Sam Altman can slow much, given each other and China.

### 7. Nvidia's backstops: pragmatic, not a Ponzi

**SemiAnalysis now tracks $588B of off-balance-sheet backstops** supported by Nvidia. That is up from **$497B** in the "Backstop Universe" article discussed in [[sa-whos-funding-the-11-trillion-ai-buildout-20261009]] about a month earlier, consistent with the ~$100B a month pace cited there. Nvidia's revenue is "approaching 400, about to cross 500 billion" (~2.5% of US M2).

**Nanos's case that it is pragmatic:**
- Nvidia wants a **diverse customer base**, not dependence on three or four hyperscalers.
- Nvidia signs as the investment-grade offtaker so neoclouds can borrow. When the capacity comes online, **someone else usually wants it at a higher price**, so Nvidia resells it and rolls to the next deal.
- Capacity Nvidia keeps for internal research (it publishes more models on Hugging Face than anyone; Nemotron) is a **very small share of Nvidia's revenue**.
- Backstops cover construction, memory suppliers, fab builders, and industrial equipment, whatever "the long pole in the tent" is for a project.

This answers the Ed Zitron critique that Nvidia is funding its own demand. It does not address what happens to the guarantees if resale prices fall.

### 8. Neocloud security is weak

SemiAnalysis published "Most Neoclouds Suck at Security." Hours later, **Ilya Sutskever** tweeted that neoclouds have limited cybersecurity and that rogue agents "will try taking over a Neocloud to run more copies."

- Patel: **open-source Chinese models (GLM 5.3 especially) "can just hack dozens of the neoclouds."**
- On one cloud, SemiAnalysis **accidentally saw other tenants' storage and Slurm jobs**, including workloads from a **non-US government security agency of a top-10 GDP country**, and reported it immediately.
- Nanos: sovereign AI demand means governments share infrastructure when only one facility in a country has GB300 NVL72. "It's a seller's market."

### 9. ClusterMAX 3.0: quality vs stock performance

- **Tiers:** CoreWeave and Nebius at the top; Oracle and Google Cloud in the second tier; a long "not recommended / unavailable" tail with more logos than the top four tiers combined. **SemiAnalysis tracks 323 providers.**
- **Patel:** ClusterMAX is "not stock recommendations." It measures service quality (reliability, security, storage, networking, Slurm/Kubernetes), not build pace or delivery delays, which matter more for stocks.
- **Oracle**, "one of the top neoclouds in terms of quality of service," carries three stock risks:
  1. Its OpenAI deals, signed about a year ago, have a **fixed margin**, so Oracle can't benefit from higher GPU rental prices.
  2. It **raised a lot of debt** just as markets turned wary of AI leverage, "even though Oracle is completely solvent."
  3. **Execution:** the **New Mexico site, contracted for OpenAI, is delayed potentially multiple years** for lack of gas pipelines. SemiAnalysis flagged this to clients in April, May, and June before Oracle declared force majeure and the stock "tanked." Wisconsin has delays too.
- **Nebius has the shortest average contract length** of the top clouds, so it has been able to "really jack up pricing." CoreWeave and Oracle locked in long-term contracts and captured less of the rental-price surge.
- **Nanos:** a seller's market means providers prioritize raising money, building, and deploying over service quality, and the failures (security, reliability) are "dead simple" to fix.

### 10. Google: selling compute is starving DeepMind

- DeepMind's share of Google's compute has **fallen** even as Google produces far more ("Thomas Kurian won and Demis lost"). **By the end of this year DeepMind will have the least compute of the three frontier labs.**
- Selling large volumes of TPUs to Anthropic "is hurting Google DeepMind's business."
- Next year OpenAI and Anthropic each try to **add 5–10GW**, while Google adds "only a few gigawatts."
- Nanos: "Nobody wants the third or fourth or fifth best coding model." Even with Gemini 4 "Argon," Google needs a niche. Top researchers keep getting poached.

### 11. Labs are keeping their best models internal

- **Anthropic:** "Mythos" was ready in February. Two newer models have appeared in safety cards. The public got a restricted version ("Fable") months later, and "Glasswing" gave Mythos to only some sectors.
- **OpenAI:** "Astra" was finished a couple of months before release, and a newer model ("Bell") was shown solving math problems but not released.
- **Why:** releasing invites distillation, and the public six-month gap to Chinese open source hides **months of progress kept internal**.
- **Expectations:** Patel expects a new Anthropic model "in the coming weeks, for their IPO," and one from OpenAI. Nanos's bet is "minimum viable models" released to stay ahead of Chinese and open-source competitors, with labs pursuing high-value end applications internally.

## IV. Portfolio Positioning & Action Items

- **Don't read a capex growth deceleration as a bubble signal.** Consensus already expects it (116% to <100% to ~70%). The signals that matter are the dollar level of capex, lab revenue run rates (Patel: $600–700B combined by Dec 2027), and whether AI revenue tracks toward multiple trillions by 2031.
- **Prefer short-contract or merchant-priced capacity in a rising-rent market.** Nebius's short contracts let it reprice; CoreWeave's and Oracle's long fixed-margin deals cap upside. Contract length is a key variable when comparing neocloud equities.
- **Oracle:** the service is high quality, but the equity is exposed to fixed margins, debt sentiment, and project delays (New Mexico force majeure). Treat the credit as solvent and the stock as execution-sensitive.
- **Nvidia:** off-balance-sheet backstops grew ~$91B in about a month, to $588B. Track the figure quarterly against Nvidia's revenue and cash.
- **Alphabet:** TPU sales and Cloud win at the expense of DeepMind's compute share. Value GOOGL increasingly as an infrastructure seller rather than a frontier-model leader.
- **Anthropic IPO:** at ~20x revenue (~$100B), the bull case needs revenue to keep compounding while the multiple compresses. Size any position for a wide outcome range.
- **Security risk at neoclouds** is an underpriced operational and reputational risk, especially for providers serving sovereign customers.

**Indicators to monitor:**
- Hyperscaler capex vs consensus each quarter
- OpenAI and Anthropic revenue run rates and compute-adjusted profitability
- Nvidia's tracked backstop total
- Neocloud average contract length and repricing
- Oracle project milestones (New Mexico pipelines)
- Model releases ahead of the Anthropic IPO

## V. Asset Class & Sector Breakdown Table

| Asset Class / Sector | Stock / ETF | View | Rationale / Catalyst |
| :--- | :--- | :--- | :--- |
| AI labs (private / IPO) | Anthropic, OpenAI | Very bullish on business; valuation-sensitive | Anthropic ~10x revenue growth to >$100B; ~75% inference gross margin; compute-profitable; IPO at ~$2T (~20x revenue) |
| Neoclouds | Nebius (NBIS) | Bullish | Top ClusterMAX tier; shortest contracts, able to reprice in a rising-rent market |
| Neoclouds | CoreWeave (CRWV) | Neutral to bullish | Top ClusterMAX tier but long-term contracts limit capture of higher rental prices |
| Cloud / IG credit | Oracle (ORCL) | Cautious on stock, fine on solvency | Fixed-margin OpenAI deals; heavy debt; New Mexico force majeure (pipelines), Wisconsin delays |
| Hyperscalers | Amazon (AMZN) | Bullish | AI infrastructure already profitable; Bedrock lifted gross margin |
| Hyperscalers | Meta (META) | Neutral | Solvent ("can just stop buying"); self-build flexibility; Muse demand |
| Hyperscalers | Alphabet (GOOGL) | Mixed | TPU and Cloud sales strong; DeepMind compute share falling; Gemini behind on coding |
| AI accelerators | Nvidia (NVDA) | Bullish with rising contingent exposure | Revenue nearing $500B; $588B of backstops; diversifying beyond hyperscalers |
| Chip design | Nvidia, Broadcom (AVGO) | Bullish | Flat engineer headcount with exploding value; AI-assisted design improves margins |
| Long tail of neoclouds | — | Bearish | 323 providers; most fail basic security and reliability; seller's market masks weak quality |

## VI. Cross-References

- [[sa-whos-funding-the-11-trillion-ai-buildout-20261009]]: Nishball and Nanos on the financing side ($11.3T capex, $497B backstops a month earlier, rising H100 rents).
- [[sa-fight-for-fast-tokens-tpu-v7-vera-rubin-engrams-20261002]]: InferenceX team on serving margins, TPU v7, and Vera Rubin.
- [[klement-ai-bubble-2027-forecast-20261008]]: the bear case this episode argues against (depleted FCF, prohibitive debt cost).
- [[brookings-financing-ai-buildout-van-nieuwerburgh-2026-09]]: source of the $3.5T / 8.8%-of-GDP revenue requirement Patel calls too low.
- [[ai-compute-commencement-wall-and-refinancing-trap]]: 2027–28 payment-timing framework; Nanos's binding-contract point affects how much of that obligation is truly fixed.
- [[valuations]]: valuation background for the Anthropic multiple discussion.

## Caveats

- **Incentives and affiliation:** SemiAnalysis sells ClusterMAX, TCO models, and tokenomics data to the industry it describes. Patel calls himself "extremely bullish" on Anthropic.
- **Unverified forecasts:** the revenue forecasts ($600–700B by Dec 2027; "1.5 trillion" by end-2027) come from SemiAnalysis's internal models and are not checked against company disclosures. The 1.5T figure is spoken loosely in the transcript.
- **Model names:** Mythos, Fable, Glasswing, Astra, Bell, and Gemini 4 Argon are as spoken in YouTube auto-captions and may be misspelled.
