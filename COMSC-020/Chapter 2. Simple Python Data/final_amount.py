# Huu Hung Nguyen
# 09/08/2021
# final_amount.py
# The program will assigns the principal amount, the number of times the interest is compounded per year, and the interest rate. 
# The program will prompt the user for the number of years that the money will be compounded for. 
# The program calculates the final amount and print it after t years.

# Principal amount
P = 10000

# Number of times the interest is compounded per year
N = 12

# Interest rate
R = 0.08

# Prompt user for number of years
year = int(input('Compound for how many years? '))

# Calculate final amount
final = P * ((1 + R / N)**(N * year)) 

# Display final amount
print(f'The final amount after {year} years is ${final:.2f}.')
