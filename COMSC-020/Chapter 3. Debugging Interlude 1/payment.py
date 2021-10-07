# Huu Hung Nguyen
# 09/19/2021
# payment.py
# The program prompts the user for the amount of the loan,
# the annual percentage rate, and the number of years of the loan.
# It then calculates the monthly payment and prints the result.

# Prompt user for principal
principal = float(input('Enter amount of loan: $'))

# Prompt user for annual interest rate as a percent and calculate annual rate
annual_percent = float(input('Enter annual interest rate as a percent: '))
annual_rate = annual_percent / 100

# Prompt user for number of years for the loan
years = int(input('Enter number of years for the loan: '))

# Calculate monthly interest rate, months of the loan, and subformula
monthly_rate = annual_rate / 12
months = years * 12
subformula = (1 + monthly_rate)**months

# Calculate monthly payment on the loan
payment = principal * monthly_rate * subformula / (subformula - 1)

# Print result
print(f'Your monthly payment is ${payment:,.2f}')
