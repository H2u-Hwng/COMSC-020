# Huu Hung Nguyen
# 12/12/2021
# Nguyen_HuuHung_testaccounts.py
# The program imports Nguyen_HuuHung_accounts.py
# The program deposits and withdraws money.
# It then determines and display each account status.

# Import all the functions defined in Nguyen_HuuHung_accounts.py
from accounts import Account, SavingAccount, CreditCardAccount

def main():
    ''' Define main function. '''
    
    # Initialize a list of 5 accounts
    accounts_list = [
                     Account(1066, 7500),
                     SavingAccount(30507, 4500, 1.5),
                     CreditCardAccount(517822, 7000, 8, 1000),
                     CreditCardAccount(629553, 1500, 7.5, 5000),
                     CreditCardAccount(497720, -5000, 7, 10000)
                     ]
    
    # Check each account in the accounts list
    for account in accounts_list:
        # Deposit money to the account
        account.deposit(2134)
        
        # Withdraw money from the account
        account.withdraw(4782)
        
        # Display the account
        print(account)
        
        # Check if the account is saving account
        if type(account).__name__ == 'SavingAccount':
            # Determine and display the annual interest
            annual_interest = account.calculate_interest()
            print(f'Annual interest: ${annual_interest:,.2f}')
        
        # Check if the account is credit card account
        if type(account).__name__ == 'CreditCardAccount':
            # Determine and display the monthly payment
            monthly_payment = account.calculate_payment()
            print(f'Monthly payment: ${monthly_payment:,.2f}')
        
        print() # for readability
        
# Call main function
main()
