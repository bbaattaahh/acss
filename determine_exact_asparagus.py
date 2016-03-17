__author__ = 'Henrik'

import cv2
import numpy as np
from matplotlib import pyplot as plt
from asparagus import define_default_asparagus

from find_the_asparagus import runningMean


def determine_exact_asparagus(my_class):

    first_sub_image = my_class.list_of_asparagus_subimages[0].sub_image

    lower_white = np.array([get_the_lower_limit_of_white(first_sub_image)])
    upper_white = np.array([255])


    mask = cv2.inRange(first_sub_image, lower_white, upper_white)

    kernel = np.ones((2,2),np.uint8)
    dilation = cv2.dilate(mask,kernel,iterations = 1)


    contours,hierarchy = cv2.findContours(dilation, 1, 2)

    max_area_contur = get_max_area_contur(contours)


    rect = cv2.minAreaRect(max_area_contur)
    box = cv2.cv.BoxPoints(rect)
    box = np.int0(box)
    cv2.drawContours(first_sub_image,[box],0,(0,0,255),10)

    x,y,w,h = cv2.boundingRect(max_area_contur)
    cv2.rectangle(first_sub_image,(x,y),(x+w,y+h),(0, 255, 0),10)


    x_range1 = my_class.list_of_asparagus_subimages[0].top_left_corner_x
    x_range2 = my_class.list_of_asparagus_subimages[0].top_left_corner_x + my_class.list_of_asparagus_subimages[0].width
    y_range1 = my_class.list_of_asparagus_subimages[0].top_left_corner_y
    y_range2 = my_class.list_of_asparagus_subimages[0].top_left_corner_y + my_class.list_of_asparagus_subimages[0].hight

    my_class.picture_with_modifications[y_range1:y_range2, x_range1:x_range2] = first_sub_image

    # cv2.imshow('frame',img)
    # plt.imshow(img)

    first_asparagus = define_default_asparagus()
    first_asparagus.hight_pixel = rect[1][1]
    first_asparagus.width_pixel = rect[1][0]

    my_class.add_asparagus(first_asparagus)

    return None



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



def get_max_area_contur(conturs):
    max_area_contur = conturs[0]
    max_area = cv2.contourArea(max_area_contur)


    for contur in conturs:
        area = cv2.contourArea(contur)
        if area > max_area :
            max_area = area
            max_area_contur = contur

    return max_area_contur
