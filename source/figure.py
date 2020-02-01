import math


class Figure:
    __name = None
    __area = None
    __angles = None
    __perimeter = None

    def __init__(self, name):
        self.__name = name

    def __str__(self):
        return self.__name

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
            self.__area = math.sqrt(
                semiperimeter * (semiperimeter - self._first_side) * (semiperimeter - self._second_side) * (
                        semiperimeter - self._third_side))
        elif isinstance(self, Rectangle):
            self.__area = self._length * self._width
        elif isinstance(self, Circle):
            self.__area = math.pi * math.pow(self._radius, 2)
        return round(self.__area, 1)

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
        return round(self.__perimeter)

    def add_area(self, figure):
        if isinstance(figure, Figure):
            return round(self.area + figure.area, 1)
        else:
            raise AttributeError("Переданный объект не является геометрической фигурой!")


class Triangle(Figure):
    def __init__(self, first_side, second_side, third_side):
        if second_side + third_side > first_side > math.fabs(second_side - third_side) and \
                first_side + third_side > second_side > math.fabs(first_side - third_side) and \
                first_side + second_side > third_side > math.fabs(first_side - second_side):
            self._first_side = first_side
            self._second_side = second_side
            self._third_side = third_side
            super().__init__("Треугольник")
        else:
            raise AttributeError("Такой треугольник создать нельзя! Любая сторона треугольника "
                                 "меньше суммы двух других сторон и больше их разности")


class Rectangle(Figure):
    def __init__(self, length, width):
        if length > 0 and width > 0:
            self._length = length
            self._width = width
            super().__init__("Прямоугольник")
        else:
            raise AttributeError("Такой прямоугольник создать нельзя! Длина и ширина прямоугольника "
                                 "должны быть положительным числом, большим 0!")


class Square(Figure):
    def __init__(self, side):
        if side > 0:
            self._side = side
            super().__init__("Квадрат")
        else:
            raise AttributeError("Такой квадрат создать нельзя! "
                                 "Сторона квадрата должна быть положительным числом, большим 0!")


class Circle(Figure):
    def __init__(self, radius):
        if radius > 0:
            self._radius = radius
            super().__init__("Круг")
        else:
            raise AttributeError("Такой круг создать нельзя! "
                                 "Радиус круга должен быть положительным числом, большим 0!")
