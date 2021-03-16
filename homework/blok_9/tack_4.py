row=int(input('Введите кол-во рядов:'))
seat=int(input('Введите кол-во сидений в ряде: '))
gap=int(input('Введите кол-во метров между рядами: '))
print('\n Сцена \n')
for construction in range(seat):
  print('=' * seat, '*' * gap, '=' * seat)
