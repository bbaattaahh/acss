__author__ = '502444620'


import numpy as np
from merge_binary_layers import merge_binary_layers


def test_merge_binary_layers_preserve_black():
    layer1 = np.array( [[255, 255, 255, 255, 255],
                        [255, 255,   0, 255, 255],
                        [255, 255, 255, 255, 255]], np.uint8)

    layer2 = np.array( [[0,   0,   0,   0,   0],
                        [0, 255, 255, 255,   0],
                        [0,   0,   0,   0,   0]], np.uint8)

    expe_res = np.array( [[0,   0,   0,   0,   0],
                          [0, 255,   0, 255,   0],
                          [0,   0,   0,   0,   0]], np.uint8)

    assert (merge_binary_layers(layer1, layer2, 0, 255) == expe_res).all()


def test_merge_binary_layers_preserve_white():
    layer1 = np.array( [[255, 255, 255, 255, 255],
                        [255, 255,   0,   0, 255],
                        [255, 255, 255, 255, 255]], np.uint8)

    layer2 = np.array( [[0,   0,   0,   0,   0],
                        [0, 255, 255, 255,   0],
                        [0,   0,   0,   0,   0]], np.uint8)

    expe_res = np.array( [[255, 255, 255, 255, 255],
                          [255, 255, 255, 255, 255],
                          [255, 255, 255, 255, 255]], np.uint8)

    assert (merge_binary_layers(layer1, layer2, 255, 0) == expe_res).all()

