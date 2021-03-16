import math
precision = float(input('Введите точность: '))
number = float(input('Введите число: '))
result = 0 #результат
counter = 0 #переменная под числитель и знаменатель
decision = 1 #итог решения формулы
degree_per_sign = 0 #контейнер для знака
while abs(decision) >= precision:
    decision = ((-1) ** degree_per_sign) * ((number ** counter) / math.factorial(counter)) 
    result += decision
    counter += 2 
    degree_per_sign += 1	
print('Сумма ряда:', result)
