# Constants for prices, regular units, and extra money of two plans
PRICE_1 = 9.38
LIMIT_UNITS_1 = 65
EXTRA_MONEY_1 = 0.045

PRICE_2 = 8.57
LIMIT_UNITS_2 = 50
EXTRA_MONEY_2 = 0.052

# Define get units function
def get_units():
    
    # Prompt user for the number of units used
    units = int(input('Enter number of units used, or zero to quit: '))
    
    return units

# Define calculate cost function
def calculate_cost(units, price, limit_units, extra_money):
    
    # Calculate cost for units using the plan
    total_cost = price
    if units > limit_units:
        extra_units = units - limit_units
        total_cost += extra_units * extra_money
        
    return total_cost

# Define main function
def main(units):
    
    # Get cost for units using the first plan
    total_cost_1 = calculate_cost(units, PRICE_1, LIMIT_UNITS_1, EXTRA_MONEY_1)
    
    # Get cost for units using the second plan
    total_cost_2 = calculate_cost(units, PRICE_2, LIMIT_UNITS_2, EXTRA_MONEY_2)
    
    # Display cost of two plans and tell which plan is cheaper
    print(f'Cost for plan 1: ${total_cost_1:,.2f}')
    print(f'Cost for plan 2: ${total_cost_2:,.2f}')
    
    if total_cost_1 < total_cost_2:
        print(f'Plan 1 is cheaper. \n')
    else:
        print(f'Plan 2 is cheaper. \n')
        
# Get results
while True:
    
    # Get units
    units = get_units()
    
    # Call main function
    if units < 0:
        print('You cannot have negative units.')
    elif units == 0:
        break
    else:
        main(units)
    