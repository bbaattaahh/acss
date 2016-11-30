import unittest
import cv2
import numpy as np

from RGBImageSlicer import RGBImageSlicer


class TestRGBImageSlicer(unittest.TestCase):
    def test_first_quarter_working(self):
        # given
        image = cv2.imread("./images/RGBImageSlicer/test_rgb_image_slicer_input_image.jpg")
        rgb_image_slicer = RGBImageSlicer(image=image)

        expected_first_quarter = cv2.imread("./images/RGBImageSlicer/test_rgb_image_slicer_first_quarter_output.png")

        # when
        actual_first_quarter = rgb_image_slicer.first_quarter

        # that
        self.assertEqual(np.array_equal(actual_first_quarter, expected_first_quarter), True)

    def test_second_quarter_working(self):
        # given
        image = cv2.imread("./images/RGBImageSlicer/test_rgb_image_slicer_input_image.jpg")
        rgb_image_slicer = RGBImageSlicer(image=image)

        expected_second_quarter = cv2.imread("./images/RGBImageSlicer/test_rgb_image_slicer_second_quarter_output.png")

        # when
        actual_second_quarter = rgb_image_slicer.second_quarter

        # that
        self.assertEqual(np.array_equal(actual_second_quarter, expected_second_quarter), True)

    def test_third_quarter_working(self):
        # given
        image = cv2.imread("./images/RGBImageSlicer/test_rgb_image_slicer_input_image.jpg")
        rgb_image_slicer = RGBImageSlicer(image=image)

        expected_third_quarter = cv2.imread("./images/RGBImageSlicer/test_rgb_image_slicer_third_quarter_output.png")

        # when
        actual_third_quarter = rgb_image_slicer.third_quarter

        # that
        self.assertEqual(np.array_equal(actual_third_quarter, expected_third_quarter), True)

    def test_fourth_quarter_working(self):
        # given
        image = cv2.imread("./images/RGBImageSlicer/test_rgb_image_slicer_input_image.jpg")
        rgb_image_slicer = RGBImageSlicer(image=image)

        expected_fourth_quarter = cv2.imread("./images/RGBImageSlicer/test_rgb_image_slicer_fourth_quarter_output.png")

        # when
        actual_fourth_quarter = rgb_image_slicer.fourth_quarter

        # that
        self.assertEqual(np.array_equal(actual_fourth_quarter, expected_fourth_quarter), True)

if __name__ == '__main__':
    unittest.main()
