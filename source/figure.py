import math
from abc import abstractmethod


class Figure:
    __name = None
    __area = None
    __angles = None
    __perimeter = None

    def __init__(self, name, angles):
        self.__name = name
        self.__angles = angles

    def __str__(self):
        return self.__name

    @property
    def name(self):
        return self.__name

    @property
    def angles(self):
        return self.__angles

    @property
    @abstractmethod
    def area(self):
        return NotImplemented

    @property
    @abstractmethod
    def perimeter(self):
        return NotImplemented

    @staticmethod
    def distance(a: list, b: list):
        """
        Метод возвращает расстояние между двумя точками, лежащими в прямоугольной системе координат.
        Принимает два аргумента: a - координаты точки A, напр. [1, 5],
        b - координаты точки B, напр. [2, 3].
        """
        xa = a[0]
        xb = b[0]
        ya = a[1]
        yb = b[1]
        return round(math.sqrt(math.pow(xb - xa, 2) + math.pow(yb - ya, 2)), 1)

    @staticmethod
    def is_on_one_line(a: list, b: list, c: list):
        """
        Проверяет, лежат ли точки на одной прямой.
        Принимает три аргумента: a, b, c - координаты точек, образующих треугольник.
        Возвращает True, если точки лежат на одной прямой. Иначе - False.
        Уравнение прямой (x-x1)/(x2-x1) = (y-y1)/(y2-y1)
        """
        return (c[0] - a[0])/(b[0] - a[0]) == (c[1] - a[1])/(b[1] - a[1])

    def add_area(self, figure):
        """
        Метод возвращает сумму площадей двух фигур.
        Принимает в качестве аргумента другую геометрическую фигуру.
        """
        if isinstance(figure, Figure):
            return round(self.area + figure.area, 1)
        else:
            raise AttributeError("Переданный объект не является геометрической фигурой!")


class Triangle(Figure):
    def __init__(self, a_point: list, b_point: list, c_point: list):
        """
        Создает объект класса "Треугольник"
        Принимает три аргумента: a_point - координаты точки A,
        b_point - координаты точки B, c_point - координаты точки С.
        Координаты точек задаются списком из двух значений - по оси X, и по оси Y
        """
        if self.is_on_one_line(a_point, b_point, c_point):
            raise AttributeError("Такой треугольник создать нельзя! Точки A, B и C лежат на одной прямой.")
        else:
            self.__side_one = self.distance(a_point, b_point)
            self.__side_two = self.distance(a_point, c_point)
            self.__side_three = self.distance(b_point, c_point)
            super().__init__("Треугольник", 3)

    @property
    def area(self):
        semiperimeter = (self.__side_one + self.__side_two + self.__side_three) / 2
        self.__area = math.sqrt(
            semiperimeter * (semiperimeter - self.__side_one) * (semiperimeter - self.__side_two) * (
                    semiperimeter - self.__side_three))
        return round(self.__area, 1)

    @property
    def perimeter(self):
        self.__perimeter = self.__side_one + self.__side_two + self.__side_three
        return round(self.__perimeter, 1)


class Rectangle(Figure):
    def __init__(self, a_point: list, b_point: list, c_point: list):
        """
        Создает объект класса "Прямоугольник"
        Принимает три аргумента: a_point - координаты точки A,
        b_point - координаты точки B, c_point - координаты точки С.
        Точки A и B соединяют одну сторону прямоугольника,
        а точки B и C - вторую сторону.
        Координаты точек задаются списком из двух значений - по оси X, и по оси Y
        """
        self.__side_one = self.distance(a_point, b_point)
        self.__side_two = self.distance(b_point, c_point)
        super().__init__("Прямоугольник", 4)

    @property
    def area(self):
        self.__area = self.__side_one * self.__side_two
        return round(self.__area, 1)

    @property
    def perimeter(self):
        self.__perimeter = self.__side_one * 2 + self.__side_two * 2
        return round(self.__perimeter)


class Square(Figure):
    def __init__(self, a_point: list, b_point: list):
        """
        Создает объект класса "Квадрат"
        Принимает два аргумента: a_point - координаты точки A,
        b_point - координаты точки B.
        Координаты точек задаются списком из двух значений - по оси X, и по оси Y
        """
        if a_point == b_point:
            raise AttributeError("Такой квадрат создать нельзя! Координаты точек A и B одной из сторон совпадают.")
        self.__side = self.distance(a_point, b_point)
        super().__init__("Квадрат", 4)

    @property
    def area(self):
        self.__area = math.pow(self.__side, 2)
        return round(self.__area, 1)

    @property
    def perimeter(self):
        self.__perimeter = self.__side * 4
        return round(self.__perimeter)


class Circle(Figure):
    def __init__(self, center_point: list, circle_point: list):
        """
        Создает объект класса "Окружность"
        Принимает два аргумента: center_point - координаты центра окружности,
        circle_point - координаты точки, лежащей на окружности.
        Координаты точек задаются списком из двух значений - по оси X, и по оси Y
        """
        if center_point == circle_point:
            raise AttributeError("Такой круг создать нельзя! Центр окружности совпадает с точкой окружности.")
        else:
            self.__radius = self.distance(center_point, circle_point)
            super().__init__("Круг", 0)

    @property
    def area(self):
        self.__area = math.pi * math.pow(self.__radius, 2)
        return round(self.__area, 1)

    @property
    def perimeter(self):
        self.__perimeter = math.pi * self.__radius * 2
        return round(self.__perimeter)


sq = Square([2, 1], [4, 1])
print(sq.area)
