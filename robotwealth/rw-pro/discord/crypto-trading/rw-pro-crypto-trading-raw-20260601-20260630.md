# RW Pro Discord — #crypto-trading raw transcript

- **Period:** June 1–30, 2026
- **Channel:** https://discord.com/channels/1368787013763072040/1368845831113015346
- **Message count:** 83
- **Extraction method:** Browser automation (Claude in Chrome) against the live Discord DOM, using Discord's `in:crypto-trading after:2026-05-31 before:2026-07-01` search to bound the range, then scroll-and-merge extraction of the message list, trimmed to exact June 1–30 boundaries. Some individual messages are capped at 250 characters by the extraction tooling; these are marked `[capped]` below where the cutoff is mid-sentence.

---

6/1/26, 4:14 AM | SatoriNakaMoto: @robotkris what if instead f 1 rebalance per day we rebalance portfolio at every 1 hr it will help with two things: anything that has gone disproportionately high or low will get soothened out, and I think it will help with overall portfolio variance
---
6/1/26, 4:15 AM | SatoriNakaMoto: upside is can be be really scalable and better execution px if done correctly
---
6/1/26, 5:24 AM | {Overly Powerly}: i think fees might be an issue rebalancing that often
---
6/1/26, 6:20 AM | SatoriNakaMoto: but the turnover will be lower i guess
---
6/1/26, 6:21 AM | SatoriNakaMoto: my rationale is since we are momentum heavy portfolio we dont have to wait 24 hr for rebal we can capture the shift early on
---
6/1/26, 9:14 AM | llIHeroic: It's probably higher sharpe by a very slight degree but trading longer lookbacks at higher freq doesn't really add much performance generally
---
6/1/26, 9:15 AM | llIHeroic: You actually need to pair higher trade freq with faster signals and they you do really start butting into cost frictions
---
6/1/26, 9:15 AM | llIHeroic: So it's more of an infrastructure question. Kind of starts to become a different game than what most of us are trying or able to do
---
6/1/26, 10:36 AM | robotkris: If you can get on top of your execution, and you can tune your no-trade buffer to handle the more frequent turnover, in theory it's decent idea. But those are two big "ifs" and forcing a slower rebalance cadence makes those issues go away.

One big issue you'd need to deal with - there are mean-reversion effects that show up on a sub-daily timescale that are essentially unmodelled in our framework. You'd want to understand the impact of that as well.
---
6/1/26, 1:30 PM | SatoriNakaMoto: Agreed that there are some nuances that are easier said than done, esp how to hande trade buffer but this thought stemmed up from rather than turnoving the portfolio if i churn my portfolio small bit i can be on the maker side and lower my exec cost by a factor of 2
---
6/1/26, 1:30 PM | SatoriNakaMoto: this way we can also look at some high turnover factors
---
6/1/26, 1:31 PM | SatoriNakaMoto: but yeah its cumbersome
---
6/2/26, 7:54 PM | mr_bluesky [HYPE]: Bit of a long read, but an interesting profile of the founder of Hyperliquid, Jeff Yan, here: https://colossus.com/article/beyond-the-sky-jeffrey-yan-hyperliquid/
---
6/5/26, 3:46 PM | iaminarush: With how things are looking zec might be out of the universe on next refresh
---
6/5/26, 4:53 PM | llIHeroic: Yeah that was quite unfortunate timing on the switch
---
6/5/26, 4:53 PM | llIHeroic: Hindsight 20/20 but maybe longevity in top mcap should be factored in somehow
---
6/5/26, 4:57 PM | llIHeroic: I guess it's 50/50 we could have been pointed the right way though so having so unstable coins just add var and don't cost much/any model ev per se
---
6/5/26, 4:59 PM | iaminarush: I think kris is already using some sort of rolling mcap for universe selection, hard to avoid every edge case
---
6/5/26, 5:17 PM | llIHeroic: I don't think it's rolling but I could be mistaken. I largely agree though a lot of this you can't see coming
---
6/5/26, 6:32 PM | {Overly Powerly}: the strange thing is (it seems) is this is not even a new bug it was known about for a long time
---
6/5/26, 6:55 PM | Rachit: What happened?
---
6/5/26, 7:23 PM | {Overly Powerly}: there could be an infinite minting bug in ZEC and as its private there is no way to truly account for it
---
6/5/26, 7:24 PM | {Overly Powerly}: https://x.com/zooko/status/2062644925590900980
---
6/6/26, 12:27 AM | mr_bluesky [HYPE]: I guess this is testament to the robustness of the YOLO algorithm, that it can withstand being long such a name
---
6/8/26, 3:32 PM | robotkris [reply]: Being net short at the moment helps... probably should replace ZEC with something else though.
---
6/8/26, 11:16 PM | mr_bluesky [HYPE] [reply]: It's an interesting one, as the furore may be entirely FUD - I don't think there is actually any proof that anyone exploited the hole before they patched it? May end up being a buying opportunity..
---
6/14/26, 1:56 AM | emsin44: https://x.com/the_delta_dog/status/2065787614762803330 interesting signal from L/s ratio from nance
---
6/14/26, 4:01 AM | Ewan: im almost certain this is an Unravel factor
---
6/15/26, 11:20 AM | robotkris [reply]: This is where the trade buffer really pays for itself
---
6/16/26, 12:21 PM | Malhar: hi everyone
tiny question about getting started on hyperliquid - what methods do people use to deposit money? I'm trying to find a good fiat on-ramp to deposit money into metamask, then move it to hyperliquid.
Metamask has its own on-ramp quote, but its charging a pretty steep price
---
6/16/26, 2:01 PM | emsin44 [reply]: Where are you based?
---
6/16/26, 2:55 PM | robotkris [reply]: Highly dependent on where you live, like Emsin alluded to. Let us know where you're based and we can suggest some options.
---
6/16/26, 3:35 PM | Malhar: based in India for the summer
---
6/16/26, 4:50 PM | emsin44 [reply]: Probably just check the different cex's that allow it. There's also peer.xyz that does p2p but I'm not sure what the regulatory stuff on that is
---
6/16/26, 11:06 PM | mr_bluesky [HYPE] [reply]: I used Kraken last time and they were good from here in Switzerland
---
6/16/26, 11:08 PM | mr_bluesky [HYPE]: FYI: TON has just delisted (off Hyperliquid already at least - I think Binance not until EOM) and is rebranding to GRAM - but Hyperliquid didn't list that one yet, in case anyone is wondering why their strategy is a position short like I was...
---
6/17/26, 3:04 AM | SatoriNakaMoto [reply]: if u are doing INR -> USDT/C-> be wary of taxmen in India, if u have any offshore account outside infia it will be defo better, binance works in India
---
6/17/26, 3:05 AM | SatoriNakaMoto: indian authorities are very wary of INR leaving the system in wake of recent depreciation
---
6/18/26, 2:09 AM | Dave: Hey guys, with Hyperliquid (and other exchanges too) offering tradfi markets in the same place as crypto perps, is anyone experimenting momentum/trend strategies that use a mixed universe of crypto and tradfi markets?
---
6/18/26, 5:29 AM | mm: https://x.com/coindesk/status/2067212744193872038
---
6/18/26, 5:30 AM | mm: when i move money from my left pocket to my right pocket and owe the government 0.2% of it
---
6/18/26, 5:48 PM | Malhar: hi
question about pnl/trade management: ik we're supposed to think about trades as continuously evolving weights rather than discrete entry/exit, but how do people approach managing positions?

