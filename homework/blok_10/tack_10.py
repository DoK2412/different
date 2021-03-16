numbre = int(input('Введите число строк: '))
counter = 1
for row in range(numbre, 0, -1):
  for col in range(numbre, 0, -1):
    if col>= row:
      print(col, end='')
    elif col < row:
      print(end='.')
  for col_2 in range(1, numbre+1):
    if col_2>= row:
      print(col_2, end='')
    elif col_2 < row:
      print(end='.')
  print()
