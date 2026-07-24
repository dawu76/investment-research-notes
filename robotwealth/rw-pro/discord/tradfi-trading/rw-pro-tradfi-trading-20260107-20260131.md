# #tradfi-trading digest — Robot Wealth Community (Jan 2026)

**Period:** 2026-01-07 to 2026-01-31 (no channel activity Jan 1–6)
**Channel:** https://discord.com/channels/1368787013763072040/1370226295941763154
**Source:** `rw-pro-tradfi-trading-raw-20260107-20260131.md` (277 messages, verbatim transcript)

---

## 1. The UVXY-VXZ calendar spread: outside scrutiny, beta-hedge refinements, and a "best trade of 2025" reveal

**Question raised:** Yan opened January by sharing an outside Twitter thread (macrocephalopod) attacking short-UVXY as a strategy, whose backtest looked very different from Euan's — kicking off the month's longest and most technical thread.

- **Euan** dismissed the critique's framing quickly but precisely: *"you can't tell me that shorting this thing is worse [than] being long spy"* — but conceded the outside analysis wasn't wrong about mechanics, just incomplete: *"the observation needs to be translated into a strategy, so details about rebalance frequency etc are very important. without knowing that, he really isn't saying anything concrete."* He added a separate, general principle worth flagging on its own: *"purely directional views shouldn't be traded with options."*
- **robotkris** supplied the number that ended the debate before it really started: in that week's webinar comparison across every "flavour" of vol trade the community runs — costs, borrow, and rebalancing all included — Euan's UVXY-VXZ trade was **the single best-performing vol trade of 2025**. He also flagged the outside thread's actual flaw directly: the twitter version was a 100%-allocation naked UVXY short with no hedge, which is exactly the volatility-drag trap Euan's version is built to avoid.
- User `4D` then did the most substantive independent replication work of the thread: simulating the VX-futures version of the trade (short front-month, long back-month, weighted 50/80 days-to-expiry per a technique attributed to "James" in an earlier webinar) — 5 contracts got results nearly identical to 30 contracts. Adding a beta hedge improved the Sharpe from **1.37 to 2.27** (10 front contracts) and meaningfully tamed the Liberation Day drawdown, though at some cost to final PnL when the backtest was extended back to 2022 (a period 4D flagged as "not great" for the hedged version, since the extra back-month leg bled while the front stayed flat).
- **robotkris** then walked Sam through the actual position-sizing math live in the channel: 2% of $100k allocated to the UVXY short, 2.8x beta hedge into VXZ → 7.6% total notional allocation ($7,600) → roughly **1% annualised vol contribution to the portfolio** — a concrete, reusable worked example other members could copy.
- A few days later (Jan 9), **Euan** added a refinement that matters for anyone replicating this: a *static* 2.8x beta hedge undersells the trade — using an **adaptive, regime-dependent beta** ("2.8 is a common average but mine ranges from 2 to 3.5... use regime dependent betas, VIX high and VIX low") removes the weak-performing middle years entirely. MidKnight followed up with a supporting SSRN paper on regime-based rules for the same calendar trade (abstract_id=5316487).

**Sentiment:** High conviction, evidence-backed — this is treated as the community's flagship vol trade, and the month's activity was mostly refinement (adaptive betas, contract-count efficiency) rather than reconsideration.

**Pull quotes:**
- Euan: *"you can't tell me that shorting this thing is worse the being long spy... the observation needs to be translated into a strategy, so details about rebalance frequency etc are very important."*
- robotkris: *"Euan's UVXY-VXZ trade was the best performing of all the different flavours of vol trades that we do in 2025. Including costs, borrow, rebalancing."*
- Euan: *"Using an adaptive beta makes this a lot more consistent. I don't see the weak performance in those middle years. 2.8 is a common average but mine ranges from 2 to 3.5."*
- 4D: *"The Sharpe ratio is improved to 2.27 from 1.37 with 10 front contracts."*

---

## 2. Portfolio construction masterclass: vol targeting, leverage, and risk budgeting across strategies

