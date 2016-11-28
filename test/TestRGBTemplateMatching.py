import unittest
import cv2
import numpy as np

from RGBTemplateMatching import RGBTemplateMatching


class TestRGBTemplateMatching(unittest.TestCase):
    def test_rgb_template_matching_working(self):
        # given
        rgb_image = cv2.imread("./images/RGBTemplateMatching/test_rgb_template_matching_working_rgb_image.jpg")
        rgb_template = cv2.imread("./images/RGBTemplateMatching/test_rgb_template_matching_working_rgb_template.jpg")
        threshold = 2.3
        cv2_method = cv2.TM_CCOEFF_NORMED
        rgb_template_matching = RGBTemplateMatching(rgb_image=rgb_image,
                                                    rgb_template=rgb_template,
                                                    threshold=threshold,
                                                    cv2_method=cv2_method)

        expected_rectangle_top_left_vertices =[[ 729, 845],
                                               [1507, 845]]

        # when
        actual_rectangle_top_left_vertices = rgb_template_matching.rectangle_top_left_vertices()

        # that
        self.assertEqual(actual_rectangle_top_left_vertices, expected_rectangle_top_left_vertices)


if __name__ == '__main__':
    unittest.main()