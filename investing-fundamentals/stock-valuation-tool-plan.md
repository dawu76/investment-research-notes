# Stock Valuation Analysis Tool - Implementation Plan

## Overview
A comprehensive stock valuation tool that enables users to:
1. Perform traditional DCF (Discounted Cash Flow) analysis to determine intrinsic stock value
2. Conduct reverse DCF analysis to reveal growth assumptions embedded in the current market price
3. Compare market expectations versus personal assumptions to identify investment opportunities

## Core Objectives

### 1. Forward DCF Analysis
Calculate intrinsic stock value based on user-provided assumptions about future cash flows and growth.

**Output**: "Fair value" price per share based on user's assumptions

### 2. Reverse DCF Analysis
Work backwards from the current stock price to determine what growth rates and assumptions the market is implicitly pricing in.

**Output**: Growth rates and assumptions embedded in current market price

### 3. Comparative Analysis
Side-by-side comparison enabling users to see:
- What the market expects vs. what the user believes
- Upside/downside potential
- Sensitivity analysis for key assumptions

---

## Required User Inputs

### Company Financials (Historical/Current)
- **Revenue** (current/trailing twelve months)
- **Free Cash Flow (FCF)** (current/TTM)
- **Operating Margin** (current/TTM)
- **Shares Outstanding**
- **Current Stock Price**
- **Net Debt** (Total Debt - Cash)

### User Assumptions (for Forward DCF)
1. **Revenue Growth Rate**
   - Year 1-5: Individual year projections or single average
   - Year 6-10: Long-term growth rate
   - Terminal growth rate (typically 2-3% or GDP growth)

2. **Margin Assumptions**
   - Operating margin trajectory
   - Target operating margin (for mature phase)

3. **Discount Rate / WACC (Weighted Average Cost of Capital)**
   - Option A: User provides WACC directly (8-12% typical range)
   - Option B: Tool calculates WACC from:
     - Risk-free rate (10-year Treasury yield)
     - Equity risk premium (typically 5-7%)
     - Beta (stock volatility vs. market)
     - Cost of debt
     - Debt-to-equity ratio

4. **Capital Expenditure & Working Capital**
   - CapEx as % of revenue
   - Change in Net Working Capital (NWC) as % of revenue change

5. **Tax Rate**
   - Effective corporate tax rate (typically 21-25%)

### Market Context (for Reverse DCF)
- Current stock price
- Shares outstanding
- Net debt

---

## API Integration & Data Auto-Population

### Overview
Rather than manually entering all company data, the tool can automatically fetch most financial metrics from public data sources, leaving users to focus only on their forward-looking assumptions and judgments.

### What Can Be Auto-Populated

#### ✅ Fully Automatable (High Confidence)
These can be reliably fetched from APIs:

1. **Current Stock Price & Market Data**
   - Real-time or 15-min delayed price
   - Shares outstanding
   - Market capitalization
   - Beta
   - 52-week high/low

2. **Historical Financials (from 10-K/10-Q filings)**
   - Revenue (annual & quarterly)
   - Operating income / EBIT
   - Net income
   - Free cash flow
   - Total debt
   - Cash & cash equivalents
   - Operating cash flow
   - Capital expenditures
   - Depreciation & amortization

3. **Balance Sheet Items**
   - Total assets
   - Total liabilities
   - Shareholders' equity
   - Working capital components

4. **Key Metrics & Ratios**
   - Operating margin (historical)
   - Net margin
   - ROE, ROIC
   - Debt-to-equity ratio
   - Current ratio

5. **Company Information**
   - Company name
   - Sector/industry
   - Description
   - Number of employees
   - Headquarters location

#### ⚠️ Partially Automatable (User Verification Recommended)
These can be fetched but may need adjustment:

1. **Tax Rate**
   - Can calculate from historical effective tax rate
   - User may want to adjust for future changes

