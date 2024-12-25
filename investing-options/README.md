### What is 'skew' and how is it measured?

In options trading, "skew" refers to the difference in implied volatility (IV) between options with different strike prices but the same expiration date. It is a measure of how the market perceives the risk of an asset moving in a particular direction. Skew is often observed as a higher implied volatility for out-of-the-money (OTM) puts compared to at-the-money (ATM) options, reflecting a market expectation of potential downside risk.

One common way to measure skew is through "**normalized skew**," which calculates the percent premium or discount of implied volatility at a specific delta strike (e.g., 25 delta) compared to the 50 delta strike. For example, if the 50 delta IV is 30% and the 25 delta put is 36%, the normalized skew is 20%. [since 36% is 600 bp higher than the 50-delta IV of 30%, and 6% / 30% = 20%]. This measure helps to determine if the skew is relatively or historically high or low by charting it as a time series or comparing it across correlated assets [[12](https://moontowermeta.com/ratiod)].

Skew can also be analyzed through option premiums rather than implied volatility, which might be more intuitive for some investors. This involves looking at how option premiums change and expressing skew through structures like vertical spreads and ratio spreads [[1](https://moontowermeta.com/ratiod)].

---

### what are the best ways to measure and view normalized skew?

To measure and view normalized skew effectively, several approaches can be utilized:

- _Normalized Skew Calculation_: This involves computing the percent premium or discount of implied volatility (IV) at a specific delta strike (e.g., 25 delta) compared to the 50 delta strike. For instance, if the 50 delta IV is 30% and the 25 delta put is 36%, the normalized skew is 20%. This measure helps determine if the skew is relatively or historically high or low by charting it as a time series or comparing it across correlated assets [[12](https://blog.moontower.ai/ratiod)].

- Charting and Visualization: Visualizing skew as a time series or percentile over a 1 or 2-year lookback can provide insights into its _behavior over time_. This can be done by plotting the normalized skew values to observe trends and anomalies¹.

- Cross-Sectional Comparison: Comparing skew across different assets or sectors can provide a broader market perspective. This involves looking at how skew behaves in similar or correlated markets, which can highlight _relative value opportunities¹_.

- Alternative Measures: Besides normalized skew, other methods like tracking the ratio of further out-of-the-money (OTM) options needed to make a spread vega-neutral can be used. This approach reduces volatility artifacts and maps to option premium as a percentage of the stock price, making it more interpretable².

- Skew Models: Using skew models to parameterize a volatility surface can help fit an implied volatility curve to a discrete chain of strikes. This involves using breakpoints like moneyness, standard deviation, or delta to measure the distance from the at-the-money (ATM) strike to the **breakpoint** [[3](https://blog.moontower.ai/breakpoints)].

By employing these methods, traders can gain a comprehensive understanding of skew dynamics and make informed trading decisions.

---

### what does a "breakpoint" mean in the context of skew models?

In the context of skew models, a "breakpoint" refers to specific points on the implied volatility (IV) curve that are used to parameterize the volatility surface. These breakpoints are critical in defining how the IV changes across different strike prices and are used to fit an IV curve to a discrete chain of option strikes.

Breakpoints can be defined using various measures, such as:
- Moneyness: This refers to the percentage distance of a strike price from the at-the-money (ATM) level. For example, a strike that is 5% out-of-the-money (OTM) is considered a _moneyness breakpoint_.

- Standard Deviation (SD) Points: These are based on the number of standard deviations a strike is from the ATM level, calculated using the ATM volatility. For instance, a '_1 SD breakpoint_' might represent a strike that is one standard deviation away from the ATM price.

- Delta: This is a measure of the option's sensitivity to changes in the underlying asset's price. A _delta-relative breakpoint_ might be a 25 delta strike, which is often used to assess skew.

These breakpoints help traders and analysts understand and model the skew by measuring the distance from the ATM strike to these specific points. The goal is to fit the market snugly without creating arbitrages in the option premiums due to irregularities in the curve [[12](https://blog.moontower.ai/breakpoints)].
