# Layer 1 backtest results (1972-2025, annual rebalance, nominal USD)

Trend sleeve is **simulated**: monthly 12-month time-series momentum on us_stocks, tsy_10y, gold, equal weight, long or short, cost drag 2.0%/yr. `trend_annual_signal` is the older version (prior-year signal, adds intl stocks), kept for comparison. T-bills stand in for TIPS and short Treasuries; the 10y Treasury stands in for long Treasuries. US small value is a Fama-French paper portfolio before investable funds existed (early 1990s).

## Portfolios

| Portfolio | CAGR | Real CAGR | Vol | Max DD (annual) | Max DD (monthly) | Worst year | 10y windows beating CPI |
|---|---|---|---|---|---|---|---|
| P1 20 gold / 20 tsy / 60 US | 10.54% | 6.40% | 10.96% | -17.0% | -25.9% | -17.0% (2008) | 100% |
| P2 20 gold / 20 tsy / 30 US / 30 intl | 10.16% | 6.02% | 11.60% | -19.0% | n/a | -19.0% (2008) | 100% |
| P4 candidate mix (layer 1) | 9.97% | 5.90% | 9.85% | -17.0% | n/a | -17.0% (2008) | 100% |
| P5 Golden Butterfly (layer 1) | 10.03% | 5.90% | 8.38% | -8.9% | -17.5% | -8.9% (2008) | 100% |
| P3a stocks 100 US / 0 intl | 10.54% | 6.40% | 10.96% | -17.0% | -25.9% | -17.0% (2008) | 100% |
| P3b stocks 75 / 25 | 10.37% | 6.23% | 11.03% | -18.0% | n/a | -18.0% (2008) | 100% |
| P3c stocks 50 / 50 | 10.16% | 6.02% | 11.60% | -19.0% | n/a | -19.0% (2008) | 100% |
| P3d stocks 25 / 75 | 9.89% | 5.77% | 12.60% | -20.0% | n/a | -20.0% (2008) | 100% |
| P3e stocks 0 US / 100 intl | 9.59% | 5.48% | 13.95% | -21.0% | n/a | -21.0% (2008) | 100% |

Monthly max drawdown is only computed where every sleeve has monthly data (there is no monthly EAFE). Monthly US stocks use the CRSP total market, not the S&P 500. Monthly gold and Treasuries use month-end prices and yields.

## Standalone assets

| Asset | CAGR | Real CAGR | Vol | Max DD (annual) | Worst year |
|---|---|---|---|---|---|
| us_stocks | 11.06% | 6.89% | 17.04% | -37.4% | -36.6% (2008) |
| intl_stocks | 9.36% | 5.26% | 21.00% | -43.1% | -43.1% (2008) |
| us_small_value | 14.48% | 10.19% | 22.23% | -42.9% | -33.8% (2008) |
| tsy_10y | 5.90% | 1.93% | 9.79% | -21.5% | -17.8% (2022) |
| tbill | 4.45% | 0.53% | 3.39% | 0.0% | 0.0% (2014) |
| gold | 8.89% | 4.81% | 27.31% | -53.5% | -32.6% (1981) |
| trend | 8.17% | 4.16% | 11.39% | -18.7% | -11.8% (2016) |
| trend_annual_signal | 4.04% | 0.13% | 12.33% | -32.8% | -18.9% (1975) |

## Start-date sensitivity (nominal / real CAGR through end year)

| Portfolio | from 1972 | from 1980 | from 1990 | from 2000 | from 2010 |
|---|---|---|---|---|---|
| P1 20 gold / 20 tsy / 60 US | 10.54% / 6.40% | 10.11% / 6.71% | 9.40% / 6.57% | 8.43% / 5.73% | 11.09% / 8.31% |
| P2 20 gold / 20 tsy / 30 US / 30 intl | 10.16% / 6.02% | 9.36% / 5.98% | 7.96% / 5.16% | 7.60% / 4.92% | 9.09% / 6.35% |
| P4 candidate mix (layer 1) | 9.97% / 5.90% | 9.08% / 5.78% | 7.68% / 4.97% | 6.73% / 4.18% | 7.44% / 4.92% |

## Trend sleeve in crisis years (simulated)

| Year | Trend (monthly signal) | Trend (annual signal) | US stocks | 10y Treasury | Gold |
|---|---|---|---|---|---|
| 1973 | 31.3% | 11.7% | -14.3% | 3.7% | 73.0% |
| 1974 | 41.6% | 37.8% | -25.9% | 2.0% | 66.1% |
| 2008 | 10.4% | -15.8% | -36.6% | 20.1% | 4.3% |
| 2022 | -1.8% | -3.6% | -18.0% | -17.8% | 0.5% |

## Rolling 10-year CAGR: US minus international (EAFE)

- Windows: 45 (ending 1981-2025). US led in 24, international led in 21.
- Longest US-led stretch: 12 consecutive windows (ending 1995-2006).
- Longest international-led stretch: 14 consecutive windows (ending 1981-1994).

| 10y window | US minus intl |
|---|---|
| 1972-1981 | -4.1% |
| 1973-1982 | -0.4% |
| 1974-1983 | -0.5% |
| 1975-1984 | -0.2% |
| 1976-1985 | -2.2% |
| 1977-1986 | -8.6% |
| 1978-1987 | -7.7% |
| 1979-1988 | -6.1% |
| 1980-1989 | -5.4% |
| 1981-1990 | -3.2% |
| 1982-1991 | -1.1% |
| 1983-1992 | -1.0% |
| 1984-1993 | -3.0% |
| 1985-1994 | -3.6% |
| 1986-1995 | 0.9% |
| 1987-1996 | 6.5% |
| 1988-1997 | 11.3% |
| 1989-1998 | 13.2% |
| 1990-1999 | 10.7% |
| 1991-2000 | 8.7% |
| 1992-2001 | 8.0% |
| 1993-2002 | 5.0% |
| 1994-2003 | 6.2% |
| 1995-2004 | 6.0% |
| 1996-2005 | 2.8% |
| 1997-2006 | 0.3% |
| 1998-2007 | -3.2% |
| 1999-2008 | -2.5% |
| 2000-2009 | -2.5% |
| 2001-2010 | -2.6% |
| 2002-2011 | -2.2% |
| 2003-2012 | -1.7% |
| 2004-2013 | -0.1% |
| 2005-2014 | 2.7% |
| 2006-2015 | 3.7% |
| 2007-2016 | 5.7% |
| 2008-2017 | 6.0% |
| 2009-2018 | 6.2% |
| 2010-2019 | 7.4% |
| 2011-2020 | 7.7% |
| 2012-2021 | 7.9% |
| 2013-2022 | 7.3% |
| 2014-2023 | 7.1% |
| 2015-2024 | 7.3% |
| 2016-2025 | 6.0% |

## Gold timing check: year-end vs annual-average gold

Rebalancing bonus = portfolio CAGR minus the weighted average of the sleeves' own CAGRs.

| Split | CAGR (year-end gold) | Bonus (year-end) | CAGR (avg gold) | Bonus (avg gold) |
|---|---|---|---|---|
| P3a stocks 100 US / 0 intl | 10.54% | 0.95% | 10.40% | 0.88% |
| P3b stocks 75 / 25 | 10.37% | 1.03% | 10.24% | 0.97% |
| P3c stocks 50 / 50 | 10.16% | 1.07% | 10.02% | 1.01% |
| P3d stocks 25 / 75 | 9.89% | 1.07% | 9.76% | 1.00% |
| P3e stocks 0 US / 100 intl | 9.59% | 1.01% | 9.46% | 0.95% |

