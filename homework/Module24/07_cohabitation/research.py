class Human:
    # имя сытость
    def __init__(self, name, satiety=50):
        self.name = name
        self.satiety = satiety
        self.house = True


class House:
    # деньги еда
    def __init__(self, money=0, fridge=50):
        self.fridge = fridge
        self.money = money
