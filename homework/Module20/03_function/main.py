# функуия на обработку запроса
def processing_a_tuple(user_data, element):
    # кртеж для работы
    processed_tuple = tuple()
    # цикл для проверки наличия значения в кортеже
    for i_user_data in user_data:
        # проверка на наличие если нет возвращваем пустой кортеж
        if element not in user_data:
            print('Данного элемента нет в кортеже!')
            return processed_tuple
        # если находим элемент начинаем создавать новый кортеж
        elif element == i_user_data:
            one_meaning = user_data[user_data.index(i_user_data):]
            # проверем если значений в кортеже больше 1
            if user_data.count(element) > 1:
                # то запускаем цикл на поиск второго значени
                for i_one_meaning in one_meaning[1:]:
                    # когда находим создаем новый срез и прекращаем цикл
                    if element == i_one_meaning:
                        two_meanings = one_meaning[:one_meaning[1:].index(i_one_meaning)+2]
                        processed_tuple += two_meanings
                        return processed_tuple
            # если элемент только 1 то возвращаем значение полученного среза
            processed_tuple += one_meaning
            return processed_tuple

# запрос данных от пользователя
user_data = tuple(input('Введите данные: '))
element = input('Введите элемент: ')

# запрос функции и вывод возвратного значения
print(processing_a_tuple(user_data, element))
