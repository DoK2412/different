def calculator(): # работа функции
  number_1 = int(input('Введите число: '))
  action = int(input('Введите действие. 1 - сумма, 2 - максимальное число, 3 - минимальное число '))
  series_of_numbers = '' # разбитое число
  sum_of_the_number = 0 # сумма числа

  while number_1 > 0: # разбиваем число 
    cow = number_1 % 10 
    sum_of_the_number += cow # считаем сумму числа
    series_of_numbers += str(cow) # передаем значение в список
    number_1 //= 10

  if action == 1: # определение действия пользователя
    summ(sum_of_the_number) # запрос функции
  elif action == 2:
    max_number(series_of_numbers) # запрос функции
  elif action == 3:
    min_number(series_of_numbers) # запрос функции
  else:
    print('Действие не определено.')


def summ(sum_of_the_number):  # работа функции на вывод суммы
  print('Сумма чисел', sum_of_the_number)
  calculator()

def max_number(series_of_numbers): # работа функции на максимальное число
  print('Максимальное число: ', max(series_of_numbers))
  calculator()

def min_number(series_of_numbers): # работа функции не минимальное число
  print('Минимальное число: ', min(series_of_numbers))
  calculator()


calculator() # запрос функции
