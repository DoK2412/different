import random

def list_transformation(list_of_numbers):
    final_result = list()
    lists = list()
    for values in list_of_numbers:
        lists.append(values)
        if len(lists) >= 2:
            final_result.append(tuple(lists))
            lists.clear()
    return(final_result)

list_of_numbers = [random.randint(1, 9) for number in range(10)]

print(list_transformation(list_of_numbers))


