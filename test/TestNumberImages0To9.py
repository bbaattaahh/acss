import cv2
import unittest

from NumberImages0To9 import NumberImages0To9


class TestNumberImages0To9(unittest.TestCase):
    def test_number_images_0_to_9_working(self):
        # given
        folder_path = "./images/NumberImages0To9/test_number_images_0_to_9_working_inputs"
        parent_image_resolution = (480, 640)
        number_images_0_to_9 = NumberImages0To9(folder_path=folder_path,
                                                parent_image_resolution=parent_image_resolution)

        expected_number_0 = cv2.imread("./images/NumberImages0To9/test_number_images_0_to_9_working_outputs/0.jpg",
                                       flags=cv2.CV_LOAD_IMAGE_GRAYSCALE)
        expected_number_1 = cv2.imread("./images/NumberImages0To9/test_number_images_0_to_9_working_outputs/1.jpg",
                                       flags=cv2.CV_LOAD_IMAGE_GRAYSCALE)
        expected_number_2 = cv2.imread("./images/NumberImages0To9/test_number_images_0_to_9_working_outputs/2.jpg",
                                       flags=cv2.CV_LOAD_IMAGE_GRAYSCALE)
        expected_number_3 = cv2.imread("./images/NumberImages0To9/test_number_images_0_to_9_working_outputs/3.jpg",
                                       flags=cv2.CV_LOAD_IMAGE_GRAYSCALE)
        expected_number_4 = cv2.imread("./images/NumberImages0To9/test_number_images_0_to_9_working_outputs/4.jpg",
                                       flags=cv2.CV_LOAD_IMAGE_GRAYSCALE)

        # when
        actual_number_0 = number_images_0_to_9.number_0
        actual_number_1 = number_images_0_to_9.number_1
        actual_number_2 = number_images_0_to_9.number_2
        actual_number_3 = number_images_0_to_9.number_3
        actual_number_4 = number_images_0_to_9.number_4

        # that
        self.assertEqual((actual_number_0 == expected_number_0).all(), True)
        self.assertEqual((actual_number_1 == expected_number_1).all(), True)
        self.assertEqual((actual_number_2 == expected_number_2).all(), True)
        self.assertEqual((actual_number_3 == expected_number_3).all(), True)
        self.assertEqual((actual_number_4 == expected_number_4).all(), True)


if __name__ == '__main__':
    unittest.main()
