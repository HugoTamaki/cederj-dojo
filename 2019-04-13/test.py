import unittest
from fizzbuzz import *

class TestFizzBuzz(unittest.TestCase):
    def test_fizz_buzz_1(self):
        self.assertEqual(fizz_buzz(1), 1)

    def test_fizz_buzz_2(self):
        self.assertEqual(fizz_buzz(2), 2)

    def test_fizz_buzz_3(self):
        self.assertEqual(fizz_buzz(3), "Fizz")

    def test_fizz_buzz_4(self):
        self.assertEqual(fizz_buzz(4), 4)

    def test_fizz_buzz_5(self):
        self.assertEqual(fizz_buzz(5), "Buzz")

    def test_fizz_buzz_6(self):
        self.assertEqual(fizz_buzz(6), "Fizz")

    def test_fizz_buzz_7(self):
        self.assertEqual(fizz_buzz(7), 7)

    def test_fizz_buzz_8(self):
        self.assertEqual(fizz_buzz(8), 8)

    def test_fizz_buzz_9(self):
        self.assertEqual(fizz_buzz(9), "Fizz")

    def test_fizz_buzz_10(self):
        self.assertEqual(fizz_buzz(10), "Buzz")

    def test_fizz_buzz_12(self):
        self.assertEqual(fizz_buzz(12), "Fizz")

    def test_fizz_buzz_15(self):
        self.assertEqual(fizz_buzz(15), "FizzBuzz")

unittest.main()