2. **WACC Components**
   - Risk-free rate: Auto-fetch 10-year Treasury yield
   - Beta: Auto-fetch from financial APIs
   - Market risk premium: Use standard 5-7% or user override
   - Cost of debt: Calculate from interest expense / total debt
   - Debt-to-equity: Auto-calculate from balance sheet
   - **Final WACC**: Tool can calculate, user should review

3. **Working Capital as % of Revenue**
   - Calculate historical average
   - User may want to adjust for future expectations

#### ❌ Cannot Be Auto-Populated (Require User Judgment)
These are forward-looking and require user assumptions:

1. **Future Revenue Growth Rates**
   - Historical growth can be shown for reference
   - User must input their expectations

2. **Future Operating Margin**
   - Historical margins shown for context
   - User decides on margin expansion/contraction path

3. **Terminal Growth Rate**
   - User judgment (typically 2-3%)

4. **Future CapEx as % of Revenue**
   - Historical average shown
   - User adjusts based on business stage

### Available Data Sources & APIs

#### Free APIs (Good for MVP)

**1. yfinance (Yahoo Finance) - BEST FREE OPTION**
- **Cost**: Free, no API key required
- **Python Library**: `pip install yfinance`
- **Data Available**:
  - Real-time stock prices
  - Historical prices
  - Financial statements (annual & quarterly)
  - Balance sheet, income statement, cash flow
  - Key statistics (beta, market cap, shares outstanding)
  - Company info
- **Limitations**:
  - Unofficial API (relies on Yahoo Finance scraping)
  - Rate limits (but generous for individual use)
  - Occasional data inconsistencies
  - May break if Yahoo changes their structure
- **Best For**: Personal use, prototyping, testing

**Example Code**:
```python
import yfinance as yf

# Fetch company data
ticker = yf.Ticker("AAPL")

# Current price and market data
current_price = ticker.info['currentPrice']
shares_outstanding = ticker.info['sharesOutstanding']
beta = ticker.info['beta']

# Financial statements
income_stmt = ticker.income_stmt  # Annual
quarterly_income = ticker.quarterly_income_stmt
balance_sheet = ticker.balance_sheet
cash_flow = ticker.cashflow

# Specific metrics
revenue = income_stmt.loc['Total Revenue'][0]  # Most recent year
operating_income = income_stmt.loc['Operating Income'][0]
fcf = cash_flow.loc['Free Cash Flow'][0]
```

**2. Financial Modeling Prep (FMP) - Free Tier**
- **Cost**: Free tier available (250 calls/day)
- **API Key**: Required (sign up at financialmodelingprep.com)
- **Data Available**:
  - Stock prices
  - Financial statements (3-5 years free)
  - Company profiles
  - Key metrics
  - DCF calculations (can compare against your model)
- **Limitations**:
  - 250 API calls per day limit on free tier
  - Limited historical data (5 years)
- **Best For**: More reliable than yfinance, good for serious projects

**Example Code**:
```python
import requests

API_KEY = 'your_api_key'
symbol = 'AAPL'

# Income statement
url = f'https://financialmodelingprep.com/api/v3/income-statement/{symbol}?apikey={API_KEY}'
income_data = requests.get(url).json()

# Get most recent annual data
latest = income_data[0]
revenue = latest['revenue']
operating_income = latest['operatingIncome']
```

**3. Alpha Vantage - Free Tier**
- **Cost**: Free tier (25 calls/day)
- **API Key**: Required
- **Data Available**:
  - Stock prices
  - Financial statements
  - Company overview
  - Earnings data
- **Limitations**:
  - Very restrictive rate limits (25/day)
  - 5 calls per minute max
- **Best For**: Backup option, limited use

**4. SEC EDGAR API - Most Reliable**
- **Cost**: Free, no key required
- **Data Available**:
  - All public company filings (10-K, 10-Q, etc.)
  - Direct from the source (most reliable)
  - Historical data going back decades
- **Limitations**:
  - Requires parsing XBRL/HTML documents
  - More complex implementation
  - No ready-made financial ratios
- **Best For**: Production applications needing reliability

