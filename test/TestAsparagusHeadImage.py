import unittest
import cv2
import numpy as np

from AsparagusHeadImage import AsparagusHeadImage


class TestAsparagusHeadImage(unittest.TestCase):

    def test_resized_top_part_working(self):
        # given
        image = cv2.imread("./images/AsparagusHeadImage/test_resized_top_part_working_input.jpg")
        top_part_to_keep_ratio = 0.15
        output_resolution = 50, 50
        asparagus_head_image = AsparagusHeadImage(image=image,
                                                  top_part_to_keep_ratio=top_part_to_keep_ratio,
                                                  output_resolution=output_resolution)

        expected_top_part \
            = cv2.imread("./images/AsparagusHeadImage/test_resized_top_part_working_output.png")

        # when
        actual_top_part = asparagus_head_image.resized_top_part

        # that
        self.assertEqual(np.array_equal(actual_top_part, expected_top_part), True)

    def test_top_part_working(self):
        # given
        image = cv2.imread("./images/AsparagusHeadImage/test_top_part_working_input.jpg")
        top_part_to_keep_ratio = 0.15
        asparagus_head_image = AsparagusHeadImage(image=image,
                                                   top_part_to_keep_ratio=top_part_to_keep_ratio,
                                                   output_resolution=None)

        expected_top_part \
            = cv2.imread("./images/AsparagusHeadImage/test_top_part_working_output.png")

        # when
        actual_top_part = asparagus_head_image.top_part
        cv2.imwrite("./images/AsparagusHeadImage/test_top_part_working_output.png", actual_top_part)

        # that
        self.assertEqual(np.array_equal(actual_top_part, expected_top_part), True)


if __name__ == '__main__':
    unittest.main()
