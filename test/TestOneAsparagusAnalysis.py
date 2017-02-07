import unittest
import cv2
import numpy as np

from DetectionToOneAsparagusAnalysis import DetectionToOneAsparagusAnalysis
from Rectangle import Rectangle
from OneAsparagusAnalysis import OneAsparagusAnalysis


class TestOneAsparagusAnalysis(unittest.TestCase):
    def test_get_contour_working(self):
        # given
        image = cv2.imread(
            "./images/OneAsparagusAnalysis/test_get_contour_working_input.jpg")
        non_used_rectangle = Rectangle(0, 0, 0, 0, 0)
        detection_to_one_asparagus_analysis = DetectionToOneAsparagusAnalysis(image, non_used_rectangle)
        one_asparagus_analysis = OneAsparagusAnalysis(detection_to_one_asparagus_analysis)

        jpg_distorted_contour = cv2.imread("./images/OneAsparagusAnalysis/test_get_contour_working_output.jpg",
                                           cv2.IMREAD_GRAYSCALE)
        _, expected_contour = cv2.threshold(jpg_distorted_contour, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        # when
        actual_contour = one_asparagus_analysis.asparagus_contour

        # that
        self.assertEqual(np.array_equal(actual_contour, expected_contour), True)

    def test_asparagus_in_smallest_enclosing_box_working(self):
        # given
        image = cv2.imread(
            "./images/OneAsparagusAnalysis/test_asparagus_in_smallest_enclosing_box_working_input.jpg")
        non_used_rectangle = Rectangle(0, 0, 0, 0, 0)
        detection_to_one_asparagus_analysis = DetectionToOneAsparagusAnalysis(image, non_used_rectangle)
        one_asparagus_analysis = OneAsparagusAnalysis(detection_to_one_asparagus_analysis)

        expected_asparagus_in_smallest_enclosing_box = \
            cv2.imread("./images/OneAsparagusAnalysis/test_asparagus_in_smallest_enclosing_box_working_output.png")

        # when
        actual_asparagus_in_smallest_enclosing_box = one_asparagus_analysis.asparagus_in_smallest_enclosing_box

        # that
        self.assertEqual(np.array_equal(actual_asparagus_in_smallest_enclosing_box,
                                        expected_asparagus_in_smallest_enclosing_box),
                         True)

    def test_asparagus_thickness_working(self):
        # given
        image = cv2.imread(
            "./images/OneAsparagusAnalysis/test_test_asparagus_thickness_working.jpg")
        non_used_rectangle = Rectangle(0, 0, 0, 0, 0)
        detection_to_one_asparagus_analysis = DetectionToOneAsparagusAnalysis(image, non_used_rectangle)
        one_asparagus_analysis = OneAsparagusAnalysis(detection_to_one_asparagus_analysis)

        expected_asparagus_thickness = 22

        # when
        actual_asparagus_thickness = one_asparagus_analysis.asparagus_thickness()

        # that
        self.assertEqual(actual_asparagus_thickness, expected_asparagus_thickness)

    def test_asparagus_length_working(self):
        # given
        image = cv2.imread(
            "./images/OneAsparagusAnalysis/test_asparagus_length_working.jpg")
        non_used_rectangle = Rectangle(0, 0, 0, 0, 0)
        detection_to_one_asparagus_analysis = DetectionToOneAsparagusAnalysis(image, non_used_rectangle)
        one_asparagus_analysis = OneAsparagusAnalysis(detection_to_one_asparagus_analysis)

        expected_asparagus_length = 431

        # when
        actual_asparagus_length = one_asparagus_analysis.asparagus_length()

        # that
        self.assertEqual(actual_asparagus_length, expected_asparagus_length)


if __name__ == '__main__':
    unittest.main()
