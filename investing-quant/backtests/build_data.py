# Run from this directory:  uv run --with xlrd build_data.py
"""Build data/annual_returns.csv and data/monthly_returns.csv from data/raw/ (no network access)."""

import csv
import html
import json
import io
import re
import zipfile
from pathlib import Path

import xlrd

HERE = Path(__file__).resolve().parent
RAW = HERE / "data" / "raw"
OUT = HERE / "data"

FIRST_YEAR = 1971
LAST_YEAR = 2025
FIRST_MONTH = "1971-01"

COLUMNS = ["us_stocks", "intl_stocks", "us_small_value", "tsy_10y", "tbill", "gold", "cpi"]


def damodaran_annual():
    book = xlrd.open_workbook(str(RAW / "histretSP.xls"))
    sheet = book.sheet_by_name("Returns by year")
    header_row = next(r for r in range(sheet.nrows) if sheet.cell_value(r, 0) == "Year")
    headers = [str(sheet.cell_value(header_row, c)) for c in range(sheet.ncols)]

    def col(prefix):
        return next(i for i, h in enumerate(headers) if h.startswith(prefix))

    idx = {
        "us_stocks": col("S&P 500"),
        "tbill": col("3-month T.Bill"),
        "tsy_10y": col("US T. Bond"),
        "gold": col("Gold"),
    }
    out = {}
    for r in range(header_row + 1, sheet.nrows):
        year = sheet.cell_value(r, 0)
        if not isinstance(year, float):
            break
        out[int(year)] = {k: float(sheet.cell_value(r, c)) for k, c in idx.items()}
    return out


def novelinvestor_eafe():
    text = (RAW / "novelinvestor_historical_returns.html").read_text(encoding="utf-8", errors="replace")
    table = re.findall(r"<table.*?</table>", text, re.S)[0]
    rows = re.findall(r"<tr.*?</tr>", table, re.S)

    def cells(row):
        return [html.unescape(re.sub(r"<[^>]+>", "", c)).strip() for c in re.findall(r"<t[hd][^>]*>(.*?)</t[hd]>", row, re.S)]

    header = cells(rows[0])
    col = header.index("International Stocks")
    out = {}
    for row in rows[1:]:
        c = cells(row)
        if c[0].isdigit() and c[col]:
            out[int(c[0])] = float(c[col].rstrip("%")) / 100
    return out


def french_sections(zip_name):
    with zipfile.ZipFile(RAW / zip_name) as z:
        text = z.read(z.namelist()[0]).decode("latin-1")
    sections = {}
    current = None
    for line in text.splitlines():
        stripped = line.strip()
        first = stripped.split(",")[0].strip()
        if first.isdigit():
            if current is not None:
                sections[current].append([p.strip() for p in stripped.split(",")])
        elif stripped and not stripped.startswith(","):
            current = stripped
            sections[current] = []
        elif stripped.startswith(","):
            if current is None:
                current = "header"
                sections[current] = []
            sections[current + "::cols"] = [p.strip() for p in stripped.split(",")]
    return sections


def french_small_value():
    sec = french_sections("6_Portfolios_2x3_CSV.zip")
    cols = sec["Average Value Weighted Returns -- Monthly::cols"]
    i = cols.index("SMALL HiBM")
    monthly = {f"{r[0][:4]}-{r[0][4:]}": float(r[i]) / 100 for r in sec["Average Value Weighted Returns -- Monthly"]}
    annual = {int(r[0]): float(r[i]) / 100 for r in sec["Average Value Weighted Returns -- Annual"]}
    return annual, monthly


def french_market_monthly():
    sec = french_sections("F-F_Research_Data_Factors_CSV.zip")
    key = next(k for k in sec if not k.endswith("::cols") and sec[k] and len(sec[k][0][0]) == 6)
    cols = sec[key + "::cols"]
    mkt, rf = cols.index("Mkt-RF"), cols.index("RF")
    return {f"{r[0][:4]}-{r[0][4:]}": (float(r[mkt]) + float(r[rf])) / 100 for r in sec[key]}


def fred(series):
    with open(RAW / f"fred_{series}.csv") as f:
        return {row["observation_date"][:7]: float(row[series]) for row in csv.DictReader(f) if row[series] not in ("", ".")}


