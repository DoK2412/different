import functools
from collections.abc import Callable

app = {}


def callback(a):
    def callback_decor(func: Callable) -> Callable:
        """Декоратор записывающий полученный урл и запрашивающую его функцию"""
        app[a] = func
        @functools.wraps(func)
        def function_recording(*args, **kwargs):
            return func(*args, **kwargs)
        return function_recording
    return callback_decor


@callback('//')
def example() -> str:
    """Метот возврата функции после обработки запроса"""
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'


route = app.get('//')

if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')
