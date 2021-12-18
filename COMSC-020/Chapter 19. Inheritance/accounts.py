# Huu Hung Nguyen
# 12/12/2021
# Nguyen_HuuHung_accounts.py
# The program stores the Account class, the SavingAccount class, and
# the CreditCardAccount class.

class Account:
    ''' Account class for representing and
        manipulating number, balance coordinates. '''
    
    def __init__(self, number, balance):
        ''' Create a new point at the given coordinates. '''
        
        self.number = number
        self.balance = balance
        
    def __str__(self):
        ''' Display the account number and balance. '''
        
        display = f'Account number: {self.number}' + '\n' + \
                  f'Balance: ${self.balance:,.2f}'
        
        return display 
        
    def deposit(self, amount):
        ''' Return the balance after depositting. '''
        
        if amount >= 0:
            self.balance += amount
            
        return self.balance
    
    def withdraw(self, amount):
        ''' Return the balance after withdrawing. '''
        
        if amount <= self.balance:
            self.balance -= amount
            
        return self.balance

class SavingAccount(Account):
    ''' SavingAccount class for representing and
        manipulating number, balance, apr coordinates. '''
    
    def __init__(self, number, balance, apr):
        ''' Create a new point at the given coordinates. '''
        
        super().__init__(number, balance)
        self.apr = apr / 100
        
    def __str__(self):
        ''' Display the account number, balance, and apr. '''
        
        return super().__str__() + f'\nAPR: {self.apr * 100:,.2f}%'
    
    def calculate_interest(self):
        ''' Return the annual interest. '''
        
        annual_interest = self.balance * self.apr
        
        return annual_interest
    
class CreditCardAccount(Account):
    ''' SavingAccount class for representing and
        manipulating number, balance, apr, credit limit coordinates. '''
    
    def __init__(self, number, balance, apr, credit_limit):
        ''' Create a new point at the given coordinates. '''
        
        super().__init__(number, balance)
        self.apr = apr / 100
        self.credit_limit = credit_limit
        
    def __str__(self):
        ''' Display the account number, balance, apr, and credit limit. '''
        
        display = super().__str__() + f'\nAPR: {self.apr * 100:,.2f}%' + \
                  f'\nCredit Limit: ${self.credit_limit:,.2f}'
        
        return display
    
    def withdraw(self, amount):
        ''' Return the balance after withdrawing. '''
        
        if amount <= self.balance + self.credit_limit:
            self.balance -= amount
        
        return self.balance
    
    def calculate_payment(self):
        ''' Return the monthly payment. '''
        
        if self.balance > 0:
            monthly_payment = 0
        elif (self.apr / 12) * (-self.balance) >= 20:
            monthly_payment = 20
        else:
            monthly_payment = (self.apr / 12) * (-self.balance)
        
        return monthly_payment
