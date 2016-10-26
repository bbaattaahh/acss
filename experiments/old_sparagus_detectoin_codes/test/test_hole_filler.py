__author__ = '502444620'

import numpy as np
from hole_filler import hole_filler


def test_hole_filler_working():
    #one white pixel in the middle
    test_img = np.array( [[0,   0,   0,   0, 0],
                          [0, 255, 255, 255, 0],
                          [0, 255,   0, 255, 0],
                          [0, 255, 255, 255, 0],
                          [0,   0,   0,   0, 0]], np.uint8)

    expe_img = np.array( [[0,   0,   0,   0, 0],
                          [0, 255, 255, 255, 0],
                          [0, 255, 255, 255, 0],
                          [0, 255, 255, 255, 0],
                          [0,   0,   0,   0, 0]], np.uint8)

    assert (hole_filler(test_img) == expe_img).all()


def test_hole_filler_shape_at_the_edge():
    #one white pixel in the middle
    test_img = np.array( [[0,   0,   0,   0, 0],
                          [0, 255, 255, 255, 0],
                          [0, 255,   0, 255, 0],
                          [0, 255, 255, 255, 0],
                          [0, 255, 255, 255, 0]], np.uint8)

    expe_img = np.array( [[0,   0,   0,   0, 0],
                          [0, 255, 255, 255, 0],
                          [0, 255, 255, 255, 0],
                          [0, 255, 255, 255, 0],
                          [0, 255, 255, 255, 0]], np.uint8)

    assert (hole_filler(test_img) == expe_img).all()
