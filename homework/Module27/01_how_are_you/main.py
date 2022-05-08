import functools
from typing import Callable


def how_are_you(func: Callable) -> Callable:
    """Декоратор который всем мешает жить"""
    @functools.wraps(func)
    def annoying_function():
        """Надоедливый декоратор"""
        input('Как дела? ')
        print('А у меня не очень! Ладно, держи свою функцию.')
        func()
    return annoying_function


@how_are_you
def test() -> None:
    """Функция для выполнения определенного действия"""
    print('<Тут что-то происходит...>')


@how_are_you
def test_2() -> None:
    """Пустая функция которая просто зачем то есть"""
    print('<А тут ничего не происходит...>')


test()
# print(test.__doc__)
test_2()
# print(test_2.__doc__)
