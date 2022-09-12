### Asset allocation strategies

Below is a collection of asset allocation strategies that can be self-managed.

---

### Alpha Architect: [Robust Asset Allocation (RAA)](https://alphaarchitect.com/2014/12/the-robust-asset-allocation-raa-index/)

The tactical objectives of our RAA indexes are as follows:
- Portfolio growth that keeps up with inflation (principal growth): the goal is not to outperform some other index or benchmark
- Downside protection (avoid large drawdowns)
- Superior tax efficiency (tax-savvy investing)
- Liquidity (facilitates flexibility)
 
3 variants of RAA
- balanced: 40% equities, 40% real assets, 20% bonds
- moderate: 60% equities, 20% real assets, 20% bonds
- aggressive: 80% equities, 10% real assets, 10% bonds

The moderate variant uses the following allocations
- 60% equities = 30% domestic, 30% international: the allocations may change based on value & momentum
- 20% real assets = 10% commercial real estate via REIT index, 10% diversified commodities via commodity index
- 20% government bonds (10-year UST)

Principles of RAA approach

> We are biased towards simplicity because it works and also has the following benefits: less susceptible to data-mining, harder to disguise as black-box solutions that charge higher fees.
>
> 3 elements of the approach
> - Asset Allocation: Instead of complex asset allocation, use simple allocation.
> - Security Selection: Instead of story-based stock selection, use evidence-based stock selection.
> - Risk Management: Instead of buy-and-hold, use a downside-protection system.

Value/Momentum rules
- RAA Moderate uses both a "time-series absolute momentum" rule as well as a long-term moving average rule. The goals are to avoid assets with poor absolute and relative performance
- Absolute momentum rule: If "excess return" := return above Treasury bills over the past N = 12 months > 0, go long risky assets; otherwise go to cash or T-bills.
- Moving-average rule: If current price > moving average over past N = 12 months, then go long risky assets; otherwise go to cash or T-bills.
- RAA spreads its bets based on both rules, going to cash/T-bills or partial risk or full risk based on whether one or both rules are triggered: "we’ve found evidence that these rules sometimes have a difference of opinion, where one rule says 'risk' and the other says 'no risk.' We also find that spreading our trend-following bet across these two systems is more robust than simply relying on one or the other."

Notes on performance comparisons
- > One can expect to underperform (and outperform) the generic 60/40 in any given year or set of years. But that is to be expected because the US 60/40 is a different portfolio with different objectives than the RAA Moderate Index. The RAA Moderate Index is built to capture global risk premiums and minimize the chance of large tail risks. The US 60/40 portfolio is built to capture US risk premiums. Different portfolios will mechanically lead to different outcomes.

Simulated backtest performance: 1995-2017
- The study notes that "the results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained."
- Compare RAA Moderate Index to RAA Simple (30% US Combo, 30% Int’l Combo, 10% REIT, 10% Comm, 20% Bonds) and RAA Simple + Value/Momentum (like RAA Simple but with Value/Momentum overlay)
- These backtests show RAA Moderate outperforming RAA Simple with a CAGR 4% higher, with much higher Sharpe and more modest drawdown of 15% vs. 40% - 45%.

Actual performance of SMAs based on RAA methodology
- Its main benchmark is the "RAA Simple Moderate Index," which has the following allocations: 30% S&P 500, 30% MSCI EAFE, 10% passive REITs, 10% passive global commodities, and 20% intermediate-term (7-10 year) USTs.
- Per the [2022.07 performance file](https://alphaarchitect.com/wp-content/uploads/compliance/sma/gips/RAA%20Mod%20RM.pdf) listing the RAA Moderate strategy's returns through 2022-June, the RAA has significantly underperformed its benchmarks and has just a 1% 5-year annualized return. It also has a slightly negative Sharpe ratio since 2014.
- It has about the same max drawdown and more modest worst 1-month, 3-month, 6-month drawdowns than the main benchmark.

Performance of Robust RAA portfolio
- Based on [study by PortfolioLabs](https://portfolioslab.com/portfolio/alpha-architect-robust)

Ongoing trend signals for RAA strategy
- [This page](https://alphaarchitect.com/indexes/trend/#_trendcurrent) lists current signals for the GVMT (Global Value Momentum Trend Index) and RAA
- As of early 2022-September, the balanced, moderate, and aggressive variants of RAA have 80-95% Treasuries and 5% to 20% commodities (balanced = 20% commodities) according to the "Current Signals" section of the page.
- In the "Historical Signals" section, RAA was listed as having a signal of 100% for commodities during the past several months.

---

### References

The following are listed as strategies tested by Alpha Architect
- Simple MA Rules: [Faber (2007)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=962461), "A Quantitative Approach to Tactical Asset Allocation."
- Challenging MA rule #1: Scholz and Walther (2011), "The trend is not your friend! Why empirical timing success is determined by the underlying’s price characteristics and market efficiency is irrelevant"
- Challenging MA Rule #2: Zakamulin, "The Real-Life Performance of Market Timing with Moving Average and Time-Series Momentum Rules"
- Challenging MA Rule #3: Marmi, Pacati, Risso, Reno, "A Quantitative Approach to Faber’s Tactical Asset Allocation"
