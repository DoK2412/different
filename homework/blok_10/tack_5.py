start_of_verification = int(input('Введите конец диапазона проверки: '))
counter = 0
while start_of_verification < 0:
  print('Вы ввели отрицательное число.')
  break
for checking in range(2, start_of_verification + 1):
  for i in range(2, checking):
    if checking % i == 0:
      break
  else:
    counter +=1  
print(counter, 'простых чисел')
