__author__ = '502444620'

import numpy as np


from hard_condition_to_asparagus_shape import ratio_of_bounding_box_sides


def test_ratio_of_bounding_box_sides_working():

    contour = np.array([[[  0,  0]],
                        [[ 10,  0]],
                        [[  0, 10]],
                        [[ 10, 10]]])

    assert ratio_of_bounding_box_sides(contour) == 1