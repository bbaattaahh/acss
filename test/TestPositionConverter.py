import unittest

from PositionConverter import PositionConverter


class TestPositionConverter(unittest.TestCase):
    def test_position_converter_working(self):
        # given
        position_converter = PositionConverter(original_position=(1, 2),
                                               original_resolution=(100, 100),
                                               target_resolution=(300, 200))

        expected_target_position = (2, 6)

        # when
        actual_target_position = position_converter.get_target_position

        # that
        self.assertEqual(actual_target_position, expected_target_position)

    def test_position_converter_three_element_resolution_tuples_input(self):    # modeling shape of RGB images as input
        # given
        original_rgb_image_shape = (100, 100, 3)
        target_rgb_image_shape = (300, 200, 3)
        position_converter = PositionConverter(original_position=(1, 2),
                                               original_resolution=original_rgb_image_shape,
                                               target_resolution=target_rgb_image_shape)

        expected_target_position = (2, 6)

        # when
        actual_target_position = position_converter.get_target_position

        # that
        self.assertEqual(actual_target_position, expected_target_position)
