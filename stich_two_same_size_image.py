__author__ = '502444620'

import cv2
import numpy as np

# TFH: 1. High of the pictures are same
#      2. In worst case left is the same size like right, but in the most case the right image is much wider

def abs_normed_difference(image_left, image_right, overlap):
    left_piece = image_left[:, image_left.shape[1]-overlap:image_left.shape[1], :]
    right_piece = image_right[:, 0:overlap, :]
    abs_difference = sum(sum(sum(cv2.absdiff(right_piece, left_piece))))
    number_of_checked_numbers = left_piece.shape[0] * left_piece.shape[1] * left_piece.shape[2]
    normed_difference = float(abs_difference) / float(number_of_checked_numbers)

    return normed_difference


def get_overlap_size(image_left, image_right):
    upper_limit = image_left.shape[1]
    res = np.zeros(upper_limit)
    res[0] = 1.0

    for i in range(1, upper_limit):
        res[i] = abs_normed_difference(image_left, image_right, i)

    overlap_size = res.argmin()

    return  overlap_size


def concat_images(image_left, image_right, overlap):
    right_piece = image_right[:, overlap:image_right.shape[1], :]
    concatenated_image = np.hstack((image_left, right_piece))

    return concatenated_image

