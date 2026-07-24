# RW Pro Discord — #data-analysis digest, March 2026

- **Period:** March 1–31, 2026
- **Channel:** https://discord.com/channels/1368787013763072040/1368844739465707572
- **Raw transcript:** [rw-pro-data-analysis-raw-20260301-20260331.md](./rw-pro-data-analysis-raw-20260301-20260331.md)
- **Volume:** 28 main-channel messages clustered into three distinct windows (March 10–12, March 20, March 28–31) with multi-day silent gaps between them — low but focused traffic, split between equity-fundamentals data work and VIX-complex futures methodology.

---

## 1. PEAD v2 momentum model, and how trustworthy is FMP's fundamentals data?

Ben shared progress on revamping his PEAD (post-earnings-announcement-drift) model after finding the "twin momentum" paper in the equity factors pod — he ran a quick analysis combining the paper's fundamental momentum features with technical momentum features from his own PEAD system, weighting each feature by IC and stability ("nothing scientific, higher IC and stability gets more weight"), on Russell 1000 stocks from 2010–2025. He reported the resulting PEAD system is "travelling ok" in live testing.

**robotkris pressed on data integrity rather than just praising the results** — this is the substantive part of the thread:
- His first reaction to Ben's backtest results was skepticism dressed as a compliment: *"Those results look very good...better than I would have expected. Any chance they might be serving you revised fundamentals, rather than what was reported at the time?"* — i.e., a direct challenge on point-in-time (PIT) correctness, the single most common way a fundamentals backtest silently looks better than it should.
- Ben's response showed he'd already guarded against this specific failure mode: he uses FMP's `acceptedDate` field (the SEC filing acceptance timestamp, not `date` or `filingDate`) for PIT alignment, and shared a sample JSON record showing the field structure. He committed to re-downloading and diffing FMP's full historical data against his weekly-updated local copy to double check for retroactive revisions.

**Data-quality side discussion** (data source reliability, not the PIT question specifically):
- mm asked whether FMP's data is reliable, noting FMP support never responded to a simple question after promising a few business days' turnaround.
- Ben: hasn't personally hit problems, but has heard secondhand reports of data quality issues and retrospective figure updates over his ~1 year of use — his bar is pragmatic ("if a few bits of dodgy data here and there is going to break my system I have bigger problems").
- mm: has only used FMP's free tier so far, mainly for historical earnings estimates, hasn't paid.
- bdkoepke raised a substitute worth noting: direct XBRL feeds carry both as-reported and revised fundamentals (unlike most vendor APIs), at the cost of not being normalized — a real data-cleaning burden. Zacks was mentioned as a normalized alternative but with lower resolution.
- blue664203 asked whether Ben's Russell 1000 universe was a static end-of-2025 snapshot; Ben clarified it includes current and past constituents, though historical coverage thins the further back you go — roughly 2000 symbols total from memory.

**Sentiment:** Constructively skeptical — robotkris's PIT challenge is the kind of question that catches a whole class of backtest overstatement, and Ben had a specific, defensible answer ready rather than a vague one.

**Pull quotes:**
- robotkris: *"Those results look very good...better than I would have expected. Any chance they might be serving you revised fundamentals, rather than what was reported at the time?"*
- Ben: *"I have been using accepted date for PIT alignment... 'acceptedDate': '2024-11-01 06:01:36'"*
- bdkoepke: *"My understanding is that the [XBRL] data isn't normalized (which is a PITA), but it should have as reported and revised."*

## 2. Databento expanding to HK stocks and futures

TimExcellent shared a databento announcement (via X/Twitter) that HK stocks and futures data are coming to the platform. Standalone post, no in-channel discussion followed.

**Sentiment:** Informational share, neutral — a data-vendor coverage expansion worth knowing about for anyone researching HK-listed names.

**Pull quote:**
- TimExcellent: *"HK stocks and Futs coming to databento"*

## 3. Daily-bar timing mismatch between VIX3M and synthetic VX30 futures positions

Rachit flagged a subtle data-alignment problem: when comparing VIX3M against a synthetic VX30 futures position using 1-day interval data, VIX3M closes at 4pm while VX futures keep trading afterward — so a naive daily close-to-close comparison mixes prices from different points in time.

- MidKnight's first take: regular trading hours (RTH) close should still be usable as the futures daily bar close.
- **robotkris gave the more careful answer**, breaking the question down by what "close" actually means in the data: it depends on whether the futures close price is settlement-based (closer to VIX timing) or an RTH close. Either way there's some information leakage, but he judged it acceptable for slower-moving research. His concrete suggestion: check what the close field actually represents, and test the impact by lagging the futures data by a full day.
- Rachit was mid-build on an aggregated dashboard of all the VIX-complex signals discussed in the channel (working through a synthetic VX30–VIX3M premium z-score) and hit a data-source discrepancy on the way: raw daily data and rescaled hourly data (both sourced from IBKR) produced "wildly different numbers" — flagged for further investigation with "a fresher brain," not yet resolved in this window.
- robotkris welcomed the dashboard effort as something he'd personally wanted done for a long time.

**Sentiment:** A real, easy-to-miss data pitfall (cross-asset daily-bar timing misalignment) surfaced and given a practical test (day-lag sensitivity check) rather than just flagged and dropped — plus an open discrepancy (raw vs. rescaled IBKR data) still unresolved at month's end.

