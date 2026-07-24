# Raw message log — #tradfi-trading (Robot Wealth Community)

**Period:** 2026-01-07 to 2026-01-31 (no activity Jan 1-6)
**Channel:** https://discord.com/channels/1368787013763072040/1370226295941763154
**Message count:** 277
**Extraction method:** Browser automation (Claude in Chrome) — Discord search (`in:tradfi-trading after:2025-12-31 before:2026-02-01`) to locate the range start, then DOM scroll-and-extract to pull message text, author, and timestamp directly from the rendered page. See `rw-pro-tradfi-trading-20260107-20260131.md` for the thematic summary.

Format: `timestamp | author [reply]: message text`. `[reply]` marks a threaded reply to an earlier message. Long messages may be truncated at ~250 characters at source.

---

1/7/26, 11:40 PM | Yan: https://x.com/macrocephalopod/status/2008837030265180165

What do you guys think about this thread from macrocephalopod on shorting UVXY? His backtest looks very different from Euan’s. Even the unhedged version appeared very profitable, though with e
---
1/7/26, 11:50 PM | Euan: it would depend on how he is rebalancing and leveraging. but you can't tell me that shorting this thing is worse the being long spy.
---
1/7/26, 11:51 PM | Euan: but you should also remember that the observation needs to be translated into a strategy, so details about rebalance frequency etc are very important. without knowing that, he really isn't saying anything concrete
---
1/7/26, 11:59 PM | robotkris: I had a look at that strategy cephalopod is trashing... the guy is doing it with options... that's just going to be expensive
---
1/8/26, 12:00 AM | Euan: Ah. Also a good reminder that purely directional views shouldn't be traded with options
---
1/8/26, 12:01 AM | robotkris: Spoiler alert from the webinar tomorrow, but Euan's UVXY-VXZ trade was the best performing of all the different flavours of vol trades that we do in 2025. Including costs, borrow, rebalancing.
---
1/8/26, 12:15 AM | robotkris: Also @Yan the thing in the twitter thread is a straight up short of UVXY, at 100% allocation I think. The cephaolopod guy is saying that's a bad idea because of the volatility drag, and he's right about that. He posts another chart where he reduces t
---
1/8/26, 2:32 AM | 4D: I simulated VX futures version of this trade with 5 contracts, which is already very close to the results using 30 contracts. The weighted maturities of front and back contracts are 50 and 80. So every day I follow a schedule to trade futures to keep
---
1/8/26, 2:54 AM | TheCTAFan [reply]: Nice! Thanks for sharing. One question — you mention 50 at the front. Doesn’t UVXY use 30-day at the front?
---
1/8/26, 2:55 AM | 4D [reply]: I followed what James does in a webinar last year, and found 50 / 80 is better
---
1/8/26, 2:56 AM | 4D: and if you short the very first month contract, the margin req would be larger
---
1/8/26, 2:59 AM | Rachit: man that whack in april was not fun
---
1/8/26, 3:53 AM | William [reply]: Are you adjusting the ratio to maintain a constant beta between the futures contracts?I’m currently doing the original calendar with futures were essentially it just rolls once a month. It’s been a good trade, but if there are simple enhancements, it
---
1/8/26, (edited) | William: I assume that if you have an unequal ratio of front to back months, your margin would go up significantly as well?
---
1/8/26, 4:01 AM | Sam [reply]: Volatility drag benefits those who are short UVXY though
---
1/8/26, 4:08 AM | 4D [reply]: I don't beta hedge on vx futures. I think back month is enough. if you trade more than 30 vx contracts, maybe?
---
1/8/26, 4:38 AM | William [reply]: I haven’t been either, I’ve been trading between five and 15 calendars. Perhaps I misunderstood your earlier post - I’ve reread and it and I understand it a bit better I think. You’re trading a fixed one to one ratio of short versus long, but trying 
---
1/8/26, 12:09 PM | 4D [reply]: I tested, it is very close to the original James' calendar spread. No noticable improvement
---
1/8/26, 12:24 PM | 4D: but the beta hedge does improve the drawdown on the liberation day with 20 contracts, but lower the final pnl.

the hedge ratio is 1.3 between vx_50 and vx_80.
---
1/8/26, 12:32 PM | 4D: The Sharpe ratio is improved to 2.27 from 1.37 with 10 front contracts
---
1/8/26, 2:24 PM | robotkris: This is great. Thanks @4D. I'm going to include this in tonight's webinar when I talk about the calendar trade if you don't mind me stealing your plots.
---
1/8/26, 2:36 PM | 4D: yeah, sure, but when I extend the data to 2022, the hedged calendar spread is not great, because the extra back month contract was bleeding and the front month contract was flat-ish during 2022-2024  . 

I put the simulation of uvxy/vxz, 50/80 calend
---
1/8/26, 2:38 PM | robotkris: Good to know!! Thanks. So 2025 was something of an anomaly...
---
1/8/26, 2:47 PM | robotkris [reply]: It does! The volatility drag on UVXY at the instrument level will benefit people who are short UVXY. 

BUT... volatility drag applies to any position with convexity, including your own P&L. When you size something large enough, you introduce volatili
---
1/8/26, 3:10 PM | Sam [reply]: Had to read it a few times...but yes, it makes sense! On  a 100k acct, what percentage would you allocate to UVXY, assuming hedging as per Euan's model? Many thanks!
---
1/8/26, 3:32 PM | robotkris: I can’t really give you an answer because it depends on you. But I can help you think about it.  From memory that trade realises about 15-vol (the hedge tames it really well). I’m vol targeting it on that basis, but also sizing it down because of the
---
1/8/26, 3:48 PM | Sam [reply]: Both. In terms of size, I keep the uvxy short market value at 2% of my portfolio. The beta hedge using futures is 2.8x.
---
1/8/26, 4:02 PM | robotkris: That sounds pretty reasonable. There’s a simulation notebook in the lab - I’ll plug those numbers in later and we can see how they play out.
---
1/8/26, 4:32 PM | jgao_imm [reply]: i may be confusing webinars but i remember the long cal spread strat was to short something like a 60 day constant maturity VX and long the back months (5-6 months out). but you're doing the 30 day / 80 day calendar?
---
1/8/26, 4:37 PM | jgao_imm [reply]: if, say, the distribution of front month outcomes turns out to be a lot more leptokurtic than the back months, would that invalidate the harvesting vol drag argument? i wasn't around to trade this in feb 2018 or q1 2020 but looking back at 2018 it's 
---
1/8/26, 5:01 PM | -k [reply]: 2023 and 2024 were pretty mid years. here's plots on the etfs going back to just before volmageddon. the beta hedge helped a lot then. 

