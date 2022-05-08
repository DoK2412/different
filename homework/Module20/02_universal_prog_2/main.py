# долго я думал над этим заданием
import random


# основная функция возвращающая итоговый список
def data_output(numeric_list):
    return [values for checking, values in enumerate(numeric_list) if checking in is_prime(numeric_list)]


# функция для определения индексов - простох чисел 
def is_prime(numeric_list):
    list_of_prime_numbers = list()
    for checking, values in enumerate(numeric_list):
        divisor_account = 0
        for i in range(2, len(numeric_list)):
            if checking >= 2:
                if checking % i == 0:
                    divisor_account += 1
        if divisor_account == 1:
            list_of_prime_numbers.append(checking)
    return list_of_prime_numbers


# TODO можно сделать чуть проще:
def is_prime(number):
    for i_num in range(2, number):
        if number % i_num == 0:
            return False
    return True


# работа программы с строкой, кортежем, списком, словарем, множеством
numeric_list = 'Привет'
# numeric_list = tuple(random.randint(1, 10) for _ in range(10))
# numeric_list = [random.randint(1, 10) for _ in range(10)]
# numeric_list = {'name': 'Bob', 'surname': 'Vazovski', 'age': 23,}
# numeric_list = set(random.randint(1, 10) for _ in range(10))


# запрос функции и вывод данных
print(data_output(numeric_list))
