
number = int(input('Введите количетсво столбцов:'))
counter = 1
while number  > 0:
        print(' '*number + '#'*counter)
        counter += 2
        number -= 1
