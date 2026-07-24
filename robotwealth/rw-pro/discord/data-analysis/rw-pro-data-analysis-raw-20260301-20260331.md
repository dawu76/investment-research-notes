# RW Pro Discord — #data-analysis raw transcript

- **Period:** March 1–31, 2026
- **Channel:** https://discord.com/channels/1368787013763072040/1368844739465707572
- **Message count:** 28
- **Extraction method:** Browser automation (Claude in Chrome) against the live Discord DOM, using Discord's `in:data-analysis after:2026-02-28 before:2026-04-01` search to bound the range, then scroll-and-merge extraction of the message list, trimmed to exact March boundaries. Channel activity was clustered into three windows this month — March 10–12, March 20, and March 28–31 — with multi-day silent gaps between them.

---

3/10/26, 10:41 AM | Ben: I have been looking at revamping my PEAD model and I came across the twin momentum paper in the equity factors pod.  It caught my interest as I use momentum in some of my PEAD fundamental features.  Thought I would do some quick analysis of the features in the paper and some technical momentum features.  Interesting results which are sparking further thought around PEAD v2 model.  This is just the raw features, Russell 1000 stocks, 2010 to 2025.
---
3/10/26, 10:45 AM | Ben: I then added technical momentum and weighted each feature according to IC and stability (nothing scientific, higher IC and stability gets more weight)
---
3/10/26, 2:40 PM | robotkris: That looks very good. What's the source of your fundamentals data?
---
3/10/26, 2:47 PM | Ben [reply]: FMP
---
3/10/26, 2:48 PM | mm: is their data reliable? i tried messaging their support with a simple question and it said it'd be a few business days before i got a response and they just never answered it
---
3/10/26, 2:56 PM | Ben [reply]: Personally I haven't had any problems with it but I have heard others mention that there have been data quality issues and figures have been retrospectively updated.  Been using them just over a year.   Obviously I want the best quality data possible, but if a few bits of dodgy data here and there is going to break my system I have bigger problems.
---
3/10/26, 3:07 PM | mm: agreed. i used their free stuff for a few quick tests but havent paid for it yet. mainly wanted historical earnings estimates from it.
---
3/10/26, 3:11 PM | robotkris: Those results look very good...better than I would have expected. Any chance they might be serving you revised fundamentals, rather than what was reported at the time?
---
3/10/26, 3:13 PM | Ben: I will have more of a look.  I have been using accepted date for PIT alignment.

    "date": "2024-09-28",
        "symbol": "AAPL",
        "reportedCurrency": "USD",
        "cik": "0000320193",
        "filingDate": "2024-11-01",
        "acceptedDate": "2024-11-01 06:01:36",
        "fiscalYear": "2024",
---
3/10/26, 3:15 PM | Ben: My PEAD system seems to be travelling ok in live testing.  Will eventually re-download all the data from FMP and compare to what my weekly update one looks like .
---
3/11/26, 12:14 AM | blue664203 [KONG], Server Tag: KONGKONG: Thanks for sharing @Ben . Is the Russell 1000 stocks a snapshot at the end of 2025?
---
3/11/26, 4:26 AM | bdkoepke: Has anyone used the direct XBRL feeds for fundamentals? My understanding is that the data isn't normalized (which is a PITA), but it should have as reported and revised. https://xbrl.us/membership/benefits/. Zacks has both as well, normalized, but with less resolution.
---
3/11/26, 7:43 AM | Ben [reply]: It consists of current and past constituents but not all past constituents are available.  The further back you go the less are available.  I think there were about 2000 symbols from memory.
---
3/12/26, 7:47 PM | TimExcellent: https://x.com/databentohq/status/2031717025903485005?s=46&t=N-bRxq_vUy3zqgpzvnA6zA HK stocks and Futs coming to databento
---
3/20/26, 10:20 AM | Rachit: hey @robotkris Given I'm comparing something like vix3m with a synthetic vx30 position using 1d interval data,

