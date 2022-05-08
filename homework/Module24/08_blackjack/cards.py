import random


class Player:
    def __init__(self, name, total_points=0):
        self.name = name
        self.total_points = total_points


class Maps:

    def __init__(self, map, name, meaning=0):
        self.map = map
        self.meaning = meaning
        self.map_definition(name)

    def map_definition(self, name):
        if self.map in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
            self.meaning = self.map
        elif self.map in ['Валет', 'Дама', 'Король']:
            self.meaning = 10
        elif self.map == 'Туз':
            if Player(name).total_points >= 10:
                self.meaning = 1
            else:
                self.meaning = 11


class Gema:
    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Валет', 'Дама', 'Король', 'Туз']
    computer_arm = list()
    players_hand = list()

    def map_definition(self):
        issued_card = random.choice(Gema.deck)
        on_the_issue = Maps(issued_card, self)
        self.total_points += on_the_issue.meaning
        if self.name == 'Компьютер':
            Gema.computer_arm.append(issued_card)
            Gema.deck = list(set(Gema.deck) ^ set(Gema.computer_arm))
        else:
            Gema.players_hand.append(issued_card)
            Gema.deck = list(set(Gema.deck) ^ set(Gema.players_hand))

    def the_first_distribution(self, player_2):
        for player in [self, player_2]:
            for _ in range(2):
                Gema.map_definition(player)

    def game_progress(self, action, player_2):

        if action == 1:
            Gema.map_definition(self)
            if self.total_points > 21:
                print('{} сгорел набрав: {}\nПобедил {}'.format(
                    self.name, self.total_points, player_2.name))
                self.total_points = 0
                return 0
        elif action == 2:
            if self.total_points > player_2.total_points:
                print(
                    'Вскрываем карты:\n У {} - {}\n У {} - {}\nПобедил {}'
                    .format(self.name, self.total_points, player_2.name,
                            player_2.total_points, self.name))

            elif self.total_points < player_2.total_points:
                print(
                    'Вскрываем карты:\n У {} - {}\n У {} - {}\nПобедил {}'
                    .format(self.name, self.total_points, player_2.name,
                            player_2.total_points, player_2.name))

            elif self.total_points == player_2.total_points:
                print('Все остались при своих.')

    def processing(self, action, player):
        if action == 2:
            Gema.game_progress(self, action, player)
            return 0
        else:
            motion = Gema.game_progress(self, action, player)
            if motion == 0:
                return 0
