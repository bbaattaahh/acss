__author__ = 'Henrik'
import numpy as np
import cv2
from matplotlib import pyplot as plt

from asparagus import define_default_asparagus
from asparagus_sub_image import asparagus_sub_image
from whole_image import whole_image

from find_the_asparagus import find_the_asparagus

from determine_exact__asparagus import get_the_lower_limit_of_white

from calculate_millimeter_value_from_pixel_value import calculate_millimeter_value_from_pixel_value

from classify_the_asparagus import classify_the_asparagus

from print_claasification_result_to_picture import print_classification_result_to_picture

PIXEL_MILLIMETER_RATIO = 110.0/1571.0



def get_max_area_contur(conturs):
    max_area_contur = conturs[0]
    max_area = cv2.contourArea(max_area_contur)


    for contur in conturs:
        area = cv2.contourArea(contur)
        if area > max_area :
            max_area = area
            max_area_contur = contur

    return max_area_contur



img = cv2.imread('images/test_img_1.jpg', 0)
img_col = cv2.imread('images/test_img_1.jpg')


first_asparagus = define_default_asparagus()



first_sub_img = asparagus_sub_image(0, 0, 0, 0)
find_the_asparagus(img, first_sub_img)



my_class = whole_image(img, [], [], 0)

my_class.add_asparagus_subimage(first_sub_img)

my_class.calculate_sub_image(0)



lower_white = np.array([get_the_lower_limit_of_white(my_class.sub_image)])
upper_white = np.array([255])


mask = cv2.inRange(my_class.sub_image, lower_white, upper_white)

kernel = np.ones((2,2),np.uint8)
dilation = cv2.dilate(mask,kernel,iterations = 1)


contours,hierarchy = cv2.findContours(dilation, 1, 2)

max_area_contur = get_max_area_contur(contours)


rect = cv2.minAreaRect(max_area_contur)
box = cv2.cv.BoxPoints(rect)
box = np.int0(box)
cv2.drawContours(my_class.sub_image,[box],0,(0,0,255),10)

x,y,w,h = cv2.boundingRect(max_area_contur)
cv2.rectangle(my_class.sub_image,(x,y),(x+w,y+h),(0, 255, 0),10)


x_range1 = my_class.list_of_asparagus_subimages[0].top_left_corner_x
x_range2 = my_class.list_of_asparagus_subimages[0].top_left_corner_x + my_class.list_of_asparagus_subimages[0].width
y_range1 = my_class.list_of_asparagus_subimages[0].top_left_corner_y
y_range2 = my_class.list_of_asparagus_subimages[0].top_left_corner_y + my_class.list_of_asparagus_subimages[0].hight

img[y_range1:y_range2, x_range1:x_range2] = my_class.sub_image

# cv2.imshow('frame',img)
# plt.imshow(img)


first_asparagus.hight_pixel = rect[1][1]
first_asparagus.width_pixel = rect[1][0]
calculate_millimeter_value_from_pixel_value(PIXEL_MILLIMETER_RATIO, first_asparagus)
classify_the_asparagus(first_asparagus)

my_class.add_asparagus(first_asparagus)

print_classification_result_to_picture(my_class)
plt.imshow(my_class.original_picture)
cv2.imshow('frame',my_class.original_picture)

print 1