# #tradfi-trading digest — Robot Wealth Community (Feb 2026)

**Period:** 2026-02-01 to 2026-02-27 (no channel activity Feb 28)
**Channel:** https://discord.com/channels/1368787013763072040/1370226295941763154
**Source:** `rw-pro-tradfi-trading-raw-20260201-20260227.md` (228 messages, verbatim transcript)

---

## 1. Natural gas / BOIL vol blowup and the ongoing NG-storage event trade

**Question raised:** Was the early-Feb natural gas vol spike a sign the BOIL strategy is broken, and is trading the weekly NG storage report still a durable edge?

**Findings:**
- On Feb 3, CME pro-cyclically raised margin rates on silver (+36%) and gold (+33%) right after the market had already started correcting — bdkoepke flagged this as a recurring pattern (margin hikes arriving *after* the move, not before).
- The same week, natural gas whipsawed hard on an Arctic-weather/holiday collision: Monday was a market holiday, so rebalancing couldn't happen until Tuesday's close, "so bad luck squared, doesn't happen very often" (Dan). deal_me_in reported the underlying strategy down 23% even after a big win day, saved only by small position sizing (portfolio down just 1.23%).
- **Euan** stepped in with the framing that stuck: *"a positions dollar volatility is largely on you. if you BOIL position is too volatile you should trade it smaller... asset volatility is beyond our control. position volatility isn't."* He noted he thought hard about whether to say it — a gentle but direct correction to people blaming the instrument rather than their sizing.
- **robotkris** confirmed the scale of the move with a concrete number: he entered the BOIL trade in November at ~80 vol (20-day rolling); by Feb 3 it was running at **280 vol** — a >3x increase — so cutting size was "absolutely the right thing to do."
- Separately, Sam kept running the weekly NG-storage-report event trade all month (short gas around the number) with a real-money track record visible in the transcript: +97 pips (Feb 5), +26 pips (Feb 12), +120 pips (Feb 13), then a −36 pip loss (Feb 27). Sam's own framing: *"Just a market inefficiency. Like the BOIL trade... it works till it doesn't."*
- BOIL itself technically rolled fully into the May NG contract by Feb 12 (per a holdings CSV `si` posted), and Sam closed the BOIL trade entirely on Feb 24, a few days before original plan, citing a decent overall profit and thanking Euan.

