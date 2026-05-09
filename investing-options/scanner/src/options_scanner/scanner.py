#!/usr/bin/env python3
"""
Options Premium Scanner
Analyzes options premiums as % of strike price and annualized % for covered calls and cash-secured puts.
"""

import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
import argparse
import warnings
warnings.filterwarnings('ignore')


class OptionsPremiumScanner:
    def __init__(self, symbols, min_annual_return=0, max_delta=1.0, min_volume=0, min_open_interest=0,
                 min_dte=0, max_dte=365):
        self.symbols = symbols
        self.min_annual_return = min_annual_return
        self.max_delta = max_delta  # Maximum absolute delta (e.g., 0.30 for conservative)
        self.min_volume = min_volume  # Minimum daily volume for liquidity
        self.min_open_interest = min_open_interest  # Minimum open interest for liquidity
        self.min_dte = min_dte  # Minimum days to expiration
        self.max_dte = max_dte  # Maximum days to expiration
        self.results = []

    def get_stock_price(self, ticker):
        """Get current stock price"""
        try:
            stock = yf.Ticker(ticker)
            return stock.info.get('currentPrice') or stock.info.get('regularMarketPrice')
        except:
            return None

    def calculate_premium_metrics(self, premium, strike, days_to_expiration):
        """Calculate premium as % of strike and annualized %"""
        premium_pct = (premium / strike) * 100
        if days_to_expiration > 0:
            annualized_pct = premium_pct * (365 / days_to_expiration)
        else:
            annualized_pct = 0
        return premium_pct, annualized_pct

    def get_atm_strike(self, chain, current_price, option_type='call'):
        """Find the at-the-money or closest strike"""
        if chain.empty:
            return None

        strikes = chain['strike'].values
        closest_strike = min(strikes, key=lambda x: abs(x - current_price))
        return closest_strike

    def scan_symbol(self, symbol, strike_offset=0):
        """
        Scan options for a single symbol
        strike_offset: 0 = ATM, 1 = 1 strike OTM, -1 = 1 strike ITM, etc.
        """
        try:
            ticker = yf.Ticker(symbol)
            current_price = self.get_stock_price(symbol)

            if not current_price:
                print(f"❌ Could not get price for {symbol}")
                return

            # Get available expiration dates
            expirations = ticker.options

            if not expirations:
                print(f"❌ No options available for {symbol}")
                return

            print(f"\n📊 Analyzing {symbol} (Current Price: ${current_price:.2f})")

            for exp_date in expirations[:8]:  # Limit to next 8 expirations
                try:
                    # Get options chain
                    opt_chain = ticker.option_chain(exp_date)
                    calls = opt_chain.calls
                    puts = opt_chain.puts

                    # Calculate days to expiration
                    exp_datetime = datetime.strptime(exp_date, '%Y-%m-%d')
                    days_to_exp = (exp_datetime - datetime.now()).days

                    # Skip expired options
                    if days_to_exp < 0:
                        continue

                    # Filter by DTE range
                    if days_to_exp < self.min_dte or days_to_exp > self.max_dte:
                        continue

                    # Find ATM strikes
                    call_strikes = sorted(calls['strike'].unique())
                    put_strikes = sorted(puts['strike'].unique())

                    # Get target strikes
                    call_strike_idx = min(range(len(call_strikes)),
                                         key=lambda i: abs(call_strikes[i] - current_price))
                    put_strike_idx = min(range(len(put_strikes)),
                                        key=lambda i: abs(put_strikes[i] - current_price))

                    # Adjust for offset
                    call_strike_idx = min(max(0, call_strike_idx + strike_offset), len(call_strikes) - 1)
                    put_strike_idx = min(max(0, put_strike_idx + strike_offset), len(put_strikes) - 1)

                    call_strike = call_strikes[call_strike_idx]
                    put_strike = put_strikes[put_strike_idx]

                    # Get call data (for covered calls)
                    call_data = calls[calls['strike'] == call_strike].iloc[0]
                    call_bid = call_data['bid']
                    # Use lastPrice if bid is 0 (markets closed)
                    if call_bid == 0 or pd.isna(call_bid):
                        call_bid = call_data.get('lastPrice', 0)
                    call_delta = call_data.get('delta', None)
                    if call_delta is not None and not pd.isna(call_delta):
                        call_delta = abs(call_delta)
                    else:
                        call_delta = None
                    call_volume = int(call_data.get('volume', 0)) if not pd.isna(call_data.get('volume', 0)) else 0
                    call_oi = int(call_data.get('openInterest', 0)) if not pd.isna(call_data.get('openInterest', 0)) else 0
                    call_premium_pct, call_annual_pct = self.calculate_premium_metrics(
                        call_bid, call_strike, days_to_exp
                    )
                    # Calculate moneyness (% OTM/ITM)
                    # For calls: positive = OTM (strike above price)
                    call_moneyness = ((call_strike - current_price) / current_price) * 100

                    # Get put data (for cash-secured puts)
                    put_data = puts[puts['strike'] == put_strike].iloc[0]
                    put_bid = put_data['bid']
                    # Use lastPrice if bid is 0 (markets closed)
                    if put_bid == 0 or pd.isna(put_bid):
                        put_bid = put_data.get('lastPrice', 0)
                    put_delta = put_data.get('delta', None)
                    if put_delta is not None and not pd.isna(put_delta):
                        put_delta = abs(put_delta)
                    else:
                        put_delta = None
                    put_volume = int(put_data.get('volume', 0)) if not pd.isna(put_data.get('volume', 0)) else 0
                    put_oi = int(put_data.get('openInterest', 0)) if not pd.isna(put_data.get('openInterest', 0)) else 0
                    put_premium_pct, put_annual_pct = self.calculate_premium_metrics(
                        put_bid, put_strike, days_to_exp
                    )
                    # Calculate moneyness (% OTM/ITM)
                    # For puts: positive = OTM (strike below price)
                    put_moneyness = ((current_price - put_strike) / current_price) * 100

                    # Filter by minimum annual return, maximum delta, volume, and open interest
                    # Only store if either calls OR puts meet ALL thresholds
                    # If delta is not available (None), skip delta filter
                    call_meets_threshold = (call_annual_pct >= self.min_annual_return and
                                          (call_delta is None or call_delta <= self.max_delta) and
                                          call_volume >= self.min_volume and
                                          call_oi >= self.min_open_interest)
                    put_meets_threshold = (put_annual_pct >= self.min_annual_return and
                                         (put_delta is None or put_delta <= self.max_delta) and
                                         put_volume >= self.min_volume and
                                         put_oi >= self.min_open_interest)

                    meets_threshold = call_meets_threshold or put_meets_threshold

                    if meets_threshold:
                        self.results.append({
                            'Symbol': symbol,
                            'Current Price': current_price,
                            'Expiration': exp_date,
                            'DTE': days_to_exp,
                            'Call Strike': call_strike,
                            'Call Bid': call_bid,
                            'Call Delta': call_delta,
                            'Call Moneyness': call_moneyness,
                            'Call Volume': call_volume,
                            'Call OI': call_oi,
                            'Call Premium %': call_premium_pct,
                            'Call Annual %': call_annual_pct,
                            'Put Strike': put_strike,
                            'Put Bid': put_bid,
                            'Put Delta': put_delta,
                            'Put Moneyness': put_moneyness,
                            'Put Volume': put_volume,
                            'Put OI': put_oi,
                            'Put Premium %': put_premium_pct,
                            'Put Annual %': put_annual_pct,
                        })

                except Exception as e:
                    print(f"  ⚠️  Error processing {exp_date}: {str(e)}")
                    continue

        except Exception as e:
            print(f"❌ Error scanning {symbol}: {str(e)}")

    def scan_all(self, strike_offset=0):
        """Scan all symbols"""
        print("=" * 80)
        print("🔍 OPTIONS PREMIUM SCANNER")
        print("=" * 80)

        # Check market hours
        now = datetime.now()
        market_open = now.replace(hour=9, minute=30, second=0, microsecond=0)
        market_close = now.replace(hour=16, minute=0, second=0, microsecond=0)
        is_market_hours = market_open <= now <= market_close and now.weekday() < 5

        if not is_market_hours:
            print("⚠️  Markets are CLOSED - using last traded prices instead of live bids")
            print("   (Prices may not reflect current market conditions)")
            print("   (Delta values may not be available - showing N/A when unavailable)")
            print("=" * 80)

        # Display active filters
        filters = []
        if self.min_annual_return > 0:
            filters.append(f"Min Annual Return = {self.min_annual_return:.1f}%")
        if self.max_delta < 1.0:
            filters.append(f"Max Delta = {self.max_delta:.2f}")
        if self.min_volume > 0:
            filters.append(f"Min Volume = {self.min_volume}")
        if self.min_open_interest > 0:
            filters.append(f"Min Open Interest = {self.min_open_interest}")
        if self.min_dte > 0 or self.max_dte < 365:
            if self.min_dte > 0 and self.max_dte < 365:
                filters.append(f"DTE Range = {self.min_dte}-{self.max_dte} days")
            elif self.min_dte > 0:
                filters.append(f"Min DTE = {self.min_dte} days")
            else:
                filters.append(f"Max DTE = {self.max_dte} days")

        if filters:
            print(f"📊 Filtering: {', '.join(filters)}")
            print("=" * 80)

        for symbol in self.symbols:
            self.scan_symbol(symbol, strike_offset)

        return self.get_results()

    def get_results(self):
        """Return results as DataFrame"""
        if not self.results:
            return pd.DataFrame()

        df = pd.DataFrame(self.results)
        return df


