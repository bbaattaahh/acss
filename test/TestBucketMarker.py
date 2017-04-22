import unittest
import cv2
import numpy as np


from BucketMarker import BucketMarker
from Rectangle import Rectangle
from BucketNumbersIdentifier2 import BucketNumbersIdentifier2


class TestBucketMarker(unittest.TestCase):

    def test_bucket_marker_image_working(self):
        # given
        image = cv2.imread("./images/BucketMarker/test_bucket_marker_image_working__image.jpg")
        bounding_rectangle = Rectangle(top_left_x=727, top_left_y=843, width=374, high=368)
        bucket_number_identifier = BucketNumbersIdentifier2(numbers_folder="./images/BucketMarker/numbers",
                                                            number_matching_resolution=(50, 25),
                                                            max_bucket_number=110)
        bucket_marker = BucketMarker(image,
                                     bounding_rectangle,
                                     bucket_number_identifier)

        expected_bucket_marker_image = \
            cv2.imread("./images/BucketMarker/test_bucket_marker_image_working__bucket_marker_image.png")

        # when
        actual_bucket_marker_image = bucket_marker.bucket_marker_image

        # that
        self.assertEqual(np.array_equal(actual_bucket_marker_image, expected_bucket_marker_image), True)

    def test_left_bucket_number_working(self):
        # given
        image = cv2.imread("./images/BucketMarker/test_left_bucket_number_working__image.jpg")
        bounding_rectangle = Rectangle(top_left_x=727, top_left_y=843, width=374, high=368)
        bucket_number_identifier = BucketNumbersIdentifier2(numbers_folder="./images/BucketMarker/numbers",
                                                            number_matching_resolution=(25, 13),
                                                            max_bucket_number=110)
        bucket_marker = BucketMarker(image,
                                     bounding_rectangle,
                                     bucket_number_identifier)

        expected_left_bucket_number = "001"

        # when
        actual_left_bucket_number = bucket_marker.left_bucket_number

        # that
        self.assertEqual(actual_left_bucket_number, expected_left_bucket_number)

    def test_right_bucket_number_working__not_found(self):
        # given
        image = cv2.imread("./images/BucketMarker/test_right_bucket_number_working__image.jpg")
        bounding_rectangle = Rectangle(top_left_x=727, top_left_y=843, width=374, high=368)
        bucket_number_identifier = BucketNumbersIdentifier2(numbers_folder="./images/BucketMarker/numbers",
                                                            number_matching_resolution=(50, 25),
                                                            max_bucket_number=110)
        bucket_marker = BucketMarker(image,
                                     bounding_rectangle,
                                     bucket_number_identifier)

        expected_right_bucket_number = ""

        # when
        actual_right_bucket_number = bucket_marker.right_bucket_number

        # that
        self.assertEqual(actual_right_bucket_number, expected_right_bucket_number)

    def test_middle_x_working(self):
        # given
        any_image = np.zeros((600, 800, 3), dtype=np.uint8)
        bounding_rectangle = Rectangle(top_left_x=10, top_left_y=10, width=30, high=300)
        bucket_number_identifier = BucketNumbersIdentifier2(numbers_folder="./images/BucketMarker/numbers",
                                                            number_matching_resolution=(50, 25),
                                                            max_bucket_number=110)
        bucket_marker = BucketMarker(any_image,
                                     bounding_rectangle,
                                     bucket_number_identifier)

        expected_middle_x = 25

        # when
        actual_middle_x = bucket_marker.middle_x

        # that
        self.assertEqual(actual_middle_x == expected_middle_x, True)


if __name__ == '__main__':
    unittest.main()
