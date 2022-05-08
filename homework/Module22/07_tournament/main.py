import os


# даная функция обрабатывает словарь вышедших
# во второй тур и записывает данные в новый файл
def writing_to_a_file(winners):
    with open('second_tour.txt', 'w', encoding='utf-8') as on_the_record:
        on_the_record.write(str(len(winners)) + '\n')
        place = 1
        for i_points in sorted(winners.values(), reverse=True):
            for name, i_player in winners.items():
                if winners[name] == i_points:
                    on_the_record.write(str(place) + ') '+ name + ' ' + str(i_player) + '\n')
                    place += 1
        print('Файл успешно записан!')


# функция принимает данные из файла, преобразует
# их в словарь и возвращает обратно в запрос
def file_processing(data_of_participants):
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    formation_of_participants = dict()
    player = list()
    for participant in data_of_participants[1:]:
        # проверкой определяем является ли переменная числом,
        # формируем словарь из игроков и их баллов, переменная
        # player необходима для переформирования имени и фамилии участника
        if participant[0] in numbers:
            abbreviation_of_the_surname = str((player[1][0]) + '. ' + player[0])
            crutch = data_of_participants[1:].index(participant)
            formation_of_participants[abbreviation_of_the_surname] = int(participant)
            player.clear()
            continue
        player.append(participant)
    # возвращвем полученный словарь
    return(formation_of_participants)


# функция получет список из файла,
# вызывает функция для формирования словаря
# и создает новый словать для отбора прошедших во второй тур
# после чего вызывает функция на запись данных
def determining_the_winners(data_of_participants):
    winners = dict()
    # этот цикл определяет кто прошел во второй тур
    for player, points in file_processing(data_of_participants).items():
        if int(data_of_participants[0]) < points:
            winners[player] = points
    writing_to_a_file(winners)


# открываем файл на чтение и вызываем функцию
with open(os.path.abspath(os.path.join('first_tour.txt')), 'r', encoding='utf-8') as participants:
    data_of_participants = participants.read().split()
    determining_the_winners(data_of_participants)
