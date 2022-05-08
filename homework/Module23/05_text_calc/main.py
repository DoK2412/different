import os

# проверка на длину строки и преобразование знчений
def converting_numbers(miscalculation):  # TODO не забывайте отделять определение функции от остального кода двумя
                                         #  пустыми строками
    if len(miscalculation) < 3 or len(miscalculation) > 3:
        raise IndexError('Строка не соответствует стандарту')
    else:
        number_1 = int(miscalculation[0])
        number_2 = int(miscalculation[2])
        return [number_1, number_2]

# проверка для определения принадлежни знака
def checking_the_sign(miscalculation):
    if miscalculation[1] not in '+, -, /, *, %, //':
        raise SyntaxError

# проверка деления на 0
def checking_for_zero(number_2):
    if number_2 == 0:
        raise ZeroDivisionError

# основная функция счета
def calculation(processing):
    the_amount = 0
    line = 0
    for miscalculation in processing:
        line += 1
        try:
            number_1, number_2 = converting_numbers(miscalculation)
            checking_the_sign(miscalculation)
            if miscalculation[1] == '+':
                the_amount += number_1 + number_2
            elif miscalculation[1] == '-':
                the_amount += number_1 - number_2
            elif miscalculation[1] == '/':
                checking_for_zero(number_2)
                the_amount += number_1 / number_2
            elif miscalculation[1] == '*':
                the_amount += number_1 * number_2
            elif miscalculation[1] == '%':
                the_amount += number_1 % number_2
            elif miscalculation[1] == '//':
                the_amount += number_1 // number_2
        except (SyntaxError, IndexError, TypeError,ZeroDivisionError, ValueError):
            print('В строке {0} обнаружена ошибка.'.format(line))

    print('Общая сумма верных выражений = ', the_amount)


# открываем файл на чтение и создаем рабочий список
with open(
    os.path.abspath(os.path.join('calc.txt')), 
    'r', encoding='utf-8') as example:
    processing = [i_example.split() for i_example in example.read().splitlines()]
    calculation(processing)
