import unittest

from BucketMarker import BucketMarker
from Rectangle import Rectangle


class TestBucketMarker(unittest.TestCase):

    def test_middle_x_working(self):
        # given
        bounding_rectangle_on_original_image = Rectangle(top_left_x=10, top_left_y=10, width=30, high=300)
        bucket_marker = BucketMarker(marker_image=None,
                                     bounding_rectangle_on_original_image=bounding_rectangle_on_original_image,
                                     right_bucket_number=None,
                                     left_bucket_number=None)

        expected_middle_x = 25

        # when
        actual_middle_x = bucket_marker.middle_x

        # that
        self.assertEqual(actual_middle_x == expected_middle_x, True)

if __name__ == '__main__':
    unittest.main()
