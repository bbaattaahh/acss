import unittest
import numpy as np
import cv2

from DetectBuckets import DetectBuckets


class TestDetectBuckets(unittest.TestCase):
    def test_get_bucket_marker_image_center_working(self):
        # given
        image = None
        bucket_marker_image = cv2.imread(
            "./images/DetectBuckets/test_get_bucket_marker_image_center_working__input_bucket_marker.jpg")
        bucket_marker_dimensions_in_millimeter = None
        pixel_millimeter_ratio = None
        detect_buckets = DetectBuckets(image=image,
                                       bucket_marker_image=bucket_marker_image,
                                       bucket_marker_dimensions_in_millimeter=bucket_marker_dimensions_in_millimeter,
                                       pixel_millimeter_ratio=pixel_millimeter_ratio)

        expected_bucket_marker_image_center = cv2.imread(
            "./images/DetectBuckets/test_prepare_images_working_output.png")

        # when
        actual_prepared_image = detect_buckets.get_bucket_marker_image_center()
        cv2.imwrite("nos.jpg", actual_prepared_image)

        # that
        self.assertEqual(np.array_equal(expected_bucket_marker_image_center))


if __name__ == '__main__':
    unittest.main()
