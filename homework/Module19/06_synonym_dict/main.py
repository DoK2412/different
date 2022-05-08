# определение количества пар и создание пустого словаря
number_of_pairs = int(input('Введите количество пар слов: '))
a_couple_of_words = dict()

# цикл для создания словаря для проведения работы сравнени
for i in range(number_of_pairs):
    meaning = input(f'{i+1} пара: ')
    meanings = meaning.split()
    a_couple_of_words[meanings[0]] = meanings[1]

# бесконечный цикл на вывод слов синонимов и завершении программы
print('\nДля полной остановки программы введите "стоп"')
while 1:
    # запрос слова
    word = input('Введите слово: ')
    # цикл на сравнение полученного слова и вывода значения необходимого ключа
    for i in a_couple_of_words:
        if word.lower() == i.lower():
            print('Синоним: ', a_couple_of_words[i])
            break
        elif word.lower() == a_couple_of_words[i].lower():
            print('Синоним: ', i)
            break

    # остановка цикла и вывод ошибки если данного слова нет
    else:
        if word.lower() == 'стоп':
            print('Выполнение программы полностью остановлено!')
            break
        print('Такого слова в словаре нет')
