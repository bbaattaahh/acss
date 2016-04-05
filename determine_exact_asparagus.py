__author__ = 'Henrik'

# TODO: Log the event when it founds nothing
# TODO: Edge detection closing must to be a little bit cleverer, may be an iterative solution would be the bast...
# TODO: Until we found some thing
# TODO: Handle the case when there is no maxarae contour
    # NOW farmer version : increased the number of the iterations of the edosion and dilatation


import cv2
import numpy as np

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
        dilate = cv2.dilate(edges,kernel,iterations = 4)
        erosion = cv2.erode(dilate,kernel,iterations = 4)


        #cv2.imshow('mask2',mask)
        # cv2.imshow('edges',erosion)
        # cv2.waitKey(0)

        inv_erosion = 255 - erosion

        inv_erosion_with_white_frame= cv2.copyMakeBorder(inv_erosion,2,2,2,2,cv2.BORDER_CONSTANT,value=[255])

        h, w = inv_erosion_with_white_frame.shape[:2]
        mask = np.zeros((h+2, w+2), np.uint8)

        # Floodfill from point (0, 0)
        cv2.floodFill(inv_erosion_with_white_frame, mask, (0,0), 0);


        # cv2.imshow('edges',inv_erosion_with_white_frame)
        # cv2.waitKey(0)

        contours,hierarchy = cv2.findContours(inv_erosion_with_white_frame, 1, 2)

        max_area_contur = get_max_area_contur(contours)
        if max_area_contur is None:
            # cv2.imshow('unfunded asparagus',inv_erosion)
            # cv2.waitKey(0)
            my_class.asparaguses.remove(act_asparagus)
            return None


        rect = cv2.minAreaRect(max_area_contur)

        act_asparagus.width_pixel = rect[1][0]
        act_asparagus.hight_pixel = rect[1][1]

    return None



def get_the_lower_limit_of_white(img):
    # TODO Not nice 15 parameter
    hist = cv2.calcHist([img],[0],None,[256],[0,256])
    moving_avarage_hist_signal = runningMean(hist, 15)


    max_place = moving_avarage_hist_signal.argmax()
    next_min_place = max_place


    while moving_avarage_hist_signal[next_min_place] > moving_avarage_hist_signal[next_min_place - 1]:
        next_min_place = next_min_place - 1


    return next_min_place



def get_max_area_contur(conturs):
    if len(conturs) == 0:
        print "Not found asparagus"
        return None


    max_area_contur = conturs[0]
    max_area = cv2.contourArea(max_area_contur)


    for contur in conturs:
        area = cv2.contourArea(contur)
        if area > max_area :
            max_area = area
            max_area_contur = contur

    return max_area_contur
