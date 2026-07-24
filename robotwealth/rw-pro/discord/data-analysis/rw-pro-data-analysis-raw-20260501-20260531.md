# RW Pro Discord — #data-analysis raw transcript

- **Period:** May 1–31, 2026
- **Channel:** https://discord.com/channels/1368787013763072040/1368844739465707572
- **Message count:** 31
- **Extraction method:** Browser automation (Claude in Chrome) against the live Discord DOM, using Discord's `in:data-analysis after:2026-04-30 before:2026-06-01` search to bound the range, then scroll-and-merge extraction of the message list, trimmed to exact May 1–31 boundaries. No activity after May 19 within the range (next message is June 10, outside range). Some individual messages are capped at 250 characters by the extraction tooling; these are marked `[capped]` below where the cutoff is mid-sentence.

---

5/1/26, 1:56 PM | robotkris [reply]: Totally. The dplyr framework for data analysis is so much more intuitive than say pandas... at least for how my brain's wired anyway.
---
5/2/26, 1:35 AM | Rachit: does anyone happen to know off the top of their head how to do a rolling percentile ranking of a column?

i thought it was roll_percent_rank but that is not working (maybe i don't have the right lib installed).

much appreciated!
---
5/2/26, 5:15 PM | Marco [reply]: Mmm maybe runPercentRank of the TTR package?
---
5/2/26, 5:25 PM | liz [reply]: check out the "roll" package

edit: if you already were diving in there tag me and i'll help you out with a code snippet when i'm awake again tomorrow haha
---
5/3/26, 12:06 PM | TimExcellent: didnt know this but Kaggle has a dataset for the weightings for up to 2025 for the SP500 https://www.kaggle.com/datasets/devaangbarthwal/s-and-p-500-holdings-and-weights-spy-2000-2024
---
5/6/26, 9:47 PM | robotkris [reply]: The slider package will let you write generic rolling window functions if you can't find something that works out of the box
---
5/6/26, 9:47 PM | Rachit [reply]: yeah thats the one i ended up using thx
---
5/11/26, 12:15 PM | robotkris: @MidKnight fleshed out an answer to this data analysis question on the TLQ channels as I get clearer on talking about the meta of data analysis - knowing where to start and what tools to reach for. #4-working-with-financial-data
---
5/11/26, 12:34 PM | MidKnight: I'll have a read @robotkris thank you.
I haven't read it yet, but I was thinking about this over the weekend. A few times you have mentioned this is a common pattern to solving this sort of problem. Pattern.

A little over 2 decades ago this term "pa [capped]
---
5/11/26, 12:54 PM | MidKnight: That was good @robotkris, thanks for that. It's a good example of a problem (how can examine seasonality) and solutions with multiple variations. I'm not sure its realistic to create a catalogue of these patterns. I'd put my hand up to help with the [capped]
---
5/11/26, 1:53 PM | robotkris [reply]: I think it is realistic, in the same way that your software design patterns example is realistic. Those software patterns exist because specific frameworks tend to form the basis of the solution to a set of problems. And while each problem is treated on its merits (which I think is where the creativity comes into it), the pattern gives you a solid place to start from. The same applies to data analysis. I think it's a really useful framing.
---
5/12/26, 9:39 PM | chi: Are there any reference data models or spreadsheets for tracking trades, costs, strategies, positions, and portfolio performance across several accounts? Or is there a book anyone recommends that goes into these? I've been doing things manually for n [capped]
---
5/12/26, 9:40 PM | chi: But I figure this is mostly solved by others and that I've probably missed something that I'll regret having missed later on
---
5/13/26, 7:47 AM | MidKnight: I agree @chi, there must be others doing it and especially with the common IB brokerage. I've been trying to have something robust and reliable using IB for the stat arb project but its been a real nightmare I think. Poor documentation at IB's end.
---
5/13/26, 5:53 PM | GeirN: Hi @chi. I just started TLAQ a little over a week ago, so I haven't given this side of the business much thought yet, but your question changed that. I am going to lean very far out of the window here and share my thoughts. I have no idea ho [capped]
---
5/13/26, 5:54 PM | GeirN: Having all the raw data in a single spreadsheet should make it easier to analyze the data. So for reporting I would create an R workbook, which would start off with reading the spreadsheet, and the document would contain a markdown outline structure [capped]
---
5/13/26, 5:54 PM | GeirN: When the trading operation gets bigger it would be possible to start generating the rows in the spreadsheet automatically, like loading broker statements and append automatically to the spreadsheet. Sidenote: I would not load orders in here, only act [capped]
---
5/13/26, 5:55 PM | GeirN: Everyone is different and the number of transactions and requirement for control will differ. Having a couple of buys/sells in the local currency per month is going to be different from trading across multiple asset classes with multiple strategies a [capped]
---
5/13/26, 9:47 PM | opm [reply]: I haven't found anything over the years, so a few months ago I actually started building a product to fill this gap

I currently use Zorro as my trading platform which does roll everything up. It's pretty robust, but the product I'm building will wo [capped]
---
5/14/26, 7:58 PM | opm [reply]: I'm surprised nothing exists.

Are you trading with python? It's a python sdk. I'm also building out infra logging/monitoring
---
5/14/26, 8:49 PM | TimExcellent [reply]: Not Python, Julia, but in today's world a connector probably cheap?
---
5/14/26, 8:52 PM | opm [reply]: Yeah, FastAPI so connection should be straight forward
---
5/14/26, 9:20 PM | chi: Yeah, every time I try to search for a solution in this space, I end up with a ton of irrelevant results about discretionary trading journals
---
5/14/26, 9:20 PM | chi: I'll have to check out what Zorro and other platforms like it are doing
---
5/14/26, 9:20 PM | chi: Do you have any other tips or advice from over your years in the meantime?
---
5/16/26, 1:18 PM | opm [reply]: Just keep it as simple as possible, but automate as much as you can! It totally depends on how many systems you run, how many brokers, time frame, budget, accountant etc. Its definitely worth mapping it out and planning to save you a massive headache
---
5/19/26, 5:13 PM | andyw [reply]: You may already be doing this, but if you toggle the switch in flex query options named "Include Audit Trail Fields" to Yes you can get the order ref to persist so you don't have to match separately
---
5/19/26, 5:14 PM | andyw: Also make sure your Trades or Trade Confirmations columns settings have order ref included
---
5/19/26, 5:16 PM | andyw: I'm part way through writing this now so will upload when done (away at present so prob over weekend). FYI this only lasts for a day, so you need an auto process that runs post trading every day
---
5/19/26, (edited) | andyw: And of course being IB this only works with live but not paper
