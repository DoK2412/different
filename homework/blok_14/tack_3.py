def flip_the_number(number):
    work = str(number)

    number_to_the_dot = ''
    the_number_after_the_dot = ''

    for i in work:
        if i == '.':
            break
        number_to_the_dot += i

    for i in work[::-1]:
        if i == '.':
            break
        the_number_after_the_dot += i

    x = ''.join(reversed(number_to_the_dot))
    return [x, the_number_after_the_dot]

number = float(input('Введите число: '))
number2 = float(input('Введите число: '))

coup_1 = flip_the_number(number)
print('\nВервое чтсло наоборот: ', coup_1[0] + '.' + coup_1[1])
coup_2 = flip_the_number(number2)
print('Вервое чтсло наоборот: ', coup_2[0] + '.' + coup_2[1])

summ_1 = int(coup_1[0]) + int(coup_2[0])
summ_2 = int(coup_1[1]) + int(coup_2[1])

print('\nСумма чисел: ', str(summ_1) + '.' + str(summ_2))
