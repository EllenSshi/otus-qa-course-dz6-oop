import pytest
from source.figure import Square, Circle


def test_create_square_with_proper_side():
    square = Square(5)
    assert square.name == "Квадрат"


def test_create_square_with_bad_side():
    with pytest.raises(AttributeError):
        Square(-8)


def test_square_angles():
    square = Square(1)
    assert square.angles == 4


@pytest.mark.parametrize("side, perimeter",
                         [(3, 12),
                          (12, 48),
                          (4, 16)],
                         ids=["side: 3; perimeter: 12",
                              "side: 12; perimeter: 48",
                              "side: 4; perimeter: 16"])
def test_square_perimeter(side, perimeter):
    square = Square(side)
    assert square.perimeter == perimeter


@pytest.mark.parametrize("side, area",
                         [(3, 9),
                          (12, 144),
                          (4, 16)],
                         ids=["side: 3; area: 9",
                              "side: 12; area: 144",
                              "side: 4; area: 16"])
def test_square_area(side, area):
    square = Square(side)
    assert square.area == area


def test_add_area_of_another_figure():
    square = Square(3)
    circle = Circle(4)
    assert square.add_area(circle) == 59.3


def test_add_square_of_not_a_figure():
    square = Square(3)
    with pytest.raises(AttributeError):
        square.add_area("add some area = 10")
