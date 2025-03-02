import unittest
import pytest
from homeworks import *

# unittest 1-3 tesks
class Test_multiplication_table(unittest.TestCase):
    def test_positive(self):
        result = multiplication_table(3)
        self.assertEqual(result, ['3x1=3', '3x2=6', '3x3=9', '3x4=12', '3x5=15', '3x6=18', '3x7=21', '3x8=24'])
        result = multiplication_table(1)
        self.assertEqual(result, ['1x1=1', '1x2=2', '1x3=3', '1x4=4', '1x5=5', '1x6=6', '1x7=7', '1x8=8', '1x9=9',
                                  '1x10=10', '1x11=11', '1x12=12', '1x13=13', '1x14=14', '1x15=15', '1x16=16', '1x17=17',
                                  '1x18=18', '1x19=19', '1x20=20', '1x21=21', '1x22=22', '1x23=23', '1x24=24', '1x25=25'])
        result = multiplication_table(25)
        self.assertEqual(result, ['25x1=25'])
        result = multiplication_table(24)
        self.assertEqual(result, ['24x1=24'])
    def test_negative(self):
        with self.assertRaises(ValueError):
            multiplication_table(-1)
        with self.assertRaises(ValueError):
            multiplication_table(0)
        with self.assertRaises(TypeError):
            multiplication_table(None)
        with self.assertRaises(TypeError):
            multiplication_table('text')
        with self.assertRaises(TypeError):
            multiplication_table(3.5)
    def test_max(self):
            result = multiplication_table(26)
            self.assertEqual(result, [])

class Test_list_avg(unittest.TestCase):
    def test_positive(self):
        result = list_avg([1, 2, 3, 4, 5.5])
        self.assertEqual(result, 3.1)
        result = list_avg([1, 2, 3, -4, -5])
        self.assertEqual(result, -0.6)
        result = list_avg([-1])
        self.assertEqual(result, -1.0)
        result = list_avg([0])
        self.assertEqual(result, 0.0)
        result = list_avg([1])
        self.assertEqual(result, 1.0)
    def test_wrong_input(self):
        with self.assertRaises(TypeError):
            list_avg(())
        with self.assertRaises(TypeError):
            list_avg({})
        with self.assertRaises(TypeError):
            list_avg(2)
        with self.assertRaises(TypeError):
            list_avg(2.2)
        with self.assertRaises(TypeError):
            list_avg('text')
        with self.assertRaises(TypeError):
            list_avg()
    def test_wrong_inTheList(self):
        test_values = [[1, 2, 3, 4, 's'],
                       [1, 2, 3, 4, [1]],
                       [1, 2, 3, 4, {3}],
                       [1, 2, 3, 4, None],
                       [1, 2, 3, 4, (3, 4)]]
        for value in test_values:
            with self.assertRaises(TypeError):
                list_avg(value)
        with self.assertRaises(ValueError):
            list_avg([])

class Test_string_reverse(unittest.TestCase):
    def test_posive(self):
        result = string_reverse('hello word')
        self.assertEqual(result, 'drow olleh')
    def test_negative(self):
        test_values = [(), [], {}, None, 576]
        for value in test_values:
            with self.assertRaises(TypeError):
                string_reverse(value)

# pytest 4-5 tasks
class TestGroupedStrFiltering:
    @pytest.mark.parametrize("test_input, expected", [
        (['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum', ('Lorem Ipsum', 2), {'key': 'value'}, [1,2]],
         ['1', '2', 'False', '6', 'Python', 'Lorem Ipsum']),
        ([True, 3], []),
    ])
    def test_str_filtering(self, test_input, expected):
        assert str_filtering(test_input) == expected
    @pytest.mark.parametrize("test_input, expected_error", [
        ([], "The input list cannot be empty."),
        (None, "The input must be a list."),
        ("string", "The input must be a list."),
        (123, "The input must be a list."),
        (2.2, "The input must be a list."),
        ({}, "The input must be a list."),
        ((), "The input must be a list."),
    ])
    def test_type_and_empty_list_error(self, test_input, expected_error):
        with pytest.raises((ValueError, TypeError)) as exc_info:
            str_filtering(test_input)
        assert str(exc_info.value) == expected_error


class TestGroupedSumOfDigits:
    @pytest.mark.parametrize("test_input, expected", [
        (12345, "The sum of the digits of the number will be 15"),
        (1, "The sum of the digits of the number will be 1"),
    ])
    def test_sum_of_digits(self, test_input, expected):
        assert sum_of_digits(test_input) == expected
    @pytest.mark.parametrize("test_input, expected_error", [
        (-1, "Input must be a natural number"),
        (0, "Input must be a natural number"),
        (1.1, "Input must be a natural number"),
        ("", "Input must be a natural number"),
        ([], "Input must be a natural number"),
        ((), "Input must be a natural number"),
        ({}, "Input must be a natural number"),
    ])
    def test_negative_sumofdigits(self, test_input, expected_error):
        with pytest.raises((TypeError, ValueError)) as exc_info:
            sum_of_digits(test_input)
        assert str(exc_info.value) == expected_error

if __name__ == '__main__':
    unitest.main()