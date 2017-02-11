import unittest
import cv2
import numpy as np

from KeepNLargestAreaContours import KeepNLargestAreaContours


class TestKeepOnlyNLargestAreaContours(unittest.TestCase):
    def test_kept_n_largest_area_contours_image__with_invert(self):
        # given
        image = cv2.imread("./images/KeepNLargestAreaContours/"
                           "test_kept_n_largest_area_contours_image__with_invert__input_image.png",
                           cv2.CV_LOAD_IMAGE_GRAYSCALE)
        kept_contour_number = 2
        invert_flag = True
        keep_n_largest_area_contours = KeepNLargestAreaContours(image=image,
                                                                kept_contour_number=kept_contour_number,
                                                                invert_flag=invert_flag)

        expected_image = \
            cv2.imread("./images/KeepNLargestAreaContours/"
                       "test_kept_n_largest_area_contours_image__with_invert__output_image.png",
                       cv2.CV_LOAD_IMAGE_GRAYSCALE)

        # when
        actual_image = keep_n_largest_area_contours.kept_n_largest_area_contours_image

        # that
        self.assertEqual(np.array_equal(actual_image, expected_image), True)

    def test_kept_n_largest_area_contours_image__no_contours(self):
        # given
        image = cv2.imread("./images/KeepNLargestAreaContours/"
                           "test_kept_n_largest_area_contours_image__no_contours__input_image.png",
                           cv2.CV_LOAD_IMAGE_GRAYSCALE)
        kept_contour_number = 2
        keep_n_largest_area_contours = KeepNLargestAreaContours(image=image,
                                                                kept_contour_number=kept_contour_number)

        expected_image = \
            cv2.imread("./images/KeepNLargestAreaContours/"
                       "test_kept_n_largest_area_contours_image__no_contours__output_image.png",
                       cv2.CV_LOAD_IMAGE_GRAYSCALE)

        # when
        actual_image = keep_n_largest_area_contours.kept_n_largest_area_contours_image

        # that
        self.assertEqual(np.array_equal(actual_image, expected_image), True)

    def test_invert_image_working(self):
        # given
        image = cv2.imread("./images/KeepNLargestAreaContours/test_invert_image_working__input_image.png",
                           cv2.CV_LOAD_IMAGE_GRAYSCALE)
        keep_n_largest_area_contours = KeepNLargestAreaContours(image=image,
                                                                kept_contour_number=None)

        expected_inverted_image = \
            cv2.imread("./images/KeepNLargestAreaContours/test_invert_image_working__output_image.png",
                       cv2.CV_LOAD_IMAGE_GRAYSCALE)

        # when
        keep_n_largest_area_contours.invert_image()
        actual_inverted_image = keep_n_largest_area_contours.image

        # that
        self.assertEqual(np.array_equal(actual_inverted_image, expected_inverted_image), True)

    def test_delete_contours_working(self):
        # given
        image = cv2.imread("./images/KeepNLargestAreaContours/test_delete_contours_working__input_image.png",
                           cv2.CV_LOAD_IMAGE_GRAYSCALE)
        kept_contour_number = 2
        keep_n_largest_area_contours = KeepNLargestAreaContours(image=image,
                                                                kept_contour_number=kept_contour_number)

        expected_output_image = \
            cv2.imread("./images/KeepNLargestAreaContours/test_delete_contours_working__output_image.png",
                       cv2.CV_LOAD_IMAGE_GRAYSCALE)

        # when
        keep_n_largest_area_contours.delete_contours()
        actual_output_image = keep_n_largest_area_contours.image

        # that
        self.assertEqual(np.array_equal(actual_output_image, expected_output_image), True)

    def test_contours_to_delete__2_smaller_upper_rectangles(self):
        # given
        image = cv2.imread("./images/KeepNLargestAreaContours/test_contours_to_delete__2_smaller_upper_rectangles.png",
                           cv2.CV_LOAD_IMAGE_GRAYSCALE)
        kept_contour_number = 2
        keep_n_largest_area_contours = KeepNLargestAreaContours(image=image,
                                                                kept_contour_number=kept_contour_number)

        expected_contours_to_delete = [np.array([[[27, 5]], [[27, 17]], [[88, 17]], [[88, 5]]]),
                                       np.array([[[4,  5]], [[4,  16]], [[21, 16]], [[21, 5]]])]

        # when
        actual_contours_to_delete = keep_n_largest_area_contours.contours_to_delete

        # that
        self.assertEqual(np.array_equal(actual_contours_to_delete, expected_contours_to_delete), True)

    def test_contour_areas_working(self):
        # given
        image = cv2.imread("./images/KeepNLargestAreaContours/test_contour_areas_working.png",
                           cv2.CV_LOAD_IMAGE_GRAYSCALE)
        keep_n_largest_area_contours = KeepNLargestAreaContours(image=image, kept_contour_number=None)

        expected_contour_areas = np.array([5246.0, 1032.0])

        # when
        actual_contour_areas = keep_n_largest_area_contours.contour_areas

        # that
        self.assertEqual(np.array_equal(actual_contour_areas, expected_contour_areas), True)

    def test_first_level_contours_working(self):
        # given
        image = cv2.imread("./images/KeepNLargestAreaContours/test_first_level_contours_working.png",
                           cv2.CV_LOAD_IMAGE_GRAYSCALE)
        keep_n_largest_area_contours = KeepNLargestAreaContours(image=image, kept_contour_number=None)

        expected_first_level_contours = [np.array([[[27, 5]], [[27, 91]], [[88, 91]], [[88, 5]]]),
                                         np.array([[[4,  5]], [[4,  91]], [[16, 91]], [[16, 5]]])]

        # when
        actual_first_level_contours = keep_n_largest_area_contours.first_level_contours

        # that
        self.assertEqual(np.array_equal(actual_first_level_contours, expected_first_level_contours), True)

if __name__ == '__main__':
    unittest.main()
