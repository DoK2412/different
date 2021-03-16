a = int(input('Введите первый член прогрессии: '))
d = int(input('Введите разность: '))
n = int(input('Введите количество членов прогрессии: '))
a -= 3
counter = 0
while counter < n:
  a += d
  print(a)
  counter += 1
