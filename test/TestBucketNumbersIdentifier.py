import unittest
import numpy as np
import cv2

from BucketNumbersIdentifier import BucketNumbersIdentifier


class TestBucketNumbersIdentifier(unittest.TestCase):
    def test_do_number_recognition_working(self):
        # given
        image = cv2.imread("./images/BucketNumbersIdentifier/test_do_number_recognition_working.png")

        expected_recognized_numbers = "100"

        # when
        actual_recognized_numbers = BucketNumbersIdentifier.do_number_recognition(image=image)

        # that
        self.assertEqual(actual_recognized_numbers, expected_recognized_numbers)

    def test_do_number_recognition_real_sample(self):
        # given
        image = cv2.imread("./images/BucketNumbersIdentifier/test_do_number_recognition_real_sample.jpg")

        expected_recognized_numbers = "001"

        # when
        actual_recognized_numbers = BucketNumbersIdentifier.do_number_recognition(image=image)

        # that
        self.assertEqual(actual_recognized_numbers, expected_recognized_numbers)


if __name__ == '__main__':
    unittest.main()