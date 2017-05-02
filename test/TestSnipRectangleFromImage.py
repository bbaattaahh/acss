import numpy as np
import cv2
import unittest

from SnipRectangleFromImage import SnipRectangleFromImage
from Rectangle import Rectangle


class TestSnipRectangleFromImage(unittest.TestCase):

    def test_snipped_image__rgb_image__0_angle(self):
        # given
        image = cv2.imread("./images/SnipRectangleFromImage/test_snipped_image__0_angle__rgb_image_input.jpg")
        rectangle = Rectangle(top_left_x=165,
                              top_left_y=0,
                              width=170,
                              high=70,
                              angle=0)

        snip_from_image = SnipRectangleFromImage(image, rectangle)

        expected_snipped_image = \
            cv2.imread("./images/SnipRectangleFromImage/test_snipped_image__0_angle__rgb_image_output.png")

        # when
        actual_snipped_image = snip_from_image.snipped_image

        # that
        self.assertEqual(np.array_equal(actual_snipped_image, expected_snipped_image), True)

    def test_snipped_image__gray_image__0_angle(self):
        # given
        image = cv2.imread("./images/SnipRectangleFromImage/test_snipped_image__gray_image__0_angle__input.jpg",
                           cv2.IMREAD_GRAYSCALE)

        rectagle = Rectangle(top_left_x=165,
                             top_left_y=0,
                             width=170,
                             high=70,
                             angle=0)

        snip_from_image = SnipRectangleFromImage(image, rectagle)

        expected_snipped_image = \
            cv2.imread("./images/SnipRectangleFromImage/test_snipped_image__gray_image__0_angle__output.png",
                       cv2.IMREAD_GRAYSCALE)

        # when
        actual_snipped_image = snip_from_image.snipped_image

        # that
        self.assertEqual(np.array_equal(actual_snipped_image, expected_snipped_image), True)

    def test_snipped_image__rgb_image__45_angle(self):
        # given
        image = cv2.imread("./images/SnipRectangleFromImage/test_snipped_image__45_angle__rgb_image_input.jpg")
        rectangle = Rectangle(top_left_x=94,
                              top_left_y=75,
                              width=100,
                              high=200,
                              angle=45)

        snip_from_image = SnipRectangleFromImage(image, rectangle)

        expected_snipped_image = \
            cv2.imread("./images/SnipRectangleFromImage/test_snipped_image__45_angle__rgb_image_output.png")

        # when
        actual_snipped_image = snip_from_image.snipped_image
        cv2.imwrite("./images/SnipRectangleFromImage/test_snipped_image__45_angle__rgb_image_output.png",
                    actual_snipped_image)

        # that
        self.assertEqual(np.array_equal(actual_snipped_image, expected_snipped_image), True)

    def test_calculate_new_coordinate_after_rotation__angle_is_45(self):
        # given
        point = [0, 0]
        blank_image = np.zeros((10, 10, 3))

        expected_rotated_point = [10/2*(np.sqrt(2)), 0.]

        # when
        actual_rotated_point = SnipRectangleFromImage.calculate_new_coordinate_after_rotation(blank_image, 45, point )

        # that
        self.assertAlmostEqual(actual_rotated_point, expected_rotated_point, delta=0.0000001)

    def test_calculate_new_coordinate_after_rotation__angle_is_minus_45(self):
        # given
        point = [0, 0]
        blank_image = np.zeros((10, 10, 3))

        expected_rotated_point = [0., 10/2*(np.sqrt(2))]

        # when
        actual_rotated_point = \
            SnipRectangleFromImage.calculate_new_coordinate_after_rotation(image=blank_image,
                                                                           angle=-45,
                                                                           vertex=point)

        # that
        self.assertAlmostEqual(actual_rotated_point, expected_rotated_point, delta=0.0000001)

    def test_calculate_new_coordinate_after_rotation__half_w_and_angle_is_45(self):
        # given
        point = [5, 0]
        blank_image = np.zeros((10, 10, 3))

        expected_rotated_point = [10/4*3*(np.sqrt(2)), 10/4*(np.sqrt(2))]

        # when
        actual_rotated_point = \
            SnipRectangleFromImage.calculate_new_coordinate_after_rotation(image=blank_image,
                                                                           angle=45,
                                                                           vertex=point)

        # that
        self.assertAlmostEqual(actual_rotated_point, expected_rotated_point, delta=0.0000001)

    def test_calculate_new_coordinate_after_rotation__angle_is_90(self):
        # given
        point = [0, 0]
        blank_image = np.zeros((10, 10, 3))

        expected_rotated_point = [10., 0.]

        # when
        actual_rotated_point = \
            SnipRectangleFromImage.calculate_new_coordinate_after_rotation(image=blank_image,
                                                                           angle=90,
                                                                           vertex=point)

        # that
        self.assertAlmostEqual(actual_rotated_point, expected_rotated_point, delta=0.0000001)

    def test_calculate_new_coordinate_after_rotation__center(self):
        # given
        point = [5., 5.]
        blank_image = np.zeros((10, 10, 3))

        expected_rotated_point = [10 / 2 * (np.sqrt(2)), 10 / 2 * (np.sqrt(2))]

        # when
        actual_rotated_point = SnipRectangleFromImage.calculate_new_coordinate_after_rotation(blank_image, 45,
                                                                                              point)

        # that
        self.assertAlmostEqual(actual_rotated_point, expected_rotated_point, delta=0.0000001)



            # def test_calculate_new_coordinate_after_rotation__real_rectangle(self):
    #     # given
    #     point = [5, 0]
    #     blank_image = np.zeros((10, 100, 3))
    #
    #     expected_rotated_point = [10/4*3*(np.sqrt(2)), 10/4*(np.sqrt(2))]
    #
    #     # when
    #     actual_rotated_point = \
    #         SnipRectangleFromImage.calculate_new_coordinate_after_rotation(image=blank_image,
    #                                                                        angle=45,
    #                                                                        vertex=point)
    #
    #     # that
    #     self.assertAlmostEqual(actual_rotated_point, expected_rotated_point, delta=0.0000001)

