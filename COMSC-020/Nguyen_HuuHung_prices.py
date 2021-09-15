# Huu Hung Nguyen
# 09/14/2021
# Nguyen_HuuHung_prices.py
# The program assigns the sales tax.
# It prompts the user for the prices of five items.
# It then displays the subtotal of the sale, the amount of sales tax,
# and the total cost.


# Assume sales tax is 7 percent
SALES_TAX_RATE = 0.07

# Prompt user for prices of five items
price1 = float(input('Enter price for item 1: '))
price2 = float(input('Enter price for item 2: '))
price3 = float(input('Enter price for item 3: '))
price4 = float(input('Enter price for item 4: '))
price5 = float(input('Enter price for item 5: '))

# Calculate subtotal
subtotal = price1 + price2 + price3 + price4 + price5

# Calculate tax 
tax = subtotal * SALES_TAX_RATE

# Calculate total cost
total_cost = subtotal + tax

# Print subtotal, tax, and total cost
print('''Subtotal: ${:.2f}
Tax: ${:.2f}
Total: ${:.2f}'''. format(subtotal, tax, total_cost))