# RW Pro Discord — #tradfi-trading raw transcript

- **Period:** April 1–30, 2026 (no channel activity April 1–5; first message is April 6)
- **Channel:** https://discord.com/channels/1368787013763072040/1370226295941763154
- **Message count:** 82
- **Extraction method:** Browser automation (Claude in Chrome) against the live Discord DOM, using Discord's `in:tradfi-trading after:2026-03-31 before:2026-05-01` search to bound the range, then scroll-and-merge extraction of the message list, trimmed to exact April 6–30 boundaries (confirmed via direct scroll-up that no messages exist April 1–5; last message before April 6 is from March 31). Some individual messages are capped at 250 characters by the extraction tooling; these are marked `[capped]` below where the cutoff is mid-sentence.

---

4/6/26, 2:14 PM | Mark Aron | Unravel: https://www.linkedin.com/posts/leonardo-falconi-bb930b5a_i-just-published-my-personal-take-on-why-ugcPost-7444722088772390913-QRV0
---
4/6/26, 2:15 PM | Mark Aron | Unravel: maybe can be made systematic
---
4/7/26, 3:55 AM | TheCTAFan: The latest Flirting With Models pod, is full of commodity futures related risk-premia ideas to explore, including description of market participants behavior, why those premia have not been arbed away, and little crumbs of edge. Totally worth a liste [capped]
---
4/7/26, 6:34 AM | Dan [reply]: I liked this one, was actually thinking "The congestion trade" could be a good one to explore. Buy futures before BCOM and PDBC etc roll, sell after they roll and flip short (just like the window dressing trade).
Could also be explored in individual [capped]
---
4/7/26, 6:35 AM | Dan: The other dynamic thing is choosing which contracts to trade it on, if the front month is already crowded for this trade by CTAs we may do lower liquidity months that are still liquid enough for retail guys like us.
---
4/7/26, 6:36 AM | Dan: Curve carry is also good but it's a huge project to do in a diversified manner, I trade a single legged version of it but it took months to get to the final version. The congestion trade would be a lot easier to explore from an edge perspective.
The [capped]
---
4/7/26, 8:43 AM | robotkris [reply]: We should put these on our list of stuff to look at. These sorts of trades are right up our alley.
---
4/7/26, 8:54 PM | Euan [reply]: Crowding isn't always a bad thing. First, it only happens when something is winning. You never get crowded out of bad trades. But, more importantly, it can actually help. When you are betting on reversion crowding will help to push prices back to whe [capped]
---
4/7/26, 9:55 PM | Dan [reply]: Interesting thanks. I was thinking it might also depend on how much trading happens and in what order, e.g. if we enter the trade 5 days before the roll, and CTAs enter 4 days before the roll, then that's fine (even helpful) for us.
I'd think we shou [capped]
---
4/7/26, 9:59 PM | Dan [reply]: Unrelated question then too since you mentioned crowding - what do you think of the COT traders that believe markets are crowded based on COT large speculator positioning being higher than normal (crowded), and they follow the commercial traders (hed [capped]
---
4/7/26, 10:43 PM | Euan: I've never tested that but I vaguely recall that that stuff hasn't worked since the days of the market wizards
---
4/8/26, 11:39 AM | Dan [reply]: Was interesting because the  interview with David Druz (back from those old days) used COT in the opposite way, trading against the commercials. Either it doesn't work so people can think they use it in both ways, or one of them is wrong, or it flipp [capped]
---
4/8/26, 6:09 PM | akhan: Hi All. I was just look at the EOM Equity Bond rebalancing trade. Are the rules given at this page https://github.com/orgs/RWLab/projects/1/views/5
the latest ones ? Or has the strategy been updated since Jan 8th, 2024 ?  i  [capped]
---
4/8/26, 6:11 PM | mm: think that should be up to date. the plot at the bottom goes up through jan 26 and its implemented properly so you should be good.
---
4/8/26, 6:21 PM | robotkris: The Edge Database you linked to is up to date, but I'm trying to make the rw-portfolio repo the central and current source of truth for all this stuff. It's a bit more useful to get you actually trading this thing: https://github.com/RWLab/rw-portfol [capped]
---
4/8/26, 6:22 PM | akhan: Cool. I will take a look it @robotkris . Thanks
---
4/8/26, 6:23 PM | robotkris [reply]: No problem! Shout if anything isn't clear... that would be good feedback for me to include anything that's missing in that doc.
---
4/8/26, 6:23 PM | akhan: sure. Will do
---
4/8/26, 8:26 PM | Euan: Just a few pre-opening VIX thoughts. There have been moves like this in the VIX before, and sometimes when VVIX was much lower. So statistically this is just something that happens. But the difference here is that this is associated with a 2 week cea [capped]
---
4/9/26, 7:25 AM | ASlan: Euan out here making posts worthy of the macro tourism channel
---
4/10/26, 8:34 PM | Sam: small loss of 8 pips of NG gas yesterday
---
4/10/26, 8:35 PM | Rachit: this might be of interest to some https://papers.ssrn.com/sol3/papers.cfm
---
4/10/26, 8:35 PM | Sam: +20 pips on short vix ahead of CPI
---
4/11/26, 6:04 AM | Dan [reply]: Interesting, looks like a bit of data collection for very short term trades. But should be achievable if can get the data I think. Should work on futures or spot I assume.
---
4/11/26, 7:37 AM | Rachit: yeah the data bit feels a bit out of reach for me tbh + anything fx related im super suspicious of once i add on the commissions
---
4/11/26, 7:46 AM | Dan [reply]: Futures should work I think, especially the liquid ones should be arb'd to match vs the time to expiry. Low commisions, and spread if it's the liquid markets.
---
4/11/26, 7:46 AM | Dan: The closing times can be different to spot though, not sure how much of the paper would rely on that would need to look into it more.
---
4/13/26, 6:24 AM | Sascha [reply]: Maybe I missed this: What was the trade?
---
4/13/26, 6:35 AM | ASlan: There is a nat gas storage announcement every thursday at around 10 ish that he shorts beforehand. Similar concept to short vix before cpi or whatever.

Though I don't know the stats on how good it is
---
4/13/26, 6:13 PM | TheCTAFan: I played with numbers for full-day variant of this (short Wed EOD, close Thu EOD), and it seems to be working better over autumn / winter months.

The chart is pre-cost NG 2000-2026 total return monthly (4-5 trades usually), and also does not accoun [capped]
---
4/13/26, 8:09 PM | Euan: Sunday night reversal again.
---
4/15/26, 6:55 AM | hac: https://watcher.guru/news/sec-approves-ending-pattern-day-trader-rule-25k-minimum
---
4/15/26, 7:03 AM | halves: Hmmm... More alpha!
---
4/15/26, 3:49 PM | Jack: market makers right now
---
4/15/26, 5:56 PM | Dan: Might be a good thing, stop beginner traders putting in too much money at the start just to avoid the PDT rule. Better for them to start with $5k rather than $25k and continually top it up to avoid the rule.
---
4/15/26, 5:57 PM | Dan: We don't have the rule in Aus as far as I know, never made sense to me to say "hey you're a beginner, we're going to restrict you unless you put even more money at risk"
---
4/15/26, 8:19 PM | Euan: the original rule was put in place to protect traders from themselves. can't see why that isn't still an issue but that has fallen out of favor now. it is the same as the cboe pushing 0dte to increase their volumes without paying too much attention t [capped]
---
4/16/26, 12:01 AM | rodeo1203 [reply]: top indicator?
---
4/18/26, 1:00 AM | Michael TW 88: going through the webinar @robotkris - what was the mechanism for the end of the month window dressing that was set straight by a fixed income asset manager who joined us?
---
4/18/26, 1:03 AM | chi [reply]: This is the newsletter where Kris shared the story on bond flows by Teckk: https://robotwealth.com/rw-pro-newsletter-welcome-and-new-insights/
---
4/18/26, 1:04 AM | chi: Oh, there's also this Discord update for the same thing and Teckk's original message
---
4/18/26, 9:53 PM | 𝕋𝕠𝕤𝕙𝕚 [reply]: I came in here for exactly this question too
ty chi
---
4/20/26, 7:44 AM | Euan: I'm going to take a shot on a Sunday night reversal
---
4/20/26, 8:00 AM | MidKnight: How might you be wanting to express that @Euan ? Pretty crazy rally the last couple weeks
---
4/20/26, 8:10 AM | Euan: Just trade futures. And take them off tomorrow morning.

My only thesis is that Sunday night opens are wrong

It is just a tiny position. I haven't done any real analysis

Also don't anchor yourself to what has happened. "Crazy rally" isn't predict [capped]
---
4/20/26, 8:26 AM | Dan [reply]: Would be interesting to see if there's any signal in weekend IG trading being wrong as well. I'm sure some are trading/fading it already
https://www.ig.com/au/indices/markets-indices/weekend-us-tech-100-e1
---
4/20/26, 11:38 AM | Dan: robotkris started a thread: Oh, there's also [this Discord update](. See all threads.
---
4/21/26, 4:34 PM | Michael TW 88 [reply]: It's only Tuesday
---
4/21/26, 10:07 PM | alvin [reply]: How will you be managing this? A couple of trades/weeks won't mean much, but seems "haphazard" to be trading this long term without proper analysis? Or just putting it on for some feel?
---
4/21/26, 10:08 PM | Euan: just winging it. it is firmly in the 5% fuck around and find out bucket
---
4/21/26, 10:15 PM | alvin: What would you be trying to find out though? Like eg after 3 months it looks good, (or bad), gonna shift to another basket? what's your thought process behind trades in that bucket?
---
4/21/26, 10:35 PM | Euan: well it has been making money so i'm going to try and get some :). this is not a serious trade. ignore me on this one
---
4/22/26, 2:18 AM | Sam: I did the same, it's a punt and you hope that the rather small sample persists one more time!
---
4/22/26, 4:08 AM | llIHeroic: What I found interesting was how much the Sunday open informs BTC pricing on big moves
---
4/22/26, 4:09 AM | llIHeroic: On some of the initial tariff weekends BTC was trading with full access to news flow all weekend but the ES print would wildly smash BTC up or down immediately.  Remember seeing that several times
---
4/24/26, 2:30 AM | Sam: NG storage: last week was a scratch. This week was +50 pips.
---
4/24/26, 5:06 AM | FullMetal37! [reply]: What are you using to trade NG? The futures? Or an etf?
---
4/24/26, 3:36 PM | Sam [reply]: I use CFDs
---
4/24/26, 3:36 PM | Marco [reply]: Same here
---
4/25/26, 2:16 AM | Euan: Ok. Did some actual analysis on the Sunday reversal. Doesn't work.

Has worked this year, but only a 0.16 Sharpe.

Doesn't really work in general
---
4/25/26, 2:48 AM | Sam: Temporary inefficiency probably caused by the war?
---
4/25/26, 3:25 AM | Euan: i think just luck
---
4/25/26, 10:44 PM | deal_me_in: Is there a reason why country equity ETFs might mean revert the day after big moves in either direction?

Is mean reversion like trend… known effect; ambiguous reason?
---
4/25/26, 10:48 PM | deal_me_in: AI notes the following possibilities:

Time Zone Arbitrage and Stale Pricing
Many country ETFs (like the EWG for Germany or EWJ for Japan) trade in New York while their home markets are closed.
• The Effect: If there is a massive move in the S&P 500  [capped]
---
4/25/26, 10:49 PM | deal_me_in: Liquidity Provision (The "Rubber Band" Effect)
When a country ETF moves 3-5% in a day, it usually requires market makers to take the other side of massive order imbalances.
• To compensate for the risk of holding these positions overnight, market mak [capped]
---
4/25/26, (edited) | deal_me_in: I guess both of those are testable.
---
4/25/26, 11:30 PM | Marco [reply]: https://open.substack.com/pub/layquant/p/trading-country-themed-etfs
There are some research links here about that
---
4/25/26, 11:47 PM | deal_me_in: Ha yeah well… that is where I got the idea to do some research on this. I can confirm the effect is there. And you don't have to do it  with IBS. I confirmed it with z scores.
---
4/25/26, (edited) | deal_me_in: But that backtest blog and the paper it's based on provide no explanation
---
4/26/26, 12:09 AM | deal_me_in: I'm looking for ex-US equity exposure which is how I got to this exact paper and idea. But I don't recall RW doing anything like this.

I recall another paper that explained mean reversion in il ETFs with illiquid underlyings and was wondering if th [capped]
---
4/26/26, 5:51 AM | brad_smith: @robotkris @hac which data vendor do you get your earnings data from? are we allowed to ask this? also is there a place that lists which data vendors you use? curious to know this list
---
4/26/26, 7:19 AM | hazler: Anyone played around with closed-end fund trading?
---
4/26/26, 9:11 AM | deal_me_in [reply]: I've been meaning to build a discount to nav screener of CEFs but haven't yet. What are you interested in them for?
---
4/26/26, 9:47 AM | hazler [reply]: cefconnect looks reasonable and free as a screener. I was looking at things like mean-reversion of discounts, new activist involvement, etc
---
4/26/26, 9:49 AM | deal_me_in: Nice I'll check it out. I have a link to something somewhere. I wonder if that's it.

Yeah mean reversion of discounts is the hypothesis… you see any evidence?
---
4/26/26, 9:50 AM | hazler: not yet, just started thinking about this stuff earlier today tbh
---
4/26/26, 9:57 AM | deal_me_in: The Armageddon videos talk about this… buying discounts during market panic.
---
4/26/26, 10:03 AM | hazler: I found one candidate where it almost looks like the opposite, where NAV looks like it's rising faster than price
---
4/26/26, 7:12 PM | deal_me_in: Oh that is interesting
---
4/30/26, 3:07 AM | FullMetal37!: @Sam nat gas tomorrow right? Do you enter on the open or today at the close?
---
4/30/26, 3:09 AM | Sam: i enter just before the report and exit 15 mins to 30 mins after.
---
4/30/26, 9:16 PM | Marco: Remember that tomorrow is Holiday in most of the civilised world, I expect a very quiet day
