"""
Tests for ird_tax_code_finder.py
=================================
Run all tests from the project root folder with:

    python -m unittest discover tests/

Or run this file directly:

    python tests/test_tax_code_finder.py

How it works
------------
These tests use unittest.mock.patch to replace the built-in input() function
with a fake version that returns answers from a list automatically, one per
call.  This lets us test every branch of the program without typing anything.

    patch('builtins.input', side_effect=['yes', 'no', ...])

Each string in the list is returned the next time input() is called, in order.
"""

import io
import os
import sys
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

# Add the project root to the Python path so we can import the module.
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ird_tax_code_finder import main, secondary_income


# ---------------------------------------------------------------------------
# Shared helper
# ---------------------------------------------------------------------------

def run_with_inputs(func, answers):
    """Call func() with mocked input() values and return its result.

    Args:
        func:    The function to call (e.g. main or secondary_income).
        answers: A list of strings; each is returned for one input() call.

    Returns:
        Whatever func() returns (a tax code string, or None).
    """
    with patch("builtins.input", side_effect=answers):
        # Capture any print() output so it does not clutter the test results.
        captured = io.StringIO()
        with redirect_stdout(captured):
            result = func()
    return result


# ---------------------------------------------------------------------------
# Tests: secondary_income()
# ---------------------------------------------------------------------------

class TestSecondaryIncome(unittest.TestCase):
    """Tests for the secondary_income() helper function.

    The secondary income function asks up to four income-bracket questions
    (answered from lowest to highest) then one student loan question.
    The first 'yes' to a bracket question sets the base code; all remaining
    bracket questions are skipped.
    """

    def test_sb_no_student_loan(self):
        """Income $15,600 or less, no student loan → SB"""
        # 'yes' to bracket 1, 'no' to student loan
        result = run_with_inputs(secondary_income, ["yes", "no"])
        self.assertEqual(result, "SB")

    def test_sb_with_student_loan(self):
        """Income $15,600 or less, with student loan → SB SL"""
        result = run_with_inputs(secondary_income, ["yes", "yes"])
        self.assertEqual(result, "SB SL")

    def test_s_no_student_loan(self):
        """Income $15,601–$53,500, no student loan → S"""
        # 'no' to bracket 1, 'yes' to bracket 2, 'no' to student loan
        result = run_with_inputs(secondary_income, ["no", "yes", "no"])
        self.assertEqual(result, "S")

    def test_s_with_student_loan(self):
        """Income $15,601–$53,500, with student loan → S SL"""
        result = run_with_inputs(secondary_income, ["no", "yes", "yes"])
        self.assertEqual(result, "S SL")

    def test_sh_no_student_loan(self):
        """Income $53,501–$78,100, no student loan → SH"""
        result = run_with_inputs(secondary_income, ["no", "no", "yes", "no"])
        self.assertEqual(result, "SH")

    def test_sh_with_student_loan(self):
        """Income $53,501–$78,100, with student loan → SH SL"""
        result = run_with_inputs(secondary_income, ["no", "no", "yes", "yes"])
        self.assertEqual(result, "SH SL")

    def test_st_no_student_loan(self):
        """Income $78,101–$180,000, no student loan → ST"""
        result = run_with_inputs(secondary_income, ["no", "no", "no", "yes", "no"])
        self.assertEqual(result, "ST")

    def test_st_with_student_loan(self):
        """Income $78,101–$180,000, with student loan → ST SL"""
        result = run_with_inputs(secondary_income, ["no", "no", "no", "yes", "yes"])
        self.assertEqual(result, "ST SL")

    def test_sa_no_student_loan(self):
        """Income over $180,000 (no bracket matched), no student loan → SA"""
        # 'no' to all four bracket questions causes the code to fall through to SA.
        result = run_with_inputs(secondary_income, ["no", "no", "no", "no", "no"])
        self.assertEqual(result, "SA")

    def test_sa_with_student_loan(self):
        """Income over $180,000, with student loan → SA SL"""
        result = run_with_inputs(secondary_income, ["no", "no", "no", "no", "yes"])
        self.assertEqual(result, "SA SL")


# ---------------------------------------------------------------------------
# Tests: main() — main income paths
# ---------------------------------------------------------------------------

class TestMainIncome(unittest.TestCase):
    """Tests for paths through main() where this is the main income source.

    Input order for these tests (no benefit, main income, NZ resident):
        name, Q1=no, Q2=yes, Q3=yes, Q4=?, Q5=?, [Q6=?]
    """

    def test_me_no_loan(self):
        """$24K–$70K income, not WFF eligible, no loan → ME"""
        # Q4=yes (mid-range), Q5=no (no WFF), Q6=no (no loan)
        result = run_with_inputs(main, ["Alex", "no", "yes", "yes", "yes", "no", "no"])
        self.assertEqual(result, "ME")

    def test_me_with_loan(self):
        """$24K–$70K income, not WFF eligible, has loan → ME SL"""
        result = run_with_inputs(main, ["Alex", "no", "yes", "yes", "yes", "no", "yes"])
        self.assertEqual(result, "ME SL")

    def test_m_wff_no_loan(self):
        """$24K–$70K income, WFF eligible, no loan → M (WFF blocks ME)"""
        # Q5=yes (WFF eligible), Q6=no (no loan)
        result = run_with_inputs(main, ["Alex", "no", "yes", "yes", "yes", "yes", "no"])
        self.assertEqual(result, "M")

    def test_m_wff_with_loan(self):
        """$24K–$70K income, WFF eligible, has loan → M SL"""
        result = run_with_inputs(main, ["Alex", "no", "yes", "yes", "yes", "yes", "yes"])
        self.assertEqual(result, "M SL")

    def test_m_income_outside_range_no_loan(self):
        """Income NOT $24K–$70K, no loan → M (ME not applicable)"""
        # Q4=no (outside range), Q5=no (no loan)
        result = run_with_inputs(main, ["Alex", "no", "yes", "yes", "no", "no"])
        self.assertEqual(result, "M")

    def test_m_income_outside_range_with_loan(self):
        """Income NOT $24K–$70K, has loan → M SL"""
        result = run_with_inputs(main, ["Alex", "no", "yes", "yes", "no", "yes"])
        self.assertEqual(result, "M SL")

    def test_non_resident_returns_none(self):
        """Non-NZ tax resident → tool cannot determine code, returns None"""
        # Q3=no (non-resident) → early return
        result = run_with_inputs(main, ["Alex", "no", "yes", "no"])
        self.assertIsNone(result)


