word = input('Введите слово: ')
# переводим строку в список и убираем из списока повторяющиеся знаки с помощью команды set
list_of_characters = list(set(word))
# выводим количество оставшихся символов в списке
print('Количество уникальных символов', len(list_of_characters))
