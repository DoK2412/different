# список для последующей работы
friends = []
# запросы на количество пользователей и количество долговых расписок
number_of_friends = int(input('Количество друзей: '))
debt_receipts = int(input('Долговых расписок: '))
# цикл для создания пользователей в основном списке
for definition in range(number_of_friends):
    friends.append([definition + 1, 0])
# цикл для определения кто кому сколько занял
for transfers in range(debt_receipts):
    print(transfers + 1, 'расписка')
    to_whom = int(input('Кому: '))
    from_whom = int(input('От кого: '))
    how_many = int(input('Сколько: '))
    # цикл для распределения сркдств по счетам
    for distribution in friends:
        if distribution[0] == to_whom:
            distribution[1] += how_many
        elif distribution[0] == from_whom:
            distribution[1] -= how_many
# вывод данных поэлементно из списка 
for data_output in friends:
    print(data_output[0], ':', data_output[1])
