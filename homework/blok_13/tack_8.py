danger = float(input('Ведите максимальный уровень опасности: '))
start_of_the_range = 0
the_end_of_the_range = 4

#расчет глубины
depth = ((the_end_of_the_range - start_of_the_range) / 2) + start_of_the_range
#расчет опасности
calculation_of_risk = depth ** 3 - 3 * depth ** 2 - 12 * depth + 10

#  проверяем опасность на положительность
if danger < 0:
  print('Введенное число не может быть отцательным.')
else:
  #расчет кладки
  while abs(calculation_of_risk) > danger:
    if calculation_of_risk > 0:
      start_of_the_range = depth
    else:
      the_end_of_the_range = depth
    depth = start_of_the_range + (the_end_of_the_range - start_of_the_range) / 2
    calculation_of_risk = depth ** 3 - 3 * depth ** 2 - 12 * depth + 10

  print('Приблизительная глубиа безопасной кладки: ', depth)
