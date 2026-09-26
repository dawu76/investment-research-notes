# Layer 2 backtest results (1980-2025, annual rebalance, nominal USD)

Adds real-world trend-following records next to the simulated sleeve from layer 1:

- `cta_index`: Barclay CTA Index, net of fees, from 1980. Equal-weighted average of the CTA programs reporting to BarclayHedge (15 programs in 1980, 356 in 2025), so the early years reflect a small group of managers that survived long enough to report. You could not buy the index itself.
- `aqr_net`: AQR's time-series momentum factor from 1985, a research portfolio across roughly 60 futures markets, reported gross of fees. Shown after a flat 3.0%/yr drag.
- `trend`: the layer-1 simulated sleeve (US stocks, 10y Treasury, gold; monthly signal; 2.0%/yr drag).

## Trend sources compared (1985-2025, the years all three cover)

| Series | CAGR | Excess over T-bills | Vol | Max DD (annual) | Worst year |
|---|---|---|---|---|---|
| trend | 5.97% | 2.60% | 8.43% | -18.7% | -11.8% (2016) |
| cta_index | 6.28% | 2.91% | 10.54% | -6.1% | -3.2% (2018) |
| aqr_net | 12.41% | 8.85% | 14.59% | -30.6% | -13.8% (2016) |
| tbill | 3.28% | 0.00% | 2.56% | 0.0% | 0.0% (2014) |
| us_stocks | 11.83% | 8.28% | 16.66% | -37.4% | -36.6% (2008) |

Correlation of annual returns:

|  | trend | cta_index | aqr_net | us_stocks | tsy_10y | gold |
|---|---|---|---|---|---|---|
| trend | 1.00 | 0.13 | 0.44 | 0.25 | 0.31 | 0.17 |
| cta_index | 0.13 | 1.00 | 0.44 | -0.08 | 0.15 | 0.07 |
| aqr_net | 0.44 | 0.44 | 1.00 | -0.06 | 0.41 | -0.21 |
| us_stocks | 0.25 | -0.08 | -0.06 | 1.00 | 0.04 | -0.05 |
| tsy_10y | 0.31 | 0.15 | 0.41 | 0.04 | 1.00 | 0.06 |
| gold | 0.17 | 0.07 | -0.21 | -0.05 | 0.06 | 1.00 |

## Excess return over T-bills by decade (annualized)

| Series | 1980-1989 | 1990-1999 | 2000-2009 | 2010-2019 | 2020-2025 |
|---|---|---|---|---|---|
| trend | 2.8% | 2.7% | 3.7% | 1.3% | 2.5% |
| cta_index | 13.0% | 2.0% | 3.1% | 0.2% | 1.1% |
| aqr_net | n/a | 15.4% | 11.6% | 2.2% | -1.8% |

## Crisis years

| Year | Simulated trend | Barclay CTA | AQR TSMOM (net) | US stocks | 10y Treasury |
|---|---|---|---|---|---|
| 1987 | 8.6% | 57.3% | 24.7% | 5.8% | -5.0% |
| 2001 | 2.5% | 0.8% | 18.9% | -11.8% | 5.6% |
| 2002 | 16.6% | 12.4% | 28.2% | -22.0% | 15.1% |
| 2008 | 10.4% | 14.1% | 23.3% | -36.6% | 20.1% |
| 2020 | 4.5% | 5.4% | -9.4% | 18.0% | 11.3% |
| 2022 | -1.8% | 7.1% | 24.3% | -18.0% | -17.8% |

## Portfolios (1980-2025)

| Portfolio | CAGR | Real CAGR | Vol | Max DD (annual) | Max DD (monthly) | Worst year | 10y windows beating CPI |
|---|---|---|---|---|---|---|---|
| P1 20 gold / 20 tsy / 60 US | 10.11% | 6.71% | 10.78% | -17.0% | -25.9% | -17.0% (2008) | 100% |
| P5 Golden Butterfly (layer 1) | 9.06% | 5.70% | 7.69% | -8.9% | -17.5% | -8.9% (2008) | 100% |
| P4 no trend (extra 10% T-bills) | 9.32% | 5.95% | 9.50% | -17.9% | n/a | -17.9% (2008) | 100% |
| P4 + simulated trend | 9.60% | 6.22% | 9.71% | -17.0% | n/a | -17.0% (2008) | 100% |
| P4 + Barclay CTA Index | 9.80% | 6.41% | 9.66% | -16.6% | n/a | -16.6% (2008) | 100% |

## Portfolios (1985-2025, adds the AQR version)

| Portfolio | CAGR | Real CAGR | Vol | Max DD (annual) | Max DD (monthly) | Worst year | 10y windows beating CPI |
|---|---|---|---|---|---|---|---|
| P1 20 gold / 20 tsy / 60 US | 10.22% | 7.24% | 10.70% | -17.0% | -25.9% | -17.0% (2008) | 100% |
| P5 Golden Butterfly (layer 1) | 8.82% | 5.88% | 7.54% | -8.9% | -17.5% | -8.9% (2008) | 100% |
| P4 no trend (extra 10% T-bills) | 9.15% | 6.20% | 9.64% | -17.9% | n/a | -17.9% (2008) | 100% |
| P4 + simulated trend | 9.43% | 6.47% | 9.88% | -17.0% | n/a | -17.0% (2008) | 100% |
| P4 + Barclay CTA Index | 9.49% | 6.53% | 9.66% | -16.6% | n/a | -16.6% (2008) | 100% |
| P4 + AQR TSMOM (net) | 10.16% | 7.18% | 9.67% | -15.7% | n/a | -15.7% (2008) | 100% |

The P4 variants differ only in their 10% trend sleeve; "P4 no trend" puts that 10% in T-bills.

## Start-date sensitivity (nominal / real CAGR through end year)

| Portfolio | from 1980 | from 1985 | from 1990 | from 2000 | from 2010 |
|---|---|---|---|---|---|
| P4 no trend (extra 10% T-bills) | 9.32% / 5.95% | 9.15% / 6.20% | 8.07% / 5.27% | 7.37% / 4.70% | 8.74% / 6.02% |
| P4 + simulated trend | 9.60% / 6.22% | 9.43% / 6.47% | 8.34% / 5.53% | 7.64% / 4.96% | 8.92% / 6.19% |
| P4 + Barclay CTA Index | 9.80% / 6.41% | 9.49% / 6.53% | 8.26% / 5.45% | 7.54% / 4.87% | 8.80% / 6.07% |
| P4 + AQR TSMOM (net) | n/a | 10.16% / 7.18% | 8.96% / 6.14% | 7.97% / 5.29% | 8.89% / 6.16% |

