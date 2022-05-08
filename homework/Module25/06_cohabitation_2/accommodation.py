import random


class ResultsForTheYear:
    """Подсчет годового проживания и вывод даных"""
    def __init__(self, money=0, peoples_food=0, cat_food=0, fur_coat=0):
        self.money = money
        self.peoples_food = peoples_food
        self.cat_food = cat_food
        self.fur_coat = fur_coat

    def __str__(self):
        return 'Заработано денег: ' + str(self.money) + \
               ' съедено еды людьми: ' + str(self.peoples_food) + \
               ' съедено еды котом: ' + str(self.cat_food) + \
               ' куплено шуб: ' + str(self.fur_coat)


class People:
    """Общий класс для людей и одинауовых действий"""
    def __init__(self, name, satiety=30, happiness=100):
        self.name = name
        self.satiety = satiety
        self.happiness = happiness

    def petting_the_cat(self):
        self.happiness += 5
        self.satiety -= 10

    def to_eat(self, house, result):
        get_some_food = random.randint(0, 30)
        self.satiety += get_some_food
        house.peoples_food -= get_some_food
        result.peoples_food += get_some_food


class Husband(People):
    """Действия мужа"""
    def __init__(self, name):
        super().__init__(name)

    def game(self):
        self.happiness += 20
        self.satiety -= 10

    def work(self, house, result):
        house.money += 150
        result.money += 150
        self.satiety -= 10

    def __str__(self):
        return 'имя: ' + self.name + ' голод: ' + str(self.satiety) \
               + ' счастье: ' + str(self.happiness)


class Wife(People):
    """Действия жены"""
    def __init__(self, name):
        super().__init__(name)

    def buying_a_fur_coat(self, house, result):
        house.money -= 350
        self.happiness += 60
        result.fur_coat += 1

    def cleaning(self, house):
        cleaning_volume = random.randint(50, 100)
        house.dirt -= cleaning_volume
        self.satiety -= 10

    def buying_food(self, house):
        house.peoples_food += 50
        house.cat_food += 20
        house.money -= 70

    def __str__(self):
        return 'имя: ' + self.name + ' голод: ' + str(self.satiety) + \
               ' счастье: ' + str(self.happiness)


class Cat:
    """Действия кота"""
    def __init__(self, name, satiety=30):
        self.name = name
        self.satiety = satiety

    def eat(self, house, result):
        get_some_food = random.randint(5, 10)
        self.satiety += get_some_food * 2
        house.cat_food -= get_some_food
        result.cat_food += get_some_food

    def sleep(self):
        self.satiety -= 10

    def tear_up_the_wallpaper(self, house):
        house.dirt += 5

    def __str__(self):
        return 'имя: ' + self.name + ' голод: ' + str(self.satiety)


class House:
    """Создание параметров дома"""
    def __init__(self, money=100, peoples_food=50, cat_food=30, dirt=0):
        self.money = money
        self.peoples_food = peoples_food
        self.cat_food = cat_food
        self.dirt = dirt

    def __str__(self):
        return 'деньги: ' + str(self.money) + ' еда людей: ' + \
               str(self.peoples_food) + ' еда кота: ' + str(self.cat_food) \
               + ' грязь: ' + str(self.dirt)
