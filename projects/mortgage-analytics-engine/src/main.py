from calculators.payment import calculate_monthly_payment
from calculators.ltv import calculate_ltv


def main() -> None:
    principal = 300_000
    annual_interest_rate = 6.5
    loan_term_years = 30
    property_value = 375_000

    monthly_payment = calculate_monthly_payment(
        principal,
        annual_interest_rate,
        loan_term_years,
    )

    ltv = calculate_ltv(principal, property_value)

    print("=" * 45)
    print("Mortgage Analytics Engine")
    print("=" * 45)
    print(f"Loan Amount      : ${principal:,.2f}")
    print(f"Property Value   : ${property_value:,.2f}")
    print(f"Interest Rate    : {annual_interest_rate:.2f}%")
    print(f"Loan Term        : {loan_term_years} years")
    print(f"Monthly Payment  : ${monthly_payment:,.2f}")
    print(f"LTV Ratio        : {ltv:.2f}%")


if __name__ == "__main__":
    main()