import unittest
import io

from unittest import TestCase
from unittest.mock import patch
from contextlib import redirect_stdout
from apps.main import *

if __name__ == '__main__':
    unittest.main()


class TestPrintNumsByRange(TestCase):
    def test_print_numbers_by_range_row(self):
        start = 1
        stop = 10

        # intercept data output
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            print_numbers_by_range(start, stop)

        actual = buffer.getvalue().strip()
        expected = "1, 2, 3, 4, 5, 6, 7, 8, 9, 10"
        self.assertEqual(expected, actual)

    def test_print_numbers_by_range_col(self):
        start = 1
        stop = 10

        # intercept data output
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            print_numbers_by_range(start, stop, is_row=False)
        actual = buffer.getvalue().strip()

        expected = "- 1\n- 2\n- 3\n- 4\n- 5\n- 6\n- 7\n- 8\n- 9\n- 10"
        self.assertEqual(expected, actual)

    def test_print_numbers_by_range_incorrect_range(self):
        start = 10
        stop = 1

        # wait the exception
        with self.assertRaises(ValueError) as context:
            print_numbers_by_range(start, stop)

        expected = 'Incorrect input data for range!'
        self.assertEqual(expected, str(context.exception))

    def test_print_numbers_by_range_incorrect_step(self):
        start = 1
        stop = 10
        step = 0

        # wait the exception
        with self.assertRaises(ValueError) as context:
            print_numbers_by_range(start, stop, step=step)

        expected = 'Incorrect input data for step!'
        self.assertEqual(expected, str(context.exception))


class TestPrintEnteredNums(TestCase):
    @patch("builtins.input", side_effect=["1", "2", "3", "0"])
    def test_print_entered_numbers(self, mock_input):
        # intercept data output
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            print_entered_numbers()

        actual = buffer.getvalue().strip()
        expected = 'Note. To exit, please enter the "0".\n\nEntered number: 1\nEntered number: 2\nEntered number: 3\n\nProgram finished!'
        self.assertEqual(expected, actual)

    @patch("builtins.input", side_effect=["1", "2", "3", "t", "t5", "0"])
    def test_print_entered_numbers_incorrect_input(self, mock_input):
        # intercept data output
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            print_entered_numbers()

        actual = buffer.getvalue().strip()
        expected = 'Note. To exit, please enter the "0".\n\nEntered number: 1\nEntered number: 2\nEntered number: 3\n\nProgram finished!'
        self.assertEqual(expected, actual)


class TestFindDivisor(TestCase):
    def test_find_divisor_prime(self):
        number = 13

        # intercept data output
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            find_divisor(number)

        actual = buffer.getvalue().strip()
        expected = 'Число 13 є простим.'
        self.assertEqual(expected, actual)

    def test_find_divisor_divisor(self):
        number = 12

        # intercept data output
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            find_divisor(number)

        actual = buffer.getvalue().strip()
        expected = 'Перший дільник числа 12 це 2.'
        self.assertEqual(expected, actual)

    def test_find_divisor_incorrect_input(self):
        number = 12.5

        # wait the exception
        with self.assertRaises(ValueError) as context:
            find_divisor(number)

        expected = 'Incorrect input integer number!'
        self.assertEqual(expected, str(context.exception))


class TestPrintOddNums(TestCase):
    def test_print_the_odd_numbers(self):
        start = 1
        stop = 20

        # intercept data output
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            print_odd_numbers(start, stop)

        actual = buffer.getvalue().strip()
        print(actual)
        expected_root = "1, 3, 5, 7, 9, 11, 13, 15, 17, 19"
        expected = f"{expected_root}, \b\b"
        self.assertEqual(expected, actual)
        self.assertTrue(expected_root in actual)

    def test_print_the_odd_numbers_incorrect_range(self):
        start = 20
        stop = 1

        # wait the exception
        with self.assertRaises(ValueError) as context:
            print_odd_numbers(start, stop)

        expected = 'Incorrect input data for range!'
        self.assertEqual(expected, str(context.exception))


class TestPrintRectBySign(TestCase):
    def test_print_rect_by_sign(self):
        n_rows = 5
        m_cols = 25
        sign = '*'
        left_margin = "\t"

        # intercept data output
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            print_rect_by_sign(n_rows, m_cols, sign, left_margin)

        actual = buffer.getvalue().rstrip()
        print(actual)
        expected = "\t*************************\n\t*************************\n\t*************************\n\t*************************\n\t*************************"
        print(expected)
        self.assertEqual(expected, actual)

    def test_print_rect_by_sign_incorrect_input_n(self):
        n_rows = 0
        m_cols = 25

        # wait the exception
        with self.assertRaises(ValueError) as context:
            print_rect_by_sign(n_rows, m_cols)

        expected = 'Incorrect input data!'
        self.assertEqual(expected, str(context.exception))

    def test_print_rect_by_sign_incorrect_input_m(self):
        n_rows = 5
        m_cols = 0

        # wait the exception
        with self.assertRaises(ValueError) as context:
            print_rect_by_sign(n_rows, m_cols)

        expected = 'Incorrect input data!'
        self.assertEqual(expected, str(context.exception))
