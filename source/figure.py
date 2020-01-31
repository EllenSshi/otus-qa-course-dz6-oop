import math


class Figure:
    __name = None
    __area = None
    __angles = None
    __perimeter = None

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @property
    def angles(self):
        if isinstance(self, Triangle):
            self.__angles = 3
        elif isinstance(self, Rectangle) or isinstance(self, Square):
            self.__angles = 4
        elif isinstance(self, Circle):
            self.__angles = 0
        else:
            print("This object is not a geometric figure!")
        return self.__angles

    @property
    def area(self):
        if isinstance(self, Square):
            self.__area = math.pow(self._side, 2)
        elif isinstance(self, Triangle):
            semiperimeter = (self._first_side + self._second_side + self._third_side) / 2
            self.__area = math.sqrt(semiperimeter*(semiperimeter-self._first_side)*(semiperimeter-self._second_side)*(semiperimeter-self._third_side))
        elif isinstance(self, Rectangle):
            self.__area = self._length * self._width
        elif isinstance(self, Circle):
            self.__area = math.pi * math.pow(self._radius, 2)
        return self.__area

    @property
    def perimeter(self):
        if isinstance(self, Square):
            self.__perimeter = self._side * 4
        elif isinstance(self, Triangle):
            self.__perimeter = self._first_side + self._second_side + self._third_side
        elif isinstance(self, Rectangle):
            self.__perimeter = self._length * 2 + self._width * 2
        elif isinstance(self, Circle):
            self.__perimeter = math.pi * self._radius * 2
        return self.__perimeter

    def add_area(self, figura):
        if isinstance(figura, Figure):
            return self.area + figura.area
        else:
            raise AttributeError("Переданный объект не является геометрической фигурой!")


class Triangle(Figure):
    def __init__(self, first_side, second_side, third_side):
        self._first_side = first_side
        self._second_side = second_side
        self._third_side = third_side
        super().__init__("Треугольник")


class Rectangle(Figure):
    def __init__(self, length, width):
        self._length = length
        self._width = width
        super().__init__("Прямоугольник")


class Square(Figure):
    def __init__(self, side):
        self._side = side
        super().__init__("Квадрат")


class Circle(Figure):
    def __init__(self, radius):
        self._radius = radius
        super().__init__("Круг")


triangle1 = Triangle(1, 1, 1)
rectangle1 = Rectangle(3, 1)
square1 = Square(4)
circle1 = Circle(6)
# print(triangle1.area)
# print(rectangle1.area)
# print(square1.area)
# print(circle1.area)
# print(isinstance(triangle1, Square))
str = ""
print(rectangle1.add_area(str))
