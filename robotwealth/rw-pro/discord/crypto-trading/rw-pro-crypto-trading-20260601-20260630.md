# RW Pro Discord — #crypto-trading digest, June 2026

- **Period:** June 1–30, 2026
- **Channel:** https://discord.com/channels/1368787013763072040/1368845831113015346
- **Raw transcript:** [rw-pro-crypto-trading-raw-20260601-20260630.md](./rw-pro-crypto-trading-raw-20260601-20260630.md)
- **Volume:** 83 messages, moderate-activity month with several multi-day gaps (nothing 6/9–6/13, 6/9–6/14 quiet stretch, and a light week 6/9–6/13)

---

## 1. Rebalancing cadence vs. execution cost

Opened the month. SatoriNakaMoto proposed shifting the portfolio rebalance from once every 24h to hourly, arguing it would smooth out overshoots and improve variance/capture speed for a momentum-heavy book. Pushback centered on cost: more frequent turnover eats into edge via fees and requires tighter execution (maker-side fills, tuned no-trade buffers) to pay off. robotkris flagged a more fundamental risk — a framework built on daily rebalancing has unmodelled sub-daily mean-reversion effects that would need separate handling at higher frequency.

**Sentiment:** Interesting idea, not adopted — consensus was the execution/infrastructure burden ("cumbersome," in Satori's own words) outweighs the smoothing benefit without a dedicated maker-side execution layer.

**Pull quotes:**
- robotkris: *"those are two big 'ifs' and forcing a slower rebalance cadence makes those issues go away... there are mean-reversion effects that show up on a sub-daily timescale that are essentially unmodelled in our framework."*
- SatoriNakaMoto: *"if i churn my portfolio small bit i can be on the maker side and lower my exec cost by a factor of 2... but yeah its cumbersome."*

## 2. ZEC minting vulnerability and universe selection

iaminarush flagged ZEC (Zcash) might drop from the trading universe on the next refresh given how "unstable" it had become. That set up a thread on universe-selection methodology (rolling market-cap windows, whether recency/longevity in top-mcap should be weighted) before {Overly Powerly} surfaced the actual catalyst: a long-known infinite-minting vulnerability in ZEC's shielded pool (linked to a tweet from Zcash's Zooko), meaning supply can't be reliably audited. mr_bluesky joked the YOLO strategy survived being long the name through the furore, and later floated that if the vuln is patched and the panic proves overblown, it could become a buying opportunity. robotkris said the desk went net short in the meantime.

**Sentiment:** Cautious/skeptical — treated as a genuine tail-risk data-integrity issue, not just noise, but the group is watching for a FUD overreaction to fade.

**Pull quotes:**
- {Overly Powerly}: *"there could be an infinite minting bug in ZEC and as its private there is no way to truly account for it."*
- mr_bluesky: *"the furore may be entirely FUD - I don't think there is actually any proof that anyone exploited the hole before they patched it? May end up being a buying opportunity.."*

## 3. Microstructure / signed volume imbalance edge

mr_bluesky backtested a signed-volume-imbalance signal (which side crosses the spread) on short-term tick bars (300–600 tick) using the Hyperliquid dataset. Gross Sharpe looked "AMAZING" but round-trip costs erased it — a classic microstructure-alpha-vs-transaction-cost story. robotkris's take: not viable as a standalone strategy without a market-maker-grade execution stack, but potentially useful stacked with other signals or to improve execution quality on existing edges.

**Sentiment:** Realistic/tempered — good research finding, not a deployable strategy as-is.

**Pull quotes:**
- mr_bluesky: *"Turns out this looks AMAZING. Before you add in the round-trip costs, alas..."*
- robotkris: *"You won't be able to harness a microstructure edge in isolation... you might stack with other edges."*

## 4. Factor weighting: trend vs. carry vs. momentum

Malhar (a newer, active member — see thread 5) asked how people weight trend/carry/momentum given trend had a rough year on the dashboard while carry outperformed. mr_bluesky's answer: equal-weight everything and ride out the regime — "Trend will dominate again at some point. The trick is knowing when." mm added the pragmatic heuristic of just making sure you're never underweight trend/momentum so you don't miss the eventual regime shift. A separate side-thread clarified the trend-vs-momentum distinction for newer members: trend = asset vs. its own history, momentum = cross-sectional (asset vs. peers).

**Sentiment:** Pragmatic consensus — nobody claims to time the regime shift; equal-weight-and-wait is the default answer from the more tenured members.

**Pull quotes:**
- mr_bluesky: *"I just equal weight everything. Trend has had a tough time as we were in a mean reversion phase by and large for much of the time."*
- robotkris: *"Trend is about things going up or down relative to their own history. Momentum is about things that have gone up/down more than their peers continuing to do so."*

## 5. Onboarding: India-based member, fiat on-ramps and capital controls

