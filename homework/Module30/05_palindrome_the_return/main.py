import collections
from typing import Dict
from functools import reduce


def can_be_poly(lis: str) -> bool:
    """Функция создает словарь и после проверки количество букв возвращает
     результат возможности полиндрома"""
    ist_items: Dict = collections.Counter(lis)
    parity_check: int = reduce(lambda counter, quantity:
                               counter + (ist_items[quantity] % 2 != 0),
                               ist_items, 0)
    if parity_check > 1:
        return False
    else:
        return True


print(can_be_poly('ababc'))
print(can_be_poly('abbbc'))
