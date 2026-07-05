# 🏢 Corporate Payroll & Bonus Calculator

A simple, interactive Python command-line application built to process employee payrolls. The application calculates performance-based bonuses, applies progressive tax rates based on gross income, and generates a clean, readable payroll statement.

## 🚀 Features

*   **Dynamic Bonus Allocation:** Automatically calculates employee bonuses based on a 1-5 performance rating scale.
*   **Progressive Tax Calculation:** Deducts taxes dynamically depending on the employee's gross income bracket.
*   **Input Validation:** Keeps data clean by rejecting negative salaries or out-of-bounds performance ratings.
*   **Formatted Outputs:** Generates a neat, professional terminal-based financial receipt for the employee.

## 📊 Business Logic Breakdown

### Bonus Rules
*   **Rating 5:** 20% bonus of the base salary.
*   **Rating 3 or 4:** 10% bonus of the base salary.
*   **Rating 1 or 2:** 0% bonus (Flags a "Needs Improvement" note).

### Tax Brackets
*   **Gross Salary > 7,000 EGP:** 15% tax rate.
*   **Gross Salary between 3,000 and 7,000 EGP:** 10% tax rate.
*   **Gross Salary < 3,000 EGP:** 0% tax rate (Flags a "Tax Exempt" note).

## 🛠️ How to Run

1. Make sure you have **Python 3.x** installed.
2. Clone this repository or download the source script.
3. Run the script using your terminal:
   ```bash
   python payroll_app.py
