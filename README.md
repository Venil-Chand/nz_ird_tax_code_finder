# NZ IRD Tax Code Finder

A beginner Python program that helps New Zealand employees determine the
correct IRD tax code by answering a series of yes/no questions.

---

## Project Overview

When starting a new job in New Zealand, employees must complete an
**IR330 Tax code declaration** form to tell their employer how much tax
to deduct from their pay (PAYE). Choosing the wrong code can result in
paying too much or too little tax throughout the year.

This program walks the user through the same decision process as the
IR330 form's flowchart, asking simple yes/no questions and displaying
the recommended tax code at the end.

This project was built as a first-year Python learning exercise. It
demonstrates core programming concepts without using external libraries,
web APIs, or advanced Python features.

---

## Features

- Asks clear yes/no questions to guide the user through the decision tree
- Covers main income codes: `M`, `M SL`, `ME`, `ME SL`
- Covers secondary income codes: `SB`, `S`, `SH`, `ST`, `SA` (with or
  without the `SL` student loan suffix)
- Handles Work and Income benefit recipients
- Detects student loan obligations and adds the `SL` suffix automatically
- Validates user input — accepts `yes`, `YES`, `Yes`, `  yes  `, etc.
- Rejects invalid answers and asks the question again
- Directs non-NZ tax residents to the official IRD website
- Displays a mandatory disclaimer reminding users to verify their result

---

## Python Concepts Demonstrated

| Concept | Where used |
|---|---|
| Variables and strings | Storing answers and building the tax code |
| `input()` | Collecting user responses |
| String methods (`.strip()`, `.lower()`) | Input validation |
| `if` / `elif` / `else` | Tax code decision logic |
| `while` loop | Re-prompting for invalid input |
| Functions with return values | `get_yes_no()`, `secondary_income()`, `main()` |
| Calling one function from another | `main()` calls `secondary_income()` |
| f-strings | Formatting the output message |
| Docstrings | Documenting each function's purpose |
| `if __name__ == "__main__":` | Allowing the file to be imported for testing |
| `unittest` | Writing automated tests |
| `unittest.mock.patch` | Simulating user input in tests |

---

## Requirements

- Python 3.7 or later
- No external libraries required (uses only the Python standard library)

---

## Installation

1. Make sure Python 3.7+ is installed.  
   Check by opening a terminal and running: `python --version`

2. Download or clone the project:
   ```
   git clone https://github.com/YOUR-USERNAME/nz-ird-tax-code-finder.git
   cd nz-ird-tax-code-finder
   ```

No packages need to be installed.

---

## How to Run the Program

Open a terminal in the project folder and run:

```
python ird_tax_code_finder.py
```

### How to Run the Tests

From the project root folder:

```
python -m unittest discover tests/
```

Expected output:

```
....................
----------------------------------------------------------------------
Ran 22 tests in 0.XXXs

OK
```

---

## Example Input and Output

Below is an example session for a New Zealand tax resident with a main
job earning $35,000 per year, no Working for Families entitlement, and
an active student loan.

```
==============================================================
  New Zealand IRD Tax Code Finder
  Based on Inland Revenue IR330 (August 2026)
==============================================================

Enter your name: Sarah

Hi Sarah! Please answer 'yes' or 'no' to each question.

Q1: Do you receive a main benefit from Work and Income? no

Q2: Is this tax code for your main or highest source of income? yes

Q3: Are you a New Zealand tax resident? yes

Q4: Is your estimated annual income between $24,000 and $70,000? yes
Q5: Are you (or your partner) entitled to Working for Families Tax Credits? no

Q6: Do you have a New Zealand student loan? yes

==============================================================
  Hello Sarah!
  Based on your answers, your recommended tax code is:  ME SL
==============================================================

  IMPORTANT: This result is for educational guidance only.
  Always verify your tax code using the official IR330 form:
  https://www.ird.govt.nz/income-tax/income-tax-for-individuals/
  tax-codes-and-tax-rates-for-individuals/
```

---

## Limitations

This tool covers the most common tax-code scenarios but has the following
limitations. It should never be used as a substitute for official IRD advice.

1. **Non-NZ tax residents** — The tool cannot determine codes for
   non-residents. These cases involve additional complexity and are
   redirected to the IRD website.

2. **Not all tax codes are covered** — The program does not cover codes
   such as `CAE` (casual agricultural employees), `EDW` (election day
   workers), `WT` (withholding tax), tailored tax codes, or `ESCT`
   (employer superannuation contributions).

3. **Income thresholds may change** — The ME code income range
   ($24,000–$70,000) and secondary income brackets (SB through SA) are
   correct for the 2025–2026 tax year. These should be verified annually
   at the IRD website.

4. **Working for Families entitlement is complex** — The program asks a
   simple yes/no question. In practice, WFF entitlement depends on your
   family situation, income, and children's ages. Check with IRD if you
   are unsure.

5. **Input type only** — The program accepts only text input. It does not
   validate that income estimates are reasonable numbers.

