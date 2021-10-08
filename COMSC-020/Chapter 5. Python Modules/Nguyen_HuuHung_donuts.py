# Huu Hung Nguyen
# 10/07/2021
# Nguyen_HuuHung_donuts.py
# Constants for price dozen and single of plain donuts,
# and price dozen and single of fancy donuts.
# The program prompts the user for the number of plain and fancy donuts.
# It then calculates and displays the number of dozens and single donuts
# for each type of donuts, price of each type, and total cost.

# Constants for price dozen and single of plain donuts
PRICE_DOZEN_PLAIN = 7.00
PRICE_SINGLE_PLAIN = 0.60

# Constants for price dozen and single of fancy donuts
PRICE_DOZEN_FANCY = 9.00
PRICE_SINGLE_FANCY = 0.80

# Constants for number dozen
DOZEN = 12

# Prompt user for number of plain and fancy donuts
plain = int(input('Enter number of plain donuts you want to buy: '))
fancy = int(input('Enter number of fancy donuts you want to buy: '))

# Calculate number dozen and single of plain donuts
dozen_plain = plain // DOZEN
single_plain = plain % DOZEN

# Calculate number dozen and single of fancy donuts
dozen_fancy = fancy // DOZEN
single_fancy = fancy % DOZEN

# Calculate price plain donuts, price fancy donuts, and total cost
plain_cost = \
        dozen_plain * PRICE_DOZEN_PLAIN + single_plain * PRICE_SINGLE_PLAIN
fancy_cost = \
        dozen_fancy * PRICE_DOZEN_FANCY + single_fancy * PRICE_SINGLE_FANCY
total_cost = plain_cost + fancy_cost

# Display results
print(f'''Plain donuts: 
  {dozen_plain} dozen and {single_plain} single
  Cost: ${plain_cost:,.2f}
Fancy donuts:
  {dozen_fancy} dozen and {single_fancy} single
  Cost: ${fancy_cost:,.2f}
Total amount due: ${total_cost:,.2f}''')
