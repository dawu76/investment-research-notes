# Portfolio backtests on the cached CSVs (no network).
# Layer 1: investable assets since 1972, plus a labeled simulated trend sleeve.
# Layer 2: adds real trend-following records (Barclay CTA Index from 1980, AQR TSMOM from 1985).
# Layer 3: adds TIPS (actual fund from 2001, modeled from market real yields from 2000, synthetic from 1972).
# Usage: uv run --with pandas backtest.py [--layer 1|2|3] [--trend-cost 0.02] [--aqr-cost 0.03] [--start YEAR] [--end 2025]

import argparse
from pathlib import Path

import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent

# P4 without its 10% trend-following sleeve. Layer 2 swaps in different trend sources.
P4_CORE = {"us_stocks": 0.30, "intl_stocks": 0.15, "us_small_value": 0.10, "gold": 0.15, "tsy_10y": 0.10, "tbill": 0.10}
# The full candidate mix: P4_CORE with TIPS in the T-bill slot, plus a 10% trend sleeve (layer 3).
P6_CORE = {k: v for k, v in P4_CORE.items() if k != "tbill"}

# Weights per portfolio. "trend" is the monthly-signal sleeve built in trend_monthly().
PORTFOLIOS = {
    "P1 20 gold / 20 tsy / 60 US": {"gold": 0.20, "tsy_10y": 0.20, "us_stocks": 0.60},
    "P2 20 gold / 20 tsy / 30 US / 30 intl": {"gold": 0.20, "tsy_10y": 0.20, "us_stocks": 0.30, "intl_stocks": 0.30},
    "P3a stocks 100 US / 0 intl": {"gold": 0.20, "tsy_10y": 0.20, "us_stocks": 0.60},
    "P3b stocks 75 / 25": {"gold": 0.20, "tsy_10y": 0.20, "us_stocks": 0.45, "intl_stocks": 0.15},
    "P3c stocks 50 / 50": {"gold": 0.20, "tsy_10y": 0.20, "us_stocks": 0.30, "intl_stocks": 0.30},
    "P3d stocks 25 / 75": {"gold": 0.20, "tsy_10y": 0.20, "us_stocks": 0.15, "intl_stocks": 0.45},
    "P3e stocks 0 US / 100 intl": {"gold": 0.20, "tsy_10y": 0.20, "intl_stocks": 0.60},
    "P4 candidate mix (layer 1)": {**P4_CORE, "trend": 0.10},
    "P5 Golden Butterfly (layer 1)": {
        "us_stocks": 0.20, "us_small_value": 0.20, "tsy_10y": 0.20, "tbill": 0.20, "gold": 0.20,
    },
    "P4 no trend (extra 10% T-bills)": {**P4_CORE, "tbill": 0.20},
    "P4 + simulated trend": {**P4_CORE, "trend": 0.10},
    "P4 + Barclay CTA Index": {**P4_CORE, "cta_index": 0.10},
    "P4 + AQR TSMOM (net)": {**P4_CORE, "aqr_net": 0.10},
    "P1 with TIPS (synthetic)": {"gold": 0.20, "tips_synth": 0.20, "us_stocks": 0.60},
    "P1 with TIPS (VIPSX)": {"gold": 0.20, "tips_fund": 0.20, "us_stocks": 0.60},
    "P6 full mix (synthetic TIPS, simulated trend)": {**P6_CORE, "tips_synth": 0.10, "trend": 0.10},
    "P6 full mix (VIPSX, Barclay CTA)": {**P6_CORE, "tips_fund": 0.10, "cta_index": 0.10},
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

DEFAULT_START = {1: 1972, 2: 1980, 3: 1972}
L3_FULL = ["P1 20 gold / 20 tsy / 60 US", "P1 with TIPS (synthetic)", "P4 candidate mix (layer 1)",
           "P6 full mix (synthetic TIPS, simulated trend)", "P5 Golden Butterfly (layer 1)"]
L3_FUND_ERA = ["P1 20 gold / 20 tsy / 60 US", "P1 with TIPS (VIPSX)", "P4 + Barclay CTA Index",
               "P6 full mix (VIPSX, Barclay CTA)", "P5 Golden Butterfly (layer 1)"]
L3_TIPS = ["tips_fund", "tips_10y", "tips_synth", "tsy_10y"]
L3_VALIDATION_YEARS = [2002, 2008, 2009, 2013, 2021, 2022]
L3_INFLATION_THRESHOLD = 0.06

SUMMARY_PORTFOLIOS = [
    "P1 20 gold / 20 tsy / 60 US", "P3b stocks 75 / 25", "P2 20 gold / 20 tsy / 30 US / 30 intl",
    "P3d stocks 25 / 75", "P3e stocks 0 US / 100 intl", "P1 with TIPS (synthetic)", "P1 with TIPS (VIPSX)",
    "P4 no trend (extra 10% T-bills)", "P4 candidate mix (layer 1)", "P4 + Barclay CTA Index", "P4 + AQR TSMOM (net)",
    "P6 full mix (synthetic TIPS, simulated trend)", "P6 full mix (VIPSX, Barclay CTA)", "P5 Golden Butterfly (layer 1)",
]
SUMMARY_WINDOWS = [1972, 1985, 2001]
SUMMARY_STRESS_YEARS = [1973, 1974, 1981, 2002, 2008, 2022]
L2_TREND = ["trend", "cta_index", "aqr_net"]
L2_PORTFOLIOS = ["P1 20 gold / 20 tsy / 60 US", "P5 Golden Butterfly (layer 1)", "P4 no trend (extra 10% T-bills)",
                 "P4 + simulated trend", "P4 + Barclay CTA Index", "P4 + AQR TSMOM (net)"]
L2_START_YEARS = [1980, 1985, 1990, 2000, 2010]
L2_CRISIS_YEARS = [1987, 2001, 2002, 2008, 2020, 2022]
L2_DECADES = [(1980, 1989), (1990, 1999), (2000, 2009), (2010, 2019), (2020, 2025)]


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
    if r.isna().any():
        raise ValueError(f"missing returns in {r.name!r} for {list(r.index[r.isna()])}")
    return (1 + r).prod() ** (1 / len(r)) - 1


def drawdown(wealth):
    return (wealth / wealth.cummax().clip(lower=1.0) - 1).min()


def rolling_growth(r, n=10):
    return (1 + r).rolling(n).apply(np.prod, raw=True)


def port_returns(weights, frame):
    return frame[list(weights)] @ pd.Series(weights)


def monthly_drawdown(weights, monthly, start, end):
    """Monthly path, rebalanced each January. None if any sleeve lacks monthly data."""
    if not set(weights) <= set(monthly.columns):
        return None
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


def excess_cagr(r, tbill):
    """Annualized geometric return over T-bills."""
    return ((1 + r) / (1 + tbill)).prod() ** (1 / len(r)) - 1


def portfolio_table(names, a, monthly):
    first, last = a.index[0], a.index[-1]
    rows = []
    for name in names:
        r = port_returns(PORTFOLIOS[name], a)
        m = metrics(r, a["cpi"])
        mdd_m = monthly_drawdown(PORTFOLIOS[name], monthly, first, last)
        rows.append([name, pct(m["cagr"]), pct(m["real"]), pct(m["vol"]), pct(m["mdd"], 1),
                     pct(mdd_m, 1) if mdd_m is not None else "n/a",
                     f"{pct(m['worst'][0], 1)} ({m['worst'][1]})", pct(m["beat10"], 0)])
    return table(["Portfolio", "CAGR", "Real CAGR", "Vol", "Max DD (annual)", "Max DD (monthly)",
                  "Worst year", "10y windows beating CPI"], rows)


def layer1_report(a, monthly, args):
    first, last = a.index[0], a.index[-1]
    out = [f"# Layer 1 backtest results ({first}-{last}, annual rebalance, nominal USD)", "",
           f"Trend sleeve is **simulated**: monthly 12-month time-series momentum on {', '.join(TREND_ASSETS_MONTHLY)}, "
           f"equal weight, long or short, cost drag {pct(args.trend_cost, 1)}/yr. `trend_annual_signal` is the older "
           "version (prior-year signal, adds intl stocks), kept for comparison. T-bills stand in for TIPS and short "
           "Treasuries; the 10y Treasury stands in for long Treasuries. US small value is a Fama-French paper "
           "portfolio before investable funds existed (early 1990s).", ""]

    out += ["## Portfolios", "", portfolio_table(HEADLINE + SPLITS, a, monthly),
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

    return out


def layer2_report(a, monthly, args):
    first, last = a.index[0], a.index[-1]
    common = a.loc[a["aqr_net"].first_valid_index():]
    out = [f"# Layer 2 backtest results ({first}-{last}, annual rebalance, nominal USD)", "",
           "Adds real-world trend-following records next to the simulated sleeve from layer 1:", "",
           "- `cta_index`: Barclay CTA Index, net of fees, from 1980. Equal-weighted average of the CTA programs "
           "reporting to BarclayHedge (15 programs in 1980, 356 in 2025), so the early years reflect a small group of "
           "managers that survived long enough to report. You could not buy the index itself.",
           f"- `aqr_net`: AQR's time-series momentum factor from 1985, a research portfolio across roughly 60 futures "
           f"markets, reported gross of fees. Shown after a flat {pct(args.aqr_cost, 1)}/yr drag.",
           f"- `trend`: the layer-1 simulated sleeve (US stocks, 10y Treasury, gold; monthly signal; "
           f"{pct(args.trend_cost, 1)}/yr drag).", ""]

    rows = []
    for col in L2_TREND + ["tbill", "us_stocks"]:
        r = common[col]
        m = metrics(r, common["cpi"])
        rows.append([col, pct(m["cagr"]), pct(excess_cagr(r, common["tbill"])), pct(m["vol"]), pct(m["mdd"], 1),
                     f"{pct(m['worst'][0], 1)} ({m['worst'][1]})"])
    corr = common[L2_TREND + ["us_stocks", "tsy_10y", "gold"]].corr()
    out += [f"## Trend sources compared ({common.index[0]}-{last}, the years all three cover)", "",
            table(["Series", "CAGR", "Excess over T-bills", "Vol", "Max DD (annual)", "Worst year"], rows), "",
            "Correlation of annual returns:", "",
            table([""] + list(corr.columns), [[i] + [f"{v:.2f}" for v in row] for i, row in corr.iterrows()]), ""]

    rows = []
    for col in L2_TREND:
        cells = [col]
        for s, e in L2_DECADES:
            sub = a.loc[s:e]
            cells.append(pct(excess_cagr(sub[col], sub["tbill"]), 1) if sub[col].notna().all() else "n/a")
        rows.append(cells)
    out += ["## Excess return over T-bills by decade (annualized)", "",
            table(["Series"] + [f"{s}-{e}" for s, e in L2_DECADES], rows), ""]

    crisis = a.loc[a.index.intersection(L2_CRISIS_YEARS)]
    fmt = lambda v: "n/a" if pd.isna(v) else pct(v, 1)
    out += ["## Crisis years", "",
            table(["Year", "Simulated trend", "Barclay CTA", "AQR TSMOM (net)", "US stocks", "10y Treasury"],
                  [[y, fmt(r.trend), fmt(r.cta_index), fmt(r.aqr_net), fmt(r.us_stocks), fmt(r.tsy_10y)]
                   for y, r in crisis.iterrows()]), ""]

    full = [n for n in L2_PORTFOLIOS if a[list(PORTFOLIOS[n])].notna().all().all()]
    out += [f"## Portfolios ({first}-{last})", "", portfolio_table(full, a, monthly), "",
            f"## Portfolios ({common.index[0]}-{last}, adds the AQR version)", "",
            portfolio_table(L2_PORTFOLIOS, common, monthly), "",
            "The P4 variants differ only in their 10% trend sleeve; \"P4 no trend\" puts that 10% in T-bills.", ""]

    rows = []
    for name in L2_PORTFOLIOS[2:]:
        cells = [name]
        for s in L2_START_YEARS:
            sub = a.loc[s:]
            r = port_returns(PORTFOLIOS[name], sub)
            cells.append("n/a" if r.isna().any() else f"{pct(cagr(r))} / {pct(metrics(r, sub['cpi'])['real'])}")
        rows.append(cells)
    out += ["## Start-date sensitivity (nominal / real CAGR through end year)", "",
            table(["Portfolio"] + [f"from {s}" for s in L2_START_YEARS], rows), ""]
    return out


def layer3_report(a, monthly, args):
    first, last = a.index[0], a.index[-1]
    fund = a.loc[a["tips_fund"].first_valid_index():]
    na_pct = lambda v: "n/a" if pd.isna(v) else pct(v, 1)
    out = [f"# Layer 3 backtest results ({first}-{last}, annual rebalance, nominal USD)", "",
           "Adds TIPS, in three versions:", "",
           "- `tips_fund`: Vanguard Inflation-Protected Securities Fund (VIPSX), actual total returns, from 2001.",
           "- `tips_10y`: modeled 10y constant-maturity TIPS from the Fed's market real yields (Gurkaynak-Sack-Wright "
           "TIPS curve), from 2000.",
           "- `tips_synth`: synthetic 10y TIPS from 1972. Real yield = month-end nominal 10y yield minus expected "
           "inflation (Livingston Survey 12-month forecast before 1982, Cleveland Fed 10-year expectation after). "
           "US TIPS did not exist before 1997.", ""]

    rows = []
    for col in L3_TIPS:
        r = fund[col]
        rows.append([col, pct(cagr(r)), pct(r.std()), f"{r.corr(fund['tips_fund']):.2f}",
                     "" if col == "tips_fund" else pct((r - fund["tips_fund"]).std(), 1)])
    out += [f"## How each version tracks the actual fund ({fund.index[0]}-{last})", "",
            table(["Series", "CAGR", "Vol", "Correlation with VIPSX", "Tracking error vs VIPSX"], rows), "",
            table(["Year"] + L3_TIPS, [[y] + [pct(fund.loc[y, c], 1) for c in L3_TIPS]
                                       for y in L3_VALIDATION_YEARS if y in fund.index]), ""]

    hot = a[a["cpi"] > L3_INFLATION_THRESHOLD]
    assets = ["cpi", "tbill", "tsy_10y", "tips_synth", "tips_10y", "tips_fund"]
    ports = L3_FULL[:4]
    port_ret = {n: port_returns(PORTFOLIOS[n], hot) for n in ports}

    def real_summary(r):
        return "n/a" if r.isna().any() else pct(cagr((1 + r) / (1 + hot["cpi"]) - 1), 1)

    out += [f"## Inflation years (CPI above {pct(L3_INFLATION_THRESHOLD, 0)})", "",
            table(["Year"] + assets, [[y] + [na_pct(r[c]) for c in assets] for y, r in hot.iterrows()]
                  + [["Real, annualized", ""] + [real_summary(hot[c]) for c in assets[1:]]]), "",
            "Portfolio returns in those years:", "",
            table(["Year"] + ports, [[y] + [na_pct(port_ret[n][y]) for n in ports] for y in hot.index]
                  + [["Real, annualized"] + [real_summary(port_ret[n]) for n in ports]]), ""]

    out += [f"## Portfolios ({first}-{last}, synthetic TIPS)", "", portfolio_table(L3_FULL, a, monthly), "",
            f"## Portfolios ({fund.index[0]}-{last}, actual TIPS fund and Barclay CTA Index)", "",
            portfolio_table(L3_FUND_ERA, fund, monthly), "",
            "\"P1 with TIPS\" swaps P1's 20% nominal 10y Treasury for TIPS. P6 is the full candidate mix: 30 US / "
            "15 intl / 10 small value / 15 gold / 10 nominal 10y Treasury / 10 TIPS / 10 trend. P4 is the same mix "
            "with T-bills in the TIPS slot.", ""]
    return out


def summary_report(a, monthly, args):
    last = a.index[-1]
    out = [f"# All portfolios compared (annual rebalance, nominal USD, through {last})", "",
           "Each window lists every portfolio with data for the whole window. Portfolios that need later-starting "
           "data (Barclay CTA 1980, AQR 1985, VIPSX 2001) only appear in later windows. Synthetic TIPS and the "
           "simulated trend sleeve are estimates; see the layer reports and data/SOURCES.md. \"P4 candidate mix "
           "(layer 1)\" is P4 with the simulated trend sleeve.", ""]
    for start in SUMMARY_WINDOWS:
        w = a.loc[start:]
        tbill = cagr(w["tbill"])
        rows = []
        for name in SUMMARY_PORTFOLIOS:
            weights = PORTFOLIOS[name]
            if w[list(weights)].isna().any().any():
                continue
            m = metrics(port_returns(weights, w), w["cpi"])
            rows.append([name, pct(m["cagr"]), pct(m["real"]), pct(m["vol"]), f"{(m['cagr'] - tbill) / m['vol']:.2f}",
                         pct(m["mdd"], 1), f"{pct(m['worst'][0], 1)} ({m['worst'][1]})"])
        out += [f"## {start}-{last}", "",
                table(["Portfolio", "CAGR", "Real CAGR", "Vol", "Excess return / vol", "Max DD (annual)", "Worst year"],
                      rows), ""]

    hot = a[a["cpi"] > L3_INFLATION_THRESHOLD]
    rows = []
    for name in SUMMARY_PORTFOLIOS:
        r = port_returns(PORTFOLIOS[name], a)
        h = r[hot.index]
        rows.append([name] + ["n/a" if pd.isna(r[y]) else pct(r[y], 1) for y in SUMMARY_STRESS_YEARS]
                    + ["n/a" if h.isna().any() else pct(cagr((1 + h) / (1 + hot["cpi"]) - 1), 1)])
    out += ["## Stress years", "",
            f"Last column: annualized real return across the {len(hot)} years with CPI above "
            f"{pct(L3_INFLATION_THRESHOLD, 0)}.", "",
            table(["Portfolio"] + [str(y) for y in SUMMARY_STRESS_YEARS] + ["Real, high-inflation years"], rows), ""]
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--layer", type=int, choices=[1, 2, 3], default=1)
    ap.add_argument("--summary", action="store_true", help="compare all portfolios across common windows")
    ap.add_argument("--trend-cost", type=float, default=0.02, help="annual drag on the simulated trend sleeve")
    ap.add_argument("--aqr-cost", type=float, default=0.03, help="annual fee drag applied to the gross AQR factor")
    ap.add_argument("--start", type=int, help="first year (default 1972 for layers 1 and 3, 1980 for layer 2)")
    ap.add_argument("--end", type=int, default=2025)
    ap.add_argument("--out", help="output path (default results/layer<N>_results.md)")
    args = ap.parse_args()

    annual, monthly = load()
    monthly["trend"] = trend_monthly(monthly, args.trend_cost)
    annual["trend"] = to_annual(monthly["trend"].dropna())
    annual["trend_annual_signal"] = trend_annual(annual, args.trend_cost)
    annual["aqr_net"] = annual["aqr_tsmom"] - args.aqr_cost

    a = annual.loc[args.start or DEFAULT_START[args.layer]:args.end]
    if args.summary:
        report, default_out = summary_report, "results/summary.md"
    else:
        report = {1: layer1_report, 2: layer2_report, 3: layer3_report}[args.layer]
        default_out = f"results/layer{args.layer}_results.md"
    text = "\n".join(report(a, monthly, args))
    print(text)
    path = HERE / (args.out or default_out)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text + "\n")


if __name__ == "__main__":
    main()
