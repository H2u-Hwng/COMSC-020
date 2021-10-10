# Constants for discounts
DISCOUNT_1 = 0
DISCOUNT_2 = 0.1
DISCOUNT_3 = 0.2
DISCOUNT_4 = 0.25
DISCOUNT_5 = 0.3

# Define software sales function
def software_sales(price, quantity):
    
    # Calculate total cost before discount
    total_cost = price * quantity
    
    # Calculate amount of discount 
    if quantity < 10:
        discount = DISCOUNT_1
    elif quantity in range(10, 20):
        discount = DISCOUNT_2
    elif quantity in range(20, 50):
        discount = DISCOUNT_3
    elif quantity in range(50, 100):
        discount = DISCOUNT_4
    else:
        discount = DISCOUNT_5
    
    amount_discount = total_cost * discount
    
    # Calculate total cost after discount
    total_w_discount = total_cost - amount_discount
    
    return [total_cost, amount_discount, total_w_discount]

# Define main function
def main():
    
    # Prompt user for price of product and quantity ordered
    price = float(input('Enter the price of the product: $'))
    quantity = int(input('Enter the quantity ordered: '))
    
    # Get total cost before discount and amount of discount 
    total_cost = software_sales(price, quantity)[0]
    amount_discount = software_sales(price, quantity)[1]
    
    # Get total cost after discount
    total_w_discount = software_sales(price, quantity)[2]

    # Display results
    print(f'''The price before discount is ${total_cost:,.2f}
The amount of discount is ${amount_discount:,.2f}
The total cost of purchase after the discount is ${total_w_discount:,.2f}''')
    
# Call main function
main()