# NZ IRD Tax Code Finder

A beginner-friendly Python command-line project that demonstrates how a decision tree can be implemented with user input, conditional statements, and functions. It asks a series of yes/no questions and suggests a New Zealand employment tax code for certain common situations.

> **Educational project only.** This tool is not an official Inland Revenue service and should not be relied on to select a tax code for employment. Tax rules and individual circumstances vary. Always check the current [IRD IR330 Tax Code Declaration](https://www.ird.govt.nz/forms-guides/number/forms-300-399/ir330-tax-code-declaration) or contact Inland Revenue.

## Project overview

In New Zealand, employees use the IR330 tax-code declaration when providing tax-code information to an employer. This project was created as a first-year Python learning exercise inspired by the public IR330 decision flowchart. It demonstrates programming fundamentals rather than providing comprehensive tax advice.

## Features

- Interactive command-line questions with `yes` or `no` answers.
- Input validation that accepts different capitalisations and removes surrounding spaces.
- Conditional branches for selected main-income and secondary-income situations.
- Demonstrates tax-code labels such as `M`, `ME`, `SB`, `S`, `SH`, `ST`, `SA`, and some `SL` variants.
- Redirects users in certain unsupported situations to Inland Revenue.
- Displays an educational disclaimer with the result.

## Python concepts demonstrated

| Concept | How it is used |
| --- | --- |
| Variables and strings | Store responses and tax-code labels |
| `input()` and `print()` | Communicate with the user |
| `.strip()` and `.lower()` | Normalise text input |
| `if`, `elif`, and `else` | Follow a decision tree |
| `while` loop | Request another answer when input is invalid |
| Functions and `return` | Organise and reuse program logic |
| f-strings | Format messages |
| Docstrings | Document functions |
| `if __name__ == "__main__":` | Run the program when executed directly |

## Requirements

- Python 3.7 or newer.
- No third-party Python packages.

## How to run

1. Download or clone this repository.
2. Open a terminal in the folder containing `ird_tax_code_finder.py`.
3. Run:

   ```bash
   python ird_tax_code_finder.py
   ```

4. Answer the prompts by typing `yes` or `no`.

On systems that use `python3` instead of `python`, run `python3 ird_tax_code_finder.py`.

## Example interaction

```text
New Zealand IRD Tax Code Finder
Enter your name: Sarah
Hi Sarah! Please answer 'yes' or 'no' to each question.

Q1: Do you receive a main benefit from Work and Income? no
Q2: Is this tax code for your main or highest source of income? yes
Q3: Are you a New Zealand tax resident? yes
Q4: Is your estimated annual income between $24,000 and $70,000? yes
Q5: Are you (or your partner) entitled to Working for Families Tax Credits? no
Q6: Do you have a New Zealand student loan? yes

Hello Sarah!
Based on your answers, your recommended tax code is: ME SL
```

*This example illustrates a possible program path, not independently verified tax advice.*

## Limitations

- The program does **not** cover every code, employment arrangement, or personal circumstance. For example, it does not calculate codes for casual agricultural employees, election-day workers, or tailored arrangements.
- It uses simplified yes/no questions rather than collecting and validating income amounts.
- Eligibility for credits such as the Independent Earner Tax Credit can involve conditions not fully represented in the code.
- It does not establish a person's tax residency or student-loan repayment obligations.
- Some combinations of answers can lead to an oversimplified or incorrect code. The source code should be reviewed against the latest IR330 flowchart before relying on any result.
- Tax rates, thresholds, and guidance can change. The example values in this repository may become outdated.

## Official sources and attribution

The educational decision-tree concept and tax-code terminology are based on publicly available information from **Inland Revenue New Zealand**:

- [IR330 — Tax Code Declaration](https://www.ird.govt.nz/forms-guides/number/forms-300-399/ir330-tax-code-declaration)
- [About tax codes](https://www.ird.govt.nz/income-tax/income-tax-for-individuals/tax-codes-and-tax-rates-for-individuals/about-tax-codes)
- [Independent Earner Tax Credit](https://www.ird.govt.nz/income-tax/income-tax-for-individuals/individual-tax-credits/independent-earner-tax-credit-ietc)

Inland Revenue is credited as the source of the referenced tax information. This independent educational program is **not affiliated with, approved by, or endorsed by Inland Revenue**. The links above should be used to verify current rules.

## Disclaimer

This software is provided for programming education and demonstration only. It is not financial, legal, or tax advice. Always confirm an appropriate tax code through official Inland Revenue resources or a qualified adviser before submitting an IR330 declaration.
