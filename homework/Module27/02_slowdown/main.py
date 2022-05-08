import time
import functools
from typing import Callable, Any


def start_delay(func: Callable) -> Callable:
    """Декоратор для приостановки времени выполнения функции"""
    @functools.wraps(func)
    def delay(*args: Any, **kwargs: Any) -> None:
        time.sleep(int(input('Введите через какое время в секундах'
                             ' запустить программу проверки: ')))
        func(*args, **kwargs)
    return delay


number = int(input('Введите число: '))


@start_delay
def parity_check(number: int) -> None:
    """Функция проверки на четность числа"""
    if number % 2 == 0:
        print('Число четное!')
    else:
        print('Число нечетное!')


parity_check(number)
# print(parity_check.__doc__)
