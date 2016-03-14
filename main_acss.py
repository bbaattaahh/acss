__author__ = 'Henrik'
import numpy as np
import cv2
from matplotlib import pyplot as plt

from asparagus import define_default_asparagus
from asparagus_sub_image import asparagus_sub_image
from whole_image import whole_image

from find_the_asparagus import find_the_asparagus

from determine_exact_asparagus import get_the_lower_limit_of_white
from determine_exact_asparagus import get_max_area_contur
from determine_exact_asparagus import determine_exact_asparagus

from calculate_millimeter_value_from_pixel_value import calculate_millimeter_value_from_pixel_value

from classify_the_asparagus import classify_the_asparagus

from print_claasification_result_to_picture import print_classification_result_to_picture

PIXEL_MILLIMETER_RATIO = 110.0/1571.0



img = cv2.imread('images/test_img_3.jpg', 0)
img_col = cv2.imread('images/test_img_3.jpg')




first_sub_img = asparagus_sub_image(0, 0, 0, 0)
find_the_asparagus(img, first_sub_img)



my_class = whole_image(img, img, [], [], 0)

my_class.add_asparagus_subimage(first_sub_img)

my_class.calculate_sub_image(0)


determine_exact_asparagus(my_class)
first_asparagus = my_class.list_of_asparaguses[0]
calculate_millimeter_value_from_pixel_value(PIXEL_MILLIMETER_RATIO, first_asparagus)

classify_the_asparagus(first_asparagus)

my_class.add_asparagus(first_asparagus)

print_classification_result_to_picture(my_class)
plt.imshow(my_class.original_picture)
cv2.imshow('frame',my_class.original_picture)

print 1