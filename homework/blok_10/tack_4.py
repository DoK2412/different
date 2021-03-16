width = int(input('Введите длинну поля: '))
height = int(input('Введите ширину поля: '))
for checking_width in range(width):
  for checking_height in range(height):
    if checking_width == checking_height or checking_width == width - checking_height :
      print('^', end='')
    else:
      print(end=' ')
  print()
