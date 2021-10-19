# Constants for costs
COST1 = 0.00
COST2 = 17.00
COST3 = 23.00
COST4 = 19.00

# Take the age and return the cost of the buffet 
def get_cost(age):
    
    # Determine the cost
    if age <= 3:
        cost = COST1
    elif age <= 14:
        cost = COST2
    elif age <= 64:
        cost = COST3
    else:
        cost = COST4
    
    return cost


# Define main function
def main():
    
    # Prompt user for age
    age = int(input('How old are you? '))
    
    # Obtain cost of buffet
    cost_buffet = get_cost(age)
    
    # Display result
    print(f'if you are {age} years old,', end = ' ')
    print(f'the buffet will cost ${cost_buffet:,.2f}.')
    
# Call main function
main()
