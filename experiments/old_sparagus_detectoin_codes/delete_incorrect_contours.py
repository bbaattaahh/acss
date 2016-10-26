__author__ = '502444620'

import cv2

from decide_about_contours_it_could_be_an_asparagus import dicide_about_one_contour



def delete_incorrect_contours(img, contours, delete_colour, area_limit, side_len_ratio_limit):

    for i in range(0, len(contours)):
        act_cnt = contours[i]

        if not(dicide_about_one_contour(act_cnt, area_limit, side_len_ratio_limit)):
            cv2.drawContours(img, [act_cnt], 0, delete_colour, -1)
            # cv2.imshow('steps of delete',img)
            # cv2.imshow('laplacian',laplacian)
            # k = cv2.waitKey(5) & 0xFF
        else :
            print "anyadat"



    return img
