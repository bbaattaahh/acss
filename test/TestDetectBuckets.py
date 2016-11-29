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
        template_matching_resolution = (240, 320)
        detect_buckets = DetectBuckets(image=image,
                                       bucket_marker_template=None,
                                       bucket_marker_template_original_resolution=None,
                                       template_matching_resolution=template_matching_resolution)

        expected_resized_image = cv2.imread("./images/DetectBuckets/test_resize_image_working_output.png")

        # when
        actual_resized_image = detect_buckets.resized_image

        # that
        self.assertEqual(np.array_equal(actual_resized_image, expected_resized_image), True)

    def test_resized_bucket_marker_template_working(self):
        # given
        bucket_marker_image = cv2.imread("./images/DetectBuckets/test_resized_bucket_marker_template_working_input.jpg")
        template_matching_resolution = (1920/2, 2560/2)
        bucket_marker_template_original_resolution = (1920, 2560)
        detect_buckets = DetectBuckets(image=None,
                                       bucket_marker_template=bucket_marker_image,
                                       bucket_marker_template_original_resolution=
                                                                bucket_marker_template_original_resolution,
                                       template_matching_resolution=template_matching_resolution)

        expected_resized_bucket_marker_template = cv2.imread(
                                    "./images/DetectBuckets/test_resized_bucket_marker_template_working_output.png")

        # when
        actual_resized_bucket_marker_template = detect_buckets.resized_bucket_marker_template

        # that
        self.assertEqual(np.array_equal(actual_resized_bucket_marker_template,
                                        expected_resized_bucket_marker_template),
                         True)


if __name__ == '__main__':
    unittest.main()
