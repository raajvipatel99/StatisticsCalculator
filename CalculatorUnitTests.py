import unittest
from calculator import Calculatorr
from CSVReader import CsvReader


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculatorr()

    def test_instance(self):
        self.assertIsInstance(self.calculator, Calculatorr)

    def test_addition(self):
        test_data = CsvReader('/src/Unit Test Addition.csv').data
        for row in test_data:
            self.assertAlmostEqual(self.calculator.add(row['Value 1'], row['Value 2']), float(row['Result']), 0)

    def test_subtraction(self):
        test_data = CsvReader('/src/Unit Test Subtraction.csv').data
        for row in test_data:
            self.assertAlmostEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), float(row['Result']), 0)

    def test_multiplication(self):
        test_data = CsvReader('/src/Unit Test Multiplication.csv').data
        for row in test_data:
            self.assertAlmostEqual(self.calculator.multiply(row['Value 1'], row['Value 2']), float(row['Result']), 0)

    def test_division(self):
        test_data = CsvReader('/src/Unit Test Division.csv').data
        for row in test_data:
            self.assertAlmostEqual(self.calculator.divide(row['Value 1'], row['Value 2']), float(row['Result']), 0)

    def test_square(self):
        test_data = CsvReader('/src/Unit Test Square.csv').data
        for row in test_data:
            self.assertAlmostEqual(self.calculator.square(row['Value 1']), float(row['Result']), 0)

    def test_squareroot(self):
        test_data = CsvReader('/src/Unit Test Square Root.csv').data
        for row in test_data:
            self.assertAlmostEqual(self.calculator.squareroot(row['Value 1']), float(row['Result']), 0)



if __name__ == '__main__':
    unittest.main()
