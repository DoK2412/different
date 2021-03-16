def start_of_the_program(number_1, number_2): # работа функции
  divider = 0 # контейнер для делителя
  the_greatest_divider = 0 # контейнер для наибольшего делителя 
  defining_the_range = max(number_1, number_2) # определяем наибольшее число для создания диапазона

  for checking in range(1, defining_the_range+1): # создаем проверку по наибольшее число из введенных
    if number_1 % checking == 0 and number_2 % checking == 0: # проверка деления
      divider = checking # передаем найленный делитель  
      the_greatest_divider = max(divider, the_greatest_divider) # сверяем какой делитель больше и передаем его в контейнер

  print('Наибольший делитель: ', the_greatest_divider)


number_1 = int(input('Введите первое число: ')) #запрос первого числа
number_2 = int(input('Введите второе число: ')) #запрос второго числа

start_of_the_program(number_1, number_2) #вызов функции
