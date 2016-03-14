__author__ = 'Henrik'

import cv2
import numpy as np
from matplotlib import pyplot as plt

from find_the_asparagus import runningMean


def get_the_lower_limit_of_white(img):
    # TODO Not nice 15 parameter
    hist = cv2.calcHist([img],[0],None,[256],[0,256])
    moving_avarage_hist_signal = runningMean(hist, 15)

    # plt.plot(hist)
    # plt.plot(moving_avarage_hist_signal)
    # plt.show()

    max_place = moving_avarage_hist_signal.argmax()
    next_min_place = max_place


    while moving_avarage_hist_signal[next_min_place] > moving_avarage_hist_signal[next_min_place - 1]:
        next_min_place = next_min_place - 1


    return next_min_place
