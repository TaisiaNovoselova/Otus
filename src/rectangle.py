from figure import Figure
from circle import circle


class Rectangle(Figure):
    def __init__(self, side_a, side_b):
        super().__init__(Rectangle.__name__)
        if side_a <= 0 or side_b <= 0:
            raise ValueError("нельзя создать прямоугольник")
        self.side_a = side_a
        self.side_b = side_b

    def get_area(self):
        return self.side_a * self.side_b

    def get_perimetr(self):
        return 2 * (self.side_a + self.side_b)


rectangle = Rectangle(4, 6)
rectangle.add_area(circle)
