from base import Figure
from math import pi


class Circle(Figure):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return pi * self.radius ** 2
