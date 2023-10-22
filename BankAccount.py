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


bank_account1 = BankAccount("ES12345678912345")

bank_account1.add_funds(-250)
bank_account1.add_funds(761)