though it probably does more for the ETFs than the calendar spread itself
---
1/8/26, 5:03 PM | -k: computed by
betas = ((uvxy * vxz).ewm(126).sum() / (vxz*2).ewm(126).sum()).shift(1)[252:]
---
1/8/26, 5:40 PM | Yan: Many thanks @Euan, @robotkris and @4D for chiming in, lots of food for thought. Really appreciate it. I will take the time to understand it properly. Too bad I can't make it for today's webinar since this trade will be discussed, but will watch the r
---
1/8/26, 6:40 PM | robotkris [reply]: Sam, let me know if I got these numbers wrong... 


You're allocating 2% of $100k to the UVXY short.
,
So that means you're allocating 2%*2.8 = 5.6% to the VXZ long.
,
So your total allocation to the strategy is 7.6%*100k = $7,600
,

When I plug thos
---
1/8/26, 6:41 PM | robotkris: The metrics in the plot (Vol, return, sharpe) are calculated on your allocation to the strategy (ie as if the $7,600 was your total portfolio value). 

You can then get the strategy's vol contribution to the portfolio by doing full_sized_vol * 7600/1
---
1/8/26, 7:45 PM | Sam [reply]: Numbers are right....I just use 3 month Vix futures to do the hedge instead of the VXZ etf. Thanks for this, maybe I'm underallocated on this!
---
1/8/26, 7:47 PM | robotkris [reply]: Glad it's helpful!
---
1/8/26, 11:13 PM | Sam: Gas storage in 15 mins
---
1/8/26, 11:21 PM | akhan: I have a question about this chart if I may. Just trying to ensure I haven’t misunderstood anything. Is it correct that this strategy made most of its money after Covid meltdown? And since 2022, it has only now started to be “alive” again ? If yes ? 
---
1/8/26, 11:22 PM | akhan: The chart is from @robotkris discussion a few hours ago.
---
1/8/26, 11:42 PM | Yan: To me its the contrary, a strategy that makes money most of the time with occasional drawdowns when volatility spikes (covid, August 24, tariffs in April 25...)
---
1/9/26, 1:31 AM | akhan [reply]: Thanks for the reply. I can’t seem to figure that part out . To me return line seems to be fairly flat after 2020 until late 2025. What am i missing ?
---
1/9/26, 2:22 AM | Sam [reply]: Yeah most of the gain was from 2020 to beginning of 2022...almost +50%.  So I agree with what you are saying. 2022 was a bear market in spx. You had vol problem in August 2024. And of course crash in spx in April 2025.
---
1/9/26, 2:25 AM | Sam: Doesn't answer your question ...maybe this is a upward breakout in the equity curve...I don't know!
---
1/9/26, 2:27 AM | akhan [reply]: Thanks for clarifying it
---
1/9/26, 6:37 AM | Euan [reply]: Using an adaptive beta makes this a lot more consistent. I don't see the weak performance in those middle years.

2.8 is a common average but mine ranges from 2 to 3.5.

I can only give a broad hint but use regime dependent betas. Vix high and vix lo
---
1/9/26, 6:50 AM | MidKnight: I posted a recent ssrn paper in the macro-tourism giving some basic regime rules that make a significant improvement to just the basic calendar.....You can see that the flat periods are not a major given the extent of the equity curve.
---
1/9/26, 6:51 AM | MidKnight: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5316487
---
1/9/26, 5:23 PM | Yan [reply]: Post covid to 2022, the VIX went from something like 80 to 16, so I guess it would make sense that essentially shorting VIX futures have been very profitable on the period
---
1/9/26, 10:56 PM | Sam: Shorted Vix ahead of NFP...worked okish
---
1/9/26, 10:57 PM | Sam: Shorting vol again ahead of tariff scotus news
---
1/9/26, 10:58 PM | Rachit [reply]: the front month?
---
1/9/26, 10:58 PM | Sam: I did UVXY
---
1/9/26, 10:59 PM | Sam: Actually bought back at the low of 34.4
---
1/9/26, 11:00 PM | Sam: Shows the significance of timing...
---
1/9/26, 11:04 PM | Sam [reply]: scotus will not rule today! exited my short UVXY for +50 pips
---
1/10/26, 6:05 AM | Euan: Just a general comment here.

Lots of these vol trades work totally differently in high and low environments. The way I handle this is to make 2 models. Then my forecast is a weighted average of the separate forecasts. Maybe I'm 50/50 at vix of 19. T
---
1/11/26, 1:59 PM | akhan [reply]: That sounds very interesting and I would like to try it. Would you care to explain it a bit more maybe using a few actual examples? Or maybe toy examples if there is IP involved. I have a general idea but would like not to make silly mistakes . There
---
1/11/26, 7:14 PM | Sam: Reminder that the BCOM indexers are rebalancing every day till Wed or Thursday. Silver is the biggie...
---
1/11/26, 11:22 PM | George: Hey everyone, I'm trying to implement the asymmetric beta methodology that Euan suggested in the short UVXY video, where you calculate separate regressions for different volatility regimes.

