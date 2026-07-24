# RW Pro Discord — #data-analysis digest, May 2026

- **Period:** May 1–31, 2026
- **Channel:** https://discord.com/channels/1368787013763072040/1368844739465707572
- **Raw transcript:** [rw-pro-data-analysis-raw-20260501-20260531.md](./rw-pro-data-analysis-raw-20260501-20260531.md)
- **Volume:** 31 messages, all landing between May 1–19 (no activity in the second half of the month within this channel). Two clusters: quick R/tooling Q&A early in the month, then a substantial multi-day discussion on tracking trades/positions/costs across accounts (May 12–19). Euan did not post in this channel this month; robotkris was active across three separate threads.

---

## 1. Rolling-window and percentile-ranking functions in R

Rachit asked for a working rolling-percentile-rank function in R after `roll_percent_rank` failed to run (likely a missing package). Marco suggested `runPercentRank` from the **TTR** package; liz suggested the **roll** package and offered to follow up with a code snippet. robotkris then gave the more general-purpose answer: rather than hunting for a rolling-percentile-specific function, reach for the **slider** package, which lets you write arbitrary generic rolling-window functions when nothing off-the-shelf fits your exact need — a "teach to fish" answer rather than a narrow fix. Rachit confirmed he'd ended up converging on slider independently. robotkris separately weighed in earlier in the thread with a broader framing preference: he finds the **dplyr** framework for data analysis noticeably more intuitive than pandas, "at least for how my brain's wired."

**Sentiment:** Quick, practical, well-resolved — a good example of the channel's default mode (targeted package recommendations).

**Pull quotes:**
- robotkris: *"The slider package will let you write generic rolling window functions if you can't find something that works out of the box."*
- robotkris: *"the dplyr framework for data analysis is so much more intuitive than say pandas... at least for how my brain's wired anyway."*

## 2. "Patterns" as a mental model for data analysis problems

MidKnight raised a broader meta-question, referencing content robotkris had fleshed out on the TLQ side (in `#4-working-with-financial-data`) addressing "the meta of data analysis — knowing where to start and what tools to reach for." MidKnight connected this to the software-engineering concept of design patterns (a term with roots going back over two decades) and asked whether it's realistic to build out a catalogue of recurring data-analysis "patterns," offering to help develop it further. robotkris gave a considered, detailed response defending the analogy rather than dismissing it as a stretch: software design patterns are realistic precisely *because* specific frameworks tend to recur as the basis for solving a given class of problem — each individual problem is still solved on its own merits (which is where the creativity comes in), but the pattern gives you a solid, proven starting point rather than a blank page. He explicitly endorsed this as directly applicable to data analysis, calling it "a really useful framing." This reads as a genuine, thought-through position from robotkris rather than a quick aside — he's effectively proposing a pattern-catalogue approach as a teaching/organizing tool for the group's data-analysis content going forward.

**Sentiment:** Substantive and constructive — robotkris treated MidKnight's idea seriously and validated it with a clear justification, which is a meaningful signal that a "data analysis patterns" catalogue could become part of the group's educational material.

**Pull quotes:**
- robotkris: *"I think it is realistic, in the same way that your software design patterns example is realistic. Those software patterns exist because specific frameworks tend to form the basis of the solution to a set of problems... the pattern gives you a solid place to start from. The same applies to data analysis. I think it's a really useful framing."*
- MidKnight: *"I'm not sure its realistic to create a catalogue of these patterns. I'd put my hand up to help with the task if you wanted to develop this further."*

## 3. Tracking trades, positions, and costs across multiple brokers/accounts

