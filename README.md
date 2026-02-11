# Payroll Program (Python)

## Description

This project is a modular payroll application written in Python.
The program calculates an employee’s paycheck based on hourly pay rate and hours worked. It separates tasks into multiple user-defined functions to demonstrate top-down design and code reusability.

The program will:

* Collect employee pay information
* Calculate overtime pay
* Compute gross pay
* Deduct taxes and benefits
* Calculate net pay
* Display a formatted paycheck

---

## Concepts Demonstrated

This project applies Chapter 5 concepts from *Starting Out With Python*:

* User-defined functions
* Function calls
* Parameters and arguments
* Return values
* Modular programming
* Top-down design

---

## Payroll Rules Used

* Regular hours: up to 40 hours
* Overtime: hours over 40
* Overtime pay rate: 1.5 × hourly rate
* Withholding deductions: 20% of gross pay

---

## Program Functions

The program is divided into the following functions:

| Function                           | Purpose                       |
| ---------------------------------- | ----------------------------- |
| `get_pay_rate()`                   | Gets employee hourly pay rate |
| `get_hours_worked()`               | Gets number of hours worked   |
| `calc_overtime_pay(rate, hours)`   | Calculates overtime earnings  |
| `calc_gross_pay(rate, hours)`      | Calculates total gross pay    |
| `calc_withholdings(gross)`         | Calculates deductions         |
| `calc_net_pay(gross, withholding)` | Calculates take-home pay      |
| `print_paycheck(...)`              | Displays paycheck information |

---

## How to Run the Program

1. Open Terminal
2. Navigate to the project folder:

```
cd path_to_your_folder
```

3. Run the program:

```
python3 payroll.py
```

---

## Example Output

```
Enter employee hourly pay rate: $20
Enter number of hours worked: 45

-------- PAYCHECK --------
Hourly Rate: $20.00
Hours Worked: 45.00
Gross Pay: $950.00
Deductions: $190.00
Net Pay: $760.00
--------------------------
```

---

## Author

Corey Shamburger
CIAT – Python Programming Course

---

## Notes

This program is for educational purposes and uses simplified payroll rules. Real payroll systems include tax brackets, insurance plans, retirement contributions, and government regulations.
