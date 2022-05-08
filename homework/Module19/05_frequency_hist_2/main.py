# создаем функцию для обработки полученной строки
def inverting(user_data):
    # словари для перевода и отсеивания
    symbols = dict()
    grouping = dict()
    # цикл для подсчета букв в строке
    for i_user_data in user_data:
        symbols[i_user_data] = 0
        for i in user_data:
            if i == i_user_data:
                symbols[i_user_data] += 1
    # создаем переменную содержащую отсортированные ключи словаря
    the_keys = sorted(symbols.keys())
    # цикл для вывода оригинального словаря чистот:
    print('Оригинальный словарь частот:')
    for i in the_keys:
        for x in symbols:
            if i == x:
                print(i, ':', symbols[x])
    # цикл для определения ключей с словаре и определения вида значений
    for split in symbols.values():
        grouping[split] = []
    # цикл заспределения букв
    for x in grouping.keys():
        for i in symbols:
            if x == symbols[i]:
                grouping[x].append(i)
    return grouping
# запрос строки от пользователя
user_data = input('Введите строку: ')
# получение значения от функции
dictionary_processing = inverting(user_data)
# обработка значений и вывод данных
print('\nИнвертированный словарь частот:')
for i in dictionary_processing:
    print(i, ':', dictionary_processing[i])
