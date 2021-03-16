# запрос числа от пользователя
number = int(input('Введите число: '))
# список для хранения данных
list_of_numbers = []
# перебор чисел
for i in range(number):
    # проверка на четность
    if i % 2 != 0:
        # передача в контейнер
        list_of_numbers.append(i)

print(list_of_numbers)
