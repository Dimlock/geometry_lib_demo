from .base import Figure


class Triangle(Figure):
    def __init__(self, *sides: float):
        if len(sides) != 3:
            raise ValueError("У треугольника ровно 3 стороны!")
        self.sides = sides

    def area(self) -> float:
        p = sum(self.sides) / 2
        return round((p * (p - self.sides[0]) * (p - self.sides[1]) * (p - self.sides[2])) ** (1 / 2), 2)

    def is_right(self):
        a, b, c = sorted(self.sides)
        return abs(c ** 2 - (a ** 2 + b ** 2)) < 1e-9