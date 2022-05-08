class Node:
    """Класс для формирования новых значений в список"""
    def __init__(self, data):
        self.item = data
        self.ref = None


class LinkedList:
    """Класс для реализации полной работы односвязного списка"""
    def __init__(self):
        self.start_node = None

    # функция для вывода списка
    def conclusion(self):
        if self.start_node is None:  # проверка если список пуст вывод данных
            print('Список пуст')
            return
        else:  # если нет вывод всех его значений
            link = self.start_node
            list_data = str()
            while link is not None:
                list_data += ' ' + str(link.item)
                link = link.ref
            return list_data

    # функция для добавления элемента в конец
    def append(self, data):
        new_node = Node(data)   # создаем новый экземпляр класса
        if self.start_node is None:   # проверяем концовку текушего списка
            # если пустой добавляем в него созданный экземпляр
            self.start_node = new_node
            return
        # если наполнен то создаем переменную с ссылкой на текущий узел
        link = self.start_node
        while link.ref is not None:  # ищем последний узел
            link = link.ref
        link.ref = new_node

    # функция для вывода элемента под необходимым индексом
    def get(self, index):
        counter = 0  # контейнер для подсчета индекса узла
        link = self.start_node
        while link is not None:
            if counter == index:  # сравнение индеса узла с запросом
                return link.item  # возврат найденного значения
            counter += 1   # повышение при неудаче
            link = link.ref  # переход на слудующий узел

    # функция для удаления элемента по индексу
    # сдесь я использовал двойной цикл для возможности
    # удаления любого значения из списка
    def remove(self, index):
        main_node = self.start_node
        auxiliary_node = self.start_node
        current_value = 0
        # проверяем есть ли элементы в списке
        if self.start_node is None:
            print('Список пуст. Удалять нечего.')
            return
        # проверяем не первый ли элемент искомое значение и
        # переопределяем ссылку на узел
        if index == 0:
            self.start_node = self.start_node.ref
            return
        # ищем элемент который находится перед искомым значением
        while current_value <= index-1 and auxiliary_node.ref is not None:
            if current_value == index-1:
                break
            current_value += 1
            # берем ячейку которая храние направление на следующий элемент
            auxiliary_node = auxiliary_node.ref
        # обнуляем счетчик
        current_value = 0
        # ищем элемент который необходимо удалить
        while current_value <= index and main_node.ref is not None:
            if current_value == index:
                # после того как находим его пристваиваем
                # предыдущему значению ссылку на элемент стоящий посое
                # искомого
                auxiliary_node.ref = main_node.ref
                break
            current_value += 1
            main_node = main_node.ref
        # тут по законам логики если удаляем не первый
        # элемент и не один из внутренних, тогда удаляем последний
        else:
            auxiliary_node.ref = None


my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
my_list.append(50)
print('Текущий список:', my_list.conclusion())
print('Получение третьего элемента:', my_list.get(2))
print('Удаление второго элемента.')
my_list.remove(1)
print('Новый список:', my_list.conclusion())