---
title: "The Fight for Fast Tokens, TPU v7, Vera Rubin, and Engrams (AI Supply Chain, InferenceX) | SemiAnalysis Weekly Ep. 034"
created: 2026-10-09
updated: 2026-10-09
type: concept
tags: [infrastructure, cloud, valuation, earnings, risk]
sources: ["https://youtu.be/NcqHQmpNjr0"]
confidence: medium
contested: false
---

# The Fight for Fast Tokens, TPU v7, Vera Rubin, and Engrams | SemiAnalysis Weekly Ep. 034

**Speakers:** Jordan Nanos (host) with SemiAnalysis's InferenceX benchmarking team: Cam Quilici, Bryan Shan, and Alec Ibarra. Released October 2, 2026; 63 minutes.

## I. Executive Summary

The InferenceX team reports on what real inference workloads look like on current hardware. They have three conclusions. **High-bandwidth memory (HBM) is the binding hardware constraint**, and model designers (mostly Chinese labs) are re-architecting models to push data out to cheaper DRAM and SSD. **Serving open models on the latest Nvidia racks is very profitable**: ~40–50% margins at realistic utilization. And competition is widening: **Google's TPU v7 posts the lowest cost per token** in their tests, while **Vera Rubin delivers ~3x Blackwell** in the range of speeds providers actually sell. The team is skeptical that "fast tokens" justify their price premium or that fast-token chip startups have a lasting edge over optimized GPU software.

**Sentiment:** bullish on inference demand and profitability; bullish on Nvidia's Rubin cycle and on TPU externalization; mixed to negative on specialized fast-inference silicon.

## The questions the speakers are trying to answer

1. **How are models adapting to HBM scarcity?** Engrams and offloading to DRAM/SSD.
2. **What does real agentic-coding inference look like, and how much can you earn serving it?** AgentX benchmark and profit calculator.
3. **Is Google's TPU v7 a real third merchant competitor to Nvidia and AMD?**
4. **Is Vera Rubin a big enough step over Grace Blackwell to drive an upgrade cycle?**
5. **Will users pay a premium for fast tokens?**
6. **Do fast-token chip startups have a moat against general-purpose GPUs plus better software?**

## II. Timestamps & Agenda

- **0:00 Intro.** Five InferenceX articles since the last episode.
- **0:31 Engrams.** N-gram embeddings stored in hash tables, looked up from DRAM/SSD, and overlapped with compute; a response to HBM limits.
- **12:27 AgentX benchmark.** Replays SemiAnalysis's own agentic-coding sessions; median request ~100K input tokens; >98% theoretical cache-hit rate.
- **16:36 Profit calculator.** Serving margins by chip and model, using SemiAnalysis's total cost of ownership (TCO) model and OpenRouter prices.
- **23:40 TPU v7.** Lowest cost per million tokens against B200/B300; native PyTorch backend coming; TPUs moving into neoclouds.
- **32:03 Vera Rubin.** ~3x at mid-curve and ~1.4x at max throughput on DeepSeek V4 Pro; HBM4 bandwidth; a new lookup-table quantization format.
- **40:49 Fast tokens.** The team is mostly bearish on paying for ultra-fast modes.
- **49:33 TileRT.** ~200–500 tokens/sec on near-trillion-parameter models on Nvidia GPUs via a single mega kernel.
- **54:00 Chip startups.** Demand outstrips supply, but deployment and supply chain decide winners; Nvidia's $20B Groq acquisition.
- **1:01:31 Wrap up.**

## III. Detailed Key Takeaways

### 1. HBM is the constraint, and model architecture is bending around it

**Engrams** store learned embeddings for two- and three-token sequences ("n-grams") in a hash table that is built during training and looked up at inference. Because the lookup needs only token IDs, it can run **asynchronously from DRAM or SSD, overlapped with other computation**, instead of occupying HBM. In effect, the model gets some layers "for free": early layers no longer spend parameters reconstructing word meanings.

