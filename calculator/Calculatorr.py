from calculator.Addition import Addition
from calculator.Subtraction import Subtraction
from calculator.Multiplication import Multiplication
from calculator.Division import Division
from calculator.Square import Square
from calculator.SquareRoot import SquareRoot


class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = Addition.addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = Subtraction.subtraction(a, b)
        return self.result

    def divide(self, a, b):
        self.result = Division.division(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = Multiplication.multiplication(a, b)
        return self.result

    def square(self, a):
        self.result = Square.square(a)
        return self.result

    def squareroot(self, a):
        self.result = SquareRoot.squareroot(a)
        return self.result
