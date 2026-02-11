# Payroll Program Using Functions

# ---------------------------------
# Get employee hourly pay rate
# ---------------------------------

def get_pay_rate():
    rate = float(input("Enter employee hourly pay rate: $"))
    return rate

# ---------------------------------
# Get number of hours worked
# ---------------------------------

def get_hours_worked():
    hours = float(input("Enter number of hours worked: "))
    return hours

# ---------------------------------
# Calculate overtime pay
# ---------------------------------

def calculate_overtime_pay(rate, Hours):
    if Hours > 40:
        overtime_hours = Hours - 40
        overtime_pay = overtime_hours * 1.5
    else:
        overtime_pay = 0
    return overtime_pay
    
# ---------------------------------
# Calculate gross pay
# ---------------------------------

def calculate_gross_pay(rate, hours):
    if hours > 40:
        regular_pay = 40 * rate
    else:
        regular_pay = hours * rate
        
    overtime_pay = calculate_overtime_pay(rate, hours)
    gross = regular_pay + overtime_pay
    return gross

# ------------------------------------------
# Calculate withholdings (taxes/benefits)
# ------------------------------------------

def calculate_withholdings(gross):
    withholding = gross * 0.20      # 20% Deductions
    return withholding


# ---------------------------------
# Calculate net pay
# ---------------------------------

def calculate_net_pay(gross, withholding):
    net = gross - withholding
    return net 


# ---------------------------------
# Print paycheck
# ---------------------------------

def print_paycheck(rate, hours, gross, withholding, net):
    print("\n-------- PAYCHECK --------")
    print(f"Hourly Rate: ${rate:.2f}")
    print(f"Hours Worked: {hours:.2f}")
    print(f"Gross Pay: ${gross:.2f}")
    print(f"Deductions: ${withholding:.2f}")
    print(f"Net Pay: ${net:.2f}")
    print("-------------------------")
    
    
# ---------------------------------
# Main program
# ---------------------------------

def main():
    
    rate = get_pay_rate()
    hours = get_hours_worked()
    
    gross = calculate_gross_pay(rate, hours)
    withholding = calculate_withholdings(gross)
    net = calculate_net_pay(gross, withholding)
    
    print_paycheck(rate, hours, gross, withholding, net)
    
    
# Start Program
if __name__ == "__main__":
    main()
    
    