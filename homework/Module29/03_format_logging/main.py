import time
import sys
import functools
from collections.abc import Callable
from typing import Any, Dict


def determination_time_arg(name_met: str) -> Callable:
    """Декоратор производит расчет времени работы
    метода и выводит результат пользователю"""

    def determination_time(func: Callable) -> Callable:
        @functools.wraps(func)
        def tim(*args: Any, **kwargs: Dict[str, Any]) -> Callable:
            print("Запускается '{}.{}'. Дата и время запуска: {} "
                  .format(name_met, func.__name__,
                          time.strftime('%b %d %Y - %H:%M:%S')))
            time_start = time.time()
            result = func(*args, **kwargs)
            time_stop = round(time.time() - time_start, 2)
            print('Завершение {}, время работы: {}'
                  .format(func.__name__, time_stop))
            return result
        return tim
    return determination_time


def log_methods(time_format: str):
    """Декоратор работает с методами экземпляра класса
    отсеивает магические методы и декорирует созданные"""
    if time_format in ["b d Y - H:M:S"]:
        def decorats(cls):
            for method in dir(cls):
                if method.startswith('__'):
                    continue
                else:
                    method_conversion = getattr(cls, method)
                    decorator_method = determination_time_arg(
                        name_met=cls.__name__)(method_conversion)
                    setattr(cls, method, decorator_method)
            return cls
        return decorats
    else:
        print('Формат даты указан не верно!')
        sys.exit()


@log_methods("b d Y - H:M:S")
class A:
    """Родительный класс"""
    def test_sum_1(self) -> int:
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


@log_methods("b d Y - H:M:S")
class B(A):
    """Дочерний класс"""
    def test_sum_1(self):
        super().test_sum_1()
        print("Наследник test sum 1")

    def test_sum_2(self):
        print("Наследник test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()
