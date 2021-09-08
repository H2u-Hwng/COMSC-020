# Huu Hung Nguyen
# 09/07/2021
# Buying_paper.py
# The program will prompt the user for the packages of paper and tax rate as a percent.
# The program calculates the total cost and displays the output. 


# Constant
COST_PAPER = 2.5

# Prompt user for packages of paper 
packages_paper = int(input('Enter packages of paper: '))

# Prompt user for tax rate as a percent
tax_rate = float(input('Enter tax rate: '))

# Calculate total cost
total_cost = COST_PAPER * packages_paper * (1 + tax_rate / 100)

# Display total cost with label 
print('Total cost: $', format(total_cost, '.2f'), '.', sep = '')
