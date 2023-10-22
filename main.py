from BankAccount import BankAccount

account_number = input("¿Cual es el número de tu cuenta?")

account = BankAccount(account_number)

operacion = int(input("¿Qué operación desea realizar? \n para retirar dinero pulsa 1: \n para ingresar dinero pulsa 2: \n para consultar saldo pulsa 3: "))

if operacion == 3:
    print(f"Hay{account.get_balance()}€ en tu cuenta")

elif operacion == 2:
    funds = float(input("¿Cuánto dinero quieres añadir?"))

    account.add_funds(funds)
    print(f"¡Hecho!, ahora hay {account.get_balance()}€ en tu cuenta")
    print(f"La cuenta con número: {account.get_account_number()} tiene {account.get_balance()}€ en su balance")

elif operacion == 1:
    money = float(input("¿Cuánto dinero quieres retirar?"))

    account.take_money(money)
    print(f"¡Hecho!, ahora hay {account.get_balance()}€ en tu cuenta")
    print(f"La cuenta con número: {account.get_account_number()} tiene {account.get_balance()}€ en su balance")

else:
    print("Error")