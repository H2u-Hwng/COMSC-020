# Huu Hung Nguyen
# 10/13/2021
# donuts_method.py
# Constants for price dozen and single of plain and fancy donuts.
# The program prompts the user for the number of plain and fancy donuts.
# It then calculates and displays the number of dozens and single donuts
# for each type of donuts, price of each type, and total cost.

# Constants for price dozen and single of plain donuts
COST_PLAIN_DOZEN = 7.00
COST_PLAIN = 0.60

# Constants for price dozen and single of fancy donuts
COST_FANCY_DOZEN = 9.00
COST_FANCY = 0.80

# Constants for number dozen
DOZEN = 12

# Take the costs for dozens and singles along with the number of donuts
# Calculate and return the number dozens, singles, and cost of donuts
def get_donuts(cost_dozen, cost_single, donuts):
    
    # Calculate number dozen and single of donuts
    dozens = donuts // DOZEN
    singles = donuts % DOZEN
    
    # Calculate cost donuts
    cost = dozens * cost_dozen + singles * cost_single
    
    return dozens, singles, cost
    
 
# Define main function
def main():
    
    # Prompt user for number of plain and fancy donuts
    plain_donut = int(input('Enter number of plain donuts you want to buy: '))
    fancy_donut = int(input('Enter number of fancy donuts you want to buy: '))
   
    # Obtain number dozens, singles, and cost of plain donuts
    plain_dozens, plain_singles, cost_plain_donuts = \
                  get_donuts(COST_PLAIN_DOZEN, COST_PLAIN, plain_donut)
    
    # Obtain number dozens, singles, and cost of fancy donuts
    fancy_dozens, fancy_singles, cost_fancy_donuts = \
                  get_donuts(COST_FANCY_DOZEN, COST_FANCY, fancy_donut)
    
    # Obtain total cost
    total_cost = cost_plain_donuts + cost_fancy_donuts
    
    # Display results
    print(f'''Plain donuts: 
   {plain_dozens} dozen and {plain_singles} single
   Cost: ${cost_plain_donuts:,.2f}
Fancy donuts:
   {fancy_dozens} dozen and {fancy_singles} single
   Cost: ${cost_fancy_donuts:,.2f}
Total amount due: ${total_cost:,.2f}''')

# Call main function
main()
