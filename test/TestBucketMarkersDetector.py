import unittest
import numpy as np
import cv2

from BucketMarkersDetector import BucketMarkersDetector
from Rectangle import Rectangle
from BucketMarker import BucketMarker
from BucketNumbersIdentifier2 import BucketNumbersIdentifier2


class TestBucketMarkersDetector(unittest.TestCase):
    def test_always_seen_middle_template_working(self):
        # given
        bucket_marker_template = \
            cv2.imread("./images/BucketMarkersDetector/test_always_seen_middle_template_working_input.jpg")
        bucket_markers_detector = BucketMarkersDetector(bucket_marker_template=bucket_marker_template,
                                                        bucket_marker_template_original_resolution=(2560, 1920),
                                                        template_matching_resolution=(2560, 1920),
                                                        expected_template_matching_threshold=2.3,
                                                        bucket_number_identifier=None)

        expected_always_seen_middle_template = \
            cv2.imread("./images/BucketMarkersDetector/test_always_seen_middle_template_working_output.png")

        # when
        actual_always_seen_middle_template = bucket_markers_detector.always_seen_middle_template

        # that
        self.assertEqual(np.array_equal(actual_always_seen_middle_template, expected_always_seen_middle_template),
                         True)

    def test_get_bucket_markers_working(self):
        # given
        bucket_marker_template = \
            cv2.imread("./images/BucketMarkersDetector/test_get_bucket_markers_working__bucket_marker_template.jpg")
        bucket_number_identifier = BucketNumbersIdentifier2(numbers_folder="./images/BucketMarkersDetector/numbers",
                                                            number_matching_resolution=(50, 25),
                                                            max_bucket_number=110)

        bucket_markers_detector = BucketMarkersDetector(bucket_marker_template,
                                                        bucket_marker_template_original_resolution=(1920, 2560),
                                                        template_matching_resolution=(1920, 2560),
                                                        expected_template_matching_threshold=2.3,
                                                        bucket_number_identifier=bucket_number_identifier)

        image = \
            cv2.imread("./images/BucketMarkersDetector/test_get_bucket_markers_working__image.jpg")

        bounding_rectangle_1 = Rectangle(top_left_x=727, top_left_y=843, width=374, high=368)
        bounding_rectangle_2 = Rectangle(top_left_x=1500, top_left_y=843, width=374, high=368)
        bucket_marker_1 = BucketMarker(image, bounding_rectangle_1, bucket_number_identifier)
        bucket_marker_2 = BucketMarker(image, bounding_rectangle_2, bucket_number_identifier)
        expected_bucket_markers = [bucket_marker_1, bucket_marker_2]

        # when
        actual_bucket_markers = bucket_markers_detector.get_bucket_markers(image)

        # that
        self.assertEqual(actual_bucket_markers, expected_bucket_markers)

    def test_get_bucket_markers_matching_on_different_resolution(self):
        # given
        bucket_marker_template = \
            cv2.imread("./images/BucketMarkersDetector/"
                       "test_get_bucket_markers_matching_on_different_resolution__bucket_marker_template.jpg")
        bucket_number_identifier = BucketNumbersIdentifier2(numbers_folder="./images/BucketMarkersDetector/numbers",
                                                            number_matching_resolution=(50, 25),
                                                            max_bucket_number=110)

        bucket_markers_detector = BucketMarkersDetector(bucket_marker_template,
                                                        bucket_marker_template_original_resolution=(1920, 2560),
                                                        template_matching_resolution=(480, 640),
                                                        expected_template_matching_threshold=2.3,
                                                        bucket_number_identifier=bucket_number_identifier)

        image = cv2.imread("./images/BucketMarkersDetector/"
                           "test_get_bucket_markers_matching_on_different_resolution__image.jpg")

        bounding_rectangle_1 = Rectangle(top_left_x=728, top_left_y=840, width=374, high=368)
        bounding_rectangle_2 = Rectangle(top_left_x=1500, top_left_y=840, width=374, high=368)
        bucket_marker_1 = BucketMarker(image, bounding_rectangle_1, bucket_number_identifier)
        bucket_marker_2 = BucketMarker(image, bounding_rectangle_2, bucket_number_identifier)
        expected_bucket_markers = [bucket_marker_1, bucket_marker_2]

        # when
        actual_bucket_markers = bucket_markers_detector.get_bucket_markers(image)

        # that
        self.assertEqual(actual_bucket_markers, expected_bucket_markers)


    def test_image_to_detect_bucket_markers_working(self):
        # given
        bucket_marker_template = \
            cv2.imread("./images/BucketMarkersDetector/"
                       "test_image_to_detect_bucket_markers_working__bucket_marker_template.jpg")
        bucket_markers_detector = BucketMarkersDetector(
                            bucket_marker_template=bucket_marker_template,
                            bucket_marker_template_original_resolution=(960, 1280),
                            template_matching_resolution=(240, 320),
                            expected_template_matching_threshold=2.3,
                            bucket_number_identifier=None)

        image = cv2.imread("./images/BucketMarkersDetector/test_image_to_detect_bucket_markers_working_input.jpg")

        expected_image_to_detect_bucket_markers = \
            cv2.imread("./images/BucketMarkersDetector/test_image_to_detect_bucket_markers_working_output.png")

        # when
        actual_image_to_detect_bucket_markers = bucket_markers_detector.image_to_detect_bucket_markers(image)

        # that
        self.assertEqual(np.array_equal(actual_image_to_detect_bucket_markers, expected_image_to_detect_bucket_markers),
                         True)

    def test_matching_middle_templates_position_working(self):
        # given
        bucket_marker_template = cv2.imread(
            "./images/BucketMarkersDetector/"
            "test_matching_middle_templates_positions_working__bucket_marker_template.jpg")
        bucket_markers_detector = BucketMarkersDetector(bucket_marker_template=bucket_marker_template,
                                                        bucket_marker_template_original_resolution=(2560, 1920),
                                                        template_matching_resolution=(2560, 1920),
                                                        expected_template_matching_threshold=2.3,
                                                        bucket_number_identifier=None)

        image = cv2.imread("./images/BucketMarkersDetector/test_matching_middle_templates_positions_working__image.jpg")

        expected_matching_middle_templates_positions = [[877, 843],
                                                        [1650, 843]]

        # when
        actual_matching_middle_templates_positions = bucket_markers_detector.matching_middle_templates_positions(image)

        # that
        self.assertEqual(actual_matching_middle_templates_positions, expected_matching_middle_templates_positions)

    def test_bucket_marker_top_left_corners_working(self):
        # given
        bucket_marker_template = cv2.imread(
            "./images/BucketMarkersDetector/test_bucket_marker_top_left_corners_working__bucket_marker_template.jpg")
        bucket_markers_detector = BucketMarkersDetector(bucket_marker_template,
                                                        bucket_marker_template_original_resolution=(2560, 1920),
                                                        template_matching_resolution=(2560, 1920),
                                                        expected_template_matching_threshold=2.3,
                                                        bucket_number_identifier=None)

        matching_middle_templates_positions = [[877, 843], [1650, 843]]

        expected_bucket_marker_top_left_corners = [[727, 843], [1500, 843]]

        # when
        actual_bucket_marker_top_left_corners = \
            bucket_markers_detector.bucket_marker_top_left_corners(matching_middle_templates_positions)

        # that
        self.assertEqual(actual_bucket_marker_top_left_corners, expected_bucket_marker_top_left_corners)

    def test_convert_bucket_marker_top_left_corners_to_original_image_working(self):
        # given
        bucket_marker_template = cv2.imread(
            "./images/BucketMarkersDetector/"
            "test_convert_bucket_marker_top_left_corners_to_original_image_working__bucket_marker_template.jpg")
        bucket_markers_detector = BucketMarkersDetector(bucket_marker_template=bucket_marker_template,
                                                        bucket_marker_template_original_resolution=(2560, 1920),
                                                        template_matching_resolution=(2560, 1920),
                                                        expected_template_matching_threshold=2.3,
                                                        bucket_number_identifier=None)

        bucket_marker_top_left_corners_on_smaller_image = [[727, 843], [1500, 843]]
        image_shape = (2560, 1920)

        expected_convert_bucket_marker_top_left_corners = [[727, 843], [1500, 843]]

        # when
        actual_convert_bucket_marker_top_left_corners = \
            bucket_markers_detector.convert_bucket_marker_top_left_corners_to_original_image(
                bucket_marker_top_left_corners_on_smaller_image,
                image_shape)

        # that
        self.assertEqual(actual_convert_bucket_marker_top_left_corners, expected_convert_bucket_marker_top_left_corners)

    def test_get_bounding_rectangles_working(self):
        # given
        bucket_marker_template = \
            cv2.imread("./images/BucketMarkersDetector/test_get_bounding_rectangle_working__bucket_marker_template.jpg")
        bucket_markers_detector = BucketMarkersDetector(bucket_marker_template,
                                                        bucket_marker_template_original_resolution=(2560, 1920),
                                                        template_matching_resolution=(2560, 1920),
                                                        expected_template_matching_threshold=2.3,
                                                        bucket_number_identifier=None)

        image = cv2.imread("./images/BucketMarkersDetector/test_get_bounding_rectangles_working__image.jpg")

        bucket_marker_top_left_corners_on_original_image = [[727, 843], [1500, 843]]

        bounding_rectangle_1 = Rectangle(top_left_x=727, top_left_y=843, width=374, high=368)
        bounding_rectangle_2 = Rectangle(top_left_x=1500, top_left_y=843, width=374, high=368)
        expected_bounding_rectangles = [bounding_rectangle_1, bounding_rectangle_2]

        # when
        actual_bounding_rectangles = \
            bucket_markers_detector.get_bounding_rectangles(bucket_marker_top_left_corners_on_original_image)

        # that
        self.assertEquals(actual_bounding_rectangles, expected_bounding_rectangles)


if __name__ == '__main__':
    unittest.main()