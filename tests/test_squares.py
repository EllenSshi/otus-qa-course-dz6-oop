import pytest
from source.figure import Square, Circle


def test_create_square_with_proper_side():
    square = Square([1, 1], [1, 0.5])
    assert square.name == "Квадрат"


def test_create_square_with_bad_side():
    with pytest.raises(AttributeError):
        Square([1, 1], [1, 1])


def test_square_angles():
    square = Square([1, 1], [1, 8])
    assert square.angles == 4


@pytest.mark.parametrize("a_point, b_point, perimeter",
                         [([0, 0], [3, 5], 23),
                          ([0, 0], [3, 4], 20),
                          ([1, 1], [6, 6], 28)])
def test_square_perimeter(a_point, b_point, perimeter):
    square = Square(a_point, b_point)
    assert square.perimeter == perimeter


@pytest.mark.parametrize("a_point, b_point, area",
                         [([0, 0], [3, 5], 33.6),
                          ([0, 0], [3, 4], 25.0),
                          ([1, 1], [6, 6], 50.4)])
def test_square_area(a_point, b_point, area):
    square = Square(a_point, b_point)
    assert square.area == area


def test_add_area_of_another_figure():
    square = Square([1, 1], [6, 6])
    circle = Circle([0, 0], [3, 5])
    assert square.add_area(circle) == 156.1


def test_add_square_of_not_a_figure():
    square = Square([1, 1], [6, 6])
    with pytest.raises(AttributeError):
        square.add_area("add some area = 10")
