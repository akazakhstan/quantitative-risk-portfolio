"""
Mortgage Analytics Engine

Core mortgage calculation functions for fixed-rate residential loans.

This module provides reusable financial calculations that serve as the
foundation for mortgage analytics, amortization schedules, and loan analysis.

Author: Mukhtarbek Abdurazakov
"""

from typing import Final

MONTHS_PER_YEAR: Final[int] = 12
PERCENT_TO_DECIMAL: Final[float] = 100.0


def calculate_monthly_payment(
    principal: float,
    annual_interest_rate: float,
    loan_term_years: int,
) -> float:
    """
    Calculate the fixed monthly payment for a fully amortizing fixed-rate mortgage.

    The calculation assumes equal monthly payments over the full loan term.

    Formula
    -------
                      r × (1 + r)^n
    M = P × -------------------------------
             (1 + r)^n − 1

    where

        M = Monthly mortgage payment
        P = Loan principal
        r = Monthly interest rate (decimal)
        n = Total number of monthly payments

    Parameters
    ----------
    principal : float
        Original loan amount.
    annual_interest_rate : float
        Annual interest rate expressed as a percentage
        (e.g., 6.5 for 6.5%).
    loan_term_years : int
        Loan duration in years.

    Returns
    -------
    float
        Fixed monthly mortgage payment.

    Notes
    -----
    Assumptions
    -----------
    - Fixed interest rate
    - Monthly compounding
    - Fully amortizing loan
    - Equal monthly payments
    - No taxes or insurance
    - No private mortgage insurance (PMI)
    - No additional principal payments

    Example
    -------
    >>> calculate_monthly_payment(
    ...     principal=300_000,
    ...     annual_interest_rate=6.5,
    ...     loan_term_years=30,
    ... )
    1896.20

    Raises
    ------
    ValueError
        If principal is less than or equal to zero.
        If interest rate is negative.
        If loan term is less than or equal to zero.
    """

    if principal <= 0:
        raise ValueError("Principal must be greater than zero.")

    if annual_interest_rate < 0:
        raise ValueError("Annual interest rate cannot be negative.")

    if loan_term_years <= 0:
        raise ValueError("Loan term must be greater than zero.")

    monthly_rate = (
        annual_interest_rate / PERCENT_TO_DECIMAL / MONTHS_PER_YEAR
    )

    number_of_payments = loan_term_years * MONTHS_PER_YEAR

    if annual_interest_rate == 0:
        return round(principal / number_of_payments, 2)

    payment = (
        principal
        * monthly_rate
        * (1 + monthly_rate) ** number_of_payments
        / (
            (1 + monthly_rate) ** number_of_payments - 1
        )
    )

    return payment

def main() -> None:
    principal = 300_000
    annual_interest_rate = 6.5
    loan_term_years = 30

    monthly_payment = calculate_monthly_payment(
        principal,
        annual_interest_rate,
        loan_term_years,
    )

    print("=" * 40)
    print("Mortgage Analytics Engine")
    print("=" * 40)
    print(f"Principal       : ${principal:,.2f}")
    print(f"Interest Rate   : {annual_interest_rate:.2f}%")
    print(f"Loan Term       : {loan_term_years} years")
    print(f"Monthly Payment : ${monthly_payment:,.2f}")

if __name__ == "__main__":
    main()