**Sentiment:** Cautious but unshaken — the vol spike was treated as a sizing lesson, not a reason to abandon the trade. Consensus was that position-level risk management (not the underlying's volatility) is what matters.

**Pull quotes:**
- Euan: *"if you BOIL position is too volatile you should trade it smaller... asset volatility is beyond our control. position volatility isn't."*
- robotkris: *"when I entered the BOIL trade back in November, it was running at about 80 vol... It's now at 280, using a 20-day rolling window. So reducing size is absolutely the right thing to do."*
- Sam (on exit): *"I'm out of the $BOIL trade. A few days early, but it's ok. Decent profit overall."*

---

## 2. Trend following: is it worth running, and how

**Question raised:** FullMetal37! kicked this off asking whether RW has content on general trend following beyond the YOLO strategy — quickly expanded into a long, multi-day thread on whether to DIY trend following, which ETF wrappers are worth holding, and what realistic long-run returns look like.

The thread split into distinct sub-questions, each worth calling out separately:

- **Is TF viable in mature markets?** MidKnight's hunch was that a model like YOLO isn't effective in more mature markets; Rachit countered that trend "worked in commodities but depends heavily on diversification."
- **DIY vs. buying an ETF.** Dan gave the most detailed real-account answer: he's run TF himself since Nov 2024 and finds it a good complement to the RW strategies (low correlation), but it demands real capital — futures margin, high-cost CFDs as an alternative, and (his view) a minimum of six figures to run at reasonable vol target with enough contracts for diversification. He explicitly steered away from Carver's AFTS system as "a little too complex and messy to start with," preferring to get trading first and add complexity later, and recommended Clenow's *Following the Trend* (2nd ed.) as a simpler on-ramp with demo strategies that only require daily transacting.
- **Why do CTAs/TF ETFs underperform?** Dan relayed a discussion from TF friends: the #1 reason cited was including equity indices in trend models, which "does a poor job capturing both sides" and increases correlation to the S&P — better handled by other strategy types (carry, diversified MR, risk premium). Bonds are "fine but extremely correlated" to each other. Currencies are the hardest market to trade but offer real diversification if sized right.
- **ETF-specific critique.** alvin was skeptical of TF ETFs generally — DBMF flat for 5 years including some of the strongest equity bull years, "at the same price as 3 years ago." Jakub explained DBMF runs at low vol (~7%/yr) and sits mostly in T-bills, paying the yield out as dividends — which alvin hadn't been including in his TradingView comparison (fixing this got him to ~0.76 Sharpe since inception). Jakub flagged **AHLT** (an under-promoted, sub-1%-fee ETF wrapper of the flagship AHL fund) as more interesting than DBMF, and shared a real private-fund track record showing the "Alts" sleeve keeping pace with the S&P and diversifying the 60/40 book during 1H22.
- **Reference data.** bdkoepke pointed to the SG Trend Index and BTOP50 for long-run CTA benchmark data (net of fees roughly 3.5%/yr excess since 2000, gross), plus barclayhedge.com and hfr.com as further data sources, and shared his own background: "I built a skunkworks CTA... work for a CTA firm currently... a lot of people struggle doing it over a long time horizon."
- **A working demo.** User `-k` shared a simple EWMAC-based (Carver-style) implementation with a notebook and backtest: ~0.8 Sharpe, 13% CAGR at a 15% vol target, beta 0.2 and 28% correlation to SPY since 2015.
- Jakub closed the thread with the line the group kept repeating afterward: *"TF is like a hot bipolar girlfriend. Looks good in pictures, makes your life hell."*

**Sentiment:** Broadly constructive — real practitioners in the channel are running TF live and see it as a genuine diversifier, but the group was consistent that off-the-shelf ETFs (DBMF, CTA, KMLM) are too low-vol to move the needle and that DIY requires real capital and patience through drawdowns.

**Pull quotes:**
- Dan: *"I don't want to need a live box connected 24/7 like with pysystemtrade... I recommend Clenow's book 'Following the Trend' 2nd edition."*
- Jakub: *"The difficult part of trend following is living with it. TF is like a hot bipolar girlfriend. Looks good in pictures, makes your life hell."*
- bdkoepke: *"I think a realistic excess return (gross of fees) is somewhere between 0-5% over the long-run, where the SG trend index has been approximately 3.5% since 2000."*

---

## 3. Short-vol event trading — Sam's live book and the philosophy behind it

**Question raised:** Is systematically shorting volatility around scheduled events (FOMC, CPI, earnings, political speeches) a durable edge, and how should exposure be sized relative to a "constant short vol" book?

- Sam ran this as a live, visible strategy all month — earnings straddles/calendar spreads (Amazon, Roblox), FOMC and CPI positioning, a SCOTUS tariff ruling (+155 ticks on UVXY), and Trump speeches (+50 pips, "there was at least 100 pips there... hope someone did it"), plus a State of the Union short (+102 pips).
- FullMetal37! asked directly whether Sam goes long vol into FOMC and just shorts over the event itself; Sam's answer was to go long *before* the event and flip.
- The philosophically important exchange came from llIHeroic, who pushed on methodology: does Sam track short-vol event trades separately from a constant-exposure short-vol book, given the latter would also collect ambient VRP carry? Sam's answer: yes, they're separate strategies — event trades are sized **10x** the constant short-vol allocation, because "there's no way I could hold a constant exposure of that size all the time."
- llIHeroic pressed further: a "decent" short-vol strategy is roughly 0.8–1+ Sharpe, so is the event-trade Sharpe high enough to justify 10x sizing, and how long has Sam been running it? (Answer, from Sam: a few years — and *"I think Euan said he's being doing it for 30 years!"*)
- **Euan** then gave the group's clearest statement of the actual risk discipline behind selling event vol, prompted by a separate but related question from Marco about whether earnings shorts are naked straddles: Euan confirmed yes for the earnings trade specifically, but was emphatic that the *general* rule he follows is to stay net long options overall — "almost always I'm long long dated index options or something... you don't need to be in every individual product." Pressed by Henboss ("you should only short vol when it's overpriced, or you'll blow up eventually"), Euan's reply was unambiguous: *"I've never seen an event when vol isn't overpriced. And you never need to be naked short vol. That is asking for trouble."* He closed with a striking track-record claim: *"I've pretty much been selling event vol for 30 years and have managed to not blow up (yet)."*

**Sentiment:** High confidence, grounded in a long track record — but explicitly framed by Euan as risk-managed (net-long-options overlay), not naked short vol, despite individual event trades themselves being naked.

**Pull quotes:**
- Euan: *"i think i said once that the most robust risk control is to be net long options, but that isn't a 100% firm rule... almost always I'm long long dated index options or something."*
- Euan: *"I've never seen an event when vol isn't overpriced. And you never need to be naked short vol. That is asking for trouble."*
- Euan: *"I've pretty much been selling event vol for 30 years and have managed to not blow up (yet)."*
- Sam: *"By large size, I mean 10x the short vol all the time strategy. There's no way I could hold a constant exposure of that size all the time."*

---

## 4. Covered-call ETFs and cross-sectional options mispricing

**Question raised:** Following a "active ETFs are trash" internal notebook, mm asked whether covered-call ETFs (QYLD-style) are structurally bad vehicles, and whether cross-sectional options mispricing across a universe of stocks is a real, tradeable edge.

- mm's opening take: most active ETFs are only "active" in that they mechanically repeat the same trade regardless of price ("trading a lot regardless of price is the height of dumb"), and covered-call funds specifically are a poor way to harvest the equity and volatility risk premia because margin costs eat ~20%+ of PnL unless applied to genuinely high-vol names (NVDA, TSLA).
- bdkoepke worked through the mechanics: long QQQ + short QYLD (long QQQ, short a call) nets out to a synthetic long QQQ call.
- This is where **Euan** gave the most substantive answer of the thread, unpacking the question in full: most active ETFs are bad because they trade indiscriminately, but the actual edge — cross-sectional options mispricing (finding stocks with cheap options relative to others) — genuinely "works," he confirmed flatly. The catch, in his words: *"please don't do it. It is a logistical nightmare. You need options on 50-200 stocks. Execution and cost management is crucial."* He drew a sharp distinction between cross-sectional mispricing (rare, hard to execute, real when found) versus single-product mispricing (the opposite dynamic — "the sweet spot is to watch a lot of things then trade when things get very mispriced"), and when MidKnight jokingly asked for "the 20% options recipe," Euan pointed to his own books, *"vol trading and positional option trading,"* as the actual answer rather than a shortcut.
- rodeo1203 brought supporting data: a Bloomberg SPX 30-day 50-delta IV vs. realized-vol comparison showing median VRP positive (~0.45) but mean negative (~−0.4) — i.e., the premium is real most of the time but occasionally punished hard by tail moves (consistent with Euan's framing).
- FullMetal37! added context that systematic 30dte SPY straddle selling has been roughly breakeven-to-slightly-positive over a 4-year lookback including the tariff tantrum, and that CBOE's Iron Condor / Iron Butterfly indices have been flat-to-negative since the early 2010s — coinciding with the popularization of "income"-style option-selling strategies (crowding as a plausible explanation raised by FullMetal37!).

**Sentiment:** Skeptical of the packaged product (covered-call ETFs), cautiously validating of the underlying edge (cross-sectional and event-driven options mispricing) — but only for those willing to build serious execution infrastructure.

**Pull quotes:**
- Euan: *"That is cross sectional. Finding stocks with cheap options relative to other stocks. That works. But please don't do it. It is a logistical nightmare."*
- Euan: *"cross sectional mispricing exists in options because exploiting it is hard. Valuation is easy but implementation is difficult. In a single product the opposite is true."*
- mm: *"it's hard to justify running it on something with 'low' annual returns because the margin eats ~20%+ of your pnl. with nvda/tesla/etc it's a lot more plausible."*

---

## 5. Instrument choice for short-vol trades: UVXY vs VXX vs SVXY/SVIX, and a VIX/VSTOXX relative-value idea

**Question raised:** FullMetal37! asked what determines the choice between SVIX, short UVXY, and SVXY for implementing short-vol trades, and whether there's a borrow-cost threshold that tips the decision.

- ASlan laid out the landscape: most people are short futures or short UVXY, some short VXX; SVXY is "pure volatility" (only ~50% short, so needs a bigger notional) with typically small borrow rates that spike only when vol is already high — meaning realized borrow cost tends to correlate with exactly the conditions that make the trade most profitable.
- Dan gave the most detailed practitioner comparison: he prefers **VXX** over UVXY — 30% initial margin vs. 120% at IBKR, and anecdotally easier to borrow at lower rates. Caveats: VXX needs to be sized larger than UVXY since it's unlevered, and it was delisted/relisted in 2019 (so backtests need to splice symbols across that date). He also runs SVIX in parallel as a second, independent VIX-system leg, deliberately using a *different* risk-management style — VXX carries a stop-loss for "Armageddon" scenarios, while his SVIX version runs with no stops (since it can only go to zero, and he's "not comfortable" letting an order-only-once-a-day stop trigger right before a snap-back). For backtesting further back than SVIX's inception, he uses SVXY as a splice, noting SVXY's leverage ratio changed after Volmageddon (2018), requiring stage-by-stage adjustment.
- Separately, **Stefan** proposed a genuinely new trade idea for the channel: a VIX/VSTOXX relative-value trade (inspired by Euan's IV-RV writing on SPY/QQQ). VIX and VSTOXX are highly correlated and mean-reverting relative to each other; Stefan built 30dte constant-maturity futures for both indices from firstratedata intraday data and found the dislocation effect holds even after controlling for the (not directly tradeable) index nature of VIX/VSTOXX themselves. Reported backtest: **Sharpe 1.2–1.6** depending on signal timing and z-score lookback, with low correlation to the existing UVXY/VXZ short-vol trade — a genuine diversifier if it holds up live.
- William flagged the real risk in Stefan's idea: occasional large dislocations when one of the two exchanges is closed, and a currency-hedging wrinkle since the two futures are denominated in different currencies (USD/EUR), meaning the contract ratio needs to track FX moves over time.

**Sentiment:** Practical and execution-focused — this was one of the more granular, "here's exactly what I run and why" threads of the month, with Stefan's idea standing out as a genuinely new, low-correlation addition to the group's short-vol toolkit.

**Pull quotes:**
- Dan: *"I like using VXX, initial margin short side is 30% compared to 120% for UVXY on IBKR... I do use SVIX too though... VXX has a stop loss in case there's Armageddon... my SVIX version has no stops because it can only go to zero."*
- Stefan: *"Result has sharpe 1.2 – 1.6 depending on precise implementation (time of day for the signal, zscore lookback) and as an added benefit really low correlation to e.g. the uvxy/vxz trade."*
- William: *"a key issue is to adjust for the USD-EUR exchange rate, as the 2 contracts are denominated in their local currency. so the ratio of contracts will change as the FX changes."*

---

## 6. Shorting leveraged (3x) ETFs against the underlying — equities, Japan, and crypto

**Question raised:** mm shared a paper on shorting 3x leveraged long ETFs while hedging with the underlying (rebalanced monthly to a 1:3 ratio) to harvest decay — sparking a discussion of where this works best and where it breaks.

- mm summarized the paper's finding: the strategy works best on the most volatile underlyings — QQQ/TQQQ-style pairs, SOXX/SOXL (semis), XBI/LABU (biotech) — where realized decay is largest.
- MidKnight was struck that the same pattern shows up with the "opposite shape" in Japan versus the US; mm explained the likely mechanical reason: US 3x ETFs get leverage via swaps (continuously paying interest on borrowed notional), while Japanese products use futures, so carry/roll dynamics dominate instead of financing cost — "both sides work in JP" as a result.
- The practical blocker for Japan: alvin had looked into shorting there and found "any sort of shorting in JP looks amazing, till I checked their short inventory and realised there's nothing (in IB)" — barely any borrow available except large caps.
- For US/global equity indices, alvin quantified the realistic payoff: the 3x levered ETFs "usually results in 4-5% pa, close to the risk free rate," similar for liquid 2x products — underwhelming after financing cost.
- The standout performer in the discussion was **crypto**: alvin and Stefan both run this strategy live on BTC/ETH/SOL/XRP leveraged products (BITU/BITX/BITI for BTC; IBIT/ETHA/BSOL/XRP for spot hedge legs), reporting **10-14%/yr at 1+ Sharpe** — well above the equity-index version. Stefan explained the edge holds up because "you have the carry + the levered etfs, so the borrow fees dont kill it." The shared operational risk across both equities and crypto: rebalancing (especially via market-on-close orders) can hit points where the short leg has no borrow available, forcing unwanted directional exposure on the long leg — alvin said this eventually pushed him to stop trading the equity version, worried "a huge major move + no borrows will probably wipe off a year of profit." Stefan mitigates this in the crypto version by splitting exposure across multiple leveraged-ETF issuers (e.g., splitting BITU/BITX) specifically to reduce the odds of *all* borrow drying up simultaneously.

**Sentiment:** Genuinely promising, but treated as an operational-risk trade more than a pure alpha trade — the group's consensus was that the edge is real but bounded by borrow availability, and crypto currently offers the best risk-adjusted payoff of the venues discussed.

**Pull quotes:**
- alvin: *"Any sort of shorting in JP looks amazing, till I checked their short inventory and realised there's nothing (in IB)."*
- alvin (on crypto leveraged ETFs): *"The ones that looks decent actually is the BTC etfs. Returns 10-14% a year... At a 1+ sharpe."*
- Stefan: *"the 'cool' thing with this is you have the carry + the levered etfs, so the borrow fees dont kill it."*

---

## Overall read

February's channel activity clustered around **volatility and its harvesting** — whether that's natural gas (BOIL, NG storage events), equity index options (event vol, cross-sectional mispricing, covered calls), or the VIX complex itself (UVXY/VXX/SVIX instrument selection, and a new VIX/VSTOXX RV idea from Stefan). The month opened with a real stress test (the NG margin/vol spike on Feb 3) that reinforced the group's existing risk-sizing discipline rather than shaking confidence in the underlying trades — both robotkris and Euan's contributions func­tioned as calibration checks ("here's the actual vol number," "here's the actual risk rule") rather than course corrections.

Trend following was the other major thread, driven less by a live blowup and more by a newer member's onboarding questions — the group's answer converged on "DIY with real capital and patience, skip the retail ETF wrappers" (DBMF/CTA/KMLM too low-vol to matter; AHLT flagged as a lesser-known exception).

The month's most novel contribution was Stefan's VIX/VSTOXX relative-value construction (Sharpe 1.2–1.6, low correlation to existing book) — a rare case of a member bringing a fully backtested, execution-detailed new trade to the channel rather than discussing an existing one. Euan's clearest standing lesson for the month, repeated across three separate threads (BOIL sizing, event-vol shorting, options mispricing): the edge is usually real, but almost always bounded by execution difficulty, position sizing, or both — "never naked," in his words, even when individual legs technically are.
