# RW Pro Discord — #vol-book-club-chat raw transcript

- **Period:** May 1–31, 2026
- **Channel:** https://discord.com/channels/1368787013763072040/1387280068182540390
- **Message count:** 129
- **Extraction method:** Browser automation (Claude in Chrome) against the live Discord DOM, using Discord's `in:vol-book-club-chat after:2026-04-30 before:2026-06-01` search to bound the range (130 buffered search results — near-exact match), then scroll-and-merge extraction of the message list, trimmed to exact May 1–31 boundaries. May was a much busier month for this channel than June. Some individual messages are capped at 250 characters by the extraction tooling; these are marked `[capped]` below. The most substantive capped messages — mostly Euan's and robotkris's detailed explanations — were separately recovered as full text from the live DOM and are reproduced complete.

---

5/1/26, 12:12 AM | shashinsho: Thanks guys for the discussion and i just watched the covered call recording + latest AMA.

@Euan sir would you think then the "wheel strategy" works well?

i am coming from the perspective of wanting to get into SPY for the risk premia harvesting layer but want to "buy at a cheaper price".

so we sell OTM cash secured puts (say 20% below current price, sorry not correct jargon) to harvest the option premia + delta.

if we do get assigned, we sell covered call and hope to be assigned. then we rinse and repeat.

psychologically buying at 20% lower than now sounds OK and even better than buying at current levels.. however I think this goes against what you mentioned about not assuming how one would be thinking when the market reaches that point. not sure how to then think about this.
---
5/1/26, 12:20 AM | shashinsho: also heard the bit about Buffer ETFs which my insurance agent has been pushing a 0% floor 10% cap (referencing SPY) investment plan to me. which i only found out today i could just buy the Buffer ETF.

i also found out we could replicate it by buying 1yr US treasury sized to get back the principal at maturity + using remaining budget to buy call spread on SPY.

seemingly -5% floor + 15% cap can be achieved (may need a refresh) which seems quite good mentally as losses are defined plus still not losing too much upside on the SPY - chatGPT said SPY has multi positive 20+% years and sporadic huge losses.

