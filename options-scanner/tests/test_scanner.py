#!/usr/bin/env python3
"""
Unit tests for Options Premium Scanner
Run with: python3 -m pytest tests/test_scanner.py -v
Or: pytest tests/test_scanner.py
"""

import unittest
import pandas as pd
import sys
from io import StringIO
from options_scanner import (
    OptionsPremiumScanner,
    parse_arguments,
    display_comparison_table,
    export_to_csv
)


class TestPremiumCalculations(unittest.TestCase):
    """Test the core premium calculation logic"""

    def setUp(self):
        """Set up test fixtures"""
        self.scanner = OptionsPremiumScanner(['TEST'])

    def test_calculate_premium_metrics_basic(self):
        """Test basic premium calculation"""
        premium = 5.0
        strike = 100.0
        days_to_exp = 30

        pct, annual_pct = self.scanner.calculate_premium_metrics(
            premium, strike, days_to_exp
        )

        # Premium % = (5 / 100) * 100 = 5%
        self.assertAlmostEqual(pct, 5.0, places=2)
        # Annual % = 5% * (365 / 30) = 60.83%
        self.assertAlmostEqual(annual_pct, 60.83, places=2)

    def test_calculate_premium_metrics_zero_dte(self):
        """Test calculation with 0 days to expiration"""
        premium = 2.0
        strike = 100.0
        days_to_exp = 0

        pct, annual_pct = self.scanner.calculate_premium_metrics(
            premium, strike, days_to_exp
        )

        self.assertAlmostEqual(pct, 2.0, places=2)
        self.assertEqual(annual_pct, 0.0)  # Should be 0 when DTE = 0

    def test_calculate_premium_metrics_weekly(self):
        """Test calculation for weekly option (7 DTE)"""
        premium = 1.0
        strike = 50.0
        days_to_exp = 7

        pct, annual_pct = self.scanner.calculate_premium_metrics(
            premium, strike, days_to_exp
        )

        # Premium % = (1 / 50) * 100 = 2%
        self.assertAlmostEqual(pct, 2.0, places=2)
        # Annual % = 2% * (365 / 7) = 104.29%
        self.assertAlmostEqual(annual_pct, 104.29, places=2)

    def test_calculate_premium_metrics_yearly(self):
        """Test calculation for yearly option (365 DTE)"""
        premium = 10.0
        strike = 100.0
        days_to_exp = 365

        pct, annual_pct = self.scanner.calculate_premium_metrics(
            premium, strike, days_to_exp
        )

        # Premium % = 10%
        self.assertAlmostEqual(pct, 10.0, places=2)
        # Annual % should equal Premium % for 365 DTE
        self.assertAlmostEqual(annual_pct, 10.0, places=2)


class TestMoneynessCalculations(unittest.TestCase):
    """Test moneyness (% OTM/ITM) calculations"""

    def test_call_moneyness_otm(self):
        """Test call moneyness when strike is above price (OTM)"""
        current_price = 100.0
        call_strike = 105.0

        # Call moneyness = (105 - 100) / 100 * 100 = 5% OTM
        moneyness = ((call_strike - current_price) / current_price) * 100
        self.assertAlmostEqual(moneyness, 5.0, places=2)

    def test_call_moneyness_itm(self):
        """Test call moneyness when strike is below price (ITM)"""
        current_price = 100.0
        call_strike = 95.0

        # Call moneyness = (95 - 100) / 100 * 100 = -5% (ITM)
        moneyness = ((call_strike - current_price) / current_price) * 100
        self.assertAlmostEqual(moneyness, -5.0, places=2)

    def test_put_moneyness_otm(self):
        """Test put moneyness when strike is below price (OTM)"""
        current_price = 100.0
        put_strike = 95.0

        # Put moneyness = (100 - 95) / 100 * 100 = 5% OTM
        moneyness = ((current_price - put_strike) / current_price) * 100
        self.assertAlmostEqual(moneyness, 5.0, places=2)

    def test_put_moneyness_itm(self):
        """Test put moneyness when strike is above price (ITM)"""
        current_price = 100.0
        put_strike = 105.0

        # Put moneyness = (100 - 105) / 100 * 100 = -5% (ITM)
        moneyness = ((current_price - put_strike) / current_price) * 100
        self.assertAlmostEqual(moneyness, -5.0, places=2)

    def test_moneyness_atm(self):
        """Test moneyness at-the-money"""
        current_price = 100.0
        strike = 100.0

        call_moneyness = ((strike - current_price) / current_price) * 100
        put_moneyness = ((current_price - strike) / current_price) * 100

        self.assertAlmostEqual(call_moneyness, 0.0, places=2)
        self.assertAlmostEqual(put_moneyness, 0.0, places=2)


