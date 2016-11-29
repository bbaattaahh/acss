import unittest
import numpy as np
import cv2

from DetectBuckets import DetectBuckets


class TestDetectBuckets(unittest.TestCase):
    def test_do_number_recognition_working(self):
        # given
        image = cv2.imread("./images/DetectBuckets/test_do_number_recognition_working.png")

        expected_recognized_numbers = "100"

        # when
        actual_recognized_numbers = DetectBuckets.do_number_recognition(image=image)

        # that
        self.assertEqual(actual_recognized_numbers, expected_recognized_numbers)

    def test_resize_image_working(self):
        # given
        image = cv2.imread("./images/DetectBuckets/test_resize_image_working_input.jpg")
        target_width = 320
        target_height = 240

        expected_resized_image = cv2.imread("./images/DetectBuckets/test_resize_image_working_output.png")

        # when
        actual_resized_image = DetectBuckets.resize_image(image=image,
                                                          target_width=target_width,
                                                          target_height=target_height)

        # that
        self.assertEqual(np.array_equal(actual_resized_image, expected_resized_image), True)


if __name__ == '__main__':
    unittest.main()
