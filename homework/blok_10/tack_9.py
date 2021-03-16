numbre = int(input('Введите число: '))
counter = 1
for row in range(1, numbre+1):
  for col in range(1, row+1):
    print(counter , end='\t')
    counter += 2
  print()
