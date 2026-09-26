# Layer-1 backtest on the cached CSVs (no network). Investable assets since 1972, plus a labeled simulated trend sleeve.
# Usage: uv run --with pandas backtest.py [--trend-cost 0.02] [--start 1972] [--end 2025] [--out results/layer1_results.md]

import argparse
from pathlib import Path

import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent

# Weights per portfolio. "trend" is the monthly-signal sleeve built in trend_monthly().
PORTFOLIOS = {
    "P1 20 gold / 20 tsy / 60 US": {"gold": 0.20, "tsy_10y": 0.20, "us_stocks": 0.60},
    "P2 20 gold / 20 tsy / 30 US / 30 intl": {"gold": 0.20, "tsy_10y": 0.20, "us_stocks": 0.30, "intl_stocks": 0.30},
    "P3a stocks 100 US / 0 intl": {"gold": 0.20, "tsy_10y": 0.20, "us_stocks": 0.60},
    "P3b stocks 75 / 25": {"gold": 0.20, "tsy_10y": 0.20, "us_stocks": 0.45, "intl_stocks": 0.15},
    "P3c stocks 50 / 50": {"gold": 0.20, "tsy_10y": 0.20, "us_stocks": 0.30, "intl_stocks": 0.30},
    "P3d stocks 25 / 75": {"gold": 0.20, "tsy_10y": 0.20, "us_stocks": 0.15, "intl_stocks": 0.45},
    "P3e stocks 0 US / 100 intl": {"gold": 0.20, "tsy_10y": 0.20, "intl_stocks": 0.60},
    "P4 candidate mix (layer 1)": {
        "us_stocks": 0.30, "intl_stocks": 0.15, "us_small_value": 0.10, "gold": 0.15,
        "tsy_10y": 0.10, "tbill": 0.10, "trend": 0.10,
    },
    "P5 Golden Butterfly (layer 1)": {
        "us_stocks": 0.20, "us_small_value": 0.20, "tsy_10y": 0.20, "tbill": 0.20, "gold": 0.20,
    },
}

HEADLINE = ["P1 20 gold / 20 tsy / 60 US", "P2 20 gold / 20 tsy / 30 US / 30 intl",
            "P4 candidate mix (layer 1)", "P5 Golden Butterfly (layer 1)"]
SPLITS = [k for k in PORTFOLIOS if k.startswith("P3")]
START_YEARS = [1972, 1980, 1990, 2000, 2010]
SENSITIVITY = ["P1 20 gold / 20 tsy / 60 US", "P2 20 gold / 20 tsy / 30 US / 30 intl", "P4 candidate mix (layer 1)"]
TREND_ASSETS_MONTHLY = ["us_stocks", "tsy_10y", "gold"]  # no monthly EAFE in the cache
TREND_ASSETS_ANNUAL = ["us_stocks", "intl_stocks", "tsy_10y", "gold"]
CRISIS_YEARS = [1973, 1974, 2008, 2022]
STANDALONE = ["us_stocks", "intl_stocks", "us_small_value", "tsy_10y", "tbill", "gold", "trend", "trend_annual_signal"]


def load():
    annual = pd.read_csv(HERE / "data" / "annual_returns.csv", index_col="year")
    monthly = pd.read_csv(HERE / "data" / "monthly_returns.csv", index_col="month")
    monthly.index = pd.PeriodIndex(monthly.index, freq="M")
    return annual, monthly


def signal(trailing_excess):
    # Long if trailing excess return over T-bills is positive, else short. Decided at the prior period's close.
    return np.sign(trailing_excess).replace(0, -1).shift(1)


def trend_monthly(monthly, cost):
    logs = np.log1p(monthly)
    trailing = logs[TREND_ASSETS_MONTHLY].rolling(12).sum().sub(logs["tbill"].rolling(12).sum(), axis=0)
    excess = monthly[TREND_ASSETS_MONTHLY].sub(monthly["tbill"], axis=0)
    legs = signal(trailing) * excess
    return (monthly["tbill"] + legs.mean(axis=1, skipna=False) - cost / 12).dropna()


