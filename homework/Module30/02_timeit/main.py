import timeit
import time

# тут мы производим замер времени простым способом через модуль time
start_time = time.time()
way_comprehensions = ''.join([str(numbers) for numbers in range(100)])
end_time = time.time() - start_time
print('List comprehensions', end_time)

# тут мы производим замер времени и работу функции в одной строке
way_map: float = timeit.timeit(lambda: ''.join(map(str, range(100))),
                               number=10000)
print('Lambda функции', way_map)


if end_time > way_map:
    print('Lambda функция выполняется быстрее')
elif way_map > end_time:
    print('List comprehensions выполняется быстрее')
