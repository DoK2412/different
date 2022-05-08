import  itertools
# список возможных цифр
list_number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# цикл предобразованный через модуль на получение паролей
for i_number in itertools.permutations(list_number, 4):  # TODO нужен полнынй перебор с повторами, то есть .product()
    print(i_number)
