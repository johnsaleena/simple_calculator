import unittest

from Calculator.calculator import Calculator
from CsvReader.CsvReader import CsvReader


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_add_method_calculator(self):
            test_data = CsvReader("Tests/Data/addition.csv").data
            for row in test_data:
                self.assertEqual(self.calculator.add(int(row['Value 1']), int(row['Value 2'])), int(row['Result']))
                self.assertEqual(self.calculator.result, int(row['Result']))

    def test_subtract_method_calculator(self):
            test_data = CsvReader("Tests/Data/subtraction.csv").data
            for row in test_data:
                self.assertEqual(self.calculator.subtract(int(row['Value 2']), int(row['Value 1'])), int(row['Result']))
                self.assertEqual(self.calculator.result, int(row['Result']))

    def test_multiply_method_calculator(self):
            test_data = CsvReader("Tests/Data/multiplication.csv").data
            for row in test_data:
                self.assertEqual(self.calculator.multiply(int(row['Value 1']), int(row['Value 2'])), int(row['Result']))
                self.assertEqual(self.calculator.result, int(row['Result']))

    def test_divide_method_calculator(self):
            test_data = CsvReader("Tests/Data/division.csv").data
            for row in test_data:
                x = float(row['Result'])
                self.assertEqual(self.calculator.divide(int(row['Value 2']), int(row['Value 1'])), round(x, 7))
                self.assertEqual(self.calculator.result, round(x, 7))

    def test_square_method_calculator(self):
            test_data = CsvReader("Tests/Data/square.csv").data
            for row in test_data:
                self.assertEqual(self.calculator.squaring(int(row['Value 1'])), int(row['Result']))
                self.assertEqual(self.calculator.result, int(row['Result']))

    def test_square_rt_method_calculator(self):
            test_data = CsvReader("Tests/Data/square_root.csv").data
            for row in test_data:
                y = float(row['Result'])
                self.assertEqual(self.calculator.square_rt(int(row['Value 1'])), round(y, 7))
                self.assertEqual(self.calculator.result, round(y, 7))

    if __name__ == '__main__':
        unittest.main()
