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

    def test_image_scale_factors_working(self):
        # given
        image = cv2.imread("./images/DetectBuckets/test_image_scale_factors_working.jpg")
        template_matching_resolution = (240, 320)
        detect_buckets = DetectBuckets(image=image,
                                       bucket_marker_template=None,
                                       bucket_marker_template_original_resolution=None,
                                       template_matching_resolution=template_matching_resolution)

        expected_image_scale_factors = (0.5, 0.5)

        # when
        actual_image_scale_factors = detect_buckets.image_scale_factors

        # that
        self.assertEqual(actual_image_scale_factors, expected_image_scale_factors)

    def test_template_scale_factors_working(self):
        # given
        image = cv2.imread("./images/DetectBuckets/test_template_scale_factors_working__image.jpg")
        bucket_marker_template = cv2.imread("./images/DetectBuckets/"
                                            "test_template_scale_factors_working__bucket_marker_template.jpg")
        bucket_marker_template_original_resolution = (360, 480)
        template_matching_resolution = (240, 320)
        detect_buckets = DetectBuckets(
                       image=image,
                       bucket_marker_template=bucket_marker_template,
                       bucket_marker_template_original_resolution=bucket_marker_template_original_resolution,
                       template_matching_resolution=template_matching_resolution)

        expected_template_scale_factors = (0.6610169491525424, 0.6597938144329897) # ~ 2/3

        # when
        actual_template_scale_factors = detect_buckets.template_scale_factors

        # that
        self.assertEqual(actual_template_scale_factors, expected_template_scale_factors)

    def test_matching_bucket_markers_working(self):
        # given
        image = cv2.imread("./images/RGBTemplateMatching/test_matching_bucket_markers_working__image.jpg")
        bucket_marker_template = cv2.imread(
            "./images/RGBTemplateMatching/test_matching_bucket_markers_working__bucket_marker_template.jpg")
        bucket_marker_template_original_resolution = ()
        template_matching_resolution = ()

        detect_buckets = DetectBuckets(
                       image=image,
                       bucket_marker_template=bucket_marker_template,
                       bucket_marker_template_original_resolution=bucket_marker_template_original_resolution,
                       template_matching_resolution=template_matching_resolution)

        expected_rectangle_top_left_vertices =[[ 729, 845],
                                               [1507, 845]]

        # when
        actual_rectangle_top_left_vertices = rgb_template_matching.rectangle_top_left_vertices

        # that
        self.assertEqual(actual_rectangle_top_left_vertices, expected_rectangle_top_left_vertices)


if __name__ == '__main__':
    unittest.main()
