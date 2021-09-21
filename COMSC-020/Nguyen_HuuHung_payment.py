# Huu Hung Nguyen
# 09/19/2021
# Nguyen_HuuHung_payment.py
# The program prompts the user for the amount of the loan,
# the annual percentage rate, and the number of years of the loan.
# It then calculates the monthly payment and prints the result.


# Prompt user for principal
principal = float(input('Enter amount of loan: $'))

# Prompt user for annual interest rate as a percent 
annual_rate = float(input('Enter annual interest rate as a percent: '))

# Prompt user for number of years for the loan
years = int(input('Enter number of years for the loan: '))

# Calculate monthly interest rate
monthly_rate = (annual_rate / 12) / 100 

# Calculate number of months of the loan
months = years * 12

# Common subformula
subformula = (1 + monthly_rate)**months

# Calculate monthly payment on the loan
payment = principal * monthly_rate * subformula / (subformula - 1)

# Print result
print('Your monthly payment is ${:.2f}'. format(payment))