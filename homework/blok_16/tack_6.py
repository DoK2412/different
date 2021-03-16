# создаем 2 списка в соответствии с условием
list_1 = []
list_2 = []
# заполняем первый список
for _ in range(3):
    variable = int(input('Введите число для первого списка: '))
    list_1.append(variable)
# аполняем второй список
for _ in range(7):
    variable = int(input('Введите число для второго списка: '))
    list_2.append(variable)
# объединяем списки
list_1.extend(list_2)
# проверяем на повторения, удаляем повторы, выводим данные
for repetitions in list_1:
    while list_1.count(repetitions) > 1:
        list_1.remove(repetitions)
print('Новый первый список с уникальными элементами:', list_1)
