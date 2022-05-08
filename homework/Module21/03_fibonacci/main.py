def range_function(num_pos):
    if num_pos == 0:
        return 0
    elif num_pos == 1:
        return 1
    else:
        return range_function(num_pos - 1) + range_function(num_pos - 2)


'''запрос данных от пользователя и запрос функции'''
num_pos = int(input('Введите позицию числа в ряде Фибоначчи: '))
print('Число: ', range_function(num_pos))
