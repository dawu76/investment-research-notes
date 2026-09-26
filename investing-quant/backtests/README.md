# Backtests

Annually rebalanced portfolio backtests on a local cache of historical returns. Layer 1 uses assets an investor could hold since 1972 (stocks, Treasuries, T-bills, gold), plus a simulated trend-following sleeve that is labeled as simulated.

Caveat on the trend sleeve: most of its return comes from the gold leg in 1972-81 (about 30%/yr over T-bills, riding gold's 1970s bull market and then shorting the 1981 crash). From 1982 on, the sleeve beat T-bills by about 2.6%/yr after costs, and by about 0.5%/yr in 2013-25.

## Layout

- `data/raw/`: source files as downloaded
- `data/annual_returns.csv`, `data/monthly_returns.csv`: cleaned return series (decimals)
- `data/SOURCES.md`: where each column comes from, and its caveats
- `build_data.py`: raw files → CSVs
- `backtest.py`: reads the CSVs, prints tables, writes `results/layer1_results.md`
- `results/`: saved outputs

## Run

```
uv run --with pandas backtest.py                      # reads the cache, no data fetching
uv run --with pandas backtest.py --trend-cost 0.01    # change the trend sleeve's annual cost drag
uv run --with pandas backtest.py --start 1980 --end 2025
```

uv downloads pandas into its own cache on first run, so system Python is untouched.

To add or change a portfolio, edit the `PORTFOLIOS` dict at the top of `backtest.py`.

## Update the data

- **New year, quick:** append a row to `data/annual_returns.csv` (and monthly rows if wanted). `SOURCES.md` lists where each value comes from.
- **Full refresh:** re-download the files listed in `data/SOURCES.md` into `data/raw/`, then run `uv run --with xlrd build_data.py`. Bump `LAST_YEAR` in `build_data.py` first.
