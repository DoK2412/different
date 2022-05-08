class Player:
    def __init__(self, name, sign):
        self.name = name
        self.sign = sign


class Gema:
    list_of_cells = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def installation_in_a_square(self):
        correct_input = False
        while not correct_input:
            try:
                cell = int(input('{0} укажите клетку: '.format(self.name)))
            except TypeError:
                print('Вы не ввели значение, либо ввели его не верно.')
                continue
            if 1 <= cell < 10:
                if str(Gema.list_of_cells[cell-1]) not in 'xo':
                    Gema.list_of_cells[cell-1] = self.sign
                    correct_input = True
                else:
                    print('Клетка уже занята')
            else:
                print('Вы введи неверную клетку!')

        MarkingGrid.draw_a_board(Gema.list_of_cells)
        win = Winner.checking_the_victory(self)
        return win


class MarkingGrid:

    def draw_a_board(self):
        print('_'*25)
        for i in range(3):
            print('|', ' ' * 5, '|', ' ' * 5, '|', ' ' * 5, '|', ' ' * 5)
            print('|', ' ', Gema.list_of_cells[0+i*3], ' ', '|',
                  ' ', Gema.list_of_cells[1+i*3], ' ',
                  '|', ' ', Gema.list_of_cells[2+i*3], ' ', '|')
            print('|', ' ' * 5, '|', ' ' * 5, '|', ' ' * 5, '|', ' ' * 5)
            print('_' * 25)


class Winner:
    def checking_the_victory(self):
        victory_options = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                           (0, 4, 8), (2, 4, 6), (0, 3, 6),
                           (1, 4, 7), (2, 5, 8)]
        for win in victory_options:
            if Gema.list_of_cells[win[0]] == \
                    Gema.list_of_cells[win[1]] == \
                    Gema.list_of_cells[win[2]]:
                print('Победил: ', self.name)
                win = True
                return win
