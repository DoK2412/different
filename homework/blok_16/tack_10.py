numbers = int(input('Количество чисел: '))
the_sequence = []
selection__list = []

for _ in range(numbers):
    meaning = int(input('Число: '))
    the_sequence.append(meaning)

if the_sequence[-1] == the_sequence[-2]:
    selection__list.extend(the_sequence[-3::-1])
elif the_sequence[-1] != the_sequence[-2]:
    selection__list.extend(the_sequence[-2::-1])

print('Последовательность: ', ' '.join(map(str, the_sequence)))
print('Нужно приписать чисел: ', len(selection__list))
print('Сами числа:', ' '.join(map(str, selection__list)))
