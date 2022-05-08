# калькулятор
import functools
import sys
import time
from typing import Callable, Any


def logging(func: Callable) -> Callable:
    """Функция отслеживающая ошибки и записывающая из в лог"""
    @functools.wraps(func)
    def code_check(*args: Any) -> None:
        try:
            print('Вызывается функция {funcs}, документация функции: {doc}'
                  .format(funcs=func.__name__, doc=func.__doc__))
            func(*args)
        except Exception as error:
            print('Произошла ошибка типа: ', type(error).__name__)
            with open(
                    'function_errors.log', 'a', encoding='utf-8') \
                    as log_entry:
                log_entry.write(str(time.ctime() + ' Ошибка в функции: '
                                    + func.__name__ + ' Наименование ошибки: '
                                    + type(error).__name__ + '\n'))
    return code_check


@logging
def addition(number_1: str, number_2: str) -> None:
    """функция производит сложение чисел"""
    print('Результат: ', int(number_1) + int(number_2))


@logging
def subtraction(number_1: str, number_2: str) -> None:
    """функция производит вычитание чисел"""
    print('Результат: ', int(number_1) - int(number_2))


@logging
def multiplication(number_1: str, number_2: str) -> None:
    """функция производит умножение чисел"""
    print('Результат: ', int(number_1) * int(number_2))


@logging
def division(number_1: str, number_2: str) -> None:
    """функция производит деление чисел"""
    if number_2 == 0:
        raise ZeroDivisionError
    else:
        print('Результат: ', int(number_1) / int(number_2))

@logging
def calculator():
    """Функция запроса действия пользователя и остановки программы"""
    action = int(input('Введите необходимое действие: 1 - сложение, '
                       '2 - вычитание, 3 - умножение, 4 - деление, '
                       '5 - выход.'))
    if action == 5:
        print('Выполнение программы завершено!')
        sys.exit()
    number_1 = input('Введите первое число: ')
    number_2 = input('Введите второе число: ')

    if action == 1:
        addition(number_1, number_2)
    elif action == 2:
        subtraction(number_1, number_2)
    elif action == 3:
        multiplication(number_1, number_2)
    elif action == 4:
        division(number_1, number_2)


while True:
    calculator()
