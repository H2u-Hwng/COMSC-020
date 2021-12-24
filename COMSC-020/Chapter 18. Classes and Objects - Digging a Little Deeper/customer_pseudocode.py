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

import account

#   Global variable: the account dictionary
accounts = {}

def create_dictionary():
    """Create dictionary of accounts from a data file that has
    acct number, name, pin, and current balance separated by colon"""
    infile = open('accounts.dat', 'r')
    for line in infile:
        # strip leading and trailing spaces, and split on ':'
        # create a new Account object with the given data
        # add it to the accounts dictionary with the account number as a key.
    infile.close()

def write_accounts():
    """Write back the accounts.dat file after customer finishes transaction."""
    # get list of keys for the accounts dictionary
    # sort that list
    # open the accounts.dat file for writing
    # for each key in the key list:
    #    write str(accounts[key]) + '\n' to the file
    # close the file
    
def input_account_number():
    """Return an account number as a string"""
    result = input('Enter account number (or ENTER to quit): ')
    while # result is not null and account number isn't in the dictionary:
        print('Invalid account number.')
        result = input('Enter account number (or ENTER to quit): ')
    return result

def input_pin():
    """Return a 4-digit PIN as a string"""
    #
    # repeatedly ask for a 4-digit PIN
    # while the answer isn't exactly four digits, keep asking
    # return the answer


def login(account_number):
    """Given an account number, give customer three tries to provide
    correct PIN. Return True if valid, False otherwise."""

    # set number of tries to one
    # retrieve the Account object for the given account_number
    # ask the user to input PIN (use input_pin() function)
    # while there are less than 3 tries and the input PIN doesn't match the
    # account PIN:
    #    add 1 to the number of tries
    #    ask for the PIN again
    # return True if the number of tries is not equal to 3 (good PIN),
    # otherwise return False (bad PIN)

def do_deposit(account):
    """Deposit to the given account (which is an object)."""
    # Repeatedly ask for an amount until you get a non-negative value.
    # Call the account's deposit() method with that amount.
    
def do_withdrawal(account):
    """Withdraw from the given account (which is an object)."""
    # Repeatedly ask for an amount until you get a value that is valid
    # (non-negative and not more than the balance)
    # Call the account's withdraw() method with that amount.
       
        
def do_transactions(account):
    """Ask to Deposit, Withdraw, or Finish; write new account file
    when finished. The account parameter is an Account object."""
    # Prompt for D)eposit, W)ithdraw, or F)inish and convert to uppercase
    # while action != 'F':
    #   if action == 'D':
    #       call do_deposit()
	#		print balance
    #   elif action == 'W':
    #       call do_withdrawal()
	#		print balance
    #   prompt again for D)eposit, W)ithdraw, or F)inish and convert to uppercase
    # call write_accounts()
    # print a message thanking the customer by name

def show_balance(account):
    """Return a string giving current account balance in proper
    format (2 decimals and dollar sign)"""
    return '$' + format(account.balance, '.2f')

def main():
    create_dictionary()
    account_number = input_account_number()
    while account_number != '':
        if login(account_number):
            account = accounts.get(account_number)
            print('Welcome, ', account.name, '! Your current balance is ',
                  show_balance(account), '.', sep='')
            do_transactions(account)
        else:
            print('Sorry, could not validate you as a customer.')

        account_number = input_account_number()

main()

    
