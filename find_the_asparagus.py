__author__ = 'Henrik'

import cv2
import numpy as np
from matplotlib import pyplot as plt


def find_the_asparagus(img, sub_image):
    my_img = get_asparagus_horizontal_range(img, sub_image)

    final_sp = get_asparagus_vertical_range(my_img, sub_image)

    return final_sp



def get_asparagus_horizontal_range(img, sub_image):
    sum_coloumn_values = sum_coloumn_value(img)
    # TODO 25 comed from my heart... Not too nice
    sum_coloumn_values_smoothed = runningMean(sum_coloumn_values, 25)

    diff_sum_coloumn_values = np.diff(sum_coloumn_values_smoothed)

    stat_index = diff_sum_coloumn_values.argmax()
    end_index = diff_sum_coloumn_values.argmin()

    # TODO This is not an universal constant...
    safety_zone = 30

    sub_image.top_left_corner_x = stat_index-safety_zone
    sub_image.width = (end_index+safety_zone) - (stat_index-safety_zone)

    narrowed_img = img[:, stat_index-safety_zone:end_index+safety_zone]

    return narrowed_img



def get_asparagus_vertical_range(img, sub_image):
    sum_row_values = sum_row_value(img)

    sum_row_values = runningMean(sum_row_values, 25)

    diff_sum_row_values = np.diff(sum_row_values)

    stat_index = diff_sum_row_values.argmax()
    end_index = diff_sum_row_values.argmin()

    # TODO This is not an universal constant...
    safety_zone = 30

    sub_image.top_left_corner_y = stat_index-safety_zone
    sub_image.hight = end_index+safety_zone - (stat_index-safety_zone)
    narrowed_img = img[stat_index-safety_zone:end_index+safety_zone, :]

    return narrowed_img



def runningMean(x, N):
    y = np.zeros((len(x)-N+1,))
    for ctr in range(len(x)-N+1):
         y[ctr] = np.sum(x[ctr:(ctr+N)])
    return y/N


def sum_coloumn_value(img):

    number_of_coloumns = img.shape[1]

    max_sum = np.zeros(number_of_coloumns)

    for x in range(0, number_of_coloumns):
        max_sum[x] = sum(img[:, x])

    return max_sum


def sum_row_value(img):

    number_of_rows = img.shape[0]

    max_sum = np.zeros(number_of_rows)

    for x in range(0, number_of_rows):
        max_sum[x] = sum(img[x, :])

    return max_sum


def get_the_lower_limit_of_white(img):
    # TODO Not nice 15 parameter
    hist = cv2.calcHist([img],[0],None,[256],[0,256])
    moving_avarage_hist_signal = runningMean(hist, 15)

    plt.plot(hist)
    plt.plot(moving_avarage_hist_signal)

    plt.show()

    max_place = moving_avarage_hist_signal.argmax()
    next_min_place = max_place


    while moving_avarage_hist_signal[next_min_place] > moving_avarage_hist_signal[next_min_place - 1]:
        next_min_place = next_min_place - 1


    return next_min_place