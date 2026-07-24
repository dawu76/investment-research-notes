---
title: Market and Investment Newsletter Digest — July 3, 2026
created: 2026-07-03
updated: 2026-07-19
type: query
tags: [macro, rates, valuation, infrastructure, cloud, geopolitical, earnings, ecommerce, credit]
sources: []
confidence: high
contested: false
---

# Market and Investment Newsletter Digest — July 3, 2026

## 1. The Meta Compute Debate Continues: Bear vs. Bull

Following the Meta compute-resale news covered in prior digests, two newsletters staked out opposite positions on what it signals for the AI trade.

*   **The Bear Case (George Noble):** Noble reads Meta's compute-resale launch alongside Zuckerberg's own admission that agentic-development progress "has not accelerated the way they expected" over the last four months as the AI bull thesis "unraveling in one sentence." He points to hyperscaler capex guided at a combined $690 billion this year (+81% YoY) with every major hyperscaler about to turn free-cash-flow negative, an oft-cited (if contested) claim that 95% of generative-AI pilots delivered zero measurable P&L impact against $40 billion of enterprise investment, and GPU rental prices crashing from $8/hour in 2024 to $2.99 today. His framing: "when your biggest customer becomes your competitor and starts dumping supply into the same market, the whole structure implodes from the bottom up."
*   **The Bull Rebuttal (Clouded Judgement/Jamin Ball):** Ball argues the bear thesis doesn't hold up once you look at deal structure. Both Meta's plans and SpaceX/xAI's prior compute-resale deals (which generated ~$2.32B/month renting ~450k GPUs to Anthropic, Google, and Reflection) are short-term, with 90-day mutual "outs" — structurally the opposite of a company admitting it has permanent excess capacity. He frames the underlying driver as company-specific: xAI's own model demand collapsed (team turnover, usage falling off a cliff), leaving 100% of its compute allocated to training with no inference revenue to offset the spend — an uneconomic position that renting out capacity temporarily fixes. Meta's Llama models have similarly fallen behind (especially versus Chinese open-source models), suggesting a similar "monetize until we get our act together" logic rather than genuine oversupply. Ball's bottom line: "anyone who's willing to sell capacity finds buyers immediately" — there is no excess compute in the system, only AI laggards converting an idle cost center into revenue. He also reframes the token-economics debate: even if ~80% of future tokens flow to cheap open-weight models, the ~20% of expensive frontier tokens could still drive the majority of AI-lab revenue.

*   **Cross-references:** [[semianalysis-research-2026-06]], [[ai-inference-costs-accounting]], [[valuations]]
*   **Sources:**
    *   *George Noble (The Noble Update)* — Meta Just Admitted the AI Trade Is CRACKING
    *   *Clouded Judgement (Jamin Ball)* — The End of Compute Scarcity? Not So Fast

---

## 2. AI Sovereignty and the Reckoning Index

Bonner Private Research's Dan Denning ties Alex Karp's frontier-lab criticism (also referenced in prior digests) to a broader thesis about the fragility of the closed-source, subscription-AI business model.

*   **The Case Against Closed-Source Subscription AI:** Denning lists three reasons enterprise AI spend ("tokenmaxxing") may be in structural decline: (1) closed-source US models can't be customized or owned, with no guarantee proprietary data entrusted to a vendor stays secure or unused to replicate a customer's business; (2) Chinese open-source models are cheaper and, by most accounts, comparably capable; (3) the Trump administration's brief suspension of Anthropic's Fable model on national-security grounds (since resolved — "Fable is back, baby") introduced a new risk factor: new frontier models may now require government approval to launch, with an implied nationalization threat that would put third-party customer data in government hands.
*   **Karp's "AI Sovereignty" Framing:** Denning reads Palantir CEO Alex Karp's recent comments as effectively declaring that subscription-based LLM business models "aren't going to make it," because corporations and nations want to own the full technology stack and keep data private — something closed frontier labs don't offer. He connects this to Nvidia's open-weight Nemotron model (which Palantir software can run, tune, and improve without surrendering data back to a model provider) as the alternative "AI Sovereignty" architecture: individual, corporate, or government control over one's own AI stack rather than renting access.
*   **The Stakes:** If large corporate AI spenders migrate away from closed-source frontier models toward sovereign/open alternatives, Denning frames this as a direct threat to hyperscaler capex, the broader AI capex boom, and the AI-driven equity bubble he dates to November 2022 — a potential catalyst for what his research series calls "the Big Loss," a mean-reverting market crash. Separately, he cites all standard valuation measures (CAPE, the Buffett Indicator) confirming US equities are historically expensive, while cautioning that valuation predicts the *size* of an eventual reckoning but says little about its *timing*.

