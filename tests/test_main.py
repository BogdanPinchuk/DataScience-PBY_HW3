import unittest
import io
import random as rnd

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
        expected = "\t*************************\n\t*************************\n\t*************************\n\t*************************\n\t*************************"
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


class TestCountPos(TestCase):
    def test_count_positive(self):
        numbers = [i for i in range(-10, 11)]
        actual = count_positive(numbers)
        expected = 10
        self.assertEqual(expected, actual)

    def test_count_positive_empty_array(self):
        numbers = []

        # wait the exception
        with self.assertRaises(ValueError) as context:
            _ = count_positive(numbers)

        expected = 'Input array is empty!'
        self.assertEqual(expected, str(context.exception))


class TestNumberType(TestCase):
    def test_number_type_pos(self):
        numbers = 1
        actual = number_type(numbers)
        expected = 'positive'
        self.assertEqual(expected, actual)

    def test_number_type_neg(self):
        numbers = -1
        actual = number_type(numbers)
        expected = 'negative'
        self.assertEqual(expected, actual)

    def test_number_type_zero(self):
        numbers = 0
        actual = number_type(numbers)
        expected = 'zero'
        self.assertEqual(expected, actual)


class TestMaxInList(TestCase):
    def test_max_in_list(self):
        lower = -100
        upper = 100
        count_nums = 10
        numbers = [rnd.randrange(lower, upper + 1) for _ in range(count_nums)]
        actual = max_in_list(numbers)
        expected = max(numbers)
        self.assertEqual(expected, actual)

    def test_max_in_list_empty_array(self):
        numbers = []
        actual = max_in_list(numbers)
        expected = None
        self.assertEqual(expected, actual)


class TestFuncF(TestCase):
    def test_f(self):
        value = 24
        actual = f(value)
        expected = 0.2
        self.assertEqual(expected, actual)

    def test_f_zero_error(self):
        value = -1

        # intercept data output
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            _ = f(value)

        actual = buffer.getvalue().strip()
        expected = 'Значення "-1" призводить до ділення на нуль!'
        self.assertEqual(expected, actual)

    def test_f_complex_error(self):
        value = -3

        # intercept data output
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            _ = f(value)

        actual = buffer.getvalue().strip()
        expected = 'Значення "-3" призводить до комплексного результату!'
        self.assertEqual(expected, actual)


class TestAnalyzeEvenInNumList(TestCase):
    def test_analyze_even_in_num_list(self):
        numbers = [1, 2, 3, 4, 5, 6, 7, 8]
        actual_list, actual_report = analyze_even_in_num_list(numbers)
        expected_report = """Number | Is even 
----------------
1      | False    
2      | True     
3      | False    
4      | True     
5      | False    
6      | True     
7      | False    
8      | True     
----------------
Список тільки парних чисел: [2, 4, 6, 8]"""
        expected_list = [2, 4, 6, 8]
        self.assertEqual(expected_list, actual_list)
        self.assertEqual(expected_report, actual_report)

    def test_analyze_even_in_num_list_empty_array(self):
        numbers = []

        # wait the exception
        with self.assertRaises(ValueError) as context:
            _ = analyze_even_in_num_list(numbers)

        expected = 'Input array is empty!'
        self.assertEqual(expected, str(context.exception))
