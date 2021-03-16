guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
# запускаем постоянный цикл
while True:
    # выводим список кто на вечеринке запрос о дальнейшем действии
    # и проверку на остановку цикла
    print(f'Сейчас на вечеринке {len(guests)} человек: ', guests)
    question = input('Гость пришел или ушел? ')
    if question == 'Пора спать':
        print('Вечеринка закончилась, все легли спать.')
        break
    name = input('Имя гостя: ')
    # проверка на добавление, удаление или отказ
    if question == 'пришел':
        if len(guests) >= 6:
            print(f'Прости, {name}, но мест нет.\n')
            continue
        elif len(guests) < 6:
            guests.append(name)
            print(f'Привет,  {name}!\n')
    elif question == 'ушел':
        guests.remove(name)
        print(f'Пока, {name}!\n')
