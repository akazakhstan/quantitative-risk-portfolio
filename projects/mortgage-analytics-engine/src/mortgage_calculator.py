"""
Mortgage Analytics Engine

Core mortgage calculation functions.

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
    Calculate the fixed monthly mortgage payment.

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
        Monthly mortgage payment.
    """
    monthly_rate = (
        annual_interest_rate / PERCENT_TO_DECIMAL / MONTHS_PER_YEAR
    )

    number_of_payments = loan_term_years * MONTHS_PER_YEAR

    payment = (
        principal
        * monthly_rate
        * (1 + monthly_rate) ** number_of_payments
        / (
            (1 + monthly_rate) ** number_of_payments
            - 1
        )
    )

    return payment