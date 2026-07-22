"""
Mortgage Analytics

Financial summary metrics for fixed-rate residential mortgages.

This module computes high-level mortgage statistics based on an
amortization schedule.

Author: Mukhtarbek Abdurazakov
"""

from calculators.amortization import generate_amortization_schedule
from calculators.payment import calculate_monthly_payment

def generate_loan_summary(
    principal: float,
    annual_interest_rate: float,
    loan_term_years: int,
) -> dict:
    """
    Generate summary statistics for a fixed-rate mortgage.

    Parameters
    ----------
    principal : float
        Original loan amount.

    annual_interest_rate : float
        Annual interest rate expressed as a percentage.

    loan_term_years : int
        Loan duration in years.

    Returns
    -------
    dict
        Dictionary containing key mortgage statistics.
    """

    payment = calculate_monthly_payment(
        principal,
        annual_interest_rate,
        loan_term_years,
    )

    schedule = generate_amortization_schedule(
        principal,
        annual_interest_rate,
        loan_term_years,
    )

    total_interest = sum(
        payment["interest"]
        for payment in schedule
    )

    total_principal = sum(
        payment["principal"]
        for payment in schedule
    )

    total_paid = total_interest + total_principal

    return {
        "loan_amount": round(principal, 2),
        "interest_rate": annual_interest_rate,
        "loan_term_years": loan_term_years,
        "monthly_payment": round(payment, 2),
        "number_of_payments": len(schedule),
        "total_principal_paid": round(total_principal, 2),
        "total_interest_paid": round(total_interest, 2),
        "total_amount_paid": round(total_paid, 2),
    }


if __name__ == "__main__":

    summary = generate_loan_summary(
        principal=300_000,
        annual_interest_rate=6.5,
        loan_term_years=30,
    )

    print()

    for key, value in summary.items():
        print(f"{key:25}: {value}")