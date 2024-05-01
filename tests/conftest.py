import pytest


@pytest.fixture()
def get_rectangle_area():

    def _wrapper(value: str):
        if value == "int_area":
            return 3, 5, 15
        elif value == "float_area":
            return 3.5, 5.5, 19.25
        else:
            raise AssertionError("Only int or float")

    yield _wrapper


@pytest.fixture()
def get_rectangle_perimetr():

    def _wrapper(value: str):
        if value == "int_perimetr":
            return 6, 2, 16
        elif value == "float_perimetr":
            return 6.5, 2.4, 17.8
        else:
            raise AssertionError("Only int or float")

    yield _wrapper


@pytest.fixture()
def get_square_area():

    def _wrapper(value: str):
        if value == "int_area":
            return 5, 25
        elif value == "float_area":
            return 5.5, 30.25
        else:
            raise AssertionError("Only int or float")

    yield _wrapper


@pytest.fixture()
def get_square_perimetr():

    def _wrapper(value: str):
        if value == "int_perimetr":
            return 5, 20
        elif value == "float_perimetr":
            return 5.5, 22
        else:
            raise AssertionError("Only int or float")

    yield _wrapper


@pytest.fixture()
def get_sum_area_square_rectangle():

    def _wrapper(value: str):
        if value == "int_area":
            return 40
        elif value == "float_area":
            return 49.5
        else:
            raise AssertionError("Only int or float")

    yield _wrapper


@pytest.fixture()
def get_triangle_area():

    def _wrapper(value: str):
        if value == "int_area":
            return 5, 3, 4, 6
        elif value == "float_area":
            return 4.1, 3.3, 5.2, 6.762987505533334
        else:
            raise AssertionError("Only int or float")

    yield _wrapper


@pytest.fixture()
def get_triangle_perimetr():

    def _wrapper(value: str):
        if value == "int_perimetr":
            return 5, 4, 5, 14
        elif value == "float_perimetr":
            return 5.5, 7.1, 4.8, 17.4
        else:
            raise AssertionError("Only int or float")

    yield _wrapper


@pytest.fixture()
def get_sum_area_triangle_square():

    def _wrapper(value: str):
        if value == "int_area":
            return 31
        elif value == "float_area":
            return 37.01298750553333
        else:
            raise AssertionError("Only int or float")

    yield _wrapper


@pytest.fixture()
def get_circle_area():

    def _wrapper(value: str):
        if value == "int_area":
            return 3, 28.274333882308138
        elif value == "float_area":
            return 4.8, 72.38229473870884
        else:
            raise AssertionError("Only int or float")

    yield _wrapper


@pytest.fixture()
def get_circle_perimetr():

    def _wrapper(value: str):
        if value == "int_perimetr":
            return 3, 18.84955592153876
        elif value == "float_perimetr":
            return 2.3, 14.451326206513047
        else:
            raise AssertionError("Only int or float")

    yield _wrapper


@pytest.fixture()
def get_sum_area_circle_triangle():

    def _wrapper(value: str):
        if value == "int_area":
            return 34.27433388230814
        elif value == "float_area":
            return 79.14528224424217
        else:
            raise AssertionError("Only int or float")

    yield _wrapper
