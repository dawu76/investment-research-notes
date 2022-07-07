### [Analysis of equity VRP](https://robotwealth.com/courses/trade-like-a-quant-bootcamp/lessons/5-research-mindset-and-data-analysis-techniques/topic/research-example-1-analysis-of-equity-vrp/)

Techniques covered + accompanying [Colab notebook](https://colab.research.google.com/drive/1X3rkf2bxaWqq31giX9u-Eh_zD5uAplKG?usp=sharing)
- Getting index data
- Munging and reshaping data
- Plotting distributions
- Time-series charts and stationarity
- Scatterplots
- Correlograms
- Exploratory analysis
- Splitting our data into time-subsets

---

#### Tackling a research question
- What not to do: progress immediately to simulating a given strategy and testing how it's done historically
- What to do: simple direct data analysis
- Goals of exercise: to demonstrate how a quantitative trader thinks through a problem and asking questions

---

Brief intro to R
- using pipes to chain together a series of transforms via `%>%`

---

#### Step 1: getting data

Don't get hung up on getting the perfect data - if it's close enough, use it to see if we can quickly disprove your hypothesis. If it's still unclear, then go back to get better data.

Data we want to get: IV and RV of SPX
- source of IV: IV of ATM 30-DTE SPX options
- source of RV: daily SPX prices over past 30 days

What almost equivalent data is easiest to get?
- VIX index levels from CBOE
- daily prices of the $SPY ETF (instead of $SPX): SPY is just a bit easier to get compared to SPX, which can be "fiddly" to get for free

Where can we get this data from?
- go to CBOE VIX site and download from site directly or programmatically by copying the link to CSV file and entering that in R's `read.csv()`: this gives us a dataframe of daily VIX over 1990-2022
