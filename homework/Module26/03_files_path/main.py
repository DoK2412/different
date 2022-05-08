import os


# генератор для проверки файлов и возврата найденных файлом
def gen_files_path(way) -> str:
    for file in os.listdir(way):
        print(os.path.abspath(os.path.join(way, file)))
        yield file
        if os.path.isdir(os.path.join(way, file)):
            naw_way = os.path.abspath(os.path.join(way, file))
            yield from gen_files_path(naw_way)


# стoлкнулся с проблемой если начинать работать с корнем системы "/"
# выдает ошибку PermissionError отказ в доступе, пришлось начинать
# с основной папки в коротую записана вся система, гугленье именно
# в этой проблеме не сильно помогло, но дало понятие как поднимать
# упавший сервер...
os.chdir('/home')
way = os.getcwd()
required_data = input('введите искомый каталог/файл: ')
for data in gen_files_path(way):
    if data == required_data:
        print('Искомый каталог/файл найден.'
              '\nВыше представлены все проверенные пути.')
        break
else:
    print('Искомый каталог/файл не найден на диске.'
          '\nВыше представлены все проверенные данные.')
