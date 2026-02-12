# payroll.py
# Payroll calculation logic (backend engine)

TAX_RATE = 0.20
OVERTIME_RATE = 1.5
OVERTIME_HOURS = 40


def calculate_gross_pay(hours, rate):
    if hours > OVERTIME_HOURS:
        overtime_hours = hours - OVERTIME_HOURS
        regular_pay = OVERTIME_HOURS * rate
        overtime_pay = overtime_hours * rate * OVERTIME_RATE
        gross = regular_pay + overtime_pay
    else:
        gross = hours * rate
    return gross


def calculate_taxes(gross):
    return gross * TAX_RATE


def calculate_net_pay(hours, rate):
    gross = calculate_gross_pay(hours, rate)
    taxes = calculate_taxes(gross)
    net = gross - taxes

    return gross, taxes, net
