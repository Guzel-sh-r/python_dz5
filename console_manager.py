import os
import shutil
import sys
import victory
import use_functions


while True:
    print('1. создать папку')
    print('2. удалить(файл/папку)')
    print('3. копировать(файл/папку)')
    print('4. просмотр содержимого рабочей директории')
    print('5. посмотреть только папки')
    print('6. посмотреть только файлы')
    print('7. просмотр информации об операционной системе')
    print('8. создатель программы')
    print('9. играть в викторину')
    print('10. мой банковский счет')
    print('11. смена рабочей директории')
    print('12. сохранить содержимое рабочей директории в файл')
    print('13. выход')

    choice = input('Выберите пункт меню: ')
    if choice == '1':
        name_path = input('Введите название папки: ')
        os.makedirs(f"{name_path}")
        print(f'Папка с названием "{name_path}" создана')
    elif choice == '2':
        all_name = os.listdir()
        name_path = input('Введите название папки/файла: ')
        if os.path.exists(f'{name_path}'):
            if '.py' in name_path:
                try:
                    os.remove(name_path)
                    print('Удаление выполнено')
                except:
                    print(f'Файл с названием "{name_path}" не найден')
            else:
                shutil.rmtree(name_path)
                print('Удаление выполнено')
        else:
            print(f'Папка/файл с названием "{name_path}" не найден')
    elif choice == '3':
        all_name = os.listdir()
        name_path = input('Введите название папки/файла для копирования: ')
        if os.path.exists(f'{name_path}'):
            name_copy_path = input('Введите какое название у новой папки/файла будет: ')
            if '.py' in name_path and '.py' in name_copy_path:
                shutil.copy(name_path, name_copy_path)
                print('Копирование выполнено')
            elif not '.py' in name_path or not '.py' in name_copy_path:
               print('НЕ ВЫПОЛНЕНО копирование. Если копируется файл, то в названии должен быть его формат(.py например). А если папка, то формата не должно быть')
            else:
                shutil.copytree(name_path, name_copy_path, dirs_exist_ok=True)
                print('Копирование выполнено')
        else:
            print('Нет такого файла/папки')
    elif choice == '4':
        all_name = os.listdir()
        print(f'Рабочая директория сейчас: {os.getcwd()}')
        [print(all_name[i]) for i in range(len(all_name))]
    elif choice == '5':
        all_name = os.listdir()
        for i in all_name:
            if os.path.isdir(i):
                print(i)
    elif choice == '6':
        all_name = os.listdir()
        for i in all_name:
            if os.path.isfile(i):
                print(i)
    elif choice == '7':
        print('Операционная система:', sys.platform)
    elif choice == '8':
        print('Создатель программы: Гузель Абдрахманова, телеграм https://t.me/guzelshr')
    elif choice == '9':
        victory.func_victory()
    elif choice == '10':
        use_functions.func_use_functions()
    elif choice == '11':
        cwd = os.getcwd()
        fd = input(f'Ваша рабочая директория сейчас: {cwd} Введите полный \\home\\user\\... путь: ')
        fd.replace('\\', '\\\\')
        try:
            os.chdir(fd)
            print(f'Ваша рабочая директория сейчас: {os.getcwd()}')
        except:
            print(f'Произошла ошибка: {sys.exc_info()}')
            print()
            os.chdir(cwd)
            print('Восстановление пути к текущему каталогу - ', os.getcwd())
    elif choice == '12':
        all_name = os.listdir()
        dirs, files = [], []
        for i in all_name:
            if os.path.isdir(i):
                dirs.append(i)
            elif os.path.isfile(i):
                files.append(i)
        with open('listdir.txt', 'w', encoding='utf-8') as file:
            file.write(f"dirs: {', '.join(dirs)}\nfiles: {', '.join(files)}")
        print(f'Cодержимое рабочей директории {os.getcwd()} сохранено в файл listdir.txt')
    elif choice == '13':
        break
    else:
        print('Неверный пункт меню')
