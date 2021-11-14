#
#   Simulate an ATM that allows deposits
#   and withdrawals.
#

def get_deposit_amount():
    """Repeatedly display a message asking for
    a deposit amount until you get a number >= 0.
    If the number is not valid, present an error
    message. Return the number as a float."""
    
    valid = True
    while valid:
        deposit_amount = float(input('How many do you want to deposit? '))
    
        if deposit_amount < 0:
            print('ERROR! Please enter a valid number.')
        else:
            valid = False
            
    return deposit_amount

def get_withdrawal_amount(balance):
    """Repeatedly display a message asking for
    an amount to withdraw until you get a number
    that is >=0 and <= balance. If the number is
    not valid, present an error message. Return the
    number as a float."""
    
    valid = True
    while valid:
        withdrawal_amount = float(input('How much do you want to withdraw? '))
        if withdrawal_amount < 0 or withdrawal_amount > balance:
            print('ERROR! Please enter a valid number.')
        else:
            valid = False
    return withdrawal_amount


def get_choice():
    """Repeatedly display a prompt asking user to
    Deposit, Withdraw, or Quit until you get one of
    the letters D, W, or Q (in upper or lower case.)
    If an invalid letter is given, present an error
    Return the letter in upper case."""
    
    valid = True
    while valid:

        input_prompt = 'What is your type of transaction? ' + \
                       'D)eposit, W)ithdraw, or Q)uit? '
        choice = input(input_prompt)
        choice = choice.upper()
        
        if choice not in 'DWQ':
            print('ERROR! Please enter a valid transaction.')
        else:
            valid = False
    
    return choice

def show_balance(balance):
    """Print the balance, properly labeled,
    with two decimal places."""
    
    print(f'Balence: {balance:,.2f}')
    
    pass

def main():
    """Define main function."""
    
    # Set balance to $1000.00 and display it
    balance = 1000.00
    show_balance(balance)
    
    choice = get_choice()
    
    while choice != 'Q':
        # if the person chose to make a deposit,
        # call get_deposit_amount() and then add that
        # amount to the balance, and display the balance.
        
        if choice == 'D':
            deposit_amount = get_deposit_amount()
            balance += deposit_amount
            print(balance)
        # if the person chose to make a withdrawal,
        # call get_withdrawal_amount() and then subtract that
        # amount from the balance, and display the balance.
        
        elif choice == 'W':
            withdrawal_amount = get_withdrawal_amount()
            balance -= withdrawal_amount
            print(balance)
        choice = get_choice()
        if choice == 'Q':
            print(balance)
            print('Goodbye!')
    # print the balance
    # print a "goodbye" message.

# Call main function
main()