import pytest
from source.figure import Triangle, Square


def test_create_triangle_with_proper_sides():
    triangle = Triangle(2, 4, 5)
    assert triangle.name == "Треугольник"


def test_create_triangle_with_bad_sides():
    with pytest.raises(AttributeError):
        Triangle(1, 2, 3)


def test_triangle_angles():
    triangle = Triangle(3, 4, 5)
    assert triangle.angles == 3


@pytest.mark.parametrize("fside, sside, tside, perimeter",
                         [(3, 4, 5, 12),
                          (1, 1, 1, 3),
                          (2, 4, 5, 11)],
                         ids=["sides: 3, 4, 5; perimeter: 12",
                              "sides: 1, 1, 1; perimeter: 3",
                              "sides: 2, 4, 5; perimeter: 11"])
def test_triangle_perimeter(fside, sside, tside, perimeter):
    triangle = Triangle(fside, sside, tside)
    assert triangle.perimeter == perimeter


@pytest.mark.parametrize("fside, sside, tside, area",
                         [(3, 4, 5, 6.0),
                          (1, 1, 1, 0.4),
                          (2, 4, 5, 3.8)],
                         ids=["sides: 3, 4, 5; area: 12",
                              "sides: 1, 1, 1; area: 3",
                              "sides: 2, 4, 5; area: 11"])
def test_triangle_area(fside, sside, tside, area):
    triangle = Triangle(fside, sside, tside)
    assert triangle.area == area


def test_add_area_of_another_figure():
    triangle = Triangle(4, 6, 7)
    square = Square(4)
    assert triangle.add_area(square) == 28.0


def test_add_square_of_not_a_figure():
    triangle = Triangle(4, 6, 7)
    with pytest.raises(AttributeError):
        triangle.add_area(5)
