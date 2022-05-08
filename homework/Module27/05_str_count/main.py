import functools
from typing import Callable


def counter(func: Callable) -> Callable:
    """Декоратор который считает количество отработанных раз"""
    @functools.wraps(func)
    def account_function() -> None:
        """Функция выполняет подсчет вызовов функции"""
        account_function.counter += 1
        print('Декоратор сработал: {counter} раз!'
              .format(counter=account_function.counter))
        func()

    account_function.counter = 0
    return account_function


@counter
def test() -> None:
    """Функция для выполнения определенного действия"""
    print('Привет, эта функция сработала')


# цикл для прогона функции
for i_next in range(10):
    test()
