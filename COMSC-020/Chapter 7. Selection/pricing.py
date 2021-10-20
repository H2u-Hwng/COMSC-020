# Huu Hung Nguyen
# 10/19/2021
# Nguyen_HuuHung_pricing.py
# Constants for discounts
# Program prompts user for price of product and quantity ordered.
# It then calculate and displays total price, amount discount,
# and total with discount.

# Constants for discounts
DISCOUNT1 = 0.00
DISCOUNT2 = 0.10
DISCOUNT3 = 0.20
DISCOUNT4 = 0.25
DISCOUNT5 = 0.30

# Take cost and quantity
# Calculate and return total cost, discount cost, and total with discount
def software_sales(cost, quantity):
    
    # Calculate total cost
    total_cost = cost * quantity
    
    # Check discount and calculate discount cost
    if quantity < 10:
        discount = DISCOUNT1
    elif quantity < 20:
        discount = DISCOUNT2
    elif quantity < 50:
        discount = DISCOUNT3
    elif quantity < 100:
        discount = DISCOUNT4
    else:
        discount = DISCOUNT5
    
    discount_cost = total_cost * discount
    
    # Calculate total with discount
    total_with_discount = total_cost - discount_cost

    return total_cost, discount_cost, total_with_discount


# Define main function
def main():
    
    # Prompt user for price of product and quantity ordered
    price_product = float(input('Enter price of product: $'))
    quantity_ordered = int(input('Enter quantity: '))
    
    # Obtain total price, amount discount, and total with discount
    total_price, amount_discount, total_with_discount = \
                 software_sales(price_product, quantity_ordered)
     
    # Display results
    print(f'Total price before discount: ${total_price:,.2f}')
    print(f'Amount of discount: ${amount_discount:,.2f}')   
    print(f'Total price after discount: ${total_with_discount:,.2f}')    
    
# Call main function
main()