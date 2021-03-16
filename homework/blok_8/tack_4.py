number_1 = int(input('Введите начало отрезка: '))
number_2 = int(input('Введите конец отрезка: '))
steep = int(input('Введите шаг: '))
for function in range(number_2, number_1 - 1, steep):
  y = (function ** 3) + (2 * (function ** 2)) - (4 * function) + 1
  print('В точке', function, ' функция равна', y)
