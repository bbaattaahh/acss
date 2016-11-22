import cv2
import unittest
import numpy as np

from NumberImages0To9 import NumberImages0To9


class TestNumberImages0To9(unittest.TestCase):
    def test_number_images_0_to_9_working(self):
        # given
        folder_path = "./images/NumberImages0To9/test_number_images_0_to_9_working_inputs"
        parent_image_resolution = (480, 640)
        number_images_0_to_9 = NumberImages0To9(folder_path=folder_path,
                                                parent_image_resolution=parent_image_resolution)

        number_0 = cv2.imread("./images/NumberImages0To9/test_number_images_0_to_9_working_outputs/0.jpg")
        number_1 = cv2.imread("./images/NumberImages0To9/test_number_images_0_to_9_working_outputs/1.jpg")
        number_2 = cv2.imread("./images/NumberImages0To9/test_number_images_0_to_9_working_outputs/2.jpg")
        number_3 = cv2.imread("./images/NumberImages0To9/test_number_images_0_to_9_working_outputs/3.jpg")
        number_4 = cv2.imread("./images/NumberImages0To9/test_number_images_0_to_9_working_outputs/4.jpg")
        number_5 = cv2.imread("./images/NumberImages0To9/test_number_images_0_to_9_working_outputs/5.jpg")
        number_6 = cv2.imread("./images/NumberImages0To9/test_number_images_0_to_9_working_outputs/6.jpg")
        number_7 = cv2.imread("./images/NumberImages0To9/test_number_images_0_to_9_working_outputs/7.jpg")
        number_8 = cv2.imread("./images/NumberImages0To9/test_number_images_0_to_9_working_outputs/8.jpg")
        number_9 = cv2.imread("./images/NumberImages0To9/test_number_images_0_to_9_working_outputs/9.jpg")

        expected_numbers = [number_0, number_1, number_2, number_3, number_4,
                            number_5, number_6, number_7, number_8, number_9]

        # when
        actual_numbers = number_images_0_to_9.numbers

        # that
        self.assertEqual(np.array_equal(actual_numbers, expected_numbers), True)


if __name__ == '__main__':
    unittest.main()