#### Paid APIs (Professional Grade)

**1. Financial Modeling Prep - Paid**
- **Cost**: $30-50/month
- **Features**: Unlimited calls, more historical data, real-time data

**2. Polygon.io**
- **Cost**: $29-199/month
- **Features**: Real-time market data, extensive historical data

**3. Quandl/Nasdaq Data Link**
- **Cost**: Varies by dataset
- **Features**: Premium financial data, economic indicators

**4. Bloomberg API / FactSet**
- **Cost**: $$$$ (enterprise level)
- **Features**: Institutional-grade data
- **Best For**: Professional financial firms only

### Recommended Implementation Strategy

#### Phase 1: Start with yfinance (Free)
**Pros:**
- Zero cost
- Very easy to implement
- No API key management
- Good enough for 95% of use cases

**Cons:**
- Unofficial API
- Could break in future

#### Phase 2: Add FMP as Fallback (Freemium)
**Implementation:**
```python
def get_company_data(ticker):
    """Fetch data with fallback logic"""
    try:
        # Try yfinance first (free, no rate limits)
        data = fetch_from_yfinance(ticker)
        if data_is_valid(data):
            return data
    except Exception as e:
        print(f"yfinance failed: {e}")

    try:
        # Fallback to FMP
        data = fetch_from_fmp(ticker)
        return data
    except Exception as e:
        print(f"FMP failed: {e}")

    # Last resort: manual input
    return None
```

### Auto-Population User Experience

#### Input Flow

**Step 1: Ticker Entry**
```
Enter stock ticker: AAPL
[Fetch Data Button]

Fetching data for Apple Inc. (AAPL)...
✓ Current price: $178.45
✓ Market data retrieved
✓ Financial statements loaded (last 5 years)
✓ Cash flow data retrieved
```

**Step 2: Data Review & Adjustment**
```
COMPANY FINANCIALS (Auto-Populated)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Current Stock Price: $178.45
Shares Outstanding: 15.55B
Market Cap: $2.77T
Beta: 1.29

FINANCIAL METRICS (TTM)
Revenue: $383.3B
Operating Income: $114.3B
Operating Margin: 29.8%
Free Cash Flow: $99.6B
Net Debt: -$51.0B (net cash position)

[Edit Values] [Refresh Data]
```

**Step 3: User Assumptions**
```
YOUR ASSUMPTIONS (Manual Input Required)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Historical Revenue Growth (for reference):
  3-Year CAGR: 7.8%
  5-Year CAGR: 9.2%

Your Revenue Growth Assumptions:
  Years 1-5: [8.0]% per year
  Years 6-10: [5.0]% per year
  Terminal: [2.5]%

Operating Margin Trajectory:
  Current: 29.8% (auto-filled)
  Target (Year 10): [30.0]%

[Historical margins shown in chart for reference]
```

### Implementation Code Structure

