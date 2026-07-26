# Options Scanner Review & Improvement Suggestions

**Date:** 2026-01-25
**Focus:** Conservative Put Selling & Credit Spread Opportunities

---

## Executive Summary

The current options scanner is a well-architected tool for identifying covered call and cash-secured put opportunities. However, for traders focused on **conservative put selling** and **credit spreads**, several enhancements would significantly improve usability and profitability identification.

---

## Current Design Strengths

1. **Clean Architecture**: Single-file OOP design with clear separation of concerns
2. **Comprehensive Filtering**: DTE, delta, volume, OI, and return thresholds
3. **Annualized Returns**: Enables fair comparison across different timeframes
4. **Graceful Degradation**: Works during market hours and after hours
5. **Good Test Coverage**: 27 unit tests covering core functionality
6. **CLI Flexibility**: All parameters configurable via command line

---

## Suggested Improvements

### 1. Add Credit Spread Support (High Priority)

**Current Gap:** The scanner only supports single-leg strategies (covered calls, cash-secured puts). Credit spreads (bull put spreads, bear call spreads) are popular conservative strategies that limit risk.

**Recommended Implementation:**

```python
# New class or method addition
def scan_put_credit_spreads(self, symbol, width=5):
    """
    Scan for bull put spread opportunities.

    Args:
        symbol: Stock ticker
        width: Dollar width between strikes (e.g., $5 spread)

    Returns credit spreads with:
        - Net credit received
        - Max loss (width - credit)
        - Return on risk (credit / max_loss)
        - Probability of profit (based on short leg delta)
    """
```

**New CLI Arguments:**
```bash
--strategy {puts,calls,put-spreads,call-spreads,all}
--spread-width 5  # Default $5 wide spreads
--min-credit 0.50  # Minimum net credit to collect
```

**Key Metrics to Add:**
| Metric | Formula | Purpose |
|--------|---------|---------|
| Net Credit | Short Put Bid - Long Put Ask | Actual premium collected |
| Max Loss | Spread Width - Net Credit | Worst case scenario |
| Return on Risk | Net Credit / Max Loss × 100 | Risk-adjusted return |
| Breakeven | Short Strike - Net Credit | Price where P/L = 0 |

---

### 2. Enhanced Risk Metrics for Conservative Traders (High Priority)

**Current Gap:** The scanner shows delta but lacks comprehensive risk assessment.

**Recommended Additions:**

```python
# Add to scan results
{
    'probability_otm': 1 - abs(delta),  # Approx probability of profit
    'expected_value': (prob_otm * premium) - (prob_itm * max_loss),
    'risk_reward_ratio': premium / (strike - premium),  # For puts
    'margin_requirement': calculate_margin(strike, price),
    'return_on_margin': (premium / margin) * (365 / dte) * 100,
}
```

**New CLI Filters:**
```bash
--min-prob-profit 70     # Minimum probability of profit (%)
--max-risk-reward 3      # Maximum risk/reward ratio
--show-expected-value    # Display EV calculations
```

---

### 3. Support Price & Technical Context (Medium Priority)

**Current Gap:** Decisions are made purely on premium metrics without price context.

**Recommended Additions:**

```python
def get_price_context(self, symbol):
    """Get technical context for strike selection."""
    ticker = yf.Ticker(symbol)
    hist = ticker.history(period="6mo")

    return {
        'price_52w_high': hist['High'].max(),
        'price_52w_low': hist['Low'].min(),
        'price_percentile': calculate_percentile(current, low, high),
        'sma_50': hist['Close'].rolling(50).mean().iloc[-1],
        'sma_200': hist['Close'].rolling(200).mean().iloc[-1],
        'support_levels': identify_supports(hist),  # Key for put strikes
        'iv_rank': get_iv_rank(symbol),  # Higher = better premium
    }
```