**Question raised:** MidKnight admitted a genuine gap — *"I don't have a clear picture on how it all ties in with enough detail"* — asking how position sizing, leverage, and portfolio-level volatility actually connect, and how to combine multiple strategies without a clear feel for aggregate risk.

This produced the single longest, most detailed answer of the month, delivered almost entirely by **robotkris** across more than a dozen consecutive messages — deliberately treated here as one extended answer rather than compressed, since the value is in the full derivation:

- **The core formula.** Dollar allocation to an asset = (target portfolio vol / estimated asset vol) × portfolio value. Worked example: $1M portfolio, 10% vol target, SPY at ~15% long-run annualised vol → allocate $666,667 to SPY.
- **Why "on average" isn't good enough.** A long-run vol estimate only gets you the average outcome; in practice you want a more responsive estimate (e.g., 60-day realized vol) so sizing adjusts to current conditions — with the caveat that even 60-day vol lags what happened yesterday, so in stress you may want to shorten the lookback or pad the forecast to size down faster.
- **On max drawdown as a sizing target.** robotkris was explicit that this is the wrong way to think about it directly — properly, you'd need to dynamically resize as you approach a drawdown limit — but gave the useful shortcut anyway: a normal-distribution approximation (`pnorm(threshold, mean=mu, sd=sigma)`) gives you the probability of being down X% *at a specific point in time*, not the probability of ever touching that drawdown within a window — for the latter, he recommended simulation (the GBM simulator in the RW material) over closed-form math.
- **Rule-of-thumb starting points.** ~8% annualised vol for people just starting out; 15–20% is where robotkris judges his own risk tolerance sits after years of experience; "if in doubt, target less vol to begin with, and gradually scale up until you have trouble sleeping at night — at that point you've found your risk tolerance."
- **A full worked risk-budget example**, treated as a genuinely reusable template: splitting a 15% portfolio vol target across four strategies by *conviction*, not equally — RPH (well-understood, high-confidence effect) gets the largest allocation (8%), Turn-of-month bonds gets less because it's a "decent trade but will disappear eventually" and its own vol estimate is deceptive due to sparse positions, with the rest split between the vol-slaying strategy and UVXY-VXZ. He was careful to flag that per-strategy vol contributions **aren't additive** — combined they land lower than the naive sum (his estimate: the four strategies at his stated allocations would land around 10–11% combined, not 15%) — giving you a scaling factor (target/realized) to gross everything back up if you actually want to hit your full vol budget.
- MidKnight and Rachit followed up with clarifying math (converting notional to ES/MES contract counts, applying the same framework to crypto perp funding arbitrage), and akhan asked the natural follow-on question about the *cost* of leverage itself — robotkris's answer was simple and general: *"think of leverage as a tool that lets you hit your vol target... the higher the [financing] costs, the less attractive it will be."*
- robotkris closed the thread candidly, underscoring how genuinely hard this is to communicate even for an expert: *"As I write all this down, I realise it's actually a bit more convoluted than it feels in my head... We really need a walkthrough with real data, real simulations, real code/spreadsheets."*

**Sentiment:** Extremely high value, explicitly flagged by robotkris himself as underdocumented — multiple members (Rachit, Yan) said afterward this was the clearest explanation of vol-targeted position sizing they'd seen, and robotkris committed to building better training material on it.

**Pull quotes:**
- robotkris: *"The key thing to figure out is what level of dollar exposure gives you the volatility exposure you want."*
- robotkris: *"For people just starting, I think ~8% is a good place to start. If in doubt, just target less vol to begin with, and gradually scale up until you have trouble getting to sleep at night. At that point, you've found your level of risk tolerance."*
- robotkris: *"those vol contributions aren't additive... you might go 'I'm happy with that buffer' ... or you might go 'I am here to ball, and I want my 15% portfolio vol.' Also fine."*

---

## 3. Sam's live event-vol trading book — an expanding playbook

**Question raised:** Prayaag asked Sam directly to enumerate his event-trading playbook, after watching a steady stream of trade call-outs throughout the month.

