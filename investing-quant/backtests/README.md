# Backtests

Annually rebalanced portfolio backtests on a local cache of historical returns. Layer 1 uses assets an investor could hold since 1972 (stocks, Treasuries, T-bills, gold), plus a simulated trend-following sleeve that is labeled as simulated. Layer 2 adds real trend-following records: the Barclay CTA Index (from 1980) and AQR's time-series momentum factor (from 1985). Layer 3 adds TIPS: the VIPSX fund (from 2001), a model based on market real yields (from 2000), and a synthetic series back to 1972.

Caveat on synthetic TIPS: it tracks the actual fund poorly year by year (0.58 correlation over 2001-2025, and it gets 2008-09 backwards), so pre-1997 TIPS results are a rough sketch.

Caveat on the trend sleeve: most of its return comes from the gold leg in 1972-81 (about 30%/yr over T-bills, riding gold's 1970s bull market and then shorting the 1981 crash). From 1982 on, the sleeve beat T-bills by about 2.5%/yr after costs, and by about 0.7%/yr in 2013-25.

## Layout

- `data/raw/`: source files as downloaded
- `data/annual_returns.csv`, `data/monthly_returns.csv`: cleaned return series (decimals)
- `data/SOURCES.md`: where each column comes from, and its caveats
- `build_data.py`: raw files → CSVs
- `backtest.py`: reads the CSVs, prints tables, writes `results/layer<N>_results.md`
- `results/`: saved outputs

## Run

```
uv run --with pandas backtest.py                      # layer 1, reads the cache, no data fetching
uv run --with pandas backtest.py --layer 2            # layer 2: adds Barclay CTA Index and AQR TSMOM
uv run --with pandas backtest.py --layer 3            # layer 3: adds TIPS (VIPSX, modeled, synthetic)
uv run --with pandas backtest.py --summary            # all portfolios over 1972, 1985, and 2001 windows
uv run --with pandas backtest.py --trend-cost 0.01    # change the simulated trend sleeve's annual cost drag
uv run --with pandas backtest.py --layer 2 --aqr-cost 0.04   # change the fee drag on the gross AQR factor
uv run --with pandas backtest.py --start 1990 --end 2025
```

Results go to `results/layer<N>_results.md`, or `results/summary.md` for `--summary`.

uv downloads pandas into its own cache on first run, so system Python is untouched.

To add or change a portfolio, edit the `PORTFOLIOS` dict at the top of `backtest.py`.

## Update the data

- **New year, quick:** append a row to `data/annual_returns.csv` (and monthly rows if wanted). `SOURCES.md` lists where each value comes from.
- **Full refresh:** re-download the files listed in `data/SOURCES.md` into `data/raw/`, then run `uv run --with xlrd --with openpyxl build_data.py`. Bump `LAST_YEAR` in `build_data.py` first.
