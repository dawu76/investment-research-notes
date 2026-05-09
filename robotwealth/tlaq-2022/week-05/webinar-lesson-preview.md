### Data Analysis – Mindset and Techniques

---

#### Conducting effective research

Guidelines
- formulate hypotheses and figure out the quickest way to prove or disprove it
- chunk down the problems into sub-problems and tackle each one in isolation, one step at a time
- don't just jump into testing lots of different strategy rules in some backtesting software; avoid data-mining for rules that randomly happened to do well in the past
- don't let the research turn into a big S/W engineering problem, like building a feature engineering pipeline
- make progress with rapid iterations; don't get hung up with statistical subtleties to start with
- don't take common trading platitudes for granted; break down statements into underlying assumptions

Tips for research
- get comfortable with common patterns of data analysis: reshaping and munging data, quickly exploring it via histograms, scatterplots, time-series charts, checking for stationarity, factor analysis, simulation, event studies
- comfort with ambiguity is required; you'll never know for sure whether the hypothesized edge truly exists; at some point you just have to move forward with trying it or not, and you may need to revisit it in the future as conditions change

Aim for precision in hypotheses
- related to "don't take common trading platitudes for granted"; avoid magical thinking and uncover implicit assumptions
- example of an unclear statement: "stop losses cap your downside to the stop level"
- why would this be true? think about cause & effect; what assumptions are behind the belief that if the price hits a certain level, it's likely to be trending in that same direction? and if you do exit the position at that stop level, you have to figure out a new trade and enter another position subject to the same risks of the position moving against you
- a more precise version of that would be: "it caps the downside of my current trade to the stop level, less any slippage (which can be large for discontinuous jumps during times of volatility"
- then ask yourself, "when would this be helpful to me in a portfolio?" if my stop loss level is predictive of future price actions; it wouldn't be helpful if the price would be as likely to go back up vs. continuing dowward";

Another example of a statement requiring uncovering assumptions
- "Volatility has been realizing significantly over (under) implied so it's good to be long (short) vega here"
- this is saying that IV based on options prices over the past N days has been less than RV, and we think that will continue into the future, so we should be long volatility since it's selling more cheaply than it should
- another assumption being taken for granted: volatility will continue to be over (under) implied in the near future (RV > IV) given its recent history;
- what aspects of the statement would we actually want to test?

---
