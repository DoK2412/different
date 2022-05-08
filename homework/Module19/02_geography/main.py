# создаем словарь и запрос на количество стран
countries_of_the_world = dict()
number_of_countries = int(input('Введите количество стран: '))
switch = True
# цикл на запрос стран и передачу их в словарь
for i in range(number_of_countries):
    country = input('Введите страну: ')
    cities = input('Введите 3 города из этой страны: ').split()
    countries_of_the_world[country] = cities
# цикл на запрос города от пользователя
for i in range(3):
    city = input('\n{0} город: '.format(i+1))
    # цикл для работы со словарем
    for i_city in countries_of_the_world:
        # проверка на определение страны
        if city in countries_of_the_world[i_city]:
            print(city, 'расположен в стране', i_city)
            break
    # ответ если города нигде нет
    else:
        print('По городу {0} нет данных.'.format(city))
