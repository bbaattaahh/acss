import unittest
import cv2
import numpy as np

from DetectBuckets import DetectBuckets
from NumberImages0To9 import NumberImages0To9


class TestDetectBuckets(unittest.TestCase):
    def test_prepare_images_working(self):
        # given
        folder_path = "./images/DetectBuckets/number_images_0_to_9"
        parent_image_resolution = (397, 556)
        number_images_0_to_9 = NumberImages0To9(folder_path=folder_path,
                                                parent_image_resolution=parent_image_resolution)

        image = cv2.imread("./images/DetectBuckets/test_prepare_images_working_input.jpg")
        detect_buckets = DetectBuckets(image=image,
                                       number_images_0_to_9=number_images_0_to_9)

        expected_prepared_image = cv2.imread("./images/DetectBuckets/test_prepare_images_working_output.jpg",
                                             flags=cv2.CV_LOAD_IMAGE_GRAYSCALE)

        # when
        actual_prepared_image = detect_buckets.prepare_image()

        # that
        pixel_difference_because_of_jpg_distortion = sum(sum(actual_prepared_image-expected_prepared_image))
        self.assertLess(pixel_difference_because_of_jpg_distortion, 55000)


if __name__ == '__main__':
    unittest.main()
