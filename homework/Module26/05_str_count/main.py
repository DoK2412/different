import os


# функция проверки файлов и возврата количество строк
def file_search(way) -> int:
    for file in os.listdir(way):
        print(type(file))
        if os.path.isdir(os.path.join(way, file)):
            naw_way = os.path.abspath(os.path.join(way, file))
            # получаем путь к файлу, все папки находящиеся по этому
            # пути и все файлы находящиеся в папках
            for root, dirs, files in os.walk(naw_way):
                # обрабытываем циклом списки файлов и считаем строки
                for fil_s in files:
                    if fil_s.endswith('.py'):
                        with open(os.path.join(root, fil_s), 'r',
                                  encoding='utf-8') as py_file:
                            lines_in_the_file = 0
                            # прогоняем и сортируем строки в файле
                            for line in py_file:
                                if line.startswith('#'):
                                    continue
                                elif len(line) == 1 and line.endswith('\n'):
                                    continue
                                else:
                                    lines_in_the_file += 1
                            print('Путь к файлу: {0}\nOбщее количество '
                                  'строк в файле: {1} '.format(
                                    os.path.join(root, fil_s),
                                    lines_in_the_file))
                            yield lines_in_the_file


# я вывел на 2 дерриктории назад и начал с обработки домашних всех заданий
# переменная для общего счета строки и путь к обрабатываемым файлам
total_number_of_rows = 0
way = os.path.abspath(os.path.join('..', '..'))

for lines in file_search(way):
    total_number_of_rows += lines

print('\nОбщее количество строк во всех файлах: ', total_number_of_rows)
