# функция принимает 2 значения и
# создает новый список с возвратом


def my_zip(list_1, list_2):
    processing = [(list_1[index], list_2[index]) for index in range(min(len(list_1), len(list_2)))]
    return processing


list_1 = (1, 2, 3, 4, 5)
list_2 = 10, 20, 30, 40, 50, 60

print(my_zip(list_1, list_2))

# зачтено
