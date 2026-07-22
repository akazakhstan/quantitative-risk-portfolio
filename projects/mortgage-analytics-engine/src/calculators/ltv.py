"""
Loan-to-Value (LTV) Calculator
"""

from typing import Final

PERCENT: Final[float] = 100.0


def calculate_ltv(loan_amount: float, property_value: float) -> float:
    """
    Calculate Loan-to-Value (LTV) ratio.

    Parameters
    ----------
    loan_amount : float
        Outstanding mortgage amount.
    property_value : float
        Appraised property value.

    Returns
    -------
    float
        LTV ratio as a percentage.

    Raises
    ------
    ValueError
        If property value is zero or negative.
    """

    if property_value <= 0:
        raise ValueError("Property value must be greater than zero.")

    return (loan_amount / property_value) * PERCENT

if __name__ == "__main__":
    loan = 320_000
    value = 400_000

    ltv = calculate_ltv(loan, value)

    print(f"Loan Amount : ${loan:,.0f}")
    print(f"Home Value  : ${value:,.0f}")
    print(f"LTV Ratio   : {ltv:.2f}%")

def ltv_risk_category(ltv: float) -> str:
    """
    Classify LTV according to common mortgage lending thresholds.
    """

    if ltv <= 60:
        return "Excellent"

    if ltv <= 80:
        return "Low Risk"

    if ltv <= 90:
        return "Moderate Risk"

    if ltv <= 97:
        return "High Risk"

    return "Very High Risk"
if __name__ == "__main__":
    loan = 320_000
    value = 400_000

    ltv = calculate_ltv(loan, value)

    print(f"Loan Amount : ${loan:,.0f}")
    print(f"Home Value  : ${value:,.0f}")
    print(f"LTV Ratio   : {ltv:.2f}%")
    print(f"Risk Category: {ltv_risk_category(ltv)}")