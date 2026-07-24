# RW Pro Discord — #data-analysis raw transcript

- **Period:** January 1–31, 2026
- **Channel:** https://discord.com/channels/1368787013763072040/1368844739465707572
- **Message count:** 41
- **Extraction method:** Browser automation (Claude in Chrome) against the live Discord DOM, using Discord's `in:data-analysis after:2025-12-31 before:2026-02-01` search to bound the range, then scroll-and-merge extraction of the message list, trimmed to exact January boundaries. No channel activity before January 20 within the range — the month's traffic is clustered into four windows (Jan 20–21, Jan 23, Jan 28, Jan 30–31).

---

1/20/26, 8:40 AM | Ben: Hi All,
I was wondering if someone smarter than me can help me understand the difference between running the uvxy/vxz trade with Norgate Data compared to the RW data in the lab.  Is it due to Norgate Data being adjusted from day one where RW data is only adjusted for the period of the testing? Does the different scaling somehow affect it?

The earlier and later periods look similar (and they are pretty much the same since the last reverse split and prices are identical when comparing trades).  Things seem to fall apart in the Norgate Data part way through 2022 to part way through 2024 when it takes a dive.

I understand why we all use the same data sets in the labs etc, but just trying to reconcile the differences so I can see how it would affect my portfolio if I added it and ideally I would incorporate it into my current order generation pipeline which uses Norgate Data.

This is daily rebalancing with 2% drift.
---
1/20/26, 10:12 AM | robotkris [reply]: Can you post a sample of the data you're comparing to?
---
1/20/26, 10:30 AM | Ben: I extracted the norgate data and dropped it into a pickle file
---
1/20/26, 11:16 AM | Ben: Hang on, I just plotted both and they are the same for each symbol.  Let me check which close I extracted.
---
1/20/26, 11:21 AM | Ben: Here is the norgate adjusted close series
---
1/20/26, 12:08 PM | Ben: Sorry, I think I confused myself.  Realtest uses unajusted prices and since they are reverse splits adjusted should be larger further back (even though I knew this I kept seeing the large numbers and my brain automatically said unadjusted).  However, this is fine for trade simulation but not for return calculation as returns will be distorted.
---
1/20/26, 12:10 PM | Ben: since UVXY has significant decay this will distort the equity curve if Realtest is using the unadjusted price series to calculate returns and simulate trades
---
1/20/26, 12:11 PM | Ben: sorry just thinking out loud now trying to get it straight in my head!
---
1/20/26, 2:08 PM | Ben: All sorted now!  Comes down to how realtest calculates data referenced in different sections with respect to adjusted and unadjusted prices.  Sorry if I wasted anyone's time, I have lost many hours across days trying to figure it out!
---
1/20/26, 2:41 PM | Ben: I have been looking at adding the UVXY/VXZ and vix basis to my main portfolio.  Correlations with my other strategies in the past are on the lower side.
---
1/21/26, 6:37 AM | TradeQuantiX: Hey Ben, I'm new to the course. Are these strategies all within RW Pro?
---
1/21/26, 9:28 AM | Ben [reply]: Hi @TradeQuantiX ,  no they are not.  Tactical Asset Allocation is essentially the Risk Premia Harvesting strategy in RP Pro though.  VRP is the vix basis trade in RP Pro and uvxy_vxz is the vix calendar spread in RP Pro.

The rest are different.

IDX_MR is just a mean reversion trade on Nasdaq.  Pretty simple rules.  Mean Reversion is a group of 5 or so long and short mean reversion strategies across different universes such as Russell 1000, Russell 2000, NASDAQ or all listed stocks (with a liquidity filter).  Again these are very simple strategies.  Generally one main rule plus liquidity filter.  Maybe a trend filter.

PEAD is post earnings announcement drift.  This was a group of features, many derived from how I traded earnings discretionarily, applied machine learning and then ranked based on the predictions.  Rotates weekly.  Long / short.   It has performed ok so far but I am just about to undertake a complete review to incorporate some of the analysis learnt from RW / RW Pro.

Momentum is 3 technical momentum strategies.  Really simple rule plus a trend filter.  Rotates monthly.  Long only.

Value Momentum is a combination of technical momentum measurements and value features.  I then applied machine learning and rank based on the predictions.  Long the top n and short the bottom n.  Rotates monthly.