- **Evidence:** DeepSeek's ablation found model loss is minimized with a **mix of engram and mixture-of-experts layers**, not all of one. KL-divergence tests show engram models reach next-token predictions earlier in the network.
- **Placement trade-off:** engram layers help most early in the model, but early placement leaves no compute to hide the lookup behind. A Qwen Flash model puts engrams at layer 2; DeepSeek V4.1 Flash puts them at layer 1. Meituan's LongCat team says it developed the same technique independently.
- **Lineage:** this follows DeepSeek's earlier multi-head latent attention (MLA), which also shrank the KV cache to save HBM.

> "The trend forever has been… China has been restricted in terms of HBM even more than the United States… In a way it's a curse that the US labs have infinite compute and are hoarding HBM… All the innovations feel like they're coming from China." (Cam Quilici)

**Why it matters:** if new model designs move part of the working set from HBM to DRAM and SSD, AI servers need more DRAM and flash per GPU. Nanos frames US labs as optimizing for **HBM bandwidth over capacity**, while Chinese labs, already working with lower-bandwidth domestic HBM such as that on Huawei's Ascend 950, optimize around capacity.

### 2. AgentX: what agentic coding inference really looks like

Older benchmarks used fixed 8K-in/1K-out requests with no prefix caching. **AgentX replays SemiAnalysis employees' actual coding-agent sessions**, captured by a proxy and cleaned, against real servers running open-source inference stacks.

