from base import FigureCreator
from geometry.shapes.triangle import Triangle


class TriangleCreator(FigureCreator):
    def __init__(self, *sides: float):
        self.sides = sides

    def create_figure(self) -> Triangle:
        return Triangle(*self.sides)
