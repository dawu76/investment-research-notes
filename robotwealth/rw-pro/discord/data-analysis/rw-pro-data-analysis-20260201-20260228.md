# RW Pro Discord — #data-analysis digest, February 2026

- **Period:** February 1–28, 2026
- **Channel:** https://discord.com/channels/1368787013763072040/1368844739465707572
- **Raw transcript:** [rw-pro-data-analysis-raw-20260201-20260228.md](./rw-pro-data-analysis-raw-20260201-20260228.md)
- **Volume:** 49 main-channel messages clustered into five windows (Feb 2–3, Feb 6–12, Feb 24, Feb 27) with multi-day silent gaps between them. This month was almost entirely about data sourcing — where to find cross-asset returns, short-sale history, security identifiers, and index constituents — rather than strategy results, with one exception (a seasonal-trade critique thread).

---

## 1. Finding a clean, monthly, cross-asset dataset for risk premia research

steph asked for a research-ready dataset spanning equities, bonds, commodities, and FX at monthly frequency, for testing risk-parity, momentum, value, and carry strategies over long horizons — explicitly trying to avoid reinventing the wheel.

**robotkris's first suggestion** was Ashwath Damodaran's public dataset (NYU Stern), but steph pushed back that it's annual and too limited in breadth for what she needed.

**robotkris's more substantive answer**, once he understood the actual requirement, pointed to a specific Lab resource:
- A dataset built from ETFs extended back to 1995 using mutual fund data, covering gold, non-US developed-market stocks, EM stocks, EM bonds, and Treasuries (plus some additional ETF series that were captured but not extended back — managed futures, leveraged ETFs).
- No long-term commodities dataset exists in the Lab, but there's ample raw futures data to build one from.
- Similarly, no ready-made FX dollar index, but the Lab's FX data (via rwRtools utilities, under-documented) supports building one — including a utility function specifically for constructing a total-return index, which he flagged as directly useful for steph's use case.
- His self-deprecating aside — *"Not sure why i didn't link you to that stuff in the first place. I guess I was low on caffeine at the point in the day"* — is worth noting only in that it signals the Lab's asset-class dataset isn't the first thing that comes to mind even for the person who built it, i.e., it may be underused/underdiscovered by the wider community too.

**Sentiment:** A genuinely useful pointer to an existing internal resource, delivered on the second attempt once the actual requirement (monthly, cross-asset, cross-strategy) was clarified — good example of Lab data not being fully surfaced until pushed on.

**Pull quotes:**
- steph: *"I'm looking for monthly total return data with decent breadth across equities, bonds, commodities, and FX... this feels like the kind of thing that would be really valuable to share here."*
- robotkris: *"This dataset from The Lab has a bunch of asset class data from ETFs that we extended back to 1995 using mutual fund data... We don't have a long-term commodities data set, but we do have lots of futures data. You could build your own from that."*

## 2. Historical IBKR short-sale data (fees, availability)

bdkoepke was looking for historical IBKR short-sale fee/availability data, having only found a source (iborrowdesk.com) for current values via FTP. MattM pointed him to Lab data covering short-sale data from mid-2020 onwards, sourced directly from Interactive Brokers. bdkoepke confirmed this was a better answer than what he'd found himself.

**Sentiment:** Quick, clean resolution — a specific data gap filled by an existing Lab resource.

**Pull quote:**
- MattM: *"Kris has data from mid 2020 onwards in the lab"* (linking `RWLab/macro-pod#us-stock-short-sale-data-from-interactive-brokers`)

## 3. Mapping tickers to stable security identifiers across vendors (FIGI/symbology)

bdkoepke raised a recurring data-engineering headache: CSI doesn't provide standard security identifiers, so he's been hand-building a Bloomberg FIGI mapping that works for active large/mid-cap names but is unreliable for inactive and foreign securities. His goal is a single clean-symbol anchor (`ID_BB_GLOBAL`) to tie together IBKR conid, CSI number, and Zacks identifiers across vendors, since tickers change over time.

