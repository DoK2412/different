import os


# в функции формируем путь и запрос на какой диск сохраняем
def way(text, the_path_to_the_file):
    path_conversion = the_path_to_the_file.replace(' ', '/')
    disk = input('На какой диск сохраняем: ').upper()
    file_path = str(disk + ':/' + path_conversion)
    # проверка на существование пути
    if os.path.isdir(file_path):
        name_file = input('Введите имя файла: ')
        # получаем все файлы в рабочей директории
        for data_from_the_file in os.listdir(file_path):
            # проверка сохраняемого файла на наличие в директории
            if str(name_file + '.txt') == data_from_the_file:
                # запрос на перезапись
                confirmation = input('Перезаписать файл? да\нет ')
                if confirmation == 'да':
                    with open((file_path + '/' + name_file + '.txt'), 'w') as processing:
                        processing.write(text)
                        print('Файл успешно перезаписан.')
                        break
                # отказ в сохранении
                else:
                    print('Данные не записаны.')
                    break
        # если искомого файла нет создаем его
        else:
            with open((file_path + '/' + name_file + '.txt'), 'w') as processing:
                processing.write(text)
                print('Файл успешно сохранен.')
    # вывод если пути не сушествует
    else:
        print('Такого пути не существует')

# получаем от пользователя первоначальные данные
text = input('Введите строку: ')
the_path_to_the_file = input('Куда хотите сохранить документ? \
Введите последовательность папок (через пробел):')
# запускаем функцию
way(text, the_path_to_the_file)
