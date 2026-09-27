# Data sources

All files fetched 2026-09-25 into `raw/`. `build_data.py` rebuilds both CSVs from them without network access.

## annual_returns.csv (1971-2025; 1971 is a warm-up year for the trend signal)

| Column | Source | Series used | Notes |
|---|---|---|---|
| `us_stocks` | Aswath Damodaran, NYU Stern, `histretSP.xls` (https://pages.stern.nyu.edu/~adamodar/pc/datasets/histretSP.xls) | "Returns by year" sheet, S&P 500 (includes dividends) | Total return, calendar year |
| `intl_stocks` | Novel Investor, "Historical Returns" (https://novelinvestor.com/historical-returns/), saved as `raw/novelinvestor_historical_returns.html` | Asset-class table, "International Stocks" column. The page's source note labels it **MSCI EAFE Index**, total return in USD | Values match known MSCI EAFE gross figures (1985 +56.7%, 1986 +69.9%, 2008 -43.1%). Likely gross dividends, not net of withholding tax. Secondary compilation, not an MSCI download |
| `us_small_value` | Ken French data library, `6_Portfolios_2x3_CSV.zip` (https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/6_Portfolios_2x3_CSV.zip) | "Average Value Weighted Returns -- Annual", `SMALL HiBM` | Paper portfolio (CRSP 202608 build), no fees or trading costs. Investable small-value funds only arrived in the early 1990s |
| `tsy_10y` | Damodaran `histretSP.xls` | "US T. Bond (10-year)" | Modeled total return from yields (coupon plus price change), not a fund's realized return |
| `tbill` | Damodaran `histretSP.xls` | "3-month T.Bill" | Average annual 3-month rate used as the return |
| `gold` | Damodaran `histretSP.xls` | "Gold*" (price sheet cites LBMA from 1970) | **Year-end to year-end** price change. Checked: 1979 +126.5%, 1980 +15.2%, 1981 -32.6%. No yield, storage, or fund costs |
| `cpi` | FRED `CPIAUCNS` (https://fred.stlouisfed.org/graph/fredgraph.csv?id=CPIAUCNS) | CPI-U, not seasonally adjusted | Dec-to-Dec change |
| `cta_index` | Barclay CTA Index, BarclayHedge (now ION Analytics), https://portal.barclayhedge.com/cgi-bin/indices/displayCtaIndex.cgi?indexCat=Barclay-CTA-Indices&indexName=Barclay-CTA-Index, saved as `raw/barclay_cta_index.html` | Annual returns, 1980-2025 (2026 YTD dropped). Net of fees. Equal-weighted average of reporting CTA programs: 15 programs in 1980, 356 in 2025 (`raw/barclay_cta_program_counts.xlsx`). Early years carry survivorship and backfill bias. Not directly investable. www.barclayhedge.com returns 403 to scripts; the portal page above works |
| `aqr_tsmom` | AQR, "Time Series Momentum: Factors, Monthly" (https://www.aqr.com/-/media/AQR/Documents/Insights/Data-Sets/Time-Series-Momentum-Factors-Monthly.xlsx), saved as `raw/aqr_tsmom.xlsx` | `TSMOM` (all assets) column, 1985-01 to 2026-05. The file reports excess returns; T-bill return (`TB3MS` / 1200) is added back each month, then compounded to calendar years. **Gross of fees and trading costs**: a research portfolio, not a fund. `backtest.py` subtracts a flat drag (`--aqr-cost`, default 3%/yr) |
| `tips_fund` | Vanguard Inflation-Protected Securities Fund (VIPSX), Yahoo Finance chart API (https://query1.finance.yahoo.com/v8/finance/chart/VIPSX?interval=1mo&range=max&events=div), saved as `raw/yahoo_VIPSX.json` | Dividend-adjusted month-end closes from 2000-07, compounded to calendar years from 2001. Net of the fund's ~0.2% expense ratio. Checked against published calendar-year returns: 2008 -2.8%, 2013 -8.9%, 2022 -12.0% |
| `tips_10y` | Federal Reserve TIPS yield curve (Gurkaynak, Sack, Wright), https://www.federalreserve.gov/data/yield-curve-tables/feds200805.csv. Cached as `raw/feds200805_tipspy10.csv`, only the `Date` and `TIPSPY10` columns (the full file is 15 MB) | 10y par real yield, last daily value of each month, from 1999-01. Same constant-maturity bond math as `tsy_10y`, with principal indexed to same-month CPI (actual TIPS use a ~3-month CPI lag). Annual from 2000. Tracks VIPSX with 0.99 correlation over 2001-2025; more volatile because a constant 10y maturity is longer than the fund's |
| `tips_synth` | Month-end FRED `DGS10`; Livingston Survey `MedianGrowthRate.xlsx`, sheet `CPI`, column `G_BP_To_12M` (https://www.philadelphiafed.org/surveys-and-data/real-time-data-research/livingston-historical-data), saved as `raw/livingston_median_growth.xlsx`; FRED `EXPINF10YR` (Cleveland Fed 10-year expected inflation, from 1982) | Synthetic real yield = nominal 10y yield minus expected inflation. Before 1982: Livingston median CPI forecast from each June/December survey, carried forward until the next survey (no look-ahead). It's a 12-month forecast standing in for 10-year expectations; it matches the Cleveland Fed within 0.1 point in 1982. From 1982: Cleveland Fed. Same bond math as `tips_10y`. **Weak year by year**: 0.58 correlation with VIPSX over 2001-2025, and it gets 2008-09 backwards (+13.6% vs -2.8% in 2008) because survey expectations miss TIPS liquidity sell-offs. Use pre-1997 values as a rough sketch |
| `gold_annual_avg` | datasets/gold-prices (https://raw.githubusercontent.com/datasets/gold-prices/main/data/monthly.csv), World Bank Pink Sheet from 1960 | Mean of 12 monthly averages, year over year | Diagnostic only, reproduces the first-pass (annual-average) gold timing |

## monthly_returns.csv (1971-01 to 2026-08)

| Column | Source | Transformation / notes |
|---|---|---|
| `us_stocks` | Ken French `F-F_Research_Data_Factors_CSV.zip` (https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_CSV.zip) | `Mkt-RF + RF`. CRSP value-weighted **total US market**, not the S&P 500, so it differs slightly from the annual column |
| `intl_stocks` | none | Blank. No free monthly MSCI EAFE total-return series found |
| `us_small_value` | Ken French 6 portfolios, "Average Value Weighted Returns -- Monthly", `SMALL HiBM` | Paper portfolio |
| `tsy_10y` | FRED `DGS10` daily (https://fred.stlouisfed.org/graph/fredgraph.csv?id=DGS10), fetched 2026-09-25 | Last daily yield of each month. Constant-maturity approximation: buy a 10y par bond at last month-end's yield, reprice at this month-end's yield with 10 - 1/12 years left, plus one month of coupon |
| `tbill` | FRED `TB3MS` (https://fred.stlouisfed.org/graph/fredgraph.csv?id=TB3MS) | Rate / 1200. Monthly average rate, which is fine for a rate earned over the month |
| `gold` | LBMA Gold Price PM, USD, daily (https://prices.lbma.org.uk/json/gold_pm.json), fetched 2026-09-25 | Last PM fix of each month, month over month. Year-end values reproduce Damodaran's annual gold returns (max gap 3.1 points, in 2011) |
| `cpi` | FRED `CPIAUCNS` | Month-over-month change. Blank for 2025-10 and 2025-11: BLS published no October 2025 CPI (government shutdown). Not used by the backtests; annual CPI uses December levels only |
| `aqr_tsmom` | AQR TSMOM (see annual table) | Monthly total return, gross of fees. Blank before 1985-01 and after 2026-05 |
| `tips_fund`, `tips_10y`, `tips_synth` | See annual table | Monthly total returns before compounding. For the CPI accrual in `tips_10y` and `tips_synth`, the missing October 2025 CPI level is filled with the geometric midpoint of September and November |

## Known quality issues

- Monthly gold and Treasuries originally came from monthly averages (World Bank gold, FRED `GS10`). Averaging produced fake month-to-month momentum (lag-1 autocorrelation 0.26 for gold, 0.31 for yield changes). Replaced with month-end series on 2026-09-25: autocorrelation is now 0.04 for gold and 0.11 for yield changes. The World Bank file stays in `raw/` only for the `gold_annual_avg` diagnostic.
- Shiller's `ie_data.xls` was fetched but ends at 2023-09, so it was dropped in favor of the Fama-French market factor for monthly US stocks.
- The missing October 2025 CPI value used to drop that month from `monthly_returns.csv` entirely, which silently removed 2025 from the simulated trend sleeve. Fixed 2026-09-25: a missing CPI value now leaves a blank cell, and `backtest.py` raises an error if a return series has gaps.
- Mixed index definitions: annual US stocks are the S&P 500, monthly US stocks are the CRSP total market.
