# class MyDict(dict):  # TODO достаточно просто наследовать встроенный класс dict
#                      # и переопределить один метод get
#     """класс для создание конструктора и возврата данных"""
#     def __init__(self):
#         self.storage = {}
#
#     def __getitem__(self, item):
#         return item

class MyDict(dict):
    def get(self, key):
        if key in self:
            value = self[key]
        else:
            value = 0
        return value
        # todo А можно в одну строку
        #  return self[key] if key in self else 0


# создание экземпляра
data = MyDict()
data[1] = 111
print(data.get(1))
print(data.get(2))

# создание цикла для работы со словарем
# while True:
#     action = input('Введите действие:\n'
#                    '1 - добавить значение в словарь;\n'
#                    '2 - вывести значение из словаря;\n'
#                    '3 - Завершить работу.\n')
#     if action == '1':
#         data.storage[input('Введите ключ значения: ')] = \
#             input('Введите значение: ')
#     elif action == '2':
#         print(data.storage.get(input('Введите ключ: '), 0))
#     elif action == '3':
#         print('Работа завершена')
#         break
#     else:
#         print('Введено не верное значение действия')
