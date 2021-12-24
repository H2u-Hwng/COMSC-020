#
#   Account class.
#   Each account has an account number (acct_number), account holder's name,
#   PIN (4 character string) and current balance.
#
#   

class Account:

    def __init__(self, acct_number, name, pin, balance):
        """Intialize corresponding members of the Account object
        being created."""        

    def __str__(self):
        """Return a string that has the account number, account holder's
        name, PIN, and balance; separated by colons."""

    def deposit(self, amount):
        """Add the amount to the balance if the amount is greater than
        or equal to zero. If not, leave the object untouched."""

    def withdraw(self, amount):
        """Subtract the amount from the balance if the amount is greater than
        or equal to zero and less than or equal to the current balance. If
        not, leave the object untouched."""
    
