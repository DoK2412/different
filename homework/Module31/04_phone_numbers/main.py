import re
import itertools
# список номеров аббонентов
list_of_numbers = ['9999999999', '999999-999', '99999x9999', '89999666225']
# регулярное выражение на поиск
regular = r'[8-9]\d{9}'
# нумерация цикла
counter = itertools.count(1)
# цикл прогона всех номеров и сравнения правильности ввода
for i_namber in list_of_numbers:
    phone_number = re.findall(regular, i_namber)
    if phone_number:
        print(next(counter), 'номер: всё в порядке')
    else:
        print(next(counter), 'номер: не подходит')

