__author__ = 'Henrik'
import numpy as np
import cv2
from matplotlib import pyplot as plt

PIXEL_MILLIMETER_RATIO = 0.001

def runningMean(x, N):
    y = np.zeros((len(x),))
    for ctr in range(len(x)):
         y[ctr] = np.sum(x[ctr:(ctr+N)])
    return y/N



def sum_coloumn_value(img):
    temp = np.zeros(2560L)

    for x in range(0, 2560L):
        temp[x] = sum(img[:,x])

    return temp


def get_max_area_contur(conturs):
    max_area_contur = conturs[0]
    max_area = cv2.contourArea(max_area_contur)


    for contur in conturs:
        area = cv2.contourArea(contur)
        if area > max_area :
            max_area = area
            max_area_contur = contur

    return max_area_contur

# temp2 = runningMean(temp, 200)
#
# plt.plot(temp2)
# plt.show()
img = cv2.imread('images/test_img_1.jpg', 0)
img_col = cv2.imread('images/test_img_1.jpg')

temp = sum_coloumn_value(img)

max_white = int(temp.argmax())

my_img = img[:, (max_white-200):(max_white+100)]

#plt.imshow(my_img)

# define range of blue color in HSV
lower_white = np.array([180])
upper_white = np.array([255])


mask = cv2.inRange(my_img, lower_white, upper_white)

kernel = np.ones((5,5),np.uint8)
dilation = cv2.dilate(mask,kernel,iterations = 1)


# plt.imshow(dilation)

contours,hierarchy = cv2.findContours(dilation, 1, 2)

max_area_contur = get_max_area_contur(contours)


x,y,w,h = cv2.boundingRect(max_area_contur)
# Correction to get the right place the rectangle
x = x + (max_white-200)
# OBJECT ORIENTATED PROGRAMMING MY FRIEND!!!
cv2.rectangle(img,(x,y),(x+w,y+h),(0, 0, 125),2)

plt.imshow(img)

print 1