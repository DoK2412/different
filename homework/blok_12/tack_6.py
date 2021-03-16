def calculation (number_1, number_2): # работа функции
  if (-1 <= number_1 <= 1) and (-1 <= number_2 <=1):
    print('Монетка где то рядом')
  else:
    print('Минетки в области нет')

number_1 = float(input('Введите первую координату Х: ')) # запрос первого числа
number_2 = float(input('Введите первую координату У: ')) # запрос второго числа

calculation (number_1, number_2) #вызов функции и передача в нее 2х переменных
