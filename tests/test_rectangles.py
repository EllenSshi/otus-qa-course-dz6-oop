import pytest
from source.figure import Rectangle, Square


def test_create_rectangle_with_proper_sides():
    rectangle = Rectangle(2, 4)
    assert rectangle.name == "Прямоугольник"


def test_create_rectangle_with_bad_sides():
    with pytest.raises(AttributeError):
        Rectangle(0, 2)


def test_rectangle_angles():
    rectangle = Rectangle(3, 4)
    assert rectangle.angles == 4


@pytest.mark.parametrize("length, width, perimeter",
                         [(3, 4, 14),
                          (1, 1, 4),
                          (2, 4, 12)],
                         ids=["sides: 3, 4; perimeter: 14",
                              "sides: 1, 1; perimeter: 4",
                              "sides: 2, 4; perimeter: 12"])
def test_rectangle_perimeter(length, width, perimeter):
    rectangle = Rectangle(length, width)
    assert rectangle.perimeter == perimeter


@pytest.mark.parametrize("length, width, area",
                         [(3, 4, 12),
                          (1, 9, 9),
                          (2, 4, 8)],
                         ids=["sides: 3, 4; area: 12",
                              "sides: 1, 9; area: 9",
                              "sides: 2, 4; area: 8"])
def test_rectangle_area(length, width, area):
    rectangle = Rectangle(length, width)
    assert rectangle.area == area


def test_add_area_of_another_figure():
    rectangle = Rectangle(3, 6)
    square = Square(4)
    assert rectangle.add_area(square) == 34.0


def test_add_square_of_not_a_figure():
    rectangle = Rectangle(3, 6)
    with pytest.raises(AttributeError):
        rectangle.add_area(0)
