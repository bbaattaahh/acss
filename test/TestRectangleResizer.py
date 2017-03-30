import unittest

from Rectangle import Rectangle
from RectangleResizer import RectangleResizer


class TestRectangleResizer(unittest.TestCase):

    def test_resize_working(self):
        # given
        original_resolution = 480, 640
        target_resolution = 720, 1280
        rectangle_resizer = RectangleResizer(original_resolution, target_resolution)

        top_left_x = 10
        top_left_y = 20
        width = 30
        high = 40
        rectangle = Rectangle(top_left_x, top_left_y, width, high)

        expected_resized_rectangle = Rectangle(top_left_x=20, top_left_y=30, width=60, high=60)

        # when
        actual_resized_rectangle = rectangle_resizer.resize(rectangle)

        # that
        self.assertEqual(actual_resized_rectangle, expected_resized_rectangle)

if __name__ == '__main__':
    unittest.main()
