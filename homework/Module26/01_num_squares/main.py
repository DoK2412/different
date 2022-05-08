from collections.abc import Iterator
# Способ № 1 "Итератор"

class SquaresOfNumbers:
    """ Итератор вывода квадрата чисел """
    def __init__(self, stop_number: int) -> None:
        self.stop_number = stop_number
        self.number_counter = 0

    def __iter__(self) -> Iterator:
        self.number_counter = 0
        return self

    def __next__(self) -> int:
        if self.stop_number == self.number_counter:
            raise StopIteration
        else:
            self.number_counter += 1
            return self.number_counter ** 2


numbers = SquaresOfNumbers(int(input('Введите до какого '
                                     'числа вывести квадрыты чисел: ')))
for i_numbers in numbers:
    print(i_numbers, end=' ')

'''
# Способ № 2 "Генератор"
def squares_of_numbers(number: int) -> int:


    for i_number in range(number+1):  # TODO запускали код?
        i_number **= 2
        yield i_number


numbers = squares_of_numbers(int(input('Введите до какого '
                                       'числа вывести квадрыты чисел: ')))

for i_numbers in numbers:
    print(i_numbers, end=' ')


# Способ № 3 "Генераторное выражение"

squares_of_numbers = (number ** 2 for number in range(int(
    input('Введите до какого числа вывести квадрыты чисел: '))+1))

for i_number in squares_of_numbers:
    print(i_number, end=' ')
'''