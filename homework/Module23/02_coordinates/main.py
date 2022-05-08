import os
import random


# функци первого просчета
def function_number_1(nums_list):
    x = int(nums_list[0]) + random.randint(0, 5)
    y = int(nums_list[1]) + random.randint(0, 10)
    return int(x / y)


# функция второго просчета
def function_number_2(nums_list):
    x = int(nums_list[0]) - random.randint(0, 5)
    y = int(nums_list[1]) - random.randint(0, 10)
    return int(y / x)


# функция формирования списка и записи его в файл
def recording_data(nums_list):
    for line in coordinates:
        nums_list = line.split()
        try:
            list_of_values = sorted([function_number_1(nums_list),
                                     function_number_2(nums_list),
                                     random.randint(0, 100)])
            with open('result.txt', 'a') as result:
                result.write(str(list_of_values) + '\n')
        except ZeroDivisionError:
            print('При обработке данных обнаружено деление на 0.')
        except ValueError:
            print('При обработке данных обнаружена несовместимость типов.')

# открытие файла
with open('coordinates.txt', 'r', encoding='utf-8') as coordinates:
    recording_data(coordinates)
