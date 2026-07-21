"""
Amortization Schedule Generator

Generate a complete amortization schedule for a fixed-rate mortgage.

This module provides functionality for generating a month-by-month
amortization schedule for fixed-rate residential loans.

Author: Mukhtarbek Abdurazakov
"""

from typing import Final

from mortgage_calculator import calculate_monthly_payment

MONTHS_PER_YEAR: Final[int] = 12
PERCENT_TO_DECIMAL: Final[float] = 100.0


def generate_amortization_schedule(
    principal: float,
    annual_interest_rate: float,
    loan_term_years: int,
) -> list[dict]:
    """
    Generate a complete amortization schedule for a fixed-rate mortgage.

    The amortization schedule shows how each monthly payment is allocated
    between interest and principal over the life of the loan.

    Mathematical Background
    -----------------------
    For each payment period:

        Interest Payment = Remaining Balance × Monthly Interest Rate

        Principal Payment = Monthly Payment − Interest Payment

        Remaining Balance = Previous Balance − Principal Payment

    where

        Monthly Interest Rate = Annual Interest Rate / (100 × 12)

    These calculations are repeated until the loan balance reaches zero.

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
    list[dict]
        A list containing one dictionary for each payment period.

        Each dictionary contains:

        - payment_number
        - payment
        - principal
        - interest
        - balance

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

    Raises
    ------
    ValueError
        If principal is less than or equal to zero.
        If interest rate is negative.
        If loan term is less than or equal to zero.

    Example
    -------
    >>> schedule = generate_amortization_schedule(
    ...     principal=300_000,
    ...     annual_interest_rate=6.5,
    ...     loan_term_years=30,
    ... )

    >>> schedule[0]

    {
        "payment_number": 1,
        "payment": 1896.20,
        "principal": 271.20,
        "interest": 1625.00,
        "balance": 299728.80,
    }
    """

    if principal <= 0:
        raise ValueError("Principal must be greater than zero.")

    if annual_interest_rate < 0:
        raise ValueError("Annual interest rate cannot be negative.")

    if loan_term_years <= 0:
        raise ValueError("Loan term must be greater than zero.")

    # Calculate the fixed monthly mortgage payment.
    payment = calculate_monthly_payment(
        principal,
        annual_interest_rate,
        loan_term_years,
    )

    # Convert annual interest rate to a monthly decimal rate.
    monthly_rate = (
        annual_interest_rate
        / PERCENT_TO_DECIMAL
        / MONTHS_PER_YEAR
    )

    # Initialize the remaining loan balance.
    balance = principal

    # Store the complete amortization schedule.
    schedule = []

    # Total number of monthly payments.
    number_of_payments = loan_term_years * MONTHS_PER_YEAR

    # Compute payment details for each month until the loan is fully repaid.
    for payment_number in range(1, number_of_payments + 1):

        # Monthly interest accrued on the outstanding balance.
        interest_payment = balance * monthly_rate

        # Portion of the payment applied to principal.
        principal_payment = payment - interest_payment

        # Update the remaining loan balance.
        balance -= principal_payment

        # Prevent tiny negative balances caused by floating-point rounding.
        if balance < 0:
            balance = 0.0

        schedule.append(
            {
                "payment_number": payment_number,
                "payment": round(payment, 2),
                "principal": round(principal_payment, 2),
                "interest": round(interest_payment, 2),
                "balance": round(balance, 2),
            }
        )

    return schedule


if __name__ == "__main__":
    schedule = generate_amortization_schedule(
        principal=300_000,
        annual_interest_rate=6.5,
        loan_term_years=30,
    )

    print("First five payments:\n")

    for payment in schedule[:5]:
        print(payment)