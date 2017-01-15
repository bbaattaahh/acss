import unittest

from BucketNumbersCorrector import BucketNumbersCorrector


class TestBucketNumbersCorrector(unittest.TestCase):
    def test_filter_out_not_digit_characters_working(self):
        # given
        bucket_numbers = [["001", ""], ["002", ""], ["003", "004"], ["", "005"]]
        bucket_numbers_corrector = BucketNumbersCorrector(bucket_numbers,
                                                          max_bucket_number=None)
        expected_eliminated_empty_strings = [["001", "002"], ["002", "003"], ["003", "004"], ["004", "005"]]

        # when
        actual_eliminated_empty_strings = bucket_numbers_corrector.eliminate_empty_strings()

        # that
        self.assertEqual(actual_eliminated_empty_strings, expected_eliminated_empty_strings)

    def test_int_bucket_numbers_working(self):
        # given
        bucket_numbers = [["001", ""], ["", "003"], ["003", "004"], ["004", "005"]]
        bucket_numbers_corrector = BucketNumbersCorrector(bucket_numbers,
                                                          max_bucket_number=None)
        expected_int_bucket_numbers = [[1, None], [None, 3], [3, 4], [4, 5]]

        # when
        actual_int_bucket_numbers = bucket_numbers_corrector.int_bucket_numbers

        # that
        self.assertEqual(actual_int_bucket_numbers, expected_int_bucket_numbers)

    def test_number_to_3digit_string_1_digit_number(self):
        # given
        number = 1
        expected_string = "001"

        # when
        actual_string = BucketNumbersCorrector.number_to_3digit_string(number)

        # that
        self.assertEqual(actual_string, expected_string)

    def test_number_to_3digit_string_2_digit_number(self):
        # given
        number = 12
        expected_string = "012"

        # when
        actual_string = BucketNumbersCorrector.number_to_3digit_string(number)

        # that
        self.assertEqual(actual_string, expected_string)

    def test_number_to_3digit_string_3_digit_number(self):
        # given
        number = 123
        expected_string = "123"

        # when
        actual_string = BucketNumbersCorrector.number_to_3digit_string(number)

        # that
        self.assertEqual(actual_string, expected_string)

    def test_number_to_3digit_string_4_digit_number_or_more(self):
        # given
        number = 1234
        expected_string = "1234"

        # when
        actual_string = BucketNumbersCorrector.number_to_3digit_string(number)

        # that
        self.assertEqual(actual_string, expected_string)

    def test_next_number_at_counter_roll_over(self):
        # given
        max_bucket_number = 100
        number = 100
        bucket_numbers_corrector = BucketNumbersCorrector(bucket_numbers=None,
                                                          max_bucket_number=max_bucket_number)
        expected_next_number = 1

        # when
        actual_next_number = bucket_numbers_corrector.next_number(number)

        # that
        self.assertEqual(actual_next_number, expected_next_number)

    def test_next_number_not_at_counter_roll_over(self):
        # given
        max_bucket_number = 100
        number = 1
        bucket_numbers_corrector = BucketNumbersCorrector(bucket_numbers=None,
                                                          max_bucket_number=max_bucket_number)
        expected_next_number = 2

        # when
        actual_next_number = bucket_numbers_corrector.next_number(number)

        # that
        self.assertEqual(actual_next_number, expected_next_number)

    def test_previous_number_at_counter_roll_over(self):
        # given
        max_bucket_number = 100
        number = 1
        bucket_numbers_corrector = BucketNumbersCorrector(bucket_numbers=None,
                                                          max_bucket_number=max_bucket_number)
        expected_previous_number = 100

        # when
        actual_previous_number = bucket_numbers_corrector.previous_number(number)

        # that
        self.assertEqual(actual_previous_number, expected_previous_number)

    def test_previous_number_not_at_counter_roll_over(self):
        # given
        max_bucket_number = 100
        number = 2
        bucket_numbers_corrector = BucketNumbersCorrector(bucket_numbers=None,
                                                          max_bucket_number=max_bucket_number)
        expected_previous_number = 1

        # when
        actual_previous_number = bucket_numbers_corrector.previous_number(number)

        # that
        self.assertEqual(actual_previous_number, expected_previous_number)
