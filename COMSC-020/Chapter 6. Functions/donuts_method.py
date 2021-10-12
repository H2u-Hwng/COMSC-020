# Huu Hung Nguyen
# 10/12/2021
# donuts_method.py
# Constants for price dozen and single of both donuts.
# The program prompts the user for the number of both donuts.
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

# Calculate and return number dozen and single of donuts
def get_num_donuts(donuts):
    
    # Calculate number dozen and single of donuts
    dozens = donuts // DOZEN
    singles = donuts % DOZEN

    return dozens, singles


# Calculate and return price donuts 
def get_price(dozens, price_dozen, singles, price_single):
    
    # Calculate price donuts
    price = dozens * price_dozen + singles * price_single

    return price


# Define main function
def main():
    
    # Prompt user for number of plain and fancy donuts
    plain = int(input('Enter number of plain donuts you want to buy: '))
    fancy = int(input('Enter number of fancy donuts you want to buy: '))
    
    # Obtain number dozen and single of plain and fancy donuts
    dozens_plain, singles_plain = get_num_donuts(plain)
    dozens_fancy, singles_fancy = get_num_donuts(fancy)
    
    # Obtain price of plain donuts, fancy donuts, and total cost
    plain_cost = get_price(dozens_plain, PRICE_DOZEN_PLAIN,
                           singles_plain, PRICE_SINGLE_PLAIN)
    fancy_cost = get_price(dozens_fancy, PRICE_DOZEN_FANCY,
                           singles_fancy, PRICE_SINGLE_FANCY)
    total_cost = plain_cost + fancy_cost
    
    # Display results
    print(f'''Plain donuts:
  {dozens_plain} dozen and {singles_plain} single
  Cost: ${plain_cost:,.2f}
Fancy donuts:
  {dozens_fancy} dozen and {singles_fancy} single
  Cost: ${fancy_cost:,.2f}
Total amount due: ${total_cost:,.2f}''')
    
# Call main function
main()