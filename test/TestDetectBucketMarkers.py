import unittest
import numpy as np
import cv2

from DetectBucketMarkers import DetectBucketMarkers


class TestDetectBucketMarkers(unittest.TestCase):

    def test_always_seen_middle_template_working(self):
        # given
        bucket_marker_template = \
            cv2.imread("./images/DetectBucketMarkers/test_always_seen_middle_template_working_input.jpg")
        detect_bucket_markers = DetectBucketMarkers(image=None,
                                                    bucket_marker_template=bucket_marker_template)

        expected_always_seen_middle_template = \
            cv2.imread("./images/DetectBucketMarkers/test_always_seen_middle_template_working_output.png")

        # when
        actual_always_seen_middle_template = detect_bucket_markers.always_seen_middle_template

        # that
        self.assertEqual(np.array_equal(actual_always_seen_middle_template, expected_always_seen_middle_template), True)