class TestFilterLogic(unittest.TestCase):
    """Test filtering threshold logic"""

    def test_annual_return_filter(self):
        """Test minimum annual return filtering"""
        scanner = OptionsPremiumScanner(['TEST'], min_annual_return=30.0)
        self.assertEqual(scanner.min_annual_return, 30.0)

    def test_delta_filter(self):
        """Test maximum delta filtering"""
        scanner = OptionsPremiumScanner(['TEST'], max_delta=0.30)
        self.assertEqual(scanner.max_delta, 0.30)

    def test_volume_filter(self):
        """Test minimum volume filtering"""
        scanner = OptionsPremiumScanner(['TEST'], min_volume=100)
        self.assertEqual(scanner.min_volume, 100)

    def test_dte_range_filter(self):
        """Test DTE range filtering"""
        scanner = OptionsPremiumScanner(['TEST'], min_dte=30, max_dte=45)
        self.assertEqual(scanner.min_dte, 30)
        self.assertEqual(scanner.max_dte, 45)

    def test_multiple_filters(self):
        """Test combining multiple filters"""
        scanner = OptionsPremiumScanner(
            ['TEST'],
            min_annual_return=25.0,
            max_delta=0.30,
            min_volume=50,
            min_open_interest=100,
            min_dte=30,
            max_dte=45
        )
        self.assertEqual(scanner.min_annual_return, 25.0)
        self.assertEqual(scanner.max_delta, 0.30)
        self.assertEqual(scanner.min_volume, 50)
        self.assertEqual(scanner.min_open_interest, 100)
        self.assertEqual(scanner.min_dte, 30)
        self.assertEqual(scanner.max_dte, 45)


class TestCLIArgumentParsing(unittest.TestCase):
    """Test command-line argument parsing"""

    def test_default_arguments(self):
        """Test default argument values"""
        # Mock sys.argv with just the script name
        sys.argv = ['options_premium_scanner.py']
        args = parse_arguments()

        self.assertEqual(args.symbols, ['AAPL', 'MSFT', 'GOOGL', 'NVDA', 'AMD', 'TSLA'])
        self.assertEqual(args.strike_offset, 1)
        self.assertEqual(args.min_annual_return, 25.0)
        self.assertEqual(args.max_delta, 1.0)
        self.assertEqual(args.min_volume, 10)
        self.assertEqual(args.min_open_interest, 0)
        self.assertEqual(args.min_dte, 0)
        self.assertEqual(args.max_dte, 60)
        self.assertEqual(args.csv, 'options_premiums.csv')

    def test_custom_symbols(self):
        """Test custom symbol argument"""
        sys.argv = ['options_premium_scanner.py', '--symbols', 'AAPL', 'NVDA']
        args = parse_arguments()
        self.assertEqual(args.symbols, ['AAPL', 'NVDA'])

    def test_min_annual_argument(self):
        """Test minimum annual return argument"""
        sys.argv = ['options_premium_scanner.py', '--min-annual', '30']
        args = parse_arguments()
        self.assertEqual(args.min_annual_return, 30.0)

    def test_max_delta_argument(self):
        """Test maximum delta argument"""
        sys.argv = ['options_premium_scanner.py', '--max-delta', '0.30']
        args = parse_arguments()
        self.assertEqual(args.max_delta, 0.30)

    def test_dte_range_arguments(self):
        """Test DTE range arguments"""
        sys.argv = ['options_premium_scanner.py', '--min-dte', '30', '--max-dte', '45']
        args = parse_arguments()
        self.assertEqual(args.min_dte, 30)
        self.assertEqual(args.max_dte, 45)

    def test_liquidity_arguments(self):
        """Test liquidity filter arguments"""
        sys.argv = ['options_premium_scanner.py', '--min-volume', '50', '--min-oi', '500']
        args = parse_arguments()
        self.assertEqual(args.min_volume, 50)
        self.assertEqual(args.min_open_interest, 500)

    def test_csv_output_argument(self):
        """Test custom CSV filename"""
        sys.argv = ['options_premium_scanner.py', '--csv', 'custom_output.csv']
        args = parse_arguments()
        self.assertEqual(args.csv, 'custom_output.csv')

    def test_combined_arguments(self):
        """Test multiple arguments together"""
        sys.argv = [
            'options_premium_scanner.py',
            '--symbols', 'AAPL', 'MSFT',
            '--min-annual', '30',
            '--max-delta', '0.30',
            '--min-dte', '30',
            '--max-dte', '45'
        ]
        args = parse_arguments()
        self.assertEqual(args.symbols, ['AAPL', 'MSFT'])
        self.assertEqual(args.min_annual_return, 30.0)
        self.assertEqual(args.max_delta, 0.30)
        self.assertEqual(args.min_dte, 30)
        self.assertEqual(args.max_dte, 45)


