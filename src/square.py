from src.rectangle import Rectangle, rectangle


class Square(Rectangle):
    def __init__(self, side_a):
        if side_a <= 0:
            raise ValueError("нельзя создать квадрат")
        super().__init__(side_a, side_a)


square = Square(3)
square.add_area(rectangle)

