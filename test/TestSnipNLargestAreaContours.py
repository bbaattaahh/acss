import unittest
import cv2
import numpy as np

from SnipNLargestAreaContours import SnipNLargestAreaContours


class TestSnipNLargestAreaContours(unittest.TestCase):
    def test_n_largest_area_contours_images__with_invert(self):
        # given
        image = cv2.imread("./images/SnipNLargestAreaContours/"
                           "test_n_largest_area_contours_image__with_invert__input_image.png",
                           cv2.IMREAD_GRAYSCALE)
        n = 2
        invert_flag = True
        snip_n_largest_area_contours = SnipNLargestAreaContours(image, n, invert_flag)

        expected_largest_contour_image_1 = cv2.imread(
            "./images/SnipNLargestAreaContours/test_n_largest_area_contours_images__with_invert__snipped_image_1.png",
            flags=cv2.IMREAD_GRAYSCALE)
        expected_largest_contour_image_2 = cv2.imread(
            "./images/SnipNLargestAreaContours/test_n_largest_area_contours_images__with_invert__snipped_image_2.png",
            flags=cv2.IMREAD_GRAYSCALE)

        expected_n_largest_area_contours_images = [expected_largest_contour_image_1, expected_largest_contour_image_2]

        # when
        actual_n_largest_area_contours_images = snip_n_largest_area_contours.n_largest_area_contours_images

        # that
        self.assertEqual(np.array_equal(actual_n_largest_area_contours_images[0],
                                        expected_n_largest_area_contours_images[0]), True)
        self.assertEqual(np.array_equal(actual_n_largest_area_contours_images[1],
                                        expected_n_largest_area_contours_images[1]), True)
        # self.assertEqual(np.array_equal(actual_n_largest_area_contours_images,
        #                                 expected_n_largest_area_contours_images),
        #                  True)

    def test_snip_n_largest_area_contours_image__no_contours(self):
        # given
        image = cv2.imread("./images/SnipNLargestAreaContours/"
                           "test_snip_n_largest_area_contours_image__no_contours__input_image.png",
                           cv2.IMREAD_GRAYSCALE)
        n = 2
        invert_flag = False
        snip_n_largest_area_contours = SnipNLargestAreaContours(image, n, invert_flag)

        expected_n_largest_area_contours_images = []

        # when
        actual_n_largest_area_contours_images = snip_n_largest_area_contours.n_largest_area_contours_images

        # that
        self.assertEqual(np.array_equal(actual_n_largest_area_contours_images, expected_n_largest_area_contours_images),
                         True)

    def test_invert_image_working(self):
        # given
        image = cv2.imread("./images/SnipNLargestAreaContours/test_invert_image_working__input_image.png",
                           cv2.IMREAD_GRAYSCALE)

        expected_inverted_image = \
            cv2.imread("./images/SnipNLargestAreaContours/test_invert_image_working__output_image.png",
                       cv2.IMREAD_GRAYSCALE)

        # when
        actual_inverted_image = SnipNLargestAreaContours.invert_image(image)

        # that
        self.assertEqual(np.array_equal(actual_inverted_image, expected_inverted_image), True)

    def test_delete_contours_working(self):
        # given
        image = cv2.imread("./images/SnipNLargestAreaContours/test_delete_contours_working__input_image.png",
                           cv2.IMREAD_GRAYSCALE)
        n = 2
        snip_n_largest_area_contours = SnipNLargestAreaContours(image=image,
                                                                n=n)

        expected_output_image = \
            cv2.imread("./images/SnipNLargestAreaContours/test_delete_contours_working__output_image.png",
                       cv2.IMREAD_GRAYSCALE)

        # when
        snip_n_largest_area_contours.delete_contours()
        actual_output_image = snip_n_largest_area_contours.image

        # that
        self.assertEqual(np.array_equal(actual_output_image, expected_output_image), True)

    def test_contours_to_delete__2_smaller_upper_rectangles(self):
        # given
        image = cv2.imread("./images/SnipNLargestAreaContours/test_contours_to_delete__2_smaller_upper_rectangles.png",
                           cv2.IMREAD_GRAYSCALE)
        n = 2
        get_n_largest_area_contours = SnipNLargestAreaContours(image=image,
                                                               n=n)

        expected_contours_to_delete = [np.array([[[27, 5]], [[27, 17]], [[88, 17]], [[88, 5]]]),
                                       np.array([[[4,  5]], [[4,  16]], [[21, 16]], [[21, 5]]])]

        # when
        actual_contours_to_delete = get_n_largest_area_contours.contours_to_delete

        # that
        self.assertEqual(np.array_equal(actual_contours_to_delete, expected_contours_to_delete), True)

    def test_area_limit_working(self):
        # given
        image = cv2.imread("./images/SnipNLargestAreaContours/test_area_limit_working.png",
                           cv2.IMREAD_GRAYSCALE)
        get_n_largest_area_contours = SnipNLargestAreaContours(image=image, n=1)

        expected_area_limit = 5246

        # when
        actual_area_limit = get_n_largest_area_contours.area_limit

        # that
        self.assertEqual(np.array_equal(actual_area_limit, expected_area_limit), True)

    def test_first_level_contours_working(self):
        # given
        image = cv2.imread("./images/SnipNLargestAreaContours/test_first_level_contours_working.png",
                           cv2.IMREAD_GRAYSCALE)
        get_n_largest_area_contours = SnipNLargestAreaContours(image=image, n=None)

        expected_first_level_contours = [np.array([[[27, 5]], [[27, 91]], [[88, 91]], [[88, 5]]]),
                                         np.array([[[4,  5]], [[4,  91]], [[16, 91]], [[16, 5]]])]

        # when
        actual_first_level_contours = get_n_largest_area_contours.first_level_contours

        # that
        self.assertEqual(np.array_equal(actual_first_level_contours, expected_first_level_contours), True)

if __name__ == '__main__':
    unittest.main()
