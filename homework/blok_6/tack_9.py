
number = int(input('Введите число: '))
counter = 1 
while True:
  if number > 7:
    print('Число больше, чем нужно. Попробуйте еще раз!')
    number = int(input('Введите число: '))
    counter += 1
  elif number < 7:
    print('Число меньше, чем нужно. Попробуйте еще раз!')
    number = int(input('Введите число: '))
    counter += 1
  elif number == 7:
    print('Поздравляю вы угадали! Число попыток', counter)
    break