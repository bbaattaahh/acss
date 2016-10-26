__author__ = 'Henrik'

import numpy as np
import cv2
from matplotlib import pyplot as plt

from delete_incorrect_contours import delete_incorrect_contours

from hole_filler import hole_filler

from decide_about_contours_it_could_be_an_asparagus import decide_about_conturs

img1 = cv2.imread('images/pencil_to_find.jpg',0)
img2 = cv2.imread('images/search_the_pencil.jpg')

#img1_gray = cv2.COLOR_BGR2GRAY(img1)

tresholded_gray_img1 = cv2.adaptiveThreshold(img1,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
        cv2.THRESH_BINARY, 55, 2)


#edges = cv2.Canny(img1,90,50)
# erode/dilate
kernel = np.ones((4,4),np.uint8)
eroded_edges = cv2.erode(tresholded_gray_img1, kernel, iterations = 1)

contours, hierarchy = cv2.findContours(eroded_edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

only_appropiate_conturs = delete_incorrect_contours(eroded_edges, contours, 0, 200, 18)

dilated_shapes = cv2.dilate(only_appropiate_conturs, kernel, iterations = 2)

contiguous_shapes = hole_filler(dilated_shapes)

pencil_candidate_contours, hierarchy = cv2.findContours(eroded_edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

pencil_candidate_contours = decide_about_conturs(pencil_candidate_contours, 200, 18)

if pencil_candidate_contours != [] :
    for i in range(0, len(pencil_candidate_contours)):
        rect = cv2.minAreaRect(pencil_candidate_contours[i])
        box = cv2.cv.BoxPoints(rect)
        box = np.int0(box)
        print box

        top_left_x = rect[0][0]
        top_left_y = rect[0][1]
        length = np.int0(rect[1][0])
        width = np.int0(rect[1][1])
        angle = rect[2]

        box = np.float32(box)
        pts2 = np.float32([[0,0],[width,0],[0,length],[width,length]])

        M = cv2.getPerspectiveTransform(box,pts2)
        dst = cv2.warpPerspective(img1, M,(width,length))

        # print cv2.cv.BoxPoints(rect)
        # print top_left_x, top_left_y, width, length, angle
        # M = cv2.getRotationMatrix2D((rect/2,rows/2),90,1)
        #dst = cv2.warpAffine(img,M,(cols,rows))

plt.imshow(dst,'gray')
plt.show()