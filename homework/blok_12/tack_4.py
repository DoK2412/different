def coup(number): # работа функции
  counter = 0 # контейнер под реверс
  while number > 0: 
    if number > 0: # реверс числа
      department = number % 10
      number = number // 10
      counter = counter * 10
      counter = counter + department 
  print('Число наоборот: ', counter) # вывод результата
  
    

def request(): # запрашиваем число и запускаем следующую функцию
  while True: #создаем цикл на проверку
    number = int(input("Введите целое число: "))#делаем запрос числа от пользователя
    if number == 0: # если равен нулю заканчиваем программу
      print('Программа завершена!')
      break
    coup(number) #если число не равно 0  переходим в обработку данных в следующей функции


request() # заруск программы через функцию
