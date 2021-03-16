ticket = int(input('Введите число: '))
number_1 = ticket // 1000
number_2 = ticket % 1000
counter_1 = 0
counter_2 = 0
while number_1 > 0 or number_2 > 0:
  breakdown_1 = number_1 % 10
  number_1 //= 10
  breakdown_2 = number_2 % 10
  number_2 //= 10
  counter_1 += breakdown_1
  counter_2 += breakdown_2
if counter_1 == counter_2:
  print('Счастливый билет')
else:
  print('Не счастливый билет')
