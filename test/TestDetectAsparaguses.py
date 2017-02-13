import unittest
import cv2
import numpy as np

from DetectAsparaguses import DetectAsparaguses
from DetectionToOneAsparagusAnalysis import DetectionToOneAsparagusAnalysis
from Rectangle import Rectangle


class TestDetectAsparaguses(unittest.TestCase):
    def test_data_to_analysis_one_asparagus_images_one_asparagus(self):
        # given
        image = \
            cv2.imread("./images/DetectAsparaguses/test_data_to_analysis_one_asparagus_images_one_asparagus_input.jpg")
        cascade_file = "./cascade_files/cascade.xml"
        detection_resolution = 120, 160
        swing_angle = 45

        expected_image = \
            cv2.imread("./images/DetectAsparaguses/test_data_to_analysis_one_asparagus_images_one_asparagus_output.png")
        expected_detection_rectangle = Rectangle(top_left_x=44.426171078962284,
                                                 top_left_y=284.99101714842004,
                                                 width=560.0,
                                                 high=100.0,
                                                 angle=-12)

        expected_detection_to_one_asparagus_analysis = DetectionToOneAsparagusAnalysis(
                                                            image=expected_image,
                                                            rectangle_on_original_image=expected_detection_rectangle)

        expected_data_to_analysis = [expected_detection_to_one_asparagus_analysis]

        # when
        detect_asparaguses = DetectAsparaguses(image=image,
                                               cascade_file=cascade_file,
                                               detection_resolution=detection_resolution,
                                               swing_angle=swing_angle)
        actual_data_to_analysis = detect_asparaguses.data_to_analysis_one_asparagus_images

        # that
        self.assertEqual(actual_data_to_analysis, expected_data_to_analysis)

    def test_image_detection_on(self):
        # given
        image = cv2.imread("./images/DetectAsparaguses/test_image_detection_on_input.jpg")
        cascade_file = "./cascade_files/cascade.xml"
        detection_resolution = 120, 160
        detect_asparaguses = DetectAsparaguses(image=image,
                                               cascade_file=cascade_file,
                                               detection_resolution=detection_resolution)

        expected_image_detection_on = cv2.imread("./images/DetectAsparaguses/test_image_detection_on_output.png",
                                                 cv2.IMREAD_GRAYSCALE)

        # when
        actual_image_detection_on = detect_asparaguses.image_detection_on

        # that
        self.assertEqual(np.array_equal(actual_image_detection_on, expected_image_detection_on), True)

    def test_asparagus_candidates_2_candidates(self):
        # given
        image = cv2.imread("./images/DetectAsparaguses/test_asparagus_detection_candidates_input.jpg")
        cascade_file = "./cascade_files/cascade.xml"
        detection_resolution = 120, 160
        swing_angle = 8

        asparagus_candidate_1 = Rectangle(11, 56, 140, 25, -1)
        asparagus_candidate_2 = Rectangle(16, 39, 140, 25, -6)

        expected_candidates = [asparagus_candidate_1, asparagus_candidate_2]

        # when
        detect_asparaguses = DetectAsparaguses(image=image,
                                               cascade_file=cascade_file,
                                               detection_resolution=detection_resolution,
                                               swing_angle=swing_angle)

        actual_candidates = detect_asparaguses.asparagus_candidates

        # that
        self.assertEqual(actual_candidates, expected_candidates)

    def test_rotate_about_center(self):
        # given
        image = cv2.imread("./images/DetectAsparaguses/test_rotate_about_center_input.jpg")
        cascade_file = "./cascade_files/cascade.xml"
        detect_asparaguses = DetectAsparaguses(image=image,
                                               cascade_file=cascade_file)

        expected_rotated_image = cv2.imread("./images/DetectAsparaguses/test_rotate_about_center_output.png")

        # when
        actual_rotated_image = detect_asparaguses.rotate_about_center(image, 25)

        # that
        self.assertEqual(np.array_equal(actual_rotated_image, expected_rotated_image), True)


if __name__ == '__main__':
    unittest.main()
