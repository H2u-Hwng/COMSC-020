# Huu Hung Nguyen
# 09/08/2021
# final_amount.py
# Constants for principal, times the interest per year, and interest rate. 
# The program prompts user for years that the money will be compounded for. 
# It then calculates the final amount and print it after t years.

# Constants for principal, times the interest per year, and interest rate
PRINCIPAL = 10000
TIMES = 12
INTEREST_RATE = 0.08

# Prompt user for number of years
years = int(input('Compound for how many years? '))

# Calculate final amount
final_amount = PRINCIPAL * ((1 + INTEREST_RATE / TIMES)**(TIMES * years)) 

# Display final amount
print(f'The final amount after {years} years is ${final_amount:,.2f}.')
