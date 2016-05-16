import cv2
from whole_image import whole_image
from asparagus import asparagus
import numpy as np

def get_asparagus_sub_images(my_whole_image, template):


    methode = cv2.TM_SQDIFF_NORMED

    res = cv2.matchTemplate(my_whole_image.original_picture,template,methode)
    #min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    mask_res = cv2.inRange(res, 0, 0.1)

    cv2.imshow("res", res)
    cv2.imshow("mask_res", mask_res)
    cv2.waitKey(0)

    conturs_result = cv2.findContours(mask_res,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)


    conturs = conturs_result[0]

    SAFETY_ZONE = 40

    for contur in conturs:
        x,y,w,h = cv2.boundingRect(contur)

        if check_contour_touch_image_edge(x,y,w,h,res):
            continue


        x_upper_range = x + w + template.shape[1] + SAFETY_ZONE
        y_upper_range = y + h + template.shape[0] + SAFETY_ZONE
        x = x
        y = y

        temp_asparagus = asparagus()
        temp_asparagus.top_left_corner_x = x
        temp_asparagus.top_left_corner_y = y

        temp_asparagus.sub_image = my_whole_image.original_picture[y:y_upper_range, x:x_upper_range]
        my_whole_image.add_asparagus(temp_asparagus)
        # cv2.imshow("sub_image", temp_asparagus.sub_image)
        # cv2.waitKey(0)

    return None


def check_contour_touch_image_edge(x,y,w,h,res):
    if x == 0:
        return True

    if y == 0:
        return True

    if x + w >= res.shape[1]:
        return True

    if y + h >= res.shape[0]:
        return True

    return False

# im = cv2.imread("images/test_img_9.jpg", cv2.IMREAD_GRAYSCALE)
# test_whole_image = whole_image(im)
# template = cv2.imread('images/object_to_search_1.jpg',0)

# get_asparagus_sub_images(test_whole_image, template)



# print 1