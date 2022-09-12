### Strategy: return-stacked 60/40 absolute return index

Goals
- Aims to provide exposure to a U.S. 60% equity, 40% bond allocation while stacking diversifying alternative exposures, including tail protection, on top
- Stacking is achieved by allocating to a custom basket of widely available Mutual Funds and ETFs, which embed a variety of capital efficient exposures to equities, bonds and alternative strategies
- Assets are allocated to 10 mutual funds/ETFs with weights between 3% - 15%, with weights adding up to 100%. Due to the leverage in some of these funds, the notional exposure adds up to 160%.

---

### Twitter research

[2022-08-07 tweet](https://twitter.com/HML_Compounder/status/1554943229870628865?s=20&t=QBwqSrWLWFZkHA0ezMcExw): "Fun/quick piece from @AuspiceCapital on return-stacking, specifically with CTAs - [Auspice Capital blog](https://t.co/dknnZJgIYS), "Return-stacking - What, When, Where, How"
- I remember trying this in the 1990s using fabulous looking CTAs in the same equation. It was bust. Adding a top surviving CTA sure looks in a backtest! They always do - until they don’t.
- There is no magic alpha here. You can just look once a month and go long/short based on 12m return and do great [per AQR's time-series momemtum research]. I struggle to believe you didn't have huge outperformance by adding CTAs in 1990's to equities. Were they pure trend or getting cute?
- "It was a bust. We had an entire analyst team at Smith Barney trying to pick winning CTAs. The gross returns ALWAYS look outstanding, it just doesn’t WORK in real life. The entire CTA industry is very expensive crapshoot. Just a gamble."
- ... "The most impressive investors I admire seem to have one common trait. They stay curious.  If CTAs were underperforming in the underbelly of the trenches, as you're suggesting, why on earth do they still exist? Just a buncha suckers falling for an expensive crapshoot over again?"
- ... "They exist for the same reason front-load actively managed mutual funds still exit - someone has an incentive to sell them."
- ... "Have you looked up the oldest surviving CTA mutual fund? Past performance is a significant determinant for mergers. Thus, HF, FoHF, & CTA mergers could be motivated by a need to eradicate bad performing funds. Results robust to different performance measures after correcting backfill bias & removing artificial serial correlation effects. As much as I agree the right fund can be worth a look, there's plenty that aren't. If you don't pick a systematic and well vetted methodology you can get hurt, and hurt more due to lacking of clear performance drivers. Worse yet, you can think you picked as well as possible and still get hurt. Long run is unforgiving. Stories like Rick's are worth consideration. If your CTAs only perform like cash, are you going to be OK? If so, maybe cash is worth considering instead." Linked [article](https://www.investmentnews.com/how-investors-lose-89-of-gains-from-futures-funds-54293): "How investors lose 89% of gains from futures funds".
- ... "Picking a single CTA is very, very hard.  One of the highest dispersion categories due to all the potential ways in which portfolio construction differences can vary."
- "... Thanks for sharing that. Is that why a fund like $DBMF (that targets the performance of a diversified pool of managed futures managers) may have an advantage over others? Do you have a system in place for analyzing individual CTA managers for risk/reward profile before consideration?"
- "... $DBMF may have an advantage because it (1) eliminates idiosyncratic, single manager risk and (2) potentially significantly reduces associated fees. But it introduces its own model risk.  It's all a trade off."
- ... "There are multi-manager options available to the masses but not as many as I’d like. $MAFIX is an interesting one which also includes a static 50% S&P500 exposure on top (I know you’re aware Corey but for others)." [$MAFIX exposures = 100% to managed futures, 50% to S&P futures, 70% to short-duration US fixed income.] Equity comes from futures though so not that tax-efficient. $BLNDX better in that regard with ETF equity exposure.
- Also quite likely that CTAs may exhibit less up-side participation during extended equity bull markets (such as 1990-2000, 2010-2020).
Behaviorally, it is very difficult to rebalance into a commodity allocation during expansion cycles. [Newfound Research blog](https://blog.thinknewfound.com/2020/02/can-managed-futures-offset-equity-losses/): Can managed futures offset equity losses?
- "I...  admit I don't get it.  I like NTSX and that family because the leverage is used for bond options, seems relatively stable...  I'm having trouble verifying the return data let alone understanding the construct."
- ... "NTSX to my understanding is using the 10% collateral to buy bond futures, not options. This product here would have a combo of ETFs, cash, and futures to give you 100% exposure to their managed futures, with a 60/40 or 70/30 equity/bond portfolio under it. Not too dissimilar from my taxable setup, I just use 100% equities instead of 60/40. In my case I use a margin loan to collateralize the futures, they are likely using part of the "bond" allocation (held in cash)."
- "Also I started my oldest sons UTMA return stacking. NTSX and DBMF."
- "To try and roughly replicate with US-traded ETFs, what’re your thoughts on this? BTOP50 ~= equal-weight [DBMF, KMLM, CTA], 70 / 30 ~= equal-weight [VT, NTSX, NTSI, NTSE] plus maybe GMOM, VAMO, VMOT for umph, TAIL and BTAL for protection, UPAR for classic risk parity."
- ... "Ya seems about right. Does include an equity long/flat trend on 50% of the equity. Maybe do VMOT+NTSX/I/E and then whatever CTA you like. Factor, trend, and cheap beta."
- "One Fund is quite neat. Think it’s more like 100% CTA + 100% 60/40 or 70/30 but still a slick setup. I prefer 100% equity + CTA myself :). And factors…. Cockroach is great that’s awesome you’ve got an allocation. Their 4 CTAs are all quite interesting."
- "we were discussing the funds from Mutiny. They offer a CTA fund with $100K min that exposes to 4 private CTAs, Jerry’s, Auspice Diversified, Quest(I think?), and EMC." ... "Quest was stupid high CAGR one if I remember right. Check out RCM’s [Guide to Trend-Following](https://www.rcmalternatives.com/2022/02/your-guide-to-trend-following/)."

[2022-08-07]
- Impressive results using CTAs as overlays. Because CTAs have near zero corr with 60/40 and both have Sharpe of 0.85, 100/100% of both yields 0.85*sqrt(2) = 1.19, as reported
- E(return overall) = 2\*E(R per position), while stdev(overall) = sqrt(2\*stdev[position]).
- I made a similar research & same result (sqrt(2) multiple) for different periods in [blog post](https://hedgenordic.com/2020/06/60-40-portfolios-and-the-need-for-smart-diversification/): "60/40 portfolios and the need for smart diversification".