import cards
import random

artificial_opponent = cards.Player('Компьютер')
real_player = cards.Player(input('Введите имя игрока: '))


cards.Gema.the_first_distribution(artificial_opponent, real_player)


while True:
    print('В руке', cards.Gema.players_hand)
    print('1. Еще карту.\n2. Остановиться.')
    action = int(input('Введите действие:'))

    end_1 = cards.Gema.processing(real_player, action, artificial_opponent)
    if end_1 == 0:
        break

    computer_actions = random.randint(1, 2)
    end_2 = cards.Gema.processing(artificial_opponent, computer_actions,
                                  real_player)
    if end_2 == 0:
        break
