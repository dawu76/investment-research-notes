# RW Pro #tradfi-trading — June 2026 Digest

**Source:** Robot Wealth Community (Discord), `#tradfi-trading` channel — a private community for systematic/quant retail traders.
**Period:** 2026-06-01 to 2026-06-30 · 151 messages · ~25 active participants
**Raw transcript:** `rw-pro-tradfi-trading-raw-20260601-20260630.md`
**Purpose:** Thematic summary for an active investor — market sentiment, questions the group grappled with, conclusions reached, and concrete data points. This is retail/practitioner chatter, not research — treat conclusions as hypotheses worth checking, not verified facts.

---

## 1. SpaceX IPO & index-inclusion trade (Jun 2–9) — dominant theme of the month

**Question raised:** Would SpaceX's Nasdaq 100 inclusion replicate Tesla's 2020 index-inclusion rally, and is there still a tradeable edge in front-running index inclusion generally?

**Findings / conclusions:**
- Group consensus was skeptical that the classic "buy pre-inclusion, sell on inclusion date" trade still works. The view (llIHeroic, Euan) is that the edge has been "close to zero" since the market re-priced predictable inclusions in advance; any remaining edge has shifted to modeling/predicting inclusion *before* the public announcement, not trading after it.
- Nasdaq 100 rules were reportedly changed specifically to weight SpaceX 3x, pushing its index weight to 12–15% despite a small 4–5% float — flagged as a setup for outsized passive-flow buying pressure, though no one confirmed the mechanic held up in practice.
- IPO was heavily oversubscribed: Rachit reported "4x oversubscribed" (Jun 11); Sam estimated allocations would be scaled to ~10% of what was applied for.
- Sovereign demand was notable: Sam reported Saudi Arabia and Kuwait sovereign funds placing $1B–$5B orders each (Jun 10).
- Broker mechanics mattered as much as the thesis: IBKR penalizes "flippers" (sell within 30 days → blocked from new IPO applications for 60 days); several German-broker members were surprised to get IPO access at all, since German retail brokers normally don't offer US IPOs — Alex read this as a red flag ("retail customers and etf holders are supposed to be exit liquidity").
- A grey-market pricing gap was noted but not clearly actionable: Sam cited the official IPO pricing at ~$1.77T vs. London grey-market chatter around $2.1T — framed as "an arbitrage type situation...if you can buy IPO shares," i.e. the edge exists on paper but access is the constraint.

**Sentiment:** Cautious/skeptical about the "obvious" trade being tradeable by retail; more interest in the IPO-allocation mechanics and broker access than in a specific market call.

**Quotes / data points:**
> "SpaceX IPO is priced at $1.77 trillion. The London grey markets are pricing SpaceX about $2.1 trillion. Clearly an arbitrage type situation...if you can buy IPO shares." — Sam, Jun 8
> "I think big front runners have made the edge close to zero post announcement." — llIHeroic, Jun 7
> "Beware IBKR flipping policy...if you sell IPO shares within 30 days...you can't apply for any more IPOS for a period of 60 days" — Sam, Jun 9
> "Saudi, Kuwait, said to place $1b-$5b each in orders re SpaceX" — Sam, Jun 10
> "retail customers and etf holders are supposed to be exit liquidity" — Alex, Jun 9

---

## 2. FX trading: retail traps vs. real carry economics (Jun 5–9)

**Question raised:** Is FX a viable strategy market for a systematic trader, or mainly a venue where retail gets structurally disadvantaged? What does the *real* (post-fee) carry trade economics look like across brokers?

**Findings / conclusions:**
- robotkris presented a research update on a "triangulated stat arb" FX signal: **Sharpe 1.3 before costs, 1.5 combined with a sparser variant** — but flagged a data-leakage catch he'd found during validation (an initially "too good" result traced to future-leaking date alignment), used as a cautionary tale about validating suspiciously good backtests.
- Strong shared skepticism of retail FX/CFD products: extreme leverage plus the absence of a Pattern Day Trader (PDT) rule on FX (unlike equities) lets "gurus" market to underfunded accounts (Dan, alvin) — read as a structural reason FX attracts predatory promotion.
- The TRY (Turkish Lira) carry trade was worked through with real numbers: IBKR pays ~5% on long-TRY interest while the true short-TRY rate is closer to 30% — i.e., the broker itself is capturing the bulk of the carry spread. Net annualized yield to the trader was quantified at **~31.5%–34.5%** (Sam), which beat one member's CFD broker's 29% quote.
- CME FX futures vs. IDEALPRO spot: futures show a tighter *headline* spread, but IDEALPRO lets a trader bid/offer inside the spread — so realized execution cost can favor spot depending on how actively you work the order (MidKnight, llIHeroic).
- Regional broker access is a real constraint, not just a data point: Australian and German members reported IBKR/local brokers restricting them to only ~5 major currency pairs on IDEALPRO.

