from typing import List, Any

strings: List[str] = ['a', 'b', 'c', 'd', 'e']
numbers: List[int] = [1, 2, 3, 4, 5, 6, 7, 8]

# обрабатываем оба списка через функцию map
results: List[Any] = list(map(lambda strings_new, numbers_new:
                              (strings_new, numbers_new), strings, numbers))
print(results)
