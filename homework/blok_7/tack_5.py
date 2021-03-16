n = int(input('Введите сколько учеников в классе: '))
three = 0
four = 0
five = 0
for number in range(1, n + 1):
  ratings = int(input('Введите оценку yченика: '))
  if ratings == 3:
    three += 1
  elif ratings == 4:
    four += 1
  elif ratings == 5:
    five += 1
if four < three > five:
  print('Троешкоков больше')
elif three < four > five:
  print('Хорошистов больше')
else:
  print('Отличноков больше')
