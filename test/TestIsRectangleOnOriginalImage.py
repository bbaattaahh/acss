import unittest
import cv2

from IsRectangleOnOriginalImage import IsRectangleOnOriginalImage
from Rectangle import Rectangle


class TestIsRectangleOnOriginalImage(unittest.TestCase):
    def test_is_rectangle_on_original_image_true(self):
        # given
        rectangle_on_rotated_image = Rectangle(20, 20, 20, 30, 0)
        original_image = cv2.imread(
            "./images/IsRectangleOnOriginalImage/test_is_rectangle_on_original_image_true_input.jpg")
        angle = 0

        # when
        is_rectangle_on_original_image = IsRectangleOnOriginalImage(original_image,
                                                                    rectangle_on_rotated_image,
                                                                    angle)

        # that
        self.assertEqual(is_rectangle_on_original_image.is_it, True)

    def test_calculate_original_coordinate_before_rotation__no_rotation(self):
        # given
        original_image = cv2.imread(
            "./images/IsRectangleOnOriginalImage/test_calculate_original_coordinate_before_rotation_working_input.jpg")
        rectangle_on_rotated_image = Rectangle(20, 20, 20, 30, 0)
        angle = 0
        vertex = [0, 0]
        expected_original_vertex = [0, 0]

        # when
        is_rectangle_on_original_image = IsRectangleOnOriginalImage(original_image,
                                                                    rectangle_on_rotated_image,
                                                                    angle)
        actual_original_vertex = is_rectangle_on_original_image.calculate_original_coordinate_before_rotation(vertex)

        # that
        self.assertEqual(actual_original_vertex, expected_original_vertex)

    def test_calculate_original_coordinate_before_rotation__45_rotation(self):
        # given
        original_image = cv2.imread(
            "./images/IsRectangleOnOriginalImage/test_calculate_original_coordinate_before_rotation_working_input.jpg")
        rectangle_on_rotated_image = Rectangle(20, 20, 20, 30, 0)
        angle = 45
        vertex = [0, 0]
        expected_original_vertex = [160, -160.00000000000006]

        # when
        is_rectangle_on_original_image = IsRectangleOnOriginalImage(original_image,
                                                                    rectangle_on_rotated_image,
                                                                    angle)
        actual_original_vertex = is_rectangle_on_original_image.calculate_original_coordinate_before_rotation(vertex)

        # that
        self.assertEqual(actual_original_vertex, expected_original_vertex)

    def test_is_vertex_on_original_image__false(self):
        # given
        original_image = cv2.imread(
            "./images/IsRectangleOnOriginalImage/test_is_vertex_on_original_image_input.jpg")
        rectangle_on_rotated_image = Rectangle(0, 0, 0, 0, 0)
        angle = 45
        vertex = [641, 480]

        # when
        is_rectangle_on_original_image = IsRectangleOnOriginalImage(original_image,
                                                                    rectangle_on_rotated_image,
                                                                    angle)
        actual_decision = is_rectangle_on_original_image.is_vertex_on_original_image(vertex)

        # that
        self.assertEqual(actual_decision, False)


if __name__ == '__main__':
    unittest.main()
