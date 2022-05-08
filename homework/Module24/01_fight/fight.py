class Characters:
    # создаем основу игрокам
    def __init__(self, classification, health):
        self.classification = classification
        self.health = health

    # создаем урон от ударов
    def battle(self, enemy_lives):
        enemy_lives.health -= 20
        print('Атаковал {} у противника осталось {} хп.'
              .format(self.classification, enemy_lives.health))
        if enemy_lives.health == 0:
            print('Победил ', self.classification)