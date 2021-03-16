n = int(input('Введите натуральное число'))
the_denominator = 1
the_numerator_1 = 1
summ_1 = 1
summ_2 = 1
the_decision = True

for number_1 in range(1, 7):
  the_denominator += the_denominator
  summ_1 *= n - the_denominator
  the_numerator_1 = the_denominator - 1
  summ_2 *= n - the_numerator_1
  if summ_1 == 0:
    print('Знаменатель равен нулю')
    the_decision = False
    break
  if summ_2 == 0:
    print('Числитель равен нулю')
    the_decision = False
    break
    
if the_decision == False:
  print('Решение уравнения невозможно')
if the_decision == True:
  result = summ_2 / summ_1
  print(result)
