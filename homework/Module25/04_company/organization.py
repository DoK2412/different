class Person:
    """Класс для создание объектов и передачи их данных"""
    def __init__(self, name, surname, age):
        self.__name = name
        self.__surname = surname
        self.__age = age

    def get_name(self):
        return self.__name

    def get_surname(self):
        return self.__surname

    def get_age(self):
        return self.__age


class Employee(Person):
    """Базовый класс для всех рабочих"""
    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)

    def wages(self):
        return 0


class Manager(Employee):
    """работа с менеджерами"""
    def __init__(self, name, surname, age, salary=13000):
        super().__init__(name, surname, age)
        self.salary = salary

    def wages(self):
        return self.salary

    def __str__(self):
        x = self.get_name(), 'получает', str(Manager.wages(self))
        return str(' '.join(x))


class Agent(Employee):
    """работа с агентами"""
    def __init__(self, name, surname, age, sales_volume=0):
        super().__init__(name, surname, age)
        self.sales_volume = sales_volume

    def wages(self):
        payment = 5000 + (self.sales_volume / 100 * 5)
        return payment

    def __str__(self):
        x = self.get_name(), 'получает', str(int(Agent.wages(self)))
        return str(' '.join(x))


class Worker(Employee):
    """работа с простыми работниками"""
    def __init__(self, name, surname, age, watch=0):
        super().__init__(name, surname, age)
        self.watch = watch

    def wages(self):
        payment = 100 * self.watch
        return payment

    def __str__(self):
        x = self.get_name(), 'получает', str(Worker.wages(self))
        return str(' '.join(x))
