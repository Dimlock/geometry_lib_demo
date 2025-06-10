import math

import pytest
from geometry.shapes.circle import Circle


@pytest.mark.parametrize("radius, expected", [
    (1, round(math.pi, 2)),
    (2, 12.57),
    (0, 0),
])
def test_circle_area(radius, expected):
    assert Circle(radius).area() == expected
