# Huu Hung Nguyen
# 09/14/2021
# prices.py
# Constant for the sales tax.
# The program prompts the user for the number of items purchased,
# and the price of each item.
# It then displays the subtotal, the tax cost, and the total cost.

# Constant for the sales tax
TAX_RATE = 0.07

# Assume subtotal
subtotal = 0

# Prompt user for number of items
num_items = int(input('How many items are you purchasing? '))

# Prompt user for prices of number items and calculate subtotal
for n in range(1, num_items + 1):
    price = float(input(f'Enter price for item {n}: '))
    subtotal += price
    
# Calculate tax and total cost
tax_cost = subtotal * TAX_RATE
total_cost = subtotal + tax_cost

# Print subtotal, tax, and total cost
print(f'''Subtotal: ${subtotal:,.2f}
Tax: ${tax_cost:,.2f}
Total: ${total_cost:,.2f}''')
