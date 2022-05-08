import os


# определяем подсчет требуемых параметров и вспомогательные инструменты
# (словарь для хранения букв, список исключений)
lines, words, the_letters = 0, 0, 0
number_of_characters = dict()
exceptions = [' ', '.', ',', '–', '-', '*', "'", ':', ';', '\n', '!']
# открываем файл и начинаем обработку текста


with open((os.path.abspath(os.path.join('../..', 'checking_the_text', 'zen.txt'))), 'r', encoding='utf-8') as zen:
    for line in zen.readlines():
        converting_a_string = line.split()
        words += len(converting_a_string)
        lines += 1
        for letter in line.lower():
            if letter in exceptions:
                continue
            else:
                the_letters += 1
                if number_of_characters.get(letter, None):
                    number_of_characters[letter] += 1
                else:
                    number_of_characters[letter] = 1
    zen.close()


# обрабатываем словарь для поиска наименьшего результата всреч букв
quantity = 0
letter = ''
for symbol, meaning in number_of_characters.items():
    if quantity == 0:
        quantity = meaning
        letter = symbol
    else:
        if quantity > meaning:
            quantity = meaning
            letter = symbol

print('Строк в тексте: {0}\n\
Слов в тексте: {1}\nБукв в тексе: {2}\n\
В тексте буква "{3}" встречается всего {4} раза и \
эта буква является наименьше встречаемой в тексте.\
'.format(lines, words, the_letters, letter, quantity))
