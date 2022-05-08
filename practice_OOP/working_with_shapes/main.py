from abc import ABC, abstractmethod


class Shapes(ABC):
    '''
    Класс является базовым абстрактным классом для создания экземпляров
    переменные экземпляра закрыты и передаются через методы подключенные
    к геерерам с сеттарам

    методы:
    perimeter_2d, square_2d, square_3d
    сделаны пустышками в воде абстрактных для того
    что бы в дочерних классах не было возмодности пропустить их.
    '''
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self) -> int:  # TODO в более общем случая float
        return self._width

    @width.setter
    def width(self, width: int) -> None:
        self._width = width

    @property
    def height(self) -> int:
        return self._height

    @height.setter
    def height(self, height: int) -> None:
        self._height = height

    @abstractmethod
    def perimeter_2d(self):
        pass

    @abstractmethod
    def square_2d(self):
        pass

    @abstractmethod
    def square_3d(self):
        pass


class Triangle(Shapes):
    '''
    Клас предназначен для работы с треугольниками
    perimeter_2d - расчет периметра треугоника
    square_2d - расчет площади треугоника
    square_3d - расчет площади пирамиды
    '''
    def __init__(self, width, height):
        super().__init__(width, height)
        self.apofera = self.width * 3  # апофера
        self.square_side = [1/2 * self.width * self.apofera for _ in range(4)]

    def perimeter_2d(self) -> int:
        return self.width + self.height * 2

    def square_2d(self) -> int:
        return 1/2 * self.width * self.apofera

    def square_3d(self) -> int:
        return self.width ** 2 + sum(self.square_side)



class Pyramid(Shapes):
    '''
    Клас предназначен для работы с квадратами
    perimeter_2d - расчет периметра квадрата
    square_2d - расчет площади квадрата
    square_3d - расчет площади куба
    '''
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_side = [self.width**2 for _ in range(6)]
        # так как куб имеет 6 одинаковых сторон которые расчитываются
        # по иденточной формуле расчета, я сделал список площажей всех сторон
        # которые сложил в функции общей площади

    def perimeter_2d(self) -> int:
        return self.width * 4

    def square_2d(self) -> int:
        return self.width**2

    def square_3d(self) -> int:
        general_square = 0
        for side in self.square_side:
            general_square += side
        return general_square


triangle = Triangle(5, 10)  # треугольник
print('Периметр треугольника: ', Triangle.perimeter_2d(triangle))
print('Площадь треугольника: ', Triangle.square_2d(triangle))
print('Площадь пирамиды: ', Triangle.square_3d(triangle))

pyramid = Pyramid(5, 5)  # куб

print('Периметр квадрата: ', Pyramid.perimeter_2d(pyramid))
print('Площадь квадрата: ', Pyramid.square_2d(pyramid))
print('Площадь куба: ', Pyramid.square_3d(pyramid))