```python
# data_fetcher.py

import yfinance as yf
from dataclasses import dataclass
from typing import Optional

@dataclass
class CompanyData:
    """Auto-populated company data"""
    ticker: str
    company_name: str
    current_price: float
    shares_outstanding: float
    beta: float

    # Financials (most recent year/TTM)
    revenue: float
    operating_income: float
    free_cash_flow: float
    total_debt: float
    cash: float
    net_debt: float

    # Calculated metrics
    operating_margin: float
    market_cap: float

    # Historical context
    revenue_growth_3y: float
    revenue_growth_5y: float
    historical_margins: list

def fetch_company_data(ticker: str) -> Optional[CompanyData]:
    """
    Fetch all auto-populatable data for a company

    Args:
        ticker: Stock ticker symbol

    Returns:
        CompanyData object or None if fetch fails
    """
    try:
        stock = yf.Ticker(ticker)
        info = stock.info

        # Get financial statements
        income_stmt = stock.income_stmt
        balance_sheet = stock.balance_sheet
        cash_flow = stock.cashflow

        # Extract key metrics
        data = CompanyData(
            ticker=ticker.upper(),
            company_name=info.get('longName', ''),
            current_price=info.get('currentPrice', 0),
            shares_outstanding=info.get('sharesOutstanding', 0),
            beta=info.get('beta', 1.0),

            revenue=income_stmt.loc['Total Revenue'][0],
            operating_income=income_stmt.loc['Operating Income'][0],
            free_cash_flow=cash_flow.loc['Free Cash Flow'][0],

            total_debt=balance_sheet.loc['Total Debt'][0],
            cash=balance_sheet.loc['Cash'][0],
            net_debt=balance_sheet.loc['Total Debt'][0] - balance_sheet.loc['Cash'][0],

            operating_margin=calculate_margin(income_stmt),
            market_cap=info.get('marketCap', 0),

            revenue_growth_3y=calculate_cagr(income_stmt, years=3),
            revenue_growth_5y=calculate_cagr(income_stmt, years=5),
            historical_margins=calculate_historical_margins(income_stmt)
        )

        return data

    except Exception as e:
        print(f"Error fetching data for {ticker}: {e}")
        return None

def calculate_suggested_wacc(ticker: str) -> dict:
    """
    Auto-calculate WACC components

    Returns dict with all components and final WACC
    """
    stock = yf.Ticker(ticker)
    info = stock.info

    # Get current 10-year Treasury rate (risk-free rate)
    treasury = yf.Ticker("^TNX")
    risk_free_rate = treasury.info['regularMarketPrice'] / 100

    # Get beta
    beta = info.get('beta', 1.0)

    # Use standard equity risk premium
    equity_risk_premium = 0.065  # 6.5%

    # Calculate cost of equity (CAPM)
    cost_of_equity = risk_free_rate + beta * equity_risk_premium

    # Get debt information
    balance_sheet = stock.balance_sheet
    total_debt = balance_sheet.loc['Total Debt'][0]

    # Calculate cost of debt from interest expense
    income_stmt = stock.income_stmt
    interest_expense = income_stmt.loc['Interest Expense'][0]
    cost_of_debt = abs(interest_expense) / total_debt if total_debt > 0 else 0.04

    # Get market values
    market_cap = info.get('marketCap', 0)

    # Calculate weights
    total_value = market_cap + total_debt
    weight_equity = market_cap / total_value
    weight_debt = total_debt / total_value

    # Tax rate
    tax_rate = 0.21  # Standard corporate tax rate

    # Calculate WACC
    wacc = (weight_equity * cost_of_equity) + (weight_debt * cost_of_debt * (1 - tax_rate))

    return {
        'wacc': wacc,
        'cost_of_equity': cost_of_equity,
        'cost_of_debt': cost_of_debt,
        'risk_free_rate': risk_free_rate,
        'beta': beta,
        'equity_risk_premium': equity_risk_premium,
        'weight_equity': weight_equity,
        'weight_debt': weight_debt,
        'tax_rate': tax_rate,
        'components_breakdown': f"""
        WACC Calculation:

        Cost of Equity (CAPM): {cost_of_equity:.2%}
          = {risk_free_rate:.2%} + {beta:.2f} × {equity_risk_premium:.2%}

        Cost of Debt (after-tax): {cost_of_debt * (1-tax_rate):.2%}
          = {cost_of_debt:.2%} × (1 - {tax_rate:.1%})

        Capital Structure:
          Equity: {weight_equity:.1%}
          Debt: {weight_debt:.1%}

        WACC = {wacc:.2%}
        """
    }
```

### Data Validation & Quality Checks

