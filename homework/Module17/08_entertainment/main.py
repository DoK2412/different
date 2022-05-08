import random

chopsticks = ['I' for _ in range(int(input('Введите количество палок: ')))]

for attempt in range(int(input('Введите количество бросков: '))):
    number_1 = random.randint(1, len(chopsticks))
    number_2 = random.randint(number_1, len(chopsticks))
    print(f'Бросок {attempt + 1}. Сбиты палки с номера {number_1} по номер {number_2}')

    for i in range(number_1 - 1, number_2):
        chopsticks[i] = '.'

print(' '.join(chopsticks))
