# вводим слово
word = list(input('Введите строку: '))
# определяем сколько букв нечетного количество
parity = 0
# считаем буква в слове
for letter in set(word):
    counter = 0
    for i_word in word:
        if letter == i_word:
            counter += 1
    if counter % 2 != 0:
        parity += 1
# делаем сравнение если нечетных букв больше 1 не палинром
# иначе палиндром
if parity > 1:
    print('Нельзя сделать палиндромом')
else:
    print('Можно сделать палиндромом')
