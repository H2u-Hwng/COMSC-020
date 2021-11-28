# Huu Hung Nguyen
# 09/09/2021
# MPG.py
# The program prompts the user for the miles driven and gallons used.
# It then computes miles per gallon and prints the result.

# Prompt user for miles
miles = float(input('How many miles driven? '))

# Prompt user for gallons
gallons = float(input('How many gallons used? '))

# Compute miles per gallon
mpg = miles / gallons

# Print result
print('The car can travel {:.3f} miles per gallon.'.format(mpg))