**Display Enhancement:**
```
Symbol  Price   52W%  SMA50  SMA200  Support  IV Rank
  AAPL 271.01   75%  265.50  248.20   260.00      45%
```

**New CLI Options:**
```bash
--show-technicals        # Include price context
--strike-near-support    # Prefer strikes near support levels
--min-iv-rank 30         # Only scan when IV is elevated
```

---

### 4. Improved Strike Selection for Conservative Put Selling (Medium Priority)

**Current Gap:** Strike offset (0, 1, -1) is too coarse for precise positioning.

**Recommended Changes:**

```python
# Replace strike_offset with more flexible options
def select_conservative_put_strike(self, chain, current_price, method='delta'):
    """
    Select put strike using conservative criteria.

    Methods:
        'delta': Select strike with delta closest to target
        'otm_percent': Select strike N% below current price
        'support': Select strike at or below nearest support
        'std_dev': Select strike N standard deviations below
    """
```

**New CLI Arguments:**
```bash
--strike-method {delta,otm_percent,support,std_dev}
--target-delta 0.20      # Target delta for strike selection
--target-otm-percent 5   # Target 5% OTM
--std-dev-distance 1.5   # 1.5 standard deviations OTM
```

---

### 5. Watchlist & Symbol Management (Medium Priority)

**Current Gap:** Symbols are passed via CLI each time.

**Recommended Implementation:**

```python
# Support watchlist files
WATCHLISTS = {
    'blue_chip': ['AAPL', 'MSFT', 'GOOGL', 'JNJ', 'PG'],
    'high_iv': ['TSLA', 'NVDA', 'AMD', 'MARA', 'COIN'],
    'dividend': ['KO', 'PEP', 'JNJ', 'PG', 'MMM'],
    'etf': ['SPY', 'QQQ', 'IWM', 'DIA', 'XLF'],
}

# Or load from file
def load_watchlist(filepath):
    """Load symbols from JSON/YAML/TXT file."""
```

**New CLI Arguments:**
```bash
--watchlist blue_chip           # Use predefined watchlist
--watchlist-file my_stocks.txt  # Load from file
--exclude TSLA                  # Exclude specific symbols
```

---

### 6. Position Sizing & Portfolio Context (Low Priority)

**Current Gap:** No consideration of account size or position limits.

**Recommended Additions:**

```python
def calculate_position_sizing(self, strike, account_size, max_risk_pct=2):
    """
    Calculate appropriate position size.

    Args:
        strike: Put strike price
        account_size: Total account value
        max_risk_pct: Maximum % of account to risk per trade

    Returns:
        max_contracts: Maximum contracts within risk limit
        capital_required: Cash needed for assignment
        portfolio_allocation: % of portfolio this represents
    """
```

**New CLI Arguments:**
```bash
--account-size 100000    # Account size for position sizing
--max-risk-percent 2     # Max 2% risk per position
--show-sizing            # Display position size recommendations
```

---

### 7. Enhanced Output & Sorting Options (Low Priority)

**Current Gap:** Fixed sorting by annual % only.

**Recommended Changes:**

```python
# Flexible sorting
SORT_OPTIONS = [
    'annual_pct',      # Current default
    'premium_pct',     # Raw premium %
    'probability',     # Probability of profit
    'risk_reward',     # Risk/reward ratio
    'expected_value',  # Expected value
    'volume',          # Liquidity
    'moneyness',       # Distance from current price
]
```

**New CLI Arguments:**
```bash
--sort-by probability    # Sort by probability of profit
--sort-desc              # Descending order (default)
--top-n 10               # Show only top 10 results
--group-by symbol        # Group results by symbol instead of expiration
```

---

### 8. Alert & Screening Presets (Low Priority)

**Current Gap:** Users must remember complex CLI arguments.

**Recommended Implementation:**

