class Store:
    """Создание рабочего списка добавление и стировние данны"""
    def __init__(self):
        self.stack = list()

    def __add__(self, other):
        self.stack.append(other)

    def __del__(self):
        if len(self.stack) > 0:
            self.stack.pop()

    def __str__(self):
        return str(self.stack)


class TaskManager:
    """Работа со стеком"""
    def new_task(self, other):
        Store.__add__(self, other)  # TODO метод ожидает объект своего класса Store, а не TaskManager

    def deleting_an_element(self):
        Store.__del__(self)


# TODO покажу вариант решения:
class Stack:
    def __init__(self):
        self.__stack = list()

    def pop(self):
        if self.is_empty():
            return None
        return self.__stack.pop()

    def push(self, item):
        self.__stack.append(item)

    def is_empty(self):
        return len(self.__stack) == 0

    def top(self):
        if self.is_empty():
            return None
        return self.__stack[-1]


class TaskManager:
    def __init__(self):
        self.tasks = dict()

    def new_task(self, text, priority):
        if priority in self.tasks:
            self.tasks[priority].push(text)
        else:
            self.tasks[priority] = Stack()

    def __str__(self):
        sorted_keys = sorted(self.tasks.keys())
        out = ['Список задач:']
        for key in sorted_keys:
            task_line = [str(key)]
            while not self.tasks[key].is_empty():
                task_line.append(self.tasks[key].pop())
            out.append(' '.join(task_line))
        return '\n'.join(out)


def main():
    manager = TaskManager()
    manager.new_task("сделать уборку", 4)
    manager.new_task("помыть посуду", 4)
    manager.new_task("отдохнуть", 1)
    manager.new_task("поесть", 2)
    manager.new_task("сдать дз", 2)
    print(manager)


main()
