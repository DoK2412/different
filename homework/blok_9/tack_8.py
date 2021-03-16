string=int(input('Введите длину строки: '))
signs=int(input('Введите количество восклицательных знаков: '))

wave='~'
middle=0
center=string - signs

for number in range(center):
  middle= center // 2
  if number == middle:
    print('!'*signs, end='')
  print(wave, end='')

