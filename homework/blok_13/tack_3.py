
def reverse(number):
  counter = 0
  while number > 0:
    remains = number % 10
    number = number // 10
    counter = counter * 10
    counter = counter + remains
  return counter


number_1 = int(input('Введите первое число: '))
number_2 = int(input('Введите второе число: '))

print('\nПервое число наоборот', reverse(number_1))
print('Второе число наоборот', reverse(number_2))

summ = number_1 + number_2
print('Сумма: ', reverse(summ))
print('\nСумма наоборот: ',summ)