*   **Cross-references:** [[valuations]], [[ai-inference-costs-accounting]]
*   **Sources:**
    *   *Bonner Private Research (Dan Denning)* — The Reckoning Index

---

## 3. The Memory Shortage Widens: Antitrust Suits, the Apple-Micron Feud, and Qualcomm's Workaround

Tech Taiwan's dispatch adds fresh detail to the memory-supply crisis tracked across recent digests.

*   **Margins and Antitrust:** Micron's gross margin has surged to 84.6%, with some brokerages forecasting it could reach 90% next year. Phison CEO K.S. Pua reportedly warned during a subscriber event that 80% gross margin was already "enough" for the memory industry and that greed risked antitrust exposure ("if it climbs to 90%, you'll get hit with antitrust lawsuits") — a prediction that has since materialized, with all three major DRAM makers now facing a US consumer class-action lawsuit alleging price manipulation.
*   **Apple vs. Micron, Publicly:** Tim Cook told the WSJ that sharp memory price increases were "ultimately hurting consumers" — prompting Micron's Chief Business Officer to fire back in the same publication days later, arguing the current shortage exists because "certain customers took advantage of the industry during its downturn," when 2023's terrible pricing and margins effectively froze industry-wide investment.
*   **Qualcomm's Alternative Path:** CEO Cristiano Amon told Bloomberg Television that Qualcomm's AI data-center push is largely unaffected by the memory shortage because its AI ASIC solution relies on proprietary "HBC" (High Bandwidth Compute) technology rather than standard HBM, targeting $15 billion in AI data-center revenue by fiscal 2029 (versus Macquarie's $40 billion 2028 estimate for MediaTek's comparable ASIC business). Tech Taiwan's reporting identifies the previously undisclosed partner behind Qualcomm's custom HBM-alternative memory as Nanya Technology, confirmed via a supplier-page statement from Nanya President Pei-ing Lee.

*   **Cross-references:** [[semianalysis-research-2026-06]], [[ai-inference-costs-accounting]]
*   **Sources:**
    *   *Tech Taiwan* — Exclusive: Why TSMC's First-Generation CoPoS May Be Glass-Free

---

## 4. Broadcom's Custom AI Accelerator Engine

Outperforming the Market's deep dive (Part 1 of a series) argues Broadcom's post-earnings sentiment reset has created a reasonable entry point into the market's custom-silicon leader.

*   **The Valuation Setup:** Broadcom's forward P/E has compressed to ~24x — its 5-year average, and matching the trough multiples seen in March 2025 and March 2026 — down from a peak of 48x, following weaker-than-expected guidance and a rotation of risk-on sentiment toward perceived share-gainers over market leaders. The author argues the more relevant comparison is the 3-year (2023–2026) average of 30x, given that's the period since the market began pricing Broadcom's TPU/custom-silicon involvement.
*   **The Business Mix Shift:** Semiconductor Solutions (custom accelerators/XPUs, Ethernet switching, NICs, optics) grew from 58% of FY2025 revenue to 68% of Q2 FY2026 revenue, with segment revenue up 79% YoY; within that, AI semiconductor revenue grew 143% YoY and now represents $10.8B/quarter — 72% of Semiconductor Solutions and 49% of total company revenue. Within AI semiconductors, custom XPU revenue mix is expected to rise from 60% to 70% of the category over time as custom accelerator ramps outpace AI-networking growth (currently 40% of the AI-semi mix, expected to fall to 30%).
*   **Customer Concentration:** Google remains Broadcom's dominant TPU customer under a long-term April 2026 agreement covering multiple future TPU generations. Anthropic is Broadcom's second core customer, using more than 1GW of Broadcom TPU-based compute in 2026, recently expanded by another 5GW of next-generation TPU compute starting 2027. OpenAI is identified as the third of Broadcom's six core custom-silicon customers.

