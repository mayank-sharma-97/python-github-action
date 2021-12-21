# encoding=utf-8
# Program makes a simple calculator
from decimal import Decimal

class Calculator:

    @staticmethod
    def addition(a, b):
        return a + b

    @staticmethod
    def subtraction(a, b):
        return a - b

    @staticmethod
    def multiplication(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        if b == 0:
            return "Can not be divided by zero"
        else:
            return a / b

    @staticmethod
    def sum(*args):
        return sum(args)