The month's longest thread. chi asked whether any reference data model, spreadsheet template, or book exists for tracking trades, costs, strategies, positions, and portfolio performance across multiple accounts — noting he's been doing this manually (splitting ticker positions by strategy, updating positions daily, attributing margin costs, splitting fees for combined trades) and suspected this was "mostly solved by others." MidKnight agreed this is a real, recurring pain point, particularly with Interactive Brokers, whose documentation he called a "nightmare" for building something robust for a stat-arb project. GeirN then wrote up a genuinely detailed proposed architecture (explicitly caveated as speculative, having only just started trading TLAQ): keep all account moves in a single spreadsheet, treat it as double-entry-style accounting by splitting each transaction's legs into separate rows grouped by a manually-incremented "Document number," track balance by sub-totaling on brokerage account, track free-vs-allocated capital by sub-totaling on a "Strategy" column, use a "Reconciled" column checked off against broker statements, and use a "Lot" column for strategies needing specific-lot tracking. He suggested this scales from a manual spreadsheet toward automated ingestion (e.g., auto-loading broker statements) as trading volume grows. Separately, opm revealed he's actually building a product to fill this exact gap — currently using **Zorro** as his own trading platform (which he says handles this well), with the in-development product offering a **Python SDK** and **FastAPI**-based infrastructure for logging/monitoring; a Julia-based member (TimExcellent) noted a connector would likely be cheap to build given today's tooling. opm's parting practical advice, unprompted but clearly grounded in years of experience: keep the system as simple as possible while automating as much as you can, since the right complexity level depends heavily on how many systems/brokers/timeframes/budget you're running — worth mapping out carefully up front to avoid a major headache later. The thread closed with andyw sharing an IB-specific tactical tip: toggling "Include Audit Trail Fields" to Yes in IB Flex Query options lets the order reference persist so you don't have to match trades separately across reports — though this only works for **live** trading, not paper, and the audit trail data only persists for a day, so it needs an automated daily-pull process.

**Sentiment:** Genuinely valuable, practitioner-grounded thread — no single "solved" answer emerged, but multiple credible partial solutions (GeirN's spreadsheet architecture, opm's in-progress product, andyw's IB-specific fix) plus validation that this is a widely-felt, unsolved gap in the retail quant tooling landscape.

**Pull quotes:**
- chi: *"Are there any reference data models or spreadsheets for tracking trades, costs, strategies, positions, and portfolio performance across several accounts?... I figure this is mostly solved by others."*
- GeirN: *"the easiest is probably to accept that this is a form of accounting, and therefore use the accounting concept of splitting the different legs of a transaction into separate lines in the spreadsheet."*
- opm: *"Just keep it as simple as possible, but automate as much as you can! It totally depends on how many systems you run, how many brokers, time frame, budget, accountant etc. Its definitely worth mapping it out and planning to save you a massive headache."*
- andyw: *"if you toggle the switch in flex query options named 'Include Audit Trail Fields' to Yes you can get the order ref to persist so you don't have to match separately... this only works with live but not paper."*

## 4. Miscellaneous data source note

TimExcellent flagged a free Kaggle dataset containing historical S&P 500 index holdings and weightings through 2025 (derived from SPY ETF annual reports, covering 2000–2024) — a useful lightweight source for anyone needing historical index composition without a paid data vendor.

**Pull quote:**
- TimExcellent: *"Kaggle has a dataset for the weightings for up to 2025 for the SP500."*

---

## Overall read

May's #data-analysis was lower-volume than June but arguably more substantive per message — dominated by the multi-account trade/position-tracking thread, which surfaced a genuine, widely-shared operational gap (no clean off-the-shelf solution exists) and three concrete partial approaches worth revisiting: GeirN's spreadsheet-as-accounting-ledger design, opm's in-development Zorro-adjacent product, and andyw's IB Flex Query audit-trail tip. robotkris's contributions this month leaned toward framing and philosophy rather than one-off technical fixes — his "data analysis patterns" endorsement (drawing a direct, well-reasoned parallel to software design patterns) is worth watching for whether it becomes a formal piece of RW Pro educational content later in the year. Euan was absent from this channel in May, unlike June where he was a central voice in the spread-estimation and vol-drag threads.
