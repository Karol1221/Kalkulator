import unittest
from main import *

class TestCalculator(unittest.TestCase):

    def test_Add(self):
        # given
        a=10
        b=12
        expected=22
        # when
        result= Calculator(10,12,'+')
        #then
        self.assertEqual(result, expected)

    def test_Subtract(self):
        # given
        a = 12
        b = 10
        expected = 2
        # when
        result = Calculator(12, 10,'-')
        # then
        self.assertEqual(result, expected)
    def test_Multiply(self):
        # given
        a = 10
        b = 12
        expected = 120
        # when
        result = Calculator(10, 12,'*')
        # then
        self.assertEqual(result, expected)

    def test_Divide(self):
            # given
            a = 120
            b = 12
            expected = 10
            # when
            result = Calculator(120, 12,'/')
            # then
            self.assertEqual(result, expected)

    def test_typeAdd(self):
        # given
        a = 10
        b = 12
        op = "+"
        expected = int
        # when
        result = type(Calculator(10, 12, '+'))
        # then
        self.assertEqual(result, expected)

    def test_typeSubtract(self):
        # given
        a = 12
        b = 10
        op = "-"
        expected = int
        # when
        result = type(Calculator(12, 10, '-'))
        # then
        self.assertEqual(result, expected)

    def test_typeMultiply(self):
        # given
        a = 12
        b = 10
        op = "*"
        expected = int
        # when
        result = type(Calculator(10, 12, '*'))
        # then
        self.assertEqual(result, expected)

    def test_typeDivide(self):
        # given
        a = 12
        b = 10
        op = "/"
        expected = float
        # when
        result = type(Calculator(10, 12, '/'))
        # then
        self.assertEqual(result, expected)





if __name__ == '__main__':
    unittest.main()


