import random


# класс для создания родителя
class Parent:

    def __init__(self, name, age, list_of_children):
        self.name = name
        self.age = age
        self.list_of_children = list_of_children

    def info_parent(self):
        print('\nИмя: {}\nВозраст: {}\nДети: {}.'
              .format(self.name, self.age, ', '.join(self.list_of_children)))


# класс для создания детей
class Kid:

    def __init__(self, name, age):
        self.name = name
        self.age = age - random.randint(16, age-1)
        self.calmness = random.choice(['спокоен', 'не спокоен'])
        self.hunger = random.choice(['голоден', 'не голоден'])

    def feed_the_baby(self):
        self.hunger = 'не голоден'

    def calm_the_child_down(self):
        self.calmness = 'спокоен'

    def info_kid(self):
        print('\nИмя: {}\nВозраст: {}\nСпокойствие: {}\nГолод: {}'
              .format(self.name, self.age, self.calmness, self.hunger))
