# Raw message log — #tradfi-trading (Robot Wealth Community)

**Period:** 2026-02-01 to 2026-02-27 (no activity Feb 28)
**Channel:** https://discord.com/channels/1368787013763072040/1370226295941763154
**Message count:** 228
**Extraction method:** Browser automation (Claude in Chrome) — Discord search (`in:tradfi-trading after:2026-01-31 before:2026-03-02`) to locate the range start, then DOM scroll-and-extract to pull message text, author, and timestamp directly from the rendered page. See `rw-pro-tradfi-trading-20260201-20260227.md` for the thematic summary.

Format: `timestamp | author [reply]: message text`. `[reply]` marks a threaded reply to an earlier message. Long messages may be truncated at ~250 characters at source.

---

2/1/26, 8:02 AM | Dan [reply]: The only intraday trading I do is via limit orders or stop orders on daily bars, but some lessons are still applicable.

What I do in my trades list when reviewing a backtest of MR is have a variable that shows the percentage of volume for each trade
---
2/1/26, 8:03 AM | Dan: Just saw you use mid-price, this might be better than Adaptive I'm not sure. I only have adaptive in my execution so the only midprice use I've done is manually.
---
2/1/26, 8:06 AM | Dan: The other question to ask is what percentage of $50k is that of your account size?
For mean reversion (that's best without stops) you want each trade to be only a small percentage of your account. Otherwise one single trade can take away weeks of gai
---
2/1/26, 2:03 PM | alvin: Actually if I were you i would just start trading it immediately at a fraction of the size, the objective of figuring out what the actual fills are.  Maybe instead of 50k do like 1k or something.

I mean we could simulate all we want but nothing beat
---
2/1/26, 10:30 PM | blue664203 [KONG], Server Tag: KONGKONG: Thank you guys for the very helpful insights   I really appreciate it! Will keep an eye on the real life execution and see how it lines up with the data.
---
2/3/26, 1:32 AM | bdkoepke: Here comes CME as per usual, pro cyclically increasing margin rates after  the market is already correcting…
---
2/3/26, 1:32 AM | bdkoepke: SI up 36% and GC up 33% on maintenance and initial
---
2/3/26, 2:20 AM | bdkoepke: https://www.federalreserve.gov/econresdata/feds/2014/files/201486pap.pdf
---
2/3/26, 3:34 AM | Sam: Looks like BOIL boiled over!
---
2/3/26, 4:04 AM | 4D [reply]: natural gas is way too volatile....
---
2/3/26, 4:21 AM | Yan: Cut some size on friday, added some today... Wild
---
2/3/26, 5:02 AM | deal_me_in: lol. It really is
---
2/3/26, 5:22 AM | deal_me_in: My portfolio is only down 1.23% because of how small I sized it lol. The strategy itself is down 23% even after today’s win.
---
2/3/26, 6:21 AM | MidKnight [reply]: Just basically looks like a trend following system to my naive eyes....
---
2/3/26, 6:24 AM | MidKnight [reply]: Yeah I never thought I 'd say the words "this market is too volatile" but I am.  She's a tricky one....
---
2/3/26, 6:46 AM | Euan: There is a notion that BOIL is "too volatile" but remember that a positions dollar volatility is largely on you. if you BOIL position is too volatile you should trade it smaller. I thought hard about whether i should say that. i don't want to sound l
---
2/3/26, 6:49 AM | Dan: This is true. I think I was tempted to size too large for the vol, maybe due to the low sharpe.
I have to remember to size based on vol not based on a minimum CAGR or something..
---
2/3/26, 7:39 AM | bdkoepke [reply]: I’ve never dug into the rules, but I wouldn’t at all be surprised if they have a legging system based on trailing vol. That would explain why it moves up rapidly after vol spikes and then comes down very gradually.
---
2/3/26, 2:34 PM | TheCTAFan: Having said that, it sounds like this year were some of the biggest moves in 30 years.
---
2/3/26, 2:36 PM | Dan [reply]: The market holiday just happened to fall right when the Arctic weather thing happened.
If Monday was open, being able to rebalance quicker would've been nice.
So bad luck squared, doesn't happen very often.
---
2/3/26, (edited) | Dan: If using daily bars, it's not until Tuesdays close we then get to rebalance on the open of Wednesday. If you have a system with live quotes that can trade intraday is a bit quicker.
---
2/3/26, 4:33 PM | robotkris: Further to what Euan said above, when I entered the BOIL trade back in November, it was running at about 80 vol. It's now at 280, using a 20-day rolling window. So reducing size is absolutely the right thing to do. 

Note that on the back of yesterda
---
2/3/26, 6:13 PM | jgao_imm: you can track ERCOT and PJM location specific prices (LMPs) on their website or thru something like gridstatus.
those moves on the RHS are almost entirely driven by reactions to weather reports, specifically 
winter is over
actually no winter is back
---
2/3/26, 6:47 PM | Ewan [reply]: Hard agree. I've got rebalancing in my implementation of the strategy and the size has been cut with vol increasing so I can't say I can share much of the anxiety other's have had
---
2/3/26, 11:29 PM | FullMetal37!: Is there any RW content on more general trend following beyond just YOLO?
---
2/4/26, 4:07 AM | MidKnight [reply]: I don't think there is. My hunch was because a model like YOLO isn't really effective in more mature markets?
---
2/4/26, 4:08 AM | Rachit: thought trend worked in commodities but depends heavily on diversification ?
---
2/4/26, 5:22 AM | Dan [reply]: This. I take a huge amount of trades before getting my rewards.
Many losses, many break even, some small-medium profits, and only a few big winners (Coffee, Cattle, all metals) in the last year and a half. 
It's also something that has gaps of non-pe
---
2/4/26, 5:25 AM | Dan [reply]: Been running TF since Nov 2024, happy to answer any questions. It's something I find fits really well with the RW strategies, low correlation. Downside is it requires a lot of capital to use futures, and CFDs are pretty high cost. Also automation so 
---
2/4/26, 5:38 AM | FullMetal37! [reply]: Are you running Carver’s AFTS strats? I’m interested in adding TF in non-equities for diversification like you said above. Not sure if it’s really worth doing my own implementation or just buying an ETF like CTA or KMLM. I’m bothered by the fact that
---
2/4/26, (edited) | FullMetal37!: It also is just a PITA getting sizing right because you can’t trade fractional contracts on futes. So then vol targeting and all of that becomes more difficult. I don’t think I have enough capital to run it well with a reasonable vol target. I would 
---
2/4/26, 6:12 AM | Dan [reply]: No, I agree with Kris that Carver's stuff is maybe a little too complex and messy to start with.
I like the concept of getting started trading first, then add complexity later.
I don't want to need a live box connected 24/7 like with pysystemtrade.
Y
---
2/4/26, 6:16 AM | Dan [reply]: As for whether it's worth it - CTA and KMLM are too low vol for the cash/capital usage to help diversification a lot IMO. Unlisted CTAs can do better, but not being able to combine them in the same account with your RW strategies hurts the uncorrelat
---
2/4/26, 6:19 AM | Dan [reply]: Def want 6 figures at least to run futures, even with a fairly decent account I still run at high vol just to keep diversification high by being able to afford the bigger contracts. I also had to pool my capital from all my trading accounts into one 
---
2/4/26, 6:27 AM | Dan: Regarding CTAs - a screenshot of a discussion had recently with some TF friends about some opinions why CTAs perform poorly. 
#1 is huge IMO, I don't even include indices anymore in Trend as it does a poor job capturing both sides of  them, and we ca
---
2/4/26, 11:26 AM | bdkoepke: You can get a pretty good idea of the long-term returns of diversified trend following using the data from the SG trend and CTA indexes: https://wholesale.banking.societegenerale.com/fileadmin/indices_feeds/ti_screen/index.html. I believe this is net
---
2/4/26, 11:26 AM | bdkoepke: BTOP50 is interesting too.
---
2/4/26, 11:32 AM | bdkoepke: I built a skunkworks CTA with duct tape and glue a few years ago and work for a CTA firm currently. It's an interesting space, but a lot of people struggle doing it over a long time horizon (plus the huge number of parameters, dispersion of results a
---
2/4/26, 11:32 AM | bdkoepke: https://www.managedfuturesinvesting.com/cta-database/
---
2/4/26, 11:32 AM | bdkoepke: https://portal.barclayhedge.com/cgi-bin/indices/displayHfIndex.cgi?indexCat=Barclay-Investable-Benchmarks&indexName=BTOP50-Index
---
2/4/26, 11:35 AM | bdkoepke: HFRI has some decent data too: https://www.hfr.com/
---
2/4/26, 11:40 AM | bdkoepke: I think a realistic excess return (gross of fees) is somewhere between 0-5% over the long-run, where the SG trend index has been approximately 3.5% since 2000. The insurance like properties ("crisis alpha") are more well known now, and insurance isn'
---
2/4/26, 1:48 PM | Jakub: Trend following works REALLY well as a complement to stock and bond portfolio. When you run historical simulations, the optimal allocation is usually 25-40% depending on the time period and which index you choose. I tell everybody they should have 25
---
2/4/26, 3:34 PM | alvin: I don’t get the TF ETFs. 
Eg DBMF on March 2025, the returns were flat for last 5 years. 5 of the strongest equity bull market years. As of now, it’s at the same price as it was 3 years ago. I get its low correlation with equities, but this seems pre
---
2/4/26, 3:53 PM | Jakub: Did you include dividends?
---
2/4/26, 3:53 PM | Jakub: DBMF is run at super low vol, around 7% per year. They sit on a lot of cash, put it in Treasury bills, and pay out the income as dividends.
---
2/4/26, 3:55 PM | Jakub: More interesting ETF is AHLT. It's an ETF version of the flagship AHL fund but with fees below 1% (versus whatever they charge for the real version). They don't promote it at all, for obvious reasons. I don't understand why they launched it at all. I
---
2/4/26, 3:57 PM | Jakub: I hold both in my 401k.
---
2/4/26, 4:03 PM | Jakub: Here is a real-life performance of a private fund I'm involved with (I run a sleeve inside of it). The line marked "Alts" is the fund after all fees. It has kept up pretty well with the S&P 500. And it helped to diversify the 60/40 portfolio in 1H22 
---
2/4/26, 4:47 PM | alvin [reply]: I was eyeballing TradingView and for some reason the dividends weren’t appearing at the bottom. Just saw them now. 
Around 0.76 sharpe since incorporation, seems alright. Unfortunately I’m getting taxed on dividends so there’s some drag on returns, s
---
2/4/26, 5:04 PM | Dan [reply]: Wow, thanks. I never even knew about AHLT, you're right it's not promoted very well. It never comes up in these discussions. 
Looks like it might get higher CAGR but underperformed DBMF on a sharpe basis (so far).
---
2/4/26, 5:05 PM | Dan [reply]: Looks good. I've been using ECCM with similar performance in my retirement account (as I can't trade futures there), "east coast capital management" one of the few systematic funds in Australia. They're very small, so benefited properly from commodit
---
2/4/26, 5:08 PM | Dan [reply]: These 7% vol funds are pretty useless IMO. We also do the same with TBills in IBKR, earning on our margin funds since futures don't use any cash (for us, some regulatory setups might force using cash). Or even better than TBills - use the margin fund
---
2/4/26, 5:10 PM | Dan: A good example of a classic fund, Paul Mulvaney "The Freak" global markets fund at 30-40% loose vol target. The VAMI way outperforms the S&P.
Classic style, aiming for extreme convexity at the expense of vol & sharpe ratio. 
Quite a few triple digit 
---
2/4/26, 5:16 PM | Dan: Running TF can be a PITA if that's all you're doing, but if you have the capital and going to run a systematic account anyway, then it all happens with the same push of the button as everything else each day (or even 100% automated). Of course there'
---
2/4/26, 5:34 PM | MidKnight: Keep it coming @Dan not spam at all - thank you.
---
2/4/26, 8:24 PM | Jakub: DBMF's core customers are institutions. They like low vol. Less career risk for the allocator.
---
2/4/26, 8:24 PM | Jakub: Retail demand for TF ETFs is almost non-existent. Most struggle to get $50m AUM which is the breakeven point.
---
2/5/26, 2:21 AM | Sam: Shorting silver
---
2/5/26, 2:25 AM | Sam: Out minus 33 pips
---
2/5/26, 4:23 AM | -k: regarding trend following, macrocephalopod on twitter has a nice thread describing a simple implementation. it boils down to:


