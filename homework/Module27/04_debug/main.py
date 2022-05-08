import functools
from typing import Callable, Any


def debag(func: Callable) -> Callable:
    """Функция декоратор для вывода дополнительной информации"""
    @functools.wraps(func)
    def finding_errors(*args: Any, **kwargs: Any) -> None:
        """Проверяем наличие переданных аргументов
        и выводим на экран отработунное действие с заходом в функцию"""
        if kwargs and args:
            print('Вызывается {0} ("{1}", age="{2}")'
                  .format(func.__name__, *args, kwargs.get('age')))
            print("'{fun}' вернула значение: "
                  .format(fun=func.__name__), func(*args, **kwargs))
            print(func(*args, **kwargs))
            print()
        elif kwargs:
            print('Вызывается {0} (name="{1}", age="{2}")'
                  .format(func.__name__, kwargs.get('name'),
                          kwargs.get('age')))
            print("'{fun}' вернула значение: "
                  .format(fun=func.__name__), func(**kwargs))
            print(func(**kwargs))
            print()
        elif args:
            print('Вызывается {0} ("{1}")'.format(func.__name__, *args))
            print("'{fun}' вернула значение: "
                  .format(fun=func.__name__), func(*args))
            print(func(*args))
            print()

    return finding_errors


@debag
def greeting(name: Any, age=None) -> str:
    """Функция приветствие либо определения возраста
    в зависимости от количества аргументов определяется вывод
    данных"""
    if age:
        return "Ого, {name}! Тебе уже {age} лет, ты быстро растешь!"\
            .format(name=name, age=age)
    else:
        return "Привет, {name}!".format(name=name)


print(greeting.__doc__)
greeting("Том")
greeting("Миша", age=100)
greeting(name="Катя", age=16)
