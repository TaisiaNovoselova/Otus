from abc import ABC, abstractmethod


class Figure(ABC):
    def __init__(self, name):
        self.name = name

    def get_area(self):
        """Функция вычисляет площадь фигуры"""
        raise NotImplementedError("Use get_area to calculate figure area")

    def get_perimetr(self):
        """Функция вычисляет периметр фигуры"""
        raise NotImplementedError("Use get_perimetr to calculate figure perimetr")

    def add_area(self, other_figure):
        """Функция вычисляет сумму периметров двух фигур"""
        if not isinstance(self, Figure):
            raise ValueError("Нужно передать фигуру")
        return self.get_area() + other_figure.get_area()
