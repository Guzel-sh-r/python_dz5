def func_use_functions(amount_account, purchase_history):
    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        choice = input('Выберите пункт меню для работы с банковским счетом: ')
        if choice == '1':
            summa = int(input('Введите сумму для пополнения счета: '))
            amount_account += summa
            print(f'Сумма на вашем счету: {amount_account} руб.')
        elif choice == '2':
            summa = int(input('Введите сумму покупки: '))
            if summa <= amount_account:
                purchase = input('Введите название покупки: ')
                amount_account -= summa
                purchase_history.append((purchase, summa))
            else:
                print('Недостаточно средств на счету')
        elif choice == '3':
            [print(*i, "руб") for i in purchase_history]
        elif choice == '4':
            return amount_account, purchase_history
        else:
            print('Неверный пункт меню')
