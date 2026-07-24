# RW Pro Discord — #data-analysis raw transcript

- **Period:** February 1–28, 2026
- **Channel:** https://discord.com/channels/1368787013763072040/1368844739465707572
- **Message count:** 49
- **Extraction method:** Browser automation (Claude in Chrome) against the live Discord DOM, using Discord's `in:data-analysis after:2026-01-31 before:2026-03-01` search to bound the range, then scroll-and-merge extraction of the message list, trimmed to exact February boundaries. Channel activity was clustered into five windows this month (Feb 2–3, Feb 6–12, Feb 24, Feb 27) with multi-day silent gaps between them. One message (alvin, 2/12/26) is an edited message whose DOM timestamp element didn't match the standard short-form pattern; its date is confirmed from surrounding messages and marked `[time unavailable, edited]` below per the known extraction edge case.

---

2/2/26, 11:49 PM | steph: Hi all - I'm testing simple risk premia strategies over long horizons and was wondering if anyone can point to a clean, research-ready dataset covering the main asset classes (country equity indices TR, gov/corp bonds, commodities, FX, etc.).

If not a single dataset, any advice on the best sources and how to stitch them together would be very welcome. I'm mainly trying to avoid reinventing the wheel and would love to tap into the collective experience here. Thanks in advance for the help.
---
2/3/26, 11:14 AM | robotkris [reply]: For risk premia stuff, I would go for Ashwath Damodaran's data: https://pages.stern.nyu.edu/~adamodar/
---
2/3/26, 11:14 AM | robotkris: Click the link for Data from that site - lots of good stuff there.
---
2/3/26, 4:47 PM | steph: Thanks @robotkris Damodaran's data is great, but it's annual and fairly limited, so not ideal for testing risk premia strategies (risk-parity but also momentum, value, carry, etc.). I'm looking for monthly total return data with decent breadth across equities, bonds, commodities, and FX. Does this community have anything along those lines? Or is anyone working (or has worked) on a shared cross-asset dataset? If not, I'll keep you posted if I find anything - this feels like the kind of thing that would be really valuable to share here.
---
2/3/26, 4:56 PM | robotkris [reply]: This dataset from The Lab has a bunch of asset class data from ETFs that we extended back to 1995 using mutual fund data:

Gold
,
Non-US DM stocks
,
EM stocks
,
EM bonds
,
Treasuries
,

