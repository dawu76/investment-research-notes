# RW Pro Discord — #tradfi-trading digest, May 2026

- **Period:** May 1–31, 2026
- **Channel:** https://discord.com/channels/1368787013763072040/1370226295941763154
- **Raw transcript:** [rw-pro-tradfi-trading-raw-20260501-20260531.md](./rw-pro-tradfi-trading-raw-20260501-20260531.md)
- **Volume:** 58 messages, spread across several live-trading callouts (NG storage, end-of-month, holiday effects) and two substantive methodology threads (TLT window-dressing/rebalance overlap, a third-party "RP-like" strategy critique).

---

## 1. TLT window-dressing + rebalance overlap: a genuinely bad month

The month opened with Dan flagging that the TLT bond trade (which the group runs via both a "window dressing" (WD) seasonal effect and a separate rebalance/RP overlay) had a rough month when both signals landed on TLT simultaneously — though it stayed useful as an uncorrelated return stream against his broader book (AUM at ATH despite the loss). robotkris confirmed: *"one of the worst months for that trade... timing risk innit."* This triggered a real methodology question: when rebalance and window dressing both want a TLT position at the same time, do you cut size to avoid doubling up, or run each independently at full notional? Dan sizes the rebalance leg using SPY-equivalent notional (not vol-adjusted for TLT's lower vol) as a crude size-down; Yan admitted going full size on both legs with no adjustment, unresolved. Rachit added he'd diversified the window-dressing trade this month by including small Canadian bond exposure alongside the usual instrument. A partial recovery note came May 9: Yan closed the short leg for a small profit, but Dan noted the WD leg alone had gone from solidly positive to negative for his personal start date — patience being the operative word.

**Sentiment:** A real, acknowledged drawdown month for a core group strategy, handled with equanimity — no panic, more "timing risk is real, stay diversified across return streams."

**Pull quotes:**
- robotkris: *"Yeah one of the worst months for that trade. Timing risk innit."*
- Dan: *"Curious if anyone's implementation is cutting size when both rebalance and window dressing take on TLT at the same time?"*
- Dan (later): *"That one month though puts window dressing from positive well into negative though (for my start date anyway). Patience.."*

## 2. Live-trading callouts: NG storage & end-of-month index futures

Sam continued posting near-real-time updates on two of his systematic trades throughout the month: a **natural-gas storage report trade** (enter just before the weekly EIA report, exit 15–30 min after) and an **end-of-month equity index futures trade** (buy futures 20–30 min before the close on the last trading day, exit at close). Results were mixed and reported transparently — a -15 pip loss on 5/1, a -40 pip loss reported 5/12 (exited quickly), a small win on 5/22 (exited after 5 minutes), and a skip on 5/21 (traveling) that turned out to be the right call since it would have lost. He also flagged a seasonal edge: **US holidays historically shift the next-day up-day odds from ~52% to ~62%** for index futures, prompting a specific trade callout ahead of the May 25 Memorial Day long weekend.

**Sentiment:** Transparent, disciplined live-trading log — useful as a real-world reference for what "high Sharpe on paper, noisy in practice" looks like week to week (echoed explicitly in thread 4 below).

**Pull quotes:**
- Sam: *"Heads up, US holiday on Monday, better odds (62% v 52%) than usual of being up day tomorrow. Buy index futures, hold till close."*
- Sam: *"lost 40 pips on ng storage last week...was fortunate exited pretty quickly."*
- Sam: *"NG storage gas trade: didn't do last week, was on plane to Switzerland, just as well as it was a loser."*

## 3. High-Sharpe naive strategies: a caution from experience

In direct response to Quarry614 asking whether Sam varies his event-driven NG/index trades based on prevailing VIX level, Sam gave a notably candid risk-framing answer: it's a naive strategy purely trying to capture a specific event move, someone (4D) backtested it and found a high Sharpe ratio, but Sam explicitly doesn't scale up on the back of that because **"high Sharpe strategies crumble."**

**Sentiment:** A useful, quotable risk-management heuristic from someone actually trading the strategy live rather than just backtesting it.

**Pull quote:**
- Sam: *"I think @4D tested it out, had high Sharpe. But high Sharpe strategies crumble. So wouldn't go crazy on it."*

## 4. Third-party "RP-like" strategy critique (recency bias, ticker selection)

danielscapital shared a thread (via a paywall-free mirror after Euan asked for a non-X link) describing what looked like a souped-up risk-parity-style strategy. Dan (RW member) gave a detailed critique: heavy **recency bias** in the backtest — the test period favored Bitcoin, Gold, and QQQ, and notably excluded QQQ's brutal 2000–2010 lost decade. danielscapital pushed back that the critique depends on strategy framing — if it's meant as a "beta amplifier with timing overlays" rather than a diversified risk-premia portfolio, the ticker concentration may be more defensible; Dan largely agreed as long as the high historical Sharpe isn't used naively for portfolio-level sizing/allocation, since regime dependence should be expected going forward. TimExcellent flagged a related macro-uncertainty concern specific to date center/chip buildout dynamics feeding into any such momentum/timing strategy right now.

**Sentiment:** Constructive, technically rigorous skepticism — the group's default posture toward third-party strategy claims (mirrors the vol-forecasting skepticism seen in #general this same period).

**Pull quotes:**
- Dan: *"It does look like heavy recency bias... it has excluded the poor period of 2000-2010 where it just lost money for 10+ years straight."*
- danielscapital: *"If you frame this as a beta amplifier with timing overlays rather than a diversified risk premia portfolio"* [the ticker concentration is more defensible].

## 5. Kelly Criterion clarification (from a live portfolio-construction session)

FullMetal37! asked what the "Kelly Ratio" mentioned in a recent portfolio-construction session referred to. Edux and Marco gave quick correct answers (optimal capital fraction to maximize long-term log growth; approximately mean/variance); Euan (evidently the session presenter) then gave the fuller, precise answer and floated doing a dedicated presentation on the topic — a good signal that a deeper Kelly-sizing session may be coming in a future webinar.

**Sentiment:** Educational, well-resolved — a core quant-sizing concept getting reinforced for newer members.

**Pull quote:**
- Euan: *"The kelly criterion is to maximize log growth. The kelly ratio is the proportion to invest that fulfils that criterion. And an approximate equation for that ratio is mean/variance."*

## 6. Calendar/seasonality effects beyond the well-known US patterns

Rachit asked whether holiday-effect anomalies (like the US pre/post-holiday drift) exist outside the US market or are a purely American artifact — left largely unanswered directly, but it fed into a related crypto-market seasonality tangent: Euan noted BTC used to have pronounced day-of-week patterns (useful for trading old FTX "MOVE" contracts) and asked whether that pattern has faded; ASlan separately confirmed the holiday-effect pattern specifically doesn't hold for BTC. mm shared a genuinely interesting historical alpha anecdote: shorting the crypto "MOVE" index on Saturdays and trading against predictable rebalancing flows in 3x leveraged bull/bear tokens used to be *"some of the easiest money ever"* — before conceding in hindsight it was foolish to keep capital somewhere with such a transparently exploitable (and thus eventually arbitraged-away or platform-risk-prone) structure.

**Sentiment:** Nostalgic/cautionary — a reminder that even genuinely easy historical edges (especially in crypto microstructure) carry counterparty/platform risk that eventually dominates the P&L story.

**Pull quotes:**
- mm: *"shorting move on saturdays and longing/shorting xyz shitcoin ahead of them predictably rebalancing their 3x bull/bear tokens was some of the easiest money ever."*
- mm: *"in hindsight i was a moron for keeping money somewhere that would lose so transparently."*

## 7. Market structure notes: semiconductor futures, BOIL split, SpaceX IPO/Nasdaq inclusion

Several shorter market-structure items worth flagging:
- **New semiconductor futures market**: CME launching contracts to hedge GPU rental-rate/AI infrastructure cost exposure (per a shared CNBC piece); Rachit half-joked about SaaS firms building out futures trading desks as a result.
- **BOIL (natural gas 2x ETF) did a 2:1 share split** on 5/28 — a heads-up for anyone with open positions or systematic trades referencing the ticker/price level directly.
- **ProShares "Decline of the Retail Store ETF"** — ticker **EMTY** — flagged half as market color, half as a genuinely funny/apt naming choice.
- **SpaceX IPO (June 12) and prospective Nasdaq-100 inclusion (June 27)** raised by 4D as a potential repeat of TSLA's 2020 S&P 500 inclusion trade (the well-known "index inclusion pop" pattern); Matt G said he's tempted to short once it actually joins the index, and Sam noted the offsetting mechanical bid from index trackers forced to buy — flagging this as a live setup to watch into June.

**Sentiment:** Useful forward-looking market-structure awareness — the SpaceX/Nasdaq-100 setup in particular is a concrete, dated trade idea worth tracking into next month's digest.

**Pull quotes:**
- 4D: *"spaceX ipo on June 12, and join nasdaq 100 on June 27. Would it replicate the move of TSLA in 2020 when it was going to join sp500."*
- Matt G: *"I feel very tempted to short it once it hits the index."*
- Sam: *"Thing is all the index trackers etc would have to buy it...."*

---

## Overall read

May's #tradfi-trading was dominated by two threads that both circle the same underlying lesson: **known, well-backtested edges have real timing/regime risk that live traders actually eat**. The TLT window-dressing/rebalance overlap produced one of the group's worst months for that trade this year, and Sam's live NG-storage/event-trade log showed exactly the noisy, mixed week-to-week reality behind a "high Sharpe" backtest — a point he made explicit himself. The third-party RP-strategy critique reinforced the same skepticism toward backtest-only claims seen elsewhere in the community this period. The most actionable forward-looking item is the **SpaceX IPO (June 12) → Nasdaq-100 inclusion (June 27)** setup, which at least two members are already positioning to trade as an index-inclusion pattern — worth revisiting in June's digest to see how it played out.
