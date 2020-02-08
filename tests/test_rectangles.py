import pytest
from source.figure import Rectangle, Square


def test_create_rectangle_with_proper_sides():
    rectangle = Rectangle([1, 5], [1, 1], [7, 1])
    assert rectangle.name == "Прямоугольник"


# def test_create_rectangle_with_bad_sides():
#     with pytest.raises(AttributeError):
#         Rectangle(0, 2)


def test_rectangle_angles():
    rectangle = Rectangle([1, 5], [1, 1], [7, 1])
    assert rectangle.angles == 4


@pytest.mark.parametrize("a_point, b_point, c_point, area",
                         [([1, 5], [1, 1], [7, 1], 24.0),
                          ([1, 4], [1, 1], [7, 1], 18.0),
                          ([0, 5], [0, 0], [9, 0], 45.0)])
def test_rectangle_area(a_point, b_point, c_point, area):
    rectangle = Rectangle(a_point, b_point, c_point)
    assert rectangle.area == area


@pytest.mark.parametrize("a_point, b_point, c_point, perimeter",
                         [([1, 5], [1, 1], [7, 1], 20),
                          ([1, 4], [1, 1], [7, 1], 18),
                          ([0, 5], [0, 0], [9, 0], 28)])
def test_rectangle_perimeter(a_point, b_point, c_point, perimeter):
    rectangle = Rectangle(a_point, b_point, c_point)
    assert rectangle.perimeter == perimeter


def test_add_area_of_another_figure():
    rectangle = Rectangle([0, 5], [0, 0], [9, 0])
    square = Square([-1, 0], [-5, -5])
    assert rectangle.add_area(square) == 86.0


def test_add_square_of_not_a_figure():
    rectangle = Rectangle([1, 5], [1, 1], [7, 1])
    with pytest.raises(AttributeError):
        rectangle.add_area(0)
