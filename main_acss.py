__author__ = 'Henrik'
import numpy as np
import cv2
from matplotlib import pyplot as plt

from find_the_asparagus import find_the_asparagus

class whole_image:
    def __init__(self, original_picture, list_of_asparagus_subimages, sub_image):
        self.original_picture = original_picture
        self.list_of_asparagus_subimages = list_of_asparagus_subimages
        self.sub_image = sub_image

    def add_asparagus_subimage(self, subimage):
        self.list_of_asparagus_subimages.append(subimage)

    def calculate_sub_image(self, index):
        act_sum_img = self.list_of_asparagus_subimages[index]
        self.sub_image = self.original_picture[act_sum_img.top_left_corner_y : act_sum_img.top_left_corner_y + act_sum_img.hight,
                                               act_sum_img.top_left_corner_x : act_sum_img.top_left_corner_x + act_sum_img.width]


class asparagus_sub_image:
    def __init__(self, top_left_corner_x, top_left_corner_y, width, hight):
        self.top_left_corner_x = top_left_corner_x
        self.top_left_corner_y = top_left_corner_y
        self.width = width
        self.hight = hight




PIXEL_MILLIMETER_RATIO = 0.001


def get_max_area_contur(conturs):
    max_area_contur = conturs[0]
    max_area = cv2.contourArea(max_area_contur)


    for contur in conturs:
        area = cv2.contourArea(contur)
        if area > max_area :
            max_area = area
            max_area_contur = contur

    return max_area_contur


img = cv2.imread('images/test_img_2.jpg', 0)
img_col = cv2.imread('images/test_img_2.jpg')




first_sub_img = asparagus_sub_image(0, 0, 0, 0)
find_the_asparagus(img, first_sub_img)



my_class = whole_image(img, [], 0)

my_class.add_asparagus_subimage(first_sub_img)

my_class.calculate_sub_image(0)

a = plt.imshow(my_class.sub_image)


plt.hist(my_class.sub_image.ravel(),256,[0,256]); plt.show()




lower_white = np.array([150])
upper_white = np.array([255])


mask = cv2.inRange(my_class.sub_image, lower_white, upper_white)

kernel = np.ones((5,5),np.uint8)
dilation = cv2.dilate(mask,kernel,iterations = 1)


plt.imshow(dilation)

contours,hierarchy = cv2.findContours(dilation, 1, 2)

max_area_contur = get_max_area_contur(contours)


x,y,w,h = cv2.boundingRect(max_area_contur)
# Correction to get the right place the rectangle
x = x + my_class.list_of_asparagus_subimages[0].top_left_corner_x
y = y + my_class.list_of_asparagus_subimages[0].top_left_corner_y

# OBJECT ORIENTATED PROGRAMMING MY FRIEND!!!
cv2.rectangle(img,(x,y),(x+w,y+h),(0, 0, 125),2)

plt.imshow(img)

print 1