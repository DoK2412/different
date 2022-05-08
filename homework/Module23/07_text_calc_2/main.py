import os


# функция для преобразования не верных примеров
def error_correction(miscalculation, line):
    correction = input('Обнаружена ошибка в строке {0}: \
{1} Хотите исправить? /да/нет/'.format(line, ' '.join(miscalculation)))
    if correction.lower() == 'да':
        example = input('Введите исправленную строку: ').split()
        result = processing_the_example(example, line)
        return result
    else:
        return 0


# проверка на длину строки и преобразование знчений
def converting_numbers(miscalculation):
    if len(miscalculation) < 3 or len(miscalculation) > 3:
        raise IndexError
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


# функция для расчета примеров из файлов
def processing_the_example(miscalculation, line):
    the_amount = 0
    try:
        number_1, number_2 = converting_numbers(miscalculation)
        checking_the_sign(miscalculation)
        # the_amount += error_correction(miscalculation, line)
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
    except (SyntaxError, IndexError, TypeError, ZeroDivisionError, ValueError):
        the_amount += error_correction(miscalculation, line)

    return the_amount


# начальная функция запускающая щикл
def calculation(processing):
    summ = 0
    line = 0
    for miscalculation in processing:
        line += 1
        summ += processing_the_example(miscalculation, line)
    print('Общая сумма выражений: ', summ)


# открываем файл на чтение и создаем рабочий список
with open(
        os.path.abspath(os.path.join('calc_2.txt')),
        'r', encoding='utf-8') as example:
    processing = [i_example.split() for i_example
                  in example.read().splitlines()]
    calculation(processing)
