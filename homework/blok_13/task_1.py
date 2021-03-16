def whole(number): #работаем с числом если порядок отрицательный
  counter_1 = 0
  while number > 0:
    number //= 10
    counter_1 += 1
  return counter_1

def counting_zeros(number): #работаем с числом если порядок положительный
  counter_2 = 0
  checking_for_zeros = str(number)
  for i in checking_for_zeros:
    if i == '0':
      counter_2 += 1
  return counter_2

number = float(input('Введите число: '))

if number >= 1: # сравнимаем числа, отправляем на обработку в соответствии со значением числа
  counter_1 = whole(number)
  print('Формат плавающей точки: x =', number / 10 ** (counter_1 - 1), '* 10 **', counter_1 - 1)
elif number <= 1 and number >= 0:
  counter_2 = counting_zeros(number)
  print('Формат плавающей точки: x =', number * 10 ** counter_2, '* 10 ** -', counter_2)
else:
  print('Число не распознано корректно')
