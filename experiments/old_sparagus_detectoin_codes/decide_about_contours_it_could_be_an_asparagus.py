__author__ = '502444620'

import cv2

from hard_condition_to_asparagus_shape import is_it_big_enough
from hard_condition_to_asparagus_shape import is_ratio_limit_acceptable
from hard_condition_to_asparagus_shape import ratio_of_bounding_box_sides

def decide_about_conturs(conturs, area_limit, side_ratio_limit):

    for i in range(0, len(conturs)):
        act_cnt = conturs[i]

        if not(dicide_about_one_contour(act_cnt, area_limit, side_ratio_limit)):
            conturs[i] = []


    # delete empty list elements
    if [] in conturs :
        conturs = filter(lambda a: a != [], conturs)


    return conturs


def dicide_about_one_contour(contour, area_limit, side_ratio_limit):

    if not(is_it_big_enough(contour, area_limit)):
        return False

    #check min area rectangle sied ratio
    if not(is_ratio_limit_acceptable(ratio_of_bounding_box_sides, contour, side_ratio_limit)) :
        return False

    return True