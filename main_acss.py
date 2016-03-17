__author__ = 'Henrik'
import numpy as np
import cv2
from matplotlib import pyplot as plt

from asparagus_sub_image import asparagus_sub_image
from whole_image import whole_image

from find_the_asparagus import find_the_asparagus

from determine_exact_asparagus import determine_exact_asparagus

from calculate_millimeter_value_from_pixel_value import calculate_millimeter_value_from_pixel_value

from classify_the_asparagus import classify_the_asparagus

from print_claasification_result_to_picture import print_classification_result_to_picture


# cap = cv2.VideoCapture(0)
# _, frame = cap.read()
# _, frame = cap.read()
# my_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#
# cv2.imshow('frame',my_img)


PIXEL_MILLIMETER_RATIO = 110.0/1571.0

img = cv2.imread('images/my_test.jpg', 0)
img_col = cv2.imread('images/my_test.jpg')

# img = my_img

my_class = whole_image(img, img, [], [])


first_sub_img = asparagus_sub_image([] ,0, 0, 0, 0)
first_sub_img.sub_image = find_the_asparagus(img, first_sub_img)



my_class.add_asparagus_subimage(first_sub_img)


determine_exact_asparagus(my_class)
first_asparagus = my_class.list_of_asparaguses[0]
calculate_millimeter_value_from_pixel_value(PIXEL_MILLIMETER_RATIO, first_asparagus)

classify_the_asparagus(first_asparagus)

my_class.add_asparagus(first_asparagus)

print_classification_result_to_picture(my_class)
plt.imshow(my_class.picture_with_modifications)
cv2.imshow('frame',my_class.picture_with_modifications)

print 1




