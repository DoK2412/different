counter = 0
the_increase = 0
for number in range(1, 10):
  n = int(input('Введите заработную плату: '))
  if counter < n:
    the_increase += 1
  counter = n
print('В', the_increase, 'из 10 месяцев Ваша зарплата увеличивалась в сравнении от преведущей')
