from typing import List
from functools import reduce

floats: List[float] = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
names: List[str] = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
numbers: List[int] = [22, 33, 10, 6894, 11, 2, 1]

floats_new: List[float] = list(map(lambda number:
                                   (round(number ** 3, 3)), floats))
names_new: List[str] = list(filter(lambda word: len(word) >= 5, names))
numbers_new: int = reduce(lambda number_1, number_2:
                                    number_1 + number_2, numbers)

print(floats_new)
print(names_new)
print(numbers_new)
