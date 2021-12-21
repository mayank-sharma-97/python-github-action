# coding=utf-8
from src.calculator import calculator
import pytest


class TestCalculator:

    @pytest.fixture(scope="session")
    def setup_calculator(self):
        print("Calculator initialize")
        return calculator()

    # Another solution if setup_calculator is inside the same class
    def test_addition(self, setup_calculator):
        assert calculator.addition(2, 1) == 3

    def test_addition(self):
        assert calculator.addition(2, 1) == 3

    def test_subtraction(self):
        assert calculator.subtraction(2, 3) == -1

    def test_multiplication(self):
        assert calculator.multiplication(1.5, 1.5) == 2.25

    @pytest.mark.xfail(condition=lambda: True, reason='this test is expecting failure')
    def test_divide(self):
        assert calculator.divide(0.3, 0.1) == 3.0

    def test_sum(self):
        assert calculator.sum(1, 2, 3) == 6

    @pytest.mark.parametrize('first, second, expect', [
        (2, 1, 2),
        (3, 1, 3)
    ])
    def test_division(self, first, second, expect):
        assert calculator.divide(first, second) == expect

    @staticmethod
    def tear_down(self):
        print("tear down")

    @staticmethod
    def teardown_class(self):
        print("teardown class")