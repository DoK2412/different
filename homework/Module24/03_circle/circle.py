import math


class Circle:

    def __init__(self, x=0, y=0, r=1):
        self.x = x
        self.y = y
        self.r = r

    # вычисление периметра
    def square(self):
        self.s = math.pi * (self.r ** 2)
        return self.s

    # вычисление площади
    def perimeter(self):
        self.p = 2 * math.pi * self.r
        return self.p

    # запрос на увеличение радиуса и вывод новых даных
    def increase(self, request_for_an_increase):
        if request_for_an_increase.lower() == 'да':
            new_radius = int(input(
                'Введите во сколько раз увеличится радиус окружности: '))
            self.r *= new_radius
            print('\nНовый радиус окружности равен: ', self.r)
            print('Новая площадь окружности равена: ', Circle.square(self))
            print('Новый периметр окружности равен: ',
                  Circle.perimeter(self), '\n')

        else:
            print('Радиус окружности не изменен.\n')
