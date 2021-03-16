experience = int(input('Введите количество опыта: '))
if experience > 0 and experience < 1000:
  print('Ваш уровень 1')
elif experience > 1000 and experience < 2500:
  print('Ваш уровень 2')
elif experience > 2500 and experience < 5000:
  print('Ваш уровень 3')
elif experience > 5000:
  print('Ваш уровень 4')
else:
  print('Вы ввели ошибочное значение')
