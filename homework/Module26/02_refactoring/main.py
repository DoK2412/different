list_1 = [2, 5, 7, 10]
list_2 = [3, 8, 4, 9]
to_find = 56
# Способ № 1 "Элементарный"
'''
try:
    for x in list_1:
        for y in list_2:
            result = x * y
            print(x, y, result)
            if result == to_find:
                raise StopIteration
except StopIteration:
    pass
 '''
# Способ № 2 "Через функцию"


# генератор умножения чисел
def multiplication_of_numbers() -> int:
    for x in list_1:
        for y in list_2:
            result = x * y
            print(x, '*', y, '=', result)
            yield result


for final_value in multiplication_of_numbers():
    if final_value == to_find:
        print('Found!!!')
        break