choose a set of asset classes (metals, rates, softs, equities, crypto, etc.).
,
calculate signals with ewmac(16,64), ewmac
---
2/5/26, 4:35 AM | Rachit: 2-12 momentum as in 2 period momo minus 12 period momo?
---
2/5/26, 4:46 AM | -k: yeah, which is more classic. i just did the carver ewmac thing
---
2/5/26, 5:15 AM | Sam: does the Turtle strategy still work?
---
2/5/26, 5:16 AM | Sam: https://oxfordstrat.com/coasdfASD32/uploads/2016/01/turtle-rules.pdf
---
2/5/26, 5:52 AM | Marco [reply]: Yeah, it all boils down to: follow the trend, size by vol, diversify
---
2/5/26, 6:08 AM | Sam: Cool, seems easier than carvery ewmac thang
---
2/5/26, 6:53 AM | MidKnight [reply]: What does it mean to "clip them" in your point 2?
---
2/5/26, 4:06 PM | Jakub: The difficult part of trend following is living with it. TF is like a hot bipolar girlfriend. Looks good in pictures, makes your life hell.
---
2/5/26, 4:57 PM | Dan [reply]: Pretty descriptive of trading in general for some cases too
---
2/5/26, 11:20 PM | Sam: NG storage in 10 mins
---
2/5/26, 11:47 PM | Sam [reply]: I'm out for +97 pips
---
2/5/26, 11:49 PM | Sam: @robotkris You are up very late?
---
2/5/26, 11:58 PM | robotkris [reply]: I need to go to bed! Having too much fun
---
2/5/26, 11:58 PM | robotkris: Sounds like you are too
---
2/6/26, 1:24 AM | FullMetal37!: @Sam for your event trades do you go long vol after the FOMC as well. Or just short over the event.
---
2/6/26, 4:14 AM | bdkoepke [reply]: You should net out the risk free rate and vol adjust (incorporating vol drag) when comparing sharpe ratios for products like these.
---
2/6/26, 4:29 AM | bdkoepke: Otherwise the sharpe on the lower vol funds will look artificially better.
---
2/6/26, 5:04 AM | Sam [reply]: I go long before the conference. I did that last time.
---
2/6/26, 5:11 AM | 4D: VIX is above 20, it's time to trade earnings!
---
2/6/26, 5:35 AM | Sam: I'm trading earnings. Shorting calendar put spreads.
---
2/6/26, 5:36 AM | Sam: On Amazon and Roblox. Shoulda done MSTR as well
---
2/6/26, 6:05 AM | 4D [reply]: I'm on AFRM, RBLX, IREN
---
2/6/26, 6:23 AM | Sam: What sort of structure? Short straddles?
---
2/6/26, 7:02 AM | 4D [reply]: yeah, straddle
---
2/6/26, 7:56 AM | Sam: do you have any hedge?
---
2/6/26, 10:30 AM | Dan [reply]: Oh I wasn't even using the return series, was just a rough eyeball of the percent gain vs the 7% vol that someone said DBMF was at.  True though if I did a proper comparison.
I found out afterwards that DBMF is higher than 7%  and the vols are closer
---
2/6/26, 5:48 PM | -k [reply]: Put together a demo based on this. Here's a notebook and data required to run it. Performance since 2015 is about 0.8 Sharpe and 13% CAGR when sized to a vol target of 15%. This has an overall beta of 0.2 and correlation of 28% to SPY, which would yi
---
2/7/26, 12:24 AM | Sam: https://www.hulltactical.com/2026/01/29/maximum-price-and-selling-behavior/ @Euan is this academic justification for what a price action trader would refer to as double tops/bottoms?
---
2/7/26, 12:25 AM | Sam: (just noticed it wasn't written by you! Still,  appreciate your thoughts)
---
2/7/26, 2:22 AM | Euan: I think it would be a bit of a reach to connect those. But maybe. You would need to actually pin down a ta person and make them say what they really mean.

(I write all of them)
---
2/7/26, 4:35 AM | Rachit: thanks for sharing that Sam, and for writing the piece Euan. It reminds me of the days since high factor in the crypto research and some more ideas to have a look at in the crappy crypto casino
---
2/7/26, 4:43 AM | Euan: Those blogs aren't really aimed at you guys but you might find some bits in there
---
2/11/26, 9:49 PM | Sam: NFP was great! +60 pips on UVXY, exited too early
---
2/11/26, 10:01 PM | Sam: Damn woulda made a 100...
---
2/12/26, 11:25 PM | Sam: Ng storage
---
2/12/26, 11:46 PM | Sam: +26 pips
---
2/13/26, 10:32 AM | 4D [reply]: Just wondering why , do you know any explanation to this trade by any chance?
---
2/13/26, 9:41 PM | Sam: NG is always volatile when the number comes out. You can expect a move one way or another. Maybe doing something with options is a better idea? @Euan ? But it will stop working just like everything else. Just a market inefficiency. Like the BOIL trad
---
2/13/26, 9:42 PM | Sam: +120 pips on short UVXY after CPI
---
2/14/26, 1:15 AM | si [reply]: BOIL fully in May NG now btw:

date,security_name,weight_percent,shares,market_value
2026-02-12,NATURAL GAS FUTR MAY26,199.92,16960,525590400
2026-02-12,NET OTHER ASSETS / CASH,,262906174,262906174.03
---
2/14/26, 3:35 AM | Euan [reply]: generally in situations like that, options are overpriced. So i guess you could play it by selling options but that seems to be contrary to what you want
---
2/14/26, 9:23 AM | alvin [reply]: Are you doing a directional bet? Some breakout at either side or something?
---
2/14/26, 8:08 PM | Sam: yeah short side
---
2/14/26, 8:54 PM | alvin: So it’s always a short ng during the announcement? Or it depends on some variables you’re looking at?
---
2/17/26, 2:08 AM | Sam: yeah, just short it.  Bear in mind that high Sharpe trades tend to fail as either people jump in or more likely, the market changes.
---
2/17/26, 2:49 PM | TimExcellent: Anyone else seeing the move on TMF/TLT is that an aberration?
---
2/19/26, 2:51 PM | mm: was looking at the "active etfs are trash" notebook james made and thought... yeah he's probably right about that.

in particular i thought about the plenty of covered call etfs that basically just blindly sell atm calls on the entire portfolio once 
---
2/19/26, 3:13 PM | TimExcellent: Well the shape at least within your inputs look interesting through that Covid drop
---
2/19/26, 3:36 PM | Stefan [reply]: i used to run this on all the single stock covered call etfs that they offered for a couple months last year, decently profitable even after borrow costs (i used a filter on those to exclude the ones with like 50% borrow) but as you mentioned the mar
---
2/19/26, 3:47 PM | mm: yeah it's hard to justify running it on something with "low" annual returns because the margin eats ~20%+ of your pnl. with nvda/tesla/etc it's a lot more plausible. could attempt using 2x/3x levered index etfs to see if the decay from those products
---
2/19/26, 4:35 PM | Stefan: yea plus youd lose the diversification benefit and probably end up implicitly timing when this works better vs when it doesnt... would be cool to run this if the margin would be the same as for a tight call spread on the long/short positions
---
2/19/26, 10:11 PM | ASlan: I mean arguably you could just buy the calls they’re selling no?
---
2/19/26, 10:40 PM | Stefan [reply]: sort of what it boils down do if they would do the covered call etf with underlying + short calls but from what I saw in their holdings (tbf havent checked in a while) they replicated their long delta via options as well
---
2/19/26, 10:40 PM | Stefan: and lets just say that didnt seem to be very efficient
---
2/20/26, 6:49 AM | Euan [reply]: A lot to unpack here.
Most active ETFs are bad. But most are only active in the sense that they actively do the same trade over and over. Trading a lot regardless of price is the height of dumb.

We don't do that. We go long or short a variety of str
---
2/20/26, 7:16 AM | FullMetal37! [reply]: Do you think recent underperformance has to do with the fact that vol selling has generally just been more crowded in the past few years? All these funds + retail learning about tastytrade mechanics etc. just a lot more indiscriminate price insensiti
---
2/20/26, 8:13 AM | mm [reply]: thanks for the feedback! 

my wording definitely wasn't the most precise. i agree that with covered calls you're getting both erp + vrp exposure.

i think my point was more that some of these cc etfs are terrible vehicles for capturing those premiums
---
2/20/26, 8:35 AM | Euan: Yes. There is no business that can sell a product regardless of the price. That is what the ETFs are doing.

The ETF biz is about sales. These funds have a good story. That beats performance every day
---
2/20/26, 9:18 AM | bdkoepke [reply]: If you go long QQQ, short QYLD (which is long QQQ, short a call on QQQ), then you really have QQQ -  (QQQ - QQQ Call) = long a QQQ Call.
---
2/20/26, 9:18 AM | bdkoepke [reply]: How would you look for "the right options"?
---
2/20/26, 9:24 AM | bdkoepke: I guess James looked into this a couple of years back.https://robotwealth.com/options-trading-with-cross-sectional-volatility-factors/
---
2/20/26, 9:32 AM | bdkoepke: I recall this paper from a few years ago: https://t1.daumcdn.net/brunch/service/user/gNua/file/4yxntZ5ON3opnpgymD7B73C-ios.pdf, I'm sure there are better ones.
---
2/20/26, 9:52 AM | Euan: No. No. No.
That is cross sectional. Finding stocks with cheap options relative to other stocks.

That works.

But please don't do it. It is a logistical nightmare. You need options on 50-200 stocks. Execution and cost management is crucial. And on a
---
2/20/26, 9:55 AM | MidKnight: @Euan I would like the 20% options recipe please. It's all hard (er)!
---
2/20/26, 9:57 AM | Euan: It is in vol trading and positional option trading.
---
2/20/26, 10:14 AM | bdkoepke [reply]: Thank you, that does help. I’m surprised that individuals would still be mispriced, but I suppose it makes sense given the number of strikes, expirations, etc.
---
2/20/26, 10:23 AM | Euan: cross sectional mispricing exists in options because exploiting it is hard. Valuation is easy but implementation is difficult.

In a single product the opposite is true.

The sweet spot is to watch a lot of things then trade when things get very misp
---
2/20/26, 10:27 AM | MidKnight: I've been sorta trying to use moontower for that over the past couple months. Problem I have with this concept is that cross-secnionally, almost any stock with VRP in it seems to be due to earnings for the most part. If I remove the stocks that have 
---
2/20/26, 10:59 AM | Euan: That's partly a problem w their screener. But even if that was fixed you would still have the big issue: these things are rare
---
2/20/26, 11:39 AM | veng1 [reply]: Some of the newer ETFs are changing their models.  Are you of the opinion they are all fundamentally flawed or are some, when adding dividends and NAV erosion, useful?
---
2/20/26, 12:43 PM | rodeo1203 [reply]: Isn't this the same as going long the ATM options? 

Two ATM monthly calls bought at each expiry, outperform the SPX imo over last 10 yrs atleast despite having same initial delta and are also more capital efficient.. would you say that the abundance
---
2/20/26, 1:01 PM | mm: my initial thought is that it'd mainly be the second thing. being long monthly ATM calls is going to look great not because of any structural vol mispricing but because number go up. i'm not sure if/how much 60-70b aum would impact things, especially
---
2/20/26, 1:36 PM | rodeo1203: ran something quickly in bloomberg, but this is the SPX 1month 50delta IV vs realized 30 day vol

while median VRP is positive(~0.45), mean is negative(~-0.4)... (i shifted the realized vol data in excel) so probably some edge in vol as well...
not s
---
2/20/26, 2:45 PM | FullMetal37! [reply]: Is your RV 30 trading or calendar days?
---
2/20/26, 2:48 PM | FullMetal37!: But broadly I think that tracks. Tariff tantrum was pretty rough. On a four year look back systematic selling 30dte spy straddles is breakeven/slightly positive I think.
---
2/20/26, 3:18 PM | Stefan [reply]: dont think that e.g. the yieldmax cc etfs hold the underlying at all, e.g. this are the current holdings in TSLY (the tesla one). So there might be something there but also doing the long/short probably was working for the reason that Euan mentioned,
---
2/20/26, 3:20 PM | mm: oh interesting i didn’t look at the yieldmax holdings
---
2/20/26, 5:53 PM | Stefan: tbf when I ran it my thought process was very sophisticated, theyre advertising 50%+ "yields" -> its not underlying + short calls -> simple backtest make line go up and right = I'm probably missing something, lets just try it
---
2/20/26, 10:48 PM | Sam: SCOTUS ruling on tariffs at top of the hr. Will short vol (smaller size than usual)
---
2/20/26, 11:09 PM | Sam: +155 ticks on UVXY
---
2/20/26, 11:25 PM | rodeo1203 [reply]: Bloomberg 30D calculation is 30 calendar days imo.. but yeah ATM vol seemed quite low for a while..
Picking up recently in the last couple months
---
2/20/26, 11:32 PM | FullMetal37! [reply]: Yea I mean it’s not exactly the same since it’s buying wings but the cboe has an Iron Condor and Iron Butterfly index. Both are basically flat over the last 4 yrs and have performed pretty badly since early 2010s. Which coincidentally coincides with 
---
2/21/26, 12:07 AM | rodeo1203: Yeah, also Cboe BXM is the covered call index (spx+ monthly ATM call selling)... that has been hammered brutally since 2010s
---
2/21/26, 12:07 AM | rodeo1203: When compared to just spx
---
2/21/26, 1:43 AM | Sam: Trump talking in 5 mins...might be worth shorting vol again...
---
2/21/26, 1:55 AM | Sam: Out for +50 pips.
---
2/21/26, 1:55 AM | Sam: No idea if he spoke or not
---
2/21/26, 2:21 AM | Sam: He's speaking now...I cba
---
2/21/26, 2:38 AM | Sam: There was at least 100 pips there....hope someone did it!
---
2/21/26, 5:58 AM | Marco [reply]: Do you have a list of this type of event trades that you do? Fomc, natgas... Ecc?
---
2/21/26, 7:06 AM | Euan [reply]: Those indices are suffering because of the drift of the indices. They don't actively rebalance like you would do with a short option position. 

Short vol did pretty well last year for example
---
2/21/26, 7:38 AM | MidKnight [reply]: Hi Euan, just so I completely understand what you mean. Could you please define vol trading and positional option trading? I googled positional option trading and it told me:
"Positional option trading is a long-term strategy involving buying or sell
---
2/21/26, 10:40 AM | Euan: I'm sorry I wasn't clear. I was referring to a copy of my books, "volatility trading"and "positional option trading '.
---
2/21/26, 11:12 AM | rodeo1203 [reply]: Hi @Euan, thanks for the insight.
What is the best way to measure the VRP we can harvest? Like VIX would be a variance swap calculation, is that (vs realized vol) a better proxy for understanding how rebalanced short strangles would have done
---
2/21/26, 12:37 PM | MidKnight [reply]: Maybe this helps? @71Ksander wrote this in the sharpetwo blog at the start of the year. See the section "variance swap as a retail trader".
https://app.sharpetwo.com/blog/what-structure-should-you-consider-when-trading-volatility
---
2/21/26, 1:47 PM | rodeo1203: Thank you
---
2/22/26, 9:07 AM | Euan: I was going to point you to that.
---
2/22/26, 1:16 PM | FullMetal37!: What's the RW thought on short vol implementation. When would you go long SVIX over short UVXY or vice versa? Is there a threshold where the borrow cost of shorting UVXY makes SVIX the better choice. Or perhaps SVXY since SVIX does that call buying t
---
2/22/26, 10:37 PM | ASlan: I believe most people are either short futures or short uvxy. Some short vxx.

I’ve not heard of SVXY but it looks pure volatility so could work but its only at 50% short so you’d need to buy more of it.
---
2/22/26, 10:40 PM | ASlan: The borrow rates are usually fairly small, and they tend to only be large when vol is high so the expected return relative to borrow cost would likely be quite high, though theoretically “optimizing” the strategy would have you farming around for the
---
2/23/26, 5:26 AM | Stefan: Here’s an idea for a RV trade that seems to sometimes come up (got the idea from Retail Options Trading where Euan talks about an IV RV trade between SPY & QQQ). 

VIX & VSTOXX are highly correlated and general move together so when somewhat dislocat
---
2/23/26, 5:26 AM | Stefan: That’s not tradeable though cause indices. Used data from firstratedata to get intraday futures data for both index futures and built a 30dte constant maturity futures for both and the effect is still there, just not as massive (still tradeable imo).
---
2/23/26, 5:26 AM | Stefan: I went through some iterations on how to potentially trade this (I won’t spam the channel with all the things and plots I looked at, happy to share though). Trading the actual spread is fine however with min ticks and always having to do VSTOXX futur
---
2/23/26, 5:27 AM | Stefan: Result has sharpe 1.2 – 1.6 depending on precise implementation (time of day for the signal, zscore lookback) and as an added benefit really low correlation to e.g. the uvxy/vxz trade.
---
2/23/26, 6:19 AM | MidKnight: @Stefan Thanks for sharing this! I like this a lot.
---
2/23/26, 7:24 AM | William: @Stefan  there are several papers on this concept. I did some analsis of it, with somewhat similar results. The risk is that, while highly correlated, there are occaisionally big dislocations which can occur when one of the 2 exchanges is closed (in 
---
2/23/26, 7:33 AM | William: a key issue is to adjust for the USD-EUR exchange rate, as the 2 contracts are denominated in their local currency. so the ratio of contracts will change as the FX changes
---
2/23/26, 1:21 PM | Dan [reply]: I like using VXX, initial margin short side is 30% compared to 120% for UVXY on IBKR.
Anecdotally I've found it easier to borrow as well, and it appears to be lower borrow rates. Two things to keep in mind though:
a) Size it larger than UVXY because 
---
2/23/26, 1:24 PM | Dan: I do use SVIX too though, because multiple VIX systems I spread the risk management method a bit - VXX has a stop loss in case there's Armageddon (even though it can only execute in market hours), and my SVIX version has no stops because it can only 
---
2/23/26, 1:30 PM | Dan: One other thing with SVIX: SVXY can be used earlier in the backtest before SVIX exists, then switch to SVIX after that.
The leverage rate does change through history though. E.g after volmageddon in 2018 I think. So for each of the 3 stages you'd wan
---
2/23/26, 3:16 PM | Stefan [reply]: yea, sorry did a bit of a sloppy job explaining on the trade implementation. that wouldnt trade the indices spread but just the (perceived) dislocated side using a calendar for protection (+margin). In the stat-arb strat we looked at just trading the
---
2/23/26, 7:57 PM | Sam [reply]: Short vol trades: fomc, CPI, Trump major scheduled speech, anything big that there is uncertainty and will move markets. Nvidia earnings this week is a strong possibility.  The NG trade is just an inefficiency which works till it doesn't.
---
2/23/26, 9:56 PM | Euan: I think NG is a risk premium. But nothing is ever just one thing
---
2/23/26, 11:46 PM | Henboss [reply]: You should only short vol when it's overpriced... if you just short vol over every event you will blow up sooner rather than later
---
2/23/26, 11:54 PM | Euan: True. But I've never seen an event when vol isn't overpriced. And you never need to be naked short vol. That is asking for trouble.
---
2/23/26, 11:55 PM | Euan: I've pretty much been selling event vol for 30 years and have managed to not blow up (yet)
---
2/24/26, 1:38 AM | Marco [reply]: Regarding this issue. The short earning trade is putting naked straddles, or I am wrong?
---
2/24/26, 1:42 AM | Euan: yes
---
2/24/26, 1:44 AM | Marco [reply]: I have heard before that one should always have a "equal" number of long and short options. I guess this is incompatible with the earnings trade
---
2/24/26, 1:57 AM | Euan: i think i said once that the most robust risk control is to be net long options, but that isn't a 100% firm rule (nothing ever is). So almost always I'm long long dated index options or something. I dion't think you need to be in every individual pro
---
2/24/26, (edited) | Euan: In the NVDA i lost more money on QQQ calls than the actual NVDA straddle.
---
2/24/26, 2:17 AM | Sam: I'm out of the $BOIL trade. A few days early, but it's ok. Decent profit overall. Thanks @Euan
---
2/24/26, 5:25 AM | 4D: both gld and slv are up and their vol are up a lot as well.
---
2/24/26, 5:26 AM | 4D: The Shanghai silver markets reopen later today after 10 day suspension during Chinese New Year. Silver shortage is everywhere
---
2/24/26, 10:53 AM | William [reply]: Oh that's a cool implementation. I wouldn't have guessed that the "mispricing " would be rapidly mean reverting (in the sense that the mispriced contract reverts in absolute terms), but you've got data and i just have feelings
---
2/24/26, 10:53 AM | William: The calendars are a nice idea too
---
2/24/26, 7:29 PM | Rachit: is there stuff in the lab on rp7 / tlaq / general rph implementations using futures?
---
2/24/26, 10:00 PM | Yan: The Risk Premia On Steroids course deals with futures
---
2/25/26, 10:37 PM | Sam [reply]: Shorted uvxy late last night ahead of the State of the Union address. Didn't do much though. Covered at the open for +102 pips
---
2/25/26, 10:51 PM | llIHeroic: do you have a way of tracking short vol day trades versus constant exposure short vol, which would be picking up all these events and in theory collecting additional ambient vrp carry?  what is the reasoning for incurring extra costs for going in and
---
2/25/26, 11:06 PM | Sam: I track the individual short trades. I put on very large size for those and they are a separate strategy to being short vol (with hedge) all the time. By large size, I mean 10x the short vol all the time strategy. There's no way I could hold a consta
---
2/25/26, 11:11 PM | llIHeroic: interesting.  decent short vol strat is like 0.80 to maybe 1+ sharpe i'd say.  how long have you been running this short term event strat and is the sharpe really high enough to justify 10x exposure?  hard to believe there is that much prem in there 
---
2/26/26, 4:28 AM | Sam: I've been doing it for a few years now. I think Euan said he's being doing it for 30 years!
---
2/26/26, 5:16 AM | Euan: there might be something implementable in this.
---
2/26/26, 5:16 AM | Euan: https://www.sciencedirect.com/science/article/pii/S0378426625001761
---
2/26/26, 5:17 AM | Euan: it is sort of second level to the order imbalance and ETF rebalancing trades that worked prretty well for a while
---
2/26/26, 4:46 PM | mm: been on a big levered etf dive lately and looked through this paper: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5421274

shorting the 3x long etf, hedging with the appropriate amount of the underlying. rebalances monthly to target 1:3 ratio.
---
2/26/26, 5:06 PM | MidKnight: That's really interesting about this difference. I wouldn't have expected it.
---
2/26/26, 5:08 PM | MidKnight: I mean the japanese vs usa opposite is such a similar shape. suprises me
---
2/26/26, 6:04 PM | alvin: There’s barely any shorts available in JP at all, at least in IBKR, except for the large caps
---
2/26/26, 6:04 PM | mm: if i understand it correctly the US 3x long etfs use swaps to get leverage so they're constantly paying interest on the borrowed notional but jp uses futures for those same products so the carry/roll has more of an impact
---
2/26/26, 6:04 PM | mm: both sides work in jp
---
2/26/26, 6:04 PM | alvin: I’ve looked into that. Any sort of shorting in JP looks amazing, till I checked their short inventory and realised there’s nothing (in IB)
---
2/26/26, 6:06 PM | mm [reply]: ive never traded anything outside of the US so i have no clue what borrow is like for jp/eu/etc
---
2/26/26, 6:06 PM | mm: makes sense though
---
2/26/26, 6:06 PM | alvin: The 3x levered ones usually results in 4-5% pa, close to the risk free rate. Same for the highly liquid 2x ones

The ones that looks decent actually is the BTC etfs. Returns 10-14% a year.
---
2/26/26, 6:07 PM | alvin: At a 1+ sharpe
---
2/26/26, 6:08 PM | alvin: Ive traded that, problem i noticed straight off is the shorts might not have borrows when i fire a MOC for rebalancing. So im usually end up taking directional risk (slightly) with the long leg
---
2/26/26, 6:09 PM | alvin: Traded for a bit but i stopped, concerned a huge major move + no borrows will probably wipe off a year of profit
---
2/26/26, 6:10 PM | mm: that's good to know. indexes looks like ~4-7%, been stronger in recent years. only things i've found >10% have been semis, biotech, and gold miners for some reason
---
2/26/26, 6:37 PM | Stefan [reply]: ive been running this on the crypto etfs now for a bit (on BTC, ETH, SOL, XRP), the big moves are not so much of a concern but the rebalancing is like @alvin mentioned. especially with uptick rule in effect, one needs to be a bit nimble in terms of s
---
2/26/26, 6:42 PM | Rachit [reply]: do you hedge with the spot on a crypto exchange?
---
2/26/26, 6:43 PM | Stefan [reply]: nope i use the spot etfs, IBIT, ETHA, BSOL, XRP. BSOL & XRP quite newish, BSOL is very nice as its staked SOL
---
2/26/26, 6:44 PM | Rachit: ah right on, that makes more sense
---
2/26/26, 6:44 PM | Stefan: (this comes out when a non crypto person does crypto stuff)
---
2/26/26, 6:45 PM | Stefan: i rebalance losely around bands and eyeball general exposure of all pairs together (i just assume if one dumps all probably dump, so if my exposure is off +5% on some and -5% on the others i might rebalance if theres liquidity/borrow or dont and assu
---
2/26/26, 6:52 PM | Stefan: the "cool" thing with this is you have the carry + the levered etfs, so the borrow fees dont kill it (imo)
---
2/26/26, (edited) | Stefan: ideally it'd margin better but cant have it all
---
2/26/26, 8:57 PM | Rachit [reply]: any suggestions for a reasonable borrow rate (or range) to use for a drity sim of these things?
---
2/26/26, 9:06 PM | Stefan [reply]: this is what i had in live. im using BITI for the BTC variant (so long the short etf) because BITX has usually > 5% borrow and BITU has mostly swaps so youre losing out on the carry part (and my simple BT looked better using BITI, sue me  ). might sw
---
2/26/26, 9:10 PM | Stefan: let me know what comes out
---
2/26/26, 10:03 PM | alvin: I actually split bitu and bitx half half back then to solve (minimise) the borrow issue , there were a couple times both (!!) didn’t have shorts available
---
2/27/26, 12:01 AM | Sam: minus 36 pips on gas trade
---
2/27/26, 5:05 AM | 4D [reply]: would you trade PPI tmr?
---
2/27/26, 5:22 AM | Sam: No. Don't think it's that big a number.
---
2/27/26, 7:55 AM | MidKnight: I don't know how you guys dig into all this stuff (recent LETF discussion). I'm in awe at you guys. Thanks for the inspiration. @mm  @Stefan @alvin
---
2/27/26, 9:38 PM | Sam [reply]: Might have been wrong! Still, if you did the trade and exited by now, would only be a small loss