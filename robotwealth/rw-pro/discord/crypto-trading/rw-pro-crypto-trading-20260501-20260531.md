# RW Pro Discord — #crypto-trading digest, May 2026

- **Period:** May 1–31, 2026
- **Channel:** https://discord.com/channels/1368787013763072040/1368845831113015346
- **Raw transcript:** [rw-pro-crypto-trading-raw-20260501-20260531.md](./rw-pro-crypto-trading-raw-20260501-20260531.md)
- **Volume:** 44 messages, light month with a long quiet stretch (5/8–5/20, nearly two weeks with nothing) bookended by two active clusters: May 1–7 and May 21–30.

---

## 1. CME Bitcoin Vol futures launch

Stefan flagged that CME is launching BTC Vol futures on June 1, drawing an immediate "like a VIX?" from Euan. Stefan followed up with CME's own methodology blurb (a standard variance-swap pricing model to isolate pure volatility exposure), and nxtrador asked the group to elaborate on why this is interesting — is it just a vehicle to sell vol?

robotkris gave the fullest answer, reasoning from first principles:
- The BTC variance risk premium is likely large and persistent, similar to equity vol.
- A vol future gives "a lot of scope to express variations on that view," and term structure effects become tradable both directly and as signals.
- There's likely relative-value opportunity against existing crypto vol products (options, realized-vol proxies), plus other angles not yet mapped out.

Euan added the carry angle: he expects BTC vol carry to behave similarly to VIX carry, making a short-front/long-back futures curve trade a promising starting point.

**Sentiment:** Genuinely excited, exploratory — "Party time" (robotkris) captures the mood. Nobody has a live strategy yet, but the group sees a credible new venue for a vol risk premium trade once the contract launches.

**Pull quotes:**
- robotkris: *"We'll likely find that BTC variance premium is large and persistent. A BTC vol future gives you a lot of scope to express variations on that view. Term structure effects become interesting too. Directly tradable and as signals. Likely some RV opportunities against existing crypto vol products. And more that I haven't thought of…"*
- Euan: *"The carry should behave very similarly to the vix carry so a short front/ long back seems promising."*

## 2. YOLO refresh timing and the CME-vs-DEX weekend risk tradeoff

