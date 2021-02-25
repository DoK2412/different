
def flip_the_number(number):
    counter = 0
    def form_1(number):
        work = str(number)
        number_to_the_dot = ''
        for i in work:
            if i == '.':
                break
            number_to_the_dot += i
        x = ''.join(reversed(number_to_the_dot))
        counter_1 = int(x)
    

    the_number_after_the_dot = ''
    for i in work[::-1]:
        if i == '.':
            break
        the_number_after_the_dot += i
    

    print('Число наоборот', x + '.' + the_number_after_the_dot)
        


number = float(input('Введите число: '))
number2 = float(input('Введите число: '))

flip_the_number(number)
flip_the_number(number2)

print(counter_1)




