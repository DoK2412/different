class_1 = []
class_2 = []
combining_classes = []
# заполнение первого списка и передача его в общий список
for children in range(160, 177, 2):
    class_1.append(children)
combining_classes.extend(class_1)
# заполнение второго списка и передача его в общий список
for children in range(162, 180, 3):
    class_2.append(children)
combining_classes.extend(class_2)
# выпод первых двух списков
print('Первый класс: ', class_1)
print('Второй класс: ', class_2)
# сортировка и вывод общего списка учеников
combining_classes.sort()
print('Объяденение классов по росту: ', combining_classes)
