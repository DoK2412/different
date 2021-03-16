def calculation(the_initial_amplitude, final_amplitude): #функция на нахождение амплитуды
  counter = 0
  the_amplitude = 0 # начальная амплитуда
  decrease = the_initial_amplitude # начальная дистанция
  while True:
    the_amplitude = decrease / 100 * 8.4 # подсчет амплитуды
    decrease -= the_amplitude # подсчет пройденного растояния
    counter += 1
    if decrease < final_amplitude: # вывод итогового результата
      print('Маятник считается остановившимся через', counter, 'колебаний')
      break


the_initial_amplitude = float(input('Введите начальную амплитуду: '))
final_amplitude = float(input('Введите конечную амплитуду: '))

calculation(the_initial_amplitude, final_amplitude) # вызов функции с переменными
