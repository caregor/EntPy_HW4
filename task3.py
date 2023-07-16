"""
    ---Task 3---
Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции.
Дополнительно сохраняйте все операции поступления и снятия средств в список.
"""

def calculate_withdrawal_fee(amount):
    fee = amount * 0.015
    fee = max(fee, 30)
    fee = min(fee, 600)
    return fee


def calculate_tax(amount):
    tax = amount * 0.1
    return tax


def deposit_funds(balance, operations, amount):
    if amount % 50 == 0:
        balance += amount
        operations.append(('Пополнение', amount))
        return balance
    else:
        print("Ошибка: Сумма пополнения должна быть кратна 50.")
        return balance


def withdraw_funds(balance, operations, amount):
    if amount % 50 == 0:
        if amount <= balance:
            fee = calculate_withdrawal_fee(amount)
            operations.append(('Снятие', amount))
            operations.append(('Комиссия', fee))
            balance -= (amount + fee)
            return balance
        else:
            print("Ошибка: Недостаточно средств на счете.")
            return balance
    else:
        print("Ошибка: Сумма снятия должна быть кратна 50.")
        return balance


def operation_count(balance, operations_count, operations):
    operations_count += 1
    if operations_count % 3 == 0:
        interest = balance * 0.03
        operations.append(('Начисление', interest))
        balance += interest
    return operations_count, balance


def perform_operations():
    balance = 0
    operations_count = 0
    operations = []

    while True:
        print("Текущий баланс:", balance)

        action = input("Выберите действие:\n - 1 -- пополнить;\n - 2 -- снять;\n - 3 -- выйти;\n")

        if action == '1':
            deposit = int(input("Введите сумму для пополнения (кратно 50): "))
            balance = deposit_funds(balance, operations, deposit)
            operations_count, balance = operation_count(balance, operations_count, operations)

        elif action == '2':
            withdrawal = int(input("Введите сумму для снятия (кратно 50): "))
            balance = withdraw_funds(balance, operations, withdrawal)
            operations_count, balance = operation_count(balance, operations_count, operations)

        elif action == '3':
            if balance > 5000000:
                tax = calculate_tax(balance)
                operations.append(('Удержание налога', tax))
                balance -= tax
                print("Удержан налог на богатство 10%")
            break

        else:
            print("Ошибка: Неверное действие.")

    print("Баланс:", balance)
    print("История операций:")
    for operation in operations:
        print(operation[0], operation[1])


perform_operations()