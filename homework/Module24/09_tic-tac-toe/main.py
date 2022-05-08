import crosses


player_1 = crosses.Player(input('Введите имя первого игрока: '), 'x')
player_2 = crosses.Player(input('Введите имя второго игрока: '), 'o')

crosses.MarkingGrid.draw_a_board(None)

win = False
motion = 0
while not win:
    for player in [player_1, player_2]:
        win = crosses.Gema.installation_in_a_square(player)
        motion += 1
        if win or motion >= 9:
            break
    if win:
        break
    else:
        if motion >= 9:
            print('Ходов больше нет!')
            break
