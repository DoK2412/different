# создвем два списка, идин с вводом данных, другой для обработки слова
text = input('Введите текст: ').split()
the_largest_word = []
counter = 0
# создаем цикл для проверки длины слова и созранности его
for i_text in text:
    if len(i_text) > counter:
        counter = len(i_text)
        the_largest_word.clear()
        the_largest_word.append(i_text)
# выводим получившиеся данных
print('Наибольшее слово: ' ''.join(the_largest_word))
print('Его длина: ', counter, 'букв')
