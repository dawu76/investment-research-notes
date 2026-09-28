---
title: Diversified Portfolio Backtests (1972-2025)
created: 2026-09-27
updated: 2026-09-27
type: comparison
tags: [comparison, framework, risk, inflation, bonds]
sources: [investing-quant/backtests/results/summary.md, investing-quant/backtests/results/layer1_results.md, investing-quant/backtests/results/layer2_results.md, investing-quant/backtests/results/layer3_results.md, investing-quant/backtests/data/SOURCES.md]
confidence: medium
contested: false
---

# Diversified Portfolio Backtests (1972-2025)

Backtests of a 20% gold / 20% Treasuries / 60% stocks portfolio and more diversified variants built only from liquid assets (no private equity or venture funds). Code and cached data live in `investing-quant/backtests/`. Every number here can be regenerated offline with `uv run --with pandas backtest.py --summary` (or `--layer 1|2|3`).

## Bottom line

- **P1 (20 gold / 20 10y Treasuries / 60 US stocks) had the highest return in every window with real data**: 10.5% a year from 1972 and 8.9% from 2001, with a worst calendar year of -17.0% (2008). ^[investing-quant/backtests/results/summary.md]
- **The Golden Butterfly had the best risk profile in every window**: worst year -8.9%, and the only portfolio with a positive real return across high-inflation years. It gave up 0.5 to 1.4 points a year versus P1. ^[investing-quant/backtests/results/summary.md]
- **Shifting the stock sleeve toward international cost return in every window**: about 1 point a year from all-US to all-international since 1972, and 1.7 points since 2001. ^[investing-quant/backtests/results/summary.md]
- **Trend-following helped in every version tested**, mainly by cushioning crises. The real-world CTA index added only a few tenths of a point a year. ^[investing-quant/backtests/results/layer2_results.md]
- **TIPS were a poor substitute for nominal Treasuries**: swapping them into P1 added no return and deepened the 2008 loss from -17.0% to -21.6%. ^[investing-quant/backtests/results/layer3_results.md]
- **Starting conditions drove results more than portfolio design**: the same portfolios returned 1.6 to 2.4 points a year less from 2001 than from 1972. Today's starting yields and valuations look more like 2001 than 1985.

## Portfolios tested

| Name | Mix |
|---|---|
| P1 | 20 gold / 20 10y Treasury / 60 US stocks |
| P2, P3 | P1 with the 60% stock sleeve split US/international (75/25, 50/50, 25/75, 0/100) |
| P1 with TIPS | 20 gold / 20 TIPS / 60 US stocks |
| P4 | 30 US / 15 intl / 10 US small value / 15 gold / 10 10y Treasury / 10 T-bills / 10 trend |
| P6 | P4 with TIPS in place of the T-bills |
| P5 Golden Butterfly | 20 US / 20 US small value / 20 10y Treasury / 20 T-bills / 20 gold |

All portfolios rebalance once a year. Returns are nominal USD total returns unless marked real. P4 was run with four versions of the trend sleeve: T-bills (no trend), a simulated trend rule, the Barclay CTA Index, and AQR's trend factor. The standard Golden Butterfly uses long-term and short-term Treasuries; here the 10y Treasury and 3-month T-bills stand in, so its bond sleeves carry less duration than the original.

## Results across windows

Some data starts late (Barclay CTA 1980, AQR 1985, the VIPSX TIPS fund 2001), so each window only includes portfolios with full data. \* marks results that rely on synthetic TIPS or the simulated trend sleeve. "Excess return / vol" is CAGR above T-bills divided by volatility. ^[investing-quant/backtests/results/summary.md]

| Portfolio | CAGR 1972-2025 | CAGR 1985-2025 | CAGR 2001-2025 | Excess return / vol (2001-25) | Worst year | Real return, high-inflation years |
|---|---|---|---|---|---|---|
| P1 | 10.54% | 10.22% | 8.92% | 0.63 | -17.0% | -1.9% |
| P2 (50/50 US/intl) | 10.16% | 9.51% | 8.12% | 0.53 | -19.0% | -1.6% |
| P3 all international | 9.59% | 8.61% | 7.23% | 0.42 | -21.0% | -1.5% |
| P1 with TIPS | 10.61%\* | 10.19%\* | 8.93% | 0.59 | -21.6% (VIPSX) | -0.8%\* |
| P4, no trend | 9.98% | 9.15% | 7.69% | 0.58 | -17.9% | -0.8% |
| P4 + simulated trend | 10.42%\* | 9.43%\* | 8.02%\* | 0.60 | -17.0% | -0.1%\* |
| P4 + Barclay CTA Index | n/a | 9.49% | 7.86% | 0.60 | -16.6% | n/a |
| P4 + AQR trend (after 3% fees) | n/a | 10.16% | 8.28% | 0.66 | -15.7% | n/a |
| P6 | 10.64%\* | 9.70%\* | 8.08% | 0.61 | -15.7%\* / -17.0% | -0.3%\* |
| P5 Golden Butterfly | 10.03% | 8.82% | 7.95% | 0.77 | -8.9% | +0.5% |

