class Student:

    # создаем базу
    def __init__(self, surname, name, patronymic, group, academic_performance=0):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.group = group
        self.academic_performance = academic_performance
        self.arithmetic_mean()

    # метод определения среднего балла
    def arithmetic_mean(self):
        counting = list(map(int, self.academic_performance))
        result = sum(counting) / len(self.academic_performance)
        self.academic_performance = round(result, 1)

    # выводим данные при запросе
    def info_students(self):
        print('\n{} {} {} \nГруппа: {} \nСредний балл: {} \n\n'
              .format(self.surname, self.name, self.patronymic,
                      self.group, self.academic_performance))