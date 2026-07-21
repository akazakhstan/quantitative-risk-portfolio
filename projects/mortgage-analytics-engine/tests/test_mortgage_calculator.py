"""
Unit tests for the mortgage calculator module.
"""

import unittest
from pathlib import Path
import sys

# Allow importing from the src directory
sys.path.append(
    str(Path(__file__).resolve().parents[1] / "src")
)

from mortgage_calculator import calculate_monthly_payment


class TestMortgageCalculator(unittest.TestCase):
    """Tests for calculate_monthly_payment()."""

    def test_standard_mortgage(self):
        """Test a standard 30-year fixed-rate mortgage."""
        payment = calculate_monthly_payment(
            principal=300_000,
            annual_interest_rate=6.5,
            loan_term_years=30,
        )

        self.assertAlmostEqual(payment, 1896.20, places=2)

    def test_zero_interest(self):
        """Test a zero-interest loan."""
        payment = calculate_monthly_payment(
            principal=120_000,
            annual_interest_rate=0.0,
            loan_term_years=30,
        )

        self.assertEqual(payment, 333.33)

    def test_negative_principal(self):
        """Principal must be positive."""
        with self.assertRaises(ValueError):
            calculate_monthly_payment(
                principal=-1000,
                annual_interest_rate=6.5,
                loan_term_years=30,
            )

    def test_negative_interest_rate(self):
        """Interest rate cannot be negative."""
        with self.assertRaises(ValueError):
            calculate_monthly_payment(
                principal=300_000,
                annual_interest_rate=-1,
                loan_term_years=30,
            )

    def test_invalid_loan_term(self):
        """Loan term must be greater than zero."""
        with self.assertRaises(ValueError):
            calculate_monthly_payment(
                principal=300_000,
                annual_interest_rate=6.5,
                loan_term_years=0,
            )


if __name__ == "__main__":
    unittest.main()