#### Automatic Validation
```python
def validate_fetched_data(data: CompanyData) -> dict:
    """
    Check data quality and flag potential issues

    Returns dict of warnings/issues
    """
    issues = []

    # Check for missing critical data
    if data.current_price <= 0:
        issues.append("WARNING: Invalid stock price")

    if data.shares_outstanding <= 0:
        issues.append("WARNING: Invalid shares outstanding")

    if data.revenue <= 0:
        issues.append("WARNING: Invalid revenue data")

    # Check for suspicious values
    if data.operating_margin > 0.60:
        issues.append("INFO: Very high operating margin (>60%). Verify data.")

    if data.operating_margin < 0:
        issues.append("INFO: Company is currently unprofitable")

    # Calculate implied market cap and compare
    implied_market_cap = data.current_price * data.shares_outstanding
    if abs(implied_market_cap - data.market_cap) / data.market_cap > 0.05:
        issues.append("WARNING: Market cap mismatch. Data may be stale.")

    return {
        'is_valid': len([i for i in issues if 'WARNING' in i]) == 0,
        'issues': issues
    }
```

### Caching Strategy

To minimize API calls and improve performance:

```python
import json
from datetime import datetime, timedelta
from pathlib import Path

class DataCache:
    """Cache fetched data to minimize API calls"""

    def __init__(self, cache_dir='.cache'):
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(exist_ok=True)
        self.cache_duration = timedelta(hours=4)  # Refresh every 4 hours

    def get(self, ticker: str) -> Optional[CompanyData]:
        """Get cached data if available and fresh"""
        cache_file = self.cache_dir / f"{ticker}.json"

        if not cache_file.exists():
            return None

        with open(cache_file) as f:
            cached = json.load(f)

        cached_time = datetime.fromisoformat(cached['timestamp'])

        if datetime.now() - cached_time < self.cache_duration:
            return CompanyData(**cached['data'])

        return None

    def set(self, ticker: str, data: CompanyData):
        """Cache data"""
        cache_file = self.cache_dir / f"{ticker}.json"

        with open(cache_file, 'w') as f:
            json.dump({
                'timestamp': datetime.now().isoformat(),
                'data': data.__dict__
            }, f)
```

### User Control & Override

Always allow users to:
1. **Review auto-populated data** before proceeding
2. **Manually override any value** if they have better information
3. **Refresh data** to get latest values
4. **See data source & timestamp** for transparency
5. **Save/load scenarios** with specific data snapshots

Example UI:
```
APPLE INC (AAPL)
Data fetched: 2025-11-07 10:30 AM
Source: Yahoo Finance

Revenue (TTM): $383.3B [Edit] [Info]
  ℹ️ From: Most recent 10-K filing
  📊 Historical: $365B (2023), $394B (2022)
```

---

## Calculation Methodology

### Forward DCF Process

#### Step 1: Project Free Cash Flows
For each year in the projection period (typically 10 years):

```
Revenue(t) = Revenue(t-1) × (1 + Growth Rate(t))

EBIT(t) = Revenue(t) × Operating Margin(t)

NOPAT(t) = EBIT(t) × (1 - Tax Rate)

FCF(t) = NOPAT(t)
         - CapEx(t)
         - Change in NWC(t)
         + Depreciation & Amortization(t)

Simplified FCF(t) = NOPAT(t) × (1 - Reinvestment Rate)
```

#### Step 2: Calculate Terminal Value
```
Terminal FCF = FCF(Year 10) × (1 + Terminal Growth Rate)

Terminal Value = Terminal FCF / (WACC - Terminal Growth Rate)
```

#### Step 3: Discount to Present Value
```
PV(FCF(t)) = FCF(t) / (1 + WACC)^t

PV(Terminal Value) = Terminal Value / (1 + WACC)^10
```

#### Step 4: Calculate Enterprise & Equity Value
```
Enterprise Value = Sum of all PV(FCF) + PV(Terminal Value)

Equity Value = Enterprise Value - Net Debt

Intrinsic Value per Share = Equity Value / Shares Outstanding

Upside/Downside = (Intrinsic Value - Current Price) / Current Price × 100%
```

### Reverse DCF Process

#### Objective
Solve for the implied growth rate that makes the DCF valuation equal to the current market price.

#### Step 1: Set Known Variables
- Current stock price (given)
- WACC (use same as forward DCF or typical range)
- Terminal growth rate (typically 2-3%)
- Current financials (revenue, margins, FCF)

