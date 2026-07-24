# RW Pro Discord — #data-analysis digest, June 2026

- **Period:** June 1–30, 2026
- **Channel:** https://discord.com/channels/1368787013763072040/1368844739465707572
- **Raw transcript:** [rw-pro-data-analysis-raw-20260601-20260630.md](./rw-pro-data-analysis-raw-20260601-20260630.md)
- **Volume:** A quiet, low-traffic channel this month — 25 main-channel messages clustered into two distinct technical threads (spread estimation, then vol-drag/vol-signal ensembling), with a ~12-day silent gap between them and a further gap after June 28.

---

## 1. Estimating bid-ask spreads without quote data (Corwin-Schultz)

deal_me_in shared that he'd added a risk model to his automated trading system that blocks trading any asset with a wide estimated spread, using the **Corwin-Schultz model** — which estimates spread from daily high/low data alone (no quote/tick data needed) — and asked if anyone had real-world experience with it. Euan gave a qualified "kind of": he'd done extensive prior work on spreads and market impact but found a simpler rule worked well enough in practice — **spread = k·√(trade volume)** — while noting k must be calibrated per-stock. He pointed to a more robust volatility-based variant in "Volatility Trading" (page ~111 in the print edition, though deal_me_in's Kindle edition numbered it closer to page 109/equation 4.18 — a good reminder that page references from print books don't map cleanly to e-readers). The technique is described as applicable to both stocks and ETFs, in the transaction-cost-estimation section near the end of chapter 6.

**Sentiment:** Practical, low-friction knowledge transfer — a specific, actionable reference (with the caveat that Euan personally moved past pure spread-formula approaches to a volatility-based one and never felt the need to revisit).

**Pull quotes:**
- deal_me_in: *"I have added a risk model that prevents trading of any asset with a wide spread. Im currently using the Corwin–Schultz model to estimate the spread using daily highs and lows."*
- Euan: *"I found the rule 'spread = k*sqrt($trade volume)' worked pretty well. but you need a different k for each stock so you can go a bit further and convert it into something which has volatility in it."*

## 2. Vol-signal ensembling: combining VIX-basis and "slayer" signals

Rachit described experimenting with two volatility-timing signals — "VIX basis" and "slayer" — both of which produce binary long/short-vol switches on their own. A simple ensemble rule (only take a position when both signals agree; otherwise stay flat) modestly improved performance. He asked whether it was worth the extra effort to smooth things further via decile-sorting each signal before combining, or via position sizing off VVIX, for what he estimated might be only a ~0.05bps marginal improvement. robotkris's framing: distinguishing genuine signal improvement from noise here is inherently hard because large vol explosions are rare events — with so few observations, any rule that happens to sidestep one bad event can look much better in-sample without that being statistically meaningful. His practical advice: keep position sizing modest and accept the variance rather than over-engineer the ensemble. Andre (independently running a similar ensemble) added a concrete refinement: instead of the slayer signal flipping directly from short to long at a single z-score threshold, add a **flat/neutral zone** — e.g., short below a 1.0 z-score threshold, flat between 1.0 and 1.75, only flip long above 1.75 — which reduces needless whipsaw around the threshold.

**Sentiment:** Rigorous and appropriately humble — explicit acknowledgment that small-sample tail-event backtests are easy to overfit to, with a concrete, low-complexity fix (flat threshold zone) that multiple members independently arrived at.

**Pull quotes:**
- robotkris: *"those vol explosions happen infrequently enough that anything that sidesteps one of them can make the performance look a lot better, but because the number of observations is small, it's very hard to infer whether [it's a genuine improvement]."*
- Andre: *"instead of flipping directly from short to long and vice versa"* — use *"a flat threshold for the slayer... from 1.0 to 1.75 you're not short anymore, you're flat."*

## 3. Quantifying volatility drag on leveraged ETFs (UVXY case study)

Growing out of a Discord thread deal_me_in started ("Impact of volatility drag," 6/17 — in-thread replies not captured by this extraction, but the discussion continued in the main channel), deal_me_in pushed back on the common assumption that shorting UVXY captures a reliable "volatility drag" edge. His own analysis suggested the opposite in some cases: he computed an "annualized_drag" metric per asset, finding that a fund like **UPRO can lose roughly 200% a year to volatility drag**, but crucially that a *negative* annualized_drag value means drag is actually acting as a *tailwind*, not a cost. His conclusion for UVXY specifically: since UVXY already structurally trends toward zero, volatility drag doesn't help you extract extra edge shorting it — it just accelerates money going to zero regardless, so the "drag as an edge" framing was misapplied in his own earlier thinking. Euan clarified the correct way to measure drag empirically: compare the realized return of a leveraged product to the theoretical multiple of its underlying's return (e.g., a 3x ETF "should" return 3x the base product; any shortfall from that multiple is the drag). robotkris pointed to TLQ Module 1's treatment of vol drag as a good intuition-builder, reinforcing Euan's simple framing: an asset that goes up then down will show more drag in its leveraged version than a monotonic trend would. deal_me_in ultimately converged on a pragmatic simplification: rather than fully modeling the mechanics, just approximate **vol drag ≈ variance / 2**, while noting his own math (which he credits Euan's book chapter for proving) suggests trending assets (he cites TMF as an example) can actually *benefit* from vol drag rather than being hurt by it.

**Sentiment:** A genuine, worked-through correction of a common oversimplification ("shorting leveraged/inverse products = free vol drag edge") — useful case study distinguishing when vol drag helps vs. hurts based on whether the underlying trends or mean-reverts.

**Pull quotes:**
- deal_me_in: *"so UPRO costs you like 200% a year in vol drag. If annualized_drag is negative, then the vol drag is actually a vol tailwind."*
- Euan: *"the way to see the drag is to look at the return on the base product and compare that to the return on the leveraged version. So a 3x ETF should have 3 time the return of the unleveraged. Any underperformance [is the drag]."*
- deal_me_in (final synthesis): *"vol drag won't always make everything go to zero. Things that trend can benefit from vol drag (TMF for example)... [for UVXY] its trending down, so its just gonna incinerate more money and vol drag is gonna increaee that loss."*
- deal_me_in: *"ill just calculate vol drag as variance / 2 and be done with it."*

---

## Overall read

June's #data-analysis was low-volume but high signal-to-noise — two tightly-scoped technical threads rather than scattered chatter. The spread-estimation discussion (Corwin-Schultz vs. a simpler volatility-calibrated k·√volume rule) is a useful reference for anyone building execution/risk-filtering logic without full quote-level data. The bigger takeaway is the volatility-drag thread: deal_me_in's worked example is a good corrective against the common retail assumption that shorting leveraged/inverse ETFs is a "free" structural edge — the sign and magnitude of vol drag depends heavily on whether the underlying trends or chops, and a trending decay product like UVXY doesn't offer the same drag-capture opportunity as a mean-reverting one. The vol-signal ensembling thread (VIX basis + slayer, with a flat-zone refinement) is directly actionable for anyone running similar binary vol-timing signals, with a clear-eyed caveat from robotkris about how easy it is to overfit position-sizing "improvements" to rare tail events with few historical observations.
