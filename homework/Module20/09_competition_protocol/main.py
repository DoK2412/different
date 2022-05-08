def player_base(protocols, game_database):

    players = dict()
    if 2 < len(protocols) > 2 or int(protocols[0]) < 0:
        print('В имени содержится пробел, либо колличество баллов отрицательно! \nВведите данные повторно.')
    # добавление результата в словарь
    elif len(protocols) <= 2 or int(protocols[0]) >= 0:
        if protocols[1] not in game_database:
            players[protocols[1]] = protocols[0]
        # смена результатов иока если бал выше
        else:
            for participant, result in game_database.items():
                if protocols[1] == participant:
                    if int(result) < int(protocols[0]):
                        players[participant] = protocols[0]
    return players


# функция для обработки списка и его реверса
def defining_a_list(game_database):

    winners = list()
    for participant, score in game_database.items():
        winners.append(list((participant, int(score))))

    return(sorted(winners, key=lambda c: c[1], reverse=True))


# вывод данных о победителях
def data_output(converting_a_list):

    while 1:  # TODO а) бесконечные циклы в питоне обычно записывают c True вместо 1; б) зачем тут вообще нужен цикл?
        if len(defining_a_list(game_database)) < 3:  # TODO используйте парамет вместо повторного вызова функции (и
                                                     #  ниже аналогично)
            print('Игроков меньше 3.')
            break
        else:
            for participant in range(len(defining_a_list(game_database))):
                if participant < 3:
                    print(f'{participant+1} место: ', defining_a_list(game_database)[participant][0], '(', defining_a_list(game_database)[participant][1], ')')
            break

# запрос игр
number_of_protocols = int(input('Сколько записей вносится в протокол? '))
print('Записи (результат и имя):')
# словарь для созранности данных
game_database = dict()
# цикл для работы с данными игр
for i in range(number_of_protocols):
    protocols = input('{0} запись: '"".format(i+1)).split()
    game_database.update(player_base(protocols, game_database))
# вызов функции для обработки словаря игроов
converting_a_list = defining_a_list(game_database)
# вызов функции для вывода победителей
data_output(converting_a_list)
