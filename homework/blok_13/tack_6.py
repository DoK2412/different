def check(number):
  second_num_count = 0
  temp = number
  while temp > 0:
    second_num_count += 1
    temp = temp // 10
  return second_num_count

def processing(meaning, number_of_numbers):
  counter = number_of_numbers
  last_digit = meaning % 10
  first_digit = meaning // 10 ** (counter - 1)
  betweenDigits = meaning % 10 ** (counter - 1) // 10
  second_n = last_digit * 10 ** (counter - 1) + betweenDigits * 10 + first_digit
  return second_n

def comparison(x, y):
  check_box = True
  if x < 3:
    print("В первом числе меньше трёх цифр.\nСумму посчитать не возможно.")
    check_box = False
  else:
    print('Изменённое первое число: ', processing(first_n, x))
  if y < 4:
    print("Во втором числе меньше четырёх цифр. \nСумму посчитать не возможно.")
    check_box = False
  else:
    print('Изменённое второе число: ', processing(second_n, y))
  
  if check_box == True:
    summ = processing(first_n, x) + processing(second_n, y)
    print('Сумма: ', summ)

first_n = int(input("Введите первое число: "))
second_n = int(input("Введите второе число: "))

numbers_in_the_first_number = check(first_n)
numbers_in_the_second_number = check(second_n)

comparison(numbers_in_the_first_number, numbers_in_the_second_number)
