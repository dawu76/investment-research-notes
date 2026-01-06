"""
Options Premium Scanner

Scan options premiums across multiple stocks to find the best covered call
and cash-secured put opportunities.
"""

from .scanner import (
    OptionsPremiumScanner,
    parse_arguments,
    display_comparison_table,
    export_to_csv,
    main
)

__version__ = '1.0.0'

__all__ = [
    'OptionsPremiumScanner',
    'parse_arguments',
    'display_comparison_table',
    'export_to_csv',
    'main'
]
