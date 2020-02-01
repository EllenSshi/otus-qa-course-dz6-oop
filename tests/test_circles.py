import pytest
from source.figure import Circle, Triangle


def test_create_circle_with_proper_side():
    circle = Circle(5)
    assert circle.name == "Круг"


def test_create_circle_with_bad_side():
    with pytest.raises(AttributeError):
        Circle(0)


def test_circle_angles():
    circle = Circle(1)
    assert circle.angles == 0


@pytest.mark.parametrize("radius, perimeter",
                         [(3, 19),
                          (12, 75),
                          (4, 25)],
                         ids=["radius: 3; perimeter: 19",
                              "radius: 12; perimeter: 75",
                              "radius: 4; perimeter: 25"])
def test_circle_perimeter(radius, perimeter):
    circle = Circle(radius)
    assert circle.perimeter == perimeter


@pytest.mark.parametrize("radius, area",
                         [(3, 28.3),
                          (12, 452.4),
                          (4, 50.3)],
                         ids=["radius: 3; area: 28.3",
                              "radius: 12; area: 452.4",
                              "radius: 4; area: 50.3"])
def test_circle_area(radius, area):
    circle = Circle(radius)
    assert circle.area == area


def test_add_area_of_another_figure():
    circle = Circle(4)
    triangle = Triangle(2, 4, 5)
    assert circle.add_area(triangle) == 54.1


def test_add_square_of_not_a_figure():
    circle = Circle(3)
    with pytest.raises(AttributeError):
        circle.add_area("add some area = 10")
