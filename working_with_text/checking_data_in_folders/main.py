import os


# создаем переменные для повсчета
subdirectories, files, size = 0, 0, 0
# получаем путь к проверяемому файлу глубоко не лезам работаем в даноныи каталоге
blok = os.path.abspath(os.path.join('../..'))
# цикл на сбор данных из каталога
for catalog in os.listdir(blok):
    if os.path.isdir(os.path.join(blok, catalog)):
        for file in os.listdir(os.path.join(blok, catalog)):
            if os.path.isfile(file):
                size += os.path.getsize(file)
                files += 1
        subdirectories += 1

# результат работы программы
print('Размер каталога (в Кб): ', size / 1024)
print('Количество подкаталогов: ', subdirectories)
print('Количество файлов: ', files)
