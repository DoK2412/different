# в данной задаче я использовал 2 файла один из задания второй свой,
# остал свой вариант на ктором тестил, если нужно убедиться в результате
# с образцом прошу постапить в название файла в начате программы цифру 2

import os


# открываем файл на запись с перезаписью и сохраняем
# в него отсортированный результат
def writing_to_a_file(final_count):
    with open('analysis.txt', 'w', encoding='utf-8') as record:
        for fraction in sorted(final_count.values(), reverse=True):
            for letter, the_share_being_compared in sorted(final_count.items()):
                if fraction == the_share_being_compared:
                    record.write(letter + ' ' + str(the_share_being_compared) + '\n')
                    final_count.pop(letter)
        print('Файл успешно записан.')


# опркдкляем долю каждой буквы и отправляем на запись в файл
def percentage_of_letters(the_letters):
    total_number_of_letters = sum(the_letters.values())
    final_count = dict()
    for letter, meaning in the_letters.items():
        final_count[letter] = round(meaning / total_number_of_letters, 3)
    writing_to_a_file(final_count)


# функция считает буквы и определяет их в словарь
# с их итоговым количеством после чего
# вызывет функцию для подсчета анализа
def number_of_letters(working_with_text):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    the_letters = dict()
    for letter in working_with_text.lower():
        if letter in alphabet:
            if the_letters.get(letter, None):
                the_letters[letter] += 1
            else:
                the_letters[letter] = 1
    percentage_of_letters(the_letters)


# открываем файл на чтение и фазываем функцию
with open(os.path.abspath(os.path.join('text.txt')), 'r') as text:
    working_with_text = text.read()
    number_of_letters(working_with_text)
