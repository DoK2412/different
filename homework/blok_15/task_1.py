number = int(input('Введите число: ')) # запрос числа от пользователя
list_of_numbers = [] # список для хранения данных

for i in range(number): # перебор чисел
    if i % 2 != 0: # проверка на четность
        list_of_numbers.append(i) #передача в контейнер

print(list_of_numbers) 
