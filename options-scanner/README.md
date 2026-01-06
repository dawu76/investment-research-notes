# Options Premium Scanner

Scan options premiums across multiple stocks to find the best covered call and cash-secured put opportunities.

## Quick Start

1. **Install the package:**
   ```bash
   pip install -e .
   ```

2. **Run with default settings:**
   ```bash
   python3 -m options_scanner
   ```

3. **Or customize via command line:**
   ```bash
   # Conservative monthly put selling
   python3 -m options_scanner --symbols AAPL MSFT NVDA --min-annual 25 --max-delta 0.30 --min-dte 30 --max-dte 45

   # Aggressive weekly trading
   python3 -m options_scanner --symbols TSLA AMD --min-annual 40 --max-dte 21
   ```

## CLI Usage

The scanner supports **full command-line configuration** - no need to edit the script!

### View all options:
```bash
python3 -m options_scanner --help
```

### Common Usage Patterns

**Conservative monthly put selling:**
```bash
python3 -m options_scanner \
  --symbols AAPL MSFT GOOGL \
  --min-annual 25 \
  --max-delta 0.30 \
  --min-dte 30 \
  --max-dte 45 \
  --min-volume 50 \
  --min-oi 500
```

**Aggressive weekly trading:**
```bash
python3 -m options_scanner \
  --symbols TSLA AMD NVDA \
  --min-annual 40 \
  --max-dte 21 \
  --min-volume 100
```

**High premium hunting (any stock, any timeframe):**
```bash
python3 -m options_scanner \
  --symbols AAPL MSFT GOOGL NVDA AMD TSLA META AMZN \
  --min-annual 50 \
  --min-volume 25
```

**Specific stock deep dive:**
```bash
python3 -m options_scanner --symbols NVDA --min-annual 20
```

### All Available Options

| Option | Short | Description | Default |
|--------|-------|-------------|---------|
| `--symbols` | `-s` | Stock symbols to scan | AAPL MSFT GOOGL NVDA AMD TSLA |
| `--strike-offset` | | 0=ATM, 1=1 strike OTM, -1=ITM | 1 |
| `--min-annual` | `--min-return` | Minimum annualized return % | 25.0 |
| `--max-delta` | | Maximum delta (lower=conservative) | 1.0 |
| `--min-volume` | `--min-vol` | Minimum daily volume | 10 |
| `--min-oi` | `--min-open-interest` | Minimum open interest | 0 |
| `--min-dte` | | Minimum days to expiration | 0 |
| `--max-dte` | | Maximum days to expiration | 60 |
| `--csv` | | Output CSV filename | options_premiums.csv |

## Configuration Details

**Note:** All settings can be configured via CLI arguments (recommended) or by editing the script defaults.

### CLI Arguments (Recommended)

Use command-line arguments for quick, flexible scanning without editing the script. See examples in the **CLI Usage** section above.

### Strike Selection
Adjust `STRIKE_OFFSET` to control which strikes to analyze:
- `0` = At-the-money (ATM)
- `1` = 1 strike out-of-the-money (common for covered calls)
- `2` = 2 strikes OTM
- `-1` = 1 strike in-the-money

### Minimum Annual Return Filter
Set `MIN_ANNUAL_RETURN` to filter results by minimum annualized return:
```python
MIN_ANNUAL_RETURN = 30  # Only show options with 30%+ annualized return
MIN_ANNUAL_RETURN = 0   # Show all options (no filter)
MIN_ANNUAL_RETURN = 50  # Only show options with 50%+ annualized return
```
This filters results where EITHER calls OR puts meet the threshold, helping you focus on the best opportunities.

### Maximum Delta Filter (Conservative Selling)
Set `MAX_DELTA` to filter out options too close to being in-the-money:
```python
MAX_DELTA = 1.0   # Show all deltas (no filter)
MAX_DELTA = 0.30  # Conservative - slightly OTM options
MAX_DELTA = 0.20  # Very conservative - moderately OTM options
MAX_DELTA = 0.10  # Ultra conservative - far OTM options
```

