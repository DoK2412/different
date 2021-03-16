n = int(input('Введите число для математической прогрессии: '))
counter = 0
for number in range(0, n+1):
  x = (1 ** number) * (1 / (2 ** number))

  if number % 2 == 0:
    counter += x
    print('Степень:', number, counter)
  elif number % 2 != 0: 
    counter -= x
    print('Степень:', number, counter)

print('Итог суммы математического ряда до: ',number, counter)
