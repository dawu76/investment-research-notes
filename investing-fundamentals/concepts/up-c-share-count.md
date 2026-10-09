---
title: Up-C Structures and Share-Count Distortion (Class V / Class B Shares)
created: 2026-10-09
updated: 2026-10-09
type: concept
tags: [valuation, share-count, data-quality, capital-structure, concept]
sources: [Symbotic Q3 FY26 8-K Ex. 99.1 (sec.gov), MarketBeat, StockAnalysis]
confidence: high
contested: false
---

# Up-C Structures and Share-Count Distortion

Many screeners, brokerages, and comparison tools count only the **listed** share class (Class A) for companies with an Up-C structure. They leave out the paired Class V or Class B shares, which are economically equivalent. The result is an understated market cap and EV, and inflated "cheapness" on any metric built from consolidated figures (P/S, P/FCF, EV/EBITDA, cash per share).

---

## How an Up-C Works

- The listed company (PubCo) is a holding company that owns only **part** of an operating partnership (LLC/OpCo).
- Pre-IPO owners (founders, sponsors, strategic holders) keep **OpCo units directly**. They also hold **Class V / Class B** shares in PubCo, which carry **voting rights only, with no economic rights**.
- The OpCo units plus the paired Class V shares can be exchanged **1:1 into Class A** at the holder's option, under an exchange agreement that usually lets PubCo settle in cash instead. Economically they are shares.
- PubCo consolidates 100% of OpCo's revenue, cash, and FCF. The pre-IPO owners' slice shows up as **"net income attributable to noncontrolling interests (NCI)."**
- Why companies use it: pre-IPO owners keep pass-through tax treatment, and exchanges give PubCo a tax-basis step-up. Under a **tax receivable agreement (TRA)**, PubCo typically pays the pre-IPO owners 85% of the resulting tax savings. The TRA liability on PubCo's balance sheet is debt-like and belongs in EV.
- **Size of the error:** total economic shares ÷ Class A shares. It is large in young Up-Cs where pre-IPO owners still hold most units (4.7x for Symbotic, below) and shrinks as units are exchanged into Class A over time.

## Why Data Providers Get It Wrong

- Each share class is reported separately on the 10-Q/10-K cover page (and as separate fields in the XBRL data that feeds use).
- Some feeds pull only the listed class, while others add up all classes. Coverage is **inconsistent across providers**, and sometimes differs between pages of the same provider.

## Which Metrics Break

| Metric | Built from | With a Class A-only count |
|---|---|---|
| EPS / P/E | Net income attributable to Class A ÷ Class A shares | Mostly OK: the numerator and denominator are both Class A only |
| Market cap, EV | Price × shares | **Understated** |
| P/S, P/FCF, EV/EBITDA, P/B | Consolidated (100%) figures ÷ partial share count | **Look too cheap** |
| Cash per share | Consolidated cash ÷ partial share count | **Overstated** |

**The tell:** P/E looks very expensive while P/S and P/FCF look cheap. When the two disagree that sharply, check the share count.

**EV fix:** the textbook EV formula adds NCI, but at book value, which is far below the market value of the exchangeable units, so a Class A-only market cap plus book NCI is still too low. Use price × all economic shares and don't also add NCI (that would count the pre-IPO owners' stake twice); add the TRA liability as debt.

---

## Worked Example: Symbotic (SYM), Oct 2026

Share count as of June 27, 2026 (Q3 FY26):

| Class | Shares |
|---|---|
| Class A (listed) | 128.9M |
| Class V-1 | 71.4M |
| Class V-3 | 403.6M |
| **Total economic shares** | **603.9M** |

At ~$42.35, using FY26 FCF of ~$300M and cash of $1.75B. The FCF figure is an estimate: the 9-month actual of $242.8M plus an assumed ~$57M for Q4, which the company guided only as positive.

| Metric | Class A only (129M) | All shares (604M), correct |
|---|---|---|
| Market cap | ~$5.5B | ~$25.6B |
| Cash per share | ~$13.60 | ~$2.90 |
| P/FCF | ~18x | ~85x |

- Q3 FY26: net income was $55.0M, of which $43.3M went to NCI. Class A diluted EPS was $0.09.
- The NCI share of Q3 net income (43.3 ÷ 55.0 = 78.7%) matches the Class V share of total economic shares (475.0M ÷ 603.9M = 78.7%), which confirms the share count.
- MarketBeat shows P/E of ~490x and, in a September 8 alert, a full market cap of $26.43B; other sources show market caps near $5.5B.

### Second-order trap: cash funded by customer prepayments

- SYM's cash of $1.75B is roughly equal to its deferred revenue of $1.73B ($1.55B current + $0.18B non-current). This is customer money for systems the company still has to build.
- Deferred revenue isn't repaid in cash; it is worked off by delivering systems. The cash it will consume is the cost of delivery, i.e. deferred revenue less the gross margin on it. So the truly free cash is much smaller than $1.75B, though above zero by that margin.
- FCF is inflated while prepayments build up and **reverses** as they run off. In Q3 FY26, deferred revenue fell $124M, receivables rose $156M, and FCF was **−$165M**.
- "No debt + lots of cash" overstates balance-sheet strength when deferred revenue is large.

---

## Other Up-C / Paired-Class Examples

Shake Shack, Planet Fitness, Dutch Bros, Bumble, TPG, StepStone, Hamilton Lane, and many companies that went public through SPACs in 2020–22. The non-listed class is often called **Class B** rather than Class V.

**Not the same thing:** ordinary dual-class stocks (Alphabet, Meta). There the unlisted Class B shares hold full economic rights in the same entity, and most providers include them in market cap.

---

## Checklist for Any Stock

1. Read the **10-Q/10-K cover page** and add up every class outstanding.
2. Look for a large **NCI line** on the income statement.
3. Compare market cap across **two or three sources**. A gap of 2x or more points to a share-count issue.
4. Recompute **consolidated revenue, FCF, and cash ÷ total economic shares** yourself.
5. Net the **cost of delivering deferred revenue / customer deposits** against cash before calling the balance sheet "cash-rich."
6. Add any **TRA liability** to EV as debt.

See also [[valuations]], [[pvgo]], and the full Symbotic analysis in [[sym-2-equity-report]].

References
- [Symbotic Q3 FY26 8-K Ex. 99.1 (SEC)](https://www.sec.gov/Archives/edgar/data/0001837240/000183724026000042/q3268-k_ex991.htm): primary source for the figures above
- [Symbotic Q3 FY26 results (Nasdaq)](https://www.nasdaq.com/press-release/symbotic-reports-third-quarter-fiscal-year-2026-results-2026-08-05): share counts by class, cash, deferred revenue, FCF
- [MarketBeat: SYM forecast](https://www.marketbeat.com/stocks/NASDAQ/SYM/forecast/): P/E ~490x
- [MarketBeat: Barclays target cut, 2026-09-08](https://www.marketbeat.com/instant-alerts/analyst-symbotic-nasdaq-sym-price-target-cut-to-3800-by-analysts-at-barclays-2026-09-08/): market cap $26.43B
