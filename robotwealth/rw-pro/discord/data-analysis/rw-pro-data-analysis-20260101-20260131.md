# RW Pro Discord — #data-analysis digest, January 2026

- **Period:** January 1–31, 2026
- **Channel:** https://discord.com/channels/1368787013763072040/1368844739465707572
- **Raw transcript:** [rw-pro-data-analysis-raw-20260101-20260131.md](./rw-pro-data-analysis-raw-20260101-20260131.md)
- **Volume:** 41 main-channel messages, all clustered from January 20 onward (no channel activity in the first three weeks of the month). Ben was the dominant contributor this month — a detailed data-integrity debugging session, a full strategy-portfolio writeup for a newcomer, and an extended RealTest walkthrough that pulled in several other members' questions.

---

## 1. Diagnosing a Norgate-vs-Lab data discrepancy in the UVXY/VXZ trade

Ben noticed the UVXY/VXZ trade behaved differently when run on Norgate data versus the Lab's own dataset, and asked whether this traced back to Norgate being adjusted from day one versus the Lab data only being adjusted over the testing period — the divergence appeared specifically from partway through 2022 to partway through 2024.

robotkris's only input was a diagnostic prompt rather than a direct answer — asking Ben to post a sample of the data being compared — which nudged Ben into self-diagnosing rather than being handed a fix. Ben worked through it live in the channel over several messages: plotted both series and initially found them identical per-symbol, then traced the real issue to how RealTest references adjusted versus unadjusted prices in different parts of its calculation pipeline. The root cause: RealTest uses unadjusted prices, and because UVXY has gone through reverse splits, unadjusted prices should be *larger* further back in time — his brain kept reading the large numbers and assuming "adjusted," which threw off his return calculations, even though it was fine for trade simulation. Since UVXY carries significant structural decay, using the unadjusted price series for return calculation (rather than trade simulation) would have distorted the equity curve.

**Sentiment:** A textbook self-resolved data-hygiene bug — worth flagging for anyone else using RealTest with instruments that have reverse-split history, since adjusted-vs-unadjusted confusion is exactly the kind of error that's easy to overlook and hard to spot once it's baked into a backtest.

**Pull quotes:**
- Ben: *"Realtest uses unajusted prices and since they are reverse splits adjusted should be larger further back... this is fine for trade simulation but not for return calculation as returns will be distorted."*
- Ben: *"since UVXY has significant decay this will distort the equity curve if Realtest is using the unadjusted price series to calculate returns and simulate trades"*

## 2. Ben's full RW Pro strategy roster, shared with a newcomer

TradeQuantiX, new to the course, asked whether the strategies Ben had been discussing were all part of RW Pro. Ben's reply was a comprehensive strategy-by-strategy breakdown of his live portfolio:

- **Tactical Asset Allocation** — essentially RW Pro's Risk Premia Harvesting strategy.
- **VRP** — the RW Pro VIX basis trade; **uvxy_vxz** — the RW Pro VIX calendar spread. Everything else in his portfolio is custom, not from RW Pro directly.
- **IDX_MR** — a simple Nasdaq mean-reversion trade.
- **Mean Reversion** — a group of ~5 long/short mean-reversion strategies spanning Russell 1000, Russell 2000, Nasdaq, and all listed stocks (with a liquidity filter) — simple rule sets, generally one main signal plus a liquidity filter and sometimes a trend filter.
- **PEAD** — post-earnings-announcement-drift, built from features derived from his own discretionary earnings trading, ranked via machine learning, rotating weekly, long/short. Performing "ok" but slated for a full review incorporating RW/RW Pro learnings.
- **Momentum** — 3 simple technical momentum strategies plus a trend filter, monthly rotation, long only.
- **Value Momentum** — technical momentum combined with value features, ranked via machine learning, long top-N/short bottom-N, monthly rotation.
- **ST break** — short-term breakout on a handful of ETFs, fully intraday with market-on-close exits, long/short.

**Sentiment:** Generous, detailed onboarding — a real map of how one active member structures a multi-strategy live portfolio, useful as a reference point for what a "full" RW-derived strategy stack can look like in practice.

**Pull quote:**
- Ben: *"Tactical Asset Allocation is essentially the Risk Premia Harvesting strategy in RP Pro though. VRP is the vix basis trade in RP Pro and uvxy_vxz is the vix calendar spread in RP Pro. The rest are different."*

