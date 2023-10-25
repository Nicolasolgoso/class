from BankAccount import BankAccount
while True:
    account_number = input("¿Cual es el número de tu cuenta?")

    account = BankAccount(account_number)

    operacion = int(input("¿Qué operación desea realizar? \n 1. Retirar dinero: \n 2. Ingresar dinero: \n 3. Consultar saldo: \n 4. Salir: "))

    if operacion == 3:
        print(f"Hay {account.get_balance()}€ en tu cuenta")

    elif operacion == 2:
        funds = float(input("¿Cuánto dinero quieres añadir?"))

        account.add_funds(funds)
        print(f"¡Hecho!, ahora hay {account.get_balance()}€ en tu cuenta")
        print(f"La cuenta con número: {account.get_account_number()} tiene {account.get_balance()}€ en su balance")

    elif operacion == 1:
        money = float(input("¿Cuánto dinero quieres retirar?"))

        account.take_money(money)
        print(f"¡Hecho!, ahora hay {account.get_balance()}€ en tu cuenta. Tu cuenta está en números rojos.")
        print(f"La cuenta con número: {account.get_account_number()} tiene {account.get_balance()}€ en su balance")

    elif operacion == 4:
        print("Gracias por usar el banco")
        break

    else:
        print("Error")