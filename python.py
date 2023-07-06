def func_filter(func_list, spisok):
    return list(filter(func_list, spisok))


spisok = ['bool', 0, None, True, False, 1, 1 - 1, 2 % 2]
print(func_filter(None, spisok))


def func_map(numbers):
    return list(map(int, numbers.split()))


numbers = '7 9 64 54 0 787'
print(func_map(numbers))


def func_sorted(spisok):
    return sorted(spisok, reverse=True)


spisok = [878, 78, -4478, -54, 4554, 5454]
print(func_sorted(spisok))
