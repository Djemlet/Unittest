import unittest

from calculator import calc


class TestCalc(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(5.0,calc("+", 2, 3))
        self.assertEqual(5.0, calc("+", 3, 2))

    def test_subtraction(self):
        self.assertEqual(3.0,calc("-", 5, 2))
        self.assertEqual( -3.0, calc("-", 2, 5))

    def test_multiplication(self):

        self.assertEqual(8.0,calc("*", 4, 2))
        self.assertEqual(8.0, calc("*", 2, 4))

    def test_minnum(self):
        self.assertEqual(0.000000100000001, calc("+", 0.000000000000001, 0.0000001))

    def test_maxnum(self):
        self.assertEqual(1999999999999999999998, calc("+", 999999999999999999999, 999999999999999999999))

    def test_division(self):
        self.assertEqual(3.0,calc("/", 6, 2))
        self.assertEqual(0.333333, calc("/", 6, 2))

    def test_division_by_zero(self):
        self.assertEqual("Деление на ноль!",calc("/", 4, 0))
        self.assertEqual("Деление на ноль!",calc("/", 0, 4))


if __name__ == "__main__":
    unittest.main()
