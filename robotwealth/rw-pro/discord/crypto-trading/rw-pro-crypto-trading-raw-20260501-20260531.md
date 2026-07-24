# RW Pro Discord — #crypto-trading raw transcript

- **Period:** May 1–31, 2026
- **Channel:** https://discord.com/channels/1368787013763072040/1368845831113015346
- **Message count:** 44
- **Extraction method:** Browser automation (Claude in Chrome) against the live Discord DOM, using Discord's `in:crypto-trading after:2026-04-30 before:2026-06-01` search to bound the range, then scroll-and-merge extraction of the message list, trimmed to exact May 1–31 boundaries. Some individual messages are capped at 250 characters by the extraction tooling; these are marked `[capped]` below where the cutoff is mid-sentence. Two capped messages (brad_smith, Rachit on 5/30) were minor anecdotal asides and were left capped since the gist is preserved.

---

5/1/26, 3:06 AM | 4rtfj8: Hey guys! I created this new funding rates dashboard at https://arbs.fyi/ that currently supports 18 different exchanges and thought I'd share. There are two different tabs you can use:

"Rates By Exchange" which lists every available exchange X perp pair with current and aggregated funding rates and

"Compare Exchanges" which lists each perp on the vertical axis and exchange on the horizontal axis. This makes it easy to compare the funding rates across exchanges. On this page, you can also select whether to see current rates or aggregated rates.
---
5/1/26, 6:21 PM | hecta [reply]: Just a heads-up: validators will vote to delist MAVIA on the 5th https://app.hyperliquid.xyz/announcement/15voh4lxgo2
---
5/5/26, 1:07 AM | Kamil [reply]: Thank you for letting me know, I already closed it. It was a good farm for a few weeks.
---
5/6/26, 3:48 AM | Stefan: CME BTC Vol futures coming june 1st apparently
---
5/6/26, 6:25 AM | Euan: Like a vix?
---
5/6/26, 1:00 PM | Stefan: based on this: https://www.cmegroup.com/markets/cryptocurrencies/volatility.html
"Calculated by applying a standard variance swap pricing model to isolate pure volatility exposure."
---
5/6/26, 7:34 PM | Euan: This could be really good
---
5/6/26, 9:43 PM | robotkris: Party time
---
5/7/26, 12:11 PM | nxtrador: plz elabor8 for a friend - how is CME bitcoin vol good. We just going to sell vol?
---
5/7/26, 9:44 PM | robotkris [reply]: We'll likely find that BTC variance premium is large and persistent. A BTC vol future gives you a lot of scope to express variations on that view. Term structure effects become interesting too. Directly tradable and as signals. Likely some RV opportunities against existing crypto vol products. And more that I haven't thought of…
---
5/7/26, 9:49 PM | Euan: The carry should behave very similarly to the vix carry so a short front/ long back seems promising
---
5/21/26, 8:05 PM | Matt G: On the Crypto Yolo strategy and API, when are we due to do an asset refresh @robotkris ?

I'm thinkng about moving to trade on CME micro futures because of some operational challenges on the Dex's and I do worry a bit about credit risk there. I picked up on the last video session that @Euan does this on CME and it got me thinking more seriously about it.

I notice that on CME whilst BNB, DOGE, and TRX are not available the other 7 crypto assets are so we can run the 7 now on CME. Also I see CME has an XLM and SUI micro future which are not in our 10. What would be the critieria to include other assets such as those when we do a refresh? Thanks
---
5/21/26, 8:24 PM | Euan: No. I DID it on CME but stopped. The big difference is that the CME closes over the weekend and I got hammered a few times due to saturday moves
---
5/21/26, 8:52 PM | Matt G: Interesting thanks @Euan
---
5/21/26, 9:51 PM | Euan: If YOLO had been killing it I would have done some real analysis on weekend risk, but I was super busy and YOLO wasn't going through a great run
---
5/21/26, 10:07 PM | {Overly Powerly}: yeah YOLO has been awful this year
---
5/21/26, 10:19 PM | Stefan [reply]: this looks like it might change, just got this [capped]
---
5/21/26, 10:31 PM | Euan: I think on balance, 24hr trading is going to be horrible for me
---
5/21/26, 10:52 PM | Matt G [reply]: Very interesting. That might work well for me.
---
5/22/26, 9:52 AM | robotkris [reply]: We're due for a refresh. I'll get it in the schedule for next week.
---
5/23/26, 12:34 AM | {Overly Powerly}: does anyone know if there is historical data for Hyperliquid spot markets?
---
5/23/26, 1:01 AM | emsin44 [reply]: hydromancer.xyz
---
5/23/26, 1:01 AM | emsin44: Check out their reservoir
---
5/23/26, 1:59 AM | {Overly Powerly}: thanks
---
5/27/26, 3:16 PM | robotkris: @here we are due a refresh of the yolo universe. AVAX and LINK should come out, and HYPE and ZEC should go in, according to coingecko. Admittedly I haven't been paying as much attention to crypto lately with all the focus on equity stat arb, so I am a little out of the loop. Wanted to ask if anyone sees any issues with adding these cryptocurrencies to the yolo universe? The NEAR token has slightly lower market cap, but trades more average volume than ZEC. There's also BCH and XMR which have more runs on the board, but slightly lower market cap.

