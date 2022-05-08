# подключаем модуль рандома
import random
# генерируем списки в соответствии с условиями
first_team = [round(random.uniform(4, 10), 2) for _ in range(20)]
second_command = [round(random.uniform(4, 10), 2) for _ in range(20)]
tour_winners = [first_team[member] if first_team[member] > second_command[member] else second_command[member] for member in range(len(first_team))]
# выводим получившиеся данные
print('Первая команда:', first_team)
print('Вторая команда:', second_command)
print('Победители тура:', tour_winners)