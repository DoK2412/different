class Property:
    """Создание конструктора и метода подсчета процента"""
    def __init__(self, worth):
        self.worth = worth
        self.the_tax = 0

    def tax(self):
        self.the_tax = self.worth * self.the_amount_of_tax


class Apartment(Property):
    """Класс отвечающий за налог квартиры"""
    def __init__(self, worth, the_amount_of_tax=0.005):
        super().__init__(worth)
        self.the_amount_of_tax = the_amount_of_tax
        self.tax()


class Car(Property):
    """Класс отвечающий за налог машины"""
    def __init__(self, worth, the_amount_of_tax=0.002):
        super().__init__(worth)
        self.the_amount_of_tax = the_amount_of_tax
        self.tax()


class CountryHouse(Property):
    """Класс отвечающий за налог дома"""
    def __init__(self, worth, the_amount_of_tax=0.001):
        super().__init__(worth)
        self.the_amount_of_tax = the_amount_of_tax
        self.tax()
