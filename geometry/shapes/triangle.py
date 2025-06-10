from base import Figure


class Triangle(Figure):
    def __init__(self, *sides: float):
        if len(sides) != 3:
            raise ValueError("У треугольника только 3 стороны!")
        self.sides = sides

    def area(self) -> float:
        p = sum(self.sides) / 2
        return (p * (p - self.sides[0]) * (p - self.sides[1]) * (p - self.sides[2])) ** (1 / 2)

    def is_right(self):
        if len(set(self.sides)) != 3:
            return False
        else:
            longest_side_index = max(enumerate(self.sides), key=lambda x: x[1])[0]
            return self.sides[longest_side_index] ** 2 == sum([i**2 for i in self.sides if i != self.sides[longest_side_index]])