def trend_annual(annual, cost):
    excess = annual[TREND_ASSETS_ANNUAL].sub(annual["tbill"], axis=0)
    legs = signal(excess) * excess
    return (annual["tbill"] + legs.mean(axis=1, skipna=False) - cost).dropna()


def to_annual(monthly_returns):
    full_years = monthly_returns.groupby(monthly_returns.index.year).filter(lambda s: len(s) == 12)
    return (1 + full_years).groupby(full_years.index.year).prod() - 1


def cagr(r):
    return (1 + r).prod() ** (1 / len(r)) - 1


def drawdown(wealth):
    return (wealth / wealth.cummax().clip(lower=1.0) - 1).min()


def rolling_growth(r, n=10):
    return (1 + r).rolling(n).apply(np.prod, raw=True)


def port_returns(weights, frame):
    return frame[list(weights)] @ pd.Series(weights)


def monthly_drawdown(weights, monthly, start, end):
    """Monthly path, rebalanced each January. None if any sleeve lacks monthly data."""
    m = monthly.loc[str(start):str(end), list(weights)]
    if m.isna().any().any():
        return None
    within = (1 + m).groupby(m.index.year).cumprod() @ pd.Series(weights)
    year_growth = within.groupby(within.index.year).last()
    start_wealth = year_growth.cumprod().shift(1, fill_value=1.0)
    return drawdown(within * start_wealth.loc[within.index.year].to_numpy())


def metrics(r, cpi):
    real = (1 + r) / (1 + cpi) - 1
    nominal10, cpi10 = rolling_growth(r), rolling_growth(cpi)
    return {
        "cagr": cagr(r), "real": cagr(real), "vol": r.std(), "mdd": drawdown((1 + r).cumprod()),
        "worst": (r.min(), r.idxmin()), "beat10": (nominal10 > cpi10)[nominal10.notna()].mean(),
    }


def longest_run(flags):
    run_ids = (flags != flags.shift()).cumsum()
    lengths = flags.groupby(run_ids).transform("size").where(flags, 0)
    return int(lengths.max()), lengths.idxmax()


def pct(x, digits=2):
    return f"{x * 100:.{digits}f}%"