The yolo simulation uses a universe defined purely on market cap, so we should default to that unless there's a good reason not to.
---
5/27/26, 5:28 PM | Matt G: I'm OK with those changes @robotkris . I wonder as a question though, would it break things if we kept more assets in on the API and then we choose which basket we want to trade, a bit like with the stat-arb? I can't remember if the final factors rely upon the cross-sectional factors relative to the basket of the top 10 or not? If so then of course what I am suggesting would not work out of the box.
---
5/27/26, 5:50 PM | robotkris: I've been thinking about this.... I think it's a really good idea and something I want to move towards. I definitely prefer supporting people build their own portfolios (and there's decent evidence that looking outside the top 10 is a good idea).

To do this, we'd need to push raw ticker-wise factor values and let the user do the cross-sectional ranking downstream, based on their own universe. The current yolo factors endpoint essentially takes that decision away from you and does the ranking for you. So it's easy to use and simple, but totally inflexible. The yolo factors endpoint does a little bit of both - serves some raw time series factors, and serves some cross sectionally normalised factors (based on the 10-asset universe assumption).

I think the solution would be to keep the weights endpoint as is (so people can continue trading yolo as is if they wish), but expand the factors endpoint, or make a new one.
---
5/28/26, 4:59 AM | Michael: no easy way to change part of the process by adding the asset-size as a variable you can decide with? Or this is more I want assets 1-5, 10-15 in the rank etc? You would need some kind of list of tickers to be fed into the filtering.
---
5/28/26, 5:27 AM | Dave: this would be dope

with hyperliquid having tradfi markets, has anyone investigated running a momentum/trend strategy on a mixed universe of crypto and tradfi assets? would it even make sense to research this?
---
5/28/26, 10:36 AM | llIHeroic: Yeah I was thinking about how AVAX is so small now. Refresh to HYPE and ZEC would be nice.

When building this out what were the differences in sharpe between using 5/10/20 top mcap? If there's no meaningful improvement expanding basket size, simple coin swap and continuing to work on other stuff seems like it would be fine imho
---
5/28/26, 4:02 PM | robotkris: We'll do the coin swap for now, and build out a factor endpoint for a broader universe (when we clear the decks a bit).
---
5/28/26, 5:40 PM | SatoriNakaMoto: Most of the momo factors apart from rrp and range have shown sign of decays or regime bashed which gives some pointer on a potential future webinar to understand and investigate some frameworks on alpha decay and retraining @robotkris @Euan
---
5/28/26, 5:54 PM | phraktle [VOID], Server Tag: VOIDVOID: https://x.com/phraktle/status/2059931768929579126
---
5/29/26, 5:31 AM | Dave [reply]: This is awesome! I'm trying to get started with arb stat in crypto too but I don't really know where to start in terms of universe selection
---
5/29/26, 11:48 AM | robotkris: @here we're aiming for the yolo universe refresh after US market close Friday. Just getting all our ducks in a row in our staging environment before pulling the trigger.
---
5/30/26, 5:29 PM | faz: i cant find hype on binance UK ....
---
5/30/26, 7:06 PM | mr_bluesky [HYPE], Server Tag: HYPEHYPE [reply]: Sounds good, especially re. maintaining the existing functionality. I think the pre-canned way you do it currently is already probably great for many/most. I know from having implemented Unravel that there is significant additional complexity, so for the non-quants among us (or learners like me) it's great to have the choice. One request if you are planning on opening it up, would be to make it possible to align/integrate with the Unravel factor universe i.e. implement rolling top-10, -20 or -40. Their universes are a lot more volatile. Only if it's not a massive PITA obvs. Cheers.
---
5/30/26, 8:04 PM | Rachit: lol ccxt picked the exact perfect day to bug out
---
5/30/26, 9:19 PM | robotkris [reply]: I think the way we'd do it would be to cover an even broader universe, and just serve the raw factor values and leave it up to the user to build their own universe and their cross sectional signals.

That's one level up from what Unravel do - serve portfolio weights for specific universes. I like that approach because it gives you ultimate flexibility. But with that flexibility comes some complexity.
---
5/30/26, 9:20 PM | robotkris [reply]: There should be a perp, if there isn't a spot market.
---
5/30/26, 9:35 PM | mr_bluesky [HYPE], Server Tag: HYPEHYPE [reply]: Sounds good
---
5/30/26, 11:06 PM | brad_smith [reply]: Haha this happened to me too today. Since I was using an older version of ccxt, the load markets call for hyperliquid crashed and had to update the library. Thought I would be good, then ran into another issue during order execution where my private [capped]
---
5/30/26, 11:17 PM | Rachit [reply]: Lol yeah I had the same issue with the load markets call trying to load a null spot mkt.

I just directly edited the hl implementation in the lib 😆

In hindsight not a bad day for something to go wrong since I'd set aside some time expecting something [capped]
