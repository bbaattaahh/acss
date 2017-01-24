import unittest
import cv2
import numpy as np

from AsparagusPurpleHead import AsparagusPurpleHead


class TestAsparagusPurpleHead(unittest.TestCase):
    def test_color_filtered_image_working(self):
        # given
        image = cv2.imread("./images/AsparagusPurpleHead/test_color_filtered_image_working_input.png")
        asparagus_purple_head = AsparagusPurpleHead(image=image)

        expected_color_filtered_image \
            = cv2.imread("./images/AsparagusPurpleHead/test_color_filtered_image_working_output.png")

        # when
        actual_color_filtered_image = asparagus_purple_head.color_filtered_image

        # that
        self.assertEqual(np.array_equal(actual_color_filtered_image, expected_color_filtered_image), True)

    def test_green_layer_working(self):
        # given
        image = cv2.imread("./images/AsparagusPurpleHead/test_green_layer_working_input.png")
        asparagus_purple_head = AsparagusPurpleHead(image=image)

        expected_green_layer \
            = cv2.imread("./images/AsparagusPurpleHead/test_green_layer_working_output.png",
                         cv2.CV_LOAD_IMAGE_GRAYSCALE)

        # when
        actual_green_layer = asparagus_purple_head.green_layer

        # that
        self.assertEqual(np.array_equal(actual_green_layer, expected_green_layer), True)

    def test_asparagus_with_masked_background_working(self):
        # given
        image = cv2.imread("./images/AsparagusPurpleHead/test_asparagus_with_masked_background_working_input.png")
        asparagus_purple_head = AsparagusPurpleHead(image=image)

        expected_asparagus_with_masked_background \
            = cv2.imread("./images/AsparagusPurpleHead/test_asparagus_with_masked_background_working_output.png")

        # when
        actual_asparagus_with_masked_background = asparagus_purple_head.asparagus_with_masked_background

        # that
        self.assertEqual(np.array_equal(actual_asparagus_with_masked_background,
                                        expected_asparagus_with_masked_background),
                         True)

    def test_asparagus_mask_working(self):
        # given
        image = cv2.imread("./images/AsparagusPurpleHead/test_asparagus_mask_working_input.png")
        asparagus_purple_head = AsparagusPurpleHead(image=image)

        expected_asparagus_contour \
            = cv2.imread("./images/AsparagusPurpleHead/test_asparagus_mask_output_working.png",
                         cv2.IMREAD_GRAYSCALE)

        # when
        actual_asparagus_contour = asparagus_purple_head.asparagus_mask
        cv2.imwrite("./images/AsparagusPurpleHead/test_asparagus_mask_output_working.png",
                    actual_asparagus_contour)

        # that
        self.assertEqual(np.array_equal(actual_asparagus_contour, expected_asparagus_contour), True)


if __name__ == '__main__':
    unittest.main()
