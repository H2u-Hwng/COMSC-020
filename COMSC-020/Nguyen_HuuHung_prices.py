# Huu Hung Nguyen
# 09/14/2021
# Nguyen_HuuHung_prices.py
# The program assumes the sales tax.
# It prompts the user for the number of items purchased,
# and the price of each item.
# It then displays the subtotal of the sale, the amount of sales tax,
# and the total cost.


# Assume sales tax is 7 percent
SALES_TAX_RATE = 7 / 100

# Assign subtotal
subtotal = 0

# Prompt user for number of items
num_items = int(input('How many items are you purchasing? '))

# Prompt user for prices of number items and calculate subtotal
for n in range(1, num_items + 1):
    item = float(input('Enter price for item {}: '. format(n)))
    subtotal += item
    
# Calculate tax and total cost
tax = subtotal * SALES_TAX_RATE
total_cost = subtotal + tax

# Print subtotal, tax, and total cost
print('''Subtotal: ${:.2f}
Tax: ${:.2f}
Total: ${:.2f}'''. format(subtotal, tax, total_cost))