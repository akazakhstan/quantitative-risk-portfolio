"""
Mortgage Export Module

Export mortgage analytics data to external file formats.

Author: Mukhtarbek Abdurazakov
"""

import pandas as pd

from dataframe import create_amortization_dataframe


def export_to_csv(
    dataframe: pd.DataFrame,
    filename: str,
) -> None:
    """
    Export a mortgage amortization schedule to a CSV file.

    Parameters
    ----------
    dataframe : pandas.DataFrame
        Mortgage amortization schedule.

    filename : str
        Name of the output CSV file.
    """

    dataframe.to_csv(filename, index=False)

    print(f"CSV file successfully exported to '{filename}'.")


if __name__ == "__main__":

    df = create_amortization_dataframe(
        principal=300000,
        annual_interest_rate=6.5,
        loan_term_years=30,
    )

    export_to_csv(df, "amortization_schedule.csv")

from pathlib import Path

output_dir = Path("../reports")
output_dir.mkdir(exist_ok=True)

filename = output_dir / "amortization_schedule.csv"

export_to_csv(df, filename)