**What is Delta?**
- Delta measures how likely an option is to expire in-the-money
- Lower delta = Further out-of-the-money = Less likely to be assigned
- Typical deltas: 0.50 (ATM), 0.30 (slightly OTM), 0.20 (moderately OTM), 0.10 (far OTM)

**Why filter by delta?**
- Conservative cash-secured put sellers prefer lower deltas (less assignment risk)
- Lower delta = safer but lower premium
- Good for reducing assignment risk while still earning premium

**Note:** Delta values may not be available when markets are closed. When unavailable, the delta filter is skipped and "N/A" is shown in the output.

### Liquidity Filters (Volume and Open Interest)
Filter options by trading activity to ensure you can enter and exit positions easily:

```python
MIN_VOLUME = 10          # Minimum daily trading volume
MIN_OPEN_INTEREST = 100  # Minimum open interest
```

**Volume (Vol)** - Number of contracts traded today:
- Indicates current trading activity
- Higher volume = tighter bid/ask spreads
- Typical minimums: 10 (basic), 50 (good), 100+ (excellent)

**Open Interest (OI)** - Total outstanding contracts:
- Indicates overall market interest
- Higher OI = better liquidity overall
- Typical minimums: 100 (basic), 500 (good), 1000+ (excellent)

**Why filter by liquidity?**
- Low liquidity = wider bid/ask spreads = worse fills
- Harder to exit positions if needed
- More price slippage when entering/exiting

**Recommended settings:**
- **Conservative traders**: `MIN_VOLUME=50`, `MIN_OPEN_INTEREST=500`
- **Active traders**: `MIN_VOLUME=100`, `MIN_OPEN_INTEREST=1000`
- **Any liquidity**: `MIN_VOLUME=0`, `MIN_OPEN_INTEREST=0`

**Note:** Open Interest may show as 0 when markets are closed. Volume shows the last trading day's activity.

### DTE Range Filtering (Days to Expiration)
Focus on your preferred time horizon by filtering options within a specific DTE range:

```python
MIN_DTE = 30   # Minimum days to expiration
MAX_DTE = 45   # Maximum days to expiration
```

**Why use DTE filtering?**
- **30-45 DTE** is the "sweet spot" for many options sellers (optimal theta decay)
- **7-21 DTE** for weekly options traders (faster profits, more management)
- **45-60 DTE** for longer-term positions (less monitoring needed)
- Avoid options expiring too soon (more gamma risk) or too far out (less theta)

**Common DTE strategies:**
- Conservative monthly: `MIN_DTE=30, MAX_DTE=45`
- Weekly aggressive: `MIN_DTE=0, MAX_DTE=21`
- Quarterly: `MIN_DTE=60, MAX_DTE=90`
- Show all: `MIN_DTE=0, MAX_DTE=365`

### Moneyness % Display
Every option now shows **%OTM** (percent out-of-the-money) for easy assessment:

**For Puts (Cash-Secured Puts):**
- Positive %OTM = Strike below current price (safer)
- Example: Stock at $100, $95 strike = 5.0% OTM
- Higher %OTM = further from current price = less likely to be assigned

**For Calls (Covered Calls):**
- Positive %OTM = Strike above current price (safer)
- Example: Stock at $100, $105 strike = 5.0% OTM
- Higher %OTM = more room for stock to rise before assignment

**Typical conservative ranges:**
- 2-5% OTM: Slightly conservative, decent premium
- 5-10% OTM: Conservative, lower premium, safer
- 10%+ OTM: Very conservative, low premium, very safe

**Advantage over Delta:**
- Easier to understand (5% OTM vs "0.25 delta")
- Direct relationship to stock price movement needed for assignment
- Consistent across different volatility environments

### Number of Expirations
By default, the scanner looks at the next 8 expiration dates. Change this in line 74:
```python
for exp_date in expirations[:8]:  # Change 8 to your preference
```

## Output

The script generates three outputs:

