import unittest
import cv2

from IsRectangleOnOriginalImage import IsRectangleOnOriginalImage
from Rectangle import Rectangle


class TestIsRectangleOnOriginalImage(unittest.TestCase):
    def test_is_rectangle_on_original_image_true(self):
        # given
        rectangle_on_rotated_image = Rectangle(20, 20, 20, 30, 0)
        original_image = cv2.imread("./images/IsRectangleOnOriginalImage/test_is_rectangle_on_original_image_true_input.jpg")
        angle = 0

        # when
        is_rectangle_on_original_image = IsRectangleOnOriginalImage(original_image,
                                                                    rectangle_on_rotated_image,
                                                                    angle)

        # that
        self.assertEqual(is_rectangle_on_original_image.is_it, True)


if __name__ == '__main__':
    unittest.main()