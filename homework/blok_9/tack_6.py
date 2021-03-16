string=input('Введите строку: ')
the_sequence=''
counter=0
counter_1=0
for checking in string:
  if checking == 's' or checking == 'S':
    counter+=1
  elif checking != 's' or checking != 'S':
    if counter > counter_1:
      counter_1=counter
    counter=0
  else:
    the_sequence == checking
if counter > counter_1:
  print('Самая длинная последовательность: ', counter)
else:
  print('Самая длинная последовательность: ', counter_1)
