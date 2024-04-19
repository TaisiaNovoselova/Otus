from src.rectangle import Rectangle
from src.square import Square
from src.triangle import Triangle
from src.circle import Circle
import pytest


@pytest.mark.rectangle
@pytest.mark.parametrize("value", ["int_area", "float_area"],
                         ids=["int_area", "float_area"])
def test_rectangle_area(get_rectangle_area, value):
    a, b, result = get_rectangle_area(value=value)
    r = Rectangle(a, b)
    assert r.get_area() == result


@pytest.mark.rectangle
@pytest.mark.parametrize("value", ["int_perimetr", "float_perimetr"],
                         ids=["int_perimetr", "float_perimetr"])
def test_rectangle_perimetr(get_rectangle_perimetr, value):
    a, b, result = get_rectangle_perimetr(value=value)
    r = Rectangle(a, b)
    assert r.get_perimetr() == result


@pytest.mark.rectangle
def test_rectangle_is_exist():
    with pytest.raises(ValueError):
        Rectangle(0, 5)


@pytest.mark.square
@pytest.mark.parametrize("value", ["int_area", "float_area"],
                         ids=["int_area", "float_area"])
def test_square_area(get_square_area, value):
    a, result = get_square_area(value=value)
    r = Square(a)
    assert r.get_area() == result


@pytest.mark.square
@pytest.mark.parametrize("value", ["int_perimetr", "float_perimetr"],
                         ids=["int_perimetr", "float_perimetr"])
def test_square_perimetr(get_square_perimetr, value):
    a, result = get_square_perimetr(value=value)
    r = Square(a)
    assert r.get_perimetr() == result


@pytest.mark.square
def test_square_is_exist():
    with pytest.raises(ValueError):
        Square(-9)


@pytest.mark.square
@pytest.mark.parametrize("value", ["int_area", "float_area"],
                         ids=["int_sum_area_square_rectangle", "float_sum_area_square_rectangle"])
def test_square_add_area(get_rectangle_area, get_square_area, get_sum_area_square_rectangle, value):
    a, b, rectangle_area = get_rectangle_area(value=value)  # How to simplify code?
    # I guess that I can reuse results of previous tests
    r = Rectangle(a, b)

    a, square_area = get_square_area(value=value)
    s = Square(a)
    result = get_sum_area_square_rectangle(value=value)
    assert s.add_area(r) == result


@pytest.mark.triangle
@pytest.mark.parametrize("value", ["int_area", "float_area"],
                         ids=["int_area", "float_area"])
def test_triangle_area(get_triangle_area, value):
    a, b, c, result = get_triangle_area(value=value)
    r = Triangle(a, b, c)
    assert r.get_area() == result


@pytest.mark.triangle
@pytest.mark.parametrize("value", ["int_perimetr", "float_perimetr"],
                         ids=["int_perimetr", "float_perimetr"])
def test_triangle_perimetr(get_triangle_perimetr, value):
    a, b, c, result = get_triangle_perimetr(value=value)
    r = Triangle(a, b, c)
    assert r.get_perimetr() == result


@pytest.mark.triangle
def test_triangle_is_exist():
    with pytest.raises(ValueError):
        Triangle(-9, 5, 7)


@pytest.mark.triangle
@pytest.mark.parametrize("value", ["int_area", "float_area"],
                         ids=["int_sum_area_triangle_square", "float_sum_area_triangle_square"])
def test_triangle_add_area(get_square_area, get_triangle_area, get_sum_area_triangle_square, value):
    a, square_area = get_square_area(value=value)
    s = Square(a)
    a, b, c, triangle_area = get_triangle_area(value=value)
    t = Triangle(a, b, c)
    result = get_sum_area_triangle_square(value=value)
    assert t.add_area(s) == result


@pytest.mark.circle
@pytest.mark.parametrize("value", ["int_area", "float_area"],
                         ids=["int_area", "float_area"])
def test_circle_area(get_circle_area, value):
    a, result = get_circle_area(value=value)
    r = Circle(a)
    assert r.get_area() == result


@pytest.mark.circle
@pytest.mark.parametrize("value", ["int_perimetr", "float_perimetr"],
                         ids=["int_perimetr", "float_perimetr"])
def test_circle_perimetr(get_circle_perimetr, value):
    a, result = get_circle_perimetr(value=value)
    r = Circle(a)
    assert r.get_perimetr() == result


@pytest.mark.circle
def test_circle_is_exist():
    with pytest.raises(ValueError):
        Circle(-9)


@pytest.mark.circle
@pytest.mark.parametrize("value", ["int_area", "float_area"],
                         ids=["int_sum_area_circle_triangle", "float_sum_area_circle_triangle"])
def test_circle_add_area(get_triangle_area, get_circle_area, get_sum_area_circle_triangle, value):
    a, b, c, triangle_area = get_triangle_area(value=value)
    t = Triangle(a, b, c)
    a, circle_area = get_circle_area(value=value)
    r = Circle(a)
    result = get_sum_area_circle_triangle(value=value)
    assert r.add_area(t) == result
