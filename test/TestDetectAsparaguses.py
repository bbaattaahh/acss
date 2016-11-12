import unittest
import cv2

from DetectAsparaguses import DetectAsparaguses


class TestDetectAsparaguses(unittest.TestCase):
    def test_image_detection_on(self):
        # given
        image = cv2.imread("./images/DetectAsparaguses/test_image_detection_on_input.jpg")
        cascade_file = "./cascade_files/cascade.xml"
        detection_scale = 0.25

        expected_output_image = cv2.imread("./images/DetectAsparaguses/test_image_detection_on_output.jpg",
                                           cv2.CV_LOAD_IMAGE_GRAYSCALE)

        # when
        detect_asparaguses = DetectAsparaguses(image=image,
                                               cascade_file=cascade_file,
                                               detection_scale=detection_scale)

        # that
        difference_because_of_jpg_compression = sum(sum(expected_output_image - detect_asparaguses.image_detection_on))
        self.assertLess(difference_because_of_jpg_compression, 22000)

    def test_asparagus_detection_candidates(self):
        # given
        image = cv2.imread("./images/DetectAsparaguses/test_asparagus_detection_candidates_input.jpg")
        cascade_file = "./cascade_files/cascade.xml"
        detection_scale = 0.25
        swing_angle = 8

        expected_candidates = dict()
        expected_candidates[-8] = [[17, 41, 140, 25], [17, 63, 140, 25]]
        expected_candidates[-7] = [[16, 40, 140, 25], [15, 63, 140, 25]]
        expected_candidates[-6] = [[15, 39, 140, 25], [15, 62, 140, 25]]
        expected_candidates[-5] = [[14, 61, 140, 25]]
        expected_candidates[-4] = [[13, 60, 140, 25]]
        expected_candidates[-3] = [[14, 58, 140, 25]]
        expected_candidates[-2] = [[12, 58, 140, 25]]
        expected_candidates[-1] = [[11, 56, 140, 25]]
        expected_candidates[ 0] = [[ 9, 55, 140, 25]]
        expected_candidates[ 1] = [[11, 56, 140, 25]]
        expected_candidates[ 2] = [[12, 58, 140, 25]]
        expected_candidates[ 3] = [[13, 60, 140, 25]]
        expected_candidates[ 5] = [[15, 63, 140, 25]]
        expected_candidates[ 6] = [[16, 65, 140, 25]]

        # when
        detect_asparaguses = DetectAsparaguses(image=image,
                                               cascade_file=cascade_file,
                                               detection_scale=detection_scale,
                                               swing_angle=swing_angle)

        actual_candidates = detect_asparaguses.asparagus_detection_candidates

        # that
        self.assertEqual(actual_candidates, expected_candidates)

    def test_rotate_about_center(self):
        # given
        image = cv2.imread("./images/DetectAsparaguses/test_rotate_about_center_input.jpg")
        cascade_file = "./cascade_files/cascade.xml"
        expected_rotated_image = cv2.imread("./images/DetectAsparaguses/test_rotate_about_center_output.jpg",
                                            cv2.IMREAD_GRAYSCALE)

        # when
        detect_asparaguses = DetectAsparaguses(image=image,
                                               cascade_file=cascade_file)
        actual_rotated_image = detect_asparaguses.rotate_about_center(25)

        # that
        difference_because_of_jpg_compression = sum(sum(actual_rotated_image - expected_rotated_image))
        self.assertLess(difference_because_of_jpg_compression, 32000)


if __name__ == '__main__':
    unittest.main()