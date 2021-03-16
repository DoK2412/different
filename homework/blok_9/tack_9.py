employment=input('Введите в какоих загонах есть коровы, всего их 10. a - свободно b - занято ')
liters = 0
summ = 0
counter = 0
for paddocks in employment:
  counter += 1 
  if paddocks == 'b':
    liters = counter * 2
    summ += liters
  else:
    print(end='')
print('Всего собрано молока: ', summ)