P1's real CAGR is 6.40% from 1972, 7.24% from 1985, and 6.25% from 2001. Annual data understates drawdowns: measured monthly, P1's worst drawdown was -25.9% and the Golden Butterfly's -17.5%. ^[investing-quant/backtests/results/layer3_results.md]

## Stress years

The last column is the annualized real return across the 11 years with CPI above 6% (1973-75, 1977-81, 1990, 2021-22). ^[investing-quant/backtests/results/summary.md]

| Portfolio | 1973 | 1974 | 1981 | 2002 | 2008 | 2022 | Real, CPI > 6% years |
|---|---|---|---|---|---|---|---|
| P1 | 6.7% | -1.9% | -7.7% | -5.0% | -17.0% | -14.3% | -1.9% |
| P2 (50/50 US/intl) | 6.8% | -0.8% | -6.6% | -3.2% | -19.0% | -13.1% | -1.6% |
| P1 with TIPS\* | 11.0% | 3.5% | -13.6% | -5.4% | -18.3% | -12.9% | -0.8% |
| P4, no trend | 3.6% | -1.3% | -1.1% | -4.2% | -17.9% | -9.4% | -0.8% |
| P4 + simulated trend\* | 6.0% | 2.1% | -0.7% | -2.7% | -17.0% | -9.8% | -0.1% |
| P6\* | 7.7% | 4.2% | -4.2% | -1.5% | -15.7% | -11.1% | -0.3% |
| P5 Golden Butterfly | 8.4% | 6.2% | 0.4% | 2.3% | -8.9% | -7.9% | +0.5% |

## Findings by question

### US vs. international stocks

- Portfolio CAGR falls roughly in a straight line as the stock sleeve moves from US to international, and volatility rises, because US stocks returned more (11.1% vs 9.4% for MSCI EAFE, 1972-2025) with lower volatility. ^[investing-quant/backtests/results/layer1_results.md]
- The US edge is recent. P1 beat the 50/50 version by 0.4 points a year from 1972 but by 2.0 points from 2010. In rolling 10-year windows, the US led in 24 of 45 and international in 21. International's longest lead was 14 straight windows (ending 1981-1994); the current US lead (12 windows, ending 2014-2025) ties the longest US stretch. ^[investing-quant/backtests/results/layer1_results.md]
- With US tech trading at a 20-year-high premium to defensives ([[market-newsletter-digest-2026-09-22]]), projecting the recent US edge forward is risky.

### Trend-following

| Source (1985-2025) | Excess over T-bills | 1980s | 1990s | 2000s | 2010s | 2020-25 | 2008 | 2022 |
|---|---|---|---|---|---|---|---|---|
| Simulated rule (3 assets, 2% cost) | 2.6% | 2.8% | 2.7% | 3.7% | 1.3% | 2.5% | +10.4% | -1.8% |
| Barclay CTA Index (net of fees) | 2.9% | 13.0% | 2.0% | 3.1% | 0.2% | 1.1% | +14.1% | +7.1% |
| AQR trend factor (after 3% fees) | 8.9% | n/a | 15.4% | 11.6% | 2.2% | -1.8% | +23.3% | +24.3% |

^[investing-quant/backtests/results/layer2_results.md]

- Returns for real CTAs and the AQR factor have faded over the decades. The CTA index's 1980s figure comes from only 15-21 programs that survived to report, so it's inflated.
- AQR's research factor beat the average real CTA by about 6 points a year even after an assumed 3% fee drag. Published research backtests are an upper bound on what funds deliver.
- Every trend version improved P4 versus holding T-bills in that slot and reduced the 2008 loss: +0.3 points a year for the simulated rule and +0.5 for the CTA index over 1980-2025, and +1.0 for AQR over 1985-2025. ^[investing-quant/backtests/results/layer2_results.md]
- The simulated sleeve's full-period 8.6% CAGR came mostly from one decade: its gold leg earned about 30% a year over T-bills in 1972-81 (long through the 1970s bull market, short into the 1981 crash). After 1982 the sleeve beat T-bills by about 2.5% a year. ^[investing-quant/backtests/results/layer1_results.md]
- See [[trend-following-concept]] and [[trend-following-strategy]].

