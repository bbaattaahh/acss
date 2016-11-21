import unittest
import json

from Asparagus import Asparagus
from AsparagusClassification import AsparagusClassification


class TestAsparagusClassification(unittest.TestCase):
    def test_asparagus_classification_solo_I(self):
        # given
        asparagus = Asparagus(length=225,
                              thickness=25,
                              purple_head=False)
        millimeter_pixel_ratio = 1
        with open("./json_files/test_asparagus_classification_solo_I.json") as json_data:
            classification_specification = json.load(json_data)

        expected_classification_result = "Solo I"

        # when
        asparagus_classification = AsparagusClassification(asparagus=asparagus,
                                                           millimeter_pixel_ratio=millimeter_pixel_ratio,
                                                           classification_specification=classification_specification)

        actual_classification_result = asparagus_classification.classification_result

        # that
        self.assertEqual(actual_classification_result, expected_classification_result)

    def test_asparagus_classification_no_head_no_class(self):
        # given
        asparagus = Asparagus(length=225,
                              thickness=25,
                              head=False,
                              purple_head=False)
        millimeter_pixel_ratio = 1
        with open("./json_files/test_asparagus_classification_no_head_no_class.json") as json_data:
            classification_specification = json.load(json_data)

        expected_classification_result = "no class"

        # when
        asparagus_classification = AsparagusClassification(asparagus=asparagus,
                                                           millimeter_pixel_ratio=millimeter_pixel_ratio,
                                                           classification_specification=classification_specification)

        actual_classification_result = asparagus_classification.classification_result

        # that
        self.assertEqual(actual_classification_result, expected_classification_result)

    def test_asparagus_classification_minimum_condition_open_head(self):
        # given
        asparagus = Asparagus(length=225,
                              thickness=25,
                              open_head=True)
        millimeter_pixel_ratio = 1
        with open("./json_files/test_asparagus_classification_minimum_condition_open_head.json") as json_data:
            classification_specification = json.load(json_data)

        expected_classification_result = "open head"

        # when
        asparagus_classification = AsparagusClassification(asparagus=asparagus,
                                                           millimeter_pixel_ratio=millimeter_pixel_ratio,
                                                           classification_specification=classification_specification)

        actual_classification_result = asparagus_classification.classification_result

        # that
        self.assertEqual(actual_classification_result, expected_classification_result)


if __name__ == '__main__':
    unittest.main()
