number = input('Введите экспоненциальную форму числа: ')#получаем экспоненциальную форму числа
#Создаем два контейнера для значений
mantissa_number = ''
order_number = ''
#находим мантиссу
for mantissa in number:
  if mantissa != 'e':
    mantissa_number += mantissa
  else:
    break
#находим порядок
for order in number[::-1]:
  if order != 'e':
    order_number += order
  else:
    break

#выводим мантису и порядок
print('Мантисса числа',mantissa_number)
print('Полядок числа',order_number[::-1])

