# RW Pro Discord — #tradfi-trading raw transcript

- **Period:** May 1–31, 2026
- **Channel:** https://discord.com/channels/1368787013763072040/1370226295941763154
- **Message count:** 58
- **Extraction method:** Browser automation (Claude in Chrome) against the live Discord DOM, using Discord's `in:tradfi-trading after:2026-04-30 before:2026-06-01` search to bound the range, then scroll-and-merge extraction of the message list, trimmed to exact May 1–31 boundaries. Some individual messages are capped at 250 characters by the extraction tooling; these are marked `[capped]` below where the cutoff is mid-sentence.

---

5/1/26, 12:14 AM | Sam: USA is not on holiday. Nor is the UK, but not sure we would classify us as civilised anyway 😴...
But not expecting a quieter day than usual. 1st day of the month, perhaps some equity flow comes in.
---
5/1/26, 12:15 AM | Sam: Minus 15 pips on NG storage
---
5/1/26, 12:15 AM | Rachit: orange man still has internet access
---
5/1/26, 12:41 AM | FullMetal37! [reply]: You mind sharing your live performance on this?
---
5/1/26, 2:50 AM | Sam: Live performance?
---
5/1/26, 2:50 AM | Sam: As in doing the trade live?
---
5/1/26, 3:01 AM | FullMetal37! [reply]: Yea like how you've been doing in actual performance
---
5/1/26, 3:02 AM | Sam: I post the performance every week.
---
5/1/26, 3:16 AM | Quarry614 [VBT] [reply]: Yes you do. I've tried a couple of these as well. Would you do it differently if the VIX was already very low/high; or that doesn't matter since just trying to capture the move on the specific event?
---
5/1/26, 3:20 AM | Sam: No, this is just a naive strategy, trying to capture move on a specific event. I think @4D tested it out, had high Sharpe. But high Sharpe strategies crumble. So wouldn't go crazy on it.
---
5/1/26, 7:48 AM | Dan [reply]: Thanks I had no idea.. Aussies no holiday either.
AUKUS are busy people! Though early in the year I see a lot of US holidays disrupting trading..
---
5/1/26, 7:50 AM | Dan: Seems TLT trade (window dressing + rebal) a bit of a sting this month, but AUM ATH so it's doing the uncorrelated thing which I can't complain about.
Still got the short side of WD to go, fingers cross it's not bounce time for TLT
---
5/1/26, 8:05 AM | Rachit: ya wan't fun seeing that tank. I also added some canadian bonds into the window dressing trade this month albeit in small size
---
5/1/26, 1:55 PM | robotkris [reply]: Yeah one of the worst months for that trade. Timing risk innit
---
5/1/26, 2:34 PM | mm: https://x.com/nequalonetrader/status/2049962857861693738
---
5/1/26, 2:41 PM | Dan [reply]: Curious if anyone's implementation is cutting size when both rebalance and window dressing take on TLT at the same time?
I size the rebal TLT position the same notional size as SPY would've sized (ie not vol-adjusting for TLTs lower vol). A lazy way [capped]
---
5/4/26, 3:52 PM | Yan [reply]: I'm asking myself the same question... Not sure about it! So far I just go full size on each, even if it is TLT on both trades.
---
5/4/26, 3:52 PM | Yan [reply]: Last week was bad indeed, but WD has been doing very well this year
---
5/8/26, 10:04 PM | Rachit: well im glad i didn't take the short end of the bond rebal
---
5/8/26, 10:52 PM | Stefan [reply]: closed it yday so basically implicitly up
---
5/9/26, 1:31 AM | Yan: Closed the short yesterday for a tiny profit...
---
5/9/26, 9:41 AM | Dan [reply]: The short side of window dressing hurt too.
But as always, sizing is key..
That one month though puts window dressing from positive well into negative though (for my start date anyway). Patience..
---
5/9/26, 9:43 AM | Rachit: yeah absolutely a noisy effect
---
5/9/26, 6:49 PM | danielscapital: Stumbled upon this thread.

https://x.com/derekinvest6/status/1971617580877336731

Looks quite interesting, might look a bit over complicated but looks like a bumped of version of a RP strategy.

