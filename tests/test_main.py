import pytest
import math
from main import calculate_radius


@pytest.mark.parametrize("args, expected", [
    ((1, 1, 1), 0.43),
    ((2, 2, 1), 0.97),
    ((4, 3, 5), 6.00),
    ((1,), round(math.pi, 2)),
    ((2,), 12.57),
    ((0,), 0),
])
def test_calculate_radius(args, expected):
    assert calculate_radius(*args) == expected
