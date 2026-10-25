"""
NZ IRD Tax Code Finder
======================
A beginner Python program that helps New Zealand employees determine their
correct IRD tax code by asking a series of yes/no questions.

Based on Inland Revenue's IR330 Tax code declaration form (August 2026).
  https://www.ird.govt.nz/forms-guides/number/forms-300-399/ir330-tax-code-declaration

DISCLAIMER: This project was developed for educational purposes and is not
affiliated with Inland Revenue New Zealand. Tax-code rules may change.
Always verify your tax code using the official IRD website before using it
for employment or tax purposes.
"""


# ---------------------------------------------------------------------------
# Input helper
# ---------------------------------------------------------------------------

def get_yes_no(question):
    """Ask a yes/no question and re-prompt until a valid answer is given.

    Accepts 'yes' and 'no' in any combination of upper/lower case, with or
    without leading or trailing spaces (e.g. 'YES', 'Yes', '  no  ').

    Args:
        question (str): The question to display to the user.

    Returns:
        str: Either 'yes' or 'no' (always lowercase).
    """
    while True:
        answer = input(question).strip().lower()
        if answer in ("yes", "no"):
            return answer
        print("  Please type 'yes' or 'no'.")


# ---------------------------------------------------------------------------
# Secondary income tax code
# ---------------------------------------------------------------------------

def secondary_income():
    """Determine the correct secondary income tax code.

    Secondary income codes (SB, S, SH, ST, or SA) depend on the employee's
    estimated TOTAL annual income from ALL jobs and income sources combined —
    not just the income from this particular job.

    Income brackets (2025-2026 tax year, confirmed IRD):
        SB  up to $15,600
        S   $15,601 – $53,500
        SH  $53,501 – $78,100
        ST  $78,101 – $180,000
        SA  over $180,000
    Adding 'SL' to any code above indicates a student loan obligation.

    Returns:
        str: The secondary tax code, e.g. 'S', 'SH SL'.
    """
    print()
    print("  -- Secondary Income Tax Code --")
    print("  The income ranges below refer to your estimated TOTAL annual")
    print("  income from ALL jobs and income sources combined.")
    print()

    # Work down through the income brackets; the first 'yes' answer wins.
    if get_yes_no("  Will your total annual income be $15,600 or less?          ") == "yes":
        base_code = "SB"
    elif get_yes_no("  Will your total annual income be between $15,601-$53,500?  ") == "yes":
        base_code = "S"
    elif get_yes_no("  Will your total annual income be between $53,501-$78,100?  ") == "yes":
        base_code = "SH"
    elif get_yes_no("  Will your total annual income be between $78,101-$180,000? ") == "yes":
        base_code = "ST"
    else:
        # None of the above brackets matched; income must be over $180,000.
        base_code = "SA"

    # A student loan adds the 'SL' suffix to any secondary tax code.
    print()
    if get_yes_no("  Do you have a New Zealand student loan? ") == "yes":
        return base_code + " SL"
    return base_code


# ---------------------------------------------------------------------------
# Main program
# ---------------------------------------------------------------------------

