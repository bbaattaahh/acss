import unittest
import cv2
import numpy as np

from OneAsparagusAnalysis import OneAsparagusAnalysis
from AsparagusHeadClassifier import AsparagusHeadClassifier
from Asparagus import Asparagus


class TestOneAsparagusAnalysis(unittest.TestCase):
    def test_asparagus_working(self):
        # given
        one_asparagus_image = cv2.imread("./images/OneAsparagusAnalysis/test_asparagus_working_one_asparagus_image.png")

        neural_network_hierarchy_file = "./neural_network_models/dummy_model.json"
        neural_network_weights_file = "./neural_network_models/dummy_model.h5"
        classification_labels = ["purple", "white", "no_head", "rose_head"]
        top_part_to_keep_ratio = 0.15
        head_classification_resolution = (10, 10)
        asparagus_head_classifier = AsparagusHeadClassifier(neural_network_hierarchy_file,
                                                            neural_network_weights_file,
                                                            classification_labels,
                                                            top_part_to_keep_ratio,
                                                            head_classification_resolution)

        one_asparagus_analysis = OneAsparagusAnalysis(one_asparagus_image,
                                                      asparagus_head_classifier)

        expected_asparagus = Asparagus(length=434,
                                       thickness=44,
                                       white_head=False,
                                       no_head=False,
                                       purple_head=True,
                                       open_head=False,
                                       piper=False)

        # when
        actual_asparagus = one_asparagus_analysis.asparagus

        # that
        self.assertEqual(actual_asparagus, expected_asparagus)

    def test_head_label_working(self):
        # given
        one_asparagus_image = cv2.imread("./images/OneAsparagusAnalysis/test_head_label_working.png")

        neural_network_hierarchy_file = "./neural_network_models/dummy_model.json"
        neural_network_weights_file = "./neural_network_models/dummy_model.h5"
        classification_labels = ["purple", "white", "no_head", "rose_head"]
        top_part_to_keep_ratio = 0.15
        head_classification_resolution = (10, 10)
        asparagus_head_classifier = AsparagusHeadClassifier(neural_network_hierarchy_file,
                                                            neural_network_weights_file,
                                                            classification_labels,
                                                            top_part_to_keep_ratio,
                                                            head_classification_resolution)

        one_asparagus_analysis = OneAsparagusAnalysis(one_asparagus_image,
                                                      asparagus_head_classifier)

        expected_head_label = "purple"

        # when
        actual_head_label = one_asparagus_analysis.head_label

        # that
        self.assertEqual(actual_head_label, expected_head_label)

    def test_get_contour_working(self):
        # given
        one_asparagus_image = cv2.imread("./images/OneAsparagusAnalysis/test_get_contour_working_input.jpg")
        asparagus_head_classifier = None
        one_asparagus_analysis = OneAsparagusAnalysis(one_asparagus_image,
                                                      asparagus_head_classifier)

        expected_contour = cv2.imread("./images/OneAsparagusAnalysis/test_get_contour_working_output.png",
                                      cv2.IMREAD_GRAYSCALE)

        # when
        actual_contour = one_asparagus_analysis.asparagus_contour

        # that
        self.assertEqual(np.array_equal(actual_contour, expected_contour), True)

    def test_asparagus_in_smallest_enclosing_box_working(self):
        # given
        one_asparagus_image = cv2.imread(
            "./images/OneAsparagusAnalysis/test_asparagus_in_smallest_enclosing_box_working_input.jpg")
        asparagus_head_classifier = None
        one_asparagus_analysis = OneAsparagusAnalysis(one_asparagus_image,
                                                      asparagus_head_classifier)

        expected_asparagus_in_smallest_enclosing_box = \
            cv2.imread("./images/OneAsparagusAnalysis/test_asparagus_in_smallest_enclosing_box_working_output.png")

        # when
        actual_asparagus_in_smallest_enclosing_box = one_asparagus_analysis.asparagus_in_smallest_enclosing_box

        # that
        self.assertEqual(np.array_equal(actual_asparagus_in_smallest_enclosing_box,
                                        expected_asparagus_in_smallest_enclosing_box),
                         True)

    def test_asparagus_thickness_working(self):
        # given
        one_asparagus_image = cv2.imread("./images/OneAsparagusAnalysis/test_test_asparagus_thickness_working.jpg")
        asparagus_head_classifier = None
        one_asparagus_analysis = OneAsparagusAnalysis(one_asparagus_image,
                                                      asparagus_head_classifier)

        expected_asparagus_thickness = 22

        # when
        actual_asparagus_thickness = one_asparagus_analysis.asparagus_thickness

        # that
        self.assertEqual(actual_asparagus_thickness, expected_asparagus_thickness)

    def test_asparagus_length_working(self):
        # given
        one_asparagus_image = cv2.imread("./images/OneAsparagusAnalysis/test_asparagus_length_working.jpg")
        asparagus_head_classifier = None
        one_asparagus_analysis = OneAsparagusAnalysis(one_asparagus_image,
                                                      asparagus_head_classifier)

        expected_asparagus_length = 431

        # when
        actual_asparagus_length = one_asparagus_analysis.asparagus_length

        # that
        self.assertEqual(actual_asparagus_length, expected_asparagus_length)


if __name__ == '__main__':
    unittest.main()
