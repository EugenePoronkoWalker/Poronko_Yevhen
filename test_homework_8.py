""" Задача 1-10 - оберіть декілька домашніх завдань та покрийте їх не менш ніж 10 тестами.
Код закомітьте в гіт, надайте посилання.
На оцінку впливає як якість тестів так і розмір тестового покриття.
Мінімум на 10 балів - 1 правильно задизайнений позитивний тест на функцію.
"""
import unittest
from notes_for_homework8 import *

class TestSumNumbers(unittest.TestCase):

    def test_sum_numbers_1(self):
        """The sum of integer numbers"""
        actual_result = sum_numbers(2, 2)
        expected_result = 4
        self.assertEqual(actual_result, expected_result, "The sum of the numbers 2 and 2 equals 4")


    def test_sum_numbers_2(self):
        """The sum of float numbers"""
        actual_result = sum_numbers(0.5, 1.23)
        expected_result = 1.73
        self.assertEqual(actual_result, expected_result, "The sum of the numbers 0.5 and 1.23 equals 1.73")

    def test_sum_numbers_3(self):
        """The sum of negative numbers"""
        actual_result = sum_numbers(-2, -6)
        expected_result = -8
        self.assertEqual(actual_result, expected_result, "The sum of the numbers -2 and -6 equals -8")

    def test_sum_numbers_4(self):
        """The sum of positive and negative numbers"""
        actual_result = sum_numbers(-15, 6)
        expected_result = -9
        self.assertEqual(actual_result, expected_result, "The sum of the numbers -15 and 6 equals -9")

    def test_sum_numbers_5(self):
        """The sum of float and negative numbers"""
        actual_result = sum_numbers(-15, 61.35)
        expected_result = 46.35
        self.assertEqual(actual_result, expected_result, "The sum of the numbers -15 and 61.35 equals 46.35")

class TestArithmeticAverage(unittest.TestCase):

    def test_arithmetic_average_1(self):
        """The arithmetic average of integers numbers in the list"""
        actual_result = arithmetic_average([1, 2, 3, 6, 7])
        expected_result = 3
        self.assertEqual(actual_result, expected_result)

    def test_arithmetic_average_2(self):
        """"The arithmetic average of float numbers in the list"""
        actual_result = arithmetic_average([0.5, 2.1, 3.6, 6.7, 7.1])
        expected_result = 4
        self.assertEqual(actual_result, expected_result)

    def test_arithmetic_average_3(self):
        """"The arithmetic average of negative numbers in the list"""
        actual_result = arithmetic_average([-2, -15.1, -3.67, -6.7, -7.15])
        expected_result = -6
        self.assertEqual(actual_result, expected_result)

    def test_arithmetic_average_4(self):
        """"The arithmetic average of negative and positive numbers in the list"""
        actual_result = arithmetic_average([2, 21, -3, 7, -7])
        expected_result = 4
        self.assertEqual(actual_result, expected_result)

    def test_arithmetic_average_5(self):
        """"The arithmetic average of diffirent type of data in the list"""
        actual_result = arithmetic_average([2, 21.3, -3, 7, -7])
        expected_result = 4
        self.assertEqual(actual_result, expected_result)

if __name__ == "__main__":
    unittest.main(verbosity=2)
