# RW Pro Discord — #vol-book-club-chat digest, June 2026

- **Period:** June 1–30, 2026
- **Channel:** https://discord.com/channels/1368787013763072040/1387280068182540390
- **Raw transcript:** [rw-pro-vol-book-club-chat-raw-20260601-20260630.md](./rw-pro-vol-book-club-chat-raw-20260601-20260630.md)
- **Volume:** 40 messages, a low-volume, high-signal channel — mostly live trade callouts from one active member (Sam) punctuated by a few substantive technical threads. Activity clustered in three windows: June 4–5, June 10–19, and June 25–26.

---

## 1. Structuring a bullish view when IV is expensive (quantum ETFs)

nxtrador asked a genuinely common options-structuring dilemma: bullish on quantum computing, but IV on quantum ETFs is elevated — call spread, or just buy delta-one (stock/spot)?

Euan's answer was equal parts humor and a real point about trader psychology. His actual advice, stripped of the joke: if the thesis is simply "I'm bullish," skip the options complexity entirely and just buy the underlying. He explicitly named the trap being avoided — reaching for an options structure by default just because you self-identify as an options trader, rather than because the trade actually calls for one. nxtrador's reply suggested the point landed.

**Sentiment:** Light-hearted but substantive — a reminder that expensive IV is itself information, and the simplest expression of a directional view is often correct.

**Pull quotes:**
- Euan: *"if your thesis is just 'bullish'... then just buy the stock. And, seriously, well done for checking yourself. the 'i am an option trader' mindset is a very real trap."*
- nxtrador: *"This post alone made my yearly subscription worth it."*

## 2. Systematic short-vol-around-macro-events research (4D's framework, extended by GeirN)

The month's most substantive technical thread. 4D shared a systematic setup: short VXX around NFP, CPI, and FOMC releases, entering 1 minute before the event and exiting 5 minutes after at mid-price, with a backtested equity curve from 2024–2026 that drew immediate praise from robotkris.

William asked a sharp clarifying question — his understanding was that most FOMC-related vol resolution happens in the days *before* the announcement, not in the minutes around it, so he wanted to confirm 4D's timing was genuinely minutes-scale rather than hours. 4D confirmed: for FOMC specifically, open at 1:59pm, close at 2:05pm — a 6-minute window, not a multi-day one.

GeirN then did the most substantial follow-on work of the month, independently extending 4D's framework to a much broader set of macro events:
- Built out `massive_prices_get` (his own wrapper around the massive.com stocks API, using DuckDB as a local cache to speed up retrieval) and `newsEvents_get` (pulling event data from a list of URLs) to run the same short-vol backtest across a wide event set: NFP, CPI, PPI, PCE, retail sales, jobless claims, JOLTS, ISM manufacturing/services, ADP employment, housing starts, industrial production, GDP advance, FOMC statement, and FOMC press conference.
- Found jobless claims produced good numbers alongside the known FOMC/NFP/CPI edges, across a 2021–2026 per-year breakdown — though he was careful to flag the results are **pre-transaction-cost** and that he'd already caught and fixed one sign error (JOLTS) before sharing.
- Reposted and re-explained the same methodology two days later (June 18) when Marco, Rachit, and FullMetal37 picked the thread back up asking how the FOMC trade is typically structured — good evidence the analysis held up under a second round of scrutiny from new participants.
- **4D's own read on GeirN's extended results was appropriately skeptical**: the NFP-day edge looked good, but "really good only in 2024" — a useful caution against over-generalizing a short sample.

**Sentiment:** Genuinely collaborative research — a member-shared framework got meaningfully extended by another member within days, with healthy skepticism about sample size and cost-adjustment applied throughout by multiple participants, not just the original poster.

**Pull quotes:**
- 4D: *"Short VXX on NFP + CPI + FOMC, enter 1 min before the event, exit 5 minutes after the event, mid-price."*
- GeirN: *"Jobless claims seem to have good numbers as well, but there are many of them, and I haven't tested with transaction cost... also quite likely that I have made mistakes somewhere."*
- 4D: *"great work! but it seems that the return on nfp days is really good only in 2024."*

## 3. Does the FOMC short-vol trade still work? A live real-time test, and a skeptical historical read from Euan

The June 18 FOMC meeting became a live test of the strategy discussed in section 2, and the results were genuinely mixed in real time:
- Sam ran it live and reported **-1.7%** on the trade, then later clarified his actual exit timing was off — he exits within the first 15 minutes, but this particular meeting would have needed a 15-minutes-to-the-top-of-the-hour exit instead.
- Rachit, watching the same setup, noted a few minutes before the presser wrapped that the move "very much looks like the inverse of the usual today" — a live acknowledgment that the pattern was behaving atypically that day.
- GeirN, whose own backtest results were being discussed in real time by the group, added an important caveat live: *"do not trust my analysis, I can share my functions if it helps"* — appropriately humble given the trade was actively losing money as they spoke.