ST break.  Short term breakout.  Based on a handful of ETFs.  All intraday with MOC.  Long / Short.
---
1/21/26, 9:30 AM | Ben: @TradeQuantiX I have only been here a few weeks myself and am loving it so far!
---
1/21/26, 9:37 AM | TradeQuantiX: Very cool Ben nice work! And thanks for sharing. I'm always interested to hear about what people are trading
---
1/23/26, 9:00 AM | Rachit: do either of these look like an interesting relationship ?
---
1/23/26, 10:20 AM | TradeQuantiX: Knowing nothing else, looks like higher volume = positive returns
---
1/23/26, 10:21 AM | TradeQuantiX: What's the gist of the idea?
---
1/23/26, 10:58 AM | Rachit: hmm yeah but with some reversion on the lower end ?
just looking at volume effects in crypto
---
1/23/26, 1:36 PM | robotkris: Yeah it does look interesting. With this stuff, you want to be on the lookout for anything that looks non-random.

Here, you've got lower returns associated with lower values of yoru factor and higher returns associated with higher values.

Is it a nice, clean, monotonic relationship?

No...

But it certainly looks non-random to me.

Potentially something interesting in buckets 1 and 2 - suggestive of slightly higher returns on very low volume?
---
1/28/26, 2:24 AM | neeravbm [reply]: @Ben Where do I find about these strategies and the corresponding notebooks that you mention in RW Pro? I am finding a much harder time accessing RW Pro info from one place.
---
1/28/26, 6:33 AM | Ben [reply]: I use the dashboard https://github.com/RWLab/rw-portfolio  and the index of strategies page https://robotwealth.com/index-of-strategies/.

Try the dashboard first as that is the recent info and comparison of strategies then the index if you want to run through all the past lectures and building of the strategies.
---
1/28/26, 11:53 AM | neeravbm: Thanks, @Ben !
---
1/30/26, 5:30 AM | Matt G [reply]: This is very interesting @Ben  thanks for sharing.  The correlation in drawdowns is a neat idea, I guess to look how correlations align when things go bad, right?  But how do you filter to just the drawdown periods in your dataset for that correlation?  When more than half the strategies are in drawdown or something like that?  I'd like to borrow your idea for my portfolio if I may.
---
1/30/26, 7:59 AM | Ben [reply]: I use a program called RealTest for portfolio analysis and how different strategies affect the combined portfolio (obviously knowing that it is based on the past and the future may be different).  So when I add a new strategy I look at the correlations, volatility of the strategy and contribution of volatility to the portfolio, max drawdown, CAGR, sharpe, etc.

It is a pretty handy piece of software created by Marsten Parker (from one of the more recent Market Wizards books).  I also use it to generate orders for my strategies each day.  It is really quick.

Screenshots as some examples.
---
1/30/26, 8:30 AM | Samurai35: That looks pretty slick. I'm curious to check it out. What is the learning curve like?

Does it work naturally with the way that we trade in RW or do you have to do some hacky things to make it work? I'm thinking things like vol targeting and trade buffers.

What does your daily workflow look like with trading?
---
1/30/26, 9:11 AM | Ben: @Samurai35  So far, from the RW strategies I have added uvxy/vxz, vix basis and just tested window dressing yesterday, all pretty easy to  code up, including buffers where appropriate.  If you get stuck someone has made a ChatGPT helper.

There are a tonne of example scripts of example systems that can assist and the forum is very helpful, including Marsten Parker who always goes out of his way to resolve any issues you may have.

The coding language is fairly straight forward and easy to learn.

So for the portfolio above, which can include multiple strategies in each of those groups that trade different timeframes (e.g. intraday, daily, weekly or monthly), I import the updated end of day data from Norgate (you can use yahoo or other providers)  which takes about a minute, I press orders to generate orders, which takes about 15 seconds and might include 100 orders, I then log into IBKR, open Orderclerk and hit transmit, which takes about 5 seconds.  I then repeat for another portfolio of strategies in a different account.

For strategies that are a bit more complex, e.g. where I am using a machine learning model, I run that in Python and RealTest imports the values from csv and integrates it.

There is a free trial and Enlightened Stock Trader offers a free RealTest course which I have heard is really good.

