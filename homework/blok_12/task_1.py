def the_amount(number): #работа функции
  sum_of_the_number = 0
  for checking in range(0, number + 1):
    sum_of_the_number += checking
  print('Я знаю, что сумма чисел от 1 до', number , 'равна:', sum_of_the_number)

number = int(input('Введите число: ')) #запрос числа от пользователя

the_amount(number) # запрос функции
