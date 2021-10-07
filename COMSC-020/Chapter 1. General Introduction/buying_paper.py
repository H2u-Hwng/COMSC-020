# Huu Hung Nguyen
# 09/07/2021
# buying_paper.py
# The program will prompt the user for the packages of paper and tax rate as a percent.
# The program calculates the total cost and displays the output. 

# Constant for cost paper
COST_PAPER = 2.5

# Prompt user for packages of paper 
packages_paper = int(input('Enter packages of paper: '))

# Prompt user for tax rate as a percent and calculate tax rate
tax_percent = float(input('Enter tax rate as a percent: '))
tax_rate = tax_percent / 100

# Calculate total cost
total_cost = COST_PAPER * packages_paper * (1 + tax_rate)

# Display total cost with label 
print(f'Total cost: ${total_cost:,.2f}')
