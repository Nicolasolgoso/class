class BankAccount: 
    def __init__(self,account_number, balance = 0):
        self.account_number = account_number
        self.balance = balance

    def get_account_number(self):
        return self.account_number

    def add_funds(self,funds):
        self.balance += funds

    def take_money(self,money):
        self.balance -= money

    def get_balance(self):
    
        return self.balance

class SavingAccount(BankAccount):

    def  __init__(self,account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def generate_interest(self, time_period):
        interest = (self.balance * self.interest_rate * time_period) / 12
        self.add_funds(interest)
        return interest

class CheckingAccount(BankAccount):
    def __init__(self, account_number, balance, overdraft_limit):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit

    def take_money(self, money):
        if money <= self.balance + self.overdraft_limit:
            self.balance -= money
        else:
            print("Exceeded overdraft limit")



