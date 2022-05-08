violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}
# создание списка для получения продолжительности
minutes = []
number_of_songs = int(input('Сколько песен выбрать? '))
# создние цикла для запроса псен
for i in range(number_of_songs):
    # ввод песни и проверка аличия ее в словаре
    song = input('Название {0} песни: '.format(i+1))
    if song in violator_songs:
        # передача данных о песне в список
        minutes.append(violator_songs[song])
    # вывод данных если песни нет
    else:
        print('Песни {0} в списке нет.'.format(song))
# вывод итогового подсчета
print('\nОбщее время звучания песен: ', round(sum(minutes), 2), 'минут')