__author__ = 'Henrik'

import numpy as np
import cv2
import matplotlib.pyplot as plt


def calculate_overlap(act_whole_image,
                      previous_whole_image,
                      upper_narrow_limit,
                      lower_narrow_limit):

    narrowed_left_image = narrow_horizontally_examined_part(act_whole_image.original_picture_colourful,
                                                            upper_narrow_limit,
                                                            lower_narrow_limit)

    narrowed_right_image = narrow_horizontally_examined_part(previous_whole_image.original_picture_colourful,
                                                             upper_narrow_limit,
                                                             lower_narrow_limit)

    narrowed_left_image = cv2.blur(narrowed_left_image,(10,10))
    narrowed_right_image = cv2.blur(narrowed_right_image,(10,10))

    upper_limit = narrowed_left_image.shape[1]
    res = np.zeros(upper_limit)


    for i in range(1, upper_limit):
        res[i] = abs_normed_difference(narrowed_left_image, narrowed_right_image, i)

    res = res[1:len(res)]

    plt.plot(res)
    plt.show()

    overlap_size = res.argmin()

    cv2.imshow('frame1',act_whole_image.original_picture_colourful)
    cv2.imshow('frame2',previous_whole_image.original_picture_colourful)
    cv2.waitKey(0)


    act_whole_image.overlap_forward = overlap_size
    previous_whole_image.overlap_backward = overlap_size
    print overlap_size

    return  None


def narrow_horizontally_examined_part(image, upper_limit, lower_limit):
    return image[upper_limit:lower_limit, :, :]


def abs_normed_difference(image_left, image_right, overlap):
    left_piece = image_left[:, image_left.shape[1]-overlap:image_left.shape[1], :]
    right_piece = image_right[:, 0:overlap, :]
    abs_difference = sum(sum(sum(cv2.absdiff(right_piece, left_piece))))
    number_of_checked_numbers = left_piece.shape[0] * left_piece.shape[1] * left_piece.shape[2]
    normed_difference = float(abs_difference) / float(number_of_checked_numbers)

    return normed_difference