def display_comparison_table(df, strategy='calls'):
    """Display a comparison table for a specific strategy"""
    if df.empty:
        print("No data to display")
        return

    if strategy == 'calls':
        print("\n" + "=" * 100)
        print("📈 COVERED CALLS COMPARISON")
        print("=" * 100)

        # Create pivot table for calls
        for exp_date in df['Expiration'].unique():
            exp_data = df[df['Expiration'] == exp_date].copy()
            dte = exp_data['DTE'].iloc[0]

            print(f"\n📅 Expiration: {exp_date} ({dte} days)")
            print("-" * 100)

            display_df = exp_data[['Symbol', 'Current Price', 'Call Strike',
                                   'Call Bid', 'Call Delta', 'Call Moneyness', 'Call Volume', 'Call OI',
                                   'Call Premium %', 'Call Annual %']].copy()
            display_df.columns = ['Symbol', 'Price', 'Strike', 'Bid', 'Delta', '%OTM', 'Vol', 'OI', 'Premium %', 'Annual %']
            display_df = display_df.sort_values('Annual %', ascending=False)

            # Format delta to show N/A if None
            display_df['Delta'] = display_df['Delta'].apply(
                lambda x: 'N/A' if pd.isna(x) or x is None else f'{x:.2f}'
            )

            # Custom formatting for display
            formatters = {
                'Symbol': lambda x: f'{x:>6}',
                'Price': lambda x: f'{x:>6.2f}',
                'Strike': lambda x: f'{x:>6.2f}',
                'Bid': lambda x: f'{x:>4.2f}',
                'Delta': lambda x: f'{x:>5}',
                '%OTM': lambda x: f'{x:>5.1f}',
                'Vol': lambda x: f'{x:>5.0f}',
                'OI': lambda x: f'{x:>6.0f}',
                'Premium %': lambda x: f'{x:>9.2f}',
                'Annual %': lambda x: f'{x:>8.2f}'
            }
            print(display_df.to_string(index=False, formatters=formatters))

    else:  # puts
        print("\n" + "=" * 100)
        print("📉 CASH-SECURED PUTS COMPARISON")
        print("=" * 100)

        for exp_date in df['Expiration'].unique():
            exp_data = df[df['Expiration'] == exp_date].copy()
            dte = exp_data['DTE'].iloc[0]

            print(f"\n📅 Expiration: {exp_date} ({dte} days)")
            print("-" * 100)

            display_df = exp_data[['Symbol', 'Current Price', 'Put Strike',
                                   'Put Bid', 'Put Delta', 'Put Moneyness', 'Put Volume', 'Put OI',
                                   'Put Premium %', 'Put Annual %']].copy()
            display_df.columns = ['Symbol', 'Price', 'Strike', 'Bid', 'Delta', '%OTM', 'Vol', 'OI', 'Premium %', 'Annual %']
            display_df = display_df.sort_values('Annual %', ascending=False)

            # Format delta to show N/A if None
            display_df['Delta'] = display_df['Delta'].apply(
                lambda x: 'N/A' if pd.isna(x) or x is None else f'{x:.2f}'
            )

            # Custom formatting for display
            formatters = {
                'Symbol': lambda x: f'{x:>6}',
                'Price': lambda x: f'{x:>6.2f}',
                'Strike': lambda x: f'{x:>6.2f}',
                'Bid': lambda x: f'{x:>4.2f}',
                'Delta': lambda x: f'{x:>5}',
                '%OTM': lambda x: f'{x:>5.1f}',
                'Vol': lambda x: f'{x:>5.0f}',
                'OI': lambda x: f'{x:>6.0f}',
                'Premium %': lambda x: f'{x:>9.2f}',
                'Annual %': lambda x: f'{x:>8.2f}'
            }
            print(display_df.to_string(index=False, formatters=formatters))


