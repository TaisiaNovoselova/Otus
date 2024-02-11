from figure import Figure
from rectangle import rectangle


class Square(Figure):
    def __init__(self, side_a):
        super().__init__(Square.__name__)
        if side_a <= 0:
            raise ValueError("нельзя создать квадрат")
        self.side_a = side_a

    def get_area(self):
        return self.side_a * self.side_a

    def get_perimetr(self):
        return 2 * (self.side_a + self.side_a)


square = Square(3)
square.add_area(rectangle)
