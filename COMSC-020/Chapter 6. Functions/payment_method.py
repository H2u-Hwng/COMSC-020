# Huu Hung Nguyen
# 10/12/2021
# payment_method.py
# The program prompts user for principal, annual percent, and years.
# It then calculates and displays the monthly payment.

# Calculate monthly rate, months, subformula, and payment
# Return payment
def get_monthly_payment(principal, annual_percent, years):
    
    # Calculate monthly rate, months, and subformula
    monthly_percent = annual_percent / 12
    monthly_rate = monthly_percent / 100
    months = years * 12
    subformula = (1 + monthly_rate)**months
    
    # Calculate monthly payment
    payment = principal * monthly_rate * subformula / (subformula - 1)
    
    return payment


# Define main function
def main():
    
    # Prompt user for principal, annual percent, and years
    principal = float(input('Enter amount of loan: $'))
    annual_percent = float(input('Enter annual interest rate as a percent: '))
    years = int(input('Enter number of years for the loan: '))
    
    # Obtain monthly payment
    payment = get_monthly_payment(principal, annual_percent, years)
    
    # Display monthly payment
    print(f'Your monthly payment is ${payment:,.2f}')
    
    # Obtain payment for double principal
    larger_payment = get_monthly_payment(2 * principal, annual_percent, years)
    
    # Display payment for double principal
    print(f'Your monthly payment when you borrow ${2 * principal:,.2f} \
is ${larger_payment:,.2f}')
    
# Call main function
main()
