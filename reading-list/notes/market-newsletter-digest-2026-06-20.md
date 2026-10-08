---
title: Market and Investment Newsletter Digest — June 20, 2026
created: 2026-06-20
updated: 2026-06-22
type: query
tags: [macro, infrastructure, cloud, saas, company, risk, valuation, geopolitical]
sources: []
confidence: high
contested: false
---

# Market and Investment Newsletter Digest — June 20, 2026

Summary of key themes and observations extracted from investment-related newsletters received on June 20, 2026.

---

## 1. Energy & Infrastructure: Grid Bottlenecks, Wide-Bandgap (WBG) Semiconductors, and SSTs

1. **Grain-Oriented Electrical Steel (GOES) Shortage:** The persistent bottleneck for traditional passive grid transformers (which rely on copper windings and steel cores) remains the long lead times for GOES. Supply is highly concentrated, with China producing **56%** of global GOES. The US produces only **12.5%** of global supply. Cleveland-Cliffs (Ohio) is the sole North American producer with a capacity of **240k tons**, far short of the continent's estimated annual consumption of **489k tons**.
2. **Solid-State Transformers (SSTs) as a Disruptive Replacement:** SSTs integrate transformers, rectifiers, inverters, and voltage regulators into a single active device. They are up to **14 times smaller** and **40 times lighter** than the traditional equipment they replace. The market for SSTs is forecasted by Straits Research to **more than triple by 2033**.
   - *Supply Chain Exposure:* SSTs trade steel/GOES for wide-bandgap (WBG) semiconductors (Silicon Carbide/SiC and Gallium/GaN) and advanced magnets. However, China currently produces **85%** of the advanced magnets required for SSTs.
   - *Key SST Startups:*
     - **Amperesand** (founded by veterans of ABB, GE, Siemens, Vestas) raised **$80M** in late 2025, delivering its first commercial units in 2026 targeting hyperscalers and EV charging.
     - **DG Matrix** raised **$60M** (Series A) and partnered with PowerSecure (Southern Company) to deploy SST-based infrastructure for AI data centers.
     - **WattEV** developed an SST for megawatt-class heavy-duty truck charging, production-ready units expected in 2026.
3. **Data Center Power Shifts (800 VDC):** NVIDIA is leading a transition to **800 VDC power distribution** (coinciding with its Kyber rack architecture) to support racks scaling to megawatt capacity. Bypassing traditional 54V in-rack distribution is expected to improve end-to-end power efficiency by **up to 5%**, reduce maintenance by **70%**, and cut TCO by **up to 30%**. Furthermore, SiC-based uninterruptible power supplies (UPS) achieve efficiencies of **98%** in double-conversion mode (versus 94–96% for traditional silicon).

> "It would be ironic to fix the long-maligned transformer shortage and associated chokepoint by switching to a technology that has similar dependencies and no plan for independent production."

**Sources:**
- *Yes, Transformers Are a Problem...* (Dana Golden, Argonne National Labs / ChinaTalk)

---

## 2. AI Business, Policy, and Software: Fable 5 Ban, SpaceX-Cursor Merger, and Open Source

