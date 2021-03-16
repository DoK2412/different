
number_1 = int(input('Введите начало отрезка: '))
number_2 = int(input('Введите конец отрезка: '))
for function in range(number_1, number_2 + 1):
  y = (function ** 3) + (2 * (function ** 2)) - (4 * function) + 1
  print('В точке', function, ' функция равна', y)