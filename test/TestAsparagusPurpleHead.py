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
        cv2.imwrite("./images/AsparagusPurpleHead/test_color_filtered_image_working_output.png",
                    actual_color_filtered_image)

        # that
        self.assertEqual(np.array_equal(actual_color_filtered_image, expected_color_filtered_image), True)


if __name__ == '__main__':
    unittest.main()