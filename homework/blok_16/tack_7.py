shoe_size = []
skate_size = []
counter = 0

n = int(input('Количество коньков: '))
for couple in range(n):
    skates = int(input(f'Размер {couple + 1} пары: '))
    skate_size.append(skates)

k = int(input('Количество людей: '))
for people in range(k):
    shoes = int(input(f'Размер ноги {people + 1} человека: '))
    shoe_size.append(shoes)

for i in shoe_size:
    for f in skate_size:
        if f >= i:
            skate_size.remove(f)
            counter += 1

print('Наибольшее кол-во людей, которые могут взять ролики: ', counter)
