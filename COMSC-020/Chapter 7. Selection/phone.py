# Huu Hung Nguyen
# 10/22/2021
# Nguyen_HuuHung_phone.py
# Constants for base prices, extra prices, and limit units of both plans
# Program prompts user for number of units used (integer).
# It calculates and displays the cost for the units using both plans.
# It then tells which plan is cheaper.

# Constants for base prices, extra prices, and limit units of both plans
PRICE1 = 9.38
EXTRA_PRICE1 = 0.045
LIMIT_UNITS1 = 65
PRICE2 = 8.57
EXTRA_PRICE2 = 0.052
LIMIT_UNITS2 = 50

# Prompt and return number of units used 
def get_units():
    valid = False
    
    # Enter units until valid units are entered
    while not valid:
        units = int(input('Enter number of units used, or -1 to finish: '))
        
        # Check if valid units are entered
        if units >= 0 or units == -1:
            valid = True
        else:
            print('You cannot have negative units.')
            print('Please enter valid units. \n')
    
    return units


# Calculate total cost 
def calculate_cost(units, cost, base_limit, extra_cost):
    
    # Initialize total cost
    total_cost = cost
    
    # Update the cost for extra units
    if units > base_limit:
        total_cost += (units - base_limit) * extra_cost
        
    return total_cost


# Display cheaper plan
def check_plans(total_cost1, total_cost2):
    if total_cost1 < total_cost2:
        print('Plan 1 is cheaper. \n')
    else:
        print('Plan 2 is cheaper. \n')
     
     
# Define main function
def main():
        
    # Keep entering units until finish is set to true
    finish = False
    
    # Enter units until the user enters -1
    while not finish:
        
        # Obtain the number of units used
        units_used = get_units()
        
        # Check if user finish entering units
        if units_used == -1:
            finish = True
        else:
            
            # Obtain the cost for the units using the first and second plans
            total_price1 = calculate_cost(units_used, PRICE1,
                                          LIMIT_UNITS1, EXTRA_PRICE1)
            total_price2 = calculate_cost(units_used, PRICE2,
                                          LIMIT_UNITS2, EXTRA_PRICE2)
                
            # Display the cost for the units using the first and second plans
            print(f'Cost for plan 1: ${total_price1:,.2f}')
            print(f'Cost for plan 2: ${total_price2:,.2f}')
                
            # Display cheaper plan
            check_plans(total_price1, total_price2)
    
# Call main function
main()