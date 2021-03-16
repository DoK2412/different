string=input('Введите строку: ')
the_letters=''
counter_1=0
counter_2=0
for checking in string:
  the_letters=checking
  if the_letters != ' ':
    counter_1+=1
  if counter_1 > counter_2:
      counter_2=counter_1
  if the_letters == ' ':
      counter_1=0
if counter_1 > counter_2:
  print('Длина самого длинного слова: ', counter_1)
else:
  print('Длина самого длинного слова: ', counter_2)
