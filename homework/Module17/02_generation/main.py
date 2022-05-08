# запрашиваем данные у пользоваеля
number = int(input('Введите длину списка: '))
# создаем список с проверками на передачу
list_of_numbers = [1 if check % 2 == 0 else check % 5 for check in range(number)]
#  выводим данные
print('Результат: ', list_of_numbers)