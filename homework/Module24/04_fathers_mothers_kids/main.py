import relatives


# функция преобразования действий родителя
def actions_on_children(info, childrens_data, number):
    for children in childrens_data:
            if info == children.name:
                if number == 2:
                    relatives.Kid.info_kid(children)
                elif number == 3:
                    relatives.Kid.calm_the_child_down(children)
                    print(children.name, 'успокоился и спит.')
                elif number == 4:
                    relatives.Kid.feed_the_baby(children)
                    print(children.name, 'накормлен и отдыхает.')


# запрос данных о родителе
name = input('Введите имя родителя: ')
age = int(input('Введите возраст родителя: '))
list_of_children = input('Введите имена детей: ').split()
# преобразовываем родителя через класс
data_about_the_parent = relatives.Parent(name, age, list_of_children)
# преобразовываем список дерей
childrens_data = [
    relatives.Kid(name, data_about_the_parent.age)
    for name in data_about_the_parent.list_of_children]
# действия родителя
while True:
    actions_of_the_parent = int(input('\nВыберите действие: \n1. Сообщить\
информацию о себе.\n2. Сообщить информацию о детях.\n3. \
Успокоить ребёнка\n4. Покормить ребёнка\n'))

    if actions_of_the_parent == 1:
        relatives.Parent.info_parent(data_about_the_parent)
    elif actions_of_the_parent == 2:
        info = input(
            'Введите имя ребенко о котором хотите получит информацию: ')
        actions_on_children(info, childrens_data, number=2)

    elif actions_of_the_parent == 3:
        info = input('Какого ребенка вы хотите успокоить? ')
        actions_on_children(info, childrens_data, number=3)

    elif actions_of_the_parent == 4:
        info = input('Какого ребенка вы хотите накормить? ')
        actions_on_children(info, childrens_data, number=4)