- Alex uses norgate and described its convention: current tickers as-is, delisted securities as ticker + last-traded date.
- Quarry614 offered a practical workaround for the underlying problem (tracking changes without full symbology): diff the symbol list at test start vs. test end, then ask an LLM to explain what changed (merger, rename, bankruptcy) and when, to decide whether to exclude or substitute.
- Jakub asked for FIGI lookup sources beyond Bloomberg; bdkoepke pointed to OpenFIGI, noting he'd personally worked with IBKR roughly eight years ago to get FIGI identifiers added to their reports and TWS platform.

**Sentiment:** A real, unglamorous data-engineering problem (nobody has a clean universal symbology solution) with a mix of partial fixes offered — no single answer resolves it fully.

**Pull quotes:**
- bdkoepke: *"I try to map everything to ID_BB_GLOBAL, because then it's like IBKR conid <-> FIGI, CSInum <-> FIGI, Zacks <-> FIGI, etc."*
- Quarry614: *"take the symbol list at the beginning of test and at end of test period; find differences; and ask AI what changed (merger, new symbol, BK, etc.) and when? Could then exclude or substitute new symbol."*

## 4. Sourcing historical index constituency data

TheOriginal101 asked where people source historical index constituent lists (S&P 500, Nasdaq-100, and less common ones like DAX).

- mm suggested norgate first, but TheOriginal101 already uses it and needs something broader — norgate lacks intraday and European stocks — and asked about scraping alternatives (e.g., EDGAR filings for an ETF like QQQ).
- **mm gave a detailed, skeptical breakdown of the scraping approach** across three separate messages rather than a single dismissal:
  - Scraping is technically possible but likely introduces inconsistencies or large delays between when constituent/weight changes actually happen and when they become publicly visible.
  - If you only need historical (not real-time) data, scraping is viable but a lot of extra effort.
  - The sharpest point: scraped sources carry a real lookahead-bias risk — a filing might say an asset was added/removed on date X, but that information often wasn't publicly available until weeks or months later, which would silently leak future information into a backtest if not handled carefully.
- veng1 suggested the TWS API for IBKR account holders as an alternative source.
- bdkoepke contributed the most concrete resource dump of the thread: a GitHub prediction-market-analysis repo, an EODHD S&P Global constituents API doc, and a long list of direct CSI CSV download paths covering FTSE 100, DJIA/DJC/DJT/DJU, NDX, Russell 1000/2000/3000, S&P 100/400/500/600, and several sector indices — plus a general tip that historical ETF holdings (for an ETF tracking the target index) are often easier to find than the index's own constituent history directly.
- alvin confirmed norgate "does decent," then described his own workflow using **RealTest** (a backtesting platform) to extract daily constituents via a scan filter (`InSPX`) that outputs a CSV of every trading day's constituent list — a working alternative to scraping/vendor APIs for those with RealTest access.

**Sentiment:** Thorough, practically useful thread — no single perfect source emerged, but mm's lookahead-bias warning is a genuinely important methodological point for anyone building point-in-time index membership data, and bdkoepke's CSI CSV list is a directly actionable resource.

**Pull quotes:**
- mm: *"there's also the chance of whatever you're scraping from having some form of lookahead where it'll say xyz asset was added/removed to an index on abc date but that info wasn't publicly available until a month or two or three later"*
- bdkoepke: *"Or if you can find an ETF that tracks the index, historical ETF holdings are much easier to find."*
- alvin: *"I actually use RealTest for it... And it gives a beautiful csv, every trading day and their respective stocks in the constituent for that day"*

## 5. Skepticism toward a seasonal commodity-calendar trade (BOIL/UVXY-style structures)

Dan shared a Substack article describing a seasonal commodity calendar trade (an adjustment to the natural-gas BOIL trade, plus month-specific calendar trades, using VIX/SPX as a timing overlay), but flagged real confusion about the article's mechanics — unclear whether it trades in and out of positions daily based on VIX, and unclear whether returns are computed open-to-open, open-to-close, or close-to-close. His own testing (including costs) found the rules worked better without the daily VIX-timing overlay, just holding for the full month.

