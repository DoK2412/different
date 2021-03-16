import math #подключаем библиотеку для работы с формулами

number_of_cycles = int(input('Введите количество чисел: ')) # получаем количество циклов
for checks in range(number_of_cycles): # создаем проверку

  number = float(input('Введите число: ')) # получаем число от пользователя

  if number > 0: # создаем проверку числа больше 0
    rounding = math.ceil(number) # округляем число вверх
    logarithm = math.log(rounding) # получаем натуральный логорифм
    print('x =', rounding , '\t log(x) =', logarithm) # вывод даных

  elif number < 0: # проверка числа меньше 0
    rounding = math.floor(number) # округляем число вних
    exhibitor = math.exp(rounding) # получаем экспоненту 
    print('x =', rounding , '\t exp(x) =', exhibitor) # вывод данных
