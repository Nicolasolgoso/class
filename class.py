class BankAccount: 
    def __init__(self,account_number, balance = 0):
        self.account_number = account_number
        self.balance = balance

    def get_account_number(self):
        return self.account_number

    def add_funds(self,funds):
        self.balance += funds

    def get_balance(self):
        return self.balance


bank_account1 = BankAccount("ES99999999999999999")

bank_account1.add_funds(-250)
bank_account1.add_funds(761)

print(f"La cuenta con número: {bank_account1.get_account_number()} tiene {bank_account1.get_balance()}€ en su balance")