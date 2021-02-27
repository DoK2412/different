films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон', 'Богемская рапсодия', 'Город грехов', 'Мементо', 'Отступники', 'Деревня'] # список фильмов
favorite_movies = [] # список под любимые фильмы


while True:
    entering_a_movie = input('Введите фильм: ')
    if entering_a_movie in films:
        favorite_movies.append(entering_a_movie)
        print('Фильм добавлен в избранные.')
        continued = input('Хотите ввести еще фильм? да/нет ')
    else:
        print('Данного фильма нет в нашей библиотеке')
        continued = input('Хотите ввести еще фильм? да/нет ')

    if continued == 'нет' or 'Нет':
        print('Список ваших любимых фильмов: ', favorite_movies)
        break
