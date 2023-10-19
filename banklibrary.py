from class import BankAccount

account_number = input("¿Cual es el número de tu cuenta?")

account = BankAccount(account-number)
print(f"Hay{account.get_balance()}€ en tu cuenta")

funds = float(input("¿Cuánto dinero quieres añadir?"))

account.add_funds(funds)
print(f"¡Hecho!, ahora hay {account.get_balance()}€ en tu cuenta")