Malhar (based in India for the summer) asked about fiat on-ramps into MetaMask/Hyperliquid, citing steep MetaMask on-ramp pricing. The channel suggested checking CEX support by jurisdiction and peer.xyz for P2P, but the more actionable flag came from SatoriNakaMoto: Indian authorities are actively watching capital flight given recent INR depreciation, and an offshore account outside India is "defo better" than routing INR directly — Binance was confirmed to still work from India. This thread continued into general position-sizing/PnL-tracking questions on Coinbase (fee comparisons, why Coinbase's UI shows discrete "trades" rather than continuously-adjusted weights) — Coinbase's taker fees were called out as competitive vs. Binance/Kucoin for the India use case despite a reputation for being expensive.

**Sentiment:** Practical/helpful — standard new-member onboarding, notable mainly for the regulatory-risk callout on India capital controls.

**Pull quotes:**
- SatoriNakaMoto: *"indian authorities are very wary of INR leaving the system in wake of recent depreciation."*
- Malhar: *"the only decent ones operating here are binance, coinbase and kucoin, and at least for the time being, coinbase is offering lower taker fees than the others."*

## 6. Unravel factor service

New members (Michael, others) asked what "Unravel" is — clarified as a third-party company providing crypto factors/portfolios with its own channel in the server. mr_bluesky (an active Unravel subscriber, judging by his HYPE tag) explained pricing has two tiers: tier 2 and a materially pricier tier 3 that unlocks more factors plus a "pre-canned optimal strategy" comparable to how YOLO is packaged. He also connected this to a broader idea: since he already has crypto exposure via Unravel and YOLO, he's interested in researching a strategy targeting the tradfi instruments (e.g., "XYZ" listings) now available alongside crypto perps on Hyperliquid — cross-asset momentum/trend using the same infrastructure. Dave separately raised the same crypto+tradfi mixed-universe idea earlier in the month.

**Sentiment:** Informational — no strong opinions on Unravel's value, mostly onboarding Q&A; the crypto/tradfi cross-asset idea seemed to get more genuine interest.

**Pull quotes:**
- mr_bluesky: *"there are two tiers that you can take - tier 3 is materially more expensive than tier 2, but there are more factors available to you... a pre-canned optimal strategy rather like the way YOLO is served."*
- mr_bluesky: *"I already trade Unravel and YOLO and so have exposure to the top-n crypto universe"* [as rationale for wanting tradfi diversification].

## 7. Kraken BTC perp data quality concern

mm flagged apparent price spikes/wicks on what looked like Kraken BTC perp data ("somebody go steal this guys money on kraken wtf"), prompting a data-integrity check. Alex couldn't replicate the spikes on their own Kraken feed and noted their venue access (EU vs. US) was more liquid with no anomalies — suggesting a US-specific liquidity/data quality issue on Kraken's US perp venue (only a few million in volume) rather than a broad exchange-wide problem.

**Sentiment:** Minor but worth flagging for anyone trading Kraken US perps specifically — thin liquidity, possible print/data artifacts.

**Pull quotes:**
- mm: *"there's like a few mil of volume... idk if the trades actually print or not."*
- Alex: *"mine looks way more liquid with no spikes. Maybe because its EU not US."*

## 8. Crypto perp strategy inventory & new venues

Nostalgic detour into the old FTX EOD-rebalance "free money" trade (confirmed dead — no exchange has been "as dumb as that since"), which prompted robotkris to link the group's canonical strategy writeups in the `rw-portfolio` GitHub repo: perp basis, carry (various forms), trend/momentum, and short-new-listings. mike noted perps are now listed on Kalshi, raising a new venue to watch. hecta gave a live update on paper/live testing long-short carry on Binance since May: modest, "mostly sideways" so far but with a recent +9% bump from being on the right side of the MUSDT stablecoin de-peg/meltdown (despite getting auto-deleveraged/ADL'd in the process). Dave asked whether crypto content might return to the regular webinar rotation, noting the stat-arb content has been strong lately.

**Sentiment:** Constructive — real position sizing/live-testing data point (hecta's carry result) is the most concrete signal of the month.

**Pull quotes:**
- robotkris: *"They're all written up in rw-portfolio: https://github.com/RWLab/rw-portfolio"* — Perp basis, Carry, Trend/Momentum, Short new listings.
- hecta: *"got a nice 9% bump because luckily I was on the right side of the MUSDT meltdown - got ADLd unfortunately, but still."*

## 9. Carry risk management and PnL attribution

Closing the month, Malhar (moving from research to live trading) asked whether carry positions should be sentiment-agnostic or hedged against adverse intraday moves. llIHeroic's guidance: size down until the inventoried volatility "feels like harmless noise," then size back up as conviction builds — i.e., don't try to hedge the carry signal itself, manage exposure through position sizing. Malhar then asked about PnL attribution tooling/libraries to evaluate which signals/factors are actually working; mm pointed to Chapter 11 of Paleologo's *Advanced Portfolio Management* (dense but LLM-summarizable) as the reference.

**Sentiment:** Constructive, forward-looking — reads as a member moving from paper-trading questions toward live risk management discipline.

**Pull quotes:**
- llIHeroic: *"IMO just side down until the amount of volatility you're inventorying feels like harmless noise. You can always size up later if conviction grows."*
- mm: *"chapter 11 of advanced portfolio management - paleologo goes into this... bit dense math wise if you aren't familiar but can throw it into your favorite clanker llm and it'll help."*

---

## Overall read

June was a moderate-volume month for #crypto-trading, split fairly evenly between infrastructure/portfolio-construction debate (rebalance cadence, factor weighting, PnL attribution) and reactive risk management (the ZEC minting vulnerability, Kraken US perp data quality). The most actionable threads for an active investor:

1. **ZEC carries a real, still-unresolved tail risk** (infinite-minting vulnerability in the shielded pool) — the desk went net short mid-month; watch for a patch/resolution that the group thinks could flip this into a buying opportunity.
2. **Trend has underperformed carry YTD** in the group's crypto factor book; the house view is equal-weight and wait rather than tactically tilt away from trend.
3. **Microstructure edges (signed volume imbalance) look strong gross but don't survive round-trip costs** without market-maker-grade execution — a caution against over-trusting backtested Sharpe on high-frequency crypto signals.
4. **A live carry strategy (Binance long-short) posted +9% MTD-ish**, boosted by being correctly positioned through the MUSDT stablecoin meltdown — one of the few concrete, dated performance data points shared this month.
5. Cross-asset crypto+tradfi momentum (via Hyperliquid's expanding tradfi listings) is emerging as a research interest for at least one active member (mr_bluesky), worth tracking if it develops further next month.
