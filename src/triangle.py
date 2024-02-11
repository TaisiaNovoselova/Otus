import math
from figure import Figure
from square import square


class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c):
        super().__init__(Triangle.__name__)
        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError("Нельзя создать треугольник, одна из сторон <= 0")
        if (side_a + side_b < side_c or side_a + side_c < side_b
                or side_b + side_c < side_a):
            raise ValueError("Треугольник с заданными сторонами не существует")
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def get_perimetr(self):
        perimetr = self.side_a + self.side_b + self.side_c
        return perimetr

    def get_area(self):
        per = Triangle.get_perimetr(triangle) / 2
        area = math.sqrt(per * (per - self.side_a) * (per - self.side_b) * (per - self.side_c))
        return area


triangle = Triangle(5, 6, 10)
triangle.add_area(square)
