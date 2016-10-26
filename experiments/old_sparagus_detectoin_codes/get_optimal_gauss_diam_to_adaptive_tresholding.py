__author__ = '502444620'

import cv2
import numpy as np

from decide_about_contours_it_could_be_an_asparagus import decide_about_conturs
from delete_incorrect_contours import delete_incorrect_contours
from hole_filler import hole_filler


def get_optimal_gauss_diam_to_adaptive_threasholdong(img_input):

    max_area = 0
    gauss_diameter_to_max_area = 0

    for i in range(11, 401, 2):
        img = cv2.GaussianBlur(img_input,(3,3),0)
        mask = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY, i, 1)
        mask = np.invert(mask)


        # erode
        kernel = np.ones((3,3),np.uint8)
        mask = cv2.erode(mask, kernel, iterations = 1)

        mask = hole_filler(mask)

        copy_of_mask = mask.copy()

        contours, hierarchy = cv2.findContours(copy_of_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        contours = decide_about_conturs(contours, 500, 10)

        sum_area = 0

        if len(contours) <> 0 :
            for j in range(0, len(contours)):
                act_area = cv2.contourArea(contours[j])
                sum_area = sum_area + act_area

        if sum_area > max_area :
            max_area = sum_area
            gauss_diameter_to_max_area = i


    return gauss_diameter_to_max_area


# for i in range(11, 401, 2):
#     img = cv2.imread("g.jpg", 0)
#     img = cv2.GaussianBlur(img,(3,3),0)
#     mask = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY, i, 1)
#     mask = np.invert(mask)
#
#
#
#     # erode
#     kernel = np.ones((3,3),np.uint8)
#     mask = cv2.erode(mask, kernel, iterations = 1)
#
#     copy_of_mask = mask.copy()
#
#     contours, hierarchy = cv2.findContours(copy_of_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#
#     mask = delete_incorrect_contours(mask, contours, 0, 500, 10)
#     mask = hole_filler(mask)
#
#     cv2.imshow('res',mask)
#     #cv2.imshow('laplacian',laplacian)
#     k = cv2.waitKey(5) & 0xFF
#     if k == 27:
#         break
#
#     contours = decide_about_conturs(contours, 500, 10)
#     if len(contours) == 0 :
#         d = 2
#     else :
#         area = cv2.contourArea(contours[0])
#         print i
#         print area
#
#
# cv2.destroyAllWindows()

img = cv2.imread("g.jpg", 0)

a = get_optimal_gauss_diam_to_adaptive_threasholdong(img)

print a