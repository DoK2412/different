def calculating_math_func(data):
    cache = dict()
    if data in cache:
        result = cache[data]
    else:
        result = 1
        for index in range(1, data + 1):
            result *= index
    result /= data ** 3
    result = result ** 10
    cache[data] = result

    return cache[data]


number = int(input('Введите число: '))
print(calculating_math_func(number))

# зачтено