```python
PRESETS = {
    'conservative_puts': {
        'max_delta': 0.20,
        'min_dte': 30,
        'max_dte': 45,
        'min_volume': 100,
        'min_oi': 500,
        'min_annual': 15,
    },
    'aggressive_premium': {
        'max_delta': 0.35,
        'min_dte': 7,
        'max_dte': 21,
        'min_annual': 50,
    },
    'wheel_strategy': {
        'max_delta': 0.30,
        'min_dte': 30,
        'max_dte': 60,
        'min_annual': 20,
        'strategy': 'both',  # calls and puts
    },
}
```

**New CLI Arguments:**
```bash
--preset conservative_puts   # Use predefined settings
--list-presets               # Show available presets
--save-preset my_settings    # Save current settings as preset
```

---

## Implementation Priority Matrix

| Improvement | Impact | Effort | Priority |
|------------|--------|--------|----------|
| Credit Spread Support | High | High | **P0** |
| Enhanced Risk Metrics | High | Medium | **P0** |
| Price/Technical Context | Medium | Medium | **P1** |
| Improved Strike Selection | Medium | Low | **P1** |
| Watchlist Management | Medium | Low | **P2** |
| Position Sizing | Low | Medium | **P2** |
| Enhanced Sorting | Low | Low | **P3** |
| Screening Presets | Low | Low | **P3** |

---

## Quick Wins (Can Implement Today)

### 1. Add Probability of Profit Display

In `scanner.py`, add to result dictionary:
```python
'call_prob_profit': round((1 - call_delta) * 100, 1) if call_delta else None,
'put_prob_profit': round((1 - put_delta) * 100, 1) if put_delta else None,
```

### 2. Add Risk/Reward Ratio

```python
# For cash-secured puts
'put_risk_reward': round(put_strike / put_bid, 2) if put_bid > 0 else None,
```

### 3. Add Conservative Preset

Add to argument parser:
```python
parser.add_argument('--conservative', action='store_true',
    help='Use conservative settings: delta<=0.20, DTE 30-45, vol>=100')
```

### 4. Add IV Percentile (if available)

```python
# yfinance may provide impliedVolatility
iv = option_data.get('impliedVolatility', None)
```

---

## Sample Enhanced Output (Proposed)

```
═══════════════════════════════════════════════════════════════════════════════
                    CONSERVATIVE PUT SELLING OPPORTUNITIES
═══════════════════════════════════════════════════════════════════════════════

📊 Price Context:
Symbol   Price   52W Range    %ile   SMA50   SMA200   IV Rank
  AAPL  271.01  164-275      95%    268.50   245.20     35%
  MSFT  442.50  366-468      85%    435.00   410.50     28%

📅 Expiration: 2026-02-21 (27 DTE)
Symbol  Strike    Bid  Delta  %OTM  ProbProfit  Risk/Reward  Annual%  Contracts*
  AAPL  260.00   2.85  0.18   4.1%      82%        91:1       39.8%      3
  MSFT  425.00   4.20  0.22   3.9%      78%       101:1       35.9%      2

* Based on $100,000 account with 2% max risk per position

💰 Credit Spread Opportunities (Bull Put Spreads, $5 wide):
Symbol  Short   Long  Credit  MaxLoss  RetOnRisk  ProbProfit  Annual%
  AAPL  260.00  255   $1.85    $3.15     58.7%       82%      778.4%
  MSFT  425.00  420   $2.10    $2.90     72.4%       78%      964.3%
```

---

## Conclusion

The current scanner provides an excellent foundation. The highest-impact improvements for conservative put sellers are:

1. **Credit spread support** - Enables defined-risk strategies
2. **Probability of profit display** - Critical for conservative traders
3. **Risk/reward metrics** - Helps evaluate trade quality
4. **Technical context** - Informs strike selection relative to support

Implementing even the "Quick Wins" would significantly improve the tool's utility for conservative options traders.

---

## References

- Current implementation: `src/options_scanner/scanner.py`
- Tests: `tests/test_scanner.py`
- README: `README.md`
