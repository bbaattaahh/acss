import unittest
import numpy as np
import cv2

from DetectBuckets import DetectBuckets


class TestDetectBuckets(unittest.TestCase):

    def test_image_to_detect_bucket_markers_working(self):
        # given
        image = cv2.imread("./images/DetectBuckets/test_image_to_detect_bucket_markers_working_input.jpg")
        template_matching_resolution = (240, 320)
        detect_buckets = DetectBuckets(image=image,
                                       bucket_marker_template=None,
                                       bucket_marker_template_original_resolution=None,
                                       template_matching_resolution=template_matching_resolution)

        expected_image_to_detect_bucket_markers = \
            cv2.imread("./images/DetectBuckets/test_image_to_detect_bucket_markers_working_output.png")

        # when
        actual_image_to_detect_bucket_markers = detect_buckets.image_to_detect_bucket_markers

        # that
        self.assertEqual(np.array_equal(actual_image_to_detect_bucket_markers, expected_image_to_detect_bucket_markers),
                         True)

    def test_template_to_detect_bucket_markers_working(self):
        # given
        bucket_marker_image = \
            cv2.imread("./images/DetectBuckets/test_template_to_detect_bucket_markers_working_input.jpg")
        template_matching_resolution = (1920/2, 2560/2)
        bucket_marker_template_original_resolution = (1920, 2560)
        detect_buckets = DetectBuckets(
                            image=None,
                            bucket_marker_template=bucket_marker_image,
                            bucket_marker_template_original_resolution=bucket_marker_template_original_resolution,
                            template_matching_resolution=template_matching_resolution)

        expected_template_to_template_matching = cv2.imread(
                                    "./images/DetectBuckets/test_template_to_detect_bucket_markers_working_output.png")

        # when
        actual_template_to_template_matching = detect_buckets.template_to_detect_bucket_markers

        # that
        self.assertEqual(np.array_equal(actual_template_to_template_matching,
                                        expected_template_to_template_matching),
                         True)

if __name__ == '__main__':
    unittest.main()