## 3. Spotting a non-random (but non-monotonic) volume/returns relationship in crypto

Rachit shared a chart exploring the relationship between trading volume and forward returns in crypto, asking if it looked like a genuine relationship. TradeQuantiX's first read: higher volume roughly maps to positive returns. Rachit refined that with a caveat — some reversion visible at the lower end of the volume range.

**robotkris gave the more rigorous read**, and it's a good example of pattern-reading discipline rather than pattern-matching to a story:
- His framing: with exploratory relationships like this, the goal is to look for anything that departs from pure randomness, not necessarily a clean textbook shape.
- He confirmed the basic direction (lower factor values → lower returns, higher factor values → higher returns) but was explicit that it's **not a clean, monotonic relationship** — a distinction he drew out directly rather than skipping past.
- Despite the non-monotonicity, he judged it "certainly looks non-random," and flagged a specific sub-pattern worth investigating further: buckets 1 and 2 (the very lowest volume bucket) showing suggestively higher returns than the immediately adjacent bucket — a detail easy to miss if you're only looking for a simple linear story.

**Sentiment:** A good worked example of exploratory data analysis discipline — distinguishing "non-random" from "clean and monotonic," and specifically calling out a low-volume sub-pattern that a naive read (TradeQuantiX's "higher volume = positive returns") would have missed entirely.

**Pull quotes:**
- robotkris: *"With this stuff, you want to be on the lookout for anything that looks non-random... Is it a nice, clean, monotonic relationship? No... But it certainly looks non-random to me."*
- robotkris: *"Potentially something interesting in buckets 1 and 2 - suggestive of slightly higher returns on very low volume?"*

## 4. Finding RW Pro strategy documentation in one place

neeravbm asked Ben where to find the strategies and corresponding notebooks he'd referenced, noting it was hard to access RW Pro info from a single location. Ben pointed to two resources: the `rw-portfolio` GitHub dashboard (recent info and cross-strategy comparison — recommended as the starting point) and the public "Index of Strategies" page on robotwealth.com (for working through the full historical lecture/build-out material).

**Sentiment:** Quick, practical navigation fix for a common new-member pain point.

**Pull quote:**
- Ben: *"Try the dashboard first as that is the recent info and comparison of strategies then the index if you want to run through all the past lectures and building of the strategies."*

## 5. RealTest for multi-strategy portfolio analysis and daily order generation

Growing out of a correlation-in-drawdowns idea Ben had shared (Matt G asked how he filters to just drawdown periods for that correlation calc — a question that went unanswered in-channel this month), Ben gave a detailed account of his production workflow using **RealTest**, a portfolio-analysis and order-generation tool built by Marsten Parker (of Market Wizards fame):

- For every new strategy he adds, he checks its correlation to existing strategies, its volatility and volatility-contribution to the combined portfolio, max drawdown, CAGR, and Sharpe.
- Daily workflow: import updated Norgate (or Yahoo/other) end-of-day data (~1 minute) → generate orders (~15 seconds, sometimes ~100 orders) → transmit via IBKR's Orderclerk (~5 seconds) → repeat per account/portfolio.
- For more complex signals (e.g., machine-learning-based strategies), he runs the model in Python and imports the output values into RealTest via CSV.
- He flagged a free trial and a free RealTest course from Enlightened Stock Trader as a good starting point for others.
- Follow-up detail (prompted by TimExcellent asking about tracking multiple strategy "portfolios" within one IBKR account — i.e., **sleeve accounting**, a term bdkoepke supplied, who separately noted corporate actions are the tricky part of sleeve accounting to get right): Ben described running two live portfolios — **High Octane** (5 long/2 short intraday mean-reversion strategies sharing capital/leverage, entering on limit orders and exiting via MOC) and **Quantifiable Alpha** (his main multi-strategy portfolio, mixing daily/weekly/monthly strategies, trackable both individually and as combined groups) — and confirmed RealTest can in theory track one large portfolio across multiple accounts/balances with rebalancing between them, though he currently runs them as separate portfolios.

**Sentiment:** A genuinely detailed, practitioner-level walkthrough of a real production trading workflow — the kind of concrete operational detail (exact timings, specific config choices) that's more valuable than a general tool recommendation.

**Pull quotes:**
- Ben: *"I press orders to generate orders, which takes about 15 seconds and might include 100 orders, I then log into IBKR, open Orderclerk and hit transmit, which takes about 5 seconds."*
- Ben: *"Quantifiable Alpha portfolio is my main portfolio and the strategies can all be tracked individually or as combined strategies and then as a combined portfolio... Whilst Quantifiable Alpha tracks both strategies and groups of strategies, High Octane just tracks strategies."*
- bdkoepke: *"That's more commonly known as sleeve accounting, where that gets tricky is when you have corporate actions."*

## 6. Data-sourcing gaps: international options, non-US XBRL, and HK coverage

Branching off the RealTest discussion, bdkoepke raised two open data-sourcing questions that didn't get resolved this month:
- A good source for **international options data** (equities primarily, ideally futures options too) — he's only aware of ORATS for US coverage, and CSI Data's futures options exist but the "last" price field is unreliable (can reflect a trade executed hours earlier).
- Whether any country besides the US makes extensive use of **XBRL** for fundamentals data — Canada's SEDAR was cited as a negative example (unstructured PDFs), though cross-listing of many Canadian securities partially offsets the coverage gap.

TimExcellent responded that he's "resigned" to using ORATS plus ETFs to approximate commodities exposure where direct data isn't available, and separately noted he'd love to see Hong Kong stock and options coverage (echoing a want previously raised by MidKnight in an earlier month — see February's #4 Databento thread).

**Sentiment:** Open questions, no resolution — worth flagging as unmet data needs in the community if anyone has since found sources.

**Pull quote:**
- bdkoepke: *"I'm aware of orats for US only, and csidata has futures options but their last price is contrived ('last' could have been executed hours earlier...)."*

## 7. RealTest vs. Python, and how well AI coding assistants handle each

Closing out the month, alvin flagged a real friction point with RealTest: unlike Python (well-documented, widely used, so Claude/Gemini can generate working code easily), RealTest's more niche syntax trips up AI assistants even when fed the platform's own documentation and example code — producing code that fails basic syntax checks. He asked Ben whether he vibe-codes RealTest scripts or writes them by hand.

- Ben: a mixture of both — vibe-codes the more complex bits, and otherwise leans on a community-made "RealTest GPT" (searchable on the forum) or feeds it excerpts from the RealTest guide directly.
- Dan (also a RealTest user): finds Python complex enough that AI assistance is close to essential there, whereas RealTest, once you're familiar with it, is often fast enough to prototype by hand — he described disproving an idea seen online in about 5 minutes by adapting an existing template script. More complex ideas (academic-paper-derived signals, multi-strategy portfolios) are harder either way.
- alvin's takeaway: he leans toward Python specifically *because* he can lean on AI tools to cross-check logic; in RealTest's more niche language, he's "pretty much in the blind" for complex requirements.
- Dan and Ben separately named specific AI coding tools they rely on: Dan uses Cursor mainly for data cleansing/transform/integration work (and expects to lean into Python more for RW Lab-style research); Ben highlighted Augment Code as particularly strong for larger projects.

**Sentiment:** A candid, practical comparison of tooling ergonomics — AI-assistant quality is emerging as a real factor in platform choice (Python vs. RealTest) for strategy development, not just the platforms' own feature sets.

**Pull quotes:**
- alvin: *"unlike Python which is very well documented and popular, Gemini and Claude cannot give me the code I want for RT... they'd spit out some gibberish that even fails the syntax checks."*
- Dan: *"I think python is complex enough and needs enough lines of code to do things that AI helps alot. With RT though - once you get used to it you should find it simple enough to open a template and plug in the bits fairly quickly."*

---

## Overall read

January's #data-analysis was quiet until the 20th, then dominated by Ben — a self-resolved data-adjustment bug in a live UVXY/VXZ comparison, a full strategy-portfolio breakdown for a newcomer, and a detailed RealTest production workflow that pulled in questions from four other members. robotkris's two contributions this month were both about analytical discipline rather than direct answers — nudging Ben to self-diagnose with real data rather than handing him a fix, and modeling how to read an exploratory relationship chart carefully (non-random but non-monotonic, with a specific sub-pattern worth flagging rather than accepting the first plausible story). The RealTest-vs-Python-and-AI-assistants thread closing out the month is a useful signal in its own right: platform choice for strategy development is increasingly being shaped by how well each platform's syntax plays with Claude/Gemini/Cursor, not just by the platform's native feature set. Two open data-sourcing gaps from bdkoepke (international options, non-US XBRL coverage) remain unresolved and worth revisiting.