(also contains some other ETFs that we wanted to look at but didn't extend - managed futures, leverage etfs)

We don't have a long-term commodities data set, but we do have lots of futures data. You could build your own from that.

Likewise FX - you could build a dollar index from our FX data, but it isn't well documented. However, you can see how to get it in The Lab using these utilities from rwRtools. There's even a function for making a total return index that will come in handy.
---
2/3/26, 4:58 PM | steph: That's great thanks @robotkris
---
2/3/26, 4:59 PM | robotkris [reply]: No problem. Not sure why i didn't link you to that stuff in the first place. I guess I was low on caffeine at the point in the day
---
2/6/26, 4:28 AM | bdkoepke: A few years ago I came across a website with historical IBKR short-sale data (fees, availability, etc). I can get the current values from the ftp, but it would be nice to have some of that history. Does anyone know where I could find that?
---
2/6/26, 4:42 AM | bdkoepke: iborrowdesk.com, not sure if there's anything better
---
2/6/26, 5:56 AM | MattM [reply]: Kris has data from mid 2020 onwards in the lab https://github.com/RWLab/macro-pod#us-stock-short-sale-data-from-interactive-brokers
---
2/6/26, 6:06 AM | bdkoepke: Oh wow, that's even better, thanks!
---
2/7/26, 6:47 AM | bdkoepke: How is the symbology for norgate? I'm currently working with CSI, and the main issue is they don't have any of the standard identifiers, so I'm having to hack something together with Bloomberg FIGI... That works well for active large/mid cap, but it's terribly inaccurate for inactive and foreign securities.
---
2/7/26, 9:58 PM | Alex: What exactly are you looking for? I do use norgate for a few years now. US equities are just the default ticker and delisted ones are the ticker + the last traded date or something like that.
---
2/8/26, 4:13 AM | bdkoepke: Ideally a mechanism to tie it back to a clean symbol, since tickers change over time. I suppose the date does help, I'm not sure if I can use that to restrict the figi search. I try to map everything to ID_BB_GLOBAL, because then it's like IBKR conid <-> FIGI, CSInum <-> FIGI, Zacks <-> FIGI, etc.
---
2/9/26, 10:51 AM | Quarry614 [VBT], Server Tag: VBTVBT: A bit convoluted, but take the symbol list at the beginning of test and at end of test period; find differences; and ask AI what changed (merger, new symbol, BK, etc.) and when? Could then exclude or substitute new symbol.
---
2/9/26, 7:42 PM | Alex [reply]: Ah sorry, that is beyond my knowledge. I have no clue about symbology besides tickers/ISIN.
---
2/9/26, 8:13 PM | Jakub [reply]: Is there a source other than Bloomberg where I can look up FIGI identifiers?
---
2/10/26, 4:17 AM | bdkoepke: Openfigi is the only place I'm aware of. I worked with IBKR to get them to add them to the reports and TWS about eight years ago.
---
2/10/26, 10:34 PM | Jakub [reply]: Thank you for doing that!
---
2/11/26, 4:10 AM | TheOriginal101: Where do you guys get historical index constituency data? (SP500, NQ100, or even more esoteric stuff like DAX, etc)
---
2/11/26, 5:48 AM | mm [reply]: norgate is good for this
---
2/11/26, 5:51 AM | TheOriginal101 [reply]: I know, but that is the only data I need from them (eg they don't have intraday, they don't have european stocks, etc), so not really an option for me. Is there anything else? Eg scraping from edgar filings of QQQ or similar?
---
2/11/26, 5:54 AM | mm: you could probably scrape them in theory but there's likely to be inconsistencies or large delays from when weights/constituents changed to when they're publicly available
---
2/11/26, 5:55 AM | mm: if you just need it historically and don't need it to be "real time" then yea but it's just a lot of extra effort
---
2/11/26, 5:57 AM | mm: there's also the chance of whatever you're scraping from having some form of lookahead where it'll say xyz asset was added/removed to an index on abc date but that info wasn't publicly available until a month or two or three later
---
2/11/26, 6:49 AM | veng1: If you have an IBRK account, you can probably get it via the TWS API.
---
2/11/26, 8:27 AM | bdkoepke: https://github.com/Jon-Becker/prediction-market-analysis
---
2/11/26, 2:25 PM | bdkoepke [reply]: https://eodhd.com/marketplace/unicornbay/spglobal/docs
---
2/11/26, 2:25 PM | bdkoepke: CSI also has current
---
2/11/26, 2:25 PM | bdkoepke: https://ua2.csidata.com/ua/StockIndexComponents/RUSSELL1000.csv
---
2/11/26, 2:25 PM | bdkoepke: /ua/StockIndexComponents/FTSE100.csv
/ua/StockIndexComponents/DJIA.csv
/ua/StockIndexComponents/DJC.csv
/ua/StockIndexComponents/DJT.csv
/ua/StockIndexComponents/DJU.csv
/ua/StockIndexComponents/NDX.csv
/ua/StockIndexComponents/BANK.csv
/ua/StockIndexComponents/NBI.csv
/ua/StockIndexComponents/COMP.csv
/ua/StockIndexComponents/IXCO.csv
/ua/StockIndexComponents/IXF.csv
/ua/StockIndexComponents/IXHC.csv
/ua/StockIndexComponents/INDS.csv
/ua/StockIndexComponents/INSR.csv
/ua/StockIndexComponents/QNET.csv
/ua/StockIndexComponents/OFIN.csv
/ua/StockIndexComponents/IXTC.csv
/ua/StockIndexComponents/TRAN.csv
/ua/StockIndexComponents/RUSSELL1000.csv
/ua/StockIndexComponents/RUSSELL2000.csv
/ua/StockIndexComponents/RUSSELL3000.csv
/ua/StockIndexComponents/SP100.csv
/ua/StockIndexComponents/SP400.csv
/ua/StockIndexComponents/SP500.csv
/ua/StockIndexComponents/SP600.csv
---
2/11/26, 2:26 PM | bdkoepke: Or if you can find an ETF that tracks the index, historical ETF holdings are much easier to find.
---
2/11/26, 4:17 PM | alvin [reply]: Norgate does decent
---
2/12/26, 8:19 AM | bdkoepke [reply]: How did you extract the constituents? Do you loop over each potential security in the index for each date, and check for "in index/not in index", or is there a simpler way? Their docs said they don't provide the names directly, only a "is this security in the index" test.
---
2/12/26, 1:54 PM | alvin [reply]: I think theres a way through Python, but I actually use RealTest for it.


Settings:
    DataFile:    spx.rtd
    StartDate:    Earliest
    EndDate:    Latest
    ScanNoDefCols:    True
    SaveScanAs: C:\file.csv

Scan:
    Filter:    InSPX
    Da:    BarDate {//}
    Stock:    ?Symbol


And it gives a beautiful csv, every trading day and their respective stocks in the constituent for that day
---
2/12/26, [time unavailable, edited] | alvin: Edit:'pic is sp100 not 500
---
2/24/26, 10:14 AM | Dan: Someone did their own version of the BOIL trade, but says it can mostly all be done in December.
Also they've got a separate seasonal trade for every month.
I didn't fully understand their SPX or VIX rule, because it's a whole month trade but are they jumping in and out of commodity trades daily based on the VIX?
And then is it open to open, open to close, or close to close?
Most of the cases my testing showed the rules worked better without the VIX daily trading, just holding for the whole month (but I was including costs in my tests).
https://open.substack.com/pub/layquant/p/the-commodity-calendar-trade?utm_campaign=post-expanded-share&utm_medium=web
---
2/24/26, 10:17 AM | Dan: I have low confidence in those monthly seasonals, my default thought is the backtesting is using future knowledge if we are deciding what is a seasonal period here and now in 2026..
Seasonal indexes that get built on the fly based on data up to each date are more robust, but more complex.
Anyway, I'm curious on what others think about all 3 parts of this article:
1) The adjustment to the BOIL strategy
2) The calendar trades for every month
3) Using VIX or SPX as a timing tool for commodity ETFs
---
2/24/26, 10:20 AM | alvin: This looks like just curve fitting
"Lets take a look at the best month and lets simulate a trade on that best month"
I mean, no doubt its gonna be a good sharpe... ?
---
2/24/26, 10:22 AM | Dan [reply]: Yep, my concerns.. and trying to get the timing right on so many moving parts multiplies the opportunities to fit it.
Though the sharpe wasn't actually that impressive, I only got up to July before I quit.
I could feel myself fitting it as I went
---
2/24/26, 11:53 AM | mm: if you wanna modify the boil strategy you might consider looking at UNL/BOIL.

