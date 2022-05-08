# создаем необходимые списки и запромы данных у пользователя
interpreter = ['а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я'] * 2
data_entry = [meaning for meaning in input('Введите сообщение: ')]
step = int(input('Введите шаг: '))
counter = 0
# формируем список шифрования
encryption = [interpreter[interpreter.index(first_list) + step] for first_list in data_entry for second_list in interpreter  if second_list == first_list]
# убираем лишние значения в списке
del encryption [::2]
# выставляем пробеты
for enumeration in data_entry:
    counter += 1
    if enumeration == ' ':
        encryption.insert(counter - 1, ' ')
# выводим результат
print('Зашифрованное сообщение: ',''.join(encryption))
