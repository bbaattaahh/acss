import unittest
import cv2
import numpy as np

from AsparagusesDetector2 import AsparagusesDetector2
from DetectionToOneAsparagusAnalysis import DetectionToOneAsparagusAnalysis
from Rectangle import Rectangle


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
        expected_rectangle1 = Rectangle(top_left_x=44.426171078962284,
                                                 top_left_y=284.99101714842004,
                                                 width=560.0,
                                                 high=100.0,
                                                 angle=-12)
        expected_image2 = cv2.imread("./images/AsparagusesDetector2/"
                                    "test_data_to_analysis_one_asparagus_images_two_asparaguses_output2.png")
        expected_rectangle2 = Rectangle(top_left_x=44.426171078962284,
                                                 top_left_y=284.99101714842004,
                                                 width=560.0,
                                                 high=100.0,
                                                 angle=-12)

        expected_data_to_analysis = \
            [DetectionToOneAsparagusAnalysis(expected_image1, expected_rectangle1),
             DetectionToOneAsparagusAnalysis(expected_image2, expected_rectangle2)]

        # when
        actual_data_to_analysis = asparagus_detector_2.data_to_analysis_one_asparagus_images(image)

        # that
        self.assertEqual(actual_data_to_analysis, expected_data_to_analysis)

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

    def test_rectangle_on_original_image_working(self):
        # given
        asparagus_detector_2 = AsparagusesDetector2(global_threshold=None,
                                                    high_width_ratio=None,
                                                    minimum_area=None,
                                                    detection_resolution=(160, 90),
                                                    extension_factor=None)

        image_detection_on = np.zeros((160, 90))

        asparagus_contours_bounding_rectangle = (16.0, 86.5), (3.0, 4.0), -45.0

        expected_rectangle_on_original_image = Rectangle(top_left_x=8,
                                                         top_left_y=28,
                                                         width=3,
                                                         high=4,
                                                         angle=-45.0)

        # when
        actual_rectangle_on_original_image = \
            asparagus_detector_2.rectangle_on_original_image(image_detection_on=image_detection_on,
                                                             image_shape=(160, 90),
                                                             opencv_rectangle=asparagus_contours_bounding_rectangle)

        # that
        self.assertEqual(actual_rectangle_on_original_image, expected_rectangle_on_original_image)








            # def test_asparagus_candidates_2_candidates(self):
    #     # given
    #     cascade_file = "./cascade_files/cascade.xml"
    #     detection_resolution = 120, 160
    #     swing_angle = 8
    #     detect_asparaguses = AsparagusesDetector2(cascade_file=cascade_file,
    #                                               detection_resolution=detection_resolution,
    #                                               swing_angle=swing_angle)
    #     image_detection_on = \
    #         cv2.imread("./images/AsparagusesDetector/test_asparagus_detection_candidates__image_detection_on.png",
    #                    flags=cv2.IMREAD_GRAYSCALE)
    #
    #     asparagus_candidate_1 = Rectangle(16, 39, 140, 25, -6)
    #     asparagus_candidate_2 = Rectangle(11, 56, 140, 25, -1)
    #
    #     expected_candidates = [asparagus_candidate_1, asparagus_candidate_2]
    #
    #     # when
    #     actual_candidates = detect_asparaguses.asparagus_candidates(image_detection_on)
    #
    #     # that
    #     self.assertEqual(sorted(actual_candidates), sorted(expected_candidates))


if __name__ == '__main__':
    unittest.main()
