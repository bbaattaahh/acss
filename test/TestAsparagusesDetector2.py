import unittest
import cv2
import numpy as np

from AsparagusesDetector2 import AsparagusesDetector2
from DetectionToOneAsparagusAnalysis import DetectionToOneAsparagusAnalysis


class TestAsparagusesDetector2(unittest.TestCase):
    def test_data_to_analysis_one_asparagus_images_working(self):
        # One asparagus detected. Other don't because its bounding rectangle hangs out.
        # given
        asparagus_detector_2 = AsparagusesDetector2(global_threshold=180,
                                                    high_width_ratio=4,
                                                    minimum_area=200,
                                                    detection_resolution=(160, 90),
                                                    vertical_extension_factor=0.5,
                                                    horizontal_extension_factor=0.5)

        image = \
            cv2.imread("./images/AsparagusesDetector2/"
                       "test_data_to_analysis_one_asparagus_images_working__input.png")

        expected_image1 = cv2.imread("./images/AsparagusesDetector2/"
                                    "test_data_to_analysis_one_asparagus_images_working__output1.png")
        expected_opencv_rectangle1 = ((320.37474060058594, 1109.6187744140625),
                                      (169.24445343017578, 1666.9730072021484),
                                      16.440383911132812)

        expected_data_to_analysis = \
            [DetectionToOneAsparagusAnalysis(expected_image1, expected_opencv_rectangle1)]

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
                                                    vertical_extension_factor=None,
                                                    horizontal_extension_factor=None)

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
                                                    vertical_extension_factor=None,
                                                    horizontal_extension_factor=None)

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
                                                    vertical_extension_factor=None,
                                                    horizontal_extension_factor=None)

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

    def test_opencv_rectangle_on_original_image_working(self):
        # given
        opencv_rectangle = (5, 10), (20, 100), 45

        expected_opencv_rectangle_on_original_image = (10, 20), (40, 200), 45

        # when
        actual_is_rectangle_vertically_on_image = AsparagusesDetector2.opencv_rectangle_on_original_image(
                                                        image_shape=(1920, 1080),
                                                        image_detection_on_shape=(960, 540),
                                                        opencv_rectangle=opencv_rectangle)

        # that
        self.assertEqual(actual_is_rectangle_vertically_on_image, expected_opencv_rectangle_on_original_image)

    def test_extend_opencv_rectangle_working(self):
        # given
        opencv_rectangle = (5, 10), (20, 100), 45

        asparagus_detector = AsparagusesDetector2(global_threshold=None,
                                                  high_width_ratio=None,
                                                  minimum_area=None,
                                                  detection_resolution=None,
                                                  vertical_extension_factor=0.5,
                                                  horizontal_extension_factor=0.25)

        expected_extended_opencv_rectangle = (5, 10), (25, 150), 45

        # when
        actual_extended_opencv_rectangle = asparagus_detector.extend_opencv_rectangle(opencv_rectangle)

        # that
        self.assertEqual(actual_extended_opencv_rectangle, expected_extended_opencv_rectangle)

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

    def test_orientation_correction__hangs_to_the_right(self):
        # given
        horizontally_long_rectangle = ((20, 30), (100, 25), -10)

        expected_corrected_opencv_rectangle = ((20, 30), (25, 100), 80)

        # when
        actual_corrected_opencv_rectangle = AsparagusesDetector2.orientation_correction(horizontally_long_rectangle)

        # that
        self.assertEqual(np.array_equal(actual_corrected_opencv_rectangle, expected_corrected_opencv_rectangle), True)

    def test_subimage__snip_horse_head(self):
        # given
        image = cv2.imread("./images/AsparagusesDetector2/test_subimage__snip_horse_head_input.jpg")
        opencv_rectangle = (77, 93), (75, 100), 45

        expected_subimage = cv2.imread("./images/AsparagusesDetector2/test_subimage__snip_horse_head_output.png")

        # when
        actual_subimage = AsparagusesDetector2.subimage(image, opencv_rectangle)

        # that
        self.assertEqual(np.array_equal(actual_subimage, expected_subimage), True)




if __name__ == '__main__':
    unittest.main()
