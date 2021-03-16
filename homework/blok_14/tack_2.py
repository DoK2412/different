def summ(number):
    counter = 0
    while number > 0:
        counter += number % 10
        number //= 10
    return counter


def quantity(number):
    x = len(str(number))
    return x

number = int(input('Введите число: '))

print('Сумма цифр: ', summ(number))
print('Кол-во цифр в числе: ', quantity(number))
print('Разность суммы и кол-ва цифр: ', summ(number) - quantity(number))
