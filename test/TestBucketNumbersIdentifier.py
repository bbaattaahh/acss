import unittest
import numpy as np
import cv2

from BucketNumbersIdentifier import BucketNumbersIdentifier


class TestBucketNumbersIdentifier(unittest.TestCase):
    def test_image_150_pixel_height_working(self):
        # given
        image = cv2.imread("./images/BucketNumbersIdentifier/test_image_150_pixel_height_working_input.png",
                           flags=cv2.IMREAD_GRAYSCALE)

        expected_image_150_pixel_height = \
            cv2.imread("./images/BucketNumbersIdentifier/test_image_150_pixel_height_working_output.png",
                       flags=cv2.IMREAD_GRAYSCALE)

        # when
        actual_image_150_pixel_height = BucketNumbersIdentifier.image_150_pixel_height(image)

        # that
        self.assertEqual(np.array_equal(actual_image_150_pixel_height, expected_image_150_pixel_height),
                         True)


    def test_vanish_black_contours_beside_edges_working(self):
        # given
        image = cv2.imread("./images/BucketNumbersIdentifier/test_vanish_black_contours_beside_edges_working_input.png",
                           flags=cv2.IMREAD_GRAYSCALE)

        expected_vanished_black_contours_image = \
            cv2.imread("./images/BucketNumbersIdentifier/test_vanish_black_contours_beside_edges_working_output.png",
                       flags=cv2.IMREAD_GRAYSCALE)

        # when
        actual_vanished_black_contours_image = BucketNumbersIdentifier.vanish_black_contours_beside_edges(image)

        # that
        self.assertEqual(np.array_equal(actual_vanished_black_contours_image, expected_vanished_black_contours_image),
                         True)

    def test_set_img_frame_black_working(self):
        # given
        image = cv2.imread("./images/BucketNumbersIdentifier/test_set_img_frame_black_working_input.png",
                           flags=cv2.IMREAD_GRAYSCALE)

        expected_black_frame_image = \
            cv2.imread("./images/BucketNumbersIdentifier/test_set_img_frame_black_working_output.png",
                       flags=cv2.IMREAD_GRAYSCALE)

        # when
        actual_black_frame_image = BucketNumbersIdentifier.set_img_frame_black(image)

        # that
        self.assertEqual(np.array_equal(actual_black_frame_image, expected_black_frame_image), True)

    def test_flood_fill_with_white_for_top_left_corner_working(self):
        # given
        image = \
            cv2.imread(
                "./images/BucketNumbersIdentifier/test_flood_fill_with_white_for_top_left_corner_working_input.png",
                flags=cv2.IMREAD_GRAYSCALE)

        expected_flood_filled_image = \
            cv2.imread(
                "./images/BucketNumbersIdentifier/test_flood_fill_with_white_for_top_left_corner_working_output.png",
                flags=cv2.IMREAD_GRAYSCALE)

        # when
        actual_flood_filled_image = BucketNumbersIdentifier.flood_fill_with_white_for_top_left_corner(image)

        # that
        self.assertEqual(np.array_equal(actual_flood_filled_image, expected_flood_filled_image), True)

    def test_do_number_recognition_working(self):
        # given
        image = cv2.imread("./images/BucketNumbersIdentifier/test_do_number_recognition_working.png")

        expected_recognized_numbers = "100"

        # when
        actual_recognized_numbers = BucketNumbersIdentifier.do_number_recognition(image=image)

        # that
        self.assertEqual(actual_recognized_numbers, expected_recognized_numbers)

    def test_do_number_recognition_real_sample(self):
        # given
        image = cv2.imread("./images/BucketNumbersIdentifier/test_do_number_recognition_real_sample.jpg")

        expected_recognized_numbers = "001"

        # when
        actual_recognized_numbers = BucketNumbersIdentifier.do_number_recognition(image=image)

        # that
        self.assertEqual(actual_recognized_numbers, expected_recognized_numbers)


if __name__ == '__main__':
    unittest.main()