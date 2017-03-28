import unittest
import numpy as np
import cv2

from BucketsDetector import BucketsDetector
from Bucket import Bucket


class TestBucketsDetector(unittest.TestCase):

    def test_buckets_on_image_working(self):
        # given
        bucket_marker_template = \
            cv2.imread("./images/BucketsDetector/test_buckets_on_image__bucket_marker_template.jpg")
        bucket_marker_template_original_resolution = 960, 1280
        template_matching_resolution = 480, 640
        max_bucket_number = 100
        buckets_detector = BucketsDetector(
                bucket_marker_template=bucket_marker_template,
                bucket_marker_template_original_resolution=bucket_marker_template_original_resolution,
                template_matching_resolution=template_matching_resolution,
                max_bucket_number=max_bucket_number)

        image = cv2.imread("./images/BucketsDetector/test_buckets_on_image__image.jpg")

        bucket_1 = Bucket(start=0, end=420, bucket_number="001")
        bucket_2 = Bucket(start=420, end=806, bucket_number="002")
        bucket_3 = Bucket(start=806, end=1280, bucket_number="003")
        expected_buckets_on_image = [bucket_1, bucket_2, bucket_3]

        # when
        actual_buckets_on_image = buckets_detector.buckets_on_image(image)

        # that
        self.assertEqual(actual_buckets_on_image == expected_buckets_on_image, True)

    def test_buckets_on_image__one_bucket_marker(self):
        # given
        bucket_marker_template = \
            cv2.imread("./images/BucketsDetector/test_buckets_on_image__one_bucket_marker__bucket_marker_template.jpg")
        bucket_marker_template_original_resolution = 960, 1280
        template_matching_resolution = 480, 640
        max_bucket_number = 110
        buckets_detector = BucketsDetector(
                bucket_marker_template=bucket_marker_template,
                bucket_marker_template_original_resolution=bucket_marker_template_original_resolution,
                template_matching_resolution=template_matching_resolution,
                max_bucket_number=max_bucket_number)

        image = cv2.imread("./images/BucketsDetector/test_buckets_on_image__one_bucket_marker__image.jpg")

        bucket_1 = Bucket(start=0, end=806, bucket_number="002")
        bucket_2 = Bucket(start=806, end=1280, bucket_number="003")
        expected_buckets_on_image = [bucket_1, bucket_2]

        # when
        actual_buckets_on_image = buckets_detector.buckets_on_image(image)

        # that
        self.assertEqual(actual_buckets_on_image == expected_buckets_on_image, True)

    def test_buckets_on_image__no_bucket(self):
        # given
        bucket_marker_template = \
            cv2.imread("./images/BucketsDetector/test_buckets_on_image__no_bucket__bucket_marker_template.jpg")
        bucket_marker_template_original_resolution = 960, 1280
        template_matching_resolution = 480, 640
        max_bucket_number = 100
        buckets_detector = BucketsDetector(
                bucket_marker_template=bucket_marker_template,
                bucket_marker_template_original_resolution=bucket_marker_template_original_resolution,
                template_matching_resolution=template_matching_resolution,
                max_bucket_number=max_bucket_number)

        black_image = np.zeros((960, 1280, 3), dtype=np.uint8)

        expected_buckets_on_image = []

        # when
        actual_buckets_on_image = buckets_detector.buckets_on_image(black_image)

        # that
        self.assertEqual(actual_buckets_on_image == expected_buckets_on_image, True)

    def test_buckets_on_smaller_image_working(self):
        # given
        bucket_marker_template = \
            cv2.imread("./images/BucketsDetector/test_buckets_on_smaller_image__bucket_marker_template.jpg")
        bucket_marker_template_original_resolution = 960, 1280
        template_matching_resolution = 480, 640
        max_bucket_number = 100
        buckets_detector = BucketsDetector(
                bucket_marker_template=bucket_marker_template,
                bucket_marker_template_original_resolution=bucket_marker_template_original_resolution,
                template_matching_resolution=template_matching_resolution,
                max_bucket_number=max_bucket_number)

        image = cv2.imread("./images/BucketsDetector/test_buckets_on_smaller_image__image.jpg")

        bucket_1 = Bucket(start=0, end=210, bucket_number="001")
        bucket_2 = Bucket(start=210, end=403, bucket_number="002")
        bucket_3 = Bucket(start=403, end=640, bucket_number="003")
        expected_buckets_on_smaller_image = [bucket_1, bucket_2, bucket_3]

        # when
        actual_buckets_on_smaller_image = buckets_detector.buckets_on_smaller_image(image)

        # that
        self.assertEqual(actual_buckets_on_smaller_image == expected_buckets_on_smaller_image, True)

    def test_image_to_detect_bucket_markers_working(self):
        # given
        bucket_marker_template = \
            cv2.imread("./images/BucketsDetector/"
                       "test_image_to_detect_bucket_markers_working__bucket_marker_template.jpg")
        bucket_marker_template_original_resolution = 960, 1280

        template_matching_resolution = (240, 320)
        buckets_detector = BucketsDetector(
                            bucket_marker_template=bucket_marker_template,
                            bucket_marker_template_original_resolution=bucket_marker_template_original_resolution,
                            template_matching_resolution=template_matching_resolution,
                            max_bucket_number=None)

        image = cv2.imread("./images/BucketsDetector/test_image_to_detect_bucket_markers_working_input.jpg")

        expected_image_to_detect_bucket_markers = \
            cv2.imread("./images/BucketsDetector/test_image_to_detect_bucket_markers_working_output.png")

        # when
        actual_image_to_detect_bucket_markers = buckets_detector.image_to_detect_bucket_markers(image)

        # that
        self.assertEqual(np.array_equal(actual_image_to_detect_bucket_markers, expected_image_to_detect_bucket_markers),
                         True)

    def test_template_to_detect_bucket_markers_working(self):
        # given
        bucket_marker_image = \
            cv2.imread("./images/BucketsDetector/test_template_to_detect_bucket_markers_working_input.jpg")
        template_matching_resolution = (1920/2, 2560/2)
        bucket_marker_template_original_resolution = (1920, 2560)
        buckets_detector = BucketsDetector(
                            bucket_marker_template=bucket_marker_image,
                            bucket_marker_template_original_resolution=bucket_marker_template_original_resolution,
                            template_matching_resolution=template_matching_resolution,
                            max_bucket_number=None)

        expected_template_to_template_matching = cv2.imread(
                                    "./images/BucketsDetector/test_template_to_detect_bucket_markers_working_output.png")

        # when
        actual_template_to_template_matching = buckets_detector.template_to_detect_bucket_markers

        # that
        self.assertEqual(np.array_equal(actual_template_to_template_matching,
                                        expected_template_to_template_matching),
                         True)

if __name__ == '__main__':
    unittest.main()
