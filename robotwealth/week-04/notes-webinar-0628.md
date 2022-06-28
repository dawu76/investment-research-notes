### Week 4 webinar

Notes on the research process

---

#### Keep doing the simplest thing that could possibly work

Don't built big projects to get the exact answer - get to an answer quickly and iterate. Focus on proving or disproving your hypotheses.

- Uncover assumptions
- Make testable hypotheses
- What would I expect to see in data if this were true? Look for it as directly and easily as you can with available data? What other hypotheses would explain the patterns in the data?
- Think about possible biases in your data but don't obsess over it.
- What would I expect to see if it weren't true?
- Consideration: deal with anxiety over possibility you'll never figure it out - nothing will be known for certain

Exploratory techniques for understanding data
- histograms
- time-series charts
- stationarity
- scatterplots
- factor analysis
- event studies, "markouts"
- simulation and backtesting

---

#### Calling BS

Avoid magical thinking like "let winners ride and cut your losers." Question assumptions/

Folkore: "Stop losses cap downside, lessen my slippage"
- Only if you stop trading - at some point, you have to get a new position on ...
- But when would it be helpful? When the position is more likely to keep going down. But if it's as likely to keep going down as it is to be going back up, then it won't help. So to be effective, we need to actually make a prediction about how price will move when it gets to the stop liimt level.

Recent example: "Vol has been realizing significantly over (under) implied vol, so it's good to be long (short) vega."
- Translation: "We've recently seen certain conditions, so we should put on a trade that assumes the future will be like this recent past."
- Question: on what time frame will volatility "cluster" and when will it mean-revert?

Uncovering implicit assumptions
- look at actual realized volatility over a past period (e.g. past 30 days), look at option implied volatility (IV) over next 30 days. Compare the two over recent periods to see if options were selling for too cheap.
- actual realized volatility will continue being higher than implied in the near future because it was like this in the recent past
- Testable assumption: Realized volatility (RV) > IV, then options were cheap. If by this measure, they were cheap in the last period, they're more likely to be cheap next period as well.
- Find the simplest, most direct way to test the hypothesis; don't throw in additional assumptions or conditions. E.g. just because options are selling for "cheap" doesn't mean we'd be profitable trading them. More direct condition to test: if option is cheap in period T, it will tend to be cheap in period (T+1). In other words, option prices exhibit auto-correlation or trend.

#### Getting data

Realities of working with data
- dealing with new datasets is a hassle
- cleaning data is cumbersome due to common issues like timezone issues, missing data, adjusting for asset specific issues like splits, dividends, etc

Getting to an answer more quickly
- Don't solve all your problems at once
- Use the easiest, lowest frequency data that is sufficient to prove or disprove your hypothesis
- Goals: get ATM IV of options with 30D to expiration + SPX daily returns to calculate RV over 22 trading days.
- How to get ATM IV of options with 30D to expiry: VIX seems good enough. How to get RV over next 30 days? Resort to SPY daily returns over the subsequent 22 trading days.

#### Understanding biases and assumptions in dataset

Can't make all biases go away but good to be aware of them. And often, biased datasets are still good enough for disproving hypothesis. For relative analyses, both approaches being compared will be biased in the same direction, so the effect should net out in the comparison.

Bias
- crypto: biased upwards
- dataset of *current* S&P500 members: biased up by virtue of inclusion
- dataset with no delisted assets
- price data: always shows price actually traded at, not prices that you could have traded at

Assumption
- counts of days in a given period

Example
- VIX index is biased upward due to "convexity premium". But should be okay if it tends to be constant.
- Data artifacts from using SPY daily returns and RV based on 22 trading days.

#### Thinking about shape of your data

What does each record in your datasets look like?
- How can records be joined or merged together - what are the dimensions or keys? What should be along the rows and columns?
- What do we want our data to look like to enable easier analysis?
- We want to align the option IV over next 30 days with RV over prior 30 days, i.e. joining the two by date. So we end up with columns like: date, SPY, RV of SPY, VIX, VRP, Next Day VRP. This makes it easier to see whether higher (lower) levels of SPY RV tend to be followed by higher Next Day VRP.
- If the initial results look promising, consider other explanation - is it due to mistakes? Is there data leakage or data overlaps between the two periods being compared?




