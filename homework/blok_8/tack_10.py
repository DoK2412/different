
x = int(input('Введите количество мальчиков: '))
y = int(input('Введите количество девочек: '))
if x > y * 2 or y > x * 2:
  print('Решений нет')
elif x >= y:
  the_difference = x - y
  for checking_1 in range(the_difference):
    print('BGB', end=' ')
  for checking_2 in range(y - the_difference):
    print('BG', end = ' ')
elif y >= x:
  the_difference = y - x
  for checking_1 in range(the_difference):
    print('GBG', end=' ')
  for checking_2 in range(x - the_difference):
    print('GB', end = ' ')