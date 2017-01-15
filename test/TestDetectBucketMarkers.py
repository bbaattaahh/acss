import unittest
import numpy as np
import cv2

from DetectBucketMarkers import DetectBucketMarkers


class TestDetectBucketMarkers(unittest.TestCase):

    def test_bucket_numbers_working(self):
        # given
        image = \
            cv2.imread("./images/DetectBucketMarkers/test_bucket_numbers_working__image.jpg")

        bucket_marker_template = \
            cv2.imread("./images/DetectBucketMarkers/test_bucket_numbers_working__bucket_marker_template.png")
        detect_bucket_markers = DetectBucketMarkers(image=image,
                                                    bucket_marker_template=bucket_marker_template)

        expected_numbers = [['001', '002'], ['002', '003']]

        # when
        actual_numbers = detect_bucket_markers.bucket_numbers

        # that
        self.assertEqual(actual_numbers, expected_numbers)

    def test_bucket_markers_working(self):
        # given
        image = \
            cv2.imread("./images/DetectBucketMarkers/test_bucket_markers_working__image.jpg")

        bucket_marker_template = \
            cv2.imread("./images/DetectBucketMarkers/test_bucket_markers_working__bucket_marker_template.png")
        detect_bucket_markers = DetectBucketMarkers(image=image,
                                                    bucket_marker_template=bucket_marker_template)

        expected_bucket_marker_1 = \
            cv2.imread("./images/DetectBucketMarkers/test_bucket_markers_working__bucket_marker_1_output.png")
        expected_bucket_marker_2 = \
            cv2.imread("./images/DetectBucketMarkers/test_bucket_markers_working__bucket_marker_2_output.png")

        # when
        actual_bucket_markers = detect_bucket_markers.bucket_markers

        # that
        self.assertEqual(np.array_equal(actual_bucket_markers[0], expected_bucket_marker_1), True)
        self.assertEqual(np.array_equal(actual_bucket_markers[1], expected_bucket_marker_2), True)

    def test_bucket_marker_top_left_corners_working(self):
        # given
        image = cv2.imread("./images/DetectBucketMarkers/test_bucket_marker_top_left_corners_working__image.jpg")
        bucket_marker_template = cv2.imread(
            "./images/DetectBucketMarkers/test_bucket_marker_top_left_corners_working__bucket_marker_template.jpg")

        detect_bucket_markers = DetectBucketMarkers(image=image,
                                                    bucket_marker_template=bucket_marker_template)

        expected_bucket_marker_top_left_corners = [[727, 843],
                                                   [1500, 843]]

        # when
        actual_bucket_marker_top_left_corners = detect_bucket_markers.bucket_marker_top_left_corners

        # that
        self.assertEqual(actual_bucket_marker_top_left_corners, expected_bucket_marker_top_left_corners)

    def test_bucket_marker_middle_x_positions_working(self):
        # given
        image = cv2.imread("./images/DetectBucketMarkers/test_bucket_marker_middle_x_positions_working__image.jpg")
        bucket_marker_template = cv2.imread(
            "./images/DetectBucketMarkers/test_bucket_marker_middle_x_positions_working__bucket_marker_template.jpg")

        detect_bucket_markers = DetectBucketMarkers(image=image,
                                                    bucket_marker_template=bucket_marker_template)

        expected_bucket_marker_middle_x_positions = [840, 1613]

        # when
        actual_bucket_marker_middle_x_positions = detect_bucket_markers.bucket_marker_middle_x_positions

        # that
        self.assertEqual(actual_bucket_marker_middle_x_positions, expected_bucket_marker_middle_x_positions)

    def test_matching_middle_templates_position_working(self):
        # given
        image = cv2.imread("./images/DetectBucketMarkers/test_matching_middle_templates_positions_working__image.jpg")
        bucket_marker_template = cv2.imread(
            "./images/DetectBucketMarkers/test_matching_middle_templates_positions_working__bucket_marker_template.jpg")

        detect_bucket_markers = DetectBucketMarkers(image=image,
                                                    bucket_marker_template=bucket_marker_template)

        expected_matching_middle_templates_positions = [[877, 843],
                                                        [1650, 843]]

        # when
        actual_matching_middle_templates_positions = detect_bucket_markers.matching_middle_templates_positions

        # that
        self.assertEqual(actual_matching_middle_templates_positions, expected_matching_middle_templates_positions)

    def test_always_seen_middle_template_working(self):
        # given
        bucket_marker_template = \
            cv2.imread("./images/DetectBucketMarkers/test_always_seen_middle_template_working_input.jpg")
        detect_bucket_markers = DetectBucketMarkers(image=None,
                                                    bucket_marker_template=bucket_marker_template)

        expected_always_seen_middle_template = \
            cv2.imread("./images/DetectBucketMarkers/test_always_seen_middle_template_working_output.png")

        # when
        actual_always_seen_middle_template = detect_bucket_markers.always_seen_middle_template

        # that
        self.assertEqual(np.array_equal(actual_always_seen_middle_template, expected_always_seen_middle_template),
                         True)