def fred_daily(series):
    with open(RAW / f"fred_{series}.csv") as f:
        return {row["observation_date"]: float(row[series]) for row in csv.DictReader(f) if row[series] not in ("", ".")}


def month_end(daily):
    """Last observation in each month. Keys go from YYYY-MM-DD to YYYY-MM."""
    return {day[:7]: daily[day] for day in sorted(daily)}


def lbma_gold_daily():
    rows = json.loads((RAW / "lbma_gold_pm.json").read_text())
    return {r["d"]: r["v"][0] for r in rows if r["v"][0]}


def gold_monthly_avg():
    with open(RAW / "gold_monthly.csv") as f:
        return {row["Date"][:7]: float(row["Price"]) for row in csv.DictReader(f)}


def bond_price(coupon_pct, yield_pct, years):
    """Price per 100 face of a semiannual-coupon bond."""
    y = yield_pct / 200
    n = years * 2
    c = coupon_pct / 2
    if y == 0:
        return c * n + 100
    return c * (1 - (1 + y) ** -n) / y + 100 * (1 + y) ** -n


def tsy10_monthly_tr(gs10):
    """Constant-maturity 10y total return: buy a par bond at last month's yield, reprice a month later at this month's yield."""
    months = sorted(gs10)
    out = {}
    for prev, cur in zip(months, months[1:]):
        y0, y1 = gs10[prev], gs10[cur]
        price = bond_price(y0, y1, 10 - 1 / 12)
        out[cur] = (price + y0 / 12) / 100 - 1
    return out


def pct_change(levels):
    months = sorted(levels)
    return {cur: levels[cur] / levels[prev] - 1 for prev, cur in zip(months, months[1:])}


def main():
    dam = damodaran_annual()
    eafe = novelinvestor_eafe()
    sv_annual, sv_monthly = french_small_value()
    cpi_levels = fred("CPIAUCNS")
    gold_levels = gold_monthly_avg()

    annual_rows = []
    for year in range(FIRST_YEAR, LAST_YEAR + 1):
        cpi = cpi_levels[f"{year}-12"] / cpi_levels[f"{year - 1}-12"] - 1
        gold_avg = sum(gold_levels[f"{year}-{m:02d}"] for m in range(1, 13)) / 12
        gold_avg_prev = sum(gold_levels[f"{year - 1}-{m:02d}"] for m in range(1, 13)) / 12
        annual_rows.append({
            "year": year,
            "us_stocks": dam[year]["us_stocks"],
            "intl_stocks": eafe[year],
            "us_small_value": sv_annual[year],
            "tsy_10y": dam[year]["tsy_10y"],
            "tbill": dam[year]["tbill"],
            "gold": dam[year]["gold"],
            "cpi": cpi,
            "gold_annual_avg": gold_avg / gold_avg_prev - 1,
        })

    with open(OUT / "annual_returns.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["year"] + COLUMNS + ["gold_annual_avg"])
        w.writeheader()
        for row in annual_rows:
            w.writerow({k: (f"{v:.6f}" if isinstance(v, float) else v) for k, v in row.items()})

    mkt = french_market_monthly()
    tsy = tsy10_monthly_tr(month_end(fred_daily("DGS10")))
    tb3 = fred("TB3MS")
    cpi_m = pct_change(cpi_levels)
    gold_m = pct_change(month_end(lbma_gold_daily()))
    months = sorted(m for m in mkt if m >= FIRST_MONTH and all(m in s for s in (tsy, tb3, cpi_m, gold_m, sv_monthly)))

    with open(OUT / "monthly_returns.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["month"] + COLUMNS)
        for m in months:
            w.writerow([m, f"{mkt[m]:.6f}", "", f"{sv_monthly[m]:.6f}", f"{tsy[m]:.6f}",
                        f"{tb3[m] / 1200:.6f}", f"{gold_m[m]:.6f}", f"{cpi_m[m]:.6f}"])

    print(f"annual: {len(annual_rows)} rows {FIRST_YEAR}-{LAST_YEAR}; monthly: {len(months)} rows {months[0]}..{months[-1]}")


if __name__ == "__main__":
    main()
