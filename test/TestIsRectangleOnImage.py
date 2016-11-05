import unittest
import cv2
from IsRectangleOnImage import IsRectangleOnImage
from Rectangle import Rectangle


class TestIsRectangleOnImage(unittest.TestCase):
    def test_top_left_vertex_is_not_on_image(self):
        # given
        lolling_rectangle = Rectangle(-10, -10, 20, 30)
        image = cv2.imread("./images/test_image_IsRectangleOnImage_100x100.jpg")

        # when
        is_rectangle_om_image = IsRectangleOnImage(lolling_rectangle,
                                                   image)

        # that
        self.assertEqual(is_rectangle_om_image.is_it(), False)

    def test_right_button_vertex_is_not_on_image(self):
        # given
        lolling_rectangle = Rectangle(90, 90, 20, 30)
        image = cv2.imread("./images/test_image_IsRectangleOnImage_100x100.jpg")

        # when
        is_rectangle_om_image = IsRectangleOnImage(lolling_rectangle,
                                                   image)

        # that
        self.assertEqual(is_rectangle_om_image.is_it(), False)


if __name__ == '__main__':
    unittest.main()