a = int(input('Введите первое значение диапазона: '))
b = int(input('Введите последнее число диапазона: '))
c = int(input('Кратность какого числа будем искать? '))
counter = 0
summ = 0
for score in range(a, b + 1):
  if score % c == 0:
    #print('Сработка на ', score)
    summ += score
    counter += 1
#print('Количество сработок',counter)
print('Cреднее арифметическое чисел', summ / counter)
