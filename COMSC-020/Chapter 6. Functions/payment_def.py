# Huu Hung Nguyen
# 10/05/2021
# payment_def.py
# The program prompts user for principal, annual percent, and years.
# It then calculates and displays the monthly payment.

# Define get monthly payment function
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
    principal = int(input('Enter amount of loan: $'))
    annual_percent = float(input('Enter annual interest rate as a percent: '))
    years = int(input('Enter number of years for the loan: '))
    
    # Get monthly payment
    payment = get_monthly_payment(principal, annual_percent, years)
    
    # Display monthly payment
    print(f'Your monthly payment is ${payment:,.2f}')
    
# Call main function
main()