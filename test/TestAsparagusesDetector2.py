import unittest
import cv2
import numpy as np

from AsparagusesDetector2 import AsparagusesDetector2
from DetectionToOneAsparagusAnalysis import DetectionToOneAsparagusAnalysis


class TestAsparagusesDetector2(unittest.TestCase):
    def test_data_to_analysis_one_asparagus_images_two_asparaguses(self):
        # given
        asparagus_detector_2 = AsparagusesDetector2(global_threshold=180,
                                                    high_width_ratio=4,
                                                    minimum_area=200,
                                                    detection_resolution=(160, 90),
                                                    extension_factor=0.5)

        image = \
            cv2.imread("./images/AsparagusesDetector2/"
                       "test_data_to_analysis_one_asparagus_images_two_asparaguses_input.png")

        expected_image1 = cv2.imread("./images/AsparagusesDetector2/"
                                    "test_data_to_analysis_one_asparagus_images_two_asparaguses_output1.png")
        expected_opencv_rectangle1 = ((320.37474060058594, 1109.6187744140625),
                                      (1666.9730072021484, 169.24445343017578),
                                      -73.55961608886719)

        expected_image2 = cv2.imread("./images/AsparagusesDetector2/"
                                    "test_data_to_analysis_one_asparagus_images_two_asparaguses_output2.png")
        expected_opencv_rectangle2 = ((978.5949096679688, 1115.748046875),
                                      (276.78464126586914, 1766.16650390625),
                                      -1.1457629203796387)

        expected_data_to_analysis = \
            [DetectionToOneAsparagusAnalysis(expected_image1, expected_opencv_rectangle1),
             DetectionToOneAsparagusAnalysis(expected_image2, expected_opencv_rectangle2)]

        # when
        actual_data_to_analysis = asparagus_detector_2.data_to_analysis_one_asparagus_images(image)

        # that
        self.assertEquals(actual_data_to_analysis, expected_data_to_analysis)

    def test_image_detection_on(self):
        # given
        asparagus_detector_2 = AsparagusesDetector2(global_threshold=None,
                                                    high_width_ratio=None,
                                                    minimum_area=None,
                                                    detection_resolution=(160, 90),
                                                    extension_factor=None)

        image = cv2.imread("./images/AsparagusesDetector2/test_image_detection_on_input.png")

        expected_image_detection_on = cv2.imread("./images/AsparagusesDetector2/test_image_detection_on_output.png",
                                                 cv2.IMREAD_GRAYSCALE)

        # when
        actual_image_detection_on = asparagus_detector_2.image_detection_on(image)
        cv2.imwrite("./images/AsparagusesDetector2/test_image_detection_on_output.png",
                   actual_image_detection_on)

        # that
        self.assertEqual(np.array_equal(actual_image_detection_on, expected_image_detection_on), True)

    def test_get_candidate_contours_working(self):
        # given
        asparagus_detector_2 = AsparagusesDetector2(global_threshold=200,
                                                    high_width_ratio=None,
                                                    minimum_area=None,
                                                    detection_resolution=(160, 90),
                                                    extension_factor=None)

        image_detection_on = \
            cv2.imread("./images/AsparagusesDetector2/test_get_candidate_contours_working__image_detection_on.png",
                       flags=cv2.IMREAD_GRAYSCALE)

        expected_candidate_contours = [np.array([[[8, 28]], [[8, 144]], [[9, 145]], [[23, 145]],
                                                 [[24, 144]], [[24,  28]]],
                                                dtype=np.int32)]

        # when
        actual_candidate_contours = asparagus_detector_2.get_candidate_contours(image_detection_on)

        # that
        self.assertEqual(np.array_equal(actual_candidate_contours, expected_candidate_contours), True)

    def test_asparagus_contours_bounding_rectangles_working(self):
        # given
        asparagus_detector_2 = AsparagusesDetector2(global_threshold=None,
                                                    high_width_ratio=4,
                                                    minimum_area=300,
                                                    detection_resolution=None,
                                                    extension_factor=None)

        candidate_contours = \
            [np.array([[[8,   28]], [[8, 144]], [[9, 145]], [[23, 145]], [[24, 144]], [[24,  28]]], dtype=np.int32),
             np.array([[[8,   28]], [[8, 144]]], dtype=np.int32),
             np.array([[[24, 144]], [[24, 28]]], dtype=np.int32)]

        expected_asparagus_contours_bounding_rectangles = [((16.0, 86.5), (117.0, 16.0), -90.0)]

        # when
        actual_asparagus_contours_bounding_rectangles = \
            asparagus_detector_2.asparagus_contours_bounding_rectangles(candidate_contours)

        # that
        self.assertEqual(np.array_equal(actual_asparagus_contours_bounding_rectangles,
                                        expected_asparagus_contours_bounding_rectangles), True)

    def test_is_rectangle_vertically_on_image__hangs_to_the_left(self):
        # given
        opencv_rectangle = (5, 10), (20, 100), 0

        expected_is_rectangle_vertically_on_image = False

        # when
        actual_is_rectangle_vertically_on_image = AsparagusesDetector2.is_rectangle_vertically_on_image(
                                                        image_width=1080,
                                                        opencv_rectangle=opencv_rectangle)

        # that
        self.assertEqual(actual_is_rectangle_vertically_on_image, expected_is_rectangle_vertically_on_image)

    def test_is_rectangle_vertically_on_image__hangs_to_the_right(self):
        # given
        opencv_rectangle = (1075, 10), (20, 100), 0

        expected_is_rectangle_vertically_on_image = False

        # when
        actual_is_rectangle_vertically_on_image = AsparagusesDetector2.is_rectangle_vertically_on_image(
            image_width=1080,
            opencv_rectangle=opencv_rectangle)

        # that
        self.assertEqual(actual_is_rectangle_vertically_on_image, expected_is_rectangle_vertically_on_image)

if __name__ == '__main__':
    unittest.main()