6. **Does not cover all benefit scenarios** — Only asks whether you
   receive a "main benefit" from Work and Income. It does not determine
   whether a particular benefit qualifies as income-tested.

---

## Official IRD References

All tax-code rules were verified against the following official
Inland Revenue sources (October 2026):

- **IR330 Tax code declaration (August 2026)**  
  https://www.ird.govt.nz/forms-guides/number/forms-300-399/ir330-tax-code-declaration

- **About tax codes**  
  https://www.ird.govt.nz/income-tax/income-tax-for-individuals/tax-codes-and-tax-rates-for-individuals/about-tax-codes

- **Complete my tax code declaration**  
  https://www.ird.govt.nz/income-tax/income-tax-for-individuals/tax-codes-and-tax-rates-for-individuals/complete-my-tax-code-declaration

- **Independent Earner Tax Credit (IETC) — getting IETC via salary or wages**  
  https://www.ird.govt.nz/income-tax/income-tax-for-individuals/individual-tax-credits/independent-earner-tax-credit-ietc/getting-the-independent-earner-tax-credit-if-you-earn-salary-or-wages

- **International tax for individuals**  
  https://www.ird.govt.nz/international-tax

---

## Licensing

This project is released under the **MIT Licence**.

You are free to use, copy, modify, and share this code, provided you
include the original copyright notice. See the MIT Licence text at
https://opensource.org/licenses/MIT.

**Why MIT?** It is the most common licence for student and portfolio
projects. It is permissive (anyone can use your code), requires only
that your name is credited, and is recognised everywhere.

*Alternatives considered:*  
- **CC0** — Releases the code into the public domain with no restrictions
  at all. Appropriate if you want zero obligations for users.  
- **GNU GPL v3** — Requires that anyone who distributes your code must
  also make their source code open. Good for projects where you want
  contributions to stay open, but unnecessary for a student project.

---

## Educational Disclaimer

> This project was developed for educational purposes and is not
> affiliated with Inland Revenue New Zealand. Tax-code rules may change.
> Always verify your tax code using the official IRD website before
> using it for employment or tax purposes.

---

## Recommended GitHub Repository Name

**Repository name:** `nz-ird-tax-code-finder`  
**Short description:** `A beginner Python program that determines your NZ IRD tax code using yes/no questions.`

---

## Uploading to GitHub (VS Code on Windows — Step by Step)

### Prerequisites

Before you start, make sure you have:

1. **Python 3.7+** — https://www.python.org/downloads/
2. **Git for Windows** — https://git-scm.com/download/win  
   During installation, accept the default options.
3. **Visual Studio Code** — https://code.visualstudio.com/
4. **A GitHub account** — https://github.com (free)

---

### Step 1 — Open the project folder in VS Code

1. Open VS Code.
2. Go to **File → Open Folder**.
3. Select the `nz-tax-code-finder` folder.
4. Open the built-in terminal: **Terminal → New Terminal** (or press `` Ctrl+` ``).

---

### Step 2 — Set up your Git identity (one-time only)

In the terminal, type these two commands (replace with your details):

```
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

---

### Step 3 — Initialise the local repository

```
git init
```

---

### Step 4 — Stage all project files

```
git add .
```

Check what was staged:

```
git status
```

You should see `ird_tax_code_finder.py`, `README.md`, `.gitignore`, and
`tests/test_tax_code_finder.py` listed in green.

---

### Step 5 — Make the first commit

```
git commit -m "Initial commit: NZ IRD Tax Code Finder"
```

---

### Step 6 — Create the GitHub repository

1. Go to https://github.com/new
2. Fill in:
   - **Repository name:** `nz-ird-tax-code-finder`
   - **Description:** `A beginner Python program that determines your NZ IRD tax code using yes/no questions.`
   - **Visibility:** Public
3. **Important:** Leave "Add a README file", "Add .gitignore", and
   "Choose a licence" all **unticked** — you already have these files.
4. Click **Create repository**.

---

### Step 7 — Link your local repository to GitHub

Copy the repository URL from GitHub (it looks like
`https://github.com/YOUR-USERNAME/nz-ird-tax-code-finder.git`) and run:

```
git remote add origin https://github.com/YOUR-USERNAME/nz-ird-tax-code-finder.git
git branch -M main
```

---

### Step 8 — Push to GitHub

```
git push -u origin main
```

VS Code may open a browser window asking you to sign in to GitHub.
Complete the sign-in, then the push will finish automatically.

---

### Step 9 — Verify

Go to `https://github.com/YOUR-USERNAME/nz-ird-tax-code-finder` in your
browser. You should see all your files and the README displayed.

---

### VS Code Shortcut (optional)

After Step 3 (`git init`), you can use the **Source Control** panel
(the icon on the left sidebar that looks like a branch) to stage, commit,
and then click **Publish Branch** to create the GitHub repository and
push in one step — VS Code handles Steps 4–8 for you.
