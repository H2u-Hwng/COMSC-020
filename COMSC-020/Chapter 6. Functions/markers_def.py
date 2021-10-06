# Huu Hung Nguyen
# 10/05/2021
# markers_def.py
# Constants for number markers per package, price of marker and package,
# tax rate, and shipping rate.
# The program prompts user for number of markers.
# It calculates and displays number of packages 5 markers,
# number of separate markers, subtotal, tax cost, shipping cost, total cost.

# Constants for number markers per package, price of marker and package
MARKERS_PER_PACKAGE = 5
PRICE_MARKER = 0.80
PRICE_PACKAGE = 3.50

# Constants for tax rate and shipping rate
TAX_RATE = 0.065
SHIPPING_RATE = 0.05

# Define get total cost function
def get_total_cost(markers):
    
    # Calculate number of packages and separate markers
    packages = markers // MARKERS_PER_PACKAGE
    separate_markers = markers % MARKERS_PER_PACKAGE
    
    # Calculate subtotal, tax cost, and shipping cost
    subtotal = packages * PRICE_PACKAGE + separate_markers * PRICE_MARKER
    tax_cost = subtotal * TAX_RATE
    shipping_cost = subtotal * SHIPPING_RATE
    
    # Calculate total cost
    total_cost = subtotal + tax_cost + shipping_cost
    
    return [packages, separate_markers,
            subtotal, tax_cost, shipping_cost, total_cost]

# Define main function
def main():
    
    # Prompt user for number of markers
    markers = int(input('How many markers are you buying? '))
    
    # Get packages and separate markers
    packages, separate_markers = get_total_cost(markers)[0:2]
    
    # Get subtotal, tax cost, and shipping cost
    subtotal, tax_cost, shipping_cost = get_total_cost(markers)[2:5]
    
    # Get total cost
    total_cost = get_total_cost(markers)[5]
    
    # Print results
    print(f'''Number of packages: {packages}
Number of separate markers: {separate_markers}
Subtotal: ${subtotal:,.2f}
Tax:      ${tax_cost:,.2f}
Shipping: ${shipping_cost:,.2f}
Total:    ${total_cost:,.2f}''')
    
# Call main function
main()