#### Step 2: Solve for Implied Growth Rate
Work backwards to find the revenue CAGR (Years 1-10) that produces:
```
Current Stock Price = DCF Valuation (with implied growth rate)
```

This requires an iterative/solver approach:
1. Start with a guess for growth rate (e.g., 5%)
2. Calculate DCF value with that growth rate
3. Compare to current stock price
4. Adjust growth rate and repeat until convergence

#### Step 3: Present Market Expectations
Output the implied metrics:
- **Revenue CAGR** (Years 1-10) implied by current price
- **Implied revenue in Year 10**
- **Implied operating margin trajectory** (if margin expansion is assumed)
- **Required FCF growth rate**

#### Step 4: Reality Check
Compare implied assumptions to:
- Historical company growth rates
- Industry average growth rates
- Market/GDP growth expectations
- Competitive dynamics

---

## Output Format & User Experience

### Interface Design

#### Input Section
**Tab 1: Company Basics**
- Company name/ticker
- Current financial metrics
- Current stock price

**Tab 2: Your Assumptions (Forward DCF)**
- Growth rate inputs (with sliders/input fields)
- Margin assumptions
- WACC calculation or input
- CapEx and working capital assumptions

**Tab 3: Market Assumptions (Reverse DCF)**
- Set parameters for what to solve for
- Constraints/ranges for implied metrics

#### Output Section

**Dashboard View:**

