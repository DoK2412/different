# элемент воды
class Water:
    def __init__(self):
        self.name = 'вода'

    def __add__(self, element):
        if isinstance(element, Air):
            return Storm()
        elif isinstance(element, Fire):
            return Steam()
        elif isinstance(element, Earth):
            return Dirt()
        elif isinstance(element, Tree):
            return Height()


# элемент воздуха
class Air:
    def __init__(self):
        self.name = 'Воздух'

    def __add__(self, element):
        if isinstance(element, Water):
            return Storm()
        elif isinstance(element, Fire):
            return Lightning()
        elif isinstance(element, Earth):
            return Dust()
        elif isinstance(element, Tree):
            return Photosynthesis()


# элемент огня
class Fire:
    def __init__(self):
        self.name = 'огонь'

    def __add__(self, element):
        if isinstance(element, Water):
            return Steam()
        elif isinstance(element, Air):
            return Lightning()
        elif isinstance(element, Earth):
            return Lava()
        elif isinstance(element, Tree):
            return Coal()


# элемент земли
class Earth:
    def __init__(self):
        self.name = 'земля'

    def __add__(self, element):
        if isinstance(element, Water):
            return Dirt()
        elif isinstance(element, Air):
            return Dust()
        elif isinstance(element, Fire):
            return Lava()


# элемент дерева
class Tree:
    def __init__(self):
        self.name = 'дерево'

    def __add__(self, element):
        if isinstance(element, Water):
            return Height()
        elif isinstance(element, Air):
            return Photosynthesis()
        elif isinstance(element, Fire):
            return Coal()


# блок классов вывода каждого преобразованого элемента
class Storm:
    def __str__(self):
        return 'Сложили два класса и вывели: шторм'


class Steam:
    def __str__(self):
        return 'Сложили два класса и вывели: пар'


class Dirt:
    def __str__(self):
        return 'Сложили два класса и вывели: грязь'


class Lightning:
    def __str__(self):
        return 'Сложили два класса и вывели: молния'


class Dust:
    def __str__(self):
        return 'Сложили два класса и вывели: пыль'


class Lava:
    def __str__(self):
        return 'Сложили два класса и вывели: лава'


class Height:
    def __str__(self):
        return 'Сложили два класса и вывели: рост'


class Photosynthesis:
    def __str__(self):
        return 'Сложили два класса и вывели: фотосинтез'


class Coal:
    def __str__(self):
        return 'Сложили два класса и вывели: уголь'
