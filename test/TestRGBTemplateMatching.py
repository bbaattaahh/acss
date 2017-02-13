import unittest
import cv2
import numpy as np

from RGBTemplateMatching import RGBTemplateMatching


class TestRGBTemplateMatching(unittest.TestCase):
    def test_rectangle_top_left_vertices_working(self):
        # given
        rgb_image = cv2.imread("./images/RGBTemplateMatching/test_rectangle_top_left_vertices_working_rgb_image.jpg")
        rgb_template = cv2.imread(
            "./images/RGBTemplateMatching/test_rectangle_top_left_vertices_working_rgb_template.jpg")
        threshold = 2.3
        rgb_template_matching = RGBTemplateMatching(rgb_image=rgb_image,
                                                    rgb_template=rgb_template,
                                                    threshold=threshold)

        expected_rectangle_top_left_vertices = [[729, 845],
                                                [1508, 845]]

        # when
        actual_rectangle_top_left_vertices = rgb_template_matching.rectangle_top_left_vertices

        # that
        self.assertEqual(actual_rectangle_top_left_vertices, expected_rectangle_top_left_vertices)

    def test_get_x_coordinates_working(self):
        # given
        rgb_image = cv2.imread("./images/RGBTemplateMatching/test_get_x_coordinates_working_rgb_image.jpg")
        rgb_template = cv2.imread("./images/RGBTemplateMatching/test_get_x_coordinates_working_rgb_template.jpg")
        threshold = 2.3
        rgb_template_matching = RGBTemplateMatching(rgb_image=rgb_image,
                                                    rgb_template=rgb_template,
                                                    threshold=threshold)

        expected_x_coordinates = [729, 1508]

        # when
        actual_x_coordinates = rgb_template_matching.get_x_coordinates()

        # that
        self.assertEqual(actual_x_coordinates, expected_x_coordinates)

    def test_tuple_numpy_array_to_list_working(self):
        # given
        tuple_numpy_array = (np.array([6784, 1234]),)

        expected_list = [6784, 1234]

        # when
        actual_list = RGBTemplateMatching.tuple_numpy_array_to_list(tuple_numpy_array)

        # that
        self.assertEqual(actual_list, expected_list)

    def test_numerical_derivation_position_correction_working(self):
        # given
        positions = [10, 6784]

        expected_corrected_positions = [11, 6785]

        # when
        actual_corrected_positions = RGBTemplateMatching.numerical_derivation_position_correction(positions)

        # that
        self.assertEqual(actual_corrected_positions, expected_corrected_positions)


if __name__ == '__main__':
    unittest.main()
