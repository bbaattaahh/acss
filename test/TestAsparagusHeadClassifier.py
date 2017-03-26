import unittest
import cv2
import numpy as np

from AsparagusHeadClassifier import AsparagusHeadClassifier


class TestAsparagusHeadClassifier(unittest.TestCase):
    def test_predict_working(self):
        # given
        neural_network_hierarchy_file = "./neural_network_models/dummy_model.json"
        neural_network_weights_file = "./neural_network_models/dummy_model.h5"
        classification_labels = ["class1", "class2"]
        top_part_to_keep_ratio = 0.15
        head_classification_resolution = (10, 10)
        asparagus_head_classifier = AsparagusHeadClassifier(neural_network_hierarchy_file,
                                                            neural_network_weights_file,
                                                            classification_labels,
                                                            top_part_to_keep_ratio,
                                                            head_classification_resolution)

        image = cv2.imread("./images/AsparagusHeadClassifier/test_predict_working_input.png")

        expected_label = "class1"

        # when
        actual_label = asparagus_head_classifier.predict(image)

        # that
        self.assertEqual(actual_label, expected_label)

    def test_process_image_working(self):
        # given
        image = np.array([[[0, 0, 0], [0, 0, 255]]])

        expected_processed_image = np.array([[[0., 0., 0.], [0., 0., 1.]]])

        # when
        actual_processed_image = AsparagusHeadClassifier.process_image(image)

        # that
        self.assertEqual(np.array_equal(actual_processed_image, expected_processed_image), True)


if __name__ == '__main__':
    unittest.main()
