# RobotWealth Pro Webinar: Factor Combinations & Momentum Deep Dive (2026-04-18)

## 1. Introduction: The Need for a Solo Operator Framework
Chris kicks off the session by introducing a conceptual framework for combining factors. Much of the available literature on factor investing targets institutional funds, assuming a scale of capital, operational capacity, and complex portfolio optimization tools that solo traders simply don't have. Instead of shoehorning institutional methods into an individual trading operation, Chris proposes a robust, heuristic-based approach built specifically for the constraints of a solo trader.

## 2. The Four Hats of Factor Investing
Building on the "Four Hats" framework introduced in previous sessions, Chris adapts it to the factor world:
* **The Scientist:** Exploring the factor in isolation, understanding its properties, and validating its underlying mechanism.
* **The Engineer:** Figuring out how to turn the factor into a viable, self-contained "sleeve." A sleeve is a standalone portfolio built around a single factor, with its own signal, target positions, and ideal rebalance cadence.
* **The Architect:** Combining multiple factor sleeves into a cohesive long-short equity portfolio. (This is the primary focus of today's framework).
* **The Operator:** Executing the day-to-day trading, managing sizing, handling data feeds, and navigating real-world trading constraints.

*Ewan's Note on Nomenclature:* Ewan clarifies that in academic literature, "factors" usually refer to long-term equity anomalies (like value or size). In the context of RobotWealth's stat arb strategies, "factors" are used to describe shorter-term cross-sectional edges (daily or weekly). 

## 3. Core Principles of the Portfolio Architecture
To step away from noisy mean-variance optimization models, Chris outlines four guiding principles for this approach:
1. **Focus on what you control and know:** Don't rely on highly noisy estimates like expected returns and covariance matrices. 
2. **Heavy use of constraints:** Use explicit constraints (like maximum sector or ticker concentration limits) to systematically remove risks from the portfolio.
3. **Respect each factor's character:** Instead of forcing all factors to trade simultaneously, use asynchronous rebalancing. Slow momentum might rebalance weekly or fortnightly, whereas short-term reversal (stat arb) might rebalance daily.
4. **Mechanism outranks backtested Sharpe:** With high noise and limited data, relying on a solid fundamental reason for why a factor exists is more reliable than raw backtest metrics.

## 4. Structuring the Combined Portfolio
Instead of blending signals into a single opaque master signal, the proposed approach involves:
* **Running Independent Sleeves:** Each factor runs in its own sleeve, generating target positions based on its optimal cadence.
* **Broad Signal Calculation, Narrow Execution:** Signals are computed on a broad, liquid universe (e.g., 2,000 stocks). The target positions from all sleeves are stacked and netted out at the ticker level. 
* **Universe Constraints & Buffer Management:** Finally, a top-level capacity constraint is applied (e.g., only trading the top 100 net opportunities). A smart "rebalance buffer" is used to prevent stocks from constantly slipping in and out of the tradable universe, effectively managing turnover and transaction costs.

## 5. Lab Updates: New Liquid Universe Data
Chris introduces two new datasets in the lab to support this research:
* **Liquid Universe Prices:** Price history for ~4,000 stocks going back to 2015, featuring a new `is_indexed` boolean column. This column indicates if a stock passed liquidity filters *before* the current date, removing look-ahead bias while allowing rolling calculations over a continuous price history.
* **Sector and Industry Data:** Provided to help condition and neutralize factor returns by sector.

*(A note on documentation: Following member feedback, Chris agreed to look into creating a unified documentation page for the Lab's datasets, though currently, details are housed in the READMEs of individual research pods).*

## 6. Colab Deep Dive: The Momentum Factor
The bulk of the session focuses on a deep dive into the 12-month momentum factor (skipping the most recent month) within the liquid universe.

### Mechanism Theories
Why does momentum exist? Theories include slow information diffusion, index tracking mandates, and the persistence of strong underlying business fundamentals. Chris introduces a recent paper suggesting an "Intra-month Momentum Cycle," driven by institutional funds selling their losers to raise cash. *Ewan expresses skepticism regarding the "cash-raising" narrative, suggesting it feels retrofitted, but acknowledges the statistical effect is undeniably strong.*

### General Characteristics of 12-Month Momentum
* **Return Shape:** Returns generally scale upward from decile 1 (losers) to decile 10 (winners). However, decile 1 rarely has the absolute worst return, indicating that despite skipping the most recent month, short-term reversal contamination persists.
* **Persistence:** The factor performs well in most years but is susceptible to severe crashes (e.g., 2016, 2023). 
* **Lookback Periods:** The effect transitions from short-term reversal to momentum somewhere between 21 and 63 days. Interestingly, 6-month momentum appeared slightly stronger than 12-month momentum in this dataset.

### The Intra-Month Momentum Cycle
Testing the recent paper's thesis, Chris divided the month into a "Concentration Window" (Days T-9 to T-4) and the rest of the month. 
* **Findings:** In the liquid universe, the momentum spread (Decile 10 - Decile 1) averaged 11.5 basis points within the concentration window, but was slightly negative during the rest of the month.
* **Driver:** Consistent with the paper, the spread in the concentration window is largely driven by losers continuing to lose. 
* **Liquidity:** Counterintuitively, the effect was strongest in the *most liquid* stocks (often called the "dash for cash" phenomenon, where liquid losers are sold for easy capital). In less liquid stocks, the effect was driven by a mix of selling losers and buying winners.

### Conditioning on Volatility, Beta, and Sectors
* **Volatility:** Momentum works across most volatility regimes but breaks down in the most extreme high-volatility bucket. It is not simply a disguised volatility trade.
* **Beta:** The factor generates positive returns across all beta quintiles (peaking slightly in mid-beta stocks), proving it is not just a proxy for market beta.
* **Sector Dependence:** Sector-neutralized momentum (trading momentum relative to peers within the same sector) generated about half the returns of raw momentum over the full sample. A significant portion of raw momentum is essentially sector rotation. 
* **Yearly Breakdown:** The outperformance of raw momentum over sector-neutralized momentum was mostly driven by a few extreme outlier years (2020, 2022, 2026) featuring high sector dispersion. For baseline portfolio construction, sector-neutralized momentum is more stable and better understood.

## 7. Q&A and Modeling Philosophy

### In-Sample vs. Out-of-Sample Testing
Stefan asked about validating research through out-of-sample or walk-forward testing. Chris explained his strong stance against it in this specific context:
* **Finite Data:** There is only one history of market prices. True out-of-sample data evaporates quickly once you've researched the markets for a while.
* **Low Signal-to-Noise:** Strategies operating at Sharp ratios of 0.6 to 1.2 are heavily drowned in noise. Standard statistical tests require vastly more data than is available to prove significance. 
* **The Alternative:** Lean heavily on understanding the *mechanism*. A plausible, logical driver for an edge is vastly more valuable than over-optimizing backtests. Using blunt, imprecise rules acknowledges this noise and explicitly prevents curve-fitting.

### UVXY Short Borrow Costs
Addressing a question about a different strategy (UVXY/VXZ shorting), Chris confirmed the simulation used a flat mean borrow cost (around 12.3%). To stress-test the model against extreme environments, he recommended running it against the 90th percentile or even maximum historical borrow costs. Alternatively, trading VIX futures bypasses the borrow availability issue entirely.

---
**Next Steps:** Chris plans to further investigate sector dispersion, refine the parameters for a 6-month momentum sleeve, and eventually test the asymmetrical volume factor before combining them all into a unified stat arb portfolio.