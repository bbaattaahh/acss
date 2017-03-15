import unittest
import numpy as np
import cv2

from DisplayClassification import DisplayClassification


class TestDisplayClassification(unittest.TestCase):
    def test_actual_image_working(self):
        # given
        image_size = 480, 640
        display_classification = DisplayClassification(image_size)
        display_classification.add_new_result(bucket_number=1, classification_result="Solo I")
        display_classification.add_new_result(bucket_number=2, classification_result="Solo II")
        display_classification.add_new_result(bucket_number=3, classification_result="ACSS")

        expected_actual_image = \
            cv2.imread("./images/DisplayClassification/test_actual_image_working_output.png")

        # when
        actual_actual_image = display_classification.actual_image
        cv2.imwrite("./images/DisplayClassification/test_actual_image_working_output.png", actual_actual_image)

        # that
        self.assertEqual(np.array_equal(actual_actual_image, expected_actual_image), True)

    def test_delete_old_results_which_cannot_be_displayed(self):
        # given
        image_size = 120, 640
        display_classification = DisplayClassification(image_size)
        display_classification.add_new_result(bucket_number=1, classification_result="Solo I")
        display_classification.add_new_result(bucket_number=2, classification_result="Solo II")
        display_classification.add_new_result(bucket_number=3, classification_result="Lila I")
        display_classification.add_new_result(bucket_number=4, classification_result="Lila II")
        display_classification.add_new_result(bucket_number=5, classification_result="Leves")

        expected_results = ["5 : Leves", "4 : Lila II", "3 : Lila I", "2 : Solo II"]

        # when
        actual_results = display_classification.results

        # that
        self.assertEqual(np.array_equal(actual_results, expected_results), True)

if __name__ == '__main__':
    unittest.main()