I'm wondering how you guys deal with data imbalance issues?
---
1/11/26, 11:55 PM | Rachit [reply]: bcom indexers?
---
1/12/26, 12:22 AM | Sam: Index funds that passively track the BCOM  index
---
1/13/26, 2:03 AM | Sam: Shorted silver into the rebalancing...might not work today given the massive strength in silver...
---
1/13/26, 2:14 AM | Quarry614 [VBT], Server Tag: VBTVBT [reply]: I shorted last Thu. Getting crushed so far.
---
1/13/26, 2:17 AM | Sam: but you have to exit the short when they stop selling...about 8 mins time. Imo thats the edge.
---
1/13/26, 2:29 AM | Sam: out of short silver
---
1/13/26, 2:29 AM | Sam: 73 pip profit
---
1/13/26, 2:30 AM | Sam: reversed and gone long...(the selling has stopped, imbalance imo)
---
1/13/26, 3:05 AM | Sam: out for +33 pips
---
1/13/26, 9:19 AM | robotkris: Nice Sam. Cool idea
---
1/13/26, 9:26 AM | robotkris: Just did some reading on this - seems that BCOM rebalances only once per year. So those flows while infrequent, should be quite large, especially when something's gone up as much as silver has.
---
1/13/26, 9:26 AM | robotkris: And they tell you what the new target weights are, and when the rebalancing is due to happen: https://www.bloomberg.com/company/press/bloomberg-commodity-index-2026-target-weights-announced/
---
1/13/26, 4:47 PM | Sam: The rebalancing is taking place every day and ends on the 15th.
---
1/13/26, 5:02 PM | akhan [reply]: I can’t seem to find any description of this trade. Can you please refresh my memory. What is the trade exactly? Thanks
---
1/13/26, 5:06 PM | Sam [reply]: Thanks for this. Looks like the biggest change is silver and cocoa. With cocoa they need to buy every day.
---
1/13/26, 5:39 PM | Sam [reply]: There's no description. All we know is that a ton of silver futures will have to be sold every day and at what time. Also a ton of cocoa futures will have to be bought...
---
1/13/26, 9:13 PM | Sam: CPI in 15 mins
---
1/13/26, 9:15 PM | Sam: I don't find CPI as relevant as NFP and fomc...but went short Vix ...see how it goes
---
1/13/26, 9:55 PM | Sam: Exited 2/3rds  for +33 pips...I shorted UVXY
---
1/13/26, 10:38 PM | Sam: Out of rest at breakeven
---
1/14/26, 2:38 AM | Sam: shorted silver into the rebalancing sale +60 pips
---
1/14/26, 2:38 AM | Sam: currently long...
---
1/14/26, 2:47 AM | Sam: Out of long ...+120 pips
---
1/14/26, 2:58 AM | 4D: it seems they rebalance 30 minutes before the close time of the future
---
1/14/26, 4:57 AM | Marco [reply]: Do you observe a volume change.as well?
---
1/14/26, 5:20 AM | Sam: Yes, the rebalance occurs at 6.24pm London time. You can see a huge spike in volume in that 1 min bar.
---
1/14/26, 5:23 AM | Sam: btw there is a margin increase after the close of business today
---
1/14/26, 11:28 AM | robotkris: Great trade
---
1/14/26, 8:03 PM | Rachit: poking around boil stuff / exploring the effect @Sam has been trading. seeing this weird returns on Tuesday mornings - is there something special happening on Tuesdays with NG? 

this is based on roughly 15y of data
---
1/14/26, 9:02 PM | Sam: Not that I know of. Grok doesn't know either.
---
1/14/26, 9:23 PM | Rachit: I'm suspicious it might be something weird happening with the dataset
---
1/14/26, 10:32 PM | Yan: I’m trying to find the historical annualized volatility of the VIX calendar spread trade (short the contract closest to 50 DTE, long the next maturity), but I haven’t been able to find it in the RW material. Does anyone have a rough estimate? The goa
---
1/14/26, 10:58 PM | Sam: Shorted uvxy ahead of scotus ruling on tariffs
---
1/14/26, 10:59 PM | Sam: About quarter of my normal position
---
1/14/26, 11:14 PM | Sam: SCOTUS says will not rule today!
---
1/14/26, 11:14 PM | Sam: out of UVXY, +110 pips
---
1/15/26, 12:43 AM | Prayaag: @Sam , do you have a list of all the events you trade? It sounds like you do at least the following:

Short UVXY over macro announcements (FOMC, CPI, NFP)
,
Natgas EIA weekly announcements
,
the BCOM index rebalance
,
Any others I missed?
---
1/15/26, 1:31 AM | Sam: That's it in terms of events. Short uvxy in front of scotus tariff as well.
---
1/15/26, 1:39 AM | Euan: is that silver thing happening today as well?
---
1/15/26, 2:44 AM | Rachit: yeah i think it was the last day tho
---
1/15/26, 2:51 AM | Sam: Lost 90 pips going short, + 50 pips on the long (silver BCOM index trade)
---
1/15/26, 2:52 AM | Sam: Last day is tomorrow
---
1/15/26, 3:04 AM | Sam: Shoulda kept that long...it's gone insane!
---
1/15/26, 4:21 AM | Yan: Still not crazy GME bubble like figures, but SLV IV is flying
---
1/15/26, 1:19 PM | nxtrador: shoulda sold puts -- so stupid -- instead i traded a bear put spread expecting reversion a few days ago -- silver tulips
---
1/15/26, 4:10 PM | Yan: Yeah I've been thinking about selling puts as well but haven't pulled the trigger yet. I remember Euan saying in a webinar that things need to be REALLY crazy for the "selling puts during a bubble" to work well, I don't know if this is crazy enough
---
1/15/26, 8:42 PM | Shervin: Pretty sure he said to never sell as vol is going up too.
---
1/15/26, 11:11 PM | Sam: NG storage at the bottom of the hour.
---
1/15/26, 11:32 PM | Euan: nice trade
---
1/15/26, 11:38 PM | Marco [reply]: Long or short?
---
1/15/26, 11:43 PM | Sam: Short. Exited for +70 pips
---
1/15/26, 11:46 PM | Sam: Anyone else having to keep shorting BOIL to maintain the exposure? Bit scary the number of shares I've done.
---
1/16/26, 12:20 AM | Euan: it wouldn't be scary if you weren't anchored to the number of stocks you did initially
---
1/16/26, 1:29 AM | Sam [reply]: Yes, this is true.
---
1/16/26, 3:14 AM | Sam: minus 70 on short, +50 on long silver rebalancing trade
---
1/16/26, 10:51 PM | Rachit: How do short interest charges get calculated? Specifically: 


