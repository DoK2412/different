# запрос количества
orders = int(input('Введите количество заказов: '))
# создаем словарь для обработки первоначальных данных
sorting_the_list = dict()
# создаем словарь для сортировки и обработки данных
sorting_a_dictionary = dict()
# цикл для ввода заказов
for i_orders in range(1, orders + 1):
    customers = input('{0} заказ: '.format(i_orders)).split()
    # распределение значений по ключам
    if customers[0] not in sorting_the_list.keys():
        sorting_the_list[customers[0]] = [customers[1:]]
    elif customers[0] in sorting_the_list.keys():
        sorting_the_list[customers[0]].append(customers[1:])
# отсеивание повторяющихся значений из основного словаря
for key in sorting_the_list:
    if key not in sorting_a_dictionary.keys():
        sorting_a_dictionary[key] = set()
        for value in sorting_the_list[key]:
            sorting_a_dictionary[key].add(value[0])
# обработка отсортированного списка
for key_sorting_a_dictionary in sorting_a_dictionary:
    print(key_sorting_a_dictionary, ':')
    # получение значений из словаря
    for value_key_dictionary in sorting_a_dictionary[key_sorting_a_dictionary]:
        # счетчик под счет одинаковых заказов
        amount_of_orders = 0
        # обработка основного словаря
        for key_sorting_the_list in sorting_the_list:
            # получение значений из словаря
            for valye_sorting_the_list in sorting_the_list[key_sorting_the_list]:
                # сравнение значений обоих словарей, при схожести
                # передают данные в счетчик и при необходимости суммируются
                if value_key_dictionary == valye_sorting_the_list[0]:
                    amount_of_orders += int(valye_sorting_the_list[1])
        # вывод итогового результата
        print('\t {0} : {1}'.format(value_key_dictionary, amount_of_orders))
