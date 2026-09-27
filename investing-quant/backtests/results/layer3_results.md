# Layer 3 backtest results (1972-2025, annual rebalance, nominal USD)

Adds TIPS, in three versions:

- `tips_fund`: Vanguard Inflation-Protected Securities Fund (VIPSX), actual total returns, from 2001.
- `tips_10y`: modeled 10y constant-maturity TIPS from the Fed's market real yields (Gurkaynak-Sack-Wright TIPS curve), from 2000.
- `tips_synth`: synthetic 10y TIPS from 1972. Real yield = month-end nominal 10y yield minus expected inflation (Livingston Survey 12-month forecast before 1982, Cleveland Fed 10-year expectation after). US TIPS did not exist before 1997.

## How each version tracks the actual fund (2001-2025)

| Series | CAGR | Vol | Correlation with VIPSX | Tracking error vs VIPSX |
|---|---|---|---|---|
| tips_fund | 4.00% | 6.22% | 1.00 |  |
| tips_10y | 4.25% | 8.24% | 0.99 | 2.3% |
| tips_synth | 3.69% | 6.84% | 0.58 | 6.0% |
| tsy_10y | 3.34% | 8.58% | 0.53 | 7.4% |

| Year | tips_fund | tips_10y | tips_synth | tsy_10y |
|---|---|---|---|---|
| 2002 | 11.8% | 16.9% | 13.3% | 15.1% |
| 2008 | -2.8% | -4.8% | 13.6% | 20.1% |
| 2009 | 10.8% | 13.8% | -7.8% | -11.1% |
| 2013 | -8.9% | -12.5% | -7.2% | -9.1% |
| 2021 | 5.6% | 6.0% | 4.1% | -4.4% |
| 2022 | -12.0% | -18.2% | -10.9% | -17.8% |

## Inflation years (CPI above 6%)

| Year | cpi | tbill | tsy_10y | tips_synth | tips_10y | tips_fund |
|---|---|---|---|---|---|---|
| 1973 | 8.7% | 7.0% | 3.7% | 24.7% | n/a | n/a |
| 1974 | 12.3% | 7.8% | 2.0% | 28.8% | n/a | n/a |
| 1975 | 6.9% | 5.8% | 3.6% | -6.9% | n/a | n/a |
| 1977 | 6.7% | 5.3% | 1.3% | 8.3% | n/a | n/a |
| 1978 | 9.0% | 7.2% | -0.8% | 7.5% | n/a | n/a |
| 1979 | 13.3% | 10.1% | 0.7% | 26.0% | n/a | n/a |
| 1980 | 12.5% | 11.4% | -3.0% | -1.3% | n/a | n/a |
| 1981 | 8.9% | 14.0% | 8.2% | -21.3% | n/a | n/a |
| 1990 | 6.1% | 7.8% | 6.2% | 11.3% | n/a | n/a |
| 2021 | 7.0% | 0.0% | -4.4% | 4.1% | 6.0% | 5.6% |
| 2022 | 6.5% | 2.1% | -17.8% | -10.9% | -18.2% | -12.0% |
| Real, annualized |  | -1.7% | -8.4% | -3.3% | n/a | n/a |

Portfolio returns in those years:

| Year | P1 20 gold / 20 tsy / 60 US | P1 with TIPS (synthetic) | P4 candidate mix (layer 1) | P6 full mix (synthetic TIPS, simulated trend) |
|---|---|---|---|---|
| 1973 | 6.7% | 11.0% | 6.0% | 7.7% |
| 1974 | -1.9% | 3.5% | 2.1% | 4.2% |
| 1975 | 18.0% | 15.9% | 19.1% | 17.9% |
| 1977 | 0.6% | 2.0% | 7.3% | 7.6% |
| 1978 | 11.2% | 12.8% | 16.8% | 16.8% |
| 1979 | 36.6% | 41.6% | 35.3% | 36.9% |
| 1980 | 21.5% | 21.8% | 20.2% | 18.9% |
| 1981 | -7.7% | -13.6% | -0.7% | -4.2% |
| 1990 | -1.2% | -0.2% | -6.1% | -5.8% |
| 2021 | 15.4% | 17.2% | 13.6% | 14.0% |
| 2022 | -14.3% | -12.9% | -9.8% | -11.1% |
| Real, annualized | -1.9% | -0.8% | -0.1% | -0.3% |

## Portfolios (1972-2025, synthetic TIPS)

| Portfolio | CAGR | Real CAGR | Vol | Max DD (annual) | Max DD (monthly) | Worst year | 10y windows beating CPI |
|---|---|---|---|---|---|---|---|
| P1 20 gold / 20 tsy / 60 US | 10.54% | 6.40% | 10.96% | -17.0% | -25.9% | -17.0% (2008) | 100% |
| P1 with TIPS (synthetic) | 10.61% | 6.46% | 11.17% | -18.3% | -27.2% | -18.3% (2008) | 100% |
| P4 candidate mix (layer 1) | 10.42% | 6.28% | 9.94% | -17.0% | n/a | -17.0% (2008) | 100% |
| P6 full mix (synthetic TIPS, simulated trend) | 10.64% | 6.49% | 10.08% | -15.7% | n/a | -15.7% (2008) | 100% |
| P5 Golden Butterfly (layer 1) | 10.03% | 5.90% | 8.38% | -8.9% | -17.5% | -8.9% (2008) | 100% |

## Portfolios (2001-2025, actual TIPS fund and Barclay CTA Index)

| Portfolio | CAGR | Real CAGR | Vol | Max DD (annual) | Max DD (monthly) | Worst year | 10y windows beating CPI |
|---|---|---|---|---|---|---|---|
| P1 20 gold / 20 tsy / 60 US | 8.92% | 6.25% | 11.41% | -17.0% | -25.9% | -17.0% (2008) | 100% |
| P1 with TIPS (VIPSX) | 8.93% | 6.26% | 12.13% | -21.6% | -29.2% | -21.6% (2008) | 100% |
| P4 + Barclay CTA Index | 7.86% | 5.21% | 10.15% | -16.6% | n/a | -16.6% (2008) | 100% |
| P6 full mix (VIPSX, Barclay CTA) | 8.08% | 5.42% | 10.39% | -17.0% | n/a | -17.0% (2008) | 100% |
| P5 Golden Butterfly (layer 1) | 7.95% | 5.29% | 8.00% | -8.9% | -17.5% | -8.9% (2008) | 100% |

"P1 with TIPS" swaps P1's 20% nominal 10y Treasury for TIPS. P6 is the full candidate mix: 30 US / 15 intl / 10 small value / 15 gold / 10 nominal 10y Treasury / 10 TIPS / 10 trend. P4 is the same mix with T-bills in the TIPS slot.