**Sentiment:** Interested in FX as a diversifier (low correlation to existing futures books) but consistently frustrated by broker-specific cost/access friction; no one reported abandoning the idea, but no one reported live capital deployed on FX carry either.

**Quotes / data points:**
> "Sharpe 1.3 before costs, 1.5 combined with the sparse version." — robotkris, Jun 4
> "The net annualized rate you will earn is approximately 31.5% to 34.5%... determined by subtracting the US borrowing rate from the Turkish Lira interbank lending rate." — Sam, Jun 6
> "IBKR gives you 5% for long TRY positions and the actual short rate is like 30%. IBKR still collecting huge carry off their customer's risk positions." — llIHeroic, Jun 5
> "I don't understand why so many 'gurus' push beginners into trading FX & CFDs." — Dan, Jun 5
> "in some products like the euro, it is mostly a 0.00001 spread vs the futures at 0.00005" — MidKnight, Jun 5

---

## 3. Systematic carry & VIX/vol strategies (Jun 16–18) — most technically detailed thread

**Question raised:** How does a live, multi-signal futures carry book actually perform vs. backtest/long-run expectations? What's the right practical setup for VIX-futures carry (calendar rolls, margin, borrow costs)?

**Findings / conclusions:**
- Dan shared live performance of his diversified futures carry strategy (vol-adjusted, sector-weighted, combined with Trend/Skew/Mean-Reversion/Seasonal signals): after **1 year live (started June 2025)**, the carry sleeve alone has been in an atypical regime where **shorts have dominated performance — the reverse of the long-run expectation.** This was shared as a real-world illustration of regime risk in carry strategies, not a red flag on the strategy itself (the blended 5-signal book was described as smoother).
- VIX-complex mechanics: SVIX requires meaningfully higher margin than an equivalent short-VXX position (attributed to SVIX's classification as an inverse/leveraged ETF). Borrow costs on VXX run ~2.98% typically but have exceeded 20% historically (MidKnight); UVXY borrow has exceeded 40% historically and Dan reported outright rejections trying to borrow it.
- Practical execution detail: 4D runs VIX futures **calendar spreads targeting 50/80-day maturities**, rolling one spread every few days rather than rolling the whole position at once — explicitly to reduce the "timing luck" problem Dan flagged with lump-sum rolls.
- V2TX (Euro Stoxx vol futures) was floated as a diversifier but assessed as high-correlation / less liquid relative to VIX futures by the group — "maybe too similar" to be worth the extra trading cost.
- A tangential but concrete idea surfaced late in the thread: Dan noted SSO (2x S&P) may have less decay than UPRO (3x S&P) for a long-only leveraged-ETF strategy, with a longer available history and still-adequate liquidity — a small, actionable position-sizing/instrument-selection note rather than a directional call.

**Sentiment:** Technically constructive; this is the thread with the most concrete, reusable trading mechanics (margin quirks, roll scheduling, borrow-cost thresholds) rather than market opinion.

**Quotes / data points:**
> "shorts have dominated performance which is the reverse of the [long-run behavior]" — Dan, on his carry sleeve, Jun 18
> "VXX has exceeded 20% [borrow cost] in the past" (vs. ~2.98% typical) — MidKnight, Jun 17
> "UVXY has exceeded 40% borrow costs in the past" — MidKnight, Jun 17
> "Calendar, but I make a schedule to roll one spread every couple of days" — 4D, on VIX futures calendar spreads targeting 50/80-day maturity, Jun 17
> "Maybe not intended but just given me an idea that for one of my long strategy maybe I should be using SSO instead of UPRO for less decay" — Dan, Jun 30

---

## 4. Order execution mechanics — IBKR internalization / PFOF (Jun 11)

**Question raised:** Does IBKR's order internalization amount to payment-for-order-flow (PFOF), and does it help or hurt execution quality/cost?

**Findings / conclusions:** No firm consensus. Euan researched it for a group presentation and concluded tentatively that "it probably doesn't matter much for most people." Dan raised two concrete edge cases where it could matter: (a) potential self-match-protection interactions when two of a trader's own strategies route conflicting orders (a MOC order went unfilled because a same-account LOC order filled against the same stock that day); (b) on tiered-commission accounts, internal fills might reduce exchange-fee pass-through, though the expected saving was guessed to be a "rounding error" absent hard data.

**Sentiment:** Low-conviction, informational thread — treated as a cost/mechanics curiosity rather than an actionable edge.

**Quote:**
> "Basic conclusion is that it probably doesn't matter much for most people." — Euan, Jun 11

---

## 5. DJIA reconstitution — Alphabet replaces Verizon (Jun 24–25)

**Question raised:** Is there a tradeable edge around a Dow Jones Industrial Average reconstitution event?

**Findings / conclusions:** ASlan cited the well-known academic finding that stocks *dropped* from major indices (S&P, Russell) tend to show a 1–2% one-year outsized return relative to peers, but explicitly cautioned this may not generalize to the DJIA and is likely too small to be worth trading relative to other opportunities the group discusses. No further pursuit of the idea in the channel — read as "noted, not actioned."

**Quote:**
> "Stocks tend to have a 1-2% outsized return for one year relative to their peers when dropped from indexes like spy and russell. But dont know if that would hold true for DOW and honestly not that big of a return bump." — ASlan, Jun 25

---

## 6. Recurring seasonal trade — end-of-month/quarter index futures (May 30 & Jun 30)

**Question/setup:** A recurring calendar-effects trade was mentioned twice at month boundaries by the same person (Sam): buy stock index futures ~20–30 minutes before the close and exit at the close, on the last trading day of the month/quarter.

**Findings:** Framed as a passive-rebalancing-flow trade (index/passive funds doing calendar-driven end-of-day rebalancing). No backtest stats or win-rate were shared in either instance — it reads as a standing personal heuristic Sam reuses rather than a group-validated edge.

**Quote:**
> "End of month trade: buy stock index futures at 20-30 mins before close and exit at close." — Sam, May 30
> "@Euan end of month/quarter today...calendar effects? Long index futures half hr before close?" — Sam, Jun 30

---

## 7. Minor / one-off signals (low actionability, included for completeness)

- **Jun 23 — SPY premarket print anomaly:** Stefan flagged apparently-buggy premarket SPY prints; Dan and Rachit attributed it to intraday data-vendor discrepancies and stop-loss triggering on a gap rather than a genuine market event. Not actionable.
- **Jun 30 — Synthetic short mechanics for VXX/UVXY:** llIHeroic and Robert K discussed using a long-put + short-call (same strike, "synthetic short") as a borrow-free equivalent to shorting VXX/UVXY when stock borrow is expensive or unavailable, noting the borrow cost still shows up implicitly in the options pricing. A concrete, reusable technique for anyone hitting hard-to-borrow issues on VIX ETPs.
- **Jun 30 — UVXY option spreads look wide:** akhan flagged an ITM UVXY call with a bid/ask of 1.02/1.60 (~36% spread) as unusually wide; Robert K suggested this may partly reflect quotes taken while the market was closed rather than a persistent liquidity problem.

---

## Overall read for June 2026

- **Dominant narrative:** SpaceX IPO and its index-inclusion mechanics consumed most of the month's attention, but the group's own conclusion was skeptical — the "obvious" trades (front-run inclusion, flip the IPO) are seen as largely arbitraged away or blocked by broker policy, with real edge (if any) requiring pre-announcement modeling most members don't claim to have.
- **Highest-conviction/most concrete content:** the VIX/carry futures thread (Jun 16–18) — specific borrow-cost thresholds, calendar-roll scheduling, and margin quirks (SVIX vs. VXX) that are directly reusable, plus a live performance data point (1-year carry-sleeve regime reversal) worth remembering as a base-rate check on carry-strategy expectations.
- **Recurring undercurrent:** distrust of FX/CFD retail products and awareness that brokers capture a large share of "advertised" carry/yield — a theme that resurfaced across the FX (Jun 5–9) and VIX-borrow (Jun 16–30) threads alike.
- **Nothing in June reads as a high-conviction directional call** (long/short a specific asset) — the channel's value this month was almost entirely mechanics, execution costs, and strategy-construction detail rather than market timing calls.
