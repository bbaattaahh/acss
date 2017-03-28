import unittest
import numpy as np
import cv2

from BucketMarkersDetector import BucketMarkersDetector


class TestDetectBucketMarkers(unittest.TestCase):

    def test_bucket_numbers_working(self):
        # given
        image = \
            cv2.imread("./images/BucketMarkersDetector/test_bucket_numbers_working__image.jpg")

        bucket_marker_template = \
            cv2.imread("./images/BucketMarkersDetector/test_bucket_numbers_working__bucket_marker_template.png")
        max_bucket_number = 100
        bucket_markers_detector = BucketMarkersDetector(bucket_marker_template=bucket_marker_template,
                                                        max_bucket_number=max_bucket_number)

        expected_numbers = [['001', '002'], ['002', '003']]

        # when
        actual_numbers = bucket_markers_detector.bucket_numbers(image)

        # that
        self.assertEqual(actual_numbers, expected_numbers)

    def test_bucket_numbers_some_deleted_number_from_image(self):
        # given
        bucket_marker_template = \
            cv2.imread("./images/BucketMarkersDetector/"
                       "test_bucket_numbers_some_deleted_number_from_image__bucket_marker_template.png")
        max_bucket_number = 100
        bucket_markers_detector = BucketMarkersDetector(bucket_marker_template=bucket_marker_template,
                                                        max_bucket_number=max_bucket_number)

        image = \
            cv2.imread("./images/BucketMarkersDetector/test_bucket_numbers_some_deleted_number_from_image__image.jpg")

        expected_numbers = [['001', '002'], ['002', '003']]

        # when
        actual_numbers = bucket_markers_detector.bucket_numbers(image)

        # that
        self.assertEqual(actual_numbers, expected_numbers)

    def test_bucket_markers_working(self):
        # given
        image = \
            cv2.imread("./images/BucketMarkersDetector/test_bucket_markers_working__image.jpg")

        bucket_marker_template = \
            cv2.imread("./images/BucketMarkersDetector/test_bucket_markers_working__bucket_marker_template.png")
        bucket_markers_detector = BucketMarkersDetector(bucket_marker_template=bucket_marker_template,
                                                        max_bucket_number=None)

        expected_bucket_marker_1 = \
            cv2.imread("./images/BucketMarkersDetector/test_bucket_markers_working__bucket_marker_1_output.png")
        expected_bucket_marker_2 = \
            cv2.imread("./images/BucketMarkersDetector/test_bucket_markers_working__bucket_marker_2_output.png")

        # when
        actual_bucket_markers = bucket_markers_detector.bucket_markers(image)

        # that
        self.assertEqual(np.array_equal(actual_bucket_markers[0], expected_bucket_marker_1), True)
        self.assertEqual(np.array_equal(actual_bucket_markers[1], expected_bucket_marker_2), True)

    def test_bucket_marker_top_left_corners_working(self):
        # given
        bucket_marker_template = cv2.imread(
            "./images/BucketMarkersDetector/test_bucket_marker_top_left_corners_working__bucket_marker_template.jpg")

        bucket_markers_detector = BucketMarkersDetector(bucket_marker_template=bucket_marker_template,
                                                        max_bucket_number=None)

        image = cv2.imread("./images/BucketMarkersDetector/test_bucket_marker_top_left_corners_working__image.jpg")

        expected_bucket_marker_top_left_corners = [[727, 843],
                                                   [1500, 843]]

        # when
        actual_bucket_marker_top_left_corners = bucket_markers_detector.bucket_marker_top_left_corners(image)

        # that
        self.assertEqual(actual_bucket_marker_top_left_corners, expected_bucket_marker_top_left_corners)

    def test_bucket_marker_middle_x_positions_working(self):
        # given
        bucket_marker_template = cv2.imread(
            "./images/BucketMarkersDetector/test_bucket_marker_middle_x_positions_working__bucket_marker_template.jpg")

        bucket_markers_detector = BucketMarkersDetector(bucket_marker_template=bucket_marker_template,
                                                        max_bucket_number=None)

        image = cv2.imread("./images/BucketMarkersDetector/test_bucket_marker_middle_x_positions_working__image.jpg")

        expected_bucket_marker_middle_x_positions = [840, 1613]

        # when
        actual_bucket_marker_middle_x_positions = bucket_markers_detector.bucket_marker_middle_x_positions(image)

        # that
        self.assertEqual(actual_bucket_marker_middle_x_positions, expected_bucket_marker_middle_x_positions)

    def test_matching_middle_templates_position_working(self):
        # given
        bucket_marker_template = cv2.imread(
            "./images/BucketMarkersDetector/test_matching_middle_templates_positions_working__bucket_marker_template.jpg")
        bucket_markers_detector = BucketMarkersDetector(bucket_marker_template=bucket_marker_template,
                                                        max_bucket_number=None)

        image = cv2.imread("./images/BucketMarkersDetector/test_matching_middle_templates_positions_working__image.jpg")

        expected_matching_middle_templates_positions = [[877, 843],
                                                        [1650, 843]]

        # when
        actual_matching_middle_templates_positions = bucket_markers_detector.matching_middle_templates_positions(image)

        # that
        self.assertEqual(actual_matching_middle_templates_positions, expected_matching_middle_templates_positions)

    def test_always_seen_middle_template_working(self):
        # given
        bucket_marker_template = \
            cv2.imread("./images/BucketMarkersDetector/test_always_seen_middle_template_working_input.jpg")
        bucket_markers_detector = BucketMarkersDetector(bucket_marker_template=bucket_marker_template,
                                                        max_bucket_number=None)

        expected_always_seen_middle_template = \
            cv2.imread("./images/BucketMarkersDetector/test_always_seen_middle_template_working_output.png")

        # when
        actual_always_seen_middle_template = bucket_markers_detector.always_seen_middle_template

        # that
        self.assertEqual(np.array_equal(actual_always_seen_middle_template, expected_always_seen_middle_template),
                         True)
