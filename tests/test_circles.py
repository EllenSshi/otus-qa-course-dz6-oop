import pytest
from source.figure import Circle, Triangle


def test_create_circle_with_proper_side():
    circle = Circle([0, 0], [3, 5])
    assert circle.name == "Круг"


def test_create_circle_with_bad_side():
    with pytest.raises(AttributeError):
        Circle([1, 1], [1, 1])


def test_circle_angles():
    circle = Circle([0, 0], [3, 5])
    assert circle.angles == 0


@pytest.mark.parametrize("center_point, circle_point, perimeter",
                         [([0, 0], [3, 5], 36),
                          ([0, 0], [3, 4], 31),
                          ([1, 1], [6, 6], 45)])
def test_circle_perimeter(center_point, circle_point, perimeter):
    circle = Circle(center_point, circle_point)
    assert circle.perimeter == perimeter


@pytest.mark.parametrize("center_point, circle_point, area",
                         [([0, 0], [3, 5], 105.7),
                          ([0, 0], [3, 4], 78.5),
                          ([1, 1], [6, 6], 158.4)])
def test_circle_area(center_point, circle_point, area):
    circle = Circle(center_point, circle_point)
    assert circle.area == area


def test_add_area_of_another_figure():
    circle = Circle([0, 0], [3, 5])
    triangle = Triangle([1, -2], [0.5, -4], [6, -3])
    assert circle.add_area(triangle) == 111.0


def test_add_square_of_not_a_figure():
    circle = Circle([0, 0], [3, 5])
    with pytest.raises(AttributeError):
        circle.add_area("add some area = 10")
