import random

summ = 0
line = 0
# цикл на получение чисел обработку и запись в файл
while summ < 777:
    line += 1
    number = int(input('Введите число: '))
    summ += number
    if random.randint(1, 13) == 1 or line == 13:
        raise ValueError('Возникла ошибка, программа аварийно закрылась!')
    else:
        with open('result.txt', 'a', encoding='utf-8') as result:
            result.write(str(number) + '\n')

print('Вы набрали больше 777. Поздравляем!')

# задачу изменил условие поправил, в проверке при получении рандомного
# числа обнаружил что рандом может не выбрость нужное число (в данном случае 1)
# больше 13ти раз, поэтому на всякий случай сделал еще проверку на 13тое
# выполнение. как я понял по уловию мы должны выбрость ошибку 1 раз в
# диапазоне от 1 до 13