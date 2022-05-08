import circle
# список для хранения данных
list_of_circles = []
# цикл для создания переменных с данными
for a_circle in ['a_circle_1', 'a_circle_2']:
    a_circle = circle.Circle(
        int(input('Введите координату Х: ')),
        int(input('Введите координату У: ')),
        int(input('Введите радиу окружности: ')))
    list_of_circles.append(a_circle)
    # вывод периметра и площади
    print('Площадь окружности равена: ', a_circle.square())
    print('Периметр окружности равен: ', a_circle.perimeter())
    # запрос и вывод умеличения радиуса
    request_for_an_increase = input(
        '\nХотите ли учеличить радиус окружности? да\нет ')
    a_circle.increase(request_for_an_increase)
# вычисление растояние между центрами и сравниваем их пересечения
distance = (list_of_circles[0].x - list_of_circles[1].x) ** 2
+ (list_of_circles[0].y - list_of_circles[1].y) ** 2
print('\nОкружность пересекаются.'
      if (list_of_circles[0].r - list_of_circles[1].r
          ) ** 2 <= distance <= (list_of_circles[0].r + list_of_circles[1].r
                                 ) ** 2
      else 'Окружность не пересекается')
