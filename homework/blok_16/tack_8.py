players = int(input('Количество человек: '))
retiring = int(input('Какое число в считалке? '))
print(f'Значит выбывает каждый {retiring} человек')
list_of_players = list(range(1, players + 1))
for i in range(len(list_of_players)-1):
    print('Текущий круг людей: ', list_of_players)
    w = len(list_of_players) % retiring
    list_of_players.remove(w)
    print('Выбывает человек под номером: ', w)

print('Остался человек под номером: ', list_of_players)
