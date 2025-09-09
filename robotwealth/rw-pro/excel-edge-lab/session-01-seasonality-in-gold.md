## [Excel Edge Lab session 1](https://robotwealth.com/courses/excel-edge-lab/lessons/0-welcome-logistics-and-a-taster/topic/live-session-1-a-simple-seasonality-effect-in-gold/): Exploring a simple day of week effect in gold

**Key idea**: Use quick and dirty analysis to disprove the idea that a strategy is easily tradeable. Don't waste time on a very precise, thorough analysis of a strategy that isn't reliably profitable.
- Walkthrough of [Excel workbook](https://docs.google.com/spreadsheets/d/1BKycC7ivUsPX6MRcVNTgivI_irY5i5vK/edit?usp=sharing&ouid=110912496236866475625&rtpof=true&sd=true) from session 1.
- Don't be prissy with your analysis.
- Don't jump into backtesting a complicated version of a strategy. Look for broad, coarse effects at the outset.

Populating the 'prices' data tab
- inputs specified by user: Ticker (GLD), StartDate (1/1/2004), EndDate (9/9/2025)
- columns populated by API: date, open, high, low, close, volume, adjclose
- calculated columns: log-returns, dow [day of week], month, year, long/short-position, long/short-returns,	long-only-position, long-only-returns

Calculated formulas in 'prices' data tab
- `=IFERROR(LN(Prices!$H8/H7),0)`: daily logged returns; use logs so that cumulative returns = sum of logged returns
- `=TEXT(Prices!$B8,"ddd")`: to get day of week of the dates
- `=MONTH(Prices!$B8)`: to extract month from dates
- `=YEAR(Prices!$B8)`: to extract year from dates
- `=IF(Prices!$J8="Fri",1,IF(Prices!$J8="Mon",-1,0))`: 1 = go long on that date, -1 = go short, 0 = flat
- `=Prices!$I8*Prices!$M8`: daily logged returns of strategy that goes long/short/flat depending on DOW
- `=IF(Prices!$J8="Fri",1,0)`: 1 = go long on that date, 0 = flat
- `=Prices!$O8*Prices!$I8`: daily logged returns of strategy that goes long/flat depending on DOW

Is it a good idea to buy gold on Thu and selling it short on Fri, and covering it on Monday?
- We can quickly check this adding a column to the daily log(returns) table in Excel - let's call it 'position' - that equals 0 when flat, +1 when long, -1 when short, and calculating the sum of `position * log(return)` over time, segmented by dimensions like day-of-week or year. This tells us the cumulative return from going long / short that asset on certain dates over a period of time.
- We expect tradeable effects to decay over time as they become known and more people try to take advantage of them, and possibly front-running them, causing the effect to appear earlier in the week, before disappearing. Some modest decay in a strategy actually gives us more confidence that its excess returns actually exist.
- How stable is this effect over time? Do we come to a different analysis if we focus on particular portions of the time period?
- Excess returns from day-of-week trading in gold has decayed in recent years, with some negative years. If we filter the pivot table to just 2019+ years and look at the bar charts of returns, we wouldn't conclude that there is any reliable excess return. Ask whether there is a logical reason why this strategy could still exist - if so, maybe it's worth sticking to it or tracking it, as it may return to positive returns. What would you expect to see if the effect was still tradeable? It would be reasonable to see some decay, but with a flater negative slope over time.
- If there is an understandable reason for a strategy's effect to exist (e.g. it's difficult / inconvenient to trade), then it may be worth allocating funds to it even if it hasn't done as well in recent years. But if you don't understand why such an effect should exist, and it would a signficant amount of time for you to perform enough research to really understand it, then cross it off the list and spend your time digging into more promising leads.
- Regarding the 'skewness' of returns by time unit - check this by aggregating returns by annual / monthly / daily units. Ideally the strategy's returns are not dominated by a few outlying data points.

Viewing the equity curve
- What if we calculated a total return as a 'running total' across years? The resulting annual equity curve would show a flattening in the later years.
- If we convert the pivot table from monthly -> daily and recreate the curve, then we can see a more obvious degradation in the returns in the later years, as the curve has a negative slope in some portions.

The 2nd dimension for this analysis: the asset dimension. E.g. repeat it on another asset that is possibly similar - e.g. silver, gold miners, etc.
- In the Excel file, get the daily prices for $GDX instead of $GLD. We see a similar pattern - negative returns on Mon, positive returns on Wed and Fri. Then change the row labels from day of week to year - do we see a similar decay in strategy returns over time? Yes - returns were more consistently positive in the mid-to-late 2000s, but have been mixed in recent years (and very negative in 2020). So applying the strategy to $GDX does not seem like a good idea either.
- For other asset classes such as stocks, this asset dimension could represent different tickers.

What if we felt the effect still existed to some extent and wanted to trade a simpler version of it - e.g just going long on Friday and staying flat on the other days?
- Then compare this to the even simpler strategy of just staying long all the time.
- In the data table, define a new 'position' flag that equals 1 on Fri, 0 on other days, and calculate strategy returns as sum of `position * log(return)` as before.
- Create a pivot table with dates as row labels and the running total of strategy returns - `sum(position * log(return))` - to produce a daily equity curve.
- Follow-up question: Are the positive returns due to the strategy or due to the underlying asset doing well during this time? To check this, add a new column to the pivot table containing the daily `log(return)` series from holding the asset all the time ($GLD). By plotting the two equity curves together, we can get a sense of whether the strategy added any value over a simple buy and hold approach. Answer: The underlying asset has been more volatile, but has performed a lot better, especially in recent years. If you want to be long gold, then just stay long all the time.

---

### Summary of effect

The effect looks clear and obvious when we first look at it. (But it should because someone told us it existed!)
- But starts falling apart the more carefully we pick it apart. This is nearly always the case. We see degradation of the effect over time, and we don't really understand it. 
- I'd be more ok trading something I didn't understand if it were more consistent over time and didn't require such active trading.
- On the face of it, it looks like it performed pretty well recently. But that's mostly because the asset has done well recently. I wouldn't trade this - but I don't think it would be unreasonable to add to a GLD position on Thursday close and reducing at the end of the week if you wanted to be long anyway.

What have we learned generally? A lot of the patterns we saw here are patterns you always want to use
1. Try to disprove the idea as quickly as possible
2. Think about what else could be causing this effect (like luck, for example)/
3. Look for stability along time and asset dimensions/
4. Wrestle with causality and try to pick apart cause and effect as much as possible
5. Think about the practicalities of actually trading it vs something simpler (like just being long gold)

The benefit of this kind of analysis is we can repeat it easily on other assets - for example bitcoin! (But be careful to avoid snooping problems!)

Homework: repeat the above process on BTC, ETH, or some other asset
- does the effect still exist?
