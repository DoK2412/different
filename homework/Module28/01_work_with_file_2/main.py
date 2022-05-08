from typing import Optional


class File:
    '''

    Класс определяющий работу с файлами

    __init__ создает конструктор определяющие поступившие данные

    __enter__ опререляет первоначальную работу с файлом
        если файл сушествует выводит его содержимое
        если не существует то создает новый файл в режиме записи

    __exit__ завершает работу с файлом закрывая его

    '''
    def __init__(self, name: str, expansion: str) -> None:
        self.file_name = name
        self.file_expansion = expansion

    def __enter__(self):
        try:
            self.file_open = open(self.file_name, self.file_expansion,
                                  encoding='utf-8')
            print(self.file_open.read())
            return self.file_open
        except Exception:
            self.file_open = open(self.file_name, 'w', encoding='utf-8')
            self.file_open.write('Данные записаны в файл')
            return self.file_open

    def __exit__(self, exc_type, exc_val, exc_tb) -> Optional[bool]:
        # self.file_open.close()
        """ Подавляем все исключения IOError """
        if exc_type is IOError:
            self.file_open.close()
            return True
        self.file_open.close()


with File(input('Введите название файла: '), 'r') as file:
    print()
