import random
# подключаем свой модуль
import fight


character_1 = fight.Characters(input('Введите имя первого персонажа: '), 100)
character_2 = fight.Characters(input('Введите имя второго персонажа: '), 100)
name = ['character_1', 'character_2']

# создаем бесконечный цикл боя
while character_1.health > 0 and character_2.health > 0:
    # выбираем кто будет наносить удар
    the_blow_strikes = random.choice(name)

    if the_blow_strikes == 'character_1':
        character_1.battle(character_2)
    else:
        character_2.battle(character_1)