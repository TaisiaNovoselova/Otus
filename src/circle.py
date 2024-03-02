import math
from figure import Figure
from triangle import triangle


class Circle(Figure):
    def __init__(self, side_a):
        super().__init__(Circle.__name__)
        if side_a <= 0:
            raise ValueError("Нельзя создать круг, радиус <= 0")
        self.side_a = side_a

    def get_perimetr(self):
        perimetr = 2 * math.pi * self.side_a
        return perimetr

    def get_area(self):
        area = math.pi * self.side_a**2
        return area


circle = Circle(5)
circle.add_area(triangle)
