import research
import random

# содаем двух людей и дом
human_1 = research.Human(input('Введите имя человека: '))
human_2 = research.Human(input('Введите имя человека: '))
house = research.House()
day = 1

# создаем цикл на прогон года
while day <= 365:
    print('\nДень: ', day)
    # пверяем все ли живы
    if human_1.satiety < 0:
        print(human_1.name, 'умер. \nЭксперемент окончен.')
        break
    elif human_2.satiety < 0:
        print(human_2.name, 'умер. \nЭксперемент окончен.')
        break
    else:
        # еи все живы реализуем действие персонажа.
        for name in (human_1, human_2):
            number = random.randint(1, 6)
            if name.satiety < 20 and house.fridge >= 10:
                name.satiety += 10
                house.fridge -= 10
            elif house.fridge < 10:
                house.fridge += 10
                house.money -= 10
            elif house.money < 50:
                name.satiety -= 10
                house.money += 10
            elif number == 1:
                name.satiety -= 10
                house.money += 10
            elif number == 2:
                name.satiety += 10
                house.fridge -= 10
            else:
                name.satiety -= 10

            print(name.name, 'Еды {0} Денег {1} Сытость {2}'
                  .format(house.fridge, house.money, name.satiety))
    day += 1
