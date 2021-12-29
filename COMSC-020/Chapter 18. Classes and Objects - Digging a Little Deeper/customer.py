#
#   Customer program.
#
#   This program constructs a dictionary of accounts keyed by account number
#   from a text file named accounts.dat. This file has one account per
#   line, with the account number, customer name, PIN, and balance,
#   separated by colons. For example, one entry might be:
#
#   10627:Georges Remi:0174:3571.85
#
#   The program then repeatedly allows customers to "log in" with account
#   number and PIN. (three tries). If user presses ENTER when asked for
#   account number, the program ends.
#
#   Once authenticated, the customer can deposit, withdraw, or finish.
#   When the customer finishes, the program writes the dictionary back to the
#   accounts.dat file in the same format as previously described.

from account import Account

accounts = {} # Global variable: the account dictionary

def create_dictionary():
    """Create dictionary of accounts from a data file that has
    acct number, name, pin, and current balance separated by colon"""
    
    infile = open('accounts.dat', 'r') # open the accounts.dat file for reading
  
    for line in infile:
        # strip leading and trailing spaces, and split on ':'
        data = line.strip().split(':')
        
        # create a new Account object with the given data
        account = Account(data[0], data[1], data[2], data[3])
        
        # add it to the accounts dictionary with the account number as a key.
        accounts[str(account.acct_number)] = account
        
    infile.close() # close the file


def write_accounts():
    """Write back the accounts.dat file after customer finishes transaction."""
    
    # get list of keys for the accounts dictionary
    accts_numbers_list = [acct_number for acct_number in accounts.keys()]
    
    sorted_list = sorted(accts_numbers_list) # sort that list
    
    infile = open('accounts.dat', 'w') # open the accounts.dat file for writing
    
    for acct_number in sorted_list:
        infile.write(str(accounts[acct_number]) + '\n') # write str(accounts[key]) + '\n' to the file
    
    infile.close() # close the file
    
    
def input_account_number():
    """Return an account number as a string"""
    
    # result is not null and account number isn't in the dictionary:
    valid = False
    while not valid:
        # prompt the user for an account number
        result = input('Enter account number (or ENTER to quit): ')
        if result in accounts or result == '':
            valid = True
        else:
            print('Invalid account number. \n')

    return result 


def input_pin():
    """Return a 4-digit PIN as a string"""

    # repeatedly ask for a 4-digit PIN until the pin is exactly four digits
    valid = False
    while not valid:
        # prompt the user for a 4-digit PIN
        pin = input('Enter 4-digit PIN: ')
        
        if len(pin) != 4:
            print('Invalid account number.')
        else:
            valid = True
            
    return pin


def login(account_number):
    """Given an account number, give customer three tries to provide
    correct PIN. Return True if valid, False otherwise."""
    
    trying = 1 # set number of tries to one
    
    # retrieve the Account object for the given account_number
    finished = False 
    while not finished:
        pin = input_pin() # ask the user to input PIN
        
        # while there are less than 3 tries and the input PIN doesn't match the account PIN
        if pin != accounts[account_number].pin:
            if trying == 3:
                finished = True
                result = False
            else:
                trying += 1 # add 1 to the number of tries
                print("The input PIN doesn't match the account PIN!")
        else:
            finished = True
            result = True
  
    return result


def do_deposit(account):
    """Deposit to the given account (which is an object)."""
    
    # Repeatedly ask for an amount until you get a non-negative value.
    valid = False
    while not valid:
        amount = float(input('Enter an amount: '))
        if amount < 0:
            print('Please enter the positive value!')
        else:
            valid = True
    
    # Call the account's deposit() method with that amount.
    account.balance = account.deposit(amount)
    
    
def do_withdrawal(account):
    """Withdraw from the given account (which is an object)."""
    
    # Repeatedly ask for an amount until you get a value that is valid
    # (non-negative and not more than the balance)
    valid = False
    while not valid:
        amount = float(input('Enter an amount: '))
        if amount < 0 or amount > account.balance:
            print('Please enter the valid value!')
        else:
            valid = True
            
    # Call the account's withdraw() method with that amount.
    account.balance = account.withdraw(amount)
    
        
def do_transactions(account):
    """Ask to Deposit, Withdraw, or Finish; write new account file
    when finished. The account parameter is an Account object."""
    
    # Prompt for D)eposit, W)ithdraw, or F)inish and convert to uppercase
    action = input('D)eposit, W)ithdraw, or F)inish: ')
    action = action.upper()
    
    while action != 'F':
        if action == 'D':
            do_deposit(account)
            print(account.balance)
        elif action == 'W':
            do_withdrawal(account)
            print(account.balance)
        
        # Prompt for D)eposit, W)ithdraw, or F)inish and convert to uppercase
        action = input('D)eposit, W)ithdraw, or F)inish: ')
        action = action.upper()
        
    write_accounts()
    
    # display a message thanking the customer by name
    print(f'Thanks {account.name} for using our services! \n') 


def show_balance(account):
    """Return a string giving current account balance in proper
    format (2 decimals and dollar sign)"""
    
    return '$' + format(account.balance, '.2f')


def main():
    ''' define main function. '''
    
    create_dictionary() # create the dictionary
    
    account_number = input_account_number() # prompt the user for the account number
    
    while account_number != '':
        if login(account_number):
            # determine and display the account
            account = accounts.get(account_number)
            print(f'Welcome, {account.name}! Your current balance is {show_balance(account)}.')
            
            # do the services on the account
            do_transactions(account)
        else:
            print('Sorry, could not validate you as a customer. \n')
            
        # ask the users whether they want to use another services
        again = input('Do you want to use our another services? (Y/N) ')
        again = again.upper()
        
        if again == 'Y':
            account_number = input_account_number()
        else:
            account_number = ''
            
    print('Bye. See you next time!')
    
# call main fuction
main()