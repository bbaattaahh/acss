__author__ = '502444620'

import numpy as np
from set_img_frame import set_img_frame


def test_set_img_frame_to_black_one_frame_wide():
    test_img = np.array( [[255, 255, 255, 255, 255],
                          [255, 255, 255, 255, 255],
                          [255, 255, 255, 255, 255]], np.uint8)

    expe_img = np.array( [[0,   0,   0,   0,   0],
                          [0, 255, 255, 255,   0],
                          [0,   0,   0,   0,   0]], np.uint8)

    assert (set_img_frame(test_img, 0, 1) == expe_img).all()
