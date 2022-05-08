import os
# вспомогательные элементы программы
alphabet = 'abcdefghijklmnopqrstuvwxyz'
encrypted_text = []
split = 1


# открытие файла на чтение
with open(os.path.abspath(os.path.join('text.txt')), 'r', encoding='utf-8') as for_encryption:
    lines = for_encryption.read().split()
    # после преобразование данных в список
    # начинаем шифровку данных и передачу
    # их на временное хванение
    for i_lines in lines:
        separate_encryption = ''
        for separate_value in i_lines:
            position = alphabet.index(separate_value.lower()) % len(alphabet)
            separate_encryption += alphabet[(position + split) % len(alphabet)]
        encrypted_text.append(separate_encryption.title())
        split += 1


# открытие списка на запись и передача данных в него
with open('cipher_text.txt', 'w', encoding='utf-8') as writing_to_a_file:
    for i_encrypted_text in encrypted_text:
        writing_to_a_file.write(str(i_encrypted_text + '\n'))
    print('Файл успешно записан!')
