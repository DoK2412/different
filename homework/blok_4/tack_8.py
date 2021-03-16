hours = int(input('Введите количество отработанных часов: '))
credit = int(input('Введите остаток по кредиту: '))
meal = int(input('Введите траты на еду: '))
formula = ((200 * hours) / (2**3)) + hours
if credit + meal <= formula:
  print('Часов хватает. Можно отдохнуть.')
else:
  print('Часов не хватает. Прийется поработать')
