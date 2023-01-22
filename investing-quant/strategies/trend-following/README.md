### On trend-following performance

[AQR](https://www.aqr.com/Insights/Research/White-Papers/Trend-Following-Why-Now-A-Macro-Perspective): "Trend-Following: Why Now? A Macro Perspective"
- "Both the macroeconomic picture and empirical evidence, however, suggest that strong performance for trend-following may persist, making it a potentially valuable source of diversifying returns during a challenging time for the rest of investors’ portfolios."
- "given the backdrop of persistently high inflation, a rapid and resolute shift in central banks’ policies, and the unexpected war in Ukraine, macroeconomic volatility is on the rise. As we would expect, this rise in macroeconomic volatility has also been accompanied by larger market moves and  improved trend-following performance. So far in 2022, market moves are significantly larger than average, and the SG Trend Index is on track for its best annual return since its inception in 2000, as shown in Figure 3. The current environment provides out-of-sample evidence that the relationship between large market moves and trend performance remains intact."
- "At their core, trend-following strategies capture the tendency of markets to gradually incorporate new information. This tendency creates persistent price trends, which may allow trend-following to be profitable on average. Notably, large market drawdowns and crises generally tend to have identifiable 
catalysts and to evolve gradually (e.g., GFC, 2022), which explains why trend-following strategies tend to perform particularly well in such environments. There is a direct relationship between macroeconomic volatility and the size of market moves, with the latter strongly (and intuitively) associated with trend￾following performance."
- "There is no tendency for trend-following strategies to perform worse than average following periods of extremely strong performance."

[AQR](https://www.aqr.com/Insights/Trend-Following): additional resources on trend-following
- [paper](https://www.aqr.com/Insights/Research/Journal-Article/A-Century-of-Evidence-on-Trend-Following-Investing): A century of evidence on trend-following. "This paper seeks to establish whether the strong performance of trend following is a statistical fluke of the last few decades or a more robust phenomenon that exists over a wide range of economic conditions. Using historical data from a number of sources, we construct a time series momentum strategy back to 1880 and find that the strategy was consistently profitable over the next 110 years."
- [paper](https://www.aqr.com/Insights/Research/White-Papers/A-Half-Century-of-Macro-Momentum): A Half Century of Macro Momentum. "Macro momentum – a systematic global macro strategy that takes long positions in assets for which fundamental macroeconomic trends are improving and short positions in assets for which fundamental macroeconomic trends are deteriorating – has the potential to deliver strong positive returns with low correlation to traditional asset classes across various macroeconomic and market environments, including the potential to provide important diversification benefits in bear equity markets and rising yield environments."

---

### Implementations of trend-following

[Raposa Tech](https://medium.com/raposa-technologies/beat-the-market-with-a-diversified-trend-following-model-and-the-donchian-channel-10f850ce6aee): Beat the Market with a Diversified Trend Following Model and the Donchian Channel
- Any trading system has 4 basic rules: Instrument Rule: What instruments do you trade? Entry Rule: When do you enter a trade? Exit Rule: When do you exit a trade? Position Rule: How much do you put on a trade?
- I like to use a **volatility-based position sizing** module. This scales your allocation based on the volatility of the stock, so the higher the volatility, the lower the allocation and vice versa. I usually use a 252-day lookback period (there are 252 trading days per year, so that’s a 1-year lookback) to get a reasonable sample size of the volatility.
- Specify the target risk. If we set this to 10%, it means that each position will be risk-adjusted so it takes 10% of our portfolio. Example: Say we have two stocks, A and B with a 10% Target Risk. If the volatility of stock A is 2 and the volatility of stock B is 5, then we’d allocate 5% of our capital to stock A and 2% to stock B after adjusting for risk because 10% / 2% = 5% allocation and 10% / 5% = 2% allocation.
- Entry rules: Start by keeping our entry rule quite simple and just use a Donchian Channel breakout over 100 days. This is a classic trend following indicator. I find I get better results with longer term signals (100+ days) but you could easily make it shorter term as well to suit your needs.
- ...

---

### Macro influences on trend-following performance

[Raposa Tech](https://medium.com/raposa-technologies/why-last-years-most-profitable-trading-strategy-won-t-slow-down-in-2023-2277224ebdd3): Why Last Year’s Most Profitable Trading Strategy Won’t Slow Down in 2023
- Volatility is great for trend following strategies. We need prices to move to have breakouts and if we’re positioned long or short, we don’t care which direction. Just get them moving and our systems will jump on board. Many of the major geopolitical fissures that cracked in 2022 and led to things like soaring energy prices have not been resolved. This means we can expect a continuation of these trends in the near future. Same goes for continued efforts to “green the economy.” This push shows no signs of slowing anytime soon, so a system that’s exposed to these sectors and underlying commodities stands to gain from continued trends.
- As rates begin to move, interest rates, which underpin the pricing of everything in the economy, experience more volatility. This volatility leads to more trends, opening trading opportunities that have been suppressed over the past decade.
- On-shoring consists of reducing the interconnectedness of global supply chains by bringing production closer to the end consumer and making markets more local. If, as many market participants predict, this leads to de-coupling of regional markets, we could see historic correlations break and have opportunities for further diversification as traders. Additionally, these moves often come hand-in-hand with protectionist policies such as tariffs and trade restrictions. This may further increase dispersion among formerly tightly connected global markets.

---

### CTA vs. Global Macro

Global macro strategy definitions
- This is a flexible strategy whose positions are based on views regarding the economic and geopolitical prospects of various countries. These views are informed by interest rates, politics, domestic and foreign poilcies, international trade, currency exchange rates, etc.
- Holdings may include long and short positions in various equity, fixed income, currency, commodities, and futures markets. The funds may take directional or relative value bets.

3 primary types of global macro funds
- discretionary global macro: in these funds, the PMs take a high-level view of global markets and allocate funds to asset classes accordingly in a flexible, discretionary manner
- CTAS: these funds rely primarily on trend-following algorithms to go long or short different assets (commodities, currencies, etc.)
- systematic global macro: these funds blend a discretionary and CTA-based approach

References
- [Investopedia](https://www.investopedia.com/terms/g/globalmacro.asp): Global macro strategy funds
- [Crystal Capital Funds post](https://www.crystalfunds.com/insights/breaking-down-global-macro-hedge-funds): Breaking down global macro hedge funds

---
