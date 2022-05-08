# работа функции заключающаяся на основе рекурсии
# и вовод данных после ее остановки'''


def output_of_numbers(number):
    if number == 0:
        return 0
    output_of_numbers(number - 1)
    print(number)


# запрос необходимого числа в и запрос функции
output_of_numbers(int(input('Введите число: ')))

# зачтено
