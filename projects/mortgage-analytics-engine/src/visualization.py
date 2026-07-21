"""
Mortgage Visualization Module

Create charts for mortgage amortization analysis.

Author: Mukhtarbek Abdurazakov
"""

import matplotlib.pyplot as plt

from amortization import generate_amortization_schedule


def plot_remaining_balance(
    principal: float,
    annual_interest_rate: float,
    loan_term_years: int,
) -> None:
    """
    Plot the remaining mortgage balance over time.
    """

    schedule = generate_amortization_schedule(
        principal,
        annual_interest_rate,
        loan_term_years,
    )

    months = [payment["payment_number"] for payment in schedule]
    balances = [payment["balance"] for payment in schedule]

    plt.figure(figsize=(10, 6))
    plt.plot(months, balances)
    plt.title("Remaining Mortgage Balance")
    plt.xlabel("Payment Number")
    plt.ylabel("Remaining Balance ($)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def plot_payment_breakdown(
    principal: float,
    annual_interest_rate: float,
    loan_term_years: int,
) -> None:
    """
    Plot the principal and interest portions of each monthly payment.
    """

    schedule = generate_amortization_schedule(
        principal,
        annual_interest_rate,
        loan_term_years,
    )

    months = [payment["payment_number"] for payment in schedule]
    principal_paid = [payment["principal"] for payment in schedule]
    interest_paid = [payment["interest"] for payment in schedule]

    plt.figure(figsize=(10, 6))
    plt.plot(months, principal_paid, label="Principal")
    plt.plot(months, interest_paid, label="Interest")
    plt.title("Principal vs. Interest Over Time")
    plt.xlabel("Payment Number")
    plt.ylabel("Payment Amount ($)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    plot_remaining_balance(
        principal=300000,
        annual_interest_rate=6.5,
        loan_term_years=30,
    )

    plot_payment_breakdown(
        principal=300000,
        annual_interest_rate=6.5,
        loan_term_years=30,
    )