*   **Cross-references:** [[semianalysis-research-2026-06]], [[valuations]]
*   **Sources:**
    *   *Outperforming the Market* — The Case for Broadcom (Part 1)

---

## 5. Doomberg: Why Financial Sanctions Backfire — Huawei's EUV-Free Chip Path

Doomberg extends its long-running thesis that sanctions against powerful countries tend to strengthen rather than weaken them, using China's semiconductor progress as its latest proof point.

*   **The Core Argument:** Sanctions on weak countries (Syria, Cuba) can be superficially effective but mostly harm their populations; sanctions on powerful countries instead provoke an emergence "far stronger for the experience," like a partially treated cancer. Doomberg has argued since 2022 that this applies to both Russian energy sanctions (the world needs Russian energy more than Russia needs the money) and US semiconductor export controls on China.
*   **The Huawei Evidence:** Huawei announced a new chip-design framework it claims can deliver transistor densities equivalent to 1.4-nanometer-class chips by 2031 without relying on cutting-edge EUV lithography tools — directly undercutting Commerce Secretary Howard Lutnick's stated concern that China may already possess such EUV machinery. Doomberg's read: "China's chip ambitions won't be denied, and they will almost certainly leapfrog the best Western technology as a result" of having been forced to independently engineer around the export-control roadblocks.

*   **Cross-references:** [[semianalysis-research-2026-06]], [[hormuz-closure-scenarios-2026]]
*   **Sources:**
    *   *Doomberg* — Treatment Resistant

---

## 6. America's Business Formation Boom, at 250

James Wang (Weighty Thoughts) used the July 4th anniversary to examine unusually strong US business-formation data and its plausible AI linkage.

*   **The Corporate Age Contrast:** SpaceX's recent IPO (the largest in history) made it America's sixth most valuable company; all six of the top American companies (SpaceX, Nvidia, Alphabet, Apple, Microsoft, Amazon) are relatively young — the oldest, Microsoft, was founded in 1975. By contrast, Europe's largest companies (ASML aside) run far older: Roche (1896), HSBC (1865), Novartis/AstraZeneca (1990s mergers of firms dating to the 1700s–1800s), Nestlé (1866), Siemens (1847) — illustrating starkly different rates of corporate "creative destruction" (citing the 2025 Nobel economics prize awarded to Mokyr, Aghion, and Howitt for that concept).
*   **The Data:** Americans filed 5.67 million business applications in 2025 (a record, with 2026 running ahead of pace); the pre-pandemic monthly rate of ~292,000 has risen to ~524,000 as of this May, with two distinct step-changes — one starting mid-2020 (pandemic-driven: remote work, stimulus, the "quits wave," not AI-attributable) and a second starting mid-2025. Actual business *establishment births* (not just applications, most of which never become real businesses) are running ~45% above pre-pandemic rates — a figure the Economic Innovation Group calls the largest increase in American economic dynamism in at least 30 years, and one that skeptical labor economist John Haltiwanger (who has spent two decades documenting declining US business dynamism) has conceded is genuine.
*   **Torsten Slok's Attribution:** Apollo's chief economist attributes the boom to AI/LLMs "dramatically reducing the cost and complexity of launching a company" — Wang agrees directionally but notes this continues a much longer trend of software (mainframes → PCs → early internet → SaaS → cloud → AI) progressively lowering the cost of starting a business, rather than representing something entirely new. Wang cites personal observation of ~20 companies he knows running $10–100M in annual recurring revenue with only 3–5 employees as anecdotal confirmation of the trend's real economic bite.

*   **Cross-references:** [[macro-frameworks]]
*   **Sources:**
    *   *James Wang (Weighty Thoughts)* — America Turns 250. Its Biggest Companies Never Do—And That's Great!

---

## 7. Fixed Income: A CLO Trade Built for Higher-for-Longer

Michael Gayed profiled a structured-credit ETF designed to benefit from exactly the rate environment that hurts most income vehicles.

