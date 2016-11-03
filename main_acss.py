__author__ = 'Henrik'


import ConfigParser
import copy
import datetime

import cv2
from moviepy.editor import *

from calculate_millimeter_value_from_pixel_value import calculate_millimeter_value_from_pixel_value
from classify_the_asparagus import classify_the_asparaguses
from determine_exact_asparagus import determine_exact_asparagus
from display_results import diplay_results
from image_flow import image_flow
from preprocess_input_image import preprocess_input_image
from whole_image import whole_image

config = ConfigParser.RawConfigParser()

config.read('config/config.txt')

TEMPLATE = cv2.imread('images/uj.jpg',0)

PIXEL_MILLIMETER_RATIO = 110.0/1571.0

my_image_folw = image_flow([])

clip = VideoFileClip("videos/live_test_2.avi")
first_image = clip.get_frame("00:00:00")

first_image = preprocess_input_image(first_image)

first_image_gray = cv2.cvtColor(first_image, cv2.COLOR_BGR2GRAY)

first_imgage_to_concatenate = copy.deepcopy(first_image)

filterer_of_background = detect_background(first_image_gray)

i = 0

for x in range(35, 59):

    act_str = '00:00:' + str(x)

    img_col = clip.get_frame(act_str)

    img_col = preprocess_input_image(img_col)

    cv2.imwrite("D:/" + str(x) + ".jpg", img_col)
    # Hecking
    #img_col = cv2.imread("images/test_img_1.jpg")

    img = cv2.cvtColor(img_col, cv2.COLOR_BGR2GRAY)

    # img = my_img
    my_image_folw.add_whole_image(whole_image(img,
                                              original_picture_colourful = img_col,
                                              picture_with_modifications = None,
                                              background_mask = None,
                                              creation_time_original_image = datetime.datetime.now(),
                                              asparaguses = [],
                                              overlap_forward = 0 ,
                                              overlap_backward = 0))


    get_asparagus_sub_images(my_image_folw.whole_images[0], TEMPLATE)

    determine_exact_asparagus(my_image_folw.whole_images[0])

    calculate_millimeter_value_from_pixel_value(PIXEL_MILLIMETER_RATIO, my_image_folw.whole_images[0])

    classify_the_asparaguses(my_image_folw.whole_images[0])

    if i<>0:
        calcualte_overlap2(my_image_folw,
                           config.getint('narrow_image_to_concatonate_them', 'upper_limit'),
                           config.getint('narrow_image_to_concatonate_them', 'lower_limit'))


    i = i + 1

    if i>4:
        delay = config.getfloat('display_results', 'delay_in_sec')
        width_to_display = config.getint('display_results', 'width_of_displayed_image')
        res = diplay_results(my_image_folw, delay, width_to_display)

        cv2.imshow('res',res)
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break

print 1




