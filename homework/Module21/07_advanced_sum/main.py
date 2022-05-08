def summ(*args):
    def processing(i_args):
        unpacking = []
        for meaning in i_args:
            if isinstance(meaning, int):
                unpacking.append(meaning)
            else:
                unpacking.extend(processing(meaning))
        return unpacking
    return sum(processing(args))

# изучил ваше решение через простое вычисление не используя списка 
# программа действует без лишнего распаковывания, по началу мне показалась 
# что списком проше, учту в будующем
print(summ([[1, 2, [3]], [1], 3]))


# TODO немного сложновато из-за вложенной функции, вот другой вариант:
def my_sum(*args):
    total_sum = 0
    for i_elem in args:
        if isinstance(i_elem, int):
            total_sum += i_elem
        elif isinstance(i_elem, list):
            for x in i_elem:
                total_sum += my_sum(x)

    return total_sum
