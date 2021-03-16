width = int(input('Введите высоту квадрата: '))
height = int(input('Введите ширину квадрата: '))


for row in range(width):
  for col in range(height+2):

    
    if col == 0 or col == height + 1:
      print('|', end='')
    elif row == 0 or row == width -1:
      print('-', end='')
    else:
      print(end=' ')
  print()
