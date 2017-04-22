import unittest
import numpy as np
import cv2

from BucketNumbersIdentifier2 import BucketNumbersIdentifier2


class TestBucketNumbersIdentifier2(unittest.TestCase):
    def test_left_bucket_number_working(self):
        # given
        image = cv2.imread("./images/BucketNumbersIdentifier2/test_left_bucket_number_working.png")
        bucket_number_identifier2 = BucketNumbersIdentifier2("./images/BucketNumbersIdentifier2/numbers")
        expected_left_bucket_number = "006"

        # when
        actual_left_bucket_number = bucket_number_identifier2.left_bucket_number(image)

        # that
        self.assertEqual(actual_left_bucket_number, expected_left_bucket_number)

    def test_right_bucket_number_working(self):
        # given
        image = cv2.imread("./images/BucketNumbersIdentifier2/test_right_bucket_number_working.png")
        numbers_folder = "./images/BucketNumbersIdentifier2/numbers"
        number_matching_resolution = (50, 25)
        max_bucket_number = 110
        bucket_number_identifier = BucketNumbersIdentifier2(numbers_folder,
                                                            number_matching_resolution,
                                                            max_bucket_number)
        expected_right_bucket_number = "002"

        # when
        actual_right_bucket_number = bucket_number_identifier.right_bucket_number(image)

        # that
        self.assertEqual(actual_right_bucket_number, expected_right_bucket_number)

    def test_evaluate_identifications_double_correct_hit(self):
        # given
        numbers_folder = "./images/BucketNumbersIdentifier2/numbers"
        number_matching_resolution = (50, 25)
        max_bucket_number = 110
        bucket_number_identifier = BucketNumbersIdentifier2(numbers_folder,
                                                            number_matching_resolution,
                                                            max_bucket_number)

        identification_1 = "001"
        identification_2 = "001"

        expected_evaluated_identification = "001"

        # when
        actual_evaluated_identification = bucket_number_identifier.evaluate_identifications(identification_1,
                                                                                            identification_2)

        # that
        self.assertEqual(actual_evaluated_identification, expected_evaluated_identification)

    def test_evaluate_identifications_one_correct_hit(self):
        # given
        numbers_folder = "./images/BucketNumbersIdentifier2/numbers"
        number_matching_resolution = (50, 25)
        max_bucket_number = 110
        bucket_number_identifier = BucketNumbersIdentifier2(numbers_folder,
                                                            number_matching_resolution,
                                                            max_bucket_number)

        identification_1 = "01"
        identification_2 = "001"

        expected_evaluated_identification = "001"

        # when
        actual_evaluated_identification = bucket_number_identifier.evaluate_identifications(identification_1,
                                                                                            identification_2)

        # that
        self.assertEqual(actual_evaluated_identification, expected_evaluated_identification)

    def test_evaluate_identifications_contradiction(self):
        # given
        numbers_folder = "./images/BucketNumbersIdentifier2/numbers"
        number_matching_resolution = (50, 25)
        max_bucket_number = 110
        bucket_number_identifier = BucketNumbersIdentifier2(numbers_folder,
                                                            number_matching_resolution,
                                                            max_bucket_number)

        identification_1 = "001"
        identification_2 = "002"

        expected_evaluated_identification = ""

        # when
        actual_evaluated_identification = bucket_number_identifier.evaluate_identifications(identification_1,
                                                                                            identification_2)

        # that
        self.assertEqual(actual_evaluated_identification, expected_evaluated_identification)

    def test_number_identification_working(self):
        # given
        image = cv2.imread("./images/BucketNumbersIdentifier2/test_number_identification_working.jpg")
        bucket_number_identifier2 = BucketNumbersIdentifier2("./images/BucketNumbersIdentifier2/numbers")

        expected_identified_numbers = "002"

        # when
        actual_identified_numbers = bucket_number_identifier2.number_identification(image)

        # that
        self.assertEqual(expected_identified_numbers, actual_identified_numbers)

    def test_process_image_working(self):
        # given
        image = cv2.imread("./images/BucketNumbersIdentifier2/test_process_image_working_input.jpg")

        expected_processed_image = cv2.imread(
                "./images/BucketNumbersIdentifier2/test_process_image_working_output.png",
                flags=cv2.IMREAD_GRAYSCALE)

        # when
        actual_processed_image = BucketNumbersIdentifier2.process_image(image)

        # that
        self.assertEqual(np.array_equal(actual_processed_image, expected_processed_image), True)

    def test_delete_top_and_lower_20_percent_of_image_working(self):
        # given
        image = cv2.imread(
                    "./images/BucketNumbersIdentifier2/test_delete_top_and_lower_20_percent_of_image_working_input.png",
                    flags=cv2.IMREAD_GRAYSCALE)

        expected_narrowed_image = cv2.imread(
                "./images/BucketNumbersIdentifier2/test_delete_top_and_lower_20_percent_of_image_working_output.png",
                flags=cv2.IMREAD_GRAYSCALE)

        # when
        actual_narrowed_image = BucketNumbersIdentifier2.delete_top_and_lower_20_percent_of_image(image)

        # that
        self.assertEqual(np.array_equal(actual_narrowed_image, expected_narrowed_image),
                         True)

    def test_image_150_pixel_height_working(self):
        # given
        image = cv2.imread("./images/BucketNumbersIdentifier2/test_image_150_pixel_height_working_input.png",
                           flags=cv2.IMREAD_GRAYSCALE)

        expected_image_150_pixel_height = \
            cv2.imread("./images/BucketNumbersIdentifier2/test_image_150_pixel_height_working_output.png",
                       flags=cv2.IMREAD_GRAYSCALE)

        # when
        actual_image_150_pixel_height = BucketNumbersIdentifier2.image_150_pixel_height(image)

        # that
        self.assertEqual(np.array_equal(actual_image_150_pixel_height, expected_image_150_pixel_height),
                         True)

    def test_vanish_black_contours_beside_edges_working(self):
        # given
        image = \
            cv2.imread("./images/BucketNumbersIdentifier2/test_vanish_black_contours_beside_edges_working_input.png",
                       flags=cv2.IMREAD_GRAYSCALE)

        expected_vanished_black_contours_image = \
            cv2.imread("./images/BucketNumbersIdentifier2/test_vanish_black_contours_beside_edges_working_output.png",
                       flags=cv2.IMREAD_GRAYSCALE)

        # when
        actual_vanished_black_contours_image = BucketNumbersIdentifier2.vanish_black_contours_beside_edges(image)

        # that
        self.assertEqual(np.array_equal(actual_vanished_black_contours_image, expected_vanished_black_contours_image),
                         True)

    def test_set_img_frame_black_working(self):
        # given
        image = cv2.imread("./images/BucketNumbersIdentifier2/test_set_img_frame_black_working_input.png",
                           flags=cv2.IMREAD_GRAYSCALE)

        expected_black_frame_image = \
            cv2.imread("./images/BucketNumbersIdentifier2/test_set_img_frame_black_working_output.png",
                       flags=cv2.IMREAD_GRAYSCALE)

        # when
        actual_black_frame_image = BucketNumbersIdentifier2.set_img_frame_black(image)

        # that
        self.assertEqual(np.array_equal(actual_black_frame_image, expected_black_frame_image), True)

    def test_flood_fill_with_white_for_top_left_corner_working(self):
        # given
        image = \
            cv2.imread(
                "./images/BucketNumbersIdentifier2/test_flood_fill_with_white_for_top_left_corner_working_input.png",
                flags=cv2.IMREAD_GRAYSCALE)

        expected_flood_filled_image = \
            cv2.imread(
                "./images/BucketNumbersIdentifier2/test_flood_fill_with_white_for_top_left_corner_working_output.png",
                flags=cv2.IMREAD_GRAYSCALE)

        # when
        actual_flood_filled_image = BucketNumbersIdentifier2.flood_fill_with_white_for_top_left_corner(image)

        # that
        self.assertEqual(np.array_equal(actual_flood_filled_image, expected_flood_filled_image), True)

    def test_do_number_recognition_paint_written_0(self):
        # given
        numbers_folder = "./images/BucketNumbersIdentifier2/numbers"
        number_matching_resolution = (50, 25)
        max_bucket_number = 110
        bucket_number_identifier2 = BucketNumbersIdentifier2(numbers_folder,
                                                             number_matching_resolution,
                                                             max_bucket_number)

        number_image = cv2.imread("./images/BucketNumbersIdentifier2/test_do_number_recognition_paint_written_0.png",
                                  flags=cv2.IMREAD_GRAYSCALE)

        expected_recognized_numbers = "0"

        # when
        actual_recognized_numbers = bucket_number_identifier2.do_number_recognition(number_image)

        # that
        self.assertEqual(actual_recognized_numbers, expected_recognized_numbers)

    def test_do_number_recognition_paint_written_2(self):
        # given
        numbers_folder = "./images/BucketNumbersIdentifier2/numbers"
        number_matching_resolution = (50, 25)
        max_bucket_number = 110
        bucket_number_identifier2 = BucketNumbersIdentifier2(numbers_folder,
                                                             number_matching_resolution,
                                                             max_bucket_number)

        number_image = cv2.imread("./images/BucketNumbersIdentifier2/test_do_number_recognition_paint_written_2.jpg",
                                  flags=cv2.IMREAD_GRAYSCALE)

        expected_recognized_numbers = "2"

        # when
        actual_recognized_numbers = bucket_number_identifier2.do_number_recognition(number_image)

        # that
        self.assertEqual(actual_recognized_numbers, expected_recognized_numbers)

    def test_process_number_working(self):
        # given
        number_image = cv2.imread("./images/BucketNumbersIdentifier2/test_process_number_working__number_image.png",
                                  flags=cv2.IMREAD_GRAYSCALE)

        numbers_folder = "./images/BucketNumbersIdentifier2/numbers"
        number_matching_resolution = (50, 25)
        bucket_number_identifier2 = BucketNumbersIdentifier2(numbers_folder,
                                                             number_matching_resolution)

        expected_processed_number_image = \
            cv2.imread("./images/BucketNumbersIdentifier2/test_process_number_working__processed_number_image.png",
                       flags=cv2.IMREAD_GRAYSCALE)

        # when
        actual_processed_number_image = bucket_number_identifier2.process_number(number_image)

        # that
        self.assertEqual(np.array_equal(actual_processed_number_image, expected_processed_number_image), True)

    def test_get_number_templates_working(self):
        # given
        numbers_folder = "./images/BucketNumbersIdentifier2/number_templates_working_input"
        number_matching_resolution = (25, 12)
        bucket_number_identifier2 = BucketNumbersIdentifier2(numbers_folder,
                                                             number_matching_resolution)

        number_0_image = cv2.imread("./images/BucketNumbersIdentifier2/number_templates_working_output/0.png",
                                    flags=cv2.IMREAD_GRAYSCALE)
        number_1_image = cv2.imread("./images/BucketNumbersIdentifier2/number_templates_working_output/1.png",
                                    flags=cv2.IMREAD_GRAYSCALE)
        number_2_image = cv2.imread("./images/BucketNumbersIdentifier2/number_templates_working_output/2.png",
                                    flags=cv2.IMREAD_GRAYSCALE)
        number_3_image = cv2.imread("./images/BucketNumbersIdentifier2/number_templates_working_output/3.png",
                                    flags=cv2.IMREAD_GRAYSCALE)
        number_4_image = cv2.imread("./images/BucketNumbersIdentifier2/number_templates_working_output/4.png",
                                    flags=cv2.IMREAD_GRAYSCALE)
        number_5_image = cv2.imread("./images/BucketNumbersIdentifier2/number_templates_working_output/5.png",
                                    flags=cv2.IMREAD_GRAYSCALE)
        number_6_image = cv2.imread("./images/BucketNumbersIdentifier2/number_templates_working_output/6.png",
                                    flags=cv2.IMREAD_GRAYSCALE)
        number_7_image = cv2.imread("./images/BucketNumbersIdentifier2/number_templates_working_output/7.png",
                                    flags=cv2.IMREAD_GRAYSCALE)
        number_8_image = cv2.imread("./images/BucketNumbersIdentifier2/number_templates_working_output/8.png",
                                    flags=cv2.IMREAD_GRAYSCALE)
        number_9_image = cv2.imread("./images/BucketNumbersIdentifier2/number_templates_working_output/9.png",
                                    flags=cv2.IMREAD_GRAYSCALE)

        expected_number_templates = [number_0_image,
                                     number_1_image,
                                     number_2_image,
                                     number_3_image,
                                     number_4_image,
                                     number_5_image,
                                     number_6_image,
                                     number_7_image,
                                     number_8_image,
                                     number_9_image]

        # when
        actual_number_templates = bucket_number_identifier2.number_templates

        # that
        self.assertEqual(np.array_equal(actual_number_templates, expected_number_templates), True)

    def test_do_number_recognition_working(self):
        # given
        numbers_folder = "./images/BucketNumbersIdentifier2/numbers"
        number_matching_resolution = (50, 25)
        bucket_number_identifier2 = BucketNumbersIdentifier2(numbers_folder,
                                                             number_matching_resolution)

        number_image_to_recognize = \
            cv2.imread("./images/BucketNumbersIdentifier2/test_do_number_recognition_working__image_to_recognize.png",
                       flags=cv2.IMREAD_GRAYSCALE)

        expected_recognized_number = "2"

        # when
        actual_number_templates = bucket_number_identifier2.do_number_recognition(number_image_to_recognize)

        # that
        self.assertEqual(actual_number_templates, expected_recognized_number)

if __name__ == '__main__':
    unittest.main()
