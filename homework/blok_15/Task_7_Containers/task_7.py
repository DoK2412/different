counter = int(input('Ввелите количество контейнеров: '))
the_weight_of_the_container = []
check = 0

for _ in range(counter):
    weight = int(input('Введите вес контейнера: '))
    the_weight_of_the_container.append(weight)

new_counter = int(input('Ввелите вес нового контейнера: '))
if new_counter > 200:
    print('Вес контейнера привышает норму!')
else:
    for i in the_weight_of_the_container:
        if i > new_counter:
            check += 1
    print('Номер, куда встанет новый контейнер: ', check + 1)