I have to run at the moment but I will post some more example  output and reports later if you are interested (and if allowed on the forum - I have no affiliation, just a happy user)
---
1/30/26, 10:23 AM | TimExcellent [reply]: Was looking at RT last week, if you use one IBKR account and different strategies via RT can it track the different strategy "portfolios" in the one account… notice you said you have another account as well - so just curious if it adds this feature
---
1/30/26, 10:46 AM | bdkoepke: That's more commonly known as sleeve accounting, where that gets tricky is when you have corporate actions. I'd be curious to learn how they handle that.
---
1/30/26, 10:47 AM | bdkoepke: Is anyone aware of a good data source for international options (equities primarily), and ideally also futures options? I'm aware of orats for US only, and csidata has futures options but their last price is contrived ('last' could have been executed hours earlier...).
---
1/30/26, 10:50 AM | bdkoepke: Also, are there any countries (other than the US) that extensively use XBRL for fundamentals data? In Canada we have Sedar which is absolutely terrible unstructured PDFs, but so many securities are cross-listed the coverage isn't too bad.
---
1/30/26, 1:19 PM | TimExcellent [reply]: No I've resigned to using orats and ETFs to build a picture of commods
---
1/30/26, 1:29 PM | TimExcellent: Would love Hong Kong stock and options - like what MidKnight says
---
1/30/26, 3:02 PM | Ben [reply]: In theory I could create one large portfolio for it to track using different accounts and balances, even rebalancing between accounts at different intervals.

At the moment I have 2 portfolios of strategies for stocks High Octane - I just revamped this and cut the number of strategies down to 5 long and 2 short all using the same capital and leverage, all mean reversion that enter intraday on limit orders and close that day with a MOC order.  RealTest tracks these strategies separately and shows a combined total.

Quantifiable Alpha portfolio is my main portfolio and the strategies can all be tracked individually or as combined strategies and then as a combined portfolio if that makes sense.  These are all different, some daily, weekly and monthly.  In this portfolio I have:

Tactical Asset Allocation - just the one strategy
,
Mean Reversion - represents 4 long and 2 short strategies from memory.  I group this but could track separately.
,
Momentum - 3 long only technical momentum.  I track as one strategy but could track separately.
,
Value Momentum - long / short
,
and some others but you get the drift.
,

Some screen shots from the different portfolio's live trades for example.  Whilst Quantifiable Alpha tracks both strategies and groups of strategies, High Octane just tracks strategies.  Probably overkill but just as an example of how you can configure things differently.  You can also place different constraints on different groups of strategies.
---
1/30/26, 3:18 PM | TimExcellent [reply]: thats pretty neat thanks!
---
1/31/26, 9:31 AM | alvin [reply]: I love RT!

The only issue I have is when I have a certain idea and unlike Python which is very well documented and popular, Gemini and Claude cannot give me the code I want for RT. Even when I've gave them all the example codes and documentation for "learning" they'd spit out some gibberish that even fails the syntax checks..
do you vibe code this or you write every line yourself?
---
1/31/26, 11:58 AM | Ben [reply]: A mixture of both.  Sometimes I need to vibe code it a bit when it is more complex.  Search the forum for Realtest GPT, I find that is usually pretty good and if not I just feed it some of the things in the RealTest guide and it figures it out.
---
1/31/26, 2:38 PM | Dan [reply]: Also love RT!
I think python is complex enough and needs enough lines of code to do things that AI helps alot.
With RT though - once you get used to it you should find it simple enough to open a template and plug in the bits fairly quickly I think.
I can see an idea online and often have a simple test to disprove it done in 5 minutes, just from opening a similar script and changing a few things.
Of course the more complex things such as we see in academic papers are a bit more difficult.. and doing a portfolio of many strategies is a larger job too.
---
1/31/26, 3:16 PM | alvin: When it gets a bit more complex I tend to lean towards Python as I can spam the hell out of AI tools to cross check if the logic is right. With RT language I'm pretty much in the blind (for more complex requirements)
---
1/31/26, 3:22 PM | Ben [reply]: AI tools definitely get a good workout from me!
---
1/31/26, 3:48 PM | Dan: I do love cursor, though it's been more of a data cleansing, transform and integration assistant for me so far.
Looking at all this RW Lab stuff I'll have to get into more python for research
---
1/31/26, 4:52 PM | Ben [reply]: I have found Augment code to be really good, especially for large projects
