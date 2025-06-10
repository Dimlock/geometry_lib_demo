from .base import FigureCreator
from geometry.shapes.circle import Circle


class CircleCreator(FigureCreator):
    def __init__(self, radius: float):
        self.radius = radius

    def create_figure(self) -> Circle:
        return Circle(self.radius)
