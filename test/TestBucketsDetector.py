import unittest
import numpy as np
import cv2

from BucketsDetector import BucketsDetector
from BucketMarker import BucketMarker
from Bucket import Bucket
from Rectangle import Rectangle
from BucketNumbersIdentifier2 import BucketNumbersIdentifier2


class TestBucketsDetector(unittest.TestCase):

    def test_template_to_detect_bucket_markers_working(self):
        # given
        bucket_marker_image = \
            cv2.imread("./images/BucketsDetector/test_template_to_detect_bucket_markers_working_input.jpg")
        buckets_detector = BucketsDetector(
                            bucket_marker_template=bucket_marker_image,
                            bucket_marker_template_original_resolution=(1920, 2560),
                            template_matching_resolution=(1920/2, 2560/2),
                            max_bucket_number=None,
                            expected_template_matching_threshold=2.3,
                            numbers_folder="./images/BucketsDetector/numbers",
                            number_matching_resolution=(50, 25))

        expected_template_to_template_matching = \
            cv2.imread("./images/BucketsDetector/test_template_to_detect_bucket_markers_working_output.png")

        # when
        actual_template_to_template_matching = buckets_detector.template_to_detect_bucket_markers

        # that
        self.assertEqual(np.array_equal(actual_template_to_template_matching,
                                        expected_template_to_template_matching),
                         True)

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

    def test_bucket_markers_on_smaller_image_working(self):
        # given
        bucket_marker_template = \
            cv2.imread("./images/BucketsDetector/"
                       "test_bucket_markers_on_smaller_image_working__bucket_marker_template.jpg")
        buckets_detector = BucketsDetector(
                            bucket_marker_template=bucket_marker_template,
                            bucket_marker_template_original_resolution=(960, 1280),
                            template_matching_resolution=(240, 320),
                            max_bucket_number=110,
                            expected_template_matching_threshold=2.3,
                            numbers_folder="./images/BucketsDetector/numbers",
                            number_matching_resolution=(50, 25))

        image = cv2.imread("./images/BucketsDetector/test_bucket_markers_on_smaller_image_working__image.jpg")

        bucket_number_identifier = BucketNumbersIdentifier2(numbers_folder="./images/BucketsDetector/numbers",
                                                            number_matching_resolution= (50, 25),
                                                            max_bucket_number=110)
        image_1 = cv2.imread("./images/BucketsDetector/test_bucket_markers_on_smaller_image_working__image_1.png")
        bounding_rectangle_1 = Rectangle(top_left_x=90, top_left_y=105, width=46, high=46)
        bucket_marker_1 = BucketMarker(image_1, bounding_rectangle_1, bucket_number_identifier)
        image_2 = cv2.imread("./images/BucketsDetector/test_bucket_markers_on_smaller_image_working__image_2.png")
        bounding_rectangle_2 = Rectangle(top_left_x=187, top_left_y=105, width=46, high=46)
        bucket_marker_2 = BucketMarker(image_2, bounding_rectangle_2, bucket_number_identifier)

        expected_bucket_markers_on_smaller_image = [bucket_marker_1, bucket_marker_2]

        # when
        actual_bucket_markers_on_smaller_image = buckets_detector.bucket_markers_on_smaller_image(image)

        # that
        self.assertEqual(np.array_equal(actual_bucket_markers_on_smaller_image,
                                        expected_bucket_markers_on_smaller_image),
                         True)

    def test_image_to_detect_bucket_markers_working(self):
        # given
        bucket_marker_template = \
            cv2.imread("./images/BucketsDetector/"
                       "test_image_to_detect_bucket_markers_working__bucket_marker_template.jpg")
        buckets_detector = BucketsDetector(
                            bucket_marker_template=bucket_marker_template,
                            bucket_marker_template_original_resolution=(960, 1280),
                            template_matching_resolution=(240, 320),
                            max_bucket_number=None,
                            expected_template_matching_threshold=2.3,
                            numbers_folder="./images/BucketsDetector/numbers",
                            number_matching_resolution=(50, 25))

        image = cv2.imread("./images/BucketsDetector/test_image_to_detect_bucket_markers_working_input.jpg")

        expected_image_to_detect_bucket_markers = \
            cv2.imread("./images/BucketsDetector/test_image_to_detect_bucket_markers_working_output.png")

        # when
        actual_image_to_detect_bucket_markers = buckets_detector.image_to_detect_bucket_markers(image)

        # that
        self.assertEqual(np.array_equal(actual_image_to_detect_bucket_markers, expected_image_to_detect_bucket_markers),
                         True)

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
        image_1 = cv2.imread("./images/BucketsDetector/test_corrected_bucket_numbers_working__image_1.png")
        bounding_rectangle_1 = Rectangle(top_left_x=90, top_left_y=105, width=46, high=46)
        bucket_marker_1 = BucketMarker(image_1, bounding_rectangle_1, bucket_number_identifier)
        image_2 = cv2.imread("./images/BucketsDetector/test_corrected_bucket_numbers_working__image_2.png")
        bounding_rectangle_2 = Rectangle(top_left_x=187, top_left_y=105, width=46, high=46)
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
        bucket_marker_template = \
            cv2.imread("./images/BucketsDetector/test_bucket_borders_working__bucket_marker_template.jpg")
        buckets_detector = BucketsDetector(
                            bucket_marker_template=bucket_marker_template,
                            bucket_marker_template_original_resolution=(960, 1280),
                            template_matching_resolution=(240, 320),
                            max_bucket_number=110,
                            expected_template_matching_threshold=2.3,
                            numbers_folder="./images/BucketsDetector/numbers",
                            number_matching_resolution=(50, 25))

        image = cv2.imread("./images/BucketsDetector/"
                           "test_bucket_borders_working__image.jpg")

        bucket_number_identifier = BucketNumbersIdentifier2(numbers_folder="./images/BucketsDetector/numbers",
                                                            number_matching_resolution= (50, 25),
                                                            max_bucket_number=110)
        image_1 = cv2.imread("./images/BucketsDetector/"
                             "test_bucket_borders_working__image_1.png")
        bounding_rectangle_1 = Rectangle(top_left_x=90, top_left_y=105, width=46, high=46)
        bucket_marker_1 = BucketMarker(image_1, bounding_rectangle_1, bucket_number_identifier)
        image_2 = cv2.imread("./images/BucketsDetector/"
                             "test_bucket_borders_working__image_2.png")
        bounding_rectangle_2 = Rectangle(top_left_x=187, top_left_y=105, width=46, high=46)
        bucket_marker_2 = BucketMarker(image_2, bounding_rectangle_2, bucket_number_identifier)
        bucket_markers = [bucket_marker_1, bucket_marker_2]

        expected_bucket_borders = [0, 452, 840, 1280]

        # when
        actual_bucket_borders = buckets_detector.bucket_borders(bucket_markers_on_smaller_image=bucket_markers,
                                                                image=image)

        # that
        self.assertEqual(actual_bucket_borders, expected_bucket_borders)

    def test_bucket_marker_bounding_rectangles_on_original_image_working(self):
        # given
        bucket_marker_template = \
            cv2.imread("./images/BucketsDetector/"
                       "test_bucket_marker_bounding_rectangles_on_original_image_working__bucket_marker_template.jpg")
        buckets_detector = BucketsDetector(
                            bucket_marker_template=bucket_marker_template,
                            bucket_marker_template_original_resolution=(960, 1280),
                            template_matching_resolution=(240, 320),
                            max_bucket_number=110,
                            expected_template_matching_threshold=2.3,
                            numbers_folder="./images/BucketsDetector/numbers",
                            number_matching_resolution=(50, 25))

        image = cv2.imread("./images/BucketsDetector/"
                           "test_bucket_marker_bounding_rectangles_on_original_image_working__image.jpg")

        bucket_number_identifier = BucketNumbersIdentifier2(numbers_folder="./images/BucketsDetector/numbers",
                                                            number_matching_resolution= (50, 25),
                                                            max_bucket_number=110)
        image_1 = cv2.imread("./images/BucketsDetector/"
                             "test_bucket_marker_bounding_rectangles_on_original_image_working__image_1.png")
        bounding_rectangle_1 = Rectangle(top_left_x=90, top_left_y=105, width=46, high=46)
        bucket_marker_1 = BucketMarker(image_1, bounding_rectangle_1, bucket_number_identifier)
        image_2 = cv2.imread("./images/BucketsDetector/"
                             "test_bucket_marker_bounding_rectangles_on_original_image_working__image_2.png")
        bounding_rectangle_2 = Rectangle(top_left_x=187, top_left_y=105, width=46, high=46)
        bucket_marker_2 = BucketMarker(image_2, bounding_rectangle_2, bucket_number_identifier)
        bucket_markers = [bucket_marker_1, bucket_marker_2]

        bounding_rectangle_1 = Rectangle(top_left_x=360, top_left_y=420, width=184, high=184)
        bounding_rectangle_2 = Rectangle(top_left_x=748, top_left_y=420, width=184, high=184)
        expected_bounding_rectangles = [bounding_rectangle_1, bounding_rectangle_2]

        # when
        actual_bounding_rectangles = buckets_detector.bucket_marker_bounding_rectangles_on_original_image(
            bucket_markers_on_smaller_image=bucket_markers,
            image=image)

        # that
        self.assertEqual(actual_bounding_rectangles, expected_bounding_rectangles)


if __name__ == '__main__':
    unittest.main()
