import unittest
import numpy as np
import cv2

from ImageResizer import ImageResizer


class TestImageResizer(unittest.TestCase):
    def test_image_resizer_no_parent_image_resolution(self):
        # given
        image = cv2.imread("./images/ImageResizer/test_image_resizer_no_parent_image_resolution_input.jpg")
        target_resolution = (120, 160)
        image_resizer = ImageResizer(image=image,
                                     target_resolution=target_resolution)

        expected_resized_image = \
            cv2.imread("./images/ImageResizer/test_image_resizer_no_parent_image_resolution_output.png")

        # when
        actual_resized_image = image_resizer.resized_image

        # that
        self.assertEqual(np.array_equal(actual_resized_image, expected_resized_image), True)

    def test_image_resizer_with_parent_image_resolution(self):
        # given
        image = cv2.imread("./images/ImageResizer/test_image_resizer_with_parent_image_resolution_input.jpg")
        target_resolution = (120, 160)
        parent_image_resolution = (240, 320)
        image_resizer = ImageResizer(image=image,
                                     target_resolution=target_resolution,
                                     parent_image_resolution=parent_image_resolution)

        expected_resized_image = \
            cv2.imread("./images/ImageResizer/test_image_resizer_with_parent_image_resolution_output.png")

        # when
        actual_resized_image = image_resizer.resized_image

        # that
        self.assertEqual(np.array_equal(actual_resized_image, expected_resized_image), True)

    def test_new_sizes_working(self):
        # given
        image = cv2.imread("./images/ImageResizer/test_new_sizes_working.png")
        target_resolution = (120, 160)
        parent_image_resolution = (240, 320)
        image_resizer = ImageResizer(image=image,
                                     target_resolution=target_resolution,
                                     parent_image_resolution=parent_image_resolution)

        expected_new_sizes = (93, 92)

        # when
        actual_new_sizes = image_resizer.new_sizes

        # that
        self.assertEqual(actual_new_sizes, expected_new_sizes)


if __name__ == '__main__':
    unittest.main()
