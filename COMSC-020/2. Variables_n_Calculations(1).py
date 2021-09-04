# Huu Hung Nguyen
# September 3, 2021
# Total_Purchase.py
# The program will prompt the user for prices of items.
# The program performs the subtotal of the sale, the amount of sales tax, and the total.
# The program displays the output.


# Prompt the subtotal
subtotal = 0

# Prompt the user for the prices of items
for n in range(1, 100):
    n = str(n)
    price = input('Enter price for item ' + n + ': ')
    if price is not '':
      
        #Perform the subtotal
        subtotal += float(price)
   
    else:
        break

# Perform the tax
tax = float(subtotal) * 0.07

# Perform the total
total = subtotal + tax

# Display the output
print('Subtotal: $ {:,.2f} \nTax: $ {:,.2f} \nTotal: $ {:,.2f}'.format(subtotal, tax, total))