*   **The Structural Pitch:** Most retail CLO income vehicles reach for yield by owning the equity tranche — the riskiest slice of the capital structure that absorbs the first dollar of loss. The Panagram BBB-B CLO ETF (CLOZ) instead owns BBB/BB mezzanine tranches, positioned higher in the waterfall with subordination layers beneath them, while still paying a floating coupon of SOFR-plus-spread. Result: a ~7.5% distribution yield against a maximum historical drawdown of just 6.1%.
*   **The Rate Sensitivity (Inverted):** Because CLOZ's holdings pay a floating rate tied to SOFR, a Fed under Kevin Warsh holding rates or hiking further translates directly into *more* income for shareholders — the mirror image of rate-sensitive REIT and preferred-stock funds, which suffer in the same higher-for-longer scenario.
*   **Fund Specifics:** NYSE Arca: CLOZ; ~$816M AUM across 203 individual CLO tranches; 0.50% expense ratio; inception January 2023; 30-day SEC yield 6.85%, distribution yield 7.46% (monthly distributions ~$0.171/share); trades essentially at NAV (active ETF structure, not a closed-end fund); benchmarked to the JPMorgan CLO High Quality Mezzanine Index.

*   **Cross-references:** [[macro-frameworks]]
*   **Sources:**
    *   *Lead-Lag Report (Michael Gayed)* — The CLO Income Play That Doesn't Blow Up

---

## 8. Southeast Asia's E-Commerce War: Shopee's Multi-Platform Defense Against TikTok Shop

Asia Tech Review detailed Shopee's expanding partnership strategy to defend its Southeast Asian e-commerce lead against a fast-growing TikTok Shop.

*   **The Threat:** TikTok Shop reached an estimated $54.6 billion in Southeast Asian GMV last year (+50%+ YoY per Momentum Works), versus Shopee's $83.2 billion — a gap that TikTok Shop's growth rate suggests will keep narrowing. The strategic distinction: TikTok Shop *creates* purchasing intent through discovery-driven short video, while Shopee and Lazada remain destination sites for shoppers who already know they want to buy.
*   **Shopee's Response:** A new partnership with Meta brings affiliate-revenue tools to creators on Instagram and Facebook (minimum 1,000 followers) across Southeast Asia, Taiwan, and Brazil — mirroring an existing YouTube affiliate partnership dating to 2024 and a more recent OpenAI tie-up embedding Shopee shopping capability directly into ChatGPT in the same regions. The strategy assembles a "patchwork" of external platform partnerships (Instagram, Facebook, YouTube, ChatGPT) rather than TikTok's single integrated discovery-to-checkout flow.
*   **Competitive Context:** ByteDance's earlier acquisition of Tokopedia helped drive its Indonesian shopping business (Indonesia is TikTok Shop's second-largest market after the US) and helped make Tokopedia parent GoTo profitable — but TikTok Shop has since laid off a large share of Tokopedia staff in Indonesia (local reports suggested up to 90% were affected), raising questions about whether TikTok is preparing a more aggressive, integrated regional push.

*   **Cross-references:** [[valuations]]
*   **Sources:**
    *   *Asia Tech Review* — Shopee Calls in Friends from Instagram and YouTube to Fend Off TikTok

---

## 9. Quick Hits: TSOH Weekly Roundup and Middle-Market Rate Stress

*   **TSOH (Alex Morris):** Flagged Comcast's NBCUniversal spinoff (covered in the June 30 digest) as a strategic move he'd been waiting "more than five years" for; noted Nestlé executives observing consumer pack-size polarization amid inflation (shoppers moving to either the smallest or largest pack sizes, squeezing mid-sized formats) as directly relevant to value retailers like Dollar Tree/Ollie's versus warehouse clubs like BJ's/Costco; and flagged Meta's compute-resale plans (Section 1) as evidence that "blurring lines" in mega-cap tech business models are making position-sizing decisions harder given a materially different long-term risk/reward profile than five years ago.
*   **Torsten Slok (Apollo):** More than 40% of Russell 2000 companies are currently unprofitable, meaning a higher-for-longer rate environment directly threatens middle-market firms as debt-servicing costs consume a growing share of thin or negative earnings — a data point that sits in tension with the small-cap earnings-strength narrative highlighted in this digest series' July 2 edition (Section 1's Russell 2000 discussion), underscoring that small-cap performance likely masks meaningful dispersion between profitable and unprofitable constituents.

*   **Cross-references:** [[valuations]], [[macro-frameworks]]
*   **Sources:**
    *   *TSOH Investment Research (Alex Morris)* — TSOH Weekly Roundup (07/03/26)
    *   *Torsten Slok (Apollo)* — Middle Market Investing: When Higher Rates Meet Thin Earnings
