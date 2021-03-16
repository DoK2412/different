x = int(input('Введите первое число: '))
y = int(input('Введите второй число: '))


while x < y:
    for i in range(10):
        if 3 == str(x).count(str(i)):
            print(x)
    x += 1