are charges calculated at the close of rth? or at the close of extended hours? or when we tick over to a new day ?
,
does holding time within the day matter? e.g. opening a short at 4am v
---
1/17/26, 12:11 AM | Sam: Do you mean borrow fees on short stock?
---
1/17/26, 12:12 AM | Rachit: yeah
---
1/17/26, 12:15 AM | Quarry614 [VBT], Server Tag: VBTVBT: I think IBKR calculate on settlement. Going short something and then covering the same day will not count becuase at settlement you are not short.
---
1/17/26, 9:21 PM | akhan: has any one trade month end TLT trade with interest rate futures ? Especially for people located in a EU where US ETFs are not allowed for retail trades.
---
1/17/26, 11:07 PM | Yan: If you're in the EU, there are UCITS ETFs you can use to run the trade. Same for the stocks / bonds rebalance trade. Personally I'm using futures because of the capital efficiency (bonds futures, not interest rates)
---
1/17/26, 11:48 PM | deal_me_in [reply]: Alpaca is the same way. I don’t know about tradier.
---
1/18/26, 12:36 AM | M4TZEHDF [reply]: IS04 is the ticker for the UCITS version of TLT
---
1/18/26, 9:33 PM | Sam [reply]: Using futures is the best way to go. I only need to put 0.5% margin in my acct for my required exposure so it's extremely capital efficient.
---
1/18/26, 9:35 PM | Sam: Also you probably want to do this trade using leverage anyway.
---
1/18/26, 11:26 PM | akhan [reply]: How do you structure that if you don’t minds sharing. It’s perfectly fine if you don’t want to. I mean futures are normally expiring 3-4 times a year if i remember correctly. So you just go long the front month for 20 year treasury bond future ? Or a
---
1/18/26, 11:49 PM | Sam: Say I want a million pounds of bond exposure, I just buy 1 million pounds notional value of March 10 year bond future depositing 5k pounds in the account....exit at the end of the month or whenever.
---
1/19/26, 9:53 AM | MidKnight: This part always confuses me about portfolios and leverage and exposure. I don't have a clear picture on how it all ties in with enough detail. I'm used to thinking of a trade = n contracts which = n $ of risk which = ~ n% of account risk.

Lets say 
---
1/19/26, 11:36 AM | robotkris [reply]: We really need some better training material on this... I will put it on the calendar!

The key thing to figure out is what level of dollar exposure gives you the volatility exposure you want. 

I suspect that the bit that confuses people is the fact
---
1/19/26, 11:37 AM | robotkris: Let's say I want my entire portfolio to consist of SPY, and I want 10% portfolio volatility. 

I look at the long run vol of SPY, and eyeballing it gives me about 15% annualised.
---
1/19/26, 11:38 AM | robotkris: That means that if I was fully invested in SPY, my portfolio would go at about 15% annualised vol on average. 

But I only want 10%. Since volatility scales linearly with size, I can get my dollar allocation as follows:

