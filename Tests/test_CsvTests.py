import unittest
from CsvReader import CsvReader


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.csv_reader = CsvReader()


if __name__ == '__main__':
    unittest.main()
