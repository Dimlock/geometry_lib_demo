from geometry.shapes.triangle import Triangle
import pytest


@pytest.mark.parametrize("sides, expected", [
    ((1, 1, 1), 0.43),
    ((2, 2, 1), 0.97),
    ((4, 3, 5), 6.00),
])
def test_triangle_area(sides, expected):
    assert Triangle(*sides).area() == expected


@pytest.mark.parametrize("sides, expected", [
    ((1, 1, 1), False),
    ((2, 2, 1), False),
    ((4, 3, 5), True),
    ((1, 1, 2 ** (1 / 2)), True)
])
def test_is_right(sides, expected):
    assert Triangle(*sides).is_right() == expected