class TestDataFrameOperations(unittest.TestCase):
    """Test DataFrame transformations and exports"""

    def test_export_to_csv(self):
        """Test CSV export functionality"""
        # Create sample data
        data = {
            'Symbol': ['AAPL', 'NVDA'],
            'Current Price': [150.0, 200.0],
            'Call Strike': [155.0, 205.0],
            'Call Bid': [3.0, 4.0],
            'Call Delta': [0.30, 0.35],
            'Call Moneyness': [3.33, 2.50],
            'Call Volume': [100, 200],
            'Call OI': [500, 1000],
            'Call Premium %': [1.94, 1.95],
            'Call Annual %': [35.0, 40.0]
        }
        df = pd.DataFrame(data)

        # Export to temp file
        import tempfile
        import os

        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv') as f:
            temp_file = f.name

        try:
            export_to_csv(df, filename=temp_file)

            # Verify file was created and has content
            self.assertTrue(os.path.exists(temp_file))

            # Read back and verify
            df_read = pd.read_csv(temp_file)
            self.assertEqual(len(df_read), 2)
            self.assertEqual(list(df_read['Symbol']), ['AAPL', 'NVDA'])
        finally:
            # Clean up
            if os.path.exists(temp_file):
                os.remove(temp_file)

    def test_empty_dataframe_export(self):
        """Test that empty DataFrame doesn't create file"""
        df = pd.DataFrame()

        import tempfile
        import os

        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv') as f:
            temp_file = f.name

        # Remove the file first
        os.remove(temp_file)

        try:
            export_to_csv(df, filename=temp_file)
            # File should not be created for empty DataFrame
            self.assertFalse(os.path.exists(temp_file))
        finally:
            if os.path.exists(temp_file):
                os.remove(temp_file)


class TestEdgeCases(unittest.TestCase):
    """Test edge cases and boundary conditions"""

    def test_very_small_premium(self):
        """Test calculation with very small premium"""
        scanner = OptionsPremiumScanner(['TEST'])
        premium = 0.01
        strike = 100.0
        days_to_exp = 30

        pct, annual_pct = scanner.calculate_premium_metrics(
            premium, strike, days_to_exp
        )

        self.assertAlmostEqual(pct, 0.01, places=2)
        self.assertGreater(annual_pct, 0)

    def test_very_large_premium(self):
        """Test calculation with very large premium"""
        scanner = OptionsPremiumScanner(['TEST'])
        premium = 50.0
        strike = 100.0
        days_to_exp = 7

        pct, annual_pct = scanner.calculate_premium_metrics(
            premium, strike, days_to_exp
        )

        self.assertAlmostEqual(pct, 50.0, places=2)
        # Should be very high annualized return
        self.assertGreater(annual_pct, 2000)

    def test_high_strike_price(self):
        """Test moneyness with high strike price"""
        current_price = 1000.0
        strike = 1050.0

        moneyness = ((strike - current_price) / current_price) * 100
        self.assertAlmostEqual(moneyness, 5.0, places=2)


if __name__ == '__main__':
    # Run tests with verbose output
    unittest.main(verbosity=2)
