import unittest
import numpy as np

from MergeBucketsAndAsparagusesPositions import MergeBucketsAndAsparagusPositions
from Rectangle import Rectangle
from Bucket import Bucket


class TestMergeBucketsAndAsparagusesPositions(unittest.TestCase):
    def test_bucket_asparagus_pairs_working(self):
        # given
        bucket1 = Bucket(start=0, end=100, bucket_number="001")
        bucket2 = Bucket(start=100, end=200, bucket_number="002")
        bucket3 = Bucket(start=200, end=300, bucket_number="003")
        bucket4 = Bucket(start=300, end=400, bucket_number="004")
        buckets = [bucket1, bucket2, bucket3, bucket4]

        one_asparagus_image_rectangle_1 = Rectangle(top_left_x=10, top_left_y=20, width=6, high=40, angle=0)
        one_asparagus_image_rectangle_2 = Rectangle(top_left_x=110, top_left_y=20, width=6, high=40, angle=0)
        one_asparagus_image_rectangles = [one_asparagus_image_rectangle_1, one_asparagus_image_rectangle_2]

        asparagus_classes = ["Solo I", "Solo II"]

        marge_buckets_and_asparaguses_posotions = MergeBucketsAndAsparagusPositions(buckets,
                                                                                    one_asparagus_image_rectangles,
                                                                                    asparagus_classes)
        expected_bucket_asparagus_pairs = [["001", "Solo I"],["002", "Solo II"]]

        # when
        actual_bucket_asparagus_pairs = marge_buckets_and_asparaguses_posotions.bucket_asparagus_pairs

        # that
        self.assertEqual(actual_bucket_asparagus_pairs, expected_bucket_asparagus_pairs)

    def test_asparagus_image_middles_working(self):
        # given
        one_asparagus_image_rectangle_1 = Rectangle(top_left_x=10, top_left_y=20, width=6, high=40, angle=0)
        one_asparagus_image_rectangle_2 = Rectangle(top_left_x=110, top_left_y=20, width=6, high=40, angle=0)
        one_asparagus_image_rectangles = [one_asparagus_image_rectangle_1, one_asparagus_image_rectangle_2]

        merge_buckets_and_asparaguses_positions = MergeBucketsAndAsparagusPositions(
                                                        buckets=None,
                                                        one_asparagus_image_rectangles=one_asparagus_image_rectangles,
                                                        asparagus_classes=None)

        expected_asparagus_image_middles = [13, 113]

        # when
        actual_asparagus_image_middles = merge_buckets_and_asparaguses_positions.asparagus_image_middles

        # that
        self.assertEqual(actual_asparagus_image_middles, expected_asparagus_image_middles)

    def test_horizontal_middle_of_oblique_rectangle_anagel_0(self):
        # given
        rectangle = Rectangle(top_left_x=10,
                              top_left_y=20,
                              width=6,
                              high=40,
                              angle=0)

        expected_horizontal_middle_of_oblique_rectangle = 13

        # when
        actual_horizontal_middle_of_oblique_rectangle = \
            MergeBucketsAndAsparagusPositions.horizontal_middle_of_oblique_rectangle(rectangle)

        # that
        self.assertEqual(actual_horizontal_middle_of_oblique_rectangle, expected_horizontal_middle_of_oblique_rectangle)

    def test_horizontal_middle_of_oblique_rectangle_anagel_45(self):
        # given
        rectangle = Rectangle(top_left_x=10,
                              top_left_y=20,
                              width=np.sqrt(2)*6,
                              high=np.sqrt(2)*10,
                              angle=45)

        expected_horizontal_middle_of_oblique_rectangle = 8

        # when
        actual_horizontal_middle_of_oblique_rectangle = \
            MergeBucketsAndAsparagusPositions.horizontal_middle_of_oblique_rectangle(rectangle)

        # that
        self.assertEqual(actual_horizontal_middle_of_oblique_rectangle, expected_horizontal_middle_of_oblique_rectangle)



if __name__ == '__main__':
    unittest.main()
