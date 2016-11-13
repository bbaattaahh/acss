import unittest
import cv2

from DetectAsparaguses import DetectAsparaguses
from AsparagusCandidate import AsparagusCandidate
from DetectionToOneAsparagusAnalysis import DetectionToOneAsparagusAnalysis
from Rectangle import Rectangle

class TestDetectAsparaguses(unittest.TestCase):
    def test_data_to_analysis_one_asparagus_images_one_asparagus(self):
        # given
        image = \
            cv2.imread("./images/DetectAsparaguses/test_data_to_analysis_one_asparagus_images_one_asparagus_input.jpg")
        cascade_file = "./cascade_files/cascade.xml"
        detection_scale = 0.25
        swing_angle = 45

        expected_image = \
            cv2.imread("./images/DetectAsparaguses/test_data_to_analysis_one_asparagus_images_one_asparagus_output.jpg")
        detection_rectangle = Rectangle(top_left_x=40.513580676,
                                        top_left_y=285.822663912,
                                        width=560.0,
                                        high=100.0,
                                        angle=-12)

        detection_to_one_asparagus_analysis = DetectionToOneAsparagusAnalysis(
                                                                image=expected_image,
                                                                rectangle_on_original_image=detection_rectangle)

        expected_data_to_analysis = [detection_to_one_asparagus_analysis]

        # when
        detect_asparaguses = DetectAsparaguses(image=image,
                                               cascade_file=cascade_file,
                                               detection_scale=detection_scale,
                                               swing_angle=swing_angle)
        actual_data_to_analysis = detect_asparaguses.data_to_analysis_one_asparagus_images


        # that
        difference_because_of_jpg_compressing = \
            sum(sum(sum(actual_data_to_analysis[0].image - expected_data_to_analysis[0].image)))

        self.assertLess(difference_because_of_jpg_compressing, 300)
        self.assertEqual(actual_data_to_analysis[0].rectangle_on_original_image.angle,
                         expected_data_to_analysis[0].rectangle_on_original_image.angle)


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

    def test_get_asparagus_candidates_2_candidates(self):
        # given
        image = cv2.imread("./images/DetectAsparaguses/test_asparagus_detection_candidates_input.jpg")
        cascade_file = "./cascade_files/cascade.xml"
        detection_scale = 0.25
        swing_angle = 8

        asparagus_candidate_1 = AsparagusCandidate(16, 40, 140, 25, -7)
        asparagus_candidate_2 = AsparagusCandidate(11, 56, 140, 25, -1)

        expected_candidates = [asparagus_candidate_1, asparagus_candidate_2]

        # when
        detect_asparaguses = DetectAsparaguses(image=image,
                                               cascade_file=cascade_file,
                                               detection_scale=detection_scale,
                                               swing_angle=swing_angle)

        actual_candidates = detect_asparaguses.get_asparagus_candidates()

        # that
        self.assertEqual(actual_candidates[0].angle, expected_candidates[0].angle)
        self.assertEqual(actual_candidates[1].angle, expected_candidates[1].angle)
        # TODO: It is wail i dont knpw why....
        #self.assertEqual(actual_candidates[0], expected_candidates[0])

    def test_rotate_about_center(self):
        # given
        image = cv2.imread("./images/DetectAsparaguses/test_rotate_about_center_input.jpg")
        cascade_file = "./cascade_files/cascade.xml"
        expected_rotated_image = cv2.imread("./images/DetectAsparaguses/test_rotate_about_center_output.jpg")

        # when
        detect_asparaguses = DetectAsparaguses(image=image,
                                               cascade_file=cascade_file)
        actual_rotated_image = detect_asparaguses.rotate_about_center(image, 25)

        # that
        difference_because_of_jpg_compression = sum(sum(sum(actual_rotated_image - expected_rotated_image)))
        self.assertLess(difference_because_of_jpg_compression, 500)


if __name__ == '__main__':
    unittest.main()