import unittest
import cv2
import numpy as np

from KeepNLargestAreaContours import KeepNLargestAreaContours


class TestKeepOnlyNLargestAreaContours(unittest.TestCase):
    def test_kept_n_largest_area_contours_image__with_invert(self):
        # given
        image = cv2.imread("./images/KeepNLargestAreaContours/"
                           "test_kept_n_largest_area_contours_image__with_invert__input_image.png",
                           cv2.IMREAD_GRAYSCALE)
        kept_contour_number = 2
        invert_flag = True
        keep_n_largest_area_contours = KeepNLargestAreaContours(image=image,
                                                                kept_contour_number=kept_contour_number,
                                                                invert_flag=invert_flag)

        expected_image = \
            cv2.imread("./images/KeepNLargestAreaContours/"
                       "test_kept_n_largest_area_contours_image__with_invert__output_image.png",
                       cv2.IMREAD_GRAYSCALE)

        # when
        actual_image = keep_n_largest_area_contours.kept_n_largest_area_contours_image

        # that
        self.assertEqual(np.array_equal(actual_image, expected_image), True)

    def test_kept_n_largest_area_contours_image__contour_at_the_edge(self):
        # given
        image = cv2.imread("./images/KeepNLargestAreaContours/"
                           "test_kept_n_largest_area_contours__contour_at_the_edge__input_image.png",
                           cv2.IMREAD_GRAYSCALE)

        keep_n_largest_area_contours = KeepNLargestAreaContours(image=image,
                                                                kept_contour_number=1,
                                                                invert_flag=False)

        expected_output_image = \
            cv2.imread("./images/KeepNLargestAreaContours/"
                       "test_kept_n_largest_area_contours__contour_at_the_edge__output_image.png",
                       cv2.IMREAD_GRAYSCALE)

        # when
        actual_output_image = keep_n_largest_area_contours.kept_n_largest_area_contours_image

        # that
        self.assertEqual(np.array_equal(actual_output_image, expected_output_image), True)

    def test_kept_n_largest_area_contours_image__no_contours(self):
        # given
        image = cv2.imread("./images/KeepNLargestAreaContours/"
                           "test_kept_n_largest_area_contours_image__no_contours__input_image.png",
                           cv2.IMREAD_GRAYSCALE)
        kept_contour_number = 2
        keep_n_largest_area_contours = KeepNLargestAreaContours(image=image,
                                                                kept_contour_number=kept_contour_number)

        expected_image = \
            cv2.imread("./images/KeepNLargestAreaContours/"
                       "test_kept_n_largest_area_contours_image__no_contours__output_image.png",
                       cv2.IMREAD_GRAYSCALE)

        # when
        actual_image = keep_n_largest_area_contours.kept_n_largest_area_contours_image

        # that
        self.assertEqual(np.array_equal(actual_image, expected_image), True)

    def test_invert_image_working(self):
        # given
        image = cv2.imread("./images/KeepNLargestAreaContours/test_invert_image_working__input_image.png",
                           cv2.IMREAD_GRAYSCALE)
        keep_n_largest_area_contours = KeepNLargestAreaContours(image=image,
                                                                kept_contour_number=None)

        expected_inverted_image = \
            cv2.imread("./images/KeepNLargestAreaContours/test_invert_image_working__output_image.png",
                       cv2.IMREAD_GRAYSCALE)

        # when
        keep_n_largest_area_contours.invert_image()
        actual_inverted_image = keep_n_largest_area_contours.image

        # that
        self.assertEqual(np.array_equal(actual_inverted_image, expected_inverted_image), True)

    def test_delete_contours_working(self):
        # given
        image = cv2.imread("./images/KeepNLargestAreaContours/test_delete_contours_working__input_image.png",
                           cv2.IMREAD_GRAYSCALE)
        kept_contour_number = 2
        keep_n_largest_area_contours = KeepNLargestAreaContours(image=image,
                                                                kept_contour_number=kept_contour_number)

        expected_output_image = \
            cv2.imread("./images/KeepNLargestAreaContours/test_delete_contours_working__output_image.png",
                       cv2.IMREAD_GRAYSCALE)

        # when
        keep_n_largest_area_contours.delete_contours()
        actual_output_image = keep_n_largest_area_contours.image

        # that
        self.assertEqual(np.array_equal(actual_output_image, expected_output_image), True)

    def test_contours_to_delete__2_smaller_upper_rectangles(self):
        # given
        image = cv2.imread("./images/KeepNLargestAreaContours/test_contours_to_delete__2_smaller_upper_rectangles.png",
                           cv2.IMREAD_GRAYSCALE)
        kept_contour_number = 2
        keep_n_largest_area_contours = KeepNLargestAreaContours(image=image,
                                                                kept_contour_number=kept_contour_number)

        expected_contours_to_delete = [np.array([[[27, 5]], [[27, 17]], [[88, 17]], [[88, 5]]]),
                                       np.array([[[4,  5]], [[4,  16]], [[21, 16]], [[21, 5]]])]

        # when
        actual_contours_to_delete = keep_n_largest_area_contours.contours_to_delete

        # that
        self.assertEqual(np.array_equal(actual_contours_to_delete, expected_contours_to_delete), True)

    def test_area_limit_working(self):
        # given
        image = cv2.imread("./images/KeepNLargestAreaContours/test_area_limit_working.png",
                           cv2.IMREAD_GRAYSCALE)
        keep_n_largest_area_contours = KeepNLargestAreaContours(image=image, kept_contour_number=1)

        expected_area_limit = 5246

        # when
        actual_area_limit = keep_n_largest_area_contours.area_limit

        # that
        self.assertEqual(np.array_equal(actual_area_limit, expected_area_limit), True)

    def test_first_level_contours_working(self):
        # given
        image = cv2.imread("./images/KeepNLargestAreaContours/test_first_level_contours_working.png",
                           cv2.IMREAD_GRAYSCALE)
        keep_n_largest_area_contours = KeepNLargestAreaContours(image=image, kept_contour_number=None)

        expected_first_level_contours = [np.array([[[27, 5]], [[27, 91]], [[88, 91]], [[88, 5]]]),
                                         np.array([[[4,  5]], [[4,  91]], [[16, 91]], [[16, 5]]])]

        # when
        actual_first_level_contours = keep_n_largest_area_contours.first_level_contours

        # that
        self.assertEqual(np.array_equal(actual_first_level_contours, expected_first_level_contours), True)

    def test_add_black_edge_working(self):
        # given
        image = cv2.imread("./images/KeepNLargestAreaContours/test_add_black_edge_working__input_image.jpg",
                           cv2.IMREAD_GRAYSCALE)

        expected_black_edged_image = \
            cv2.imread("./images/KeepNLargestAreaContours/test_add_black_edge_working__output_image.png",
                       cv2.IMREAD_GRAYSCALE)

        # when
        actual_black_edged_image = KeepNLargestAreaContours.add_black_edge(image)

        # that
        self.assertEqual(np.array_equal(actual_black_edged_image, expected_black_edged_image), True)

    def test_remove_black_edge_working(self):
        # given
        image = cv2.imread("./images/KeepNLargestAreaContours/test_remove_black_edge_working__input_image.png",
                           cv2.IMREAD_GRAYSCALE)

        expected_removed_black_edge_image = \
            cv2.imread("./images/KeepNLargestAreaContours/test_remove_black_edge_working__output_image.png",
                       cv2.IMREAD_GRAYSCALE)

        # when
        actual_removed_black_edge_image = KeepNLargestAreaContours.remove_black_edge(image)

        # that
        self.assertEqual(np.array_equal(actual_removed_black_edge_image, expected_removed_black_edge_image), True)

if __name__ == '__main__':
    unittest.main()
