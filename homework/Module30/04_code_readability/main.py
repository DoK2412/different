import sympy
from typing import List

# создаем список простых чисел через filter и lambda
list_via_lambda: List[int] = \
    list(filter(lambda x: sympy.isprime(x),
                [i_number for i_number in range(0, 10000)]))
print('Простые числа через Lambda', list_via_lambda)

# создаем список простых чисел через простой цикл
list_through_a_oop: List[int] = list()
for number in range(0, 1000):
    if sympy.isprime(number):
        list_through_a_oop.append(number)
print('Простые числа через цикл', list_through_a_oop)
