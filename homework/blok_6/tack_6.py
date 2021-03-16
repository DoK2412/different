counter_1 = 0
counter_2 = 0
while True:
  x = int(input('Введите число: '))
  if x == 0:
    print('Приложение остановлено')
    break
  if 0 <= x <= 100:
    counter_1 += 1
  elif 0 >= x >= -100:
    counter_2 += 1
  else:
    print('Вы ввели не верное значение')
print('Количество положительных оценок: ', counter_1)
print('Количество отрицатеьных оценок: ', counter_2)
