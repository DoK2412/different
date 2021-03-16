n = int(input('Введите число бакторий: '))
a = int(input('Стартовая температура в первой пробирке: '))
b = int(input('Конечная температура в первой пробирке: '))
population_1 = 1
result_1 = 1
for test_tube_1 in range(a, b + 1):
  population_1 *= test_tube_1
  result_1 = population_1 * n
print('Популяция в первой пробирке: ', result_1)
c = int(input('Стартовая температура во второй пробирке: '))
d = int(input('Конечная температура во второй пробирке: '))
population_2 = 1
result_2 = 1
for test_tube_2 in range(c, d + 1):
  population_2 *= test_tube_2
  result_2 = population_2 * n
print('Популяция вo второй пробирке: ', result_2)
if result_1 > result_2:
  print('Разность популяции: ',result_1 - result_2)
elif result_1 < result_2:
  print('Разность популяции: ',result_2 - result_1)
