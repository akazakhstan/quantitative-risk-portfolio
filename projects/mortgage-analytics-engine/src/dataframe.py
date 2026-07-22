"""
Mortgage DataFrame Module

Convert amortization schedules into pandas DataFrames.

Author: Mukhtarbek Abdurazakov
"""

import pandas as pd

from amortization import generate_amortization_schedule


def create_amortization_dataframe(
    principal: float,
    annual_interest_rate: float,
    loan_term_years: int,
) -> pd.DataFrame:
    """
    Create a pandas DataFrame from an amortization schedule.

    Parameters
    ----------
    principal : float
        Original loan amount.

    annual_interest_rate : float
        Annual interest rate.

    loan_term_years : int
        Loan duration in years.

    Returns
    -------
    pandas.DataFrame
        Mortgage amortization schedule.
    """

    schedule = generate_amortization_schedule(
        principal,
        annual_interest_rate,
        loan_term_years,
    )

    return pd.DataFrame(schedule)

if __name__ == "__main__":

    df = create_amortization_dataframe(
        principal=300000,
        annual_interest_rate=6.5,
        loan_term_years=30,
    )

    print(df.head())

    print()

    print(df.tail())