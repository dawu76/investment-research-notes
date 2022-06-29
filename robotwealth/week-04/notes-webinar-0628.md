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

Avoid magical thinking like "let winners ride and cut your losers." Question assumptions.

Folkore: "Stop losses cap downside, lessen my slippage"
- Only if you stop trading - at some point, you have to get a new position on ...
- But when would it be helpful? When the position is more likely to keep going down. But if it's as likely to keep going down as it is to be going back up, then it won't help. So to be effective, we need to actually make a prediction about how price will move when it gets to the stop liimt level.

Recent example: "Vol has been realizing significantly over (under) implied vol, so it's good to be long (short) vega."
- Translation: "We've recently seen certain conditions, so we should put on a trade that assumes the future will be like this recent past."
- Question: on what time frame will volatility "cluster" and when will it mean-revert?

Uncovering implicit assumptions
- Look at actual realized volatility over a past period (e.g. past 30 days), look at option implied volatility (IV) over next 30 days. Compare the two over recent periods to see if options were selling for too cheap.
- Actual realized volatility will continue being higher than implied in the near future because it was like this in the recent past
- Break the assumptions into parts if necessary so that they can each be tested.
- Come up with testable assumptions: Realized volatility (RV) > IV, then options were cheap. If by this measure, they were cheap in the last period, they're more likely to be cheap next period as well.
- Find the simplest, most direct way to test the hypothesis; don't throw in additional assumptions or conditions. E.g. just because options are selling for "cheap" doesn't mean we'd be profitable trading them. More direct condition to test: if option is cheap in period T, it will tend to be cheap in period (T+1). In other words, option prices exhibit auto-correlation or trend.

---

#### Getting data

Realities of working with data
- dealing with new datasets is a hassle
- cleaning data is cumbersome due to common issues like timezone issues, missing data, adjusting for asset specific issues like splits, dividends, etc
- don't get hung up on collecting all the relevant data upfront: it will end up being a waste of time if the hypothesis turns out to be utterly wrong
- don't let this turn into a big data engineering project

Getting to an answer more quickly
- Don't solve all your problems at once
- Use the easiest, lowest frequency data that is sufficient to prove or disprove your hypothesis
- We're after "stonkingly obvious" edges, not subtle effects that require pristine data
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

---

#### Thinking about shape of your data

What does each record in your datasets look like?
- How can records be joined or merged together - what are the dimensions or keys? What should be along the rows and columns?
- What do we want our data to look like to enable easier analysis?
- We want to align the option IV over next 30 days with RV over prior 30 days, i.e. joining the two by date. So we end up with columns like: date, SPY, RV of SPY, VIX, VRP, Next Day VRP. This makes it easier to see whether higher (lower) levels of SPY RV tend to be followed by higher Next Day VRP.

If the initial results look promising, consider other explanations
- is it due to mistakes? Is there data leakage or data overlaps between the two periods being compared? Even having a day's worth of overlapping data will overwhelm any other effects.
- Is there conditional bias in the VIX?
- Are there calendar anomalies in how we calculated RV, e.g. due to inconsistencies in how we defined time period in the backward and forward-looking periods? For example, trailing 30 days vs. future 22 trading days.
- Be paranoid, not hopeful. More likely you've made a mistake vs. finding a strong effect.
- Next, how do we make this finding actionable? How/what do we trade to take advantage of this effect.

---

#### Elaborating on navigating chaos in markets

What are open-ended funds?
- A fund manager creates 2 companies - the actual fund, and a company to manage it. Investors put in money, say $1K, and he creates 1 share x $1K. Suppose the fund's NAV goes up to $1.1K.
- Investors buy and sell shares from the fund, transactions occur once daily at the NAV.
- New shares are created when investors put in money, and destroyed when investors want to take out money.

What are close-ended funds (CEF)?
- Funds are created via IPO. May trade close to NAV, but during financial dislocations, NAV discounts can grow to 20% to 30%.
- For CEF, the supply of shares is fixed; investors can't buy or sell shares from the fund itself, so shares are not getting created/destroyed unlike in the case of an OEF; they can only do so among themselves. So the NAV and the value of the shares can be decoupled. Suppose a CEF's NAV goes from $5K to $6K. The shares may still trade at the lower price unless we can find someone to trade at the higher level.
- Suppose a new investor is willing to buy at $1.3K per share. The NAV wouldn't change but the price per share would be higher. As a result, the shares trade at a premium to the NAV of 8%. This is easier for the fund manager because they don't have to think about creating and destroying shares.

Looking for NAV discounts in CEFs
- happens rarely but during dislocations, we may see big NAV discounts of 20+%, e.g. we saw this recently with CEFs for corporate bonds as investors were selling off any bond assets.
- Use CEF Connect to screen for NAV discounts during times of economic distress and forced selling.
- But don't worry about doing this on a regular basis. During benign economic conditions, it's not worth looking for CEF NAV discounts since you'd be competing with hedge funds. Check if 
- Warning: funds can be discounted due to understandable reasons - bad management, high expenses, illiquid assets. Tax implications can be a hassle as well.

Stink-bids
- This is a bid well below current market prices, where you're providing liquidity to anyone who wants to get out at any price, e.g. during forced liquidations. So you're trying to take advantage of these forced sellers.
- Example: $IVT, an "mortage REIT". They layered orders starting at 25% below the current price based on an educated guess that there could be forced selling down there. The reason is that a few of the larger REIT EPTs had stricter mandate criteria, and during the 2020 Covid crash, $IVT fell out of the mandate criteria. So during the forced selling, a few of the stink-bids for $IVT were executed. 

---

#### Questions
- Where can we get free or cheap data? It's been getting harder to get free financial data ...
- How do we scan for stocks based on certain criteria? What we really want is a way to screen for characteristics that are positively associated with expected returns. Start with the analysis here.
- What is "carry-whoring"? Activities that tend to make a bit of money most of the time but occasionally lose a lot.
- Why did you say this time-series of basis, colored by "full factor decile sort", was "stationary-ish"? It means the distribution of outcomes over different periods looked largely the same.
- Can you explain the "composite score" based on 50% basis ratio decile, 25% VIX level decile, 25% VVIX level decile? The point of this score was to identify when we should go long or short volatility. The effect is noisy, but it was better to be long volatility for lower levels of this score, and short volatility for higher levels of this score. This is a simple but common tactic in trading research - reduce a bunch of measures into a sinle measure that we then rank.
