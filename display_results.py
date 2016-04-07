__author__ = 'Henrik'

import numpy as np
import datetime

# from print_classification_result_to_picture import print_classification_result_to_picture

def diplay_results(image_flow, delay, width_to_display):

    start_image_index, start_pixel = calculate_starting_pixel(image_flow, delay)

    end_image_index = calculate_ending_pixel(image_flow, start_image_index, start_pixel, width_to_display)

    image_without_text = image_to_display(image_flow, start_image_index, start_pixel, end_image_index)



    #TODO Put the text on it

    return image_without_text


def image_to_display(image_flow, start_image_index, start_pixel, end_image_index):

    width_of_first_image = image_flow.whole_images[start_image_index].original_picture_colourful.shape[1]

    final_image = image_flow.whole_images[start_image_index].original_picture_colourful[:,start_pixel:width_of_first_image,:]

    for act_index in range(start_image_index + 1, end_image_index):
        final_image = concat_images(final_image,
                                    image_flow.whole_images[act_index].original_picture_colourful,
                                    image_flow.whole_images[act_index].overlap_backward)


    return final_image



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


        if (sum_pixel > width_to_display):
            break

    return image_index


def concat_images(image_left, image_right, overlap):
    right_piece = image_right[:, overlap:image_right.shape[1], :]
    concatenated_image = np.hstack((image_left, right_piece))

    return concatenated_image



