salespeople = int(input('Введите количество продавцов: '))
customers = int(input('Введите количество покупателей: '))
salary = int(input('Введите зарплату продавца: '))
counting = customers / salespeople
if counting > 4:
  print('Слишком мало продавцов')
else:
  print('Продавцов достаточно')
if salary < 20000:
  salary += 2000
  print('Выша зарплата повышена на 2000 рублей')

print('Заработная плата всего персонала составляет: ', salary * salespeople)
print('Заработная плата одного продавца составляет: ', salary)