# ---------------------------------------------------------------------------
# Tests: main() — Work and Income benefit paths
# ---------------------------------------------------------------------------

class TestBenefitScenarios(unittest.TestCase):
    """Tests for paths where the user receives a Work and Income benefit."""

    def test_benefit_income_no_loan(self):
        """Code for benefit income, no student loan → M"""
        # Q1=yes (benefit), Q2=yes (for benefit), Q3=no (no loan)
        result = run_with_inputs(main, ["Alex", "yes", "yes", "no"])
        self.assertEqual(result, "M")

    def test_benefit_income_with_loan(self):
        """Code for benefit income, has student loan → M SL"""
        result = run_with_inputs(main, ["Alex", "yes", "yes", "yes"])
        self.assertEqual(result, "M SL")

    def test_benefit_other_income_secondary_no_loan(self):
        """Code for OTHER income while on benefit → secondary code SB"""
        # Q2=no (not for benefit income) → secondary_income()
        # secondary: 'yes' to ≤$15,600 → SB, 'no' to student loan
        result = run_with_inputs(main, ["Alex", "yes", "no", "yes", "no"])
        self.assertEqual(result, "SB")

    def test_benefit_other_income_secondary_with_loan(self):
        """Code for OTHER income while on benefit, has loan → SB SL"""
        result = run_with_inputs(main, ["Alex", "yes", "no", "yes", "yes"])
        self.assertEqual(result, "SB SL")


# ---------------------------------------------------------------------------
# Tests: main() — secondary income via non-benefit path
# ---------------------------------------------------------------------------

class TestSecondaryIncomeViaMain(unittest.TestCase):
    """Tests for reaching secondary_income() when NOT a benefit recipient."""

    def test_secondary_code_s(self):
        """Not main income, income $15,601–$53,500, no loan → S"""
        # Q1=no (no benefit), Q2=no (not main income) → secondary_income()
        # secondary: 'no' to ≤$15,600, 'yes' to $15,601-$53,500, 'no' to loan
        result = run_with_inputs(main, ["Alex", "no", "no", "no", "yes", "no"])
        self.assertEqual(result, "S")

    def test_secondary_code_st_with_loan(self):
        """Not main income, income $78,101–$180,000, has loan → ST SL"""
        # secondary: 'no','no','no','yes' to $78,101-$180,000 bracket, 'yes' to loan
        result = run_with_inputs(main, ["Alex", "no", "no", "no", "no", "no", "yes", "yes"])
        self.assertEqual(result, "ST SL")


# ---------------------------------------------------------------------------
# Tests: input validation
# ---------------------------------------------------------------------------

class TestInputValidation(unittest.TestCase):
    """Tests that get_yes_no() handles upper/lower case and extra spaces."""

    def test_uppercase_yes_accepted(self):
        """'YES' should be treated as 'yes'."""
        # Q1='YES' (benefit), Q2='YES' (for benefit), Q3='no' (no loan) → M
        result = run_with_inputs(main, ["Alex", "YES", "YES", "no"])
        self.assertEqual(result, "M")

    def test_mixed_case_yes_accepted(self):
        """'Yes' should be treated as 'yes'."""
        result = run_with_inputs(main, ["Alex", "Yes", "Yes", "no"])
        self.assertEqual(result, "M")

    def test_uppercase_no_accepted(self):
        """'NO' should be treated as 'no'."""
        # Q1='NO' (no benefit), Q2='NO' (not main → secondary), SB, no loan
        result = run_with_inputs(main, ["Alex", "NO", "NO", "yes", "no"])
        self.assertEqual(result, "SB")

    def test_spaces_stripped(self):
        """Answers with leading/trailing spaces should be accepted."""
        # '  yes  ' and '  no  ' should all work correctly.
        result = run_with_inputs(main, ["Alex", "  yes  ", "  yes  ", "  no  "])
        self.assertEqual(result, "M")

    def test_invalid_answer_then_valid(self):
        """An invalid answer ('maybe') should be rejected; next valid answer accepted."""
        # Q1: 'maybe' → rejected; 'yes' → benefit accepted.
        # Q2: 'yes' (for benefit), Q3: 'no' (no loan) → M
        result = run_with_inputs(main, ["Alex", "maybe", "yes", "yes", "no"])
        self.assertEqual(result, "M")


if __name__ == "__main__":
    unittest.main(verbosity=2)
