# Huu Hung Nguyen
# 09/20/2021
# Nguyen_HuuHung_markers.py
# The program prompts the user for the number of markers purchased.
# It calculates the number of packages, the number of separate markers,
# the subtotal, the tax, the shipping cost, and the total cost.
# It then prints all of them.


# Prompt user for number of markers purchased
num_markers = int(input('How many markers are you buying? '))

# calculates number of packages and number of separate markers
num_packages = num_markers // 5
num_separate_markers = num_markers % 5

# Calculate subtotal, tax, shipping cost, and total cost
subtotal = num_packages * 3.50 + num_separate_markers * 0.80 
tax = subtotal * 6.5 / 100
shipping_cost = subtotal * 5 / 100
total_cost = subtotal + shipping_cost + tax

# Print all of them
print('''Number of packages: {}
Number of separate markers: {}
Subtotal: ${:.2f}
Tax:      ${:.2f}
Shipping: ${:.2f}
Total:    ${:.2f}'''. format(num_packages, num_separate_markers,
                             subtotal, tax, shipping_cost, total_cost))