import functools
from collections.abc import Callable

user_permissions = ['admin']


def check_permission(permissions: str) -> Callable:
    def tolerance_level(func: Callable) -> Callable:
        @functools.wraps(func)
        def checking_the_possibilities():
            """Метод предназначен для проверки
            уровня доступа пользователей"""
            if permissions not in user_permissions:
                print('PermissionError: У пользователя недостаточно'
                      'прав, чтобы выполнить функцию', func.__name__)
            else:
                return func()
        return checking_the_possibilities
    return tolerance_level


@check_permission('admin')
def delete_site() -> None:
    """Метод предназначен для действий администраторов"""
    print('Удаляем сайт')


@check_permission('user_1')
def add_comment() -> None:
    """Метод предназначен для действий рядового пользователя"""
    print('Добавляем комментарий')


delete_site()
add_comment()
