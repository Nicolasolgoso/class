from class import BankAccount

account_number = input("¿Cual es el número de tu cuenta?")

operacion = int(input("¿Que operación deseas realizar? \n Para ingresar dinero marca 1: \n Para retirar dinero marca 2: \n Para consultar el saldo marca 3:"))

if operacion == 1:
    account = BankAccount(account-number)
    print(f"Hay{account.get_balance()}€ en tu cuenta")


funds = float(input("¿Cuánto dinero quieres añadir?"))

account.add_funds(funds)
print(f"¡Hecho!, ahora hay {account.get_balance()}€ en tu cuenta")
