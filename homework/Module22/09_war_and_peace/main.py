import os
import zipfile


# получаем словать с посчитанными буквами, сортируе
# значения, записываем их в файл
def sorting_letters(letter_storage):
    with open('the_final_result.txt', 'w', encoding='utf=8') as on_the_record:
        for number_of_letters in sorted(letter_storage.values(), reverse=True):
            for i_letter, values in letter_storage.items():
                if number_of_letters == values:
                    on_the_record.write(i_letter + ' - ' + str(number_of_letters) + '\n')
    print('Подсчет окончен. Сформитрован файл \
с результатом "the_final_result.txt"')


# берем все знаки как исключения, а буквы помещаем в словарь
# с вызовом функции на запись
def text_filtering(text):
    punctuation_marks = ['!', '@', '#', '$', '%', '^', '&', '*', '(',
                         ')', '"', '№', ';', ':', '?', '-', '_', '=',
                         '+', '.', ',', '\\', '/', '|', '\n', ' ', "'",
                         '«', '»', '–', '\xa0', '…', '„', '“', '—', '°',
                         '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
                         '`', '[', ']', '{', '}']

    letter_storage = dict()
    for letter in text:
        if letter in punctuation_marks:
            continue
        else:
            if letter_storage.get(letter, None):
                letter_storage[letter] += 1
            else:
                letter_storage[letter] = 1
    sorting_letters(letter_storage)


# открываем файл через ziz модуль, помещаем его в переменную и закрываем архив
archive_processing = zipfile.ZipFile(os.path.abspath(os.path.join('voyna-i-mir.zip')), 'r')
archive_file = archive_processing.extract('voyna-i-mir.txt')
archive_processing.close()
# открываем файл на чтение и вызываем функцию на обработку
with open(archive_file, 'r', encoding='utf-8') as voyna_i_mir:
    text = voyna_i_mir.read()
    text_filtering(text)