1. **Console output** - Formatted tables comparing premiums across stocks
2. **CSV file** (`options_premiums.csv`) - All data for further analysis
3. **Two comparison tables:**
   - Covered calls (sell calls against stock you own)
   - Cash-secured puts (sell puts to potentially acquire stock)

## Metrics Explained

- **Premium %**: Option premium as percentage of strike price
- **Annual %**: Premium % annualized based on days to expiration
  - Formula: `(Premium / Strike) × (365 / DTE) × 100`
  - This lets you compare short-term vs long-term options

## Example Output

```
📅 Expiration: 2026-01-16 (15 days)
Symbol  Price Strike  Bid Delta  %OTM   Vol     OI Premium % Annual %
  NVDA 145.23 147.00 2.15  0.28   1.2  1500   2400      1.46    35.52
   AMD  98.45 100.00 1.20  0.32   1.6   850   1200      1.20    29.20
  AAPL 234.56 235.00 2.80  0.29   0.2  3200   5600      1.19    29.00
```

## Tips

1. **Higher Annual %** = Better premium income (but consider risk)
2. **Weekly options** often have high annualized returns but more transaction costs
3. **Monthly options** (30-45 DTE) are popular for the theta/premium balance
4. **Compare similar DTE** expirations for apples-to-apples comparison
5. **Minimum return filter** - Start with 25-30% to focus on quality opportunities, or use 50%+ for aggressive premium hunting
6. **Delta filter for conservative selling** - Use MAX_DELTA=0.30 for conservative puts, or 0.20 for very conservative (lower assignment risk)
7. **Liquidity is critical** - Always check Vol and OI before trading; low liquidity means wider spreads and harder exits
8. **Volume vs OI** - High volume with low OI = recent interest; High OI with low volume = established position
9. **DTE sweet spot** - Most sellers prefer 30-45 DTE for optimal theta decay; use `MIN_DTE=30, MAX_DTE=45` to focus on this range
10. **Moneyness for quick assessment** - %OTM shows safety margin at a glance; 5-8% OTM is a good balance of safety and premium
11. **Combine all filters** - Example: `MIN_ANNUAL_RETURN=30`, `MAX_DELTA=0.30`, `MIN_VOLUME=50`, `MIN_OI=100`, `MIN_DTE=30`, `MAX_DTE=45` = safe, liquid, high-premium monthly options

## Testing

The scanner includes a comprehensive test suite with 27 unit tests covering:
- Premium and annualized return calculations
- Moneyness (% OTM) calculations
- Filter threshold logic
- CLI argument parsing
- DataFrame operations and CSV export
- Edge cases and boundary conditions

### Run Tests

**Using unittest (no dependencies):**
```bash
python3 -m unittest tests/test_scanner.py
```

**Using pytest (recommended):**
```bash
# Install dev dependencies
pip install -r requirements-dev.txt

# Run tests with verbose output
pytest tests/test_scanner.py -v

# Run with coverage report
pytest tests/ --cov=options_scanner --cov-report=term-missing
```

### Test Coverage

| Component | Tests | Coverage |
|-----------|-------|----------|
| Premium calculations | 4 | ✅ Complete |
| Moneyness calculations | 5 | ✅ Complete |
| Filter logic | 5 | ✅ Complete |
| CLI argument parsing | 9 | ✅ Complete |
| DataFrame operations | 2 | ✅ Complete |
| Edge cases | 3 | ✅ Complete |

All tests pass with 100% success rate.

## Limitations

- Uses Yahoo Finance (free but unofficial)
- Data may be delayed 15-20 minutes
- Rate limits apply if you scan too many symbols too quickly
- Bid prices may not reflect actual fills

## Advanced Usage

### Scan only specific strikes relative to stock price:
```python
# In scan_symbol(), modify strike selection logic
# Current: finds closest to ATM then applies offset
# Custom: filter by delta, % OTM, etc.
```

### Filter by minimum premium:
```python
# Add after calculating premiums:
if call_premium_pct < 1.0:  # Skip if less than 1%
    continue
```

### Export to Excel with formatting:
```python
# Replace CSV export with:
df.to_excel('options_premiums.xlsx', index=False)
```