def main():
    """Run the NZ IRD Tax Code Finder.

    Asks the user a series of yes/no questions and returns the recommended
    NZ IRD tax code based on the IR330 decision guidelines.

    Returns:
        str or None: The recommended tax code (e.g. 'ME SL'), or None when
                     the program exits early because it cannot determine a
                     code (e.g. for non-NZ tax residents).
    """
    print()
    print("=" * 62)
    print("  New Zealand IRD Tax Code Finder")
    print("  Based on Inland Revenue IR330 (August 2026)")
    print("=" * 62)
    print()

    name = input("Enter your name: ").strip()
    print()
    print(f"Hi {name}! Please answer 'yes' or 'no' to each question.")

    # ------------------------------------------------------------------
    # Step 1: Work and Income benefit
    # ------------------------------------------------------------------
    print()
    receives_benefit = get_yes_no(
        "Q1: Do you receive a main benefit from Work and Income? "
    )

    if receives_benefit == "yes":
        # Step 2 (benefit path): Is this code for the benefit income itself?
        for_benefit_income = get_yes_no(
            "Q2: Is this tax code for the income-tested benefit? "
        )

        if for_benefit_income == "yes":
            # The benefit income uses code M (or M SL if you have a student loan).
            print()
            has_student_loan = get_yes_no(
                "Q3: Do you have a New Zealand student loan? "
            )
            tax_code = "M SL" if has_student_loan == "yes" else "M"

        else:
            # Any other employment income while on a benefit is treated as
            # secondary income, because the benefit counts as the main income.
            tax_code = secondary_income()

    else:
        # ------------------------------------------------------------------
        # Step 2 (non-benefit path): Main or secondary income?
        # ------------------------------------------------------------------
        print()
        is_main_income = get_yes_no(
            "Q2: Is this tax code for your main or highest source of income? "
        )

        if is_main_income == "no":
            # This is a secondary job or income source.
            tax_code = secondary_income()

        else:
            # --------------------------------------------------------------
            # Step 3: NZ tax resident?
            # --------------------------------------------------------------
            print()
            is_resident = get_yes_no(
                "Q3: Are you a New Zealand tax resident? "
            )

            if is_resident == "no":
                # Non-residents need different tax arrangements that this tool
                # cannot reliably determine. Direct the user to the IRD.
                print()
                print("  This tool cannot determine the tax code for")
                print("  non-NZ tax residents.")
                print()
                print("  Please visit the IRD website or call 0800 775 247:")
                print("  https://www.ird.govt.nz/international-tax")
                print()
                return None

            # --------------------------------------------------------------
            # Step 4: Is income between $24,000 and $70,000?
            # This range determines eligibility for the ME code, which allows
            # your employer to apply the Independent Earner Tax Credit (IETC).
            # Source: https://www.ird.govt.nz/income-tax/income-tax-for-individuals/
            #         individual-tax-credits/independent-earner-tax-credit-ietc
            # --------------------------------------------------------------
            print()
            is_mid_range_income = get_yes_no(
                "Q4: Is your estimated annual income between $24,000 and $70,000? "
            )

            if is_mid_range_income == "yes":
                # Step 5: Working for Families Tax Credits?
                # Receiving WFF disqualifies you from the ME code (IRD confirmed).
                is_wff_eligible = get_yes_no(
                    "Q5: Are you (or your partner) entitled to Working for "
                    "Families Tax Credits? "
                )

                # Step 6: Student loan?
                print()
                has_student_loan = get_yes_no(
                    "Q6: Do you have a New Zealand student loan? "
                )

                if is_wff_eligible == "no":
                    # Eligible for ME (Independent Earner Tax Credit applies).
                    tax_code = "ME SL" if has_student_loan == "yes" else "ME"
                else:
                    # WFF recipients are not eligible for ME; use standard M.
                    tax_code = "M SL" if has_student_loan == "yes" else "M"

            else:
                # Income is outside $24,000–$70,000; not eligible for ME.
                # Use the standard M code.
                print()
                has_student_loan = get_yes_no(
                    "Q5: Do you have a New Zealand student loan? "
                )
                tax_code = "M SL" if has_student_loan == "yes" else "M"

    # ------------------------------------------------------------------
    # Display result
    # ------------------------------------------------------------------
    print()
    print("=" * 62)
    print(f"  Hello {name}!")
    print(f"  Based on your answers, your recommended tax code is:  {tax_code}")
    print("=" * 62)
    print()
    print("  IMPORTANT: This result is for educational guidance only.")
    print("  Always verify your tax code using the official IR330 form:")
    print("  https://www.ird.govt.nz/income-tax/income-tax-for-individuals/")
    print("  tax-codes-and-tax-rates-for-individuals/")
    print()

    return tax_code


if __name__ == "__main__":
    main()
