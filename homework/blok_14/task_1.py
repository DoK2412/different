print("Введите первую точку: ")

x1 = float(input('X: '))
y1 = float(input('Y: '))

print("\nВведите вторую точку: ")

x2 = float(input('X: '))
y2 = float(input('Y: '))


k = (x1 - x2) / (y1 - y2)
b = y2 - k * x2


print("Уравнение прямой, проходящей через эти точки:")
print("y = ", k, " * x + ", b)
