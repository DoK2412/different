# список фильмов
films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон', 'Богемская рапсодия', 'Город грехов', 'Мементо', 'Отступники', 'Деревня']
# список под любимые фильмы
favorite_movies = []

# цикл на проверку и добавление фильмов
while True:
    entering_a_movie = input('Введите фильм: ')
    if entering_a_movie in films:
        favorite_movies.append(entering_a_movie)
        print('Фильм добавлен в избранные.')
        continued = input('Хотите ввести еще фильм? да/нет ')
    else:
        print('Данного фильма нет в нашей библиотеке')
        continued = input('Хотите ввести еще фильм? да/нет ')

    if continued == 'нет':
        print('Список ваших любимых фильмов: ', favorite_movies)
        break
