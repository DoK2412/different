n = int(input('Введите число: '))
counter = 1
for number in range(1, n + 1):
  counter *= number
print('Факториал числа', n, 'равен', counter)
