### How Allocate Smartly's Tactical Asset Allocation tool works

Users can combine strategies with the click of a button to create their own custom Model Portfolios
- strategies are sourced from books, academic papers and other publications
- these strategies are quantitative and systematic, meaning well-defined mathematical rules govern exactly when and what to trade
- analyze each strategy with thorough, up to date backtests
- combine them to create their own custom Model Portfolios to reduce the risk of any single strategy going off the rails and to provide smoother, more consistent investment returns
- assumptions: all strategies trade at the market close (read more about when we trade), and that trades are executed using large, liquid ETFs. From the FAQ: "All of the strategies that you’ll find here trade ETFs that track broad asset classes such as stock indices (ex. SPY), bond indices (AGG), or gold (GLD). We represent each asset class using the largest, most liquid ETF available "
- refer to the FAQ for more info on the assets used to replicate each strategy

Users can follow [Meta Strategies](https://allocatesmartly.com/meta-strategy-smart-approach-combining-taa-strategies/), or combinations of TAA strategies
- Each month, AllocateSmartly's Meta selects a representative sample of 10 TAA strategies based on a number of factors.
- These selection criteria include: (1) consistent performance relative to risk, i.e. performance of each strategy relative to volatility, drawdown and other measures of risk across multiple timeframes; (2) the dissimilarity of the strategies, the idea being that minor performance differences between similar strategies are more likely to reflect noise; (3) performance adjusted for the "impact of current interest rates across the yield curve," which tries to account for the fact that certain assets have enjoyed tailwinds from falling interest rates, which can further fall only so far in the future; the general methodology is described in the "Modelling Treasury ETF Performance during Rising Rates" [blog post](https://allocatesmartly.com/modelling-treasury-etf-performance-era-rising-rates/).
- Testing of these strategies is “walked forward”, meaning at each data point Meta only had access to the data that was available at that point in time. Meta can’t "peek" into the future the way we could if we simply chose the best performing strategies as of today. That provides a certain degree of confidence that our approach is targeting future outperformance, not simply past outperformance."
- Reference: [meta strategy](https://allocatesmartly.com/advanced-features/) page 

---

### On reported backtested results [from FAQ]

Notes on AllocateSmartly's backtesting methodology
- "Our results are more pessimistic (realistic) than you’ll find elsewhere because our test assumptions tend to be stricter. Some examples - We account for transaction costs/slippage, which developers often do not. See Backtest Assumptions."
- "We represent each asset class using the largest, most liquid ETF in that space. We do not allow for niche or less commonly traded assets for both practical reasons (it makes combining multiple strategies together more manageable), as well as analytical reasons (it’s a guard against overfitting)".
- "When simulating historical asset data (read more), we only use indices or other data sources that are closely related to a large, liquid ETF trading today."

---

### Blog posts & forum threads

Scott's Investments
- [post](https://scottsinvestments.com/2017/05/17/testing-dual-momentum-with-allocatesmartly/): Testing dual momentum with Allocate Smartly
- [post](https://scottsinvestments.com/2016/05/11/dual-etf-momentum-may-update-2/): Dual ETF momentum - May update

Quantified Strategies
- [post](https://quantifiedstrategies.substack.com/p/meb-fabers-momentumtrend-following?s=w): Meb Faber's momentum and trend-following strategy
- [post](https://www.quantifiedstrategies.com/meb-faber-momentum-trend-following-strategy/): Is Meb Faber's momentum and trend-following strategy still working?

bogleheads.org
- [post](https://www.bogleheads.org/forum/viewtopic.php?t=267191): anyone using Allocate Smartly?

---
