import unittest

from BucketNumbersCorrector import BucketNumbersCorrector


class TestBucketNumbersCorrector(unittest.TestCase):

    def test_corrected_bucket_numbers_004_is_badly_detected(self):
        # given
        bucket_numbers = [["001", ""], ["002", ""], ["004", ""], ["", "005"]]
        max_bucket_number = 100
        bucket_numbers_corrector = BucketNumbersCorrector(bucket_numbers=bucket_numbers,
                                                          max_bucket_number=max_bucket_number)
        expected_corrected_bucket_numbers = [["001", "002"], ["002", "003"], ["003", "004"], ["004", "005"]]

        # when
        actual_corrected_bucket_numbers = bucket_numbers_corrector.corrected_bucket_numbers

        # that
        self.assertEqual(actual_corrected_bucket_numbers, expected_corrected_bucket_numbers)

    def test_corrected_bucket_numbers_123_is_badly_detected_and_at_roll_over_and_some_missing(self):
        # given
        bucket_numbers = [["098", ""], ["", ""], ["123", ""], ["", "002"]]
        max_bucket_number = 100
        bucket_numbers_corrector = BucketNumbersCorrector(bucket_numbers=bucket_numbers,
                                                          max_bucket_number=max_bucket_number)
        expected_corrected_bucket_numbers = [["098", "099"], ["099", "100"], ["100", "001"], ["001", "002"]]

        # when
        actual_corrected_bucket_numbers = bucket_numbers_corrector.corrected_bucket_numbers

        # that
        self.assertEqual(actual_corrected_bucket_numbers, expected_corrected_bucket_numbers)

    def test_best_matching_bucket_numbers_004_is_badly_detected_at_roll_over(self):
        # given
        bucket_numbers = [["99", "100"], ["100", "001"], ["004", ""], ["", "003"]]
        max_bucket_number = 100
        bucket_numbers_corrector = BucketNumbersCorrector(bucket_numbers=bucket_numbers,
                                                          max_bucket_number=max_bucket_number)
        expected_best_matching_bucket_numbers = [99, 100, 100, 1, 1, 2, 2, 3]

        # when
        actual_best_matching_bucket_numbers = \
            bucket_numbers_corrector.best_matching_bucket_numbers

        # that
        self.assertEqual(actual_best_matching_bucket_numbers, expected_best_matching_bucket_numbers)

    def test_best_matching_bucket_numbers_004_is_badly_detected(self):
        # given
        bucket_numbers = [["001", ""], ["002", ""], ["004", ""], ["", "005"]]
        max_bucket_number = 100
        bucket_numbers_corrector = BucketNumbersCorrector(bucket_numbers=bucket_numbers,
                                                          max_bucket_number=max_bucket_number)
        expected_best_matching_bucket_numbers = [1, 2, 2, 3, 3, 4, 4, 5]

        # when
        actual_best_matching_bucket_numbers = \
            bucket_numbers_corrector.best_matching_bucket_numbers

        # that
        self.assertEqual(actual_best_matching_bucket_numbers, expected_best_matching_bucket_numbers)

    def test_int_flatten_bucket_numbers_working(self):
        # given
        bucket_numbers = [["001", ""], ["", "003"], ["003", "004"], ["004", "005"]]
        bucket_numbers_corrector = BucketNumbersCorrector(bucket_numbers,
                                                          max_bucket_number=None)
        expected_int_flatten_bucket_numbers = [1, None, None, 3, 3, 4, 4, 5]

        # when
        actual_int_flatten_bucket_numbers = bucket_numbers_corrector.int_flatten_bucket_numbers

        # that
        self.assertEqual(actual_int_flatten_bucket_numbers, expected_int_flatten_bucket_numbers)

    def test_one_item_bucket_numbers_working(self):
        # given
        bucket_numbers = [["001", ""], ["002", ""], ["003", "004"], ["", "005"]]
        max_bucket_number = 100
        index_to_keep = 2
        bucket_numbers_corrector = BucketNumbersCorrector(bucket_numbers=bucket_numbers,
                                                          max_bucket_number=max_bucket_number)
        expected_one_item_bucket_numbers = [None, None, 2, None, None, None, None, None]

        # when
        actual_one_item_bucket_numbers = \
            bucket_numbers_corrector.one_item_bucket_numbers(index_to_keep)

        # that
        self.assertEqual(actual_one_item_bucket_numbers, expected_one_item_bucket_numbers)

    def test_fulfill_bucket_numbers_which_has_one_item_at_counting_roll_over(self):
        # given
        bucket_numbers_which_has_one_item = [None, None, None, 1, None, None]
        max_bucket_number = 100
        bucket_numbers_corrector = BucketNumbersCorrector(bucket_numbers=None,
                                                          max_bucket_number=max_bucket_number)
        expected_fulfilled_bucket_numbers = [99, 100, 100, 1, 1, 2]

        # when
        actual_fulfilled_bucket_numbers = \
            bucket_numbers_corrector.fulfill_bucket_numbers_which_has_one_item(bucket_numbers_which_has_one_item)

        # that
        self.assertEqual(actual_fulfilled_bucket_numbers, expected_fulfilled_bucket_numbers)

    def test_fulfill_bucket_numbers_which_has_one_item_not_at_counting_roll_over(self):
        # given
        bucket_numbers_which_has_one_item = [None, None, None, 10, None, None]
        max_bucket_number = 100
        bucket_numbers_corrector = BucketNumbersCorrector(bucket_numbers=None,
                                                          max_bucket_number=max_bucket_number)
        expected_fulfilled_bucket_numbers = [8, 9, 9, 10, 10, 11]

        # when
        actual_fulfilled_bucket_numbers = \
            bucket_numbers_corrector.fulfill_bucket_numbers_which_has_one_item(bucket_numbers_which_has_one_item)

        # that
        self.assertEqual(actual_fulfilled_bucket_numbers, expected_fulfilled_bucket_numbers)

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

    def test_bucket_numbers_distance_none_doesnt_matter(self):
        # given
        bucket_numbers_1 = [1, 2, 2, 3, 3, 4, 4, 5]
        bucket_numbers_2 = [1, None, None, 3, 3, 4, 4, 5]

        expected_distance = 0

        # when
        actual_distance = BucketNumbersCorrector.bucket_numbers_distance(bucket_numbers_1, bucket_numbers_2)

        # that
        self.assertEqual(actual_distance, expected_distance)

    def test_bucket_numbers_distance_one_mismatch(self):
        # given
        bucket_numbers_1 = [1, 2, 2, 3, 3, 4, 4, 5]
        bucket_numbers_2 = [1, 2, 8, 3, 3, 4, 4, 5]

        expected_distance = 1

        # when
        actual_distance = BucketNumbersCorrector.bucket_numbers_distance(bucket_numbers_1, bucket_numbers_2)

        # that
        self.assertEqual(actual_distance, expected_distance)

    def test_convert_int_bucket_numbers_to_original_format_working(self):
        # given
        int_bucket_numbers = [1, 2, 2, 3, 3, 4, 4, 5]

        expected_original_format = [["001", "002"], ["002", "003"], ["003", "004"], ["004", "005"]]

        # when
        actual_original_format = \
            BucketNumbersCorrector.convert_int_bucket_numbers_to_original_format(int_bucket_numbers)

        # that
        self.assertEqual(actual_original_format, expected_original_format)

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
