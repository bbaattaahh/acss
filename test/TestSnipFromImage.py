import numpy as np
import cv2
import unittest

from SnipFromImage import SnipFromImage


class TestSnipFromImage(unittest.TestCase):

    def test_snipped_image__rgb_image(self):
        # given
        image = cv2.imread("./images/SnipFromImage/test_snipped_image__rgb_image_input.jpg")
        top_left_corner_x = 165
        top_left_corner_y = 0
        width = 170
        height = 70

        snip_from_image = SnipFromImage(image=image,
                                        x=top_left_corner_x,
                                        y=top_left_corner_y,
                                        w=width,
                                        h=height)

        expected_snipped_image = cv2.imread("./images/SnipFromImage/test_snipped_image__rgb_image_output.png")

        # when
        actual_snipped_image = snip_from_image.snipped_image

        # that
        self.assertEqual(np.array_equal(actual_snipped_image, expected_snipped_image), True)

    def test_snipped_image__gray_image(self):
        # given
        image = cv2.imread("./images/SnipFromImage/test_snipped_image__gray_image_input.jpg",
                           cv2.IMREAD_GRAYSCALE)
        top_left_corner_x = 165
        top_left_corner_y = 0
        width = 170
        height = 70

        snip_from_image = SnipFromImage(image=image,
                                        x=top_left_corner_x,
                                        y=top_left_corner_y,
                                        w=width,
                                        h=height)

        expected_snipped_image = cv2.imread("./images/SnipFromImage/test_snipped_image__gray_image_output.png",
                                            cv2.IMREAD_GRAYSCALE)

        # when
        actual_snipped_image = snip_from_image.snipped_image

        # that
        self.assertEqual(np.array_equal(actual_snipped_image, expected_snipped_image), True)
