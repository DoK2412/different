# функция для обработки обоих списков и преобразования их
def list_procession(list_1, list_2):
    # список для сбора данных
    final_list = list()
    # цикл для работы с обоими списками
    for index_list_1, variable_list_1 in enumerate(list_1):
        for index_list_2, variable_list_2 in enumerate(list_2):
            # сравнение индексов списков и создание отдельного значения
            if index_list_1 == index_list_2:
                concatenation_of_values = list()
                concatenation_of_values.append(variable_list_1)
                concatenation_of_values.append(variable_list_2)
                final_list.append(tuple(concatenation_of_values))
                break
    # возвращение данных из функции
    return(final_list)

list_1 = 'adcd'
list_2 = (10, 20, 30, 40)
# функция для вывода нового списка
for index in list_procession(list_1, list_2):
    print(index)


# TODO Другой вариант решения:
def shortest_sequence_range(string, tpl):
    return min(len(string), len(tpl))


string = 'abcd'
nums_tpl = (10, 20, 30, 40)
answer = ((string[i], nums_tpl[i]) for i in range(shortest_sequence_range(string, nums_tpl)))
for x in answer:
    print(x)
