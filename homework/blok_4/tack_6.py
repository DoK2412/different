player = int(input('Кубик Кости: '))
owner = int(input('Кубик Владельца: '))
if player >= owner:
  itog = player - owner
  print('Разность: ', itog)
  print('Костя платит')
else:
  itog_1 = player + owner
  print('Сумма: ', itog_1)
  print('Владелец платит')
print('Игра окончена')
