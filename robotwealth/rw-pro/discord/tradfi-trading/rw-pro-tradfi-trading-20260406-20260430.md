# RW Pro Discord — #tradfi-trading digest, April 2026

- **Period:** April 1–30, 2026 (channel was quiet April 1–5; content begins April 6)
- **Channel:** https://discord.com/channels/1368787013763072040/1370226295941763154
- **Raw transcript:** [rw-pro-tradfi-trading-raw-20260406-20260430.md](./rw-pro-tradfi-trading-raw-20260406-20260430.md)
- **Volume:** 82 messages. A research-heavy month with no single dominant event — instead a steady stream of specific, testable trade ideas (commodity roll/congestion trades, NG storage announcements, country-ETF mean reversion, closed-end fund discounts) alongside a live discretionary experiment (Euan's Sunday night reversal) that ran its full course from idea to disproof within the month.

---

## 1. Commodity futures roll/congestion trades, sparked by the Flirting With Models podcast

TheCTAFan flagged a podcast episode full of commodity risk-premia ideas, which **Dan turned into the month's most developed research thread**:

- Dan proposed "the congestion trade" as the most approachable idea to explore: buy futures ahead of the BCOM/PDBC index roll, sell after the roll completes, then flip short — structurally similar to the equity window-dressing trade. He noted it could also be explored at the individual-fund level (naming PALL, WOOD, SLV, IAU as candidates) since those may have less liquidity impact than the index-level trade.
- He contrasted this with curve carry, which he trades in a single-legged form himself but called "a huge project" to build out in a properly diversified manner — it took him months to reach a final version, making the congestion trade the more tractable starting point from a pure edge-exploration perspective. He also flagged the dynamic difficulty of curve carry: choosing which contract-type of carry to trade (Z-score, mean-reverting, absolute, ranked/market-neutral) creates real analysis paralysis.
- **robotkris confirmed interest directly**: these are exactly the kind of trades RW should be looking at.
- Dan raised a crowding concern — if CTAs are already trading the front-month congestion trade, retail traders may need to look at lower-liquidity months that are still tradeable at their size, and the entry-order-relative-to-CTA-entry timing matters (entering ahead of CTA flow can be neutral-to-helpful, not harmful).
- **Euan gave the most substantive answer on crowding itself**, distinguishing stabilizing crowding from destabilizing crowding: crowding only ever happens on trades that are *winning* (you never get crowded out of a bad trade), and for a reversion-style trade specifically, crowding is actually stabilizing — it helps push prices back toward fair value faster. It only becomes a problem when the crowded trade is itself directional/trend-amplifying (e.g., a crowded trend-following bubble). His read on the congestion trade specifically: the roughly fixed exit timing likely makes it more stabilizing than destabilizing, though the "front-running the known move" effect persists regardless of crowding.
- A side debate on COT (Commitments of Traders) positioning as a crowding signal went nowhere conclusively — Euan said he's "never tested that" but recalled it hasn't worked reliably "since the days of the market wizards," while Dan noted an interview with veteran trader David Druz used COT data in the *opposite* direction (trading against, not with, commercial hedgers), leaving the group without a settled read on which interpretation (if either) holds up.

**Sentiment:** High-quality, exploratory research energy — a concrete idea (congestion trade) with robotkris buy-in to actually pursue it, plus a genuinely useful conceptual framework (Euan's stabilizing-vs-destabilizing crowding distinction) that generalizes beyond this specific trade.

**Pull quotes:**
- Euan: *"Crowding isn't always a bad thing. First, it only happens when something is winning. You never get crowded out of bad trades... When you are betting on reversion crowding will help to push prices back to where they should be. The crowd is a stabilizing mechanism. Where it becomes a problem is when it is a destabilizing thing like when trend following gets crowded and the prices get amplified into a bubble."*
- robotkris: *"We should put these on our list of stuff to look at. These sorts of trades are right up our alley."*
- Dan: *"The congestion trade would be a lot easier to explore from an edge perspective [than curve carry]."*

## 2. EOM equity/bond rebalancing trade: which source of truth is current

akhan asked whether the rules on the older Edge Database GitHub page were still current, or whether the strategy had been updated since a January 2024 date shown there. **robotkris clarified directly**: that page is up to date, but he's actively working to make the `rw-portfolio` GitHub repo the single central and current source of truth for implementation — pointing akhan to the more actionable seasonality strategy doc there instead, and inviting feedback on anything unclear or missing from it.

**Sentiment:** Minor housekeeping, resolved immediately — useful to know if you're referencing older Edge Database links versus the newer `rw-portfolio` repo going forward.

**Pull quote:**
- robotkris: *"The Edge Database you linked to is up to date, but I'm trying to make the rw-portfolio repo the central and current source of truth for all this stuff. It's a bit more useful to get you actually trading this thing."*

## 3. VIX positioning around a fragile ceasefire

Euan shared pre-market VIX/VVIX observations: moves of this size in the VIX have happened before, sometimes with VVIX even lower, so statistically this kind of move isn't unusual on its own. What made this instance different was that it coincided with a 2-week ceasefire that Israel reportedly wasn't fully part of, layered on top of Trump having proposed (and apparently had rejected) a 10-point plan — leading Euan to expect this fragile situation "probably" isn't over and to hedge accordingly by covering short-VIX positions, with the caveat that outcomes would likely hinge on VVIX behavior specifically.

**Sentiment:** Careful, geopolitically-grounded risk management from Euan — treated by ASlan as unusually high-quality macro commentary ("worthy of the macro tourism channel").

**Pull quote:**
- Euan: *"There have been moves like this in the VIX before, and sometimes when VVIX was much lower. So statistically this is just something that happens. But the difference here is that this is associated with a 2 week ceasefire... So I'm covering all my short VIX positions and will probably get long something, depending on VVIX."*

## 4. Natural gas storage-announcement and CPI-adjacent short-vol trades

A recurring, concrete trade running through the whole month: shorting ahead of the weekly (Thursday ~10am) NG storage announcement, and separately shorting VIX ahead of CPI prints.

- Sam ran both live: a small 8-pip loss on NG one week, +20 pips shorting VIX ahead of CPI another week, later +50 pips on NG storage (after a scratch the prior week). By month-end he described his execution rule precisely: enter just before the report, exit 15-30 minutes after.
- ASlan explained the underlying logic for the NG trade — conceptually similar to shorting VIX ahead of CPI — while being upfront that he doesn't know the actual statistical track record of the edge.
- Rachit shared an SSRN paper as potentially relevant, but flagged real implementation skepticism: the data collection looks out of reach for him personally, and he's "super suspicious" of anything FX-related once realistic commissions are added back in.
- Dan gave the most useful practical filter: futures should work better than spot/FX for this kind of trade, since liquid futures are arbitraged tightly to time-to-expiry with low commissions and tight spreads — though he flagged an open question about whether closing-time mismatches between futures and spot data could matter for the underlying research.
- **TheCTAFan contributed real backtest numbers** on a full-day variant (short Wednesday EOD, close Thursday EOD): pre-cost NG total return from 2000-2026, monthly with 4-5 trades usually, working better across autumn/winter months specifically — he flagged the analysis excludes holiday-shifted announcement days (which may explain some of a December dip) and that the daily variant isn't worth trading after-cost in late spring/summer, since the announcement reaction is more pronounced when NatGas usage (and shortage risk) is elevated.
- FullMetal37! and Marco both confirmed they execute the NG trade via CFDs rather than futures or an ETF.

**Sentiment:** A genuinely live, actively-traded seasonal edge with real (if modest) numbers being reported in real time — the most "in the market together" thread of the month.

**Pull quotes:**
- TheCTAFan: *"I played with numbers for full-day variant of this (short Wed EOD, close Thu EOD), and it seems to be working better over autumn / winter months... IMO the daily variant after-cost is not worth trading in late spring / summer. The way I understand it, is that the announcement reaction / hedging need is more pronounced when NatGas usage is high, and there's a bigger chance of shortage."*
- Sam: *"i enter just before the report and exit 15 mins to 30 mins after."*

## 5. SEC ends the Pattern Day Trader (PDT) $25k minimum rule

hac shared the news that the SEC approved ending the PDT rule's $25k minimum requirement. The reaction split into two threads:

- Dan welcomed it, arguing the old rule perversely pushed beginners to over-capitalize just to avoid restriction ("start with $5k rather than $25k") — noting Australia never had an equivalent rule and it never made sense to him to tell a beginner "we're going to restrict you unless you put even more money at risk."
- **Euan gave the more skeptical, structurally-grounded take**: the original rule existed specifically to protect traders from themselves, and that underlying problem hasn't gone away just because the rule has fallen out of political favor. He drew a direct parallel to the CBOE's push toward 0DTE options to boost volume "without paying too much attention to who the customers are," and offered a useful heuristic for judging any deregulation like this: look at who was actually lobbying for the change.

**Sentiment:** A genuine two-sided debate — pro-access-for-small-traders (Dan) versus skeptical-of-industry-motives (Euan) — without a clear resolution, but Euan's "look at who was pushing for the change" framing is a reusable lens for evaluating future regulatory changes in this space.

**Pull quotes:**
- Euan: *"the original rule was put in place to protect traders from themselves. can't see why that isn't still an issue but that has fallen out of favor now. it is the same as the cboe pushing 0dte to increase their volumes without paying too much attention to who the customers are. the best way to see if this will be a good thing is to see who was pushing for the change..."*
- Dan: *"Better for them to start with $5k rather than $25k and continually top it up to avoid the rule."*

## 6. End-of-month window dressing: bond flows mechanism clarified via newsletter

Michael TW 88 asked about the specific mechanism behind end-of-month window dressing that a fixed-income asset manager (referred to as Teckk) had corrected during a webinar. chi pointed to the exact reference material: an RW Pro newsletter where robotkris shared Teckk's story on bond flows, plus a related Discord thread with Teckk's original message. Toshi confirmed the same question had brought them into the channel too.

**Sentiment:** Simple reference-lookup thread — worth noting the newsletter/Discord-thread combo as the canonical source if this mechanism question comes up again.

**Pull quote:**
- chi: *"This is the newsletter where Kris shared the story on bond flows by Teckk: [rw-pro-newsletter-welcome-and-new-insights]"*

## 7. Euan's live Sunday-night-reversal experiment: idea, execution, and disproof within the month

The month's clearest example of hypothesis-to-disproof discipline, playing out as a real, small, live position:

- Euan opened with a bare-bones thesis — Sunday night futures opens tend to be "wrong" — sized as a tiny position with explicitly *no* real analysis behind it yet, and an accompanying warning not to over-anchor on the recent "crazy rally" as if it were predictive of anything.
- **alvin pushed back constructively**, questioning whether trading long-term on pure feel without proper analysis was sound, and asking what Euan's actual exit criteria for the experiment would be. **Euan was candid about the bucket this trade lived in**: "firmly in the 5% fuck around and find out bucket" — explicitly not a serious, analyzed edge, continued mostly because it happened to be making money.
- Sam ran the same trade in parallel, describing it identically as a punt on a small sample persisting one more time.
- llIHeroic added a related observation from the same weekend-pricing phenomenon in crypto: during tariff-news weekends, BTC traded with full access to news flow all weekend, yet still got violently repriced the instant the ES futures print opened — a related but distinct manifestation of weekend/Sunday pricing inefficiency.
- **The resolution**: four days later, Euan ran the actual analysis and reported back honestly that the trade **doesn't work** — it had a positive Sharpe this year (0.16) but that's not statistically meaningful, and doesn't hold up as a general effect. His own conclusion: "just luck." Sam speculated it might have been a temporary war-related inefficiency; Euan didn't accept that framing.

**Sentiment:** A model of honest research discipline — Euan explicitly labeled the trade as unanalyzed speculation from the start, then killed it himself once real analysis contradicted the live P&L, rather than letting a small winning streak become a justification to keep it running.

**Pull quotes:**
- Euan: *"just winging it. it is firmly in the 5% fuck around and find out bucket"* ... *"Ok. Did some actual analysis on the Sunday reversal. Doesn't work. Has worked this year, but only a 0.16 Sharpe. Doesn't really work in general"*
- Euan: *"Just trade futures. And take them off tomorrow morning. My only thesis is that Sunday night opens are wrong... Also don't anchor yourself to what has happened. 'Crazy rally' isn't predictive of anything."*

## 8. Country-themed ETF mean reversion after large moves

deal_me_in asked why country equity ETFs (e.g., EWG for Germany, EWJ for Japan) might mean-revert the day after a large move in either direction, and whether the mechanism is well understood or just an empirically-observed-but-unexplained effect like trend.

- He worked through two AI-suggested hypotheses himself: **time-zone arbitrage/stale pricing** (the ETF trades in New York while its home market is closed, so a big S&P move gets used as a global-risk proxy overnight, and the next day's reversion is the local market "correcting" that overnight overshoot once it actually opens and digests the news) and the **"rubber band" liquidity-provision effect** (large 3-5% moves force market makers to absorb order imbalances by widening spreads/pushing prices to extremes, which then "snaps back" once next-morning selling/buying pressure subsides) — noting the second hypothesis seems harder to test cleanly since it's about the volume of the *underlying*, not the ETF itself.
- Marco pointed to existing third-party research (a Substack post specifically on trading country-themed ETFs) as a starting reference.
- **deal_me_in did real work following up**: confirmed the effect exists empirically using z-scores (not just IBS), but noted the backtest blog and underlying paper he found don't actually explain *why* it happens — he's specifically interested because he's hunting for ex-US equity exposure ideas, and separately recalled another paper explaining mean reversion in illiquid-underlying ETFs that might be a related mechanism.

**Sentiment:** Genuine, still-open research thread — effect confirmed empirically by a member's own work, but the causal mechanism remains unresolved and worth someone digging into further (a natural fit for the group's stat-arb-adjacent interests).

**Pull quotes:**
- deal_me_in: *"I can confirm the effect is there. And you don't have to do it with IBS. I confirmed it with z scores... But that backtest blog and the paper it's based on provide no explanation"*
- deal_me_in: *"The Effect: If there is a massive move in the S&P 500 late in the day, traders will buy or sell the country ETF as a proxy for global risk. The Reversion: When the local market actually opens the next day... the initial emotional move in the US-listed ETF is often found to be an overshoot."*

## 9. Closed-end fund (CEF) discount trading

hazler asked whether anyone had explored closed-end fund trading. **deal_me_in engaged directly**, having independently considered building a discount-to-NAV screener but not yet done so. hazler's specific interest: mean-reversion of CEF discounts and reactions to new activist involvement, and he found **cefconnect** as a free, reasonable-looking screener to start with. deal_me_in connected it to material already in the RW ecosystem — the "Armageddon" videos specifically discuss buying CEF discounts during market panic — while hazler, still early in exploring the idea, reported one interesting counter-example candidate where NAV appeared to be rising *faster* than price (the opposite of the expected discount-widening pattern).

**Sentiment:** Early-stage, genuinely exploratory — no conclusions yet, but a concrete tool (cefconnect) and a link to existing RW material (Armageddon videos) give this a running start if either member follows up.

**Pull quotes:**
- hazler: *"cefconnect looks reasonable and free as a screener. I was looking at things like mean-reversion of discounts, new activist involvement, etc"*
- deal_me_in: *"The Armageddon videos talk about this… buying discounts during market panic."*

---

## Overall read

April's #tradfi-trading was defined by concrete, testable trade ideas rather than one big theme — the commodity congestion/roll trade (with robotkris's explicit buy-in to pursue it further) and the NG-storage/CPI short-vol trades (with real live P&L being reported, including TheCTAFan's seasonally-aware backtest) are the two most actionable threads if you're looking to build something new this quarter. **Euan's contributions were the strongest single-person thread of the month**: his crowding framework (stabilizing vs. destabilizing) is a reusable mental model well beyond the congestion trade specifically, his VIX/ceasefire risk read showed careful geopolitical reasoning, and his Sunday-night-reversal experiment is worth pointing to as a template for how to run a small discretionary punt honestly — declare it unanalyzed from the start, size it as truly disposable, then kill it without ego once real analysis contradicts a lucky streak. The country-ETF mean-reversion thread (deal_me_in) and the closed-end-fund discount thread (hazler) are both still open and worth revisiting if either member reports back with further findings — neither reached a tradeable conclusion this month, but both have concrete next steps (a discount-to-NAV CEF screener; explaining *why* the country-ETF reversion effect holds, not just that it does).
