import unittest
import numpy as np
import cv2

from BucketsDetector import BucketsDetector
from BucketMarker import BucketMarker
from Bucket import Bucket
from Rectangle import Rectangle
from BucketNumbersIdentifier2 import BucketNumbersIdentifier2


class TestBucketsDetector(unittest.TestCase):

    def test_buckets_on_image_working(self):
        # given
        bucket_marker_template = \
            cv2.imread("./images/BucketsDetector/test_buckets_on_image__bucket_marker_template.jpg")
        buckets_detector = BucketsDetector(
                bucket_marker_template=bucket_marker_template,
                bucket_marker_template_original_resolution=(960, 1280),
                template_matching_resolution=(480, 640),
                max_bucket_number=110,
                expected_template_matching_threshold=2.3,
                numbers_folder="./images/BucketsDetector/numbers",
                number_matching_resolution=(25, 13))

        image = cv2.imread("./images/BucketsDetector/test_buckets_on_image__image.jpg")

        bucket_1 = Bucket(start=0, end=457, bucket_number="001")
        bucket_2 = Bucket(start=457, end=843, bucket_number="002")
        bucket_3 = Bucket(start=843, end=1280, bucket_number="003")
        expected_buckets_on_image = [bucket_1, bucket_2, bucket_3]

        # when
        actual_buckets_on_image = buckets_detector.buckets_on_image(image)

        # that
        self.assertEqual(actual_buckets_on_image == expected_buckets_on_image, True)

    def test_buckets_on_image__one_bucket_marker(self):
        # given
        bucket_marker_template = \
            cv2.imread("./images/BucketsDetector/test_buckets_on_image__one_bucket_marker__bucket_marker_template.jpg")
        buckets_detector = BucketsDetector(
                bucket_marker_template=bucket_marker_template,
                bucket_marker_template_original_resolution=(960, 1280),
                template_matching_resolution=(480, 640),
                max_bucket_number=110,
                expected_template_matching_threshold=2.3,
                numbers_folder="./images/BucketsDetector/numbers",
                number_matching_resolution=(25, 13))

        image = cv2.imread("./images/BucketsDetector/test_buckets_on_image__one_bucket_marker__image.jpg")

        bucket_1 = Bucket(start=0, end=843, bucket_number="002")
        bucket_2 = Bucket(start=843, end=1280, bucket_number="003")
        expected_buckets_on_image = [bucket_1, bucket_2]

        # when
        actual_buckets_on_image = buckets_detector.buckets_on_image(image)

        # that
        self.assertEqual(actual_buckets_on_image == expected_buckets_on_image, True)

    def test_buckets_on_image__no_bucket(self):
        # given
        bucket_marker_template = \
            cv2.imread("./images/BucketsDetector/test_buckets_on_image__no_bucket__bucket_marker_template.jpg")
        buckets_detector = BucketsDetector(
                bucket_marker_template=bucket_marker_template,
                bucket_marker_template_original_resolution=(960, 1280),
                template_matching_resolution=(480, 640),
                max_bucket_number=110,
                expected_template_matching_threshold=2.3,
                numbers_folder="./images/BucketsDetector/numbers",
                number_matching_resolution=(50, 25))

        black_image = np.zeros((960, 1280, 3), dtype=np.uint8)

        expected_buckets_on_image = []

        # when
        actual_buckets_on_image = buckets_detector.buckets_on_image(black_image)

        # that
        self.assertEqual(actual_buckets_on_image == expected_buckets_on_image, True)

    def test_bucket_markers_working(self):
        # given
        bucket_marker_template = \
            cv2.imread("./images/BucketsDetector/test_bucket_markers_working__bucket_marker_template.jpg")
        buckets_detector = BucketsDetector(
                            bucket_marker_template=bucket_marker_template,
                            bucket_marker_template_original_resolution=(960, 1280),
                            template_matching_resolution=(240, 320),
                            max_bucket_number=110,
                            expected_template_matching_threshold=2.3,
                            numbers_folder="./images/BucketsDetector/numbers",
                            number_matching_resolution=(50, 25))

        image = cv2.imread("./images/BucketsDetector/test_bucket_markers_working__image.jpg")

        bucket_number_identifier = BucketNumbersIdentifier2(numbers_folder="./images/BucketsDetector/numbers",
                                                            number_matching_resolution= (50, 25),
                                                            max_bucket_number=110)
        image_1 = cv2.imread("./images/BucketsDetector/test_bucket_markers_working__image.jpg")
        bounding_rectangle_1 = Rectangle(top_left_x=360, top_left_y=420, width=187, high=184)
        bucket_marker_1 = BucketMarker(image_1, bounding_rectangle_1, bucket_number_identifier)
        image_2 = cv2.imread("./images/BucketsDetector/test_bucket_markers_working__image.jpg")
        bounding_rectangle_2 = Rectangle(top_left_x=748, top_left_y=420, width=187, high=184)
        bucket_marker_2 = BucketMarker(image_2, bounding_rectangle_2, bucket_number_identifier)

        expected_bucket_markers = [bucket_marker_1, bucket_marker_2]

        # when
        actual_bucket_markers = buckets_detector.bucket_markers(image)

        # that
        self.assertEquals(actual_bucket_markers, expected_bucket_markers)

    def test_corrected_bucket_numbers_working(self):
        # given
        bucket_marker_template = \
            cv2.imread("./images/BucketsDetector/test_corrected_bucket_numbers_working__bucket_marker_template.jpg")
        buckets_detector = BucketsDetector(
                bucket_marker_template=bucket_marker_template,
                bucket_marker_template_original_resolution=(960, 1280),
                template_matching_resolution=(480, 640),
                max_bucket_number=110,
                expected_template_matching_threshold=2.3,
                numbers_folder="./images/BucketsDetector/numbers",
                number_matching_resolution=(50, 25))

        bucket_number_identifier = BucketNumbersIdentifier2(numbers_folder="./images/BucketsDetector/numbers",
                                                            number_matching_resolution=(25, 12),
                                                            max_bucket_number=110)
        image_1 = cv2.imread("./images/BucketsDetector/test_corrected_bucket_numbers_working__image.jpg")
        bounding_rectangle_1 = Rectangle(top_left_x=360, top_left_y=420, width=200, high=200)
        bucket_marker_1 = BucketMarker(image_1, bounding_rectangle_1, bucket_number_identifier)
        image_2 = cv2.imread("./images/BucketsDetector/test_corrected_bucket_numbers_working__image.jpg")
        bounding_rectangle_2 = Rectangle(top_left_x=748, top_left_y=420, width=200, high=200)
        bucket_marker_2 = BucketMarker(image_2, bounding_rectangle_2, bucket_number_identifier)

        bucket_markers = [bucket_marker_1, bucket_marker_2]

        expected_corrected_bucket_numbers = [["001", "002"], ["002", "003"]]

        # when
        actual_corrected_bucket_numbers = buckets_detector.corrected_bucket_numbers(bucket_markers)

        # that
        self.assertEqual(actual_corrected_bucket_numbers, expected_corrected_bucket_numbers)

    def test_unique_bucket_numbers_working(self):
        # given
        corrected_bucket_numbers = [["001", "002"], ["002", "003"], ["003", "004"], ["004", "005"]]

        expected_unique_bucket_numbers = ["001", "002", "003", "004", "005"]

        # when
        actual_bucket_borders = BucketsDetector.unique_bucket_numbers(corrected_bucket_numbers)

        # that
        self.assertEqual(actual_bucket_borders, expected_unique_bucket_numbers)

    def test_bucket_borders_working(self):
        # given
        bucket_number_identifier = BucketNumbersIdentifier2(numbers_folder="./images/BucketsDetector/numbers",
                                                            number_matching_resolution= (50, 25),
                                                            max_bucket_number=110)
        image_1 = cv2.imread("./images/BucketsDetector/test_bucket_borders_working__image.jpg")
        bounding_rectangle_1 = Rectangle(top_left_x=360, top_left_y=420, width=187, high=184)
        bucket_marker_1 = BucketMarker(image_1, bounding_rectangle_1, bucket_number_identifier)
        image_2 = cv2.imread("./images/BucketsDetector/test_bucket_borders_working__image.jpg")
        bounding_rectangle_2 = Rectangle(top_left_x=748, top_left_y=420, width=187, high=184)
        bucket_marker_2 = BucketMarker(image_2, bounding_rectangle_2, bucket_number_identifier)

        bucket_markers = [bucket_marker_1, bucket_marker_2]

        image = cv2.imread("./images/BucketsDetector/test_bucket_borders_working__image.jpg")

        expected_bucket_borders = [0, 453, 841, 1280]

        # when
        actual_bucket_borders = BucketsDetector.bucket_borders(bucket_markers, image)

        # that
        self.assertEqual(actual_bucket_borders, expected_bucket_borders)

if __name__ == '__main__':
    unittest.main()
