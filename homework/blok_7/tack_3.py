
n = int(input('Введите натуральное число: '))
for number in range(100, 999):
  variable_1 = number % 10
  variable_2 = (number // 10) % 10
  variable_3 = (number // 100) % 10
  result = variable_1 + variable_2 + variable_3
  if result == n:
    print('Подходящее число ', number)