**Pull quotes:**
- Rachit: *"Won't the analysis be borked bcs vix3m closes at 4pm but the futures keep trading so the close prices of the 1d bar would be for different times??"*
- robotkris: *"Depends what the close price in your futures data is... if it's settlement, it should be closer to VIX timing I think. I think it'll leak a little information either way, but should be OK for research on slower moving stuff. Still, worth being aware of. Do you know what the close price represents? You could lag your futures data by a full day and see what impact that has."*
- Rachit: *"Got wildly different numbers between using raw daily and rescaled hourly data (both from ibkr)."*
- robotkris: *"This has been on my list of things I want to do for ages... great that someone is doing it."*

## 4. Constant-maturity VX futures construction, and reconstructing UVXY/VXZ mechanics

TimExcellent worked on recreating UVXY and VXZ-style products from VX futures directly, flagging 2018 as roughly where his eyeballed return path starts looking right versus the real product, while noting he expects some methodology errors and that exporting a working notebook would be complicated (his data caching layer is tightly coupled to the analysis).

ilikepizza314 asked how the constant-maturity (CM) series are actually constructed — a pair of weighted contracts targeting a calendar-day maturity target?

TimExcellent's detailed answer laid out the mechanics precisely:
- For each date, find the two VX futures that bracket the target days-to-expiry (DTE) — one at or before, one after — and weight linearly by distance to target:
  `near_wt = (far_DTE - target) / (far_DTE - near_DTE)`, `CM_price = near_wt * near + (1 - near_wt) * far`.
- Weights shift daily as DTE counts down; there are no discrete roll dates, just continuous interpolation to 30 or 150 calendar days (i.e., CM_30 and CM_150).
- This differs from how the actual ETFs work: **UVXY** holds 1st + 2nd month futures by contract rank, rolling daily on a business-day schedule between settlement Tuesdays; **VXZ** holds 4th through 7th month contracts (5th and 6th at static full weight, only the 4th and 7th roll) — four contracts, not two.
- His own CM_30/CM_150 series loosely target the same tenors as the real products but use DTE-bracketing with always exactly two contracts for the mid-term leg, rather than monthly-rank with four.

ilikepizza314 uses the discrete contract-rank/business-day schedule instead (matching what the ETFs actually follow, i.e., the index methodology) and hadn't compared it against the two-contract CM approach. TimExcellent floated trying a strict ETF reconstruction but questioned whether it's worth the effort versus just measuring transaction costs directly given how cheap LLM-assisted analysis has become.

**Sentiment:** Technically precise infrastructure-building thread — a clear, reusable reference for anyone constructing their own constant-maturity VIX futures series, with an honest methodology gap (CM approach vs. actual ETF mechanics) identified but not yet resolved.

**Pull quotes:**
- TimExcellent: *"For each date, find the two VX futures that bracket the target DTE (one ≤, one >), weight linearly by distance... Weights shift daily as DTE counts down. No discrete roll dates — just continuous interpolation to 30 or 150 calendar days."*
- TimExcellent: *"UVXY holds 1st + 2nd month by contract rank, rolling daily on a business-day schedule between settlement Tuesdays. VXZ holds 4th through 7th month... four contracts, not two."*
- ilikepizza314: *"I do the contract rank business day schedule thing (the index methodology), but only because that's what the ETFs follow, I haven't done any comparisons to the 2 contract CMs."*

## 5. TimesFM for 0DTE options path modeling

TimExcellent explored using Google's TimesFM (a foundation model for time series forecasting) to model price paths for 0DTE options strategies (strangles or similar spreads), sourcing all data from IBKR. He hit and fixed (with LLM assistance) a bug in IBKR's native protobuf messaging that was breaking options-chain retrieval, and separately noted `ib_async` silently hung on a related error rather than surfacing it, requiring a source-level fix. He also shared an external post (Danielle Fong on X) that motivated trying the idea despite finding the post itself irritating.

**Sentiment:** Exploratory and unresolved — a new-tooling experiment (TimesFM for options path forecasting) blocked partway by IBKR API bugs rather than a modeling result; no other members weighed in this month.

**Pull quote:**
- TimExcellent: *"Thought I'd have a carck at thinking about 0DTE options trading... so the idea would be setting up a strangle or whatever spread really and then have a model guess at paths (alledgedly it is good at doing that)."*

---

## Overall read

March's #data-analysis split cleanly into two technical domains: equity fundamentals data integrity (PEAD/momentum modeling, with robotkris's PIT-correctness challenge as the sharpest moment of the month) and VIX-complex futures mechanics (daily-bar timing alignment, then constant-maturity futures construction, both largely driven by TimExcellent and Rachit). The recurring thread across both domains is the same discipline: don't trust a good-looking backtest number until you've checked how the data was actually timestamped and constructed — robotkris's point-in-time question to Ben and his settlement-vs-RTH-close breakdown for Rachit are both instances of the same underlying habit. The VX30/VIX3M ecosystem is clearly an active, multi-person area of research this quarter (Rachit's aggregated signal dashboard, TimExcellent's CM series and UVXY/VXZ reconstruction), with a couple of concrete open loose ends worth checking back on: Rachit's raw-vs-hourly IBKR data discrepancy, and the gap between TimExcellent's two-contract DTE-bracketed CM series and the ETFs' actual four/two-contract rank-based construction.
