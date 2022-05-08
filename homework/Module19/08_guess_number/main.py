# подключаем модуль рандом для создания случайного числа
import random


# преобразуем полученые данные от пользователя в мнжество
def converting_numbers(request_for_numbers):
    converting_to_a_number = set()
    for i in request_for_numbers:
        converting_to_a_number.add(int(i))
    return converting_to_a_number
# получаем данные от пользователя генерируем множетство и случайное число
number = int(input('Введите максимальное число: '))
numeric_range = set([i for i in range(1, number)])
the_hidden_number = random.randint(1, number)
# создаем цикл для обработки данных
while 1:
    request_for_numbers = input('Нужное число есть среди вот этих чисел: ').split()
    # проверяем запрос на необходимость помощи
    if request_for_numbers[0] != 'Помогите!':
        checking_the_list = converting_numbers(request_for_numbers)
    # создаем проверку на количество значений в множестве
    # и проверку на верность
    if len(checking_the_list) <= 1:
        if the_hidden_number == list(checking_the_list)[0]:
            print('Вы угадали число!')
            break
    # создаем проверку на отсеивание чисел из множества
    if request_for_numbers[0] == 'Помогите!':
        print('Артём мог загадать следующие числа: ', list(checking_the_list))
    elif the_hidden_number not in checking_the_list:
        numeric_range = numeric_range.difference(checking_the_list)
        print('Ответ Артёма: Нет')
    else:
        numeric_range = numeric_range.intersection(checking_the_list)
        print('Ответ Артёма: Да')
