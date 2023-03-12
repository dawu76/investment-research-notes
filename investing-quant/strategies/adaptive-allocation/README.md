### Asset allocation strategies

Below is a collection of asset allocation strategies that can be self-managed.

---

#### Dual Momentum – Global Equity Momentum

From Antonacci's Dual Momentum book [notes](https://read.amazon.com/kp/notebook?ref_=k4w_ms_notebook):

> In absolute momentum, we look at an asset’s excess return (its return less the return on Treasury bills) over a given look-back period. If the excess return is above zero, then the asset has positive absolute momentum. If the excess return is below zero, then the asset has negative absolute momentum. Absolute momentum is roughly the same as relative momentum applied to an asset paired up with Treasury bills.
>
> The best approach is to use absolute and relative together in order to gain the advantages of both. The way we do that is by first using relative momentum to select the best-performing asset over the preceding 12 months. We then apply absolute momentum as a trend-following filter by seeing if the excess return of our selected asset has been positive or negative over the preceding year. If it has been positive, that means its trend is up and we proceed to use that asset. If our asset’s excess return over the past year has been negative, then its trend is down and we invest instead in short- to intermediate-term fixed-income instruments until the trend turns positive. This way, we are always in harmony with the trend of the market.

And from Antonacci's 2018 blog post:

> When the trend of stocks is up according to absolute momentum applied to the S&P 500, we use relative strength to determine if we will be in U.S. or non-U.S. stocks. When the trend of stocks is down, we invest in bonds. We use a 12-month lookback period for both types of momentum and rebalance monthly.

##### References
- Gary Antonacci's [Optimal Momentum](https://www.optimalmomentum.com/faq/) site + [running tally](https://www.optimalmomentum.com/global-equities-momentum/) of monthly & annual returns of GEM
- InvestResolve's [executive summary](https://investresolve.com/global-equity-momentum-executive-summary/) + [whitepaper](https://investresolve.com/global-equity-momentum-a-craftsmans-perspective-lp/)
- Antonaaci's 2019 [blog post](https://dualmomentum.net/2019/01/17/whither-fragility-dual-momentum-gem/), "Whither Fragility: Dual Momentum GEM", on Corey Hoffstein's "Fragility Case Study: Dual Momentum GEM" article advocating the use of multiple lookback periods to avoid specification bias 
- Extrategic [blog post](https://extradash.com/en/strategies/models/10/dual-momentum/) on Antonaaci's Dual Momentum

---

#### Meb Faber's Tactical Asset Allocation

From the Extrategic [blog post](https://extradash.com/en/strategies/models/5/faber-tactical-asset-allocation/):

> The Faber TAA model uses a 10-month Simple Moving Average (SMA) of the monthly closing prices to determine whether to enter or exit a particular market.
> 
> You calculate the SMA value by simply taking the average of the closing prices of the most recent 10 months. On the following month, the oldest data is dropped off and is replaced by the newest one.
> 
> At the end of each month, we buy if the price is greater than the SMA, and we sell if the price is lesser than the SMA. We ignore any price changes in the middle of the month. If you’ve looked into Fabian’s timing model, you’ll notice that the logic is the same, except Faber uses 10 months for lookback while Fabian uses 39 weeks (10 months is approximately 40 weeks).

##### References
- Fabers [2014 paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=962461): A Quantitative Approach to Tactical Asset Allocation
- Extrategic [blog post](https://extradash.com/en/strategies/models/5/faber-tactical-asset-allocation/) on Faber's TAA

---

#### Alpha Architect: [Robust Asset Allocation (RAA)](https://alphaarchitect.com/2014/12/the-robust-asset-allocation-raa-index/)

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

[Alpha Architect (2015)](https://alphaarchitect.com/2015/08/avoiding-the-big-drawdown-with-trend-following-investment-strategies/): Avoiding the Big Drawdown with Trend-Following Investment Strategies
- This post evaluates the performance of two common strategies: 1) If weak absolute performance appears, go to cash; 2) If weak trending performance appears, go to cash.
- These rules together constitute the "Downside Protection Model" based on Time-series Momentum (TMOM) and Simple Moving Averages (SMA).
- Time Series (Absolute) Momentum Rule (TMOM) Excess return = total return over the past 12 months less return of T-Bills > 0, go long risky assets. Otherwise, go long alternative assets (T-Bills)
- Simple Moving Average (Trending Performance) Rule (MA): If Current Price – Moving Average (12) > 0, go long risky assets. Otherwise, go long alternative assets (T-Bills).

---

### Research

[paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4318157): A Century of Asset Allocation Crash Risk [2023]
- While endowment strategy is a front runner in cumulative returns and surpasses both classic strategies, such as U.S. 60/40, Global 60/40, Diversified, and more sophisticated and innovativeRisk Parity, Factor-Based, and Dynamic allocation, it only comes out third on the risk-adjusted basis, losing to Factor-Based and Dynamic strategies. It turns out that most strategies are prone to deep, frequent, and prolonged downturns in portfolio value (drawdowns) in the event of market crash that occur several times during the observed period.
- Only Factor-Based allocation offers a significant improvement over others when it comes to a large-scale loss of wealth when markets approach their trough. Dynamic allocation stands out in stark contrast with others with maximum drawdown of only 26% and very infrequent incidences of 15-25% drawdowns, as compared to 62% maximum wealth loss in US 60/40, Risk Parity, and Endowments.
- Dynamic allocation stands out sharply among the rest of the popular investment strategies with only 8 drawdowns of 15% or more, only 2 of 25% or more, and the maximum drawdown of 26%, a stunning achievement, when the next lowest of Factor-Based portfolio is at 44%. In sum, unconditionally, Dynamic allocation significantly reduces drawdown risk.

---

### Discussion forum posts

Reddit
- [post](https://www.reddit.com/r/investing/comments/9u57vp/why_are_taa_strategies_preferred_over_a_long_term/): Why are TAA strategies preferred over long-term buy & hold?

bogleheads.org
- [post](https://www.bogleheads.org/forum/viewtopic.php?t=158297): Dual momentum investing
- [post](https://www.bogleheads.org/forum/viewtopic.php?f=10&t=29844): Debunking a Meb Faber backtesting paper
- [post](https://www.bogleheads.org/forum/viewtopic.php?t=27460): 200-day moving average market timing

---

### References

The following are listed as strategies tested by Alpha Architect
- Simple MA Rules: [Faber (2007)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=962461), "A Quantitative Approach to Tactical Asset Allocation."
- Challenging MA rule #1: Scholz and Walther (2011), "The trend is not your friend! Why empirical timing success is determined by the underlying’s price characteristics and market efficiency is irrelevant"
- Challenging MA Rule #2: Zakamulin, "The Real-Life Performance of Market Timing with Moving Average and Time-Series Momentum Rules"
- Challenging MA Rule #3: Marmi, Pacati, Risso, Reno, "A Quantitative Approach to Faber’s Tactical Asset Allocation"