UNL is effectively a 12 month blend of nat gas futures:
"UNL's Benchmark Futures Contracts are the futures contracts on natural gas as traded on the NYMEX that are the near month futures contract to expire and the contracts for the following 11 months, for a total of 12 consecutive months."

BOIL is a bit different:
"The lead contract is defined as March for January and February, May for March and April, July for May and June, September for July and August, November for September and October, January for November and December."

it's a different trade from the original boil one but it turns into something similar to uvxy/vxz or uvxy/vixm where you're shorting levered near term exposure and hedging it with something further back.
---
2/24/26, 12:22 PM | MidKnight: @mm Thanks for sharing that idea. I've been hunting for more of these sorts of trades but missed this one entirely. I tried to look for more of these sorts of futures backed ETFs a while ago but I couldn't find a list other than manually going through ETFs one at a time on etfdb....
---
2/24/26, 12:25 PM | mm [reply]: the only other one ive found that made sense to me was with crude oil but they changed the product after covid and it pretty much died
---
2/24/26, 12:25 PM | mm: you could probably just run that unl/boil one during the same months as the current boil strat does
---
2/24/26, 12:26 PM | mm: havent taken a look at it but id imagine the winter months would still be best
---
2/24/26, 12:27 PM | MidKnight: i like the idea a lot, thank you.
---
2/24/26, 10:27 PM | veng1: https://proactiveadvisormagazine.com/trading-the-seasonal-heating-oil-gasoline-spread/
---
2/27/26, 10:25 PM | TimExcellent: Been experimenting (guessing earinings beats was all I used to do) with earning catalyst trading and how I'd approach it now with having backfilled required base knowledge with what we do here... the calculation of EPS and EPS forecasting and testing that against Street numbers.

Basically just using FMP's excel API and Claude and different ways of weighting the EPS forecast and adjustments. theres likely more to think about but taking as reported annual numbers and then backing out my own numbers, its easy to see where things fall down. If I still forked out $ for XENITH (Eikon for Retail) I'd be interested to know roughly how close or far away "gold standard" estimates really are. Likely they go into all sorts of modelling of course and isnt so dirty like this, but close enough is likely good enough.
---
2/27/26, 10:26 PM | TimExcellent: I just threw Jensens Correction in there for solidarity as it was the first thing that came to mind