one approach seems going in take-profit/stop-loss figu [capped]
---
6/18/26, 7:45 PM | Rachit: i think it will depend on the strategy but generally i'm adjusting positions as a function of the signal/edge, and volatility (either of the instrument or the strategy/portfolio)
---
6/18/26, 9:21 PM | robotkris [reply]: It's like Rachit says... at any given time, you'll be able to calculate your ideal positions. You then compare that ideal with what you actually have. And depending on how much they differ and what your costs are, you trade from your actuals towards [capped]
---
6/19/26, 1:14 AM | Malhar: I think I was confused because of the coinbase ui - I put on my first position, and it shows an open trade for that. I was wondering if the next time I wanted to adjust my position, would I have to open a new trade or just add to the existing positio [capped]
---
6/19/26, 3:27 PM | emsin44 [reply]: Might be worth comparing coinbase fees against other venues
---
6/19/26, 3:41 PM | {Overly Powerly} [reply]: id go as far as to say it is totally worth to do so
---
6/19/26, 5:51 PM | Malhar [reply]: the only decent ones operating here are binance, coinbase and kucoin, and at least for the time being, coinbase is offering lower taker fees than the others
---
6/19/26, 6:38 PM | emsin44 [reply]: Oh wow, that's surprising. I always had coinbase down as having extortionate fees
---
6/20/26, 11:26 PM | mr_bluesky [HYPE] [reply]: I think this must be a very common experience. I am playing around with the Hyperliquid dataset, and was looking at creating signed volume imbalance (based on which side crossed the spread) on short-term bars (300-, 600-tick etc.). Turns out this looks AMAZING. Before you add in the round-trip costs, alas... You'd probably need to have a market-maker spec execution layer in any case 😆
---
6/21/26, 2:00 PM | Malhar: ik this is extrapolative, but from the dashboard, trend seems to have had a bad time this year, carry seems to have fared better. The dashboard default settings are equal weights on trend, carry and momo, but how do people approach overall factor wei [capped]
---
6/21/26, 2:14 PM | Malhar: also, does the api expose individual signals or only factor-level aggregates?
---
6/21/26, 4:32 PM | mr_bluesky [HYPE] [reply]: I just equal weight everything. Trend has had a tough time as we were in a mean reversion phase by and large for much of the time. Trend will dominate again at some point. The trick is knowing when. 😉
---
6/21/26, 4:36 PM | mm: you could try and build a simple model that will predict/calculate the optimal weights but yea equal weighting is an easy shortcut
---
6/21/26, 4:38 PM | mm: really you just wanna make sure you have enough weight on the trend/momo factors for whenever they ultimately kick in
---
6/22/26, 11:25 AM | robotkris [reply]: You won't be able to harness a microstructure edge in isolation, but it's the sort of thing that can help your execution in some cases (not as easy as it sounds though), or that you might stack with other edges.
---
6/22/26, 1:50 PM | robotkris: mr_bluesky started a thread: "You won't be able to harness a..." (thread marker, no additional message content)
---
6/22/26, 8:09 PM | Malhar: rookie question: i read in a couple of places that a composition of trend strats vs a long-short momentum portfolio are similar in many important aspects, though there's obviously differences. If the core aim is 'winners keep [capped]
---
6/22/26, 11:15 PM | robotkris [reply]: They look like two flavours of the same thing, but they're actually quite different things. Trend is about things going up or down relative to their own history. Momentum is about things that have gone up/down more than their peers continuing to do s [capped]
---
6/23/26, 8:57 PM | mr_bluesky [HYPE] [reply]: I definitely think it would be worthwhile researching a crypto strategy that targets tradfi assets like the XYZ listings on Hyperliquid, yes - main reason being that I already trade Unravel and YOLO and so have exposure to the top-n crypto universe.
---
6/24/26, 12:05 AM | SatoriNakaMoto: How much does Unravel cost @mr_bluesky
---
6/24/26, 1:43 PM | mr_bluesky [HYPE] [reply]: The answer is: it depends (sorry - there are two tiers that you can take - tier 3 is materially more expensive than tier 2, but there are more factors available to you, as well as a pre-canned optimal strategy rather like the way YOLO is served. Th [capped]
---
6/24/26, 4:43 PM | mm: somebody go steal this guys money on kraken wtf
---
6/24/26, 5:31 PM | Michael [3024]: at the risk of sounding a n00b what is unravel?
---
6/24/26, 5:41 PM | iaminarush: A company providing factors/portfolios for crypto, they have a channel in here
---
6/24/26, 6:35 PM | Michael [3024]: ah ok, now I see, sorry.
---
6/25/26, 3:52 AM | Alex [reply]: Is this actually kraken btc perp? Mine doesnt look like that at all and I would be surprised if there were spikes like that.
---
6/25/26, 3:55 AM | mm: kraken us perps?
---
6/25/26, 3:56 AM | mm: there's like a few mil of volume
---
6/25/26, 3:56 AM | mm: idk if the trades actually print or not
---
6/25/26, 3:57 AM | mm: but the other ones i checked didn't have those wicks so im not sure
---
6/25/26, 3:41 PM | Alex: Weird, mine looks way more liquid with no spikes. Maybe because its EU not US.
---
6/26/26, 3:05 AM | mike: I think I remember a while ago there was a strategy people were doing with crypto perps on FTX or something like that. Am I remembering this correctly/is this still a thing?
---
6/26/26, 3:08 AM | Rachit: which strategy? FTX isn't a thing so....

there was the eod rebalance thing that was like free money but there hasn't been an exchange as dumb as that since (that i know of)
---
6/26/26, 11:35 AM | robotkris [reply]: There are a few:

Perp basis,
Carry (various forms),
Trend/Momentum,
Short new listings,

They're all written up in rw-portfolio: https://github.com/RWLab/rw-portfolio
---
6/26/26, 10:11 PM | mike [reply]: Anybody still trading them on other platforms? I just saw perps are now available on Kalshi
---
6/28/26, 4:38 PM | hecta [reply]: I'm testing long-short carry on binance since May. Very recent, so I don't have much to report. It was mostly going sideways but just got a nice 9% bump because luckily I was on the right side of the MUSDT meltdown - got ADLd unfortunately, but still [capped]
---
6/29/26, 12:22 AM | Dave: Hey Kris, I was taking a look at all the wonderful work that's being done with stat ARB, I was wondering if there are plans to get crypto back in the webinars sometimes
---
6/29/26, 10:24 PM | Malhar: are we supposed to be agnostic to market sentiment while trading carry? Carry is the first set of signals I implemented and planned to start trading - but I'm slightly afraid of getting caught on the wrong side of intraday moves
---
6/29/26, 10:56 PM | llIHeroic: How would you hedge market beta without trading partially or almost completely against the carry signal?

IMO just side down until the amount of volatility you're inventorying feels like harmless noise. You can always size up later if conviction gro [capped]
---
6/30/26, 5:55 PM | Malhar: does anyone use pnl attribution to see which signals/factors are doing well and which ones are not? If so, are there any good libraries for it or is it diy?
---
6/30/26, 6:15 PM | mm: chapter 11 of advanced portfolio management - paleologo goes into this. you can find a pdf in like 5 seconds. bit dense math wise if you aren't familiar but can throw it into your favorite clanker llm and it'll help.
---
6/30/26, 9:22 PM | Malhar [reply]: thanks!