def table(headers, rows):
    lines = ["| " + " | ".join(headers) + " |", "|" + "---|" * len(headers)]
    lines += ["| " + " | ".join(str(c) for c in r) + " |" for r in rows]
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--trend-cost", type=float, default=0.02, help="annual drag on the trend sleeve (fees + trading costs)")
    ap.add_argument("--start", type=int, default=1972)
    ap.add_argument("--end", type=int, default=2025)
    ap.add_argument("--out", default="results/layer1_results.md")
    args = ap.parse_args()

    annual, monthly = load()
    monthly["trend"] = trend_monthly(monthly, args.trend_cost)
    annual["trend"] = to_annual(monthly["trend"].dropna())
    annual["trend_annual_signal"] = trend_annual(annual, args.trend_cost)

    a = annual.loc[args.start:args.end]
    first, last = a.index[0], a.index[-1]
    out = [f"# Layer 1 backtest results ({first}-{last}, annual rebalance, nominal USD)", "",
           f"Trend sleeve is **simulated**: monthly 12-month time-series momentum on {', '.join(TREND_ASSETS_MONTHLY)}, "
           f"equal weight, long or short, cost drag {pct(args.trend_cost, 1)}/yr. `trend_annual_signal` is the older "
           "version (prior-year signal, adds intl stocks), kept for comparison. T-bills stand in for TIPS and short "
           "Treasuries; the 10y Treasury stands in for long Treasuries. US small value is a Fama-French paper "
           "portfolio before investable funds existed (early 1990s).", ""]

    rows = []
    for name in HEADLINE + SPLITS:
        r = port_returns(PORTFOLIOS[name], a)
        m = metrics(r, a["cpi"])
        mdd_m = monthly_drawdown(PORTFOLIOS[name], monthly, first, last)
        rows.append([name, pct(m["cagr"]), pct(m["real"]), pct(m["vol"]), pct(m["mdd"], 1),
                     pct(mdd_m, 1) if mdd_m is not None else "n/a",
                     f"{pct(m['worst'][0], 1)} ({m['worst'][1]})", pct(m["beat10"], 0)])
    out += ["## Portfolios", "",
            table(["Portfolio", "CAGR", "Real CAGR", "Vol", "Max DD (annual)", "Max DD (monthly)",
                   "Worst year", "10y windows beating CPI"], rows),
            "", "Monthly max drawdown is only computed where every sleeve has monthly data (there is no monthly EAFE). "
            "Monthly US stocks use the CRSP total market, not the S&P 500. Monthly gold and Treasuries use month-end prices and yields.", ""]

    rows = []
    for col in STANDALONE:
        m = metrics(a[col], a["cpi"])
        rows.append([col, pct(m["cagr"]), pct(m["real"]), pct(m["vol"]), pct(m["mdd"], 1),
                     f"{pct(m['worst'][0], 1)} ({m['worst'][1]})"])
    out += ["## Standalone assets", "", table(["Asset", "CAGR", "Real CAGR", "Vol", "Max DD (annual)", "Worst year"], rows), ""]

    rows = []
    for name in SENSITIVITY:
        cells = [name]
        for s in START_YEARS:
            sub = a.loc[s:]
            r = port_returns(PORTFOLIOS[name], sub)
            cells.append(f"{pct(cagr(r))} / {pct(metrics(r, sub['cpi'])['real'])}")
        rows.append(cells)
    out += ["## Start-date sensitivity (nominal / real CAGR through end year)", "",
            table(["Portfolio"] + [f"from {s}" for s in START_YEARS], rows), ""]

    crisis = a.loc[a.index.intersection(CRISIS_YEARS)]
    out += ["## Trend sleeve in crisis years (simulated)", "",
            table(["Year", "Trend (monthly signal)", "Trend (annual signal)", "US stocks", "10y Treasury", "Gold"],
                  [[y, pct(r.trend, 1), pct(r.trend_annual_signal, 1), pct(r.us_stocks, 1), pct(r.tsy_10y, 1),
                    pct(r.gold, 1)] for y, r in crisis.iterrows()]), ""]

    diffs = (rolling_growth(a["us_stocks"]) ** 0.1 - rolling_growth(a["intl_stocks"]) ** 0.1).dropna()
    us_lead = diffs > 0
    us_run, us_start = longest_run(us_lead)
    intl_run, intl_start = longest_run(~us_lead)
    out += ["## Rolling 10-year CAGR: US minus international (EAFE)", "",
            f"- Windows: {len(diffs)} (ending {diffs.index[0]}-{diffs.index[-1]}). "
            f"US led in {us_lead.sum()}, international led in {(~us_lead).sum()}.",
            f"- Longest US-led stretch: {us_run} consecutive windows (ending {us_start}-{us_start + us_run - 1}).",
            f"- Longest international-led stretch: {intl_run} consecutive windows "
            f"(ending {intl_start}-{intl_start + intl_run - 1}).",
            "", table(["10y window", "US minus intl"], [[f"{e - 9}-{e}", pct(d, 1)] for e, d in diffs.items()]), ""]

    rows = []
    for name in SPLITS:
        w = PORTFOLIOS[name]
        cells = [name]
        for gold_col in ("gold", "gold_annual_avg"):
            view = a.assign(gold=a[gold_col])
            port = cagr(port_returns(w, view))
            weighted = sum(wt * cagr(view[col]) for col, wt in w.items())
            cells += [pct(port), pct(port - weighted)]
        rows.append(cells)
    out += ["## Gold timing check: year-end vs annual-average gold", "",
            "Rebalancing bonus = portfolio CAGR minus the weighted average of the sleeves' own CAGRs.", "",
            table(["Split", "CAGR (year-end gold)", "Bonus (year-end)", "CAGR (avg gold)", "Bonus (avg gold)"], rows), ""]

    text = "\n".join(out)
    print(text)
    path = HERE / args.out
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text + "\n")


if __name__ == "__main__":
    main()
