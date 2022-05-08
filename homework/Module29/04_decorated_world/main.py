import functools
from typing import Callable, Any


class DecoratorWithArgsForAnyDecorator:
    """Декоратор класс для работы с другими декораторами"""
    def __init__(self, func) -> None:
        functools.update_wrapper(self, func)
        self.func = func

    def __call__(self, *args, **kwargs) -> Any:
        print('Переданные арги и кварги в декоратор: ', *args, **kwargs)
        self.func(*args, **kwargs)
        return self.func(*args, **kwargs)


@DecoratorWithArgsForAnyDecorator
def decorated_decorator(*args, **kwargs) -> Callable:
    """Декоратор для какого то действия
    в нашем случае принимает аргументы и декорируется
    декоратором-классом"""
    def calling_decarator(func: Callable, ) -> Callable:
        @functools.wraps(func)
        def calling(*args, **kwargs):
            func(*args, **kwargs)
        return calling
    return calling_decarator


# декорируемая функция вывода данных
@decorated_decorator(100, 'рублей', 200, 'друзей', 300, 'трактористов')
def decorated_function(text: str, num: int) -> None:
    print("Привет", text, num)


decorated_function("Юзер", 101)
