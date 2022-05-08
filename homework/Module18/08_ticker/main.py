# запрос на ввод данных от пользователя
first_ine = input('Первая строка: ')
second_line = input('Вторая строка: ')
# вспомогательная строка
auxiliary_string = ''
# функция для проверки сдвига строки
for i in range(len(first_ine)):
    auxiliary_string = first_ine[-i:] + first_ine[:-i]
    # проверка на сравнение строк
    if auxiliary_string == second_line:
        print('Первая строка получается из второй со сдвигом {}.'.format(i))
        break
# вывод если сделать строки одинаковыми на возможно
else:
    print('Первую строку нельзя получить из второй с помощью циклического сдвига.')
