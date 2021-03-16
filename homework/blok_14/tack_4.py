import math


def check_the_position_of_the_point(x, y, radius):
    distance_to_the_point = math.sqrt(x ** 2 + y ** 2)
    if distance_to_the_point <= radius:
        print('Монетка где-то рядом')
    else:
        print('Монетки в области нет')


x = float(input('Введите координаты точки x: '))
y = float(input('Введите координаты точки y: '))
radius = float(input('Введите радиус: '))

check_the_position_of_the_point(x, y, radius)
