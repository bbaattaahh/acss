__author__ = '502444620'

import cv2


def is_it_big_enough(contour, limit = 100):

    # Minimum area
    if cv2.contourArea(contour) < limit :
        return False

    return True


def is_ratio_limit_acceptable(ratio_fun, rectangle, limit):
    if ratio_fun(rectangle) < limit :
        return False
    else :
        return True


def ratio_of_bounding_box_sides(contour):
    min_area_bound_rectangle = cv2.minAreaRect(contour)

    longer_side_len = max(min_area_bound_rectangle[1])
    shorter_side_len = min(min_area_bound_rectangle[1])

    ratio = longer_side_len/shorter_side_len

    return ratio
