counter_1 = 1
counter_2 = 0
n = int(input('Ведите число: '))
for value in range(1, n+1):
    counter_1 *= value
    counter_2 += counter_1
print(counter_2)