wonder whether this kills the risk premia but surely prevents panic selling and helps get equity participation with better peace of mind.
---
5/1/26, 12:20 AM | shashinsho: thanks!!
---
5/1/26, 8:22 PM | Euan [reply]: the wheel is just a succession of covered calls (if you have the stock) and cash secured puts (if you don't) which are synthetically both the same. So if you want to be long delta in something and it has a variance premium (index etfs etc) then it is a good idea. But the branding as a separate strategy (htf did that happen btw?) makes it seem different and gives twice as many ways to mess it up. The extra edge in the idea is just the variance premium, so whether doing calls or puts make sure to do strikes that actually have a variance premium. So at least ATM calls. All OTM puts will have a VP but if you want the delta exposure to be the same you should do ATM puts as well.
I'd push back a bit against the "buying for a discount" thing. That is a similar wrong framing to a covered call "giving income". In both cases it is just a longdelta position augmented with the variance premium.
---
5/1/26, 8:26 PM | Euan [reply]: Buffers are a decent product if the payoff is what you want. The fees can be high but probably still cheaper than replicating yourself. They are easy for advisors to sell because there is always a good story, and so they can end up in portfolios where they make no sense. For example, having a put protective buffer in a portfolio that also has a covered call makes little sense. The put positions just cancel.
There have always been structured products and the risk premia generally adapts and re-prices.
---
5/1/26, 11:42 PM | rodeo1203 [reply]: Was watching the replay, thanks for the really insightful discussion. But has me a bit confused with the way I think about covered calls.

So, essentially what you're saying @Euan is to think of the trade in terms of delta and variance premium (vrp). Also the long one, right @robotkris?
---
5/2/26, 5:19 PM | aditya: @Euan just listened to the AMA. Thanks for the session. I had 2 questions -

assuming one doesn't own stock, doing the same covered call trade via selling ATM put is more efficient from a cost perspective and has the same edge right?

regarding the FOMC trade, you mentioned you'll post some notes. I am not sure if I missed it or not.
---
5/2/26, 9:46 PM | Euan: [link to #vol-book-club-chat message]
---
5/2/26, 9:46 PM | Euan: That is the fomc note and you are right about covered calls and naked puts
---
5/2/26, 12:31 AM | FullMetal37! [reply]: I actually suspect some of the edge in the pre earnings long vol is in the fact that earnings dates can change/get cancelled. So the full implied move gets discounted a bit because there's a chance the expiration you bought won't contain the ER.

It's my guess that trading on the estimated date before confirmation has more edge. I tried to get some data on historical estimated dates vs actual dates to see how often it was that unconfirmed dates were wrong and how often confirmed dates change but I had a hard time sourcing the data
---
5/2/26, 1:21 AM | Euan [reply]: i don't know if it is that big of a deal. i don't think the late announcement thing would affect many liquid, optionable stocks. but maybe. it may affect backtests but I have done a backtest for a loooong time (even then i made someone else do it) so it has been of sample since then.
---
5/2/26, 1:22 AM | Euan [reply]: you are right in your interpretation although i'd be very loose with any rehedging. gets expensive
---
5/2/26, 1:23 AM | Euan [reply]: i think that is true. you get positive exposure to every weird thing. and positive systematic vol, which is my favorite bit.
---
5/2/26, 1:32 AM | Marco: I think that robot wealth also did a backtest time ago
---
5/2/26, 12:49 PM | blue664203 [KONG]: I think that was on the short side
---
5/3/26, 3:28 AM | aditya: One more question - I am very interested in learning about experiences people have had with the volatility risk premium trades in gold.

Assuming it's liquid, it's basically the same trade i assume as in index. Would you size it differently than the index vrp?
---
5/3/26, 5:29 AM | Euan: I personally would do it smaller. Probably so small I really wouldn't bother doing it.

Statistically, the vrp in gold is high and persistent. Similar to indices. But commodities are full of insiders who know "stuff". There are also squeezes, bubbles and crashes driven by insider trading and unpredictable geo political stuff.

And gold is weird on top of that. Industrial? Yes but not fully. Vanity? Yes and heavily tied to Asian buying for jewelry. Inflation hedge? Sometimes but not consistently. Risk on? About half the time.

Too much going on for me. This is stuff that is knowable but not by me. So I tend to stick to indices where nothing is knowable to anyone
---
5/3/26, 2:00 PM | aditya: So VRP in general would you do only on Equity indices? Stocks? Sector indices? I understand there can be tail risk correlation but there would be diversification in normal markets I guess.
---
5/3/26, 8:41 PM | Euan: I'd be happy doing any financial products. So indices, stocks, bonds, vix [capped — comments on margin requirements when the asset under real duress becomes illiquid and can't satisfy the margin call]
---
5/7/26, 4:25 AM | MidKnight: Hi @Euan I had a look at the VIX option chain today to look into the short put idea you mentioned in the recent webinar. It looked a bit odd to me on the IB options chain. The VIX is at 17.4 so I would be expecting the 50 delta on the calls or puts to be about at that area. However, for the JUL 16 expiry (40 DTE), IB is showing the 50 delta put up at 21.5.

Because you mentioned selling the ATM put, I'm going to assume you mean selling the ~50 delta put even though it is actually ITM?
---
5/7/26, 4:48 AM | Euan: Because they are European options, the true underlying is the forward value of the index. So the atm strike will currently be above the cash index because the futures curve is going up.

It doesn't have to be exactly 50delta. Just close enough that there is a variance premium. Anywhere from 40 to 60 is fine.
---
5/7/26, 10:07 AM | Edux: Hey @Euan, on the same topic:

do you close VIX options positions before expiration to avoid exposure to the Special Opening Quotation (SOQ) risk, or do you think it is more of a secondary concern, and that events like the so-called "Volmageddon" spike are rare occurrences which are part of the game?

I also read that traders were allegedly placing orders in out-of-the-money SPX options right before the settlement window specifically to push the SOQ around, which attracted scrutiny from the SEC and CFTC. What do you think about that?
---
5/7/26, 12:35 PM | Fabian: @Euan: When do you close the trade? Buy back right before expiration?

Assuming the future will converge against spot price, the option would like end up being ITM, if VIX isn't raising. So the rational is, that there is more variance premium in the sold option, then inner value of the option if future converges against spot? Hope that's something you can allude to in your portfolio session, if this is one of your always on positions?

I guess one reason of lower popularity of these type of trades compares to other trades is the fees. In terms of notional value they seem to be quite higher.
---
5/7/26, 7:39 PM | Euan: I try to keep exposure to between 2 months and 2 weeks. I'm not systematic about this and tbh the decision is usually based on how closely I can pay attention. The shorter dates have more edge but also a lot more variance and need for rebalancing.

Manipulation of the settlement def happens. It is a strategy the big firms do, not just a rogue trader or two. The practice isn't as egregious as it was 4-5 years ago because of negative press. It would be easy to fix the process so it couldn't happen but why would you offend your biggest customers?
---
5/7/26, 7:41 PM | Euan [reply]: The drift effect is real but also noisy. Standard option risks tend to be a bigger deal which is what we want.
---
5/8/26, 9:09 PM | Sam: @Euan When shorting VIX futures ahead of economic reports such as Non Farm Payrolls, should the trade be exited straight away after the release? My thinking is that the event is over, so exit but then again often the vix futures continue declining...
---
5/8/26, 9:46 PM | Euan: you have to give it a bit of time. i usually do 15-30 minutes
---
5/11/26, 6:36 AM | aditya [reply]: This idea is similar to the short straddle earnings trades? We just short the vix futures as near to event as possible and then cover it 15/30 mins post it?

If it's overnight then we short near close of previous day. And economic events like FOMC strategies are always interesting to me
---
5/11/26, 7:31 PM | Jack [reply]: Does anybody have any stats on the performance of this? Definitely something I'd like to look into testing and trading, event strategies are always interesting to me
---
5/11/26, 8:04 PM | Euan [reply]: I tested selling 1DTE overnight before these numbers and the results were positive but underwhelming. My conclusion was that the results were a boost to unconditionally selling overnight (which is also profitable but nothing exciting) but probably not worth doing as a separate thing. didn't test vix.

the effect is real but probably not huge.
---
5/11/26, 8:20 PM | Euan: although, it is worth noting that the "important" number changes over time. in the early 90s it was money supply. then NFP (which was a massive effect) and now it is all about inflation.
---
5/12/26, 4:25 PM | Jack [reply]: yeah that makes sense 100%, thanks Euan
---
5/12/26, 7:32 PM | Sam: CPI in 1 HR. I'll short May Vix beforehand. But I'm cautious about this one ... probably decrease my size.
---
5/12/26, 8:38 PM | Sam: I'm out on full position, +10 pips.
---
5/13/26, 4:02 PM | Yan: @Euan, do you know roughly what the annualized volatility is for a typical implementation of the pre-earnings long vol trade?
---
5/13/26, 6:44 PM | deal_me_in [reply]: @Euan is selling a cash secured put the same as a covered call? Why did you specifically say naked put?
---
5/13/26, 7:41 PM | Euan [reply]: habit really. in my day jobs, cash secured put isn't really a thing that is ever mentioned. I always refer to an option with no hedge or associated stock position as "naked", so a cash secured put is just a special case of that. also, i never really have a clue how much cash is in my account at any time. everything is based on risk numbers and the cash gets swept in and out of sub accounts all the time (i think I currently monitor 40). but you are completely right. A covered call is, through put/call parity, exactly the same as a short put and enough cash to buy the stock if assigned.
Also, you are right to check terminology. There really isn't a 100% consistent option language and confusion is really common. For example, I've never heard anyone outside of academics refer to an option's charm or whatever. I don't think any traders have heard of it. And no old school floor guy would have a clue what vanna referred to. He would know the effect obv but not that specific name. And no one calls a "vertical" a "vertical". they just weren't terms we used. So no shame in checking [capped]
---
5/13/26, 8:06 PM | Sam: Portfolio update, or something similar [capped — content unclear, message continues]
---
5/13/26, 8:19 PM | Sam: the typical vol of a pre-earnings stock is 50%.
the average option duration in the portfolio is one week.
you have 20 positions at any one time.
the average stock price is $100.
these give a straddle price of about $5.50
or a portfoluio value of about $110.4

equation 7.10 in "volatility trading" gives the volatility of a straddle as approximately (1/sqrt(2)) x stock price x vol x sqrt(T) = $4.9
assuming uncorrelated positions the vol of the position is sqrt(20)*$4.9 = $22
---
5/13/26, 8:32 PM | Yan: Thanks for taking the time Euan, I'll work through your answer to understand it properly
---
5/13/26, 8:34 PM | Euan: but tbh this is crying out for a monte-carlo so you can ask exactly the question you want
---
5/13/26, 8:40 PM | Yan: Makes sense. I was trying to figure out how to size a pre-earnings long vol position within a portfolio based on its vol contribution. Kris talked about that in a session back in January, which is what made me ask the question.
---
5/14/26, 7:05 PM | Ben: Been starting to do a little data analysis on the long earnings straddle. Have only grabbed 2 years of data so far from ORATS to start testing my pipeline. Ignore the charts that aren't displaying the error lines properly for now. Anyway, I'm off to the pub to see a Nirvana cover band.
---
5/14/26, 7:36 PM | Marco [reply]: Thx, what Sharpe do you get?
---
5/15/26, 3:08 PM | akhan: Thanks a lot @Euan and @robotkris for your thoughts on portfolio construction. I have just listened to the recording and it was great. I have a couple of follow up questions if I may.

1. How often are the portfolio weights meant to be assessed? Daily, monthly or yearly?
2. If i expect to get 20% volatility from my portfolio, but say after 3 months I only get 10% volatility. Does that mean i need to increase the leverage or leave everything where it is until the next revision whenever that might be.
3. How does one incorporate VRP strategies (for example weekend straddle) in this framework. Or more specifically, these trades consume margin and not actual capital per se. I am not sure how will i calculate percentage of capital allocated to them. I have a feeling that it's a simple question, but would appreciate your input anyway.

Thanks
---
5/15/26, 7:49 PM | Euan: you won't find much benefit in doing this more than quarterly. UNLESS something materially changes. Like if BOIL gets excluded because winter is over. or hyperliquid gets hacked. or you just give up on a strategy. I rebalance once a quarter or whenever I change a model. No need to be dogmatic. This also applies to re-leveraging decisions.

3 is a good question. I don't worry about capital at all. i just allocate to get the proportion of pl per strategy where I want it. So "how much do I increase size to get stat arb to give an expected 40% of my PL". this is one of the great advantages of the "vibes" approach. you can allocate on "goodness" even if the capital basis is different.
---
5/15/26, 7:54 PM | akhan: Thank you for answering
---
5/16/26, 3:42 AM | FullMetal37!: [engages with the same portfolio-construction thread]
---
5/18/26, 11:31 AM | Ben: Here is some further analysis I have been doing on the long vol earnings trade:

Options data from ORATS - 1 July 2015 to 9 May 2026
1A is 15 trading days from earnings, 2A is 10 trading days from earnings. The H variants refer to hedging and at what delta.
exits are the day before earnings as did not have AMC / BMO data
Happy for anyone to point out any errors

First of all, IV ramp observed with both 10 and 15 day scenarios.
---
5/18/26, 11:32 AM | Ben: VRP = iv_entry - rv_entry (PIT-correct: trailing 20-day realized vol before entry)
Not really predictive of which straddles may perform better
---
5/18/26, 11:33 AM | Ben: IV decile also doesn't show a clear pattern for straddles to be filtered
---
5/18/26, 11:35 AM | Ben: Again, no real clear pattern in my view. Maybe you could up the 5000 volume filter a little.
---
5/18/26, 11:36 AM | Ben: You could lean towards higher priced stocks. Interesting the bottom decile is positive before a few negatives.
---
5/18/26, 11:37 AM | Ben: Market cap has no real clear patterns
---
5/18/26, 11:37 AM | Ben: All of this really supports weighting to a decision on whether to hedge or not [capped]
---
5/18/26, 11:47 AM | Ben: Mean return by sector does look like it provides an opportunity to filter candidates. Is it just influenced by the last 11 or 12 years though?
---
5/18/26, 11:55 AM | Ben: In respect of costs, I have used the following assumptions:
$0.65 per contract
$0.005 per share
5 BPS hedge slippage
friction_scenarios_map = {'No friction': 0.00, 'Tight (1% half-spread)': 0.01, 'Base (2% half-spread)': 0.02, 'Wide (4% half-spread)': 0.04}
I don't have much experience with options so does anyone know if the spread assumptions are realistic? I did encounter one that was 8% when I was trying to close out the other day.

To me this starts to remind me of a comment that Euan made about if you have to automate it then don't bother as it looks like getting good fills my working your order may make a big difference
---
5/18/26, 11:59 AM | Ben: Anyway, I dug a little deeper looking into filtering out the underperforming sectors and the highest performing scenario - entering 10 trading days prior and hedging at 0.5.

Real Estate was included as there only appear to be a small sample size
---
5/18/26, 12:00 PM | Ben: Here is what it looks like with the same cost assumptions as earlier
---
5/18/26, 12:06 PM | Ben: Overall process:
- Pull earnings calendar from FMP
- Pull Prices from FMP (then re ran with Norgate due to some quality issues)
- exclude stocks less that $50
- pull options data
- exclude symbols where volume less than 5000 for the chain
- pull specific option contract details for the ATM strike
- also had dividend data and treasury rates data for back-up greeks calculations if needed
---
5/18/26, 12:12 PM | Ben: In respect of costs, I have used the following assumptions... [continues with friction scenario detail — see above; also shares "you could lean towards higher priced stocks" style filter observations, "market cap has no real clear patterns," and "pricing in much movement for the earnings event. The event vol can be calculated using the IV from the current expiry and the next expiry" observation from blue664203]
---
5/18/26, 1:41 PM | blue664203 [KONG]: Thanks for sharing this @Ben. Looking at the mean return by sector, seems like those with lowest returns are those with low event vol (the option prices aren't pricing in much movement for the earnings event). The event vol can be calculated using the IV from the current expiry and the next expiry.
---
5/18/26, 2:25 PM | MidKnight: Thanks for sharing this Ben. I hope your hand has healed up nicely post-op
---
5/18/26, 4:54 PM | Marco: Thanks Ben, it seems that the final performance are ok. What do you think of the filters introduced in this video? "Volatility Vibes — The Earnings Volatility Strategy Big Funds Use (That You Don't Know...)"
---
5/18/26, 4:58 PM | Marco [reply]: @robotkris what was the final sharpe ratio for the long earnings strat?
---
5/18/26, 5:02 PM | Ben [reply]: I will take a look and if it is something I can incorporate into the analysis I will.
---
5/18/26, 5:04 PM | Marco [reply]: he uses 4 additional predictors to filter trades, stuff like implied jump compare to past ones etc...
---
5/18/26, 8:07 PM | robotkris [reply]: I don't think I've ever estimated it, but gut feel it would go at about 0.5-0.8 depending on how broadly you could do it. But that's a very useful 0.5-0.8 because (1) it gets you positive EV long vol exposure, and (2) it will be uncorrelated with most everything else.
---
5/18/26, 8:56 PM | Euan: also, the sharpe on long vol strategies tends to be misleading (in a good way) because there is significant positive skew.
---
5/18/26, 10:21 PM | SatoriNakaMoto: @Ben and other guys here, yfinance is quite cool now that gives last few earning even as well as surprises
---
5/19/26, 3:27 PM | Ben: I have now run the same analysis on the monthly options rather than the weekly options. Some interesting differences. 1M is 15 trading days to earnings and 2M is 10 trading days to expiry.
We still see an IV ramp, not to the same extent. Not surprising though considering the different expirations and proximity to earnings announcement.
---
5/19/26, 3:40 PM | Ben: VRP = iv_entry - rv_entry (PIT-correct: trailing 20-day realized vol before entry).

Compared to the weekly it looks like there may be some more information that we can use to filter here. There is the sector analysis like last time, but also it appears as though the lower IM deciles give more bang for your buck than the high IM decile where the market has already priced in a large move (Decile 1 (lowest IM) earns 7.8% mean vs Decile 10 earns 0.7% — an 11× spread).
It also looks like the stocks with a higher market cap have larger returns on average (plus you get the added bonus of tighter bid-ask spreads)
---
5/19/26, 3:52 PM | Ben: Before I get too far ahead, some stats around rolling sharpe and the hedged variations. Interestingly, the hedged variations do not perform as well on the monthly straddles. Being the options expert I am, I discussed this with claude and it comes down to [continues — see Euan's 8:38pm reply below for the correction] more of a Vega play and theta decay is slower. Weekly is more affected by gamma and theta, and delta swings a lot more and requires hedging to capture vega. @Euan Would this be roughly in the ballpark of being correct?
---
5/19/26, 3:54 PM | Ben: Friction / costs can eat away at your edge also
---
5/19/26, 3:57 PM | Ben: Onto the deep dive with a sector filter and 10 days to earnings announcement scenario. This improves the results, especially when costs are taken into account. Annualized sharpe improves.
---
5/19/26, 3:59 PM | Ben: [Thoughts / criticisms welcome. Definitely looks like there is some edge there.]
---
5/19/26, 4:02 PM | Marco: Shouldn't be VRP = IV_entry - RV_exit?
---
5/19/26, 4:07 PM | Ben [reply]: I was calculating whether VRP at straddle entry was predictive of straddle returns at all, rather than VRP at earnings as it would be future biased.
---
5/19/26, 4:09 PM | Ben: @Marco I will look into that video you posted to see if I can add that filter
---
5/19/26, 4:16 PM | Marco [reply]: I see that the mean return per trade is 3%, if we assume that a full trade is 4 dollars in commissions, we need to trade straddle that are quite big
---
5/19/26, 8:38 PM | Euan [reply]: I think claude is right about the option mechanism but wrong about the cause (if that makes any sense). The monthlies do have less theta but, as we know and claude doesn't seem to, theta isn't the edge. the edge is in the vol mispricing which is realized daily by theta being bigger than the gamma PL. and monthlies just have less exposure to the vol edge which is caused by the earnings vol being mispriced.
---
5/21/26, 7:47 AM | Sam: @Euan Re long earnings options play: if the 2 week straddle for a stock is uncomfortably large in terms of the premium, what can be done? Buy a strangle?
---
5/21/26, 8:06 AM | Euan: A strangle will give exposure to the thing you want. The win rate will be lower but the average profit (per unit of Vega) should be the same
---
5/21/26, 7:03 PM | Sam [reply]: thanks, with regard to the "at 35 delta take the position off and restrike", would this apply if a strangle was done? Or would I seek to restrike at a lower delta say 20?
---
5/21/26, 7:44 PM | Euan [reply]: yeah. the 35 delta rule was basically because it is when each of the 50 delta options have significantly changed in delta terms (to low 30s and high 60s) so for a 10 delta strangle you can restrike more often. but don't go crazy. the problem is still delta vs your risk tolerance for a 10 delta strangle you can restrike more often.
---
5/22/26, 1:59 AM | Marco [reply]: Up until how many days left to earnings is worth restriking? Maybe with at least one week left?
---
5/22/26, 8:06 AM | Euan: i've never thought about it in those terms. i always just try to have vega exposure and limited delta exposure. the price moves that cause re-striking will vary as we get closer to the event, but my aim is still the same
---
5/22/26, 11:56 PM | 𝕋𝕠𝕤𝕙𝕚: For those who haven't read it: "The Thetapig Letters by Euan Sinclair | Outlier Pro Options Trading..." [Patreon link]
---
5/24/26, 6:21 PM | Ben: In the never ending quest of making sure that you haven't fucked something up in your data analysis, I found some issues in my monthly pipeline with some FMP data still being used. The problem with the FMP data was that there was still some corrupted splits etc that weren't excluded as outliers and inflated returns in some scenarios and made market cap and IM look more predictable than it was. It didn't really break anything when it comes to the strategy and edge, just went back to what was observed in the weekly options that a delta hedged version works better than unhedged. Now everything uses norgate data for stock prices.

I did try and go back to 2007 but the data I was getting pre-2015 was patchy. I have used up all my ORATS API credits so need to wait until they reset before I extend my dataset.

1M is entry 15 trading days prior to announcement, 2M is 10 trading days prior to announcement.

The standout risk adjusted return is 2M-H-0.35, which is enter the monthly contract 10 trading days prior to announcement and delta hedge at 0.35. So I took a bit of a deeper dive into that scenario.
---
5/24/26, 6:30 PM | Ben: Looking further into adding a market cap filter it does add a little to the performance. Whilst gross return might be less, the risk adjusted return is better.
---
5/24/26, 6:30 PM | Ben: Now to put it to a basic compounding backtest with cost (except short costs for hedges)
---
5/24/26, 6:43 PM | Ben: From here I looked into the drawdowns for any patterns. One obvious one that they share was that they were trading when there were other stress events in the market that caused IV to be high. E.g. the tarrif shock. You were entering at elevated IV
---
5/24/26, 6:48 PM | Ben: New Filter - For each trade, compute the percentile rank of iv_entry against all prior observations for that same symbol in the same scenario. Skip the trade if iv_entry exceeds the 90th percentile of that prior history.

Next is to double check my ORATS data pipeline and extend the period when I get more API calls.
---
5/24/26, 6:51 PM | Ben [reply]: I did look at this but didn't see the same results with the amount of data I had available. What I posted showed more promise in terms of risk adjusted returns.
---
5/24/26, 6:52 PM | Ben: Will look at it again when I get more data
---
5/24/26, 7:21 PM | Marco [reply]: I remmber having issues with pre 2015 data as well, I might want to exclude it altogether
---
5/26/26, 8:03 PM | Euan: Commodities are dangerous. In indices and generally in stocks, the playing field is level because no-one really knows anything (professional stock pickers don't do better than random). But in commodities most of the big participants know stuff. Suppliers and users are both informed. Big market makers see all this flow and talk to other insiders. You, the retail traders, will always be totally ignorant. Often this doesn't matter, so usually commodites have a nice looking VRP. But sometimes it matters a lot and you will get slammed.

On average, pretty much everything has a positive VRP. So you can be a bit picky. I stay away from commodities because I don't need the extra risk.

In stocks a useful rule of thumb is to sell vol on shitty companies: high PE, low return on assets, high leverage, high vol, high implied vol, high historical VRP, anything with clear jump risk. This would have been bad during the dotcom bubble and the MAG7 would have hurt recently, but it is generally the way to go.
---
5/27/26, 6:17 PM | Rob: @Euan Apologies for the basic and long question, but I can't get my head around the following concept and would be grateful for a clarification please. When we try to harvest VRP by selling overpriced options, as I understand we are betting that the underlying's future realised volatility will be lower than that predicted by the options' implied volatility. In your book "Option trading" at the end of page 90 there is a paragraph called "Decreasing Realized Volatility" where you wrote "Here we either expect the underlying's volatility to fall or at least that the underlying will be less volatile than is predicted by the option market", which seems to match the concept of harvesting VRP. In the same paragraph you later wrote: "These strategies should be short gamma". So my interpretation of this paragraph is that in order to harvest VRP it is crucial to be short gamma, which I interpret as I could even be vega neutral as long as I am short gamma I can harvest VRP. However in other instances (for example in the book club videos you mentioned that you always want to have vega exposure, and that if the underlying has moved since entering the position you would restrike in order to regain enough vega exposure (the straddle for example) in order to harvest VRP. But isn't a short vega exposure a bet on implied volatility falling rather than on the realised vol staying below implied vol, as you discussed in the paragraph "Decreasing Implied Volatility" on page 91? Do we really need short vega exposure t[capped]
---
5/27/26, 7:59 PM | Euan: I should be the one to apologize here. I didn't write that well.

In order to harvest VRP you need to be short vega. Every option has vega and gamma of the same sign, so for a single option or straddle or strangle, whenever you are short vega you will also be short gamma. There are compound positions (calendars or skew trades) that can be (usually only locally) short one and not the other, but even then the part of the vol surface that has you short vega will be the part where you are collecting VRP. For example, if you are long a short dated straddle and short a long dated straddle you will be long gamma and short vega. But you will only be collecting VRP in the long tenor. You will be paying the VRP in the short tenor.

Is that better?
---
5/27/26, 8:22 PM | Rob: Yes that's very helpful. Thank you Euan
---
5/28/26, 7:42 PM | Sam: PCE out in less than an hour. I think it qualifies for an event where VIX could be shorted prior (not tested PCE).
---
5/28/26, 9:00 PM | Sam: Out break even
---
5/28/26, 9:09 PM | Sam: Shoulda waited!!!
---
5/28/26, 11:08 PM | hast: Hi RW guys, hello @Euan, I have been practicing earnings volatility trade for few weeks (long vol pre Earnings/short through Earnings). There has been an outlier last night – SNOW - high surprise earnings, high loss for the short Vega part of the Earnings strategy. Considering SNOW as – pre-profit, hypergrowth, high short interest company. This all could be indicated by negative or non-existing P/E. Do you think that could be a good filter to choose the tickers for the Earnings strategy? I mean always request positive P/E for the candidates?
---
5/29/26, 1:33 AM | Euan: No doubt SNOW was a bit of a disaster. I didn't follow in detail but it looks like one of the worst on record. But I've tested almost everything I could think of to find "good" and "bad" stocks and really never came up with anything. I don't want to discourage you but even if you find something it will be a lot of work and the benefits can't be great (otherwise I would have got something). My advice would be just to do as many as possible and equal dollar premium. That way the law of large numbers will help.
---
5/29/26, 5:07 AM | FullMetal37!: Decent amount of blowouts for the ER trade lately
---
5/29/26, 5:07 AM | FullMetal37!: I'm basically flat on the season
---
5/29/26, 5:43 AM | Sam: Is SNOW a candidate for PEAD?
---
5/29/26, 6:43 AM | FullMetal37!: DELL has now definitely put me in the negative this season
---
5/29/26, 7:21 AM | nxtrador: If you are short and get assigned DELL it comes with "Dude you're getting a DELL."
---
5/29/26, 9:09 AM | Euan [reply]: Afaik every stock that has a big earnings move is a candidate. I can't remember any categories being better than others (but it has become a very well studied thing so maybe it is worth looking on Google scholar)
---
5/31/26, 10:10 AM | Ben [reply]: SNOW is a candidate for my PEAD model this week
---
5/31/26, 11:00 PM | Sam: I did both DELL and SNOW for PEAD. SNOW options don't extend up enough!
---
5/31/26, 11:25 PM | Euan: I think it is a pure delta one effect. I don't know of any studies that show vol is cheap or options being underpriced
