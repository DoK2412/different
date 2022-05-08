import math


class MyMath:
    '''
    Класс основн на работе методов принимающих напрямую значения
    не завязываясь на экземпляры класса
    '''
    # метод для подсчета длины окружности
    @classmethod
    def circumference_length(cls, radius: int) -> float:
        return (2 * math.pi) * radius

    # метод для подсчета площади окрудности
    @classmethod
    def the_area_of_the_circle(cls, radius: int) -> float:
        return math.pi * radius ** 2

    # метод для подсчета объема куба
    @classmethod
    def cube_volume(cls, side: int) -> float:
        return side ** 3

    # метод для подсчета площади поверхности сферы
    @classmethod
    def cube_area(cls, radius: int) -> float:
        return 4 * math.pi * radius ** 2

    # метод для подсчета периметра прямоугольника
    @classmethod
    def rectangle_perimeter(cls, side_1: int, side_2: int) -> int:
        return 2 * (side_1 + side_2)


res_1 = MyMath.circumference_length(radius=5)
res_2 = MyMath.the_area_of_the_circle(radius=6)
res_3 = MyMath.cube_volume(side=8)
res_4 = MyMath.cube_area(radius=4)
res_5 = MyMath.rectangle_perimeter(side_1=4, side_2=7)

print('Длина окружности: ', res_1)
print('Площадь окружности: ', res_2)
print('Объем куба: ', res_3)
print('Площадь повержности куба: ', res_4)
print('Периметр прямоугольника: ', res_5)
