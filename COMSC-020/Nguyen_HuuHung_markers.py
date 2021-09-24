# Huu Hung Nguyen
# 09/23/2021
# Nguyen_HuuHung_markers.py
# The program assumes the price of 1 marker is 80 cents, 5 markers is $3.50,
# the tax sale rate is 6.5%, the shipping rate is 5%.
# It prompts the user for the number of markers.
# It calculates and displays the number of packages 5 markers,
# the number of separate markers, the subtotal, the tax cost,
# the shipping cost, and the total cost.

# Assume price of 1 marker, 5 markers, tax sale rate and shipping rate
PRICE1 = 0.80
PRICE5 = 3.50
TAX_SALE_RATE = 6.5 / 100
SHIPPING_RATE = 5 / 100

# Prompt user for number of markers
num_markers = int(input('How many markers are you buying? '))

# Calculate number of packages 5 markers and separate markers
num_packages = num_markers // 5
num_separate_markers = num_markers % 5

# Calculate subtotal, tax cost, shipping cost, and total cost
subtotal = num_packages * PRICE5 + num_separate_markers * PRICE1
tax_cost = subtotal * TAX_SALE_RATE
shipping_cost = subtotal * SHIPPING_RATE
total_cost = subtotal + tax_cost + shipping_cost

# Display program
print('''Number of packages: {}
Number of separate markers: {}
Subtotal: ${:.2f}
Tax:      ${:.2f}
Shipping: ${:.2f}
Total:    ${:.2f}'''. format(num_packages, num_separate_markers,
                             subtotal, tax_cost, shipping_cost, total_cost))