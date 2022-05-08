import os
# список для работы с данными из файла
the_resulting_list = list()
# открытие файла и обработка полученных данных из него
with open(os.path.join('zen.txt'), 'r', encoding='utf-8') as content:
    data = content.readlines()
    the_resulting_list.append(data)
    # цикл для вывода даных в обратном порядке
    for list_value in the_resulting_list:
        for list_reversal in list_value[::-1]:
            if list_reversal.endswith('\n'):
                print(list_reversal[:-1])
            else:
                print(list_reversal)
