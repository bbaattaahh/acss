__author__ = 'Henrik'

import cv2
import numpy as np

from asparagus import define_default_asparagus
from experiments.find_the_asparagus import runningMean


def determine_exact_asparagus(my_class):

    if my_class.asparaguses == []:
        return None

    for act_asparagus in my_class.asparaguses:
        sub_image = act_asparagus.sub_image

        # TODO levels linear here, instead simple hist equalization
        sub_image = cv2.equalizeHist(sub_image)

        sub_image = cv2.blur(sub_image,(5,5))




        edges = cv2.Canny(sub_image,50,100)
        kernel = np.ones((10,5),np.uint8)
        dilate = cv2.dilate(edges,kernel,iterations = 1)
        erosion = cv2.erode(dilate,kernel,iterations = 1)


        #mask = cv2.inRange(sub_image, lower_white, upper_white)

        #cv2.imshow('mask2',mask)
        cv2.imshow('edges',erosion)
        cv2.waitKey(0)

        inv_erosion = 255 - erosion

        h, w = inv_erosion.shape[:2]
        mask = np.zeros((h+2, w+2), np.uint8)

        # Floodfill from point (0, 0)
        cv2.floodFill(inv_erosion, mask, (0,0), 0);


        cv2.imshow('edges',inv_erosion)
        cv2.waitKey(0)

        contours,hierarchy = cv2.findContours(inv_erosion, 1, 2)

        max_area_contur = get_max_area_contur(contours)

        rect = cv2.minAreaRect(max_area_contur)

        act_asparagus.width_pixel = rect[1][0]
        act_asparagus.hight_pixel = rect[1][1]

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
