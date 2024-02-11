from abc import ABC, abstractmethod


class Figure(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_area(self):
        """Функция вычисляет площадь фигуры"""
        pass

    @abstractmethod
    def get_perimetr(self):
        """Функция вычисляет периметр фигуры"""
        pass

    def add_area(self, other_figure):
        """Функция вычисляет сумму периметров двух фигур"""
        if not isinstance(self, Figure):
            raise ValueError("Нужно передать фигуру")
        return self.get_area() + other_figure.get_area()