```
┌─────────────────────────────────────────────────────────────┐
│                    VALUATION SUMMARY                        │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Current Stock Price: $XXX.XX                               │
│                                                             │
│  YOUR VALUATION (Forward DCF)                               │
│  Intrinsic Value: $XXX.XX                                   │
│  Upside/(Downside): +XX% or -XX%                            │
│                                                             │
│  MARKET EXPECTATIONS (Reverse DCF)                          │
│  Implied Revenue CAGR: XX%                                  │
│  Your Assumed CAGR: XX%                                     │
│  Difference: Market expects XX% more/less growth            │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Detailed Comparison Table:**

| Metric | Your Assumption | Market Implied | Difference |
|--------|----------------|----------------|------------|
| Revenue CAGR (10Y) | X% | Y% | +/- Z% |
| Year 10 Revenue | $XXB | $XXB | +/- $XXB |
| Operating Margin (Y10) | X% | Y% | +/- Z% |
| Terminal Growth | X% | Y% | +/- Z% |

**10-Year Cash Flow Projection Table:**

| Year | Revenue | EBIT | FCF | PV of FCF | Cumulative PV |
|------|---------|------|-----|-----------|---------------|
| 1 | $XXB | $XXM | $XXM | $XXM | $XXM |
| 2 | $XXB | $XXM | $XXM | $XXM | $XXM |
| ... | ... | ... | ... | ... | ... |
| 10 | $XXB | $XXM | $XXM | $XXM | $XXM |
| Terminal | - | - | - | $XXB | $XXB |

**Sensitivity Analysis:**

Show how intrinsic value changes with different assumptions:
- WACC ± 1%, ± 2%
- Growth rate ± 2%, ± 5%
- Terminal margin ± 2%

**Visual Charts:**
1. Bar chart: Current Price vs. Your Valuation vs. Bull/Bear Case
2. Line chart: Revenue projection over 10 years (Your Assumption vs. Market Implied)
3. Waterfall chart: Bridge from current FCF to terminal value
4. Tornado chart: Sensitivity analysis showing impact of each variable

---

## Implementation Options

### Option 1: Excel/Google Sheets Template
**Pros:**
- Most accessible for finance professionals
- Easy to customize and iterate
- Built-in calculation and charting tools
- Portable and shareable

**Cons:**
- Limited automation
- Manual data entry required
- Less sophisticated UI/UX

**Implementation:**
- Create structured worksheets for inputs, calculations, and outputs
- Use Excel formulas and Goal Seek for reverse DCF
- Add data validation and conditional formatting
- Include instructions and examples

### Option 2: Python Script/Jupyter Notebook
**Pros:**
- Powerful calculation capabilities
- Can integrate with financial data APIs (yfinance, Alpha Vantage, etc.)
- Automated data retrieval
- Professional visualizations (matplotlib, plotly)
- Version control friendly
- Can use optimization libraries (scipy.optimize) for reverse DCF

**Cons:**
- Requires Python knowledge
- Setup complexity for non-technical users
- Less interactive than web app

**Key Libraries:**
- `pandas` - data manipulation
- `numpy` - numerical calculations
- `scipy.optimize` - for reverse DCF solver
- `matplotlib`/`plotly` - visualization
- `yfinance` - stock data retrieval (optional)
- `jupyter` - interactive notebook interface

**File Structure:**
```
stock-valuation-tool/
├── valuation_tool.py (core calculation functions)
├── dcf_calculator.ipynb (interactive notebook)
├── requirements.txt
├── examples/
│   ├── example_tech_company.ipynb
│   └── example_mature_company.ipynb
└── README.md
```

### Option 3: Web Application
**Pros:**
- Best user experience
- Most accessible (browser-based)
- Real-time interactivity
- Can save/load scenarios
- Professional presentation

**Cons:**
- Most complex to build
- Requires hosting
- Maintenance overhead

**Tech Stack Options:**
- Frontend: React, Vue.js, or Streamlit (Python)
- Backend: Flask/FastAPI (Python) or Node.js
- Database: PostgreSQL/SQLite for saving scenarios
- Deployment: Heroku, Vercel, or AWS

---

## Implementation Steps (Python-based Approach)

### Phase 1: Core Calculation Engine (Week 1)
1. **Create forward DCF calculator**
   - Input validation class
   - FCF projection function
   - Terminal value calculation
   - NPV calculation
   - Equity value per share calculation

2. **Create reverse DCF solver**
   - Implement optimization algorithm (scipy.optimize.fsolve or minimize)
   - Solve for implied growth rate given current price
   - Solve for implied margins (optional advanced feature)

3. **Unit tests**
   - Test with known examples
   - Verify mathematical accuracy
   - Edge case handling

### Phase 2: Data Input & Validation (Week 1-2)
1. **Create input data structures**
   - Company data class
   - Assumptions data class
   - Validation rules

2. **Optional: API integration**
   - Pull current stock price
   - Pull basic financials
   - Handle API errors gracefully

### Phase 3: Output & Visualization (Week 2)
1. **Create output formatters**
   - Summary statistics
   - Detailed projection tables
   - Comparison tables (user vs. market)

2. **Build visualizations**
   - Revenue projection charts
   - Valuation comparison charts
   - Sensitivity analysis
   - Waterfall chart for value drivers

### Phase 4: User Interface (Week 2-3)
**Option A: Jupyter Notebook**
- Interactive widgets (ipywidgets)
- Clear documentation and instructions
- Example companies pre-loaded

**Option B: Streamlit Web App**
- Input forms with validation
- Real-time calculation updates
- Professional dashboard layout
- Export functionality (PDF, CSV)

### Phase 5: Documentation & Examples (Week 3)
1. **User guide**
   - How to use the tool
   - How to interpret results
   - Common pitfalls and best practices

2. **Example analyses**
   - High-growth tech company
   - Mature stable company
   - Turnaround situation

3. **Technical documentation**
   - API documentation
   - Calculation methodology
   - Assumptions and limitations

### Phase 6: Testing & Refinement (Week 3-4)
1. **Validation testing**
   - Compare results to professional models
   - Test with real company data
   - User acceptance testing

2. **Performance optimization**
   - Speed improvements for calculations
   - Caching for API calls

3. **Polish and bug fixes**

---

## Key Formulas Reference

### WACC (Weighted Average Cost of Capital)
```
WACC = (E/V × Re) + (D/V × Rd × (1-Tc))

