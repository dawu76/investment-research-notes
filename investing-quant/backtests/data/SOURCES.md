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
| `cpi` | FRED `CPIAUCNS` | Month-over-month change |

## Known quality issues

- Monthly gold and Treasuries originally came from monthly averages (World Bank gold, FRED `GS10`). Averaging produced fake month-to-month momentum (lag-1 autocorrelation 0.26 for gold, 0.31 for yield changes). Replaced with month-end series on 2026-09-25: autocorrelation is now 0.04 for gold and 0.11 for yield changes. The World Bank file stays in `raw/` only for the `gold_annual_avg` diagnostic.
- Shiller's `ie_data.xls` was fetched but ends at 2023-09, so it was dropped in favor of the Fama-French market factor for monthly US stocks.
- Mixed index definitions: annual US stocks are the S&P 500, monthly US stocks are the CRSP total market.