Sam's answer, confirmed in the transcript: macro announcements (FOMC, CPI, NFP), the weekly NG/EIA storage report, the BCOM index rebalance (new this month — see Theme 5), and SCOTUS tariff-ruling short-vol trades. The live trades themselves ran throughout January with real, quotable pip outcomes:

- NFP/tariff-SCOTUS shorts: +50 pips (Jan 9), −60 pips on a "not ruling today" miss (Jan 20), +110 pips on a repeat SCOTUS non-ruling (Jan 14), +250 pips on UVXY around the Davos/Trump-speech period (Jan 21).
- Natural gas storage shorts: −6 pips (Jan 22, deliberately sized smaller given the week's outsized NG strength), +60 pips (Jan 29).
- **Euan** weighed in on the SCOTUS-specific trade with a distinction worth keeping: it's a good short-vol candidate because uncertainty resolves on the ruling, but *"the thing that makes this harder than FOMC or earnings is the timing uncertainty"* — you don't know exactly when the ruling lands, only that it's pending. He extended the logic further, unprompted, into a broader risk-map comment: *"we still have the uncertainty of trump invading greenland, but sooner or later he will run out of countries to invade so that's good... but nothing is ever in isolation. we just keep looking for edges even if different edges might layer or conflict."*
- Sam also asked Euan directly whether it's positive-EV to short vol ahead of Trump's scheduled remarks specifically versus Treasury auctions — Euan's answer was a clean split: *"Trump yes. Auction don't know."*

**Sentiment:** Active, expanding playbook, run with real capital and transparently reported outcomes (wins and losses both posted) — the group increasingly treats Sam's event calendar as a shared community resource rather than a personal trade log.

**Pull quotes:**
- Euan: *"the supreme court ruling is a good example of something where vol will probably come in once uncertainty is removed. the thing that makes this harder than FOMC or earnings is the timing uncertainty. but short vol seems like a solid play for that."*
- Euan: *"but nothing is ever in isolation. we just keep looking for edges even if different edges might layer or conflict."*
- Sam: *"Shorted uvxy ahead of scotus ruling on tariffs... SCOTUS says will not rule today! out of UVXY, +110 pips."*

---

## 4. BOIL/natural gas: anchoring risk, a record-breaking move, and geographic extension to Europe

**Question raised:** Sam's ongoing BOIL short position (continued from December) grew uncomfortably large in share count by mid-January, prompting a direct question to the group about whether that's a red flag — which then widened into a broader discussion of whether the US NG playbook travels internationally.

- Sam flagged the discomfort plainly: *"Anyone else having to keep shorting BOIL to maintain the exposure? Bit scary the number of shares I've done."* **Euan's** answer reframed the anxiety as a cognitive bias rather than a real risk signal: *"it wouldn't be scary if you weren't anchored to the number of stocks you did initially"* — the dollar exposure is what matters, not the nominal share count, which mechanically grows as BOIL's price decays.
- The move that made this relevant: natural gas had its **largest weekly gain since 1990** (Jan 22, per a Yan-shared news clip), over 70% in a week. Euan's immediate caution against over-generalizing: *"Energy seems to be geography specific and subject to different extraction methods and distribution channels"* — i.e., don't assume a US Henry Hub pattern implies anything about European gas without checking.
- Prayaag asked the natural next question — could the "short NG over US winter" trade extend to shorting Dutch TTF futures over the European winter for a geographic diversification benefit? **Dan** gave the most substantive answer: TTF doesn't have as long a price history as US NG for backtesting, but UK Natural Gas futures (a reasonable proxy, ~95% correlated with TTF) go back further — clean data to 2009 for the UK, TTF itself only to 2017 and "a bit scratchy." He backtests on UK gas but trades TTF live.
- The thread got a concrete follow-up close on Jan 30: `4D` reported backtested results for the extended European trade — **Sharpe 2.4 in 2025**, **Sharpe 1.0 since 2023** — giving the group an actual number to weigh the diversification claim against.

**Sentiment:** Constructive and self-correcting — the anchoring-bias catch and the geography caution both landed as genuine risk-management improvements rather than pushback on the trade itself.

**Pull quotes:**
- Euan: *"it wouldn't be scary if you weren't anchored to the number of stocks you did initially."*
- Euan: *"Energy seems to be geography specific and subject to different extraction methods and distribution channels."*
- 4D: *"it's a sharpe 2.4 trade in 2025 / sharpe 1.0 since 2023"* (Dutch TTF winter-short extension).

---

## 5. A newly discovered edge: BCOM index rebalance flows in silver (and cocoa)

**Question raised:** None initially — Sam simply started posting live trade results shorting silver "into the rebalancing," which prompted the group to reverse-engineer what he'd found.

- Sam's live trades across the week: +73 pips, then +33 pips after reversing to long once "the selling has stopped" (his read: the imbalance itself is the edge, not a directional view), then a mixed +60/−90-then-+120 sequence as the rebalance window closed out.
- Once Rachit and akhan asked what the actual trade was, Sam clarified: the Bloomberg Commodity Index (BCOM) does its annual constituent-weight rebalance over several trading days each January, and the reshuffle this year required heavy selling of silver futures (and buying of cocoa) at a specific time each day — *"you have to exit the short when they stop selling... about 8 mins time. Imo thats the edge."*
- **robotkris** did the confirming research and brought back the primary source: BCOM rebalances only once per year, so *"those flows while infrequent, should be quite large, especially when something's gone up as much as silver has"* — and linked Bloomberg's own target-weights announcement page so the group has the mechanism in writing, not just Sam's observation.
- `4D` nailed down the precise execution detail that makes the trade tradeable rather than just observed: the rebalance hits **~30 minutes before the futures close**, specifically **6:24pm London time**, with a visible one-minute volume spike confirming the exact moment.

**Sentiment:** Genuine new-edge discovery, quickly validated by the group and given a hard mechanical explanation (not just correlation) — a good example of a member's personal observation becoming a documented, sourced community trade within the same week.

**Pull quotes:**
- Sam: *"but you have to exit the short when they stop selling...about 8 mins time. Imo thats the edge."*
- robotkris: *"BCOM rebalances only once per year. So those flows while infrequent, should be quite large, especially when something's gone up as much as silver has."*
- 4D: *"Yes, the rebalance occurs at 6.24pm London time. You can see a huge spike in volume in that 1 min bar."*

---

## 6. SPY/TLT month-end rebalance: mechanism confirmation and an entry-timing variant

**Question raised:** Yan flagged the standard month-end timing for the mechanical stocks/bonds rebalance trade; the thread that followed tested whether the trade's premise (rebalancing-flow-driven) actually holds up in the data, and surfaced an alternative execution style.

- TheCTAFan mentioned using a 1% absolute-difference threshold as an entry filter rather than trading every month regardless of magnitude; Yan pushed back gently that for this specific trade he prefers not to over-engineer a simple rule, since the underlying spread between using a threshold and not barely differs.
- **robotkris** brought data to settle the "is this really rebalancing-driven" question: backtested performance is worse in periods with *less* rebalancing to do — direct support for the flow-based explanation rather than a coincidental pattern — and floated an interesting extension worth someone testing: unusually volatile periods might trigger *vol-driven* rebalancing on top of the normal performance-driven flows, potentially a distinct, addable signal.
- TradeQuantiX shared a genuinely different implementation worth noting on its own: rather than a single entry at month-end, space entries out starting the 20th, scaling in every 2 days, and **re-measure the SPY/TLT relative-performance relationship at each scale-in** — meaning the trade can flip which side it's buying mid-month if the outperformance relationship reverses before the position is fully built.

**Sentiment:** Confirmatory — the group validated their own mechanistic explanation with real backtested evidence rather than just holding an untested belief, and picked up a legitimately different execution variant along the way.

**Pull quotes:**
- robotkris: *"if it's driven by rebalancing flows as we think it is, it should do worse when there's less rebalancing to do. The data backs this up."*
- robotkris: *"It might be interesting to see what happens when one has been unusually volatile — you could also get vol-driven rebalancing as well as performance driven."*
- TradeQuantiX: *"with each scale in I remeasure the SPY/TLT relationship. So the first buy on the 20th may buy SPY, but if the outperformance/underperformance relationship flips as the month comes closer to the end I flip to buying both spy and tlt in different weights."*

---

## 7. Implementing turn-of-month bond trades for EU-based traders

**Question raised:** akhan, based in the EU where US-domiciled ETFs aren't available to retail investors, asked how to implement the month-end TLT rebalance trade using interest rate futures instead.

Yan's answer covered both routes: UCITS-compliant ETFs exist as a direct substitute for the stocks/bonds rebalance trade, but he personally prefers futures for capital efficiency (bond futures specifically, not generic interest-rate futures). M4TZEHDF supplied the concrete ticker EU traders need — **IS04**, the UCITS equivalent of TLT. Sam then gave his own futures-based mechanics for anyone wanting the leveraged route regardless of domicile: buy the notional bond exposure directly via the front-month 10-year future (e.g., ~£1M notional against ~£5k margin posted), exiting at month-end — extremely capital efficient (~0.5% margin requirement) but, as Sam noted, essentially a leveraged position by default that needs to be sized with that in mind.

**Sentiment:** Practical problem-solving — a genuine access barrier (EU retail restrictions) got a full solution (ticker + futures alternative) within the same discussion.

**Pull quote:** Sam: *"Say I want a million pounds of bond exposure, I just buy 1 million pounds notional value of March 10 year bond future depositing 5k pounds in the account....exit at the end of the month or whenever."*

---

## 8. Shorter threads worth flagging

- **Treasury basis trade feasibility.** Sam asked whether the classic cash-futures basis trade is accessible to retail; bdkoepke (a former momentum-fund PM/head trader) gave a grounded no: retail traders lack repo market access, synthetic repo via box spreads is possible but "not convinced the juice is worth the squeeze," and it further requires portfolio margin plus a broker that correctly implements futures/securities cross-margining — which, to his knowledge, IBKR does not outside limited circumstances.
- **Momentum investing implementation details.** Following a Jack/Wes-style momentum book reference, bdkoepke (revealing his own past as a PM on a momentum-focused fund) shared concrete implementation refinements: avoid buying names shortly after positive-jump events (earnings surprises, FDA approvals) since those aren't "smooth" trend continuation; a specific smoothness-screening methodology; and a note that ETFs carry a structural tax advantage individual traders can't replicate.
- **A broker risk-management horror story.** jgao_imm described a same-day "triple" margin call at Schwab — a $6M margin hike triggered by position concentration warnings across three unrelated positions (ETHA puts, SPX calls, ES futures hedges) that Schwab wouldn't explain the grouping logic for, leaving the account restricted from even hedging while the warning was active. Prompted general broker-support grievances (MidKnight has since moved day-trading to a broker with a direct phone line).

---

## Overall read

January was the month the community did its homework on its two flagship strategies. The UVXY-VXZ trade survived an outside attack not by dismissing it but by producing hard numbers (best vol trade of 2025, Sharpe improvements from beta-hedge refinement) and a genuine methodological upgrade (adaptive, regime-dependent betas from Euan). **robotkris**'s multi-message portfolio-construction walkthrough was the standout educational contribution of the month — a first-principles derivation of vol targeting, leverage, and multi-strategy risk budgeting that the group explicitly recognized as underdocumented and worth turning into permanent training material.

Beyond the two anchor threads, January was also a month of edge discovery and validation discipline: Sam found the BCOM silver-rebalance flow trade and the group didn't just take it on faith — robotkris sourced the mechanism, and 4D pinned the exact execution window. Similarly, the SPY/TLT rebalance trade's core premise (flow-driven, not coincidental) got tested against data rather than assumed. Where the record-breaking natural gas move might have tempted overconfidence or hasty geographic extrapolation, **Euan**'s recurring instinct — flagged three separate times this month (BOIL anchoring, NG geography, "nothing is ever in isolation" on event trading) — was to catch the cognitive shortcut before it became a position-sizing mistake.
