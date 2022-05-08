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


# TODO Неплохо! Покажу другой вариант:
from typing import Optional, NoReturn, Iterable, Any, Type, Union


class Node:
    def __init__(self, value: Any, next_node: Optional['Node'] = None) -> None:
        self.next_node = next_node
        self.value = value

    def get_next_node(self) -> Optional['Node']:
        """
        Возвращаем следующий узел.

        :return:
        """
        return self.next_node

    def get_value(self) -> Any:
        """
        Возвращаем значение, которое храним в узле.

        :return:
        """
        return self.value


class LinkedList:
    """

    """
    def __init__(self) -> None:
        self.root_node = None

    def append(self, value: Any) -> None:
        """
        Добавление значения в связанный список.
        В самое начало.

        :param value:
        :return:
        """
        node = Node(value, self.root_node)
        self.root_node = node

    def find(self, node_id: int) -> tuple(Optional['Node'], Optional['Node']):
        """
        Ищем узел с заданным индексом в списке, начиная с корневого - 0.
        Если ничего не найдено, то вовзращаем пустые значения.
        Если мы найденный узел - корневой, то в кортеже - первым будет пустой узел.

        :param node_id:
        :return:
        """
        for i, _ in enumerate(self):
            if i == node_id:
                break
        else:
            return None, None
        return self.prev_node, self.current_node

    def get(self, node_id: int) -> Any:
        """
        Получение значения узла с заданным индексом, начиная с корневого - 0.

        :param node_id:
        :return:
        """
        _, current_node = self.find(node_id)
        return current_node.value()

    def remove(self, node_id: int) -> None:
        """
        Удаление узла с заданным индексом, начиная с корневого - 0.

        :param node_id:
        :return:
        """
        prev_node, current_node = self.find(node_id)
        if current_node is None:
            return

        if current_node == self.root_node:
            self.root_node = current_node.get_next_node()
        else:
            self.prev_node.next_node = self.current_node.get_next_node()

    def __iter__(self) -> 'LinkedList':
        self.current_node = self.root_node
        self.prev_node = None
        return self

    def __next__(self) -> Union[Any, NoReturn]:
        if self.current_node is not None:
            self.prev_node = self.current_node
            self.current_node = self.current_node.get_next_node()
            return self.current_node.value()
        else:
            raise StopIteration

    def __str__(self) -> str:
        out_str = []
        for val in self:
            out_str.append(val)
        return f"[{' '.join(out_str)}]"


def main() -> None:
    """
    Функция для теста нашего связанного списка.

    :return:
    """
    my_list = LinkedList()
    my_list.append(10)
    my_list.append(20)
    my_list.append(30)
    print('Текущий список:', my_list)
    print('Получение третьего элемента:', my_list.get(2))
    print('Удаление второго элемента.')
    my_list.remove(1)
    print('Новый список:', my_list)


main()
