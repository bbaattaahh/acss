__author__ = 'Henrik'
import numpy as np
import cv2
from matplotlib import pyplot as plt
from moviepy.editor import *
import numpy as np

from image_flow import image_flow
from whole_image import whole_image

from get_asparagus_sub_images import get_asparagus_sub_images

from detect_background import detect_background

from determine_exact_asparagus import determine_exact_asparagus

from calculate_millimeter_value_from_pixel_value import calculate_millimeter_value_from_pixel_value

from classify_the_asparagus import classify_the_asparagus

from print_claasification_result_to_picture import print_classification_result_to_picture


TEMPLATE = cv2.imread('images/object_to_search_2.jpg',0)

PIXEL_MILLIMETER_RATIO = 110.0/1571.0

my_image_folw = image_flow([])

clip = VideoFileClip("videos/test_2.3gp")
first_image = clip.get_frame("00:00:00")
first_image_gray = cv2.cvtColor(first_image, cv2.COLOR_BGR2GRAY)


filterer_of_background = detect_background(first_image_gray)


for x in range(0, 10):

    act_str = '00:00:' + str(x)

    img_col = clip.get_frame(act_str)

    # Hecking
    img_col = cv2.imread("images/test_img_1.jpg")

    img = cv2.cvtColor(img_col, cv2.COLOR_BGR2GRAY)

    if filterer_of_background.former_image == None:
        filterer_of_background.former_image = img
        continue
    else:
        image_difference = cv2.absdiff(img, filterer_of_background.former_image)
        filterer_of_background.act_image = img
        mask = cv2.inRange(image_difference, 20, 255)
        filterer_of_background.add_mask(mask)

        if len(filterer_of_background.masks) > 4:
            del filterer_of_background.masks[0]


        commulatied_mask = mask

        for act_mask in filterer_of_background.masks:
            commulatied_mask = cv2.bitwise_or(commulatied_mask, act_mask)

        filterer_of_background.actual_mask = commulatied_mask


    # img = my_img

    my_class = whole_image(img)

    my_class.background_mask = filterer_of_background.actual_mask

    get_asparagus_sub_images(my_class, TEMPLATE)

    determine_exact_asparagus(my_class)


    cv2.imshow('frame',my_class.original_picture)
    cv2.waitKey(0)
    #filtered_image = cv2.bitwise_and(img, filterer_of_background.actual_mask)
    #cv2.imshow('filtered',filtered_image)

    my_image_folw.add_whole_image(my_class)

print 1




