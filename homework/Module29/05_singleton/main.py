def singleton(cls):
    """Декаратор записывающий значение
    в словарь без возможности его перезаписи"""
    singleton_dict = dict()

    def realization(*args, **kwargs):
        if cls not in singleton_dict:
            singleton_dict[cls] = cls(*args, **kwargs)
        return singleton_dict[cls]

    return realization


@singleton
class Example:
    """Основной класс для работы"""
    def __init__(self):
        self.meaning = 1986890616688


my_obj = Example()
my_another_obj = Example()

print(id(my_obj))
print(id(my_another_obj))

print(my_obj is my_another_obj)
