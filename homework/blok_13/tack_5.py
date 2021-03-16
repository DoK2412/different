import math

number = float(input('Точность: '))
result = 0
variable = 0
accuracy = 1

while accuracy > number:
  accuracy = 1/math.factorial(variable)
  result += accuracy
  variable += 1
print('Результат',result)