Euan then supplied the most valuable context of the thread — a multi-year, experience-based read that reframes the whole discussion: the FOMC vol trade **used to be exceptionally reliable** (his words: "the most consistent winner ever," roughly four years without a loss) but **has been "a bit useless for the last few years."** Sam and mm's live 2026 results corroborate this directly — Sam: "It's not been good this year"; mm: hasn't traded it consistently until 2026 and jokes his timing is "perfect" (i.e., started right as the edge faded).

**Sentiment:** Cautionary and well-evidenced — this is the clearest example in the month of a previously-reliable systematic edge showing real signs of decay, corroborated by both live P&L and Euan's longer memory of the trade's history.

**Pull quotes:**
- Euan: *"I haven't lost money but it used to be the most consistent winner ever. I think it went for 4 years without a loss."*
- Euan: *"The fomc vol trade has been a bit useless for the last few years."*
- Sam: *"minus 1.7% on the short vol FOMC trade."*

## 4. Fed chairman transition — a macro regime risk to watch

Ahead of the June 18 FOMC meeting, Sam flagged a standalone macro consideration: a new Fed chairman has been appointed, and he'd seen stats suggesting the S&P 500 tends to decline in the three months following a new chair's appointment — while immediately caveating that the sample size behind that stat is necessarily small (few historical chair transitions to draw from).

**Sentiment:** Informational, appropriately hedged — a real regime-change risk factor worth being aware of for anyone trading vol or equities around this transition, but not treated as a strong signal given the small sample.

**Pull quotes:**
- Sam: *"I've seen some stats that say after a new chair is appointed, the S&P500 has gone down in the following 3 months. The sample size is of course small."*

## 5. Live trade log: event-driven VIX/ES scalps through the month

Throughout June, Sam posted a running log of small, fast, event-driven trades around NFP, CPI, and PCE releases — mostly short-dated VIX futures or ES scalps held for minutes:
- +50 pips on June VIX around a CPI print (later corrected/clarified to -5 pips on a follow-up).
- A Core PCE short-vix trade on June 25, sized deliberately small ("shorted a small amount"), closing +15 pips. Sam himself noted the self-aware pattern: *"always a winner when you have a small amount on!"*
- A tangential exchange with a member questioning whether shorting VIX futures around these events is even the right instrument versus simply going long ES — Sam's implicit answer, given he kept running the VIX version, was that he prefers the vol-specific expression.

**Sentiment:** Casual and transparent — small, frequently-sized trades shared in near-real-time, useful mainly as a running data point on how the FOMC/NFP/CPI short-vol edge (section 3) is performing week to week rather than as investment advice in itself.

**Pull quotes:**
- Sam: *"+15 pips (always a winner when you have a small amount on!)"*

## 6. Closing thought: vol's negative correlation to equities is strong, but event risk breaks the pattern

Euan closed out the month's activity with a concise, generalizable observation tying the earlier threads together: the negative relationship between equities and volatility is very strong as a baseline, but **uncertain events — economic releases specifically — disproportionately affect vol** relative to that baseline relationship. This is effectively the theoretical justification for why event-driven short-vol trades (sections 2–3) exist as a distinct strategy in the first place, separate from simply being short vol as a directional equities proxy.

**Sentiment:** Reflective, synthesizing — a good one-line framework for why this channel's entire month of activity (event-driven vol trades) is a coherent strategy rather than scattered trade ideas.

**Pull quotes:**
- Euan: *"although the negative relationship between equities and vol is very strong, uncertain events like economic releases disproportionally affect vol."*

---

## Overall read

June was a quiet month by message count but produced one clear, well-evidenced finding: **the FOMC short-vol trade — historically one of the community's most reliable systematic edges (per Euan, roughly four consecutive years without a loss) — has degraded meaningfully over the past few years**, corroborated by both Euan's long-memory read and live 2026 P&L from Sam (a losing June 18 trade) and mm (only started trading it consistently this year, ironic timing acknowledged).

1. **GeirN's extension of 4D's macro-event short-vol framework to a broader event set (jobless claims, ISM, PPI, retail sales, etc.) is the month's best piece of original research** — genuinely additive work built collaboratively on another member's initial post within days, complete with appropriate caveats about transaction costs and small samples.
2. **The Fed chairman transition is a live regime-change risk worth monitoring** into Q3, per Sam's flagged (if small-sample) historical pattern of post-transition equity weakness.
3. **Euan's framing of vol/equities correlation plus event-driven disproportionate effects (section 6) is a useful mental model** for evaluating any new event-driven vol trade idea that surfaces in future months — is the trade harvesting the baseline negative correlation, or the event-specific dislocation on top of it?
4. Nothing new or actionable emerged on the quantum-ETF options question (section 1) beyond Euan's general "don't overcomplicate a simple bullish view" guidance — worth revisiting only if a member brings a more developed thesis.
