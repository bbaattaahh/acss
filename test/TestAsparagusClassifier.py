import unittest
import json

from Asparagus import Asparagus
from AsparagusClassifier import AsparagusClassifier


class TestAsparagusClassifier(unittest.TestCase):
    def test_asparagus_classifier_solo_I(self):
        # given
        millimeter_pixel_ratio = 1
        with open("./json_files/test_asparagus_classification_solo_I.json") as json_data:
            classification_specification = json.load(json_data)
        asparagus_classifier = AsparagusClassifier(millimeter_pixel_ratio=millimeter_pixel_ratio,
                                                   classification_specification=classification_specification)

        asparagus = Asparagus(length=225,
                              thickness=25,
                              purple_head=False)

        expected_classification_result = "Solo I"

        # when
        actual_classification_result = asparagus_classifier.classify(asparagus)

        # that
        self.assertEqual(actual_classification_result, expected_classification_result)

    def test_asparagus_classifier_no_head_no_class(self):
        # given
        millimeter_pixel_ratio = 1
        with open("./json_files/test_asparagus_classification_no_head_no_class.json") as json_data:
            classification_specification = json.load(json_data)
        asparagus_classifier = AsparagusClassifier(millimeter_pixel_ratio=millimeter_pixel_ratio,
                                                   classification_specification=classification_specification)

        asparagus = Asparagus(length=225,
                              thickness=25,
                              white_head=False,
                              purple_head=False)

        expected_classification_result = "no class"

        # when
        actual_classification_result = asparagus_classifier.classify(asparagus)

        # that
        self.assertEqual(actual_classification_result, expected_classification_result)

    def test_asparagus_classifier_minimum_condition_open_head(self):
        # given
        millimeter_pixel_ratio = 1
        with open("./json_files/test_asparagus_classification_minimum_condition_open_head.json") as json_data:
            classification_specification = json.load(json_data)
        asparagus_classifier = AsparagusClassifier(millimeter_pixel_ratio=millimeter_pixel_ratio,
                                                   classification_specification=classification_specification)

        asparagus = Asparagus(length=225,
                              thickness=25,
                              open_head=True)

        expected_classification_result = "open head"

        # when
        actual_classification_result = asparagus_classifier.classify(asparagus)

        # that
        self.assertEqual(actual_classification_result, expected_classification_result)

    def test_asparagus_classifier_purple_I(self):
        # given
        millimeter_pixel_ratio = 0.5
        with open("./json_files/test_asparagus_classification_purple_I.json") as json_data:
            classification_specification = json.load(json_data)
        asparagus_classifier = AsparagusClassifier(millimeter_pixel_ratio=millimeter_pixel_ratio,
                                                   classification_specification=classification_specification)

        asparagus = Asparagus(length=450,
                              thickness=50,
                              white_head=True,
                              purple_head=True,
                              open_head=False)

        expected_classification_result = "Purple I"

        # when
        actual_classification_result = asparagus_classifier.classify(asparagus)

        # that
        self.assertEqual(actual_classification_result, expected_classification_result)


if __name__ == '__main__':
    unittest.main()
