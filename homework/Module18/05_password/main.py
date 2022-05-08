# функция для определения значений
def check(lis, compared_value):
    counter = 0
    for i in lis:
        for x in compared_value:
            if i == x:
                counter += 1
    return counter
# списки для работы провепки
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
capital_letters = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']
# бесконечный цикл на запрос
while True:
    request_a_password = input('Введите пароль: ')
    # получение данных из финкции
    number_of_digits = check(request_a_password, numbers)
    number_of_capital_letters = check(request_a_password, capital_letters)
    # проверка пароля на правильность
    if len(request_a_password) >= 8:
        if number_of_digits >= 3 and number_of_capital_letters >= 1:
            print('Это надежный пароль.')
            break
        else:
            print('Пароль ненадёжный. Попробуйте ещё раз.')
    else:
        print('Пароль ненадёжный. Попробуйте ещё раз.')
