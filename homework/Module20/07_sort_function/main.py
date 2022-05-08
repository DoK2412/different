# создаем функцию для работы с данными


def sorting(data):
    # зацикливаемся на поиск не целого числа
    for i in data:
        # если находим прекращаем цикл и возвращвм котреж
        if type(i) is float:
            return(data)

    # если не находим то возвращвем отсортированный по возрастанию кортеж
    else:
        return tuple(sorted(data))
# кортеж с данными
tuple_of_numbers = (3, 7, 12, 5.5, 78, 43, 9)

# вызов функции и вывод данных из нее
print(sorting(tuple_of_numbers))
