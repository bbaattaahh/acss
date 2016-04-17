__author__ = 'Henrik'

import numpy as np
import datetime

from print_claasification_result_to_picture import print_classification_result_to_picture

def diplay_results(image_flow, delay, width_to_display):

    start_image_index, start_pixel = calculate_starting_pixel(image_flow, delay)

    end_image_index = calculate_ending_pixel(image_flow, start_image_index, start_pixel, width_to_display)

    image_without_text = image_to_display(image_flow,
                                          start_image_index,
                                          start_pixel,
                                          end_image_index,
                                          width_to_display)


    image_with_text = print_classification_result_to_picture(image_flow,
                                                             start_image_index,
                                                             start_pixel,
                                                             end_image_index,
                                                             width_to_display,
                                                             image_without_text)


    return image_with_text


def image_to_display(image_flow, start_image_index, start_pixel, end_image_index, expected_width):

    width_of_first_image = image_flow.whole_images[start_image_index].original_picture_colourful.shape[1]

    final_image = image_flow.whole_images[start_image_index].original_picture_colourful[:,start_pixel:width_of_first_image,:]

    for act_index in range(start_image_index + 1, end_image_index):
        final_image = concat_images(final_image,
                                    image_flow.whole_images[act_index].original_picture_colourful,
                                    image_flow.whole_images[act_index].overlap_backward)


    cut_to_size_final_image = cut_to_width_size_image(final_image, expected_width)

    return cut_to_size_final_image

def cut_to_width_size_image(image, expected_width):
    if image.shape[1] <= expected_width:
        return image

    expected_width_image = image[:,0:expected_width,:]

    return expected_width_image

def calculate_starting_pixel(image_flow, delay):

    now = datetime.datetime.now()

    time_diffs = get_time_differences(image_flow, now)

    for i in range(0, len(time_diffs)):
        if delay < time_diffs[i]:
            break

    if i <> 0:
        i = i - 1

    y1 = 0
    y2 = image_flow.whole_images[i].original_picture_colourful.shape[1] - image_flow.whole_images[i].overlap_forward

    x1 = time_diffs[i]
    x2 = time_diffs[i + 1]
    x = delay

    y = (y2-y1)*(x-x1)/(x2-x1)+y1

    if y < 0:
        y = 0

    return (i, y)



def get_time_differences(image_flow, now):

    whole_image_number = len(image_flow.whole_images)
    time_diffs = np.zeros(whole_image_number)

    for i in range(0, len(image_flow.whole_images)):
        time_diff = now - image_flow.whole_images[i].creation_time_original_image
        time_diffs[i] = time_diff.total_seconds()

    return time_diffs



def calculate_ending_pixel(image_flow, start_image_index, start_pixel, width_to_display):

    sum_pixel = image_flow.whole_images[start_image_index].original_picture_colourful.shape[1] - \
                image_flow.whole_images[start_image_index].overlap_forward - \
                start_pixel


    image_index = start_image_index


    while True:
        image_index = image_index + 1
        sum_pixel = sum_pixel + \
                    image_flow.whole_images[image_index].original_picture_colourful.shape[1] - \
                    image_flow.whole_images[image_index].overlap_forward


        if sum_pixel > width_to_display or image_index == len(image_flow.whole_images)-1:
            break

    return image_index


def concat_images(image_left, image_right, overlap):
    left_piece = image_left[:, 0:image_left.shape[1]-overlap, :]
    concatenated_image = np.hstack((left_piece, image_right))

    return concatenated_image