1. **US Government Ban on Anthropic's Fable 5:** Three days after Anthropic released Claude Fable 5 (a Mythos-class reasoning model made safe for general use), the US Government issued a national security order banning Anthropic from providing access to Fable 5 and Mythos 5 to any foreign nationals—including Anthropic's own overseas employees. Anthropic has disabled the models globally while negotiating a "safe release framework."
   - *Performance Benchmarks:*
     - *Cursor Bench:* Fable 5 scored **72.9%** (8.6 points higher than GPT-5.5's **64.3%**).
     - *RiemannBench (Math):* Jumps from **34%** (Opus 4.8) to **55%** (Mythos 5).
     - *USAMO 2026:* Mythos scored **99.8%** (versus **96.7%** for Opus 4.8).
     - *GPQA Diamond:* Saturated at **94%**.
2. **SpaceX Acquisition of Cursor (Anysphere):** Following its record **$75B IPO** on a **~$2T valuation** (which minted Elon Musk as the world's first trillionaire), SpaceX exercised its option to acquire Cursor's parent company, Anysphere, for **$60B in all-stock deal** (using shares trading around **$211**).
   - *Strategic Rationale:* Cursor possesses **1M+ paying customers**, **$2.6B in revenue** (projected to hit **$6–$10B** by end of 2026), and a **26%** market share in developer AI coding tools. Crucially, Cursor was one of Anthropic's largest revenue pipelines (its Composer feature ran on Claude). xAI is now injecting Cursor's proprietary developer data directly into the *pre-training* (not fine-tuning) of its upcoming **1.5 trillion parameter Grok 4.3** model, to be trained on the Memphis Colossus supercluster.
3. **Open-Source AI Response:** Zhipu AI / Tsinghua released **GLM-5.2** (MIT-licensed, 1M context), which trails Claude Opus 4.8 by only **1%** on FrontierSWE. Moonshot AI also open-sourced **Kimi K2.7 Code** on CW Inference.
4. **Weights & Biases (W&B) "HiveMind" Launch:** W&B launched HiveMind, a developer daemon that aggregates sessions across multiple agent harnesses (Claude Code, Codex, Cursor, etc.) into a unified dashboard in **30 seconds**. It supports session forking for harness-agnostic work and clones workflows into reusable personas (e.g., CoreWeave's virtual "Talk to Tim Sweeney" skill).
5. **DeepSeek's Mega-Round:** DeepSeek raised **$7.4B**, valuing the company at over **$50B**, cementing its status as the most valuable Chinese AI startup. The company was founded by Liang Wenfeng.

> "SpaceX/xAI was always strong on compute and weak on code, and the missing ingredient was exactly that kind of data... Grok 4.3, a 1.5 trillion parameter model, with Cursor’s proprietary coding data injected directly into pre-training, not fine-tuning."

**Sources:**
- *Claude Fable 5 and Mythos 5: Capabilities* (Zvi Mowshowitz / Don't Worry About the Vase)
- *The Stuff of Myth(os)* (Ben Thompson / Stratechery)
- *Fable Got Banned, Open Source Delivered* (Alex Volkov / ThursdAI)
- *AI Week in Review 26.06.19* (Patrick McGuinness / AI Changes Everything)
- *GLM > GPT? GLM-5.2 passes vibe check* (swyx / AINews)

---

## 3. Macroeconomics & Geopolitics: China's Two-Track Model and Straits Forum

1. **China's "Two-Track" Economy:** Fresh monthly macro data from Beijing highlights an increasingly uneven economic growth model.
   - *Strategic Track:* Heavy boom in AI, semiconductors, clean energy, and export-oriented manufacturing, bolstered by state investment and G7 concerns over overcapacity.
   - *Consumer Track:* Retail sales recorded their **first year-on-year decline** since the pandemic. Collapsing auto sales highlight the limits of Beijing's trade-in subsidies, and consumer confidence continues to deteriorate.
   - *Local Government Fiscal Stress:* Local governments are executing aggressive tax audits and back-tax collections ("local government chicanery") to cover mounting fiscal deficits.
2. **Cross-Strait Integration Experiment:** The 18th Straits Forum in Xiamen highlighted achievements in building "same-city living circles" between Xiamen-Kinmen and Fuzhou-Matsu. Progress was cited in the "mini four links" (establishing infrastructure connectivity for water, electricity, gas, and bridges across the Strait).

**Sources:**
- *China's Growth Model Hits Another Reality Check* (Andrew Polk & Joe Peissel / Sinica Trivium China Podcast)
- *China's Economy Is Stronger and Weaker Than You Think* (Ker Gibbs & Eric Olander / China Global South Podcast)
- *China’s cross-Strait integration experiment in Xiamen and Kinmen* (Beijing Scroll)

---

## 4. Startups and Venture Capital

1. **YC Demo Day:** Y Combinator hosted its Demo Day in San Francisco, featuring presentations from nearly **200 founders** to an active crowd of private and institutional investors.

**Sources:**
- *Y Combinator Demo Day: The Quest To Invest In The Best Startups* (Financial Samurai)

---

## Related Notes & Cross-References
- Evaluated market valuation frameworks and the $60B software valuation benchmark in [[valuations]].
- Analyzed macro growth trajectories and export dependency dynamics in [[macro-frameworks]].
- For context on historical portfolio allocations and systematic overlays, see [[trend-following-strategy]] and [[principles]].
- Previous digests: [[market-newsletter-digest-2026-06-03]] and [[market-newsletter-digest-2026-06-02]].
