"""
Unit tests for the amortization schedule generator.
"""

import sys
import unittest
from pathlib import Path

# Allow importing modules from the src directory.
sys.path.append(
    str(Path(__file__).resolve().parents[1] / "src")
)

from amortization import generate_amortization_schedule


class TestAmortizationSchedule(unittest.TestCase):
    """Tests for generate_amortization_schedule()."""

    def test_schedule_length(self):
        """A 30-year mortgage should produce 360 monthly payments."""
        schedule = generate_amortization_schedule(
            principal=300_000,
            annual_interest_rate=6.5,
            loan_term_years=30,
        )

        self.assertEqual(len(schedule), 360)

    def test_first_payment(self):
        """Verify the values of the first payment."""
        schedule = generate_amortization_schedule(
            principal=300_000,
            annual_interest_rate=6.5,
            loan_term_years=30,
        )

        first = schedule[0]

        self.assertEqual(first["payment_number"], 1)
        self.assertAlmostEqual(first["payment"], 1896.20, places=2)
        self.assertAlmostEqual(first["principal"], 271.20, places=2)
        self.assertAlmostEqual(first["interest"], 1625.00, places=2)
        self.assertAlmostEqual(first["balance"], 299728.80, places=2)

    def test_last_payment_balance(self):
        """The final balance should be zero (within rounding tolerance)."""
        schedule = generate_amortization_schedule(
            principal=300_000,
            annual_interest_rate=6.5,
            loan_term_years=30,
        )

        last = schedule[-1]

        self.assertAlmostEqual(last["balance"], 0.00, places=2)

    def test_invalid_principal(self):
        """Principal must be greater than zero."""
        with self.assertRaises(ValueError):
            generate_amortization_schedule(
                principal=0,
                annual_interest_rate=6.5,
                loan_term_years=30,
            )

    def test_negative_interest_rate(self):
        """Interest rate cannot be negative."""
        with self.assertRaises(ValueError):
            generate_amortization_schedule(
                principal=300_000,
                annual_interest_rate=-1.0,
                loan_term_years=30,
            )

    def test_invalid_loan_term(self):
        """Loan term must be greater than zero."""
        with self.assertRaises(ValueError):
            generate_amortization_schedule(
                principal=300_000,
                annual_interest_rate=6.5,
                loan_term_years=0,
            )


if __name__ == "__main__":
    unittest.main()