# запрашиваем у пользователя сдвиг знака
shift = int(input('Введите сдвиг чисел: '))
list_of_numbers = ['1', '2', '3', '4', '5',]


list_of_numbers = list_of_numbers[-shift:] + list_of_numbers[:-shift]

print(list_of_numbers)

