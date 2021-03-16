the_amount = int(input('Введите сумму: '))
check = the_amount % 100
if the_amount == 0:
  print('Вы ввели не верную сумму.')
else:
  if check == 0:
    print('Заберите деньги')
  else:
    print('Такую сумму снять невозможно. Обратитесь в другой банкомат.')