def export_to_csv(df, filename='options_premiums.csv'):
    """Export results to CSV"""
    if not df.empty:
        df.to_csv(filename, index=False)
        print(f"\n💾 Results saved to {filename}")


def parse_arguments():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(
        description='Options Premium Scanner - Find profitable covered call and cash-secured put opportunities',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  # Conservative monthly put selling
  %(prog)s --symbols AAPL MSFT NVDA --min-annual 25 --max-delta 0.30 --min-dte 30 --max-dte 45

  # Aggressive weekly trading
  %(prog)s --symbols TSLA AMD --min-annual 40 --max-dte 21 --min-volume 100

  # High liquidity blue chips only
  %(prog)s --symbols AAPL MSFT GOOGL --min-volume 50 --min-oi 500
        '''
    )

    # Watchlist
    parser.add_argument(
        '--symbols', '-s',
        nargs='+',
        default=['AAPL', 'MSFT', 'GOOGL', 'NVDA', 'AMD', 'TSLA'],
        help='Stock symbols to scan (default: AAPL MSFT GOOGL NVDA AMD TSLA)'
    )

    # Strike selection
    parser.add_argument(
        '--strike-offset',
        type=int,
        default=1,
        help='Strike offset from ATM: 0=ATM, 1=1 strike OTM, -1=1 strike ITM (default: 1)'
    )

    # Return filtering
    parser.add_argument(
        '--min-annual', '--min-return',
        type=float,
        default=25.0,
        dest='min_annual_return',
        help='Minimum annualized return percentage (default: 25.0)'
    )

    # Delta filtering
    parser.add_argument(
        '--max-delta',
        type=float,
        default=1.0,
        help='Maximum absolute delta - lower=more conservative (0.30=conservative, 0.20=very conservative, 1.0=all) (default: 1.0)'
    )

    # Liquidity filters
    parser.add_argument(
        '--min-volume', '--min-vol',
        type=int,
        default=10,
        dest='min_volume',
        help='Minimum daily trading volume for liquidity (default: 10)'
    )

    parser.add_argument(
        '--min-oi', '--min-open-interest',
        type=int,
        default=0,
        dest='min_open_interest',
        help='Minimum open interest for liquidity (default: 0)'
    )

    # DTE filtering
    parser.add_argument(
        '--min-dte',
        type=int,
        default=0,
        help='Minimum days to expiration (default: 0)'
    )

    parser.add_argument(
        '--max-dte',
        type=int,
        default=60,
        help='Maximum days to expiration - focus on your preferred time horizon (default: 60)'
    )

    # Output
    parser.add_argument(
        '--csv',
        type=str,
        default='options_premiums.csv',
        help='CSV output filename (default: options_premiums.csv)'
    )

    return parser.parse_args()


def main():
    # Parse command line arguments
    args = parse_arguments()

    # Create scanner with parsed arguments
    scanner = OptionsPremiumScanner(
        symbols=args.symbols,
        min_annual_return=args.min_annual_return,
        max_delta=args.max_delta,
        min_volume=args.min_volume,
        min_open_interest=args.min_open_interest,
        min_dte=args.min_dte,
        max_dte=args.max_dte
    )

    # Scan all symbols
    results_df = scanner.scan_all(strike_offset=args.strike_offset)

    if not results_df.empty:
        # Display comparison tables
        display_comparison_table(results_df, strategy='calls')
        display_comparison_table(results_df, strategy='puts')

        # Export to CSV
        export_to_csv(results_df, filename=args.csv)

        print("\n" + "=" * 100)
        print("✅ Scan complete!")
        print("=" * 100)
    else:
        print("\n❌ No results found")


if __name__ == "__main__":
    main()