Where:
E = Market value of equity
D = Market value of debt
V = E + D (total value)
Re = Cost of equity
Rd = Cost of debt
Tc = Corporate tax rate
```

### Cost of Equity (CAPM)
```
Re = Rf + β × (Rm - Rf)

Where:
Rf = Risk-free rate (10-year Treasury)
β = Beta (stock volatility vs market)
Rm - Rf = Equity risk premium (typically 5-7%)
```

### Free Cash Flow
```
FCF = NOPAT - Net Investment

NOPAT = EBIT × (1 - Tax Rate)

Net Investment = CapEx - Depreciation + Δ NWC

Simplified:
FCF = Operating Cash Flow - CapEx
```

### Terminal Value (Perpetuity Growth Model)
```
Terminal Value = FCF(final year) × (1 + g) / (WACC - g)

Where g = terminal growth rate (typically 2-3%)
```

---

## Risk Factors & Limitations

### Model Assumptions
1. **DCF is highly sensitive to assumptions**
   - Small changes in WACC or growth rates dramatically impact valuation
   - Terminal value often represents 60-80% of total value

2. **Garbage in, garbage out**
   - Model is only as good as the input assumptions
   - Requires deep understanding of the business

3. **Not suitable for all companies**
   - Pre-revenue or early-stage companies
   - Financial institutions (use different models)
   - Highly cyclical businesses (requires adjusted approach)

### Best Practices
1. **Use conservative assumptions**
   - Build in margin of safety
   - Use range of scenarios (base, bull, bear)

2. **Validate against multiple methods**
   - Compare to comparable company analysis
   - Check vs. precedent transactions
   - Sanity check with simple multiples (P/E, EV/EBITDA)

3. **Focus on the reverse DCF insight**
   - Understanding what's priced in is often more valuable than calculating precise intrinsic value
   - Ask: "Do I believe the company can achieve what the market expects?"

4. **Sensitivity analysis is critical**
   - Show range of outcomes
   - Identify key value drivers
   - Stress test assumptions

---

## Success Metrics

The tool will be considered successful if it:
1. **Produces accurate calculations** that match professional-grade models
2. **Provides clear insights** into market expectations vs. user assumptions
3. **Is easy to use** for someone with basic finance knowledge
4. **Enables better investment decisions** by highlighting key assumptions and risks
5. **Saves time** compared to building models from scratch in Excel

---

## Next Steps

1. **Decide on implementation format**
   - Excel template (fastest, most accessible)
   - Python/Jupyter (most flexible, best for iteration)
   - Web app (best UX, most complex)

2. **Start with MVP (Minimum Viable Product)**
   - Basic forward DCF calculator
   - Simple reverse DCF solver
   - Command-line or basic notebook interface

3. **Iterate based on usage**
   - Add features based on user needs
   - Improve UX/UI
   - Add more sophisticated features (scenario analysis, Monte Carlo, etc.)

4. **Create example analyses**
   - Document real-world use cases
   - Build confidence in the tool
   - Serve as templates for future analyses

---

## Resources & References

### Educational Resources
- Aswath Damodaran's valuation materials (NYU Stern)
- McKinsey Valuation book
- Investment Banking texts (Rosenbaum & Pearl)

### Tools & Libraries
- Python: scipy, numpy, pandas, plotly
- Excel: Solver add-in, Data Tables
- Data sources: yfinance, Alpha Vantage, Financial Modeling Prep API

### Example Models
- Damodaran's valuation spreadsheets
- Wall Street Prep DCF model templates
- Breaking Into Wall Street models

---

## Conclusion

This stock valuation tool will empower users to:
- Understand what growth and returns are embedded in current stock prices
- Make more informed investment decisions based on their own assumptions
- Quickly analyze multiple stocks with consistent methodology
- Develop deeper intuition about valuation and market expectations

The reverse DCF component is particularly valuable as it shifts the question from "What is this stock worth?" to "What would have to be true for this stock to be fairly valued?" - a much more useful framing for practical investment decisions.
