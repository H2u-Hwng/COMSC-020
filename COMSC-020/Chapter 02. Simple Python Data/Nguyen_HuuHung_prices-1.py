# Huu Hung Nguyen
# 09/11/2021
# Nguyen_HuuHung_prices.py
# The program assigns the sales tax.
# It prompts the user for the prices of five items.
# It then displays the subtotal of the sale, the amount of sales tax,
# and the total.


# Assume sales tax is 7 percent
SALES_TAX_RATE = 0.07

# Prompt user for prices of five items
price_1 = float(input('Enter price for item 1: '))
price_2 = float(input('Enter price for item 2: '))
price_3 = float(input('Enter price for item 3: '))
price_4 = float(input('Enter price for item 4: '))
price_5 = float(input('Enter price for item 5: '))

# Calculate subtotal
subtotal = price_1 + price_2 + price_3 + price_4 + price_5

# Calculate tax
tax = subtotal * SALES_TAX_RATE

# Calculate total
total_cost = subtotal + tax

# Print subtotal, tax, and total
print('''Subtotal: ${:.2f}
Tax: ${:.2f}
Total: ${:.2f}'''. format(subtotal, tax, total_cost))