Won't the analysis be borked bcs vix3m closes at 4pm but the futures keep trading so the close prices of the 1d bar would be for different times??
---
3/20/26, 10:24 AM | MidKnight: RTH close should still be the close for the futures daily bar, no?
---
3/20/26, 3:53 PM | robotkris: Depends what the close price in your futures data is... if it's settlement, it should be closer to VIX timing I think. I think it'll leak a little information either way, but should be OK for research on slower moving stuff. Still, worth being aware of. Do you know what the close price represents? You could lag your futures data by a full day and see what impact that has.
---
3/20/26, 6:03 PM | Rachit: ill see if lagging changes things. Building out an aggregated dash of all the vix signals we've talked about and  was working through the synthetic vx30 - vix3m premium zscore. Got wildly different numbers between using raw daily and rescaled hourly data (both from ibkr).

I'll need to do some double checks with a fresher brain.
---
3/20/26, 10:40 PM | robotkris [reply]: Nice mate. This has been on my list of things I want to do for ages... great that someone is doing it. I think it would be really useful.
---
3/28/26, 5:31 PM | TimExcellent: I'm taking a stab at recreating the UVXY/VXN with VX futures, >2018 is sort of a magic era perhaps, I know I will have done thing incorrectly but the return path from when abouts VXN was launched looks about right from eye balling it.  >2018 Equity curve included... I feel like I've done something wrong anyway... I'll see if I can export a notebook but probably a bit complex as would have to ship my data caching with it.
---
3/28/26, 6:53 PM | TimExcellent: Adaptive roll of VX futs based on trying to understand the curve only.
---
3/30/26, 1:14 AM | ilikepizza314: How are the CMs constructed? Pair of contracts weighted to target a maturity in calendar days?
---
3/30/26, 10:43 AM | TimExcellent: Yes. For each date, find the two VX futures that bracket the target DTE (one ≤, one >), weight linearly by distance:
near_wt = (far_DTE - target) / (far_DTE - near_DTE)
CM_price = near_wt * near + (1 - near_wt) * far

Weights shift daily as DTE counts down. No discrete roll dates — just continuous interpolation to 30 or 150 calendar days.
UVXY holds 1st + 2nd month by contract rank, rolling daily on a business-day schedule between settlement Tuesdays. VXZ holds 4th through 7th month — 5th and 6th at static full  weight, only 4th→7th rolls so four contracts, not two.

My CM_30 and CM_150 loosely targets the same tenors but use DTE-bracketing instead of monthly rank, and always two contracts instead of four for the mid-term leg.
---
3/30/26, 9:53 PM | ilikepizza314: I do the contract rank business day schedule thing (the index methodology), but only because that's what the ETFs follow, I haven't done any comparisons to the 2 contract CMs.
---
3/30/26, 10:22 PM | TimExcellent: Yeah I guess I could try strict ETF reconstruction but I do wonder about the costs - which in the age of LLM's I should probably did this and just see what the costs are rather than postulate about it
---
3/31/26, 5:34 PM | TimExcellent: Anyone played round with TimesFM from Google? Thought I'd have a carck at thinking about 0DTE options trading (all data IBKR) so the idea would be setting up a strangle or whatever spread really and then have a model guess at paths (alledgedly it is good at doing that). Found a bug in IBKR's native protobuf messaging that I had fix (with LLM's) to get the options chains to come through - I dont know what broke but something to do with corrupted protobuf messaging... and ib_async also threw an error but hung silently so had to abandon and just fix the source.
---
3/31/26, 5:40 PM | TimExcellent: I got annoyed with this post but thought the idea was cool to use TimesFM https://x.com/daniellefong/status/2038809592772346157?s=46&t=N-bRxq_vUy3zqgpzvnA6zA
---
3/31/26, 5:40 PM | TimExcellent: And Danielle appears to do cool stuff
