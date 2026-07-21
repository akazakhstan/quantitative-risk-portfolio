    """
    Calculate the fixed monthly payment for a fully amortizing fixed-rate mortgage.

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
    Assumptions:
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
    1896.20 # Monthly mortgage payment

    Raises
    ------
    ValueError
        If principal is less than or equal to zero.
        If interest rate is negative.
        If loan term is less than or equal to zero.
    """