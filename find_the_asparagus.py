__author__ = 'Henrik'

import numpy as np
from matplotlib import pyplot as plt


def find_the_asparagus(img):

    my_img = get_asparagus_horizontal_range(img)

    final_sp = get_asparagus_vertical_range(my_img)

    plt.imshow(final_sp)

    return final_sp



def get_asparagus_horizontal_range(img):
    sum_coloumn_values = sum_coloumn_value(img)
    # TODO 25 comed from my heart... Not too nice
    sum_coloumn_values_smoothed = runningMean(sum_coloumn_values, 25)

    diff_sum_coloumn_values = np.diff(sum_coloumn_values_smoothed)

    first_and_last_point = get_first_and_last_index_of_the_signal_which_out_the_given_variance(diff_sum_coloumn_values)

    # TODO This is not an universal constant...
    safety_zone = 30

    narrowed_img = img[:, first_and_last_point[0]-safety_zone:first_and_last_point[1]+safety_zone]

    return narrowed_img


def get_first_and_last_index_of_the_signal_which_out_the_given_variance(signal):
    mean = np.mean(signal)
    varaiance = np.std(signal)

    # TODO This 6 is not too nice... Later have to make it clever
    limit = mean - 3 * varaiance

    appropiate_indexes = np.where( signal < limit )
    first_index = appropiate_indexes[0][0]
    last_index = appropiate_indexes[0][-1]

    return((first_index, last_index))


def get_asparagus_vertical_range(img):
    sum_row_values = sum_row_value(img)

    sum_row_values = runningMean(sum_row_values, 25)

    diff_sum_row_values = np.diff(sum_row_values)

    stat_index = diff_sum_row_values.argmax()
    end_index = diff_sum_row_values.argmin()

    # TODO This is not an universal constant...
    safety_zone = 30

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