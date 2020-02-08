import pytest
from source.figure import Triangle, Square


def test_create_triangle_with_proper_sides():
    triangle = Triangle([-1, -1], [1, 6], [3, -1])
    assert triangle.name == "Треугольник"


def test_create_triangle_with_bad_sides():
    with pytest.raises(AttributeError):
        Triangle([1, 1], [2, 2], [3, 3])


def test_triangle_angles():
    triangle = Triangle([-1, -1], [1, 6], [3, -1])
    assert triangle.angles == 3


@pytest.mark.parametrize("a_point, b_point, c_point, perimeter",
                         [([-1, -1], [1, 6], [3, -1], 18.6),
                          ([1, 4], [2, -1], [7, 2], 17.2),
                          ([0, 5], [1, 0], [9, 1], 23)])
def test_triangle_perimeter(a_point, b_point, c_point, perimeter):
    triangle = Triangle(a_point, b_point, c_point)
    assert triangle.perimeter == perimeter


@pytest.mark.parametrize("a_point, b_point, c_point, area",
                         [([-1, -1], [1, 6], [3, -1], 14),
                          ([1, 4], [2, -1], [7, 2], 13.9),
                          ([0, 5], [1, 0], [9, 1], 20.6)])
def test_triangle_area(a_point, b_point, c_point, area):
    triangle = Triangle(a_point, b_point, c_point)
    assert triangle.area == area


def test_add_area_of_another_figure():
    triangle = Triangle([-1, -1], [1, 6], [3, -1])
    square = Square([0, 0], [3, 4])
    assert triangle.add_area(square) == 39.0


def test_add_square_of_not_a_figure():
    triangle = Triangle([-1, -1], [1, 6], [3, -1])
    with pytest.raises(AttributeError):
        triangle.add_area(5)
