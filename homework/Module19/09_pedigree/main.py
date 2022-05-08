# два словаря для хранения данных ребенок отец и ребенок рост
tree_branches = dict()
raise_people = dict()
# запрос на количество пар
number_of_branches = int(input('Введите количество человек: '))
# делаем родоначальника и передаем его в оба списка
# (я выбрал такоей способ)
forefather = input('1 пара: ').split()
tree_branches[forefather[0]] = forefather[1]
raise_people[forefather[1]] = 0
# создаем цикл для передачи данных в словарь ребенок отец
for i_number_of_branches in range(number_of_branches-2):
    children = input('{0} пара: '.format(i_number_of_branches+2)).split()
    tree_branches[children[0]] = children[1]
# обрабарываем первый словарь и выводим из него детей
# определяя их первоначальный рост как 0
for branch in tree_branches:
    raise_people.setdefault(branch, 0)
# сравниваем кто есть чей родственник и в каком росте
# и повышаем значение при определении родства
for age_determination in tree_branches:
    for people in raise_people:
        if tree_branches[age_determination] == people:
            raise_people[age_determination] = raise_people[people] + 1
# сортируем список выводим таблицу
print('\n“Высота” каждого члена семьи:')
for human, height in sorted(raise_people.items()):
    print(human, height)


# TODO это достаточно сложная задача, вот верный вариант решения:
def find_height(man):
    if man not in p_tree:
        return 0
    else:
        return 1 + find_height(p_tree[man])


p_tree = dict()
people_count = int(input('Введите количество человек: '))
for i_pair in range(people_count - 1):
    child, parent = input('{} пара: '.format(i_pair + 1)).split()
    p_tree[child] = parent

heights = dict()
for i_man in set(p_tree.keys()).union(set(p_tree.values())):
    heights[i_man] = find_height(i_man)

print('“Высота” каждого члена семьи:')
for key, value in sorted(heights.items()):
    print(key, value)
