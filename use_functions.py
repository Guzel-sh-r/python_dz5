import os.path


def func_use_functions():
    amount_account = 0
    if os.path.exists('my_account.txt'):
        with open('my_account.txt', 'r') as my_account:
            amount_account = int(my_account.read())

    purchase_history = []
    if os.path.exists('my_history.txt'):
        with open('my_history.txt', 'r', encoding='utf-8') as my_history:
            for line in my_history:
                purchase_history.append(line.strip())

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
            with open('my_account.txt', 'w', encoding='utf-8') as my_account:
                my_account.write(str(amount_account))
        elif choice == '2':
            summa = int(input('Введите сумму покупки: '))
            if summa <= amount_account:
                purchase = input('Введите название покупки: ')
                amount_account -= summa
                purchase_history.append(f'{purchase} {summa}')
                with open('my_account.txt', 'w', encoding='utf-8') as my_account:
                    my_account.write(str(amount_account))
                with open('my_history.txt', 'w', encoding='utf-8') as my_history:
                    for purchase in purchase_history:
                        my_history.write(f'{purchase}\n')
            else:
                print('Недостаточно средств на счету')
        elif choice == '3':
            [print(i, 'руб') for i in purchase_history]
        elif choice == '4':
            break
        else:
            print('Неверный пункт меню')
