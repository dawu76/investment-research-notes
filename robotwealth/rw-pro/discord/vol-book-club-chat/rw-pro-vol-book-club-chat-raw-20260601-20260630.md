# RW Pro Discord — #vol-book-club-chat raw transcript

- **Period:** June 1–30, 2026
- **Channel:** https://discord.com/channels/1368787013763072040/1387280068182540390
- **Message count:** 40
- **Extraction method:** Browser automation (Claude in Chrome) against the live Discord DOM, using Discord's `in:vol-book-club-chat after:2026-05-31 before:2026-07-01` search to bound the range (43 buffered search results), then scroll-and-merge extraction of the message list, trimmed to exact June 1–30 boundaries (no activity June 1–3, 6–9, 13–15, 20–24, 27–30). Two messages were capped at 250 characters by the extraction tooling; both were separately recovered as full text from the live DOM and are reproduced complete below.

---

6/4/26, 4:48 AM | nxtrador: If I'm bullish on quantum but IV for quantum ETFS is super high do I do a call spread or just delta 1 it and buy spot
---
6/4/26, 7:33 PM | Euan: Well first I would find a good psychiatrist to get to the bottom of these unusual thoughts.

But if your thesis is just "bullish" (that autocorrected to "bullshit". I need a laugh too) then just buy the stock.

And, seriously, well done for checking yourself. the "i am an option trader" mindset is a very real trap.
---
6/5/26, 5:19 AM | nxtrador: Hahahah Euan. This post alone made my yearly subscription worth it
---
6/5/26, 8:29 PM | Sam: nfp in 1 min
---
6/10/26, 8:20 PM | Sam: cpi in 10m
---
6/10/26, 8:45 PM | Sam: +50 pips on June VIX
---
6/10/26, 9:07 PM | Sam [reply]: This was minus 5 pips
---
6/11/26, 4:20 AM | 4D: Short VXX on NFP + CPI + FOMC, enter 1 min before the event, exit 5 minutes after the event, mid-price [attached: backtest equity curve chart, log_ret_cum_sum vs. date, 2024–2026]
---
6/12/26, 11:45 AM | robotkris [reply]: Very nice!! Thanks for sharing mate
---
6/12/26, 8:32 PM | Euan: this is a good place to check reg t margins https://wealthbee.io/margin-calculator/
---
6/16/26, 9:14 AM | William [reply]: this is very nice. Could you clarify your timing on entry and exit - do you mean minutes before and after? Or hours, etc. My understanding of the FOMC trade was that most of the vol resolution happened in the couple of days prior to the announcement
---
6/16/26, 10:03 AM | 4D: minutes before and after. For FOMC, open at 1:59pm, close at 2:05 pm.
---
6/16/26, 5:12 PM | GeirN [reply]: Thanks for posting this 4D. I did some work on getting hold of news events based on your post, and since I was at it I added in a few more and ran just the stat for all of them to see what they yield. Jobless claims seem to have good numbers as well, but there are many of them, and I haven't tested with transaction cost. Don't know if this helps, but it was an interesting excercise for me, and also quite likely that I have made mistakes somewhere
---
6/16/26, 5:24 PM | GeirN: one small note - I flipped the sign on jolts in the table above, i.e. assuming going long [attached: results table by eventKey × year (2021–2026 + Total), covering adpEmployment, advanceEconomicIndicators, cpi, fomcPressConference, fomcStatement, gdpAdvance, housingStarts, industrialProduction, ismManufacturing, ismServices, joblessClaims, jolts, nfp, ppi, retailSales, pce]
---
6/16/26, (edited) | GeirN: I cleaned up the one news event where I flipped the sign - all values are positive for short now [attached: code screenshot + updated results table]
---
6/16/26, (edited) | GeirN: massive_prices_get is just my implementation of the massive.com stocks API. I use duckDB as a cache to speed up data retrieval and fetch only the newest data (if realtime = TRUE)
---
6/16/26, (edited) | GeirN: and newsEvents_get uses the urls listed to pull news events.
---
6/16/26, (reply) | GeirN [reply]: that surprised me as well
---
6/17/26, 7:49 AM | 4D [reply]: great work! but it seems that the return on nfp days is really good only in 2024.
---
6/17/26, 11:02 PM | Sam: Bear in mind that there's a new Fed chairman...
---
6/17/26, 11:06 PM | Sam: I've seen some stats that say after a new chair is appointed, the S&P500 has gone down in the following 3 months. The sample size is of course small.
---
6/18/26, 1:39 AM | Marco: Anyone playing the FOMC? What's the trade usually?
---
6/18/26, 1:42 AM | Rachit: short announcement, long presser
---
6/18/26, 1:50 AM | FullMetal37! [reply]: Wait so is positive number here positive return for short vol?
---
6/18/26, 2:10 AM | GeirN: I have been out the whole day, and it is pretty late here, so I'll post details on how I did my analysis tomorrow morning
---
6/18/26, 2:24 AM | GeirN: actually it was quicker than I thought to document - here is what my code looks like.
---
6/18/26, 2:25 AM | GeirN: I cleaned up the one news event where I flipped the sign - all values are positive for short now
---
6/18/26, 2:27 AM | GeirN: massive_prices_get is just my implementation of the massive.com stocks API. I use duckDB as a cache to speed up data retrieval and fetch only the newest data (if realtime = TRUE)
---
6/18/26, (edited) | GeirN: and newsEvents_get uses the urls listed to pull news events.
---
6/18/26, 2:30 AM | GeirN [reply]: that surprised me as well
---
6/18/26, 2:48 AM | Sam: minus 1.7% on the short vol FOMC trade
---
6/18/26, 2:49 AM | GeirN: caveat: do not trust my analysis I can share my functions if it helps
---
6/18/26, 2:50 AM | Rachit [reply]: very much looks like the inverse of the usual today. still few mins left to the presser tho
---
6/18/26, 3:05 AM | Sam: I exit in the first 15 mins. This time should have exited at 15 mins to the top of the hr
---
6/18/26, 9:01 AM | Euan: The fomc vol trade has been a bit useless for the last few years.
---
6/19/26, 6:59 PM | Sam: It's not been good this year.
---
6/19/26, 7:37 PM | mm: i didn't start trading it consistently until the beginning of this year
---
6/19/26, 7:37 PM | mm: my timing is perfect
---
6/19/26, 10:24 PM | Euan: I haven't lost money but it used to be the most consistent winner ever. I think it went for 4 years without a loss
---
6/25/26, 8:17 PM | Sam: Core PCE in 15 mins. Mulling whether to short vix in front of it...
---
6/25/26, 8:26 PM | Sam: shorted a small amount
---
6/25/26, 8:28 PM | Sam: I'm sure you could just go long ES rather than screwing around with short VIX futs
---
6/25/26, 8:32 PM | Sam: +15 pips (always a winner when you have a small amount on!)
---
6/26/26, 11:03 PM | Euan: although the negative relationship between equities and vol is very strong, uncertain events like economic releases disproportionally affect vol