- Dan's bigger concern, stated directly: monthly seasonality claims built and evaluated using 2026 hindsight risk baking in look-ahead bias — a "best month, then simulate a trade on that month" methodology is inherently prone to curve-fitting, versus a seasonal index that's built incrementally using only data available up to each point in time (more robust, more complex to build).
- alvin agreed bluntly, calling the article's "find the best month, then backtest that month" framing exactly what it sounds like — guaranteed good Sharpe by construction, not a real edge.
- Dan concurred, adding that his own Sharpe from testing the idea "wasn't actually that impressive" and that he could feel himself overfitting as he iterated, so he stopped partway through (only reached July before quitting).
- mm redirected the conversation toward a more structurally interesting variant: **UNL/BOIL** instead of the original BOIL setup. UNL is a 12-month blend of natural gas futures (near-month plus the following 11 months); BOIL's lead contract instead jumps by two-month blocks (March covers Jan/Feb, May covers Mar/Apr, etc.). Combining them creates a structure similar to UVXY/VXZ or UVXY/VIXM — shorting levered near-term exposure while hedging with exposure further out on the curve. mm noted the only other seasonal trade of this style he'd found convincing was a crude oil variant, which stopped working after the product was changed post-COVID.
- MidKnight welcomed the idea, noting he'd been hunting for more futures-backed-ETF trades like this without much luck beyond manually trawling etfdb.com. mm suggested simply running the UNL/BOIL structure during the same seasonal months as the existing BOIL strategy, guessing winter months would likely still perform best (unverified).

**Sentiment:** Healthy skepticism winning out over an interesting-looking but methodologically shaky idea — the group correctly identified curve-fitting risk in the original article, while still extracting a legitimately interesting structural variant (UNL/BOIL) worth testing properly.

**Pull quotes:**
- Dan: *"my default thought is the backtesting is using future knowledge if we are deciding what is a seasonal period here and now in 2026... Seasonal indexes that get built on the fly based on data up to each date are more robust, but more complex."*
- alvin: *"This looks like just curve fitting... 'Lets take a look at the best month and lets simulate a trade on that best month' I mean, no doubt its gonna be a good sharpe..."*
- mm: *"it's a different trade from the original boil one but it turns into something similar to uvxy/vxz or uvxy/vixm where you're shorting levered near term exposure and hedging it with something further back."*

## 6. Building an in-house EPS forecast to benchmark against "gold standard" Street estimates

TimExcellent described experimenting with earnings-catalyst trading again, this time applying the base knowledge built up from the community — calculating his own EPS estimates and forecasts and comparing them against reported Street numbers, using FMP's Excel API plus Claude to test different feature-weighting approaches. Working from as-reported annual numbers and backing out his own figures made it easy to see where his estimates diverge from consensus. He noted that without paying for XENITH (Eikon for Retail), he can't directly benchmark how close his DIY approach gets to "gold standard" institutional estimates, but expects "close enough" to be good enough for his purposes. He closed with a lighthearted aside about throwing in a Jensen's Correction (a bias adjustment used in regression/forecasting contexts) mostly out of solidarity/habit.

**Sentiment:** Solo exploratory build, methodologically aware of its own limitations (no institutional benchmark to compare against) — standalone post, no responses this month.

**Pull quote:**
- TimExcellent: *"taking as reported annual numbers and then backing out my own numbers, its easy to see where things fall down... close enough is likely good enough."*

---

## Overall read

February's #data-analysis was a data-sourcing month more than a strategy month — four of six themes were pure "where do I find X" requests (cross-asset returns, short-sale history, security identifiers, index constituents), and robotkris and bdkoepke did the most legwork surfacing concrete answers, several pointing back to underused Lab resources (the cross-asset ETF dataset, the IBKR short-sale history) that even robotkris didn't reach for immediately. The identifier/symbology thread (Section 3) and the index-constituent thread (Section 4) are both worth bookmarking as reference material — no clean universal answer exists for either problem, but the community has assembled a decent toolkit of partial solutions (OpenFIGI, CSI's direct CSV endpoints, RealTest-based constituent extraction, ETF-holdings-as-proxy). The one strategy-adjacent thread this month (Section 5) is arguably the most valuable from a research-discipline standpoint: the group correctly flagged curve-fitting risk in a seasonal commodity trade before getting excited about it, while still salvaging a legitimately interesting structural idea (UNL/BOIL as a term-structure trade) worth testing on its own methodological footing rather than the original article's.
