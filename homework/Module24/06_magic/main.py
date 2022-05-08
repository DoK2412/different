import transformation


# функция для воздания элементов
def alchemy(element):
    if element == 'вода':
        return transformation.Water()
    elif element == 'воздух':
        return transformation.Air()
    elif element == 'огонь':
        return transformation.Fire()
    elif element == 'земля':
        return transformation.Earth()
    elif element == 'дерево':
        return transformation.Tree()

print('Выберете и добавьте 2 элемента из списка для смештвания:\
\n\n\t1. Вода 2. Воздух 3. Огонь 4. Земля 5. Дерево\n')
# запрос двух элементов
element_1 = alchemy(input('Добавьте первый элемент:  ').lower())
element_2 = alchemy(input('Добавьте второй элемент:  ').lower())


new_element = element_1 + element_2
print(new_element)
