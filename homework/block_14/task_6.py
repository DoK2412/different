
def radius(x, y, r):
    if ((r > x > 0) or (r > y > 0) or (-r < x < 0) or (-r < y < 0)):
        print('Монетка где то рядом')
    else:
        print('Монетки в области нет')

x = float(input('Введите первую координату x: '))
y = float(input('Введите вторую координату y: '))
r = float(input('Введите радиус поиска: '))

radius(x, y, r)