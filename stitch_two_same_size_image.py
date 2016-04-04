__author__ = '502444620'

import cv2
import numpy as np

# TFH: 1. High of the pictures are same
#      2. In worst case left is the same size like right, but in the most case the right image is much wider

def stitch_two_image(image_left, image_right, upper_narrow_limit, lower_narrow_limit):
    overlap_size = get_overlap_size(image_left, image_right, upper_narrow_limit, lower_narrow_limit)

    stitched_image = concat_images(image_left, image_right, overlap_size)

    return stitched_image


def concat_images(image_left, image_right, overlap):
    right_piece = image_right[:, overlap:image_right.shape[1], :]
    concatenated_image = np.hstack((image_left, right_piece))

    return concatenated_image


