### Notes on risk parity.

Refer to books by Alex Shahidi.

---

[Adaptive Asset Allocation, Risk Parity And Return Stacking With Adam Butler](https://pictureperfectportfolios.com/adaptive-asset-allocation-risk-parity-return-stacking-adam-butler-resolve/)

Context
- A more efficient portfolio can be constructed by diversifying across as many sources of return as possible, and scaling exposure to this diversified portfolio using leverage to achieve one’s target return. This concept is called "Modern Portfolio Theory." To enjoy the greatest amount of expected portfolio growth with the lowest volatility, an investor should invest in an optimally diversified portfolio, and scale exposure to the portfolio using leverage to achieve the required return.
- But most investors do not have access to borrowing at rates that make leverage attractive. And many of those who do have access are constrained by regulations, or have a behavioral aversion to leverage. New products launched in the last few years allow individual investors access to efficient leverage and alternative sources of return, and we’re seeing an acceleration in adoption. I expect this trend to continue as returns to 60/40 struggle in the more complicated environment we’re facing in the next decade or so. 

Key concept: "Risk parity is about diversity and balance."
- Diversity, in a portfolio context, is about owning investments that are designed to respond in different ways to various types of economic shocks.
- Think about economic shocks is along the axes of inflation and growth. Different asset classes thrive in different conditions.
- Balance: a simple portfolio that holds equal weight in stocks and bonds is not well balanced because stocks are much more volatile than bonds; a portfolio that has 50% stocks and 50% in bonds has over 90% of its risk coming from stocks. To create a balanced portfolio of stocks and bonds you would have to hold about 80% of capital in bonds and just 20% in stocks.

<img src="https://user-images.githubusercontent.com/1627180/172748601-709c5532-f2d5-4d39-a02f-228f5adf5018.png" width="75%" height="75%" />

Example of how risk parity uses leverage to achieve a target return
- Given: $100 to invest, borrowing rate = 2%, portfolio return and volatility = 4%, 6%
- Borrow $50 so that we have a total of $150 to invest
- Investing that $150 in the portfolio yields 1.5 * 4% return = 6% return, 1.5 * 6% volatility = 9% volatility
- Borrowing cost = $50 * 2% = 1% cost ($1)
- Net return = 6% - 5% = 5%, volatility = 9%

Example: most of the risk in a stock-heavy portfolio comes from the stock allocation 
- Given: we invest in just stocks and bonds, which we assume are uncorrelated
- stocks have a return = 6%, volatility = 20%
- bonds have return = 3%, volatility = 5%
- suppose we want to target a 5% return: this is achievable via 2/3 stock and 1/3 bond allocation = 2/3 * 6% + 1/3 * 3%
- if stocks & bonds are uncorrelated, then the volatility of this 2:1 allocation = $\sqrt{(2/3 * 20)^2 + (1/3 * 5)^2}$ = 13.5
- note that the volatility of a 2:1 stock:cash allocation is $(2/3) * 20$, which is almost as high as the 2:1 stock:bond portfolio;
- this tells us that most of the volatility of the 2:1 stock:bond portfolio comes from the stock portion

---

#### Risk Parity + Trend Following
- From the AllocateSmartly [blog post](https://allocatesmartly.com/taa-strategy-combining-risk-parity-trend-following/): "TAA Strategy Combining Risk Parity & Trend Following", we can combine two strategies: trend-following (to determine what assets to hold) and risk parity (to determine how much of each asset to hold), to produce one of the least volatile strategies [that we track](https://allocatesmartly.com/list-of-strategies/)
- This post covers two versions of the strategy: the first focused on the US, and the second on global markets.
- Results: Relative to a 60/40 benchmark or equal-weighted benchmark, this strategy results in considerably higher Sharpe & Sortino ratios and much lower max drawdowns over the backtest period.
- AllocateSmartly can be used to follow and track this strategy in near real-time.
