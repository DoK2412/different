import os


# функция для записи ошибок в файл
def writing_to_a_file(line, val):
    with open('error.log', 'a', encoding='utf-8') as error:
        error.write('Произошла ошибка в строке {0}. {1}.\n'
                    .format(line, str(val)))


# функция для проверки строки
def checking_characters(name_from_the_file):
    if len(name_from_the_file) < 3:
        raise ValueError('Строка не соответстует минимальным требованиям')


# функция для обработки полученного списка имен подсчета символов
def checking_names(file_processing):
    the_sum_of_characters = 0
    line = 0
    try:
        for name_from_the_file in file_processing:
            line += 1
            try:
                checking_characters(name_from_the_file)
                the_sum_of_characters += len(name_from_the_file)
            except ValueError as val:
                writing_to_a_file(line, val)
                print('Проверьте обрабатываемые данные в строке {0}'
                      .format(line))
    finally:
        print('Общее количество символов: ', the_sum_of_characters)


# открыти файла на чтение и вызов функции
with open(os.path.abspath(os.path.join('people.txt')), 'r') as name:
    file_processing = name.read().splitlines()
    checking_names(file_processing)