### TIPS

- A model built on the Fed's market TIPS yields tracks the VIPSX fund closely (0.99 correlation, 2001-2025). The synthetic pre-1997 series, built from nominal yields minus survey inflation expectations, does not (0.58 correlation) and gets 2008-09 backwards (+13.6% in 2008 vs the fund's -2.8%), because surveys can't see TIPS liquidity sell-offs. Pre-1997 TIPS results are a rough sketch. ^[investing-quant/backtests/results/layer3_results.md]
- In high-inflation years, the annualized real return was -1.7% for T-bills, -3.3% for synthetic TIPS, and -8.4% for 10y Treasuries. TIPS beat nominal bonds but lost to T-bills, because inflation brings rate hikes: T-bills reset right away, while a long TIPS takes a price hit when real yields jump (1981: -21%). The real 2022 data shows the same ordering: VIPSX -12.0%, 10y Treasury -17.8%, T-bills +2.1%. ^[investing-quant/backtests/results/layer3_results.md]
- Nominal Treasuries were the better crash hedge: +20.1% in 2008, when TIPS fell. That's why replacing them with TIPS made P1 worse.
- A TIPS held to maturity still locks in its real yield. The 10y TIPS yield was 2.85% on 2026-09-24 (FRED DFII10), near its highest since 2008 ([[market-newsletter-digest-2026-09-20]]). See [[tips-how-they-work]].

### Gold and rebalancing

- Gold compounded at 8.9% a year from 1972 (year-end prices) but very unevenly: 16.2% in 1972-84, -0.7% in 1985-2000, 11.7% in 2001-2025. ^[investing-quant/backtests/data/annual_returns.csv]
- Annual rebalancing added about 0.95 points a year to P1 beyond the weighted average of its sleeves' own CAGRs, because gold's high volatility and low correlation with stocks gave rebalancing something to harvest. See [[rebalancing]] and [[geometric-vs-average-returns]]. ^[investing-quant/backtests/results/layer1_results.md]

### Why returns fall in later windows

The windows are nested, so the differences come from the years each later window drops. ^[investing-quant/backtests/data/annual_returns.csv]

| Period | CPI | T-bills | 10y Treasury | US stocks | Gold | P1 | P1 real |
|---|---|---|---|---|---|---|---|
| 1972-1984 | 7.5% | 8.2% | 6.1% | 8.7% | 16.2% | 11.6% | 3.8% |
| 1985-2000 | 3.2% | 5.7% | 9.9% | 16.8% | -0.7% | 12.3% | 8.8% |
| 2001-2025 | 2.5% | 1.8% | 3.3% | 8.7% | 11.7% | 8.9% | 6.3% |

- **1972-84 was mostly inflation**: high nominal returns, but only 3.8% real for P1.
- **1985-2000 started from the best conditions**: a 10y yield of 11.55% that then fell for 15 years, and stocks at a Shiller CAPE near 10. That period had the highest real return.
- **2001-2025 started from weaker ones**: stocks near the dot-com peak (CAPE in the mid-30s), a 5.12% 10y yield, and near-zero T-bill rates for much of the period.

The 10y yield was 5.18% in late September 2026, close to 2001's start, and US valuations are high again, so the 2001-2025 column is likely a better guide to forward returns than the longer windows. See [[equity-risk-premium]] and [[bond-supply-tsunami-2026]].

## Choosing between them

- **Maximum growth with a -17% worst year**: P1. It's simple and led in every window with real data.
- **Smallest drawdowns and steadiest real returns**: the Golden Butterfly, at roughly 1 point a year less. Fits the goals in [[wealth-preservation]] and reduces [[sequence-of-returns-risk]] for someone withdrawing.
- **P6 (the most diversified mix)**: hasn't earned its extra complexity in the years with real data (8.1% vs P1's 8.9% since 2001, with the same worst year).

## Method notes and caveats

- One historical path, annual data, annual rebalancing. No taxes, and no fund fees except in VIPSX and the CTA index (net) and the explicit trend cost assumptions.
- The international series is MSCI EAFE from a secondary compilation, with no monthly data. US small value is a Fama-French paper portfolio with no costs before investable funds existed (early 1990s). Full source notes are in `investing-quant/backtests/data/SOURCES.md`.
- Two data problems were found and fixed along the way. Monthly gold and Treasury returns first came from monthly *averages*, which creates fake month-to-month momentum (see [[auto-correlation-in-markets]]); they now use month-end prices and yields. A missing October 2025 CPI value (never published because of the government shutdown) had silently dropped 2025 from the trend sleeve; the code now errors on gaps.
