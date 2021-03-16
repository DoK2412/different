
a = int(input('Введите число: '))
b = int(input('Введите число: '))
c = int(input('Введите число: '))
d = int(input('Введите число: '))

for number in range(a, b):
  if number % d == c:
    print('Вывод: ', number)