Matt G asked when the Crypto YOLO strategy/API is next due for an asset refresh, framing it around a bigger question: he's considering moving execution to CME micro futures because of operational and credit-risk concerns with DEXs. He noted CME doesn't offer BNB, DOGE, or TRX (so only 7 of YOLO's current 10 assets would map over) but does have XLM and SUI micro futures that aren't in the YOLO universe today, and asked what the criteria would be for including assets like those on the next refresh.

Euan, who has actually traded YOLO on CME before, gave the practical counterpoint:
- He tried it and stopped — CME closes over the weekend, and he got hammered a few times by Saturday moves that the DEX-traded (24/7) version would have caught in real time.
- His view is conditional on performance: if YOLO had been running hot he'd have gone deeper on quantifying the weekend-gap risk, but with the strategy having a rough year he didn't prioritize it.
- On balance, he now leans toward thinking 24/7 trading is the worse experience for him personally, given how exposed you are between fills.

robotkris confirmed a refresh was due and scheduled for the following week (this became the thread picked up in section 3 below).

**Sentiment:** Cautionary, first-hand — Euan's weekend-gap experience is a concrete data point against the CME-migration idea, not just theoretical concern.

**Pull quotes:**
- Euan: *"No. I DID it on CME but stopped. The big difference is that the CME closes over the weekend and I got hammered a few times due to saturday moves."*
- Euan: *"If YOLO had been killing it I would have done some real analysis on weekend risk, but I was super busy and YOLO wasn't going through a great run."*

## 3. YOLO universe refresh (AVAX/LINK → HYPE/ZEC) and the push toward a flexible, broader factor endpoint

The month's biggest thread. robotkris opened it by proposing the concrete refresh: AVAX and LINK out, HYPE and ZEC in, based on CoinGecko market cap, while flagging he'd been less locked-in on crypto lately given the team's focus on equity stat-arb. He asked for objections and noted the near-miss candidates (NEAR — lower mcap but higher volume than ZEC; BCH and XMR — more track record but slightly lower mcap), reaffirming that YOLO's simulation defaults to a pure market-cap-ranked universe absent a good reason otherwise.

This triggered a substantive design debate:

- **Matt G** asked whether the API could instead expose a broader asset set and let users pick their own basket (like the stat-arb product does), but flagged uncertainty about whether the underlying factors are cross-sectionally normalized against the fixed top-10 universe — which would make his suggestion break without rework.
- **robotkris** confirmed this is exactly the direction he wants to move, and explained the tradeoff in detail: the current YOLO factors endpoint does the cross-sectional ranking *for* the user against a fixed 10-asset universe, which is simple but "totally inflexible." His proposed fix is to keep the existing weights endpoint as-is (so current YOLO traders are unaffected) while building a new or expanded factors endpoint that serves raw per-ticker factor values, pushing the universe-construction and ranking decision downstream to the user. He explicitly linked this to community sentiment that looking outside the top 10 is a good idea.
- **Michael** asked for a mechanism clarification — is this closer to letting users add an asset-size variable, or specify rank ranges (e.g., assets 1–5, 10–15)?
- **llIHeroic** was fine with the immediate HYPE/ZEC swap but asked robotkris for backtested Sharpe deltas across 5/10/20-top-mcap universes, reasoning that if there's no meaningful edge from a wider basket, a simple coin swap plus continued work elsewhere is good enough for now.
- **robotkris** ultimately sequenced the work: ship the immediate coin swap now, build the broader factor endpoint later once other priorities clear ("when we clear the decks a bit"). He later reiterated the design philosophy directly: this new approach is "one level up" from what the Unravel factor service does (Unravel serves pre-built portfolio weights for a fixed universe; robotkris wants to serve raw factors and let users build cross-sectional signals on their own universe) — more flexible, but with added complexity for the user to own.
- **mr_bluesky** welcomed the direction and asked, if it's not too much extra work, for the eventual broader endpoint to align with Unravel's own rolling top-10/-20/-40 universe convention, since Unravel's universes are considerably more volatile than YOLO's fixed top-10.
- **SatoriNakaMoto** added a data point relevant to the redesign: most momentum factors besides RRP and range are showing signs of decay or regime-dependence, floating this as a potential future webinar topic on alpha decay and retraining — tagging robotkris and Euan directly.
- Separately, **Dave** floated a related but distinct idea — now that Hyperliquid lists tradfi instruments alongside crypto perps, would a momentum/trend strategy on a *mixed* crypto+tradfi universe be worth researching? He followed up later asking where to even start on universe selection for crypto stat-arb generally.

robotkris confirmed the target execution window: refresh to go live after Friday's US market close, pending final staging checks. On the day itself (May 30), faz reported being unable to find HYPE listed on Binance UK; robotkris's answer was structural — there should be a perp available as long as there's a spot market, implying the gap is jurisdictional/listing-related rather than a YOLO-side issue.

The refresh day also produced a shared, unrelated headache: both brad_smith and Rachit independently hit the same ccxt/Hyperliquid bug (an outdated ccxt version causing the `load_markets` call to crash on a null spot market), coincidentally on the same day each had set aside time expecting *other* things to go wrong with the refresh.

**Sentiment:** Substantive and constructive — this is the month's real design conversation, not just a routine universe swap. robotkris's answers set clear near-term (ship the swap) vs. longer-term (raw-factor endpoint) sequencing, and multiple members (Matt G, mr_bluesky, llIHeroic) engaged with genuine follow-up questions rather than just approving.

**Pull quotes:**
- robotkris: *"I think it's a really good idea and something I want to move towards... The yolo factors endpoint does a little bit of both — serves some raw time series factors, and serves some cross sectionally normalised factors (based on the 10-asset universe assumption)... I think the solution would be to keep the weights endpoint as is... but expand the factors endpoint, or make a new one."*
- robotkris: *"I think the way we'd do it would be to cover an even broader universe, and just serve the raw factor values and leave it up to the user to build their own universe and their cross sectional signals. That's one level up from what Unravel do... I like that approach because it gives you ultimate flexibility. But with that flexibility comes some complexity."*
- llIHeroic: *"If there's no meaningful improvement expanding basket size, simple coin swap and continuing to work on other stuff seems like it would be fine imho."*

## 4. Smaller items: tools, housekeeping, and data sources

A handful of standalone, lower-weight threads worth noting for reference:

- **Funding rate dashboard.** 4rtfj8 shared a new self-built tool at arbs.fyi covering 18 exchanges, with a "Rates By Exchange" view and a "Compare Exchanges" grid for cross-venue funding-rate comparison, plus current vs. aggregated rate toggles.
- **MAVIA delisting.** hecta gave an early heads-up that Hyperliquid validators would vote to delist MAVIA on May 5th; Kamil confirmed he'd already closed his position, calling it "a good farm for a few weeks."
- **Hyperliquid spot historical data.** {Overly Powerly} asked where to source historical data for Hyperliquid spot markets; emsin44 pointed to hydromancer.xyz, specifically its "reservoir" feature.

**Sentiment:** Routine, informational — no debate, just useful pointers for anyone tracking these venues.

---

## Overall read

May was a quiet month for #crypto-trading by volume (44 messages vs. June's 83), with a nearly two-week dead stretch (5/8–5/20) sitting between two more active clusters. Despite the low volume, the substantive content was concentrated and genuinely forward-looking rather than reactive:

1. **CME's new BTC Vol futures (launching June 1) is a real, credible opportunity the group is tracking** — robotkris's variance-premium/term-structure thesis and Euan's VIX-carry-analogy trade idea are the most substantive unstarted research leads from the month.
2. **CME migration for YOLO execution was seriously considered and largely discouraged** by Euan's first-hand experience with weekend gap risk on CME's Saturday-closed sessions — a concrete argument for staying on 24/7 DEX venues despite the credit-risk tradeoffs that motivated the question.
3. **The YOLO universe refresh (AVAX/LINK → HYPE/ZEC) shipped on schedule** after Friday's US close, but the more consequential outcome is the design commitment from robotkris to eventually decouple the *factor* endpoint from the fixed 10-asset universe — moving toward Unravel-style flexibility (broader universe, user-owned cross-sectional ranking) while keeping the existing simple YOLO weights product intact for current users. Worth tracking next month for progress.
4. **Momentum/trend factor decay was flagged** by SatoriNakaMoto as a possible future webinar topic — a signal that some of YOLO's core factors may need retraining or re-evaluation, separate from the universe-composition question.
5. Both the CME-migration thread and the universe-refresh thread show a recurring pattern: **members proposing DEX-to-CEX/CME migrations or fixed-to-flexible universe changes, met with grounded pushback from robotkris and Euan based on lived trading experience** rather than pure theory — a useful signal for weighting how much credence to give any single member's proposal versus the two most experienced voices in the channel.