Curious does anyone ru [capped]
---
5/12/26, 9:27 PM | Sam: lost 40 pips on ng storage last week...was fortunate exited pretty quickly
---
5/12/26, 10:01 PM | Euan [reply]: can you post in a way that doesn't make me log into X?
---
5/12/26, 10:02 PM | Rachit [reply]: hopefully this works without a login https://threadreaderapp.com/thread/1971617580877336731.html
---
5/12/26, 10:11 PM | Euan: thank you!
---
5/13/26, 8:55 PM | hac: https://www.cnbc.com/2026/05/12/new-futures-market-for-semiconductors-comes-as-ai-drives-costs-skyward.html
---
5/13/26, 8:58 PM | Rachit: does this mean saas firms building out futures trading desks
---
5/14/26, 2:33 AM | danielscapital [reply]: I think his claims are must to be false. But the mean reversion/timing layers looked quite interesting.
Also the ticker selection looks interesting no?
---
5/14/26, 7:30 AM | Dan [reply]: It does look like heavy recency bias.
That period being good for Bitcoin, Gold, and QQQ.
For QQQ in particular it has excluded the poor period of 2000-2010 where it just lost money for 10+ years straight, and then around the start of the test is the [capped]
---
5/14/26, 9:50 AM | TimExcellent [reply]: Yep can't wait for this, I hope I don't macro think my way to losing money on it, but I immediately thought of the way it seems like no one really knows what is going on with data center buildouts and chips
---
5/14/26, 4:31 PM | danielscapital [reply]: I think we're looking at it from different angles.

On QQQ and gold, I think the critique depends on what the strategy is actually trying to do. If you frame this as a beta amplifier with timing overlays rather than a diversified risk premia portfoli [capped]
---
5/14/26, 8:29 PM | Dan [reply]: Yep, gold does have a fair reason to include it.
QQQ maybe too because of the high beta like you mentioned.
As long as not using the high sharpe for portfolio optimisation and allocation etc, knowing that it may be different in future.
Makes sense to [capped]
---
5/15/26, 1:23 AM | FullMetal37!: What's the "Kelly Ratio" in the latest portfolio construction session?
---
5/15/26, 4:14 AM | Edux [reply]: Should be the Kelly Criterion, a formula that determines the optimal fraction of capital to allocate to a position in order to maximize long‑term logarithmic growth.
---
5/15/26, 6:40 AM | Marco [reply]: Mean over variance I think
---
5/15/26, 7:29 AM | Euan [reply]: Sorry. I shouldn't have presumed.

@Edux is right. The kelly criterion is to maximize log growth. The kelly ratio is the proportion to invest that fulfils that criterion. And an approximate equation for that ratio is mean/variance.

I should do a pre [capped]
---
5/15/26, 1:13 PM | Matt G: Do VCs add value? I thought this analysis from Bouchard et al is interesting. Makes it difficult [capped]
---
5/15/26, 7:40 PM | Euan: they are an entire industry of pershing squares
---
5/15/26, 10:14 PM | Rachit: anyone ever looked into the holiday effects outside the US market? or it is a very american thing?
---
5/17/26, 8:10 AM | ASlan: I know it doesn't work for btc.
Which doesn't answer your question but is mildly interesting.
---
5/17/26, 10:39 PM | Euan: Interesting. BTC used to have very pronounced day of week patterns. They gone now?

Used to make the ftx move contracts very easy to trade
---
5/18/26, 5:06 AM | mm: shorting move on saturdays and longing/shorting xyz shitcoin ahead of them predictably rebalancing their 3x bull/bear tokens was some of the easiest money ever
---
5/18/26, 5:09 AM | mm: in hindsight i was a moron for keeping money somewhere that would lose so transparently
---
5/20/26, 12:51 AM | Andre: here what he means by "basis between forward S&P volatility and /VX futures" its what hurricane slayer tries to do?
---
5/20/26, 2:09 AM | Euan: well he just said it was a signal. not a signal to do any particular thing. tbh a lot of what he says sounds a lot more profound than it really is
---
5/21/26, 7:05 PM | Sam: NG storage gas trade: didn't do last week, was on plane to Switzerland, just as well as it was a loser. Not sure if I will do today..
---
5/22/26, 12:35 AM | Sam: Small win, I exited after 5 mins
---
5/22/26, 12:37 AM | Sam: Heads up, US holiday on Monday, better odds (62% v 52%) than usual of being up day tomorrow. Buy index futures, hold till close.
---
5/28/26, 8:24 PM | Dan: 2:1 share split for BOIL today, if anyone still doing other trades on it.
https://www.proshares.com/press-releases/proshares-announces-etf-share-splits-052826
---
5/28/26, 9:10 PM | Sam: ProShares Decline of the Retail Store ETF...great name!
---
5/28/26, 9:21 PM | Sam: Ticker: EMTY
---
5/30/26, 1:02 AM | Sam: End of month trade: buy stock index futures at 20-30 mins before close and exit at close.
---
5/30/26, 12:34 PM | 4D: spaceX ipo on June 12, and join nasdaq 100 on June 27. Would it replicate the move of TSLA in 2020 when it was going to join sp500.
---
5/30/26, 7:36 PM | Matt G [reply]: Interesting. I feel very tempted to short it once it hits the index.
---
5/31/26, 1:54 AM | Sam: Thing is all the index trackers etc would have to buy it....