- **Median (P50) request is almost 100,000 input tokens.** Every agent turn resends the whole conversation, so the KV cache grows quickly from turn to turn.
- **The theoretical cache-hit rate is above 98%.** The engineering question is how much of that a system actually captures, through KV-cache storage, transfer between prefill and decode servers, and request routing (their stack: vLLM, NIXL, and Nvidia's Dynamo router).
- **DRAM offloading adds ~20–30% to the cache-hit rate** at high-throughput operating points (~40–60 tokens/sec per user, many concurrent sessions). That covers offline batch inference and RL training rollouts. It barely matters at high interactivity, where concurrency and KV volume are low.

### 3. The profit calculator: open-model inference is "a money printer"

The calculator combines SemiAnalysis's hourly TCO per accelerator (chip, data center, electricity), InferenceX throughput, and provider prices from OpenRouter.

| Configuration | Result |
|---|---|
| Kimi K3 on GB200 NVL72 (parameters shown on screen) | ~40.7% profit margin |
| Kimi K3 on GB300 with Dynamo, **60% utilization, 30% license fee to Moonshot** | **~50% margin** |
| Same at 30–40% utilization | "Still can be profitable" |
| DeepSeek V4.1 Flash at some settings | Unprofitable |

> "These things are just money printers right now until the cost of compute sort of normalizes… If you have a few million dollars, I would buy a GB300 rack… probably make your money back in a couple months." (Quilici; partly tongue in cheek)

These numbers use open-source software. Large inference providers run private kernels and should do better. Margins rise because newer models are both higher quality, so they command higher prices, and cheaper to serve.

**Consistency check with [[sa-whos-funding-the-11-trillion-ai-buildout-20261009]]:** that episode cited ~80% gross margins for serving Chinese open models on GB300. This episode's ~40–50% is a fuller profit margin after a utilization discount and a 30% model license fee. The two figures measure different things and are compatible. Both support the demand case behind rising GPU rental prices.

### 4. TPU v7: a real third merchant competitor

- **Cost:** in an apples-to-apples test against B200 and B300, **TPU v7 had the lowest cost per million tokens at every point on the curve but one**, using Google's external (rental) TCO, which Ibarra called "super good." The exact figure is garbled in the captions.
- **Room to improve:** these are early, open-source results (TPU vLLM is new), and recent TPU mega-kernel work produced "a huge performance boost out of nowhere."
- **Software:** a **native PyTorch backend for TPU** ("torch TPU") is coming "quite soon," replacing today's convoluted intermediate-representation path. That removes a long-standing adoption barrier.
- **Distribution:** TPUs are being **installed in neoclouds, the first hosting outside Google Cloud**. TPU v8 is close behind. Nanos calls externalization "a one-way street."
- **History:** TPUs were used mostly internally, with model designs built around their fixed-size systolic arrays. That held back open-source models on TPUs.

> "It's quite some time since you've seen a real third competitor to AMD and Nvidia." (Bryan Shan)

### 5. Vera Rubin: incremental system, large inference gain

- **Performance on DeepSeek V4 Pro** depends on the operating point:
  - **~3x better at ~100 tokens/sec per user**, the range where providers actually serve.
  - **~1.4x at maximum throughput**.
  - It can serve speeds (~200 tokens/sec) that GB300 can't reach at all.
- **The driver is memory bandwidth:** **HBM3 to HBM4 is almost 3x**, matching the ~3x gain where inference is bandwidth-bound. This is despite the "despec" to 8-high HBM stacks with less capacity, which matters less because NVL72's scale-up network pools memory across GPUs.
- **Easy to adopt:** there is no new ARM CPU and no new scale-up network, and operators already run liquid cooling. That contrasts with Hopper to Blackwell.
- **New lookup-table quantization:** Rubin adds a hardware-accelerated path that maps 3-bit keys to 8-bit table values, about **3.125 bits per weight**. There are no public uses yet, possibly something the labs use internally. Rubin CPX (a separate chip for the prefill phase) has not been tested yet.
- **Pricing:** Nvidia isn't "price gouging." "If you're going to get three times the performance and the chip doesn't cost two times more… that's a trade everybody's looking to make now going into next year." (Nanos) The team says "Jensen sandbagging again."

### 6. Fast tokens: mostly a niche

- **The team mostly doesn't pay for fast modes.** They run many agents in parallel, so one agent's speed rarely matters.
- **Tool calls are the bottleneck.** A model decoding at ~1,000 tokens/sec (Cerebras) gains little if each tool call takes ~30 seconds.
- **Price:** "I'm not paying $300 per million output tokens." Quilici: Americans "can barely afford Big Macs," so mass willingness to pay ~$100 per million output tokens is doubtful.
- **Their prediction:** coding harnesses will **route** latency-sensitive tasks, such as scaffolding an app, to fast mode and batch the rest, such as overnight benchmark hill-climbing.
- **Nanos's counterpoint:** usage patterns are hard to predict a year out. Bigger models or heavier reasoning could make speed necessary rather than optional, and "faster tokens are smarter tokens" (Jensen) is partly true.
- **Shan:** smaller models won't win, because efficiency gains always get consumed. He compares this to software expanding to fill faster CPUs and RAM.

### 7. TileRT and the threat to fast-token chip startups

- **Context:** OpenAI's ultra-fast mode for "6.1 Soul," announced at Dev Day, was widely tied to its **750MW Cerebras deal**.
- **TileRT** runs a whole model as one "mega kernel" on Nvidia GPUs. It reaches **~200 to ~500 tokens/sec on near-trillion-parameter models**, currently at batch size 1, with slow model support. There is a similar AMD result.
- **Takeaway:** you don't necessarily need specialized SRAM (on-chip memory) architectures to get high interactivity. AI agents are well suited to kernel optimization because results are easy to verify.

**Chip startups:**
- **Short term:** Nanos isn't worried for them, because "demand completely outstrips supply and anybody who can produce chips is going to find a customer."
- **Long term:** startups make or break on **yield, supply chain, server builds, and deployment**, which are harder than designing a fast chip.
- **Groq:** Nvidia's **$20B acquisition** of Groq validates the technical approach.
- **Quilici's skepticism:** many alternative chips still rely on Nvidia GPUs for prefill.
- **Design advice:** fixed prefill/decode ratios across a data center are "totally bunk." Pools need to flex as workloads change.
- **The CUDA moat** is speed of development, not a physical barrier. Expect startups to build separate prefill and decode chips and then struggle to deploy them at scale.

## IV. Portfolio Positioning & Action Items

- **Memory is a durable bottleneck.**
  - HBM scarcity is shaping model architecture itself, which supports HBM pricing for SK Hynix, Samsung, and Micron.
  - Engram and KV-cache offloading also **raise DRAM and SSD content per AI server**. That is a second-order positive for commodity DRAM and enterprise NAND, not just HBM.
- **Nvidia's Rubin cycle looks strong.** ~3x inference throughput at less than 2x price, plus easier deployment than Blackwell, gives operators a clear economic reason to upgrade. Watch for reports of Rubin pricing and allocation.
- **Google TPU externalization is a genuine competitive change.**
  - It is positive for GOOGL (Cloud revenue, plus TPU sales through neoclouds) and AVGO, Google's TPU design partner.
  - Over time it pressures Nvidia's share of inference, though not near-term demand, given supply shortages.
- **Be cautious on fast-inference specialists.**
  - Cerebras-style SRAM architectures face pressure from GPU software (TileRT, mega kernels) and from limited willingness to pay for speed.
  - Their near-term revenue is supported by the overall chip shortage, but the long-term moat is unproven.
- **Inference economics support GPU rental prices and neocloud margins.** ~40–50% profit margins serving open models reinforce the rising H100/GB300 rental prices described in Ep. 037.

**Indicators to monitor:**
- HBM and DRAM contract prices
- DRAM and SSD content per AI server
- TPU availability on non-Google clouds and the PyTorch-on-TPU launch
- Rubin InferenceX results as software matures
- OpenRouter token prices for open models
- Adoption and pricing of fast or ultra-fast modes at OpenAI and Anthropic

## V. Asset Class & Sector Breakdown Table

| Asset Class / Sector | Stock / ETF | View | Rationale / Catalyst |
| :--- | :--- | :--- | :--- |
| AI accelerators | Nvidia (NVDA) | Bullish | Vera Rubin ~3x Blackwell at mid-curve with less than 2x price; easy deployment; TileRT shows GPUs can compete on fast tokens |
| Custom silicon | Alphabet (GOOGL), Broadcom (AVGO) | Bullish | TPU v7 lowest cost per token; native PyTorch backend; TPUs entering neoclouds; v8 next |
| AI accelerators | AMD (AMD) | Neutral | Mentioned as a TileRT-style fast-inference result; TPU becomes a third competitor alongside it |
| HBM / DRAM | SK Hynix, Samsung, Micron (MU) | Bullish | HBM is the binding constraint; engram/KV offload raises DRAM per server; HBM4 delivers ~3x bandwidth |
| Enterprise SSD / NAND | — | Mildly bullish | Engram and KV offload extends to SSD tiers |
| Fast-inference chip startups | Cerebras, others | Cautious | Tool-call bottleneck, $100–300 per million output tokens pricing, GPU mega-kernel competition; long-term success depends on deployment and supply chain |
| Inference providers / neoclouds | — | Bullish | ~40–50% profit margins serving open models at 60% utilization |
| Chinese AI labs | DeepSeek, Moonshot, Meituan (LongCat), Qwen | Watch | Architecture innovation under HBM constraints (MLA, engrams) |

## VI. Cross-References

- [[sa-whos-funding-the-11-trillion-ai-buildout-20261009]]: the same team's capital-markets episode; its ~80% gross-margin and rising-rental-price claims line up with this episode's profit calculator.
- [[deepseek-v4-1-flash-memory-bottlenecks]]: DeepSeek V4.1 Flash memory-hierarchy analysis; this episode adds engram placement at layer 1 and DRAM offload results.
- [[semianalysis-research-2026-07]]: earlier SemiAnalysis themes (Nvidia backstops, Claude Code threat to SaaS).
- [[ai-inference-costs-accounting]]: inference-cost framework behind the TCO-based margins.
- [[google-marvell-broadcom-optical-20260819]]: Google and Broadcom supply-chain comparison relevant to TPU externalization.

## Caveats

- **Self-generated data:** AgentX replays SemiAnalysis's own coding sessions. The team says the workload shape is representative across harnesses, but it is one organization's usage.
- **Profit figures depend on assumptions:** utilization, OpenRouter prices, and the TCO inputs drive them, and the TCO model is a paid SemiAnalysis product ("please buy our TCO model").
- **Transcript quality:** YouTube auto-captions. Several model names and the TPU TCO figure are garbled; model names such as "6.1 Soul" are as spoken.