dollar allocation to SPY = (t
---
1/19/26, 11:40 AM | robotkris: That's a decent starting point. But "on average" is going to feel pretty bad when the shit hits the fan!

So in practice, you can get a more useful volatiltiy forecast by looking at recent volatility rather than the long-term average volatility. (Vol
---
1/19/26, 11:41 AM | robotkris: That's OK most of the time, but 60-day vol isn't super responsive to what happened yesterday. So when the shit hits the fan, you might shorten your lookback, or just bump up your vol forecast a bit so that you're sizing down a bit more aggressively t
---
1/19/26, 11:41 AM | robotkris: In reality, I'm not going to realise exactly the portfolio vol that I wanted - our estimates are noisy and lagging - but since volatility is somewhat sticky and predictable, this does turn out to be a practically useful way to keep your portfolio vol
---
1/19/26, 12:55 PM | MidKnight: @robotkris This was clear, thank you Kris.

In your calculation example when you came up with $666,667 exposure, this is the notional value and I would then take the ES micro 6900 (index price) * $5 = 34,500. Then 666,667 / 34500 = 19 micros  ?

Rega
---
1/19/26, 1:14 PM | robotkris: Yep that conversion to MES is right. 

Yeah I think switching to a more responsive lookback based on some VIX threshold would work pretty well (maybe use the median?). Or an exponentially weighted vol estimate. 

In a practical sense, you'll know whe
---
1/19/26, 1:23 PM | MidKnight: And then just building on that. Lets say I want to trade 5 strategies in my portfolio. How do you integrate that? How much is considered too much volatility at the portfolio level? I know this will be personal. But in my head I am thinking of a portf
---
1/19/26, 1:56 PM | FullMetal37! [reply]: Max DD is hard to estimate because it happens relatively unfrequently. Which is kind of the point of the tail risk hedging. If you assume a normal dist your port vol is the 1SD. Your Max DD is probably something like a 2-3 SD move. Probably on the la
---
1/19/26, 4:02 PM | robotkris [reply]: This really needs an example... but I'll write it down here anyway. Hopefully it's useful...
---
1/19/26, 4:03 PM | robotkris: Max DD is a tricky thing to size a portfolio to... 

Technically, the only way to do that is to adjust your sizing based on the depth of the current drawdown. This would have you trading smaller and smaller as you approach your 30% limit, to the poin
---
1/19/26, 4:04 PM | robotkris: That sort of question can be solved analytically to give you a probability of being down 30% in a year's time:
---
1/19/26, 4:04 PM | robotkris: mu <- 0.1  # expected ann return
sigma <- 0.20  # ann volatility 
threshold <- -0.30  # drawdown target
prob <- pnorm(threshold, mean = mu, sd = sigma)
prob
[1] 0.02275013
---
1/19/26, 4:05 PM | robotkris: But that's not that interesting. 

The reason that problem is tractable is because it's constrained to being "down 30% at the end of 12 months" - it doesn't answerthe probabiltiy of having a 30% drawdown sometime within 12 months (this will be higher
---
1/19/26, 4:06 PM | robotkris: Simulation is a useful tool here... 

Use the GBM simulator from TLQ to get a feel for what the distribution of performance in a 5-year period can look like given assumptions about your expected return and volatility. 

(If you want, I can give you t
---
1/19/26, 4:07 PM | robotkris: You've been doing this a long time, so I imagine 15-20% vol would be within your risk tolerance (but of course I don't know if that fits with your other goals and constraints). 

For people just starting, I think ~8% is a good place to start. 

If in
---
1/19/26, 4:07 PM | robotkris: Let's say you decide to target 15% vol at the portfolio level. 

Here's a practically useful way to figure out how to size your portfolio components (it's far from the only way - Euan does this slightly differently but equally practically, and there 
---
1/19/26, 4:09 PM | robotkris: RPH: very well understood, high confidence effect (give it more risk budget)
,
Turn of month bonds: Decent trade, but less confident (it will disappear eventually). Annualised vol is deceptive because its positions are sparse (size it down).
,
VIX sl
---
1/19/26, 4:09 PM | robotkris: Based on that, I might split my 15% risk budget as follows:

RPH: 8%
,
Bond thing: 3%
,
Slayer: 2%
,
UVXY-VXZ: 2%
,

(just example numbers I pulled out of my ass)
---
1/19/26, 4:10 PM | robotkris: However, those vol contributions aren't additive... if you scale the returns of each strategy and simulate them in a portfolio, the portfolio vol will come in at about 10-11% (just a guess). 

At that point, you might go "I'm happy with that buffer -
---
1/19/26, 4:10 PM | robotkris: On the other hand, you might go "I am here to ball, and I want my 15% portfolio vol." Also fine. 

In that case, you can use the same maths as before to figure out how much to scale everything up:

scaling factor  = (target portfolio vol) / (realised
---
1/19/26, 4:11 PM | robotkris: So scale everything up by 1.5:

RPH: target 12% annualised
,
Bonds: target 4.5% annualised
,
Slayer: target 3% ann
,
UVXY-VXZ: target 3% ann
,
---
1/19/26, 4:11 PM | robotkris: That gives you your strategy vol targets that you need to hit your portfolio vol target on average.
---
1/19/26, 4:11 PM | robotkris: Then you can go back to your straegy simulations and figure out your position sizing. Each strategy simulation gives you its vol if you were fully invested in it - you just scale the positions up or down depending on the ratio of your target strategy
---
1/19/26, 4:13 PM | robotkris: As I write all this down, I realise it's actually a bit more convoluted than it feels in my head. I can see why it's a point of confusion.... 

We really need a walkthrough with real data, real simulations, real code/spreadshseets or whatever.... 

I
---
1/19/26, 10:31 PM | Rachit [reply]: really helpful convo...spreadsheet walkthrough would be phenomenal.

Followup though...I think I understand using vol for sizing. Where I kind of get lost though is how to think about using leverage across strategies. What is the appropriate amount w
---
1/19/26, 11:36 PM | Yan [reply]: I’ve struggled quite a bit to wrap my head around this, and I’m not sure I actually have. I use futures, which have leverage built in, for most of my trades outside of RP7.

My understanding is that you’re fine as long as the volatility of your posit
---
1/20/26, 4:20 AM | 4D: Here is my workflow.  Since last December, I have started a new rp portfolio with no bonds, which focus on value exposure, small caps, gold, miners, non-us equities. I allocated twice the risk budget to GLD as much as other positions. 


everyday, I 
---
1/20/26, 4:35 AM | ASlan [reply]: I would describe your example as close enough to being correct. Assuming that 11% for the rebalance is already taking into account the fact that you’re only in it some of the time.
Technically there is another element of checking the correlation of t
---
1/20/26, 8:08 AM | Rachit [reply]: hmm this is interesting. I landed on exactly #2,3,4 for the perp-perp funding arb in cryptoland. computing a vol adjusted leverage across the two exchanges and then apply that to weights + some bufffer. The objective being to maximize capital use wit
---
1/20/26, 10:17 AM | robotkris [reply]: @Rachit think of leverage as a tool that lets you hit your vol target. 

For example, say you want 20% annualised vol from the RP7 strategy (you don't, but just humour me for the example...)

That strategy has a large allocation to 7-10 year treasury
---
1/20/26, 10:19 AM | Rachit: ohhhhhhhhhhhh
---
1/20/26, 10:19 AM | Rachit: ok i think that moved a stuck gear in my head
---
1/20/26, 10:23 AM | robotkris: That's great
---
1/20/26, 3:56 PM | akhan [reply]: Can you please expand on cost of leverage in this situation? For a relatively small account size IBKR is asking for roughly 6% (guessed number) for the margin loan or funding costs. So I am guessing, that assumption here is that extra profit here is 
---
1/20/26, 8:10 PM | robotkris [reply]: Yeah that's right. YOu'll want to consider the cost of the leverage you're getting. The higher the costs, the less attractive it will be.
---
1/20/26, 10:55 PM | Sam: Some tariff news from Scotus due at top of the hr
---
1/20/26, 10:56 PM | Sam: Short uvxy quarter size
---
1/20/26, 11:09 PM | Sam: Not ruling on tariffs today...exited minus 60 pips
---
1/21/26, 12:34 AM | Marco [reply]: Longed the front vx future as well...for nothing
---
1/21/26, 12:40 AM | Euan: the supreme court ruling is a good example of something where vol will probably come in once uncertainty is removed. the thing that makes this harder than FOMC or earnings is the timing uncertainty. but short vol seems like a solid play for that.
---
1/21/26, 12:41 AM | Euan: of course, that news doesn't exist in isolation. we still have the uncertainty of trump invading greenland, but sooner or later he will run out of countries to invade so thats good
---
1/21/26, 12:41 AM | Euan: but nothing is ever in isolation. we just keep looking for edges even if different edges might layer or conflict
---
1/21/26, 12:47 AM | 4D [reply]: why not short straddle, it is so fat this morning
---
1/21/26, 1:04 AM | Euan: it isn't as clean of a vol bet because you are also exposed to the underlying movement. VIX=vol, options= IV-RV
---
1/21/26, 1:53 AM | Sam: @Euan do you think it's positive ev to short vol before Trump is scheduled to speak (top of the hr btw)? How about before Treasury auctions?
---
1/21/26, 2:09 AM | Euan: Trump yes. Auction don't know
---
1/21/26, 2:36 AM | Sam: Keep forgetting that Trump is always late...
---
1/21/26, 3:47 AM | Rachit: good lord this guy really has nothing better to do
---
1/21/26, 4:25 AM | stian: just when i was starting to enjoy the BOIL ride :p
---
1/21/26, 3:54 PM | Sam: Overnight BOIL boiling...
---
1/21/26, 4:41 PM | robotkris [reply]: Geez isn't it just
---
1/21/26, 4:45 PM | Yan: Glad that I was disciplined enough yesterday evening to cut size
---
1/21/26, 5:17 PM | robotkris [reply]: Good work!!!
---
1/21/26, 5:37 PM | Yan: Now would roughly be the time to put on the stocks/bonds rebalance trade. As of yesterday’s close, SPY is down 0.64% MTD and TLT is down 0.59% MTD. From a purely mechanical standpoint, this would imply going long SPY, but in practice the move is so s
---
1/21/26, 6:22 PM | TheCTAFan [reply]: I use 1% absolute diff as a threshold, but James would have told me to not fudge with it  Still the diff as a signal seems to be correlated with the edge so
---
1/21/26, 6:26 PM | Yan: Yeah I don't want to get cute and try to complicate a simple trade, but here there is basically no difference at all between the two...
---
1/21/26, 7:06 PM | robotkris: I think it's a pretty reasonable thing to do based on what we know about the trade... if it's driven by rebalancing flows as we think it is, it should do worse when there's less rebalancing to do. The data backs this up:
---
1/21/26, 7:08 PM | robotkris: It might be interesting to see what happens when one has been unusually volatile - you could also get vol-driven rebalancing as well as performance driven.
---
1/21/26, 8:45 PM | Sam: Might want to wait till the end of the day before doing the trade. Maybe...
---
1/21/26, 8:48 PM | Sam [reply]: Trump talking in 45 mins at Davos (unless he's late). Thinking about shorting vol...but then again, is he gonna say anything that's not going to piss off the market even more???
---
1/21/26, 10:11 PM | Stefan [reply]: looks like that wouldve worked fine
---
1/21/26, 10:18 PM | Marco: You alll gamma scalping Trump declarations
---
1/21/26, 10:23 PM | TradeQuantiX [reply]: What I do for the SPY/TLT trade is I space out my entries. I start around the 20th of the month and scale in every 2 days until the end of the month, then I exit all positions. 

The interesting thing I implement is with each scale in I remeasure the
---
1/21/26, 10:36 PM | Sam [reply]: +250 pips on uvxy
---
1/22/26, 12:27 AM | Rachit: I think my new indicator for reducing boil short exposure is when I freeze my ass off during the evening dog walk
---
1/22/26, 1:01 AM | Prayaag: Does anyone know if "short natural gas (BOIL) over US winter" trade could be extended to "short Dutch TTF natural gas futures over European winter"? There's potentially a nice diversification benefit due to geographic independence of climates in US/E
---
1/22/26, 4:02 AM | Ewan: we're so fkin back
---
1/22/26, 4:49 AM | Sam: Trump manipulating markets
---
1/22/26, 4:54 AM | Yan [reply]: Today cleared things up: long TLT it is
---
1/22/26, 5:12 AM | jgold437 [reply]: I trade it with CME 30YR (ZB) and 10YR (ZN) futures. FYI, those futures have a lower volatility that TLT, so you will need to trade more $$$ value.
---
1/22/26, 5:48 AM | emsin44: Tacos for dinner it seems
---
1/22/26, 6:04 AM | zbanga [reply]: Hit LU/LD
---
1/22/26, 6:14 AM | MidKnight [reply]: That's how you buy the dip, you make the dip
---
1/22/26, 7:20 AM | Sam [reply]: Lu/LD?
---
1/22/26, 8:08 AM | zbanga [reply]: Limit up / limit down
---
1/22/26, 10:03 AM | jgao_imm: when i set up my schwab account i was wondering why they don't offer hedge fund account types unlike ib.

yday i got a triple rude awakening - a 6M margin hike on 3 position concentrations.

i was selling ETHA puts RTH and hedge with CME futs thru ou
---
1/22/26, 10:04 AM | jgao_imm: corollary

you can read the manual

or do it live and FAFO like me
---
1/22/26, 10:08 AM | robotkris: Reading the manual is way overrated
---
1/22/26, 10:20 AM | jgao_imm: reading the manual probably won't help either.
schwab don't publish what they group together as logical risk categories.

i asked the PM guy on the line

ok i can't trade now not even to hedge cuz my account is restricted while the warning is on. not
---
1/22/26, 10:26 AM | MidKnight: I hate that about these broker supports, just useless. I've had some terrible support with IB (not the trade desk, just general). I moved all my day trading to Sweet Futures where I have a direct line to a real person. The same person I've had access
---
1/22/26, 10:35 AM | MidKnight: Schwab have earnings soon, you should put this up on wallstreet bets and get them to pile-in short
---
1/22/26, 1:41 PM | Ben: Bit of start date luck/bias with some of the vol trades ... breaks the cardinal trading rule of "thou shall go into drawdown on the first day of trading a new system live"!
---
1/22/26, 1:42 PM | robotkris [reply]: We take what we can get!!
---
1/22/26, 10:34 PM | Yan [reply]: Is the lower volatility because of the duration ? If so, why not use UB instead of ZB ?
---
1/22/26, 11:02 PM | Sam: Gas storage in 30 mins. Gonna short smaller due to this strength in ng
---
1/22/26, 11:39 PM | Sam [reply]: Minus 6 pips
---
1/22/26, 11:51 PM | Yan: "US natural gas futures are on track for a weekly gain of more than 70%, the largest increase in records dating back to 1990." Biggest weekly gain in 36 years
---
1/22/26, 11:59 PM | Euan [reply]: I wouldn't assume that. Energy seems to be geography specific and subject to different extraction methods and distribution channels
---
1/23/26, 3:21 AM | Sam: https://www.telegraph.co.uk/gift/48ab1ae98e5dc0c4
---
1/23/26, 3:23 AM | Sam: Retail UK don't want UK stocks, prefer US presumably. Gotta be an edge in buying FTSE?
---
1/23/26, 3:34 AM | Sam: The changes will gradually be rolled out between March and June this year.
---
1/23/26, 4:02 AM | Ewan: afaik LifeStrategy in UK was relatively heavily home biased, so this just kind of brings it in line with normal
---
1/23/26, 5:55 AM | Ewan: Although I do think that the latest generation of UK investors who invest with app platforms instead of financial managers tend to just chuck spare income in to S&P
---
1/23/26, 4:15 PM | Sam: As part of my RP, I'm going with non US equities such as UK, Germany, Japan
---
1/24/26, 12:03 AM | robotkris [reply]: I like this... I do the same. Also some EM bonds for good measure.
---
1/25/26, 7:47 AM | 4D [reply]: imo, short dated options = 80% iv - rv + 20% vol,  long dated options = 20 % iv - rv, 80% vol, right?
---
1/25/26, 1:24 PM | Euan: I have no idea what you mean
---
1/25/26, 8:25 PM | Dan [reply]: TTF doesn't have as long history as US NG to compare, but you could test your thesis on UK Nat Gas which as been around longer and correlation has fluctuated around 95%.
I only use TTF for live trading now, but the UK version I use in backtesting htt
---
1/25/26, 9:11 PM | Marco [reply]: You mean short dated are mostly gamma bad long dated mostly Vega?
---
1/26/26, 4:31 AM | Sam: Can we do the basis Treasury trade? If so, how?
---
1/26/26, 5:03 AM | bdkoepke: It's pretty difficult to do as a retail trader because you're unlikely to have access to the repo market. You could try to use synthetic repo (box spreads), but I'm not convinced the juice is worth the squeeze. Also you need a portfolio margin accoun
---
1/26/26, 5:05 AM | bdkoepke: Assuming that you found a broker that could do it, you'd buy a T-Bill/Note/Bond, and short the corresponding future making sure you match the duration and do the cheapest to deliver calculations correctly. Then sell an option box to get the financing
---
1/26/26, 6:54 AM | Dan: @Ben have you seen this? something more for your PEAD maybe https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6041614
---
1/26/26, 7:06 AM | Ben [reply]: Thanks mate, I had meant to look at that.  Saw it and forgot all about it!
---
1/26/26, 9:00 AM | MidKnight [reply]: I've been wondering this a lot recently and have been meaning to ask this same question. Yet we never see it talked about here so I was starting to wonder that this may not actually be a thing. I would have thought the large and slow interest cycles 
---
1/26/26, 12:57 PM | Dan: @Ben @MidKnight -  continuing the VIX basis volatility chat here to take it out of support channel..
I think we probably need clarification about:

Should it be 20 for long vol to switch to the short vol hurdle as per the questions here: ⁠support⁠
,

---
1/26/26, 1:01 PM | Dan: A separate slightly related topic - for instrument vol and not strategy/portfolio vol, I wonder if the absolute price differences rather than percentages might be better due to sometimes having to measure on adjusted markets (eg VIX ETFs that have be
---
1/27/26, 12:57 AM | Sam: There are 3 US Treasury bond auctions this week. I think they will become more important as time goes by.  I may short vol ahead and close after. For reference, they are at 6.01pm London time, today, tomorrow and Thursday.
---
1/27/26, 1:01 AM | Sam: Actually, scrap that. I'll wait till they are featured prominently in the news
---
1/28/26, 10:31 AM | TimExcellent: https://youtu.be/bSxadFJUneE?si=ebZg76x1DBpziY5H I did a vanilla version of this from the book for stocks but could be fun to look at on crypto but also apply some of the stat arb ML stuff or ranking
---
1/28/26, 10:40 AM | bdkoepke: I used to be the head trader and one of the PMs for those funds. Jack and Wes are great. There's a lot of different ways to implement momentum, and if I recall that book uses 2_12. One enhancement that is pretty easy to do is to not buy securities th
---
1/28/26, 10:42 AM | bdkoepke: Another thing that I believe is mentioned in there is a screen for momentum type (generally you want smooth securities, with a trend up, not ones that discontinuously jump due to things like FDA approvals/etc). They use this method: https://www3.nd.e
---
1/28/26, 10:43 AM | bdkoepke: Also, if you're US-based, ETFs have a structural tax advantage that unfortunately you can't really replicate as an individual trader: https://ir.lawnet.fordham.edu/faculty_scholarship/722/.
---
1/28/26, 12:09 PM | robotkris [reply]: This is gold. Thanks for sharing! I talked to Wes a bit back in the day... seemed like a great guy. Are they still running their ETF?
---
1/28/26, 12:15 PM | bdkoepke: Yeah, he's very down to earth. They used to do this big 28 mile rough march in rural Pennsylvania with a ton of finance people, but they haven't done that in a few years. If they do it again it's a great way to meet people in the industry. Yes, they'
---
1/28/26, 12:17 PM | robotkris [reply]: Nice. That would have been a fantastic place to work. I remember seeing photos of that march - Wes was always smiling but it looked tough
---
1/28/26, 12:18 PM | bdkoepke: Don't do it with a 40lb pack, and when he says "the end is just up the road", don't believe him
---
1/28/26, 1:21 PM | TimExcellent [reply]: Nice! The bit I struggle with (might just require rereading) was when to rebalance, I had some truly massive wins but then ages of nothing… so was looking for a more consistent version… so hoping I can transplant some of the Stat-arb tooling to it ma
---
1/28/26, 1:23 PM | TimExcellent: I didn’t bother with a back test or anything given there is enough exploration of historic returns in the book - so it felt fine to run it on small and mid cap stocks… I ignored biotech and did it long only, but I could have done short. Anyway I want
---
1/28/26, 1:24 PM | TimExcellent: (And I’m quite a number of webinars behind for the last few months so lots of catch up to do - I may have missed where we’re at on stat arb)
---
1/28/26, 1:28 PM | bdkoepke: https://alphaarchitect.com/wp-content/uploads/2021/08/The_Quantitative_Momentum_Investing_Philosophy.pdf, page 25/26. tldr: This portfolio is rebalanced at the close on the last trading day of February, May, August, and November". FWIW I think they c
---
1/28/26, 1:31 PM | TimExcellent [reply]: Haha fantastic thanks
---
1/28/26, 1:37 PM | bdkoepke: Just be aware that single factor portfolios can experience face-ripping drawdowns: https://www.twocenturies.com/blog/2019/1/27/relevance-of-long-run-historical-data-today
---
1/28/26, 2:09 PM | TimExcellent: Yeah had some basic vol targeting - but this was likely where I could have benefitted from doing some kind of backtest/walkforward… anyway I put it on pause while Kris and Hac sort out the API and we finish the statarb… thinking to make it slightly m
---
1/28/26, 11:31 PM | Sam: Note today is corporate month end...they tend to buy USD
---
1/29/26, 10:22 AM | robotkris: All, I've been looking at vix regime-dependent betas for the UVXY-VXZ spread trade (new people can get up to speed with that trade here). 

The idea is that the 'optimal' hedge ratio would change in different volatiltiy regimes. Makes sense... this i
---
1/29/26, 10:32 AM | MidKnight: i think something like this could maybe be used for a sort of "rebalancing" of the vix calendar too. What do you think?
---
1/29/26, 10:33 AM | MidKnight: in my head I'm thinking about weights being distributed and adjusted across VX2 to VX5
---
1/29/26, 10:33 AM | MidKnight: so one would have shorts spread across them and rebalanced
---
1/29/26, 2:29 PM | robotkris: Yeah it's a reasonable idea. You'll find if you do a bunch of vix calendar spreads simultaneously you'll get a decent boost to before-cost sharpe - not sure how it goes with costs though. Suspect you could express the same idea with an equivalent pos
---
1/29/26, 3:56 PM | Yan: I ran a very similar analysis last week, but using deciles instead. I reached the same conclusion regarding both low and high VIX regimes. The dataset begins in mid-2018, and I tested two different rolling windows. Deciles may not be the best way to 
---
1/29/26, 11:25 PM | Sam: NG storage in a few mins
---
1/29/26, 11:26 PM | Sam [reply]: I've lost money on the $UVXY trade
---
1/29/26, 11:43 PM | Sam [reply]: +60 pips
---
1/30/26, 12:37 AM | Marco [reply]: It was a nice move
---
1/30/26, 1:10 AM | Dan [reply]: Does that cover Europe too?
I notice my Dutch TTF natty is up today, trending.
---
1/30/26, 3:11 AM | 4D: it's a sharpe 2.4 trade in 2025
---
1/30/26, 3:16 AM | 4D: sharpe 1.0 since 2023
---
1/30/26, 4:24 AM | Sam [reply]: US storage only afaik
---
1/31/26, 10:13 AM | bdkoepke: This is the momentum reversion paper I was talking about (unfortunately paywalled) https://joi.pm-research.com/content/29/3/38
---
1/31/26, 10:13 AM | bdkoepke: But this one about blending 1_11 with 2_12 isn’t: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5199701
---
1/31/26, 10:17 AM | bdkoepke: Also thank you for the mention @robotkris!
---
1/31/26, 1:06 PM | Dan: Big vol on Friday.
I run a 30% vol system, with loose target. It only changes vol very slowly to maintain higher performance and prevent too many position differences (I have experience white knuckling it when they get temporarily volatile).
Normally
---
1/31/26, 8:20 PM | blue664203 [KONG], Server Tag: KONGKONG: Guys, would like to get your thoughts on working with intraday data versus real life trading.
Say I get the per minute bid & ask quote price on each minute after open: 1m, 2m, 3m…. 389m.
Is it reasonable to assume that I can get a fill at the ask (bi
---
1/31/26, 9:25 PM | alvin [reply]: I might be wrong but I suspect you’re gonna get rekt, especially for slightly smaller caps where their intraday volumes are pretty erratic, though 50m seems okish. 

I highly doubt you’d get a good fill using market order at sizing at 0.1% daily volu
---
1/31/26, 9:53 PM | blue664203 [KONG], Server Tag: KONGKONG [reply]: Appreciate your feedback Alvin.

It’s a mean-reversion strategy that filters out a bunch of stocks before open and enter between 1-5m after open if the stock gaps up/down.

I use bid/ask quote in backtest to be conservative (but not sure if it’s cons
---
1/31/26, 9:56 PM | blue664203 [KONG], Server Tag: KONGKONG: Just noticed that I type a lot, sorry for throwing a bunch of questions at you!