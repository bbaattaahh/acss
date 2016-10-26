__author__ = '502444620'

import numpy as np


def set_img_frame(img, colour, num_of_layers):
    x, y = img.shape

    for i in range(0, num_of_layers):
        img[:, i] = colour
        img[:, y-i-1] =colour
        img[i, :] = colour
        img[x-i-1, :] = colour

    return img