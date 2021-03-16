def test(): # определение функции
  number = int(input('Введите число: '))
  if number > 0 :
    positive(number) #запрос функции
  else:
    negative(number) #запрос функции

def positive(number): # определение функции
  print('Число', number, 'положительно')

def negative(number): # определение функции
  print('Число', number, 'отрищательно')


